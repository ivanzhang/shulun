# MFAC 非循环实际去常数强制见证（Mellin 前）Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在实际 LCM Gram 模型中构造只依赖有限整数/Gram 条目的非循环去常数一维强制见证，并明确不将其外推为 Mellin 收缩或 RH。

**Architecture:** 新模块用 `fractions.Fraction` 保存精确系数、正交残差和能量，公共接口只返回 JSON 可序列化字段。依赖合同显式拒绝目标误差、Mellin 和零点输入；证书将一维方向强制性与全空间/Mellin 未闭合结论隔离。

**Tech Stack:** Python 3.12 标准库（`fractions`、`json`、`pathlib`、`unittest`），现有 MFAC 证书格式。

---

## 文件结构

- 新建 `experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit.py`：精确见证、依赖合同、聚合审计和证书写入器。
- 新建 `experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py`：固定为 6 项独立测试；后续任务把合同、证书与数值边界断言合并进这 6 项，确保 MFAC 全族达到 76/76。
- 新建 `docs/monograph/prime-matrix-mfac-noncircular-actual-offconstant-coercive-witness-audit.json` 与 `.md`：`limit=60` 证书。
- 修改 `docs/monograph/claim-status-table.md:2603` 与 `docs/monograph/external-theorem-index.md:13952`：登记正向门、公式与非目标。

### Task 1: 建立精确见证红绿测试

**Files:**
- Create: `experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit.py`
- Create: `experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py`

- [ ] **Step 1: 写入失败的见证测试**

```python
from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit import (
    actual_offconstant_coercive_witness_data,
)


class MFACNoncircularActualOffconstantCoerciveWitnessAuditTest(unittest.TestCase):
    def test_actual_witness_is_exactly_offconstant_and_positive(self) -> None:
        for limit, numerator, denominator in ((2, 1, 4), (3, 2, 3), (60, 15, 1)):
            with self.subTest(limit=limit):
                data = actual_offconstant_coercive_witness_data(limit)
                self.assertEqual(data["constant_orthogonality_exact_numerator"], 0)
                self.assertEqual(data["energy_exact_numerator"], numerator)
                self.assertEqual(data["energy_exact_denominator"], denominator)
                self.assertGreater(data["energy"], 0.0)
                self.assertGreaterEqual(data["energy"], data["coercivity_lower_bound"])

    def test_witness_uses_only_actual_lcm_gram_entries(self) -> None:
        data = actual_offconstant_coercive_witness_data(5)
        self.assertEqual(data["coefficient_source"], "K_X(1,2)/K_X(1,1)")
        self.assertEqual(data["coefficient_exact_numerator"], 2)
        self.assertEqual(data["coefficient_exact_denominator"], 5)
        self.assertTrue(data["witness_constructed_before_mellin"])
        self.assertFalse(data["uses_target_error"])
        self.assertFalse(data["uses_mellin_input"])

    def test_scalar_direction_obeys_declared_coercivity(self) -> None:
        data = actual_offconstant_coercive_witness_data(3, scalar=-3.0)
        self.assertTrue(math.isclose(data["scaled_energy"], 6.0, abs_tol=1e-12))
        self.assertTrue(math.isclose(data["scaled_coercivity_lower_bound"], 6.0, abs_tol=1e-12))

    def test_invalid_limits_and_scalars_are_rejected(self) -> None:
        for value in (True, 1, 2.0, "2"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    actual_offconstant_coercive_witness_data(value)
        for scalar in (float("inf"), float("nan"), True, "1"):
            with self.subTest(scalar=scalar):
                with self.assertRaises(ValueError):
                    actual_offconstant_coercive_witness_data(2, scalar=scalar)
```

- [ ] **Step 2: 运行测试确认红灯**

Run: `python3 experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py`

Expected: `ModuleNotFoundError`，因为审计模块尚未创建。

- [ ] **Step 3: 实现精确见证接口**

```python
from fractions import Fraction

SLUG = "prime-matrix-mfac-noncircular-actual-offconstant-coercive-witness-audit"


def actual_offconstant_coercive_witness_data(
    limit: int, scalar: int | float = 1.0
) -> dict[str, int | float | bool | str]:
    checked_limit = _require_integer_at_least_two(limit, "limit")
    checked_scalar = _require_finite_builtin_number(scalar, "scalar")
    half_limit = checked_limit // 2
    energy = Fraction(half_limit * (checked_limit - half_limit), checked_limit)
    lower_bound = Fraction(2 * checked_limit, 9)
    return {
        "limit": checked_limit,
        "coefficient_source": "K_X(1,2)/K_X(1,1)",
        "coefficient_exact_numerator": half_limit,
        "coefficient_exact_denominator": checked_limit,
        "constant_orthogonality_exact_numerator": 0,
        "energy_exact_numerator": energy.numerator,
        "energy_exact_denominator": energy.denominator,
        "energy": float(energy),
        "coercivity_lower_bound": float(lower_bound),
        "scaled_energy": float(checked_scalar * checked_scalar * float(energy)),
        "scaled_coercivity_lower_bound": float(checked_scalar * checked_scalar * float(lower_bound)),
        "witness_constructed_before_mellin": True,
        "uses_target_error": False,
        "uses_mellin_input": False,
    }
```

实现 `_require_integer_at_least_two` 和 `_require_finite_builtin_number`：仅接受内建 `int`/`float`，拒绝 `bool`、子类与非有限数。使用 `Fraction` 计算 `m_X(X-m_X)/X`，避免浮点误差影响恒等式。

- [ ] **Step 4: 运行测试确认绿灯**

Run: `python3 experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py`

Expected: 当前 4 项测试 `OK`。

- [ ] **Step 5: 提交见证实现**

```bash
git add experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit.py experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py
git commit -m "审计 MFAC 非循环去常数强制见证"
```

### Task 2: 审计输入独立性与门状态

**测试计数约束：** 将本任务的合同与聚合断言合并进 Task 1 已有的测试方法，不新增 `test_*` 方法；测试运行总数保持 6。

**Files:**
- Modify: `experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit.py`
- Modify: `experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py`

- [ ] **Step 1: 添加失败的合同和门状态测试**

```python
from prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit import (
    audit_noncircular_actual_offconstant_coercive_witness_before_mellin,
    audit_witness_dependency_contract,
)

    def test_dependency_contract_accepts_only_arithmetic_gram_inputs(self) -> None:
        allowed = audit_witness_dependency_contract({"witness_uses": ("integer_limit_X", "K_X(1,1)", "K_X(1,2)")})
        forbidden = audit_witness_dependency_contract({"witness_uses": ("K_X(1,2)", "psi(X)-X", "Mellin")})
        self.assertEqual(allowed["classification"], "noncircular_actual_gram_witness")
        self.assertTrue(allowed["actual_non_circular_witness_constructed"])
        self.assertEqual(forbidden["classification"], "forbidden_target_or_analytic_dependency")
        self.assertFalse(forbidden["actual_non_circular_witness_constructed"])

    def test_contract_rejects_malformed_dependency_inputs(self) -> None:
        for contract in (None, {"witness_uses": "K_X(1,2)"}, {"witness_uses": (1,)}):
            with self.subTest(contract=contract):
                with self.assertRaises(ValueError):
                    audit_witness_dependency_contract(contract)

    def test_aggregate_audit_opens_only_the_declared_positive_gate(self) -> None:
        payload = audit_noncircular_actual_offconstant_coercive_witness_before_mellin(60)
        self.assertTrue(payload["noncircular_actual_offconstant_coercive_witness_constructed"])
        self.assertTrue(payload["one_dimensional_coercivity_established"])
        self.assertFalse(payload["full_offconstant_spectral_gap_established"])
        self.assertFalse(payload["actual_chebyshev_mellin_contraction_present"])
        self.assertFalse(payload["rh_proved"])
        self.assertEqual(payload["next_positive_gate"], "UniformOffConstantCoercivityOrActualChebyshevMellinContractionLaw")
```

- [ ] **Step 2: 运行测试确认红灯**

Run: `python3 experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py`

Expected: `ImportError`，因为合同/聚合函数尚未定义。

- [ ] **Step 3: 实现合同和聚合接口**

```python
FORBIDDEN_WITNESS_DEPENDENCIES = frozenset(
    {"psi(X)-X", "Chebyshev_error", "Mellin", "zeta_zero", "explicit_formula"}
)


def audit_witness_dependency_contract(contract: Mapping[str, Any]) -> dict[str, Any]:
    checked_uses = _checked_string_iterable(contract, "witness_uses")
    forbidden_uses = tuple(value for value in checked_uses if value in FORBIDDEN_WITNESS_DEPENDENCIES)
    return {
        "witness_uses": checked_uses,
        "forbidden_uses": forbidden_uses,
        "classification": "forbidden_target_or_analytic_dependency" if forbidden_uses else "noncircular_actual_gram_witness",
        "actual_non_circular_witness_constructed": not forbidden_uses,
    }


def audit_noncircular_actual_offconstant_coercive_witness_before_mellin(limit: int = 60) -> dict[str, Any]:
    witness = actual_offconstant_coercive_witness_data(limit)
    dependency_contract = audit_witness_dependency_contract(
        {"witness_uses": ("integer_limit_X", "K_X(1,1)", "K_X(1,2)")}
    )
    return {
        "slug": SLUG,
        "limit": witness["limit"],
        "noncircular_actual_offconstant_coercive_witness_constructed": True,
        "one_dimensional_coercivity_established": True,
        "full_offconstant_spectral_gap_established": False,
        "actual_chebyshev_mellin_contraction_present": False,
        "rh_proved": False,
        "next_positive_gate": "UniformOffConstantCoercivityOrActualChebyshevMellinContractionLaw",
        "witness": witness,
        "dependency_contract": dependency_contract,
    }
```

`_checked_string_iterable` 先验证 `contract` 是 `Mapping`，再拒绝裸字符串、非可迭代值与非内建 `str` 元素；未知命名输入不得被误报为 Mellin 或 RH 证据。

- [ ] **Step 4: 运行测试确认绿灯**

Run: `python3 experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py`

Expected: 6 项测试 `OK`。

- [ ] **Step 5: 提交合同和门状态**

```bash
git add experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit.py experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py
git commit -m "完善 MFAC 非循环见证合同"
```

### Task 3: 生成证书并登记单子状态

**测试计数约束：** 将证书断言合并进既有测试方法，不新增 `test_*` 方法；测试运行总数保持 6。

**Files:**
- Modify: `experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit.py`
- Modify: `experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-noncircular-actual-offconstant-coercive-witness-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-noncircular-actual-offconstant-coercive-witness-audit.md`
- Modify: `docs/monograph/claim-status-table.md:2603`
- Modify: `docs/monograph/external-theorem-index.md:13952`

- [ ] **Step 1: 添加失败的证书边界测试**

```python
import json
import tempfile

from prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit import write_certificate

    def test_certificate_records_positive_gate_without_mellin_overclaim(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            paths = write_certificate(Path(temporary_directory), limit=60)
            payload = json.loads(paths["json_path"].read_text(encoding="utf-8"))
            markdown = paths["markdown_path"].read_text(encoding="utf-8")
        self.assertTrue(payload["noncircular_actual_offconstant_coercive_witness_constructed"])
        self.assertTrue(payload["one_dimensional_coercivity_established"])
        self.assertFalse(payload["actual_chebyshev_mellin_contraction_present"])
        self.assertFalse(payload["rh_proved"])
        self.assertIn("2X/9", markdown)
        self.assertIn("不是全空间谱隙", markdown)
        self.assertIn("不是 Mellin 收缩", markdown)
```

- [ ] **Step 2: 运行测试确认红灯**

Run: `python3 experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py`

Expected: `ImportError`，因为 `write_certificate` 尚未定义。

- [ ] **Step 3: 实现证书、生成产物并登记文档**

```python
def write_certificate(output_directory: Path, limit: int = 60) -> dict[str, Path]:
    payload = audit_noncircular_actual_offconstant_coercive_witness_before_mellin(limit)
    output_directory.mkdir(parents=True, exist_ok=True)
    json_path = output_directory / f"{SLUG}.json"
    markdown_path = output_directory / f"{SLUG}.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(_render_markdown(payload), encoding="utf-8")
    return {"json_path": json_path, "markdown_path": markdown_path}
```

`_render_markdown` 展示 `h_X=e_2-floor(X/2)e_1/X`、`m_X(X-m_X)/X` 与 `2X/9`，并逐条写明“不是全空间谱隙、不是 Chebyshev/Mellin 收缩、不是零点排除、不是 RH”。`main()` 写入 `docs/monograph`，随后运行：

```bash
python3 experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit.py
```

在状态表紧接前序 LCM 去常数投影循环条目后新增一行；在索引紧接 `MFAC-LCPC` 附录后新增 `MFAC-NOOCW` 附录，并明确不新增外部定理依赖。

- [ ] **Step 4: 运行测试确认绿灯**

Run: `python3 experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py`

Expected: 6 项测试 `OK`，且 JSON/Markdown 产物已更新。

- [ ] **Step 5: 提交证书与文档**

```bash
git add experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit.py experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py docs/monograph/prime-matrix-mfac-noncircular-actual-offconstant-coercive-witness-audit.json docs/monograph/prime-matrix-mfac-noncircular-actual-offconstant-coercive-witness-audit.md docs/monograph/claim-status-table.md docs/monograph/external-theorem-index.md
git commit -m "归档 MFAC 非循环去常数强制见证"
```

### Task 4: 验证 76/76 MFAC 全族与独立审查边界

**Files:**
- Verify: `experiments/prime_matrix_mfac_*_test.py`
- Verify: `experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit.py`
- Verify: `docs/monograph/prime-matrix-mfac-noncircular-actual-offconstant-coercive-witness-audit.json`

- [ ] **Step 1: 运行新增模块的定向测试**

Run: `python3 experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit_test.py`

Expected: `Ran 6 tests` 和 `OK`。

- [ ] **Step 2: 运行全族测试并核对总数**

Run:

```bash
python3 - <<'PY'
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

total = 0
for path in sorted(Path("experiments").glob("prime_matrix_mfac_*_test.py")):
    result = subprocess.run([sys.executable, str(path)], text=True, capture_output=True)
    if result.returncode:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise SystemExit(f"failed: {path}")
    match = re.search(r"Ran (\d+) tests? in ", result.stderr)
    if match is None:
        raise SystemExit(f"missing unittest count: {path}")
    total += int(match.group(1))
if total != 76:
    raise SystemExit(f"expected 76 MFAC tests, got {total}")
print(f"MFAC test suite: {total}/76 passed")
PY
```

Expected: `MFAC test suite: 76/76 passed`。

- [ ] **Step 3: 审查禁止依赖与证书边界**

Run:

```bash
rg -n 'psi\(X\)-X|Chebyshev_error|Mellin|zeta_zero|explicit_formula' experiments/prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit.py
python3 - <<'PY'
import json
from pathlib import Path

payload = json.loads(Path("docs/monograph/prime-matrix-mfac-noncircular-actual-offconstant-coercive-witness-audit.json").read_text(encoding="utf-8"))
assert payload["noncircular_actual_offconstant_coercive_witness_constructed"] is True
assert payload["one_dimensional_coercivity_established"] is True
assert payload["full_offconstant_spectral_gap_established"] is False
assert payload["actual_chebyshev_mellin_contraction_present"] is False
assert payload["rh_proved"] is False
print("certificate boundary review: passed")
PY
```

Expected: 禁止名称仅出现在显式拒绝集合/边界文字，且输出 `certificate boundary review: passed`。

- [ ] **Step 4: 复核隔离谱系与干净状态**

Run:

```bash
git merge-base --is-ancestor ed281b04 HEAD
git log --oneline ed281b04..HEAD
git status --short --branch
```

Expected: `ed281b04` 为当前分支祖先；日志仅含本功能的设计、实现和归档提交；状态没有未提交改动。

- [ ] **Step 5: 如证书重生成产生变更则提交**

```bash
git status --short
git add docs/monograph/prime-matrix-mfac-noncircular-actual-offconstant-coercive-witness-audit.json docs/monograph/prime-matrix-mfac-noncircular-actual-offconstant-coercive-witness-audit.md
git commit -m "验证 MFAC 非循环去常数强制见证"
```

仅当状态显示上述两个证书文件有预期变化时执行；若工作树已干净，不创建空提交。
