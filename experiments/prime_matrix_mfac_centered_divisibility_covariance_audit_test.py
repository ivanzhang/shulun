import json
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

from experiments.prime_matrix_mfac_centered_divisibility_covariance_audit import (
    audit_centered_divisibility_covariance,
    centered_covariance_entry,
    centered_divisibility_variance,
    covariance_quadratic_form,
    compare_dyadic_profiles,
    weighted_coercivity_profile,
    write_certificate,
)


class MFACCenteredDivisibilityCovarianceAuditTest(unittest.TestCase):
    def test_centered_covariance_entries_match_small_exact_values(self) -> None:
        self.assertEqual(centered_covariance_entry(12, 2, 2), Fraction(3, 1))
        self.assertEqual(centered_covariance_entry(12, 2, 3), Fraction(0, 1))
        self.assertEqual(centered_covariance_entry(12, 3, 3), Fraction(8, 3))

    def test_quadratic_form_equals_centered_divisibility_variance(self) -> None:
        coefficients = {2: Fraction(2, 1), 3: Fraction(-3, 1)}
        self.assertEqual(
            covariance_quadratic_form(12, coefficients),
            centered_divisibility_variance(12, coefficients),
        )

    def test_weighted_minimum_coercivity_ratio_matches_diagonal_small_case(self) -> None:
        result = weighted_coercivity_profile(limit=12, cutoff=3)
        self.assertAlmostEqual(result["minimum_ratio_estimate"], 0.5)
        self.assertLess(result["maximum_eigen_residual"], 1e-10)
        self.assertEqual(result["status"], "finite_profile_only")

    def test_dyadic_comparison_never_upgrades_finite_profiles_to_uniform_theorem(self) -> None:
        result = compare_dyadic_profiles(limit=64, theta=0.5)
        self.assertEqual(result["status"], "finite_dyadic_diagnostic_only")
        self.assertFalse(result["uniform_weighted_coercivity_proved"])
        self.assertFalse(result["actual_mellin_contraction_present"])
        self.assertFalse(result["rh_proved"])
        self.assertGreater(result["current"]["cutoff"], 1)
        self.assertGreater(result["next"]["cutoff"], 1)

    def test_certificate_records_finite_profile_without_rh_claim(self) -> None:
        certificate = audit_centered_divisibility_covariance(limit=256, theta=0.25)
        with tempfile.TemporaryDirectory() as directory:
            json_path = Path(directory) / "certificate.json"
            markdown_path = Path(directory) / "certificate.md"
            write_certificate(certificate, json_path, markdown_path)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
        self.assertEqual(payload["status"], "finite_covariance_profile_not_uniform_theorem")
        self.assertFalse(payload["uniform_weighted_coercivity_proved"])
        self.assertFalse(payload["actual_mellin_contraction_present"])
        self.assertFalse(payload["rh_proved"])


if __name__ == "__main__":
    unittest.main()
