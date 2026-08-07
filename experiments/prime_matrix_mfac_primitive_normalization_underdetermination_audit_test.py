#!/usr/bin/env python3
"""MFAC primitive 归一化不可识别性审计测试。"""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_primitive_normalization_underdetermination_audit import (  # noqa: E402
    normalization_models,
)


class MFACPrimitiveNormalizationUnderdeterminationTest(unittest.TestCase):
    """验证 global seed 只固定乘积而不固定 primitive 三元组。"""

    def test_distinct_models_preserve_same_square_base_seed(self) -> None:
        """不同 orientation/local-factor/coefficient 三元组均可产生 log(p)。"""
        models = normalization_models(5)
        triples = {(model["orientation"], model["local_factor"], model["coefficient"]) for model in models}
        self.assertGreaterEqual(len(triples), 3)
        for model in models:
            self.assertTrue(math.isclose(model["product"], math.log(5), abs_tol=1e-12))


if __name__ == "__main__":
    unittest.main()
