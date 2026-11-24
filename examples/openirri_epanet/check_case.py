#!/usr/bin/env python3
"""Generate and independently verify two OpenIrri/EPANET hydraulic cases.

No EPANET calculation is claimed unless --epanet-lib loads an actual 2.2 Toolkit.
Standard library only. Units: m, mm, m3/h, pressure head in m of water.
"""

from __future__ import annotations

import argparse
import ctypes as ct
import json
import os
from collections import defaultdict
from pathlib import Path
import tempfile

HERE = Path(__file__).resolve().parent
DIAMETERS_MM = {"55p4": 55.4, "66p0": 66.0}
Q_SPRINKLER = 0.52
N_LATERALS = 4
N_SPRINKLERS = 32
SPACING_M = 12.6
C_HW = 150.0
HW_COEFF = 10.67
HW_FLOW_EXP = 1.852
HW_DIAM_EXP = 4.87
PUMP_A = 61.0
PUMP_B = 0.0025
MIN_PRESSURE = 28.0


def filename(label: str) -> Path:
    return HERE / f"case_{label}.inp"


def render_inp(diameter_mm: float) -> str:
    lines = [
        "[TITLE]",
        f"; OpenIrri synthetic network - {diameter_mm:.1f} mm lateral bore",
        "; Independent EPANET 2.2 reproduction, fixed demands; NOT field measurements.",
        "",
        "[JUNCTIONS]",
        ";ID              Elevation(m)  Demand(m3/h)",
        "P0              0             0",
        "S0              0             0",
    ]
    for i in range(1, N_LATERALS + 1):
        lines.append(f"S{i}              0             0")
    for i in range(1, N_LATERALS + 1):
        lines.append(f"B{i}              0             0")
    for i in range(1, N_LATERALS + 1):
        for j in range(1, N_SPRINKLERS + 1):
            lines.append(f"L{i}_{j:02d}          {i+6}             {Q_SPRINKLER:.2f}")
    lines += [
        "",
        "[RESERVOIRS]",
        ";ID              Head(m)",
        "R0              0",
        "",
        "[PIPES]",
        ";ID        Node1    Node2    Length(m)   Diameter(mm)  C(HW)  MinorLoss  Status",
        "MAIN       P0       S0       270         176           150    0          Open",
    ]
    for i in range(1, N_LATERALS + 1):
        lines.append(f"SUB{i}       S{i-1}       S{i}       30          110           150    0          Open")
    for i in range(1, N_LATERALS + 1):
        lines.append(f"DER{i}       S{i}       B{i}       1           110           150    0          Open")
    for i in range(1, N_LATERALS + 1):
        for j in range(1, N_SPRINKLERS + 1):
            upstream = f"B{i}" if j == 1 else f"L{i}_{j-1:02d}"
            lines.append(
                f"LAT{i}_{j:02d}    {upstream:<8} L{i}_{j:02d}    {SPACING_M:.1f}       "
                f"{diameter_mm:.1f}          150    0          Open"
            )
    lines += [
        "",
        "[PUMPS]",
        ";ID        Node1   Node2   Parameter",
        "PUMP1      R0      P0      HEAD PUMPQH",
        "",
        "[CURVES]",
        ";PUMP: exactly H = 61 - 0.0025 Q^2 (Q in m3/h, H in m).",
        ";Three-point curve: EPANET fits H=A-B*Q^C (C=2 here).",
        "PUMPQH  0     61",
        "PUMPQH  40    57",
        "PUMPQH  100   36",
        "",
        "[OPTIONS]",
        "UNITS              CMH",
        "HEADLOSS           H-W",
        "DEMAND MODEL       DDA",
        "SPECIFIC GRAVITY   1.0",
        "ACCURACY           0.000001",
        "UNBALANCED         STOP",
        "",
        "[TIMES]",
        "DURATION           0:00",
        "",
        "[REPORT]",
        "STATUS             YES",
        "NODES              ALL",
        "LINKS              ALL",
        "",
        "[COORDINATES]",
        "R0       -20       0",
        "P0       0         0",
        "S0       270       0",
    ]
    for i in range(1, N_LATERALS + 1):
        x = 270 + i * 30
        lines.append(f"S{i}       {x}       0")
        lines.append(f"B{i}       {x}       1")
        for j in range(1, N_SPRINKLERS + 1):
            lines.append(f"L{i}_{j:02d}    {x}       {1 + SPACING_M*j:.1f}")
    lines += ["", "[END]", ""]
    return "\n".join(lines)


def parse_inp(path: Path) -> dict:
    sections: dict[str, list[list[str]]] = defaultdict(list)
    section = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        raw = raw.split(";", 1)[0].strip()
        if not raw:
            continue
        if raw.startswith("[") and raw.endswith("]"):
            section = raw[1:-1].upper()
        elif section is not None:
            sections[section].append(raw.split())
    junctions = {r[0]: (float(r[1]), float(r[2])) for r in sections["JUNCTIONS"]}
    reservoirs = {r[0]: float(r[1]) for r in sections["RESERVOIRS"]}
    pipes = {
        r[0]: (r[1], r[2], float(r[3]), float(r[4]), float(r[5]), float(r[6]))
        for r in sections["PIPES"]
    }
    curves = [(r[0], float(r[1]), float(r[2])) for r in sections["CURVES"]]
    options = {r[0]: r[1:] for r in sections["OPTIONS"]}
    return {"junctions": junctions, "reservoirs": reservoirs, "pipes": pipes,
            "pumps": sections["PUMPS"], "curves": curves, "options": options}


def validate(case: dict, diameter_mm: float) -> None:
    nodes = case["junctions"]
    pipes = case["pipes"]
    assert len(nodes) == 10 + 4 * 32, "Expected 138 junctions"
    assert len(pipes) == 1 + 4 + 4 + 4 * 32, "Expected 137 pipes"
    assert case["reservoirs"] == {"R0": 0.0}
    assert case["pumps"] == [["PUMP1", "R0", "P0", "HEAD", "PUMPQH"]]
    assert case["curves"] == [("PUMPQH", 0.0, 61.0),
                               ("PUMPQH", 40.0, 57.0),
                               ("PUMPQH", 100.0, 36.0)]
    for _, q, h in case["curves"]:
        assert abs(h - (PUMP_A - PUMP_B * q * q)) < 1e-12
    assert case["options"].get("UNITS") == ["CMH"]
    assert case["options"].get("HEADLOSS") == ["H-W"]
    assert case["options"].get("DEMAND") == ["MODEL", "DDA"]
    assert pipes["MAIN"] == ("P0", "S0", 270.0, 176.0, 150.0, 0.0)
    for i in range(1, 5):
        assert pipes[f"SUB{i}"] == (f"S{i-1}", f"S{i}", 30.0, 110.0, 150.0, 0.0)
        assert pipes[f"DER{i}"] == (f"S{i}", f"B{i}", 1.0, 110.0, 150.0, 0.0)
        for j in range(1, 33):
            start = f"B{i}" if j == 1 else f"L{i}_{j-1:02d}"
            node = f"L{i}_{j:02d}"
            assert nodes[node] == (float(i + 6), Q_SPRINKLER)
            assert pipes[f"LAT{i}_{j:02d}"] == (start, node, SPACING_M,
                                                  diameter_mm, C_HW, 0.0)
    assert abs(sum(demand for elevation, demand in nodes.values()) - 66.56) < 1e-9


def headloss(length_m: float, diameter_mm: float, hw_c: float, q_m3h: float) -> float:
    """Independent textbook Hazen-Williams SI formula (not the EPANET engine)."""
    q_m3s = abs(q_m3h) / 3600.0
    return HW_COEFF * length_m * q_m3s ** HW_FLOW_EXP / (
        hw_c ** HW_FLOW_EXP * (diameter_mm / 1000) ** HW_DIAM_EXP
    )


def calculate(case: dict) -> dict:
    """Tree traversal; no preassigned pipe flows or pressures."""
    junctions = case["junctions"]
    pipes = case["pipes"]
    children: dict[str, list[tuple[str, str]]] = defaultdict(list)
    parents: dict[str, str] = {}
    for name, (up, down, *_rest) in pipes.items():
        assert down not in parents, f"Multiple incoming pipes to {down}"
        parents[down] = name
        children[up].append((name, down))
    assert set(parents) == set(junctions) - {"P0"}

    flows: dict[str, float] = {}

    def traverse(node: str) -> float:
        q = junctions[node][1]
        for name, down in children[node]:
            f = traverse(down)
            flows[name] = f
            q += f
        return q

    q_total = traverse("P0")
    assert abs(q_total - 66.56) < 1e-8
    losses = {
        name: headloss(length, diam, c, flows[name])
        for name, (_, _, length, diam, c, _) in pipes.items()
    }
    pump_h = PUMP_A - PUMP_B * q_total ** 2
    heads = {"P0": pump_h}

    def propagate(node: str) -> None:
        for name, down in children[node]:
            heads[down] = heads[node] - losses[name]
            propagate(down)

    propagate("P0")
    pressure = {node: heads[node] - z for node, (z, _) in junctions.items()
                if node.startswith("L")}
    worst = min(pressure, key=pressure.get)
    m = HW_FLOW_EXP
    christiansen_f = sum(j**m for j in range(1, 33)) / (32**(m+1))
    lateral_f = headloss(SPACING_M*32, next(v[3] for k, v in pipes.items()
                                       if k == "LAT1_01"), C_HW, Q_SPRINKLER*32) * christiansen_f
    assert abs(lateral_f - sum(losses[f"LAT4_{j:02d}"] for j in range(1, 33))) < 1e-10
    assert worst == "L4_32"
    assert abs(sum(flows[f"SUB{i}"] for i in [4]) - 16.64) < 1e-8
    return {
        "method": "analytical_Hazen_Williams_not_EPANET",
        "flow_m3h": round(q_total, 8),
        "pump_head_m": round(pump_h, 8),
        "main_loss_m": round(losses["MAIN"], 8),
        "submain_loss_m": round(sum(losses[f"SUB{i}"] for i in range(1, 5)), 8),
        "submain_segments_m": [round(losses[f"SUB{i}"], 8) for i in range(1, 5)],
        "branch_loss_m": round(losses["DER4"], 8),
        "lateral_loss_m": round(sum(losses[f"LAT4_{j:02d}"] for j in range(1, 33)), 8),
        "christiansen_F": round(christiansen_f, 10),
        "christiansen_lateral_loss_m": round(lateral_f, 8),
        "minimum_pressure_node": worst,
        "minimum_pressure_m": round(pressure[worst], 8),
        "minimum_required_m": MIN_PRESSURE,
        "pressure_margin_m": round(pressure[worst] - MIN_PRESSURE, 8),
    }


def run_epanet(lib_path: Path, inp: Path) -> dict:
    """Execute the actual OWA EPANET 2.2 C Toolkit through ctypes."""
    lib = (ct.WinDLL if os.name == "nt" else ct.CDLL)(str(lib_path.resolve()))
    p = ct.c_void_p()
    lib.EN_createproject.argtypes = [ct.POINTER(ct.c_void_p)]
    lib.EN_open.argtypes = [ct.c_void_p, ct.c_char_p, ct.c_char_p, ct.c_char_p]
    lib.EN_openH.argtypes = [ct.c_void_p]
    lib.EN_initH.argtypes = [ct.c_void_p, ct.c_int]
    lib.EN_runH.argtypes = [ct.c_void_p, ct.POINTER(ct.c_long)]
    lib.EN_closeH.argtypes = [ct.c_void_p]
    lib.EN_close.argtypes = [ct.c_void_p]
    lib.EN_deleteproject.argtypes = [ct.c_void_p]
    lib.EN_getversion.argtypes = [ct.POINTER(ct.c_int)]
    lib.EN_getnodeindex.argtypes = [ct.c_void_p, ct.c_char_p, ct.POINTER(ct.c_int)]
    lib.EN_getnodevalue.argtypes = [ct.c_void_p, ct.c_int, ct.c_int, ct.POINTER(ct.c_double)]
    lib.EN_getlinkindex.argtypes = [ct.c_void_p, ct.c_char_p, ct.POINTER(ct.c_int)]
    lib.EN_getlinkvalue.argtypes = [ct.c_void_p, ct.c_int, ct.c_int, ct.POINTER(ct.c_double)]
    for name in ("EN_createproject", "EN_open", "EN_openH", "EN_initH", "EN_runH",
                 "EN_closeH", "EN_close", "EN_deleteproject", "EN_getversion",
                 "EN_getnodeindex", "EN_getnodevalue", "EN_getlinkindex", "EN_getlinkvalue"):
        getattr(lib, name).restype = ct.c_int

    def check(code: int, call: str) -> None:
        if code:
            raise RuntimeError(f"EPANET Toolkit {call}: code {code} (not a verified result)")

    check(lib.EN_createproject(ct.byref(p)), "EN_createproject")
    opened = False
    hydraulics_open = False
    try:
        version = ct.c_int()
        check(lib.EN_getversion(ct.byref(version)), "EN_getversion")
        if version.value < 20200 or version.value >= 20300:
            raise RuntimeError(f"Toolkit version {version.value} is not EPANET 2.2")
        with tempfile.TemporaryDirectory(prefix="openirri_epanet_") as temp:
            rpt = Path(temp) / "solver.rpt"
            out = Path(temp) / "solver.bin"
            check(lib.EN_open(p, str(inp.resolve()).encode(), str(rpt).encode(),
                              str(out).encode()), "EN_open")
            opened = True
            check(lib.EN_openH(p), "EN_openH")
            hydraulics_open = True
            check(lib.EN_initH(p, 0), "EN_initH")
            t = ct.c_long()
            check(lib.EN_runH(p, ct.byref(t)), "EN_runH")
            assert t.value == 0

            def node_val(name: str, code: int) -> float:
                idx = ct.c_int()
                val = ct.c_double()
                check(lib.EN_getnodeindex(p, name.encode(), ct.byref(idx)), "EN_getnodeindex")
                check(lib.EN_getnodevalue(p, idx.value, code, ct.byref(val)), "EN_getnodevalue")
                return val.value

            def flow(name: str) -> float:
                idx = ct.c_int()
                val = ct.c_double()
                check(lib.EN_getlinkindex(p, name.encode(), ct.byref(idx)), "EN_getlinkindex")
                check(lib.EN_getlinkvalue(p, idx.value, 8, ct.byref(val)), "EN_getlinkvalue")
                return val.value

            h = lambda n: node_val(n, 10)  # EN_HEAD
            pmin = min(((f"L{i}_{j:02d}", node_val(f"L{i}_{j:02d}", 11))
                        for i in range(1, 5) for j in range(1, 33)), key=lambda x: x[1])
            result = {
                "method": "executed_EPANET_2_2_toolkit",
                "epanet_version_code": version.value,
                "hydraulic_time_s": t.value,
                "flow_m3h": round(flow("PUMP1"), 8),
                "pump_head_m": round(h("P0") - h("R0"), 8),
                "main_loss_m": round(h("P0") - h("S0"), 8),
                "submain_loss_m": round(h("S0") - h("S4"), 8),
                "submain_segments_m": [round(h(f"S{i-1}") - h(f"S{i}"), 8) for i in range(1, 5)],
                "branch_loss_m": round(h("S4") - h("B4"), 8),
                "lateral_loss_m": round(h("B4") - h("L4_32"), 8),
                "minimum_pressure_node": pmin[0],
                "minimum_pressure_m": round(pmin[1], 8),
            }
            return result
    finally:
        if hydraulics_open:
            lib.EN_closeH(p)
        if opened:
            lib.EN_close(p)
        lib.EN_deleteproject(p)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate .inp and analytical reference JSON")
    parser.add_argument("--epanet-lib", type=Path, help="Path to actual EPANET 2.2 shared library")
    parser.add_argument("--solver-output", type=Path, help="Optional JSON output; written only after solver success")
    args = parser.parse_args()
    if args.solver_output and not args.epanet_lib:
        parser.error("--solver-output requires --epanet-lib")
    expected: dict[str, dict] = {}
    actual_solver: dict[str, dict] = {}
    for label, diameter_mm in DIAMETERS_MM.items():
        path = filename(label)
        rendered = render_inp(diameter_mm)
        if args.write:
            path.write_text(rendered, encoding="utf-8")
        else:
            assert path.read_text(encoding="utf-8") == rendered, f"Non-reproducible input: {path}"
        case = parse_inp(path)
        validate(case, diameter_mm)
        result = calculate(case)
        expected[label] = result
        print(f"ANALYTICAL {label}: {json.dumps(result, sort_keys=True)}")
        if args.epanet_lib:
            actual = run_epanet(args.epanet_lib, path)
            actual_solver[label] = actual
            for key in ("flow_m3h", "pump_head_m", "main_loss_m", "submain_loss_m",
                        "branch_loss_m", "lateral_loss_m", "minimum_pressure_m"):
                diff = actual[key] - result[key]
                print(f"EPANET 2.2 {label} {key}: {actual[key]:.8f}; delta={diff:+.8f}")
                tolerance = 1e-4 if key == "flow_m3h" else 0.10
                assert abs(diff) <= tolerance, f"Unexpected discrepancy for {label}: {key}"
            assert actual["minimum_pressure_node"] == result["minimum_pressure_node"]
    reference_path = HERE / "expected_analytic.json"
    doc = json.dumps({"provenance": "analytic_only; no EPANET solver implied", "cases": expected},
                     indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    if args.write:
        reference_path.write_text(doc, encoding="utf-8")
    else:
        saved = json.loads(reference_path.read_text(encoding="utf-8"))
        proposed = json.loads(doc)
        assert saved["provenance"] == proposed["provenance"], "Analytical provenance changed"
        for label in proposed["cases"]:
            old = saved["cases"][label]
            new = proposed["cases"][label]
            assert old.keys() == new.keys(), f"Analytical fields changed in {label}"
            for field in old:
                if isinstance(old[field], (int, float)) and not isinstance(old[field], bool):
                    assert abs(old[field] - new[field]) < 1e-7, (
                        f"Analytical reference drift in {label}/{field}: {old[field]} vs {new[field]}"
                    )
                elif isinstance(old[field], list):
                    assert len(old[field]) == len(new[field])
                    for a, b in zip(old[field], new[field]):
                        assert abs(a - b) < 1e-7
                else:
                    assert old[field] == new[field], f"Analytical reference drift in {label}/{field}"
    if args.solver_output:
        args.solver_output.write_text(json.dumps({"cases": actual_solver}, indent=2,
                                               sort_keys=True) + "\n", encoding="utf-8")
    if not args.epanet_lib:
        print("SOLVER STATUS: NOT EXECUTED (supply --epanet-lib to run actual EPANET 2.2).")
    else:
        print("SOLVER STATUS: EXECUTED, version checked, hydraulic deltas shown above.")


if __name__ == "__main__":
    main()
