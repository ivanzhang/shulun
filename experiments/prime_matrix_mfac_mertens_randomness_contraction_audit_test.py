import json
import tempfile
import unittest
from pathlib import Path

from experiments.prime_matrix_mfac_mertens_randomness_contraction_audit import (
    audit_mertens_randomness,
    classify_contraction_contract,
    complete_synthetic_contraction_contract,
    diagnose_layer_shuffle,
    independent_sign_baseline,
    layer_shuffle_baseline,
    mobius_and_omega_sieve,
    summarize_block,
    summarize_samples,
    write_certificate,
)


class MFACMertensRandomnessContractionAuditTest(unittest.TestCase):
    def test_mobius_sieve_and_omega_match_small_known_values(self) -> None:
        mobius, omega = mobius_and_omega_sieve(10)
        self.assertEqual(mobius[1:11], [1, -1, -1, 0, -1, 1, -1, 0, 0, 1])
        self.assertEqual(omega[1:11], [0, 1, 1, 1, 1, 2, 1, 1, 1, 2])

    def test_layered_block_deltas_reconstruct_actual_mertens_delta(self) -> None:
        mobius, omega = mobius_and_omega_sieve(48)
        block = summarize_block(mobius, omega, start=12, length=24)
        self.assertEqual(block.delta_mertens, sum(block.layer_deltas.values()))
        self.assertEqual(block.delta_mertens, sum(mobius[13:37]))

    def test_degenerate_samples_do_not_construct_standardized_moments(self) -> None:
        summary = summarize_samples([0, 0, 0])
        self.assertTrue(summary["degenerate_variance"])
        self.assertIsNone(summary["standardized_skewness"])
        self.assertIsNone(summary["excess_kurtosis"])

    def test_sample_summary_reports_signs_moments_and_tail_counts(self) -> None:
        summary = summarize_samples([-2, -1, 1, 2])
        self.assertEqual(summary["sample_count"], 4)
        self.assertEqual(summary["zero_count"], 0)
        self.assertEqual(summary["sign_bias"], 0.0)
        self.assertAlmostEqual(summary["mean"], 0.0)
        self.assertFalse(summary["degenerate_variance"])

    def test_seeded_independent_sign_baseline_is_reproducible(self) -> None:
        values = [1, -1, 1, -1, 0, 1]
        self.assertEqual(
            independent_sign_baseline(values, seed=17),
            independent_sign_baseline(values, seed=17),
        )

    def test_layer_shuffle_preserves_each_layer_multiset(self) -> None:
        layers = {1: [1, -1, 1], 2: [-1, 1]}
        shuffled = layer_shuffle_baseline(layers, seed=9)
        self.assertEqual(
            {key: sorted(value) for key, value in shuffled.items()},
            {key: sorted(value) for key, value in layers.items()},
        )

    def test_proxy_baselines_are_labeled_empirical_only(self) -> None:
        from experiments.prime_matrix_mfac_mertens_randomness_contraction_audit import build_proxy_baselines

        result = build_proxy_baselines([1, -1, 0, 1], {1: [1, -1], 2: [1]}, seed=3)
        self.assertEqual(result["status"], "empirical_proxy_baselines_only")
        self.assertFalse(result["actual_mellin_contraction_present"])

    def test_squarefree_omega_layers_are_marked_as_sign_deterministic(self) -> None:
        result = diagnose_layer_shuffle({1: [-1, -1], 2: [1, 1]})
        self.assertTrue(result["sign_deterministic_by_layer"])
        self.assertEqual(result["comparison_status"], "degenerate_not_independent_baseline")

    def test_missing_contract_fields_keep_empirical_audit_outside_mellin_closure(self) -> None:
        result = classify_contraction_contract({"fixed_actual_integer_embedding": True})
        self.assertEqual(result["status"], "empirical_randomness_model_not_a_rh_proof")
        self.assertIn("uniform_signed_block_covariance_bound", result["missing_contract_fields"])
        self.assertFalse(result["actual_mellin_contraction_present"])
        self.assertFalse(result["rh_proved"])

    def test_complete_synthetic_contract_still_is_not_an_actual_rh_proof(self) -> None:
        result = classify_contraction_contract(complete_synthetic_contraction_contract())
        self.assertEqual(result["status"], "synthetic_contract_not_actual_proof")
        self.assertFalse(result["rh_proved"])

    def test_writer_keeps_empirical_evidence_distinct_from_rh_proof(self) -> None:
        certificate = audit_mertens_randomness(limit=2048, block_length=32, seed=7)
        with tempfile.TemporaryDirectory() as directory:
            json_path = Path(directory) / "certificate.json"
            markdown_path = Path(directory) / "certificate.md"
            write_certificate(certificate, json_path, markdown_path)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            markdown = markdown_path.read_text(encoding="utf-8")
        self.assertTrue(payload["layer_reconstruction_holds"])
        self.assertEqual(payload["status"], "empirical_randomness_model_not_a_rh_proof")
        self.assertFalse(payload["actual_mellin_contraction_present"])
        self.assertIn("不构成 RH 证明", markdown)


if __name__ == "__main__":
    unittest.main()
