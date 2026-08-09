import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

from experiments.prime_matrix_mfac_uniform_offconstant_coercivity_audit import (
    audit_finite_family,
    audit_candidate_contract,
    e2_offconstant_candidate,
)


class MFACUniformOffconstantCoercivityAuditTest(unittest.TestCase):
    def test_candidate_contract_rejects_target_error_dependency(self) -> None:
        result = audit_candidate_contract({"uses": ["psi(X)-X"]})
        self.assertEqual(result["status"], "forbidden_target_dependency")

    def test_e2_candidate_is_exactly_orthogonal_to_constant_direction(self) -> None:
        candidate = e2_offconstant_candidate(12)
        self.assertEqual(candidate.constant_inner_product, Fraction(0, 1))
        self.assertEqual(candidate.coefficient, Fraction(1, 2))

    def test_finite_scan_never_claims_uniform_coercivity(self) -> None:
        certificate = audit_finite_family(limits=[12, 18], indices=[2, 3])
        self.assertEqual(certificate["status"], "finite_coercivity_scan_not_uniform_theorem")
        self.assertFalse(certificate["uniform_coercivity_proved"])
        self.assertFalse(certificate["actual_mellin_contraction_present"])
        self.assertFalse(certificate["rh_proved"])
        self.assertAlmostEqual(certificate["scans"][0]["minimum_eigenvalue_estimate"], 8 / 3)

    def test_cli_writes_finite_scan_certificates(self) -> None:
        module_path = Path(__file__).with_name("prime_matrix_mfac_uniform_offconstant_coercivity_audit.py")
        with tempfile.TemporaryDirectory() as directory:
            json_path = Path(directory) / "certificate.json"
            markdown_path = Path(directory) / "certificate.md"
            subprocess.run(
                [
                    sys.executable,
                    str(module_path),
                    "--json-out",
                    str(json_path),
                    "--markdown-out",
                    str(markdown_path),
                ],
                check=True,
            )
            self.assertTrue(json_path.exists())
            self.assertIn("uniform_coercivity_proved=false", markdown_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
