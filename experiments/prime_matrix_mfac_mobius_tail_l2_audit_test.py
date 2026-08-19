from fractions import Fraction
import unittest

from experiments.prime_matrix_mfac_mobius_tail_l2_audit import (
    euler_phi_square_energy,
    limit_kernel_energy,
)


class MFACMobiusTailL2AuditTest(unittest.TestCase):
    """验证 Möbius 尾和 L² 门槛的有限代数恒等式。"""

    def test_euler_phi_square_sum_matches_limit_kernel_for_rational_coefficients(self) -> None:
        """Euler--phi 平方和必须精确等于极限核二次型。"""
        coefficients = {
            2: Fraction(3, 2),
            3: Fraction(-2, 3),
            6: Fraction(5, 7),
        }
        self.assertEqual(
            limit_kernel_energy(coefficients),
            euler_phi_square_energy(coefficients),
        )
