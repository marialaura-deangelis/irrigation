# SPDX-License-Identifier: MIT
"""Independent, dependency-free regression tests for the committed teaching case."""
from __future__ import annotations

import json
import math
import sys
import unittest
from pathlib import Path

CASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CASE_DIR))
import check_case as case  # noqa: E402


class TeachingCaseTests(unittest.TestCase):
    def test_input_snapshots_reproduce_exactly(self):
        for label, diameter in case.DIAMETERS_MM.items():
            with self.subTest(label=label):
                self.assertEqual(case.filename(label).read_text(encoding="utf-8"),
                                 case.render_inp(diameter))

    def test_topology_and_nodal_demands(self):
        for label, diameter in case.DIAMETERS_MM.items():
            with self.subTest(label=label):
                model = case.parse_inp(case.filename(label))
                case.validate(model, diameter)
                self.assertEqual(len(model["junctions"]), 138)
                self.assertEqual(len(model["pipes"]), 137)
                self.assertEqual(len(model["pumps"]), 1)
                outlets = [name for name in model["junctions"] if name.startswith("L")]
                self.assertEqual(len(outlets), 128)
                self.assertTrue(math.isclose(
                    sum(model["junctions"][name][1] for name in outlets), 66.56,
                    abs_tol=1e-10))

    def test_analytical_reference_does_not_drift(self):
        saved = json.loads((CASE_DIR / "expected_analytic.json").read_text(encoding="utf-8"))
        self.assertEqual(saved["provenance"], "analytic_only; no EPANET solver implied")
        for label, diameter in case.DIAMETERS_MM.items():
            with self.subTest(label=label):
                model = case.parse_inp(case.filename(label))
                result = case.calculate(model)
                self.assertEqual(saved["cases"][label], result)
                self.assertEqual(result["minimum_pressure_node"], "L4_32")
                self.assertGreater(result["minimum_pressure_m"], 28.0)

    def test_christiansen_factor_is_exact_discrete_sum(self):
        n = case.N_SPRINKLERS
        exponent = case.HW_FLOW_EXP
        exact = sum(j ** exponent for j in range(1, n + 1)) / n ** (exponent + 1)
        for label in case.DIAMETERS_MM:
            result = case.calculate(case.parse_inp(case.filename(label)))
            self.assertAlmostEqual(result["christiansen_F"], exact, places=9)
            self.assertAlmostEqual(result["christiansen_lateral_loss_m"],
                                   result["lateral_loss_m"], places=7)

    def test_hydraulic_sensitivity_to_lateral_diameter(self):
        small = case.calculate(case.parse_inp(case.filename("55p4")))
        large = case.calculate(case.parse_inp(case.filename("66p0")))
        self.assertEqual(small["flow_m3h"], large["flow_m3h"])
        self.assertEqual(small["pump_head_m"], large["pump_head_m"])
        self.assertGreater(small["lateral_loss_m"], large["lateral_loss_m"])
        self.assertLess(small["minimum_pressure_m"], large["minimum_pressure_m"])

    def test_additional_derivation_loss_is_reported(self):
        for label in case.DIAMETERS_MM:
            result = case.calculate(case.parse_inp(case.filename(label)))
            self.assertGreater(result["branch_loss_m"], 0)
            self.assertLess(result["branch_loss_m"], 0.003)
            self.assertAlmostEqual(
                result["pump_head_m"] - result["main_loss_m"]
                - result["submain_loss_m"] - result["branch_loss_m"]
                - result["lateral_loss_m"] - 10.0,
                result["minimum_pressure_m"], places=6)


if __name__ == "__main__":
    unittest.main()
