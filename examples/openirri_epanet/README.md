# OpenIrri–EPANET 2.2: reproducible *hydraulic* exercise

## Scope and provenance

These files describe **one synthetic, steady-state, demand-driven sprinkler
network** with two possible internal lateral diameters. They do **not** contain
field observations, measured sprinkler discharge laws, precipitation catch-can
data, or an application-uniformity model. Neither the OpenIrri package nor
EPANET is claimed to have produced the analytical numbers committed here.
An EPANET result exists **only after** the optional Toolkit execution is run.

The upstream project record is
[`examples/README.md`](../README.md). The original analytical values in that
record remain unchanged. The independently recomputed reference in
[`expected_analytic.json`](expected_analytic.json) is explicitly labeled
`analytic_only`.

## Reproducible inputs

| Component | Network representation | Assumption / unit |
| --- | --- | --- |
| Supply | Reservoir `R0` at total head 0 m -> pump `PUMP1` -> junction `P0` | Reference datum; suction-side losses omitted |
| Pump | Three-point `PUMPQH` (Q m³/h, head m): (0, 61), (40, 57), (100, 36) | Exact quadratic `H=61-0.0025 Q²` in the EPANET three-point pump-curve convention; *synthetic*, not a manufacturer curve |
| Main | `MAIN`, `P0 -> S0`, 270 m, inside Ø 176 mm | C(Hazen–Williams)=150 |
| Submain | `SUB1` to `SUB4`, `S0 -> S1 -> S2 -> S3 -> S4` | Four **separate** 30 m pipes, inside Ø 110 mm |
| Branch connections | `DER1` to `DER4`, `S_i -> B_i` | **Added** for explicit derivation: each 1 m of inside Ø 110 mm; four small head losses not present in the source table |
| Laterals | `LATi_01` to `LATi_32`, from `B_i` to `Li_32` | 32 successive 12.6 m segments, total 403.2 m per lateral; Ø 55.4 or 66.0 mm |
| Sprinklers | 128 separate demand junctions `Li_j` | 0.52 m³/h each, all open, fixed demand (`DDA`), total 66.56 m³/h |
| Elevations | `Li_j` 7, 8, 9, 10 m on laterals 1 to 4 | Other junctions 0 m; elevation change is applied as a node head/pressure datum, without a separately modeled riser |
| Losses | `H-W`, C=150, all minor-loss coefficients zero | No valves, filters, fitting losses, emitters or leakage |
| Analysis | `UNITS CMH`, `DEMAND MODEL DDA`, `DURATION 0:00` | Steady state; no pressure-dependent discharge or transient effects |

Each case has **138 junctions + 1 reservoir; 137 pipes + 1 pump**. There is no
nonzero demand at the tees or header junctions. S1 to S4 are connected to
branch heads B1 to B4, respectively. The specified 403.2 m lateral length
includes the **first 12.6 m pipe** before the first sprinkler; no emitter sits
at B_i. The additional 1 m branches precede, rather than replace, the 403.2 m.
Coordinate geometry is illustrative and must not be read as surveyed layout.

### Analytical reference (not solver output)

`check_case.py` parses the `.inp` text, traverses the pipe tree to determine
all individual link flows from downstream nodal demands, and calculates losses
using the explicitly stated textbook SI form

`h_f = 10.67 L (Q_m3/s)^1.852 / (C^1.852 D_m^4.87)`.

The exact finite-32-outlet Christiansen factor (for equal pipe lengths and
equal outlet discharges) is `F = sum(j^1.852 for j=1..32)/32^(1+1.852)`.
It is **not** a pluviometric uniformity coefficient. `F = 0.3664065837`.
The formula and the sum of 32 different pipe-flow losses agree by construction,
within machine precision.

| Analytical value | Ø 55.4 mm | Ø 66.0 mm |
| --- | ---: | ---: |
| Total demand (m³/h) | 66.560000 | 66.560000 |
| Pump head at this demand (m) | 49.924416 | 49.924416 |
| Main head loss (m) | 0.783573 | 0.783573 |
| Submain segments 1 to 4 (m) | 0.858818 / 0.504098 / 0.237900 / 0.065900 | same |
| Total submain head loss (m) | 1.666715 | 1.666715 |
| Last branch `DER4` head loss (m) | 0.002197 | 0.002197 |
| Lateral 4 head loss (m) | 9.160905 | 3.905278 |
| Minimum computed pressure head (at `L4_32`) (m) | 28.311027 | 33.566654 |
| Margin over 28 m threshold (m) | 0.311027 | 5.566654 |

The upstream worksheet gives 28.313 and 33.569 m **without** the branch pipes;
the ~0.002 m lower heads here result from the explicitly added 1 m derivation
(`DER4`). Other small solver-versus-analytical differences may arise from the
**internal** Hazen–Williams constants, numerical convergence and rounding.
Solver differences must be measured, not assumed to be zero.

## How to reproduce

Python 3.9 or newer; **no third-party Python packages required**.
From the repository root:

```sh
python3 examples/openirri_epanet/check_case.py
```

This checks both committed `.inp` snapshots against their deterministic
renderings, verifies topology/pipe data/mass balance, recomputes analytical
heads independently from demands, and verifies `expected_analytic.json`.
It prints `SOLVER STATUS: NOT EXECUTED` unless a solver is explicitly supplied.
To regenerate the snapshots, run:

```sh
python3 examples/openirri_epanet/check_case.py --write
```

To perform a **genuine EPANET 2.2 Toolkit hydraulic run**, first install or
build the official EPANET 2.2 engine and provide its actual shared library
(`libepanet2.so` on Linux, `.dylib` on macOS or `epanet2.dll` on Windows,
using a matching Python architecture):

```sh
python3 examples/openirri_epanet/check_case.py \
  --epanet-lib /absolute/path/to/libepanet2.so \
  --solver-output /tmp/openirri_solver_2_2.json
```

On Windows, use a suitably escaped absolute path to the `.dll`. The script
checks the Toolkit version code belongs to 2.2, calls its hydraulic solver,
reads actual nodal heads, pressure and link flow through its C API, prints
**signed numerical deltas** against the separate analytical calculation,
checks the minimum-pressure node and requires differences no greater than
0.10 m for heads/losses and 0.0001 m³/h for the overall flow. A solver JSON
file is written **only after both actual solver runs complete successfully**.
For other EPANET implementations, versions, or different solver settings,
document them explicitly rather than reporting them as EPANET 2.2 results.

An alternative graphical check is to open each `.inp` in EPANET 2.2, run a
hydraulic analysis, inspect `PUMP1`, `MAIN`, `SUB1`–`SUB4`, `DER4`, and
`L4_32`, and record solver version and displayed precision. An exported EPANET
report is a solver result only if the actual solver has been run.

## Interpretation and limits

A passed hydraulic model supports comparison of **pipe losses, flow balance,
pressure at nodes, and pump operating head** under the given fixed-demand
assumptions. It does **not** validate sprinkler throw, spatial application,
Christiansen **CU** (uniformity of precipitation), DU, irrigation efficiency,
or pressure-dependent discharge. Those require a separate nozzle-law and
catch-can / spatial overlap experiment with explicit geometry and, where
appropriate, measured discharge-versus-pressure curves. Do not use the
Hazen–Williams Christiansen *F* factor as a precipitation-uniformity result.

Reference: [EPA EPANET 2.2 User Manual](https://usepa.github.io/EPANET2.2/),
particularly input file formats, pump curves, flow units and DDA options.
