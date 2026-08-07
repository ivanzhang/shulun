# MFAC LCM 去常数投影循环审计 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在实际 LCM Gram 核中审计直接 `e_1` 去常数投影的唯一目标依赖系数，并将其与真正未闭合的非循环强制能量门严格分开。

**Architecture:** 新模块复用上一轮的有限实际整数 `mobius`、`von_mangoldt` 与 `lcm_gram_entry`，但独立形成 `g=w-e_1` 的 LCM 内积读数。对任意 `alpha`，审计器同时给出实际投影缺陷和由 `psi(X)-X-alpha*X` 得到的理论缺陷；合同分类器只拒绝读取目标/解析输入的直接投影，其他“独立性”声明保持未证实而不作数学不存在性结论。

**Tech Stack:** Python 3 标准库（`argparse`、`json`、`math`、`pathlib`、`unittest`）；现有 MFAC 审计与证书约定。

---

## 文件结构

- 创建 `experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit.py`：实际投影读数、合同分类、JSON/Markdown 证书和 CLI。
- 创建 `experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test.py`：LCM 投影恒等式、唯一性、循环分类和证书边界。
- 创建 `docs/monograph/prime-matrix-mfac-lcm-offconstant-projection-circularity-audit.json`：默认 `limit=60` 的机器证书。
- 创建 `docs/monograph/prime-matrix-mfac-lcm-offconstant-projection-circularity-audit.md`：人类可读的直接投影循环证书。
- 修改 `docs/monograph/claim-status-table.md` 与 `docs/monograph/external-theorem-index.md`：登记内部有限审计及其非 RH 边界。

### Task 1: 写入直接投影循环的红灯合同测试

**Files:**
- Create: `experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test.py`
- Reference: `experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit_test.py`

- [ ] **Step 1: 写入 LCM 投影恒等式与唯一性测试**

```python
from prime_matrix_mfac_lcm_offconstant_projection_circularity_audit import (
    audit_direct_projection_contract,
    direct_projection_data,
    write_certificate,
)


def test_projection_data_recovers_actual_e1_identities(self) -> None:
    data = direct_projection_data(limit=30, alpha=0.0)
    self.assertTrue(math.isclose(data["g_e1_inner_product"], data["chebyshev_error"], abs_tol=1e-12))
    self.assertEqual(data["e1_norm_squared"], 30)
    self.assertTrue(math.isclose(data["actual_defect"], data["theoretical_defect"], abs_tol=1e-12))


def test_unique_orthogonal_coefficient_is_target_error_over_x(self) -> None:
    base = direct_projection_data(limit=30, alpha=0.0)
    data = direct_projection_data(limit=30, alpha=base["unique_orthogonal_alpha"])
    self.assertTrue(math.isclose(data["actual_defect"], 0.0, abs_tol=1e-12))
    self.assertTrue(math.isclose(data["unique_orthogonal_alpha"], data["chebyshev_error"] / 30, abs_tol=1e-12))
```

- [ ] **Step 2: 写入任意系数缺陷与循环合同测试**

```python
def test_every_alpha_has_exact_target_defect_formula(self) -> None:
    for alpha in (-2.0, 0.0, 0.5, 3.0):
        with self.subTest(alpha=alpha):
            data = direct_projection_data(limit=24, alpha=alpha)
            self.assertTrue(math.isclose(data["actual_defect"], data["theoretical_defect"], abs_tol=1e-12))


def test_target_defined_alpha_is_rejected_as_circular(self) -> None:
    result = audit_direct_projection_contract({"alpha_uses": ("psi(X)-X",)})
    self.assertEqual(result["classification"], "direct_e1_projection_uses_target_or_forbidden_analytic_input")


def test_nonforbidden_alpha_claim_stays_unverified(self) -> None:
    result = audit_direct_projection_contract({"alpha_uses": ("independent_arithmetic_name",)})
    self.assertEqual(result["classification"], "direct_e1_projection_independence_unverified")
```

- [ ] **Step 3: 运行新测试，确认红灯**

```bash
python3 -m unittest experiments.prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test -v
```

Expected: `ModuleNotFoundError` 指向尚未创建的审计模块；不得因测试拼写或框架错误失败。

- [ ] **Step 4: 提交红灯测试**

```bash
git add experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test.py
git commit -m "测试 MFAC LCM 去常数投影循环"
```

### Task 2: 实现实际投影读数与循环合同分类

**Files:**
- Create: `experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit.py`
- Test: `experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test.py`

- [ ] **Step 1: 实现有限实际 LCM 内积与 `g` 向量**

```python
from prime_matrix_mfac_actual_lcm_gram_energy_audit import (
    lcm_gram_entry,
    mobius,
    von_mangoldt,
)


def chebyshev_psi(limit: int) -> float:
    """独立逐项求和得到有限实际 psi 值。"""
    return math.fsum(von_mangoldt(value) for value in range(1, limit + 1))


def g_weight(divisor: int) -> float:
    """返回 g=w-e_1 的实际 divisor 坐标。"""
    return -mobius(divisor) * math.log(divisor) - (1.0 if divisor == 1 else 0.0)


def lcm_inner_product(limit: int, left: Mapping[int, float], right: Mapping[int, float]) -> float:
    """计算两个有限 divisor 向量的实际 LCM Gram 内积。"""
```

`lcm_inner_product` 必须拒绝非法 `limit`、非 Mapping、非有限权重、非法 divisor 和溢出项；采用 `math.fsum` 并对各项与结果做有限性检查，保持上一轮的有限实数合同。

- [ ] **Step 2: 实现投影读数与唯一系数**

```python
def direct_projection_data(limit: int, alpha: int | float) -> dict[str, float | int]:
    """审计 g-alpha*e_1 的实际投影缺陷及唯一正交系数。"""
    psi_value = chebyshev_psi(limit)
    chebyshev_error = psi_value - limit
    e1 = {1: 1.0}
    g = {divisor: g_weight(divisor) for divisor in range(1, limit + 1)}
    g_e1 = lcm_inner_product(limit, g, e1)
    e1_norm = lcm_inner_product(limit, e1, e1)
    actual_defect = lcm_inner_product(limit, {**g, 1: g[1] - alpha}, e1)
    return {
        "limit": limit,
        "psi_value": psi_value,
        "chebyshev_error": chebyshev_error,
        "g_e1_inner_product": g_e1,
        "e1_norm_squared": e1_norm,
        "alpha": float(alpha),
        "actual_defect": actual_defect,
        "theoretical_defect": chebyshev_error - float(alpha) * limit,
        "unique_orthogonal_alpha": chebyshev_error / limit,
    }
```

实现须先验证 `alpha` 是非布尔有限内建 `int|float`。测试中的实数域等式仅以明确容差作有限精度数值验证；模块 docstring 必须明确其不证明 `psi` 误差界、零点排除或 RH。

- [ ] **Step 3: 实现循环合同分类器**

```python
FORBIDDEN_DIRECT_PROJECTION_INPUTS = frozenset({
    "psi(X)", "E_psi(X)", "psi(X)-X", "target_error",
    "zero_location", "zero_free_region", "explicit_formula_remainder",
})


def audit_direct_projection_contract(contract: Mapping[str, Any]) -> dict[str, Any]:
    """分类直接 e_1 投影系数的输入来源，不虚构独立性。"""
```

`contract` 必须为 Mapping，`alpha_uses` 必须是非裸字符串的 `Iterable[str]`。若含禁止输入，返回严格分类 `direct_e1_projection_uses_target_or_forbidden_analytic_input`；否则返回 `direct_e1_projection_independence_unverified`。后者不是 actual witness，也不得返回数学不存在性。

为满足任务一已经固定的公共导入，任务二还必须临时导出：

```python
def write_certificate(output_directory: Path, limit: int = 60) -> dict[str, Path]:
    """保留证书 API；完整写出在任务三实现。"""
    raise NotImplementedError("证书写出将在任务三实现")
```

该占位只解决模块导入边界，不生成证书；任务三的红灯应期待该异常而不是缺失导入。

- [ ] **Step 4: 运行定向测试，确认绿灯**

```bash
python3 -m unittest experiments.prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test -v
python3 -m py_compile experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit.py
```

Expected: 全部已声明测试通过。

- [ ] **Step 5: 提交最小实现**

```bash
git add \
  experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit.py \
  experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test.py
git commit -m "审计 MFAC LCM 去常数投影循环"
```

### Task 3: 归档循环证书并同步项目边界

**Files:**
- Modify: `experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit.py`
- Modify: `experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-lcm-offconstant-projection-circularity-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-lcm-offconstant-projection-circularity-audit.md`
- Modify: `docs/monograph/claim-status-table.md`
- Modify: `docs/monograph/external-theorem-index.md`

- [ ] **Step 1: 写入证书红灯测试**

```python
def test_certificate_marks_direct_projection_circularity_not_global_nonexistence(self) -> None:
    with tempfile.TemporaryDirectory() as directory:
        result = write_certificate(Path(directory), limit=60)
        payload = json.loads(result["json_path"].read_text(encoding="utf-8"))
        self.assertTrue(payload["actual_lcm_e1_projection_identity_available"])
        self.assertTrue(payload["unique_direct_e1_orthogonal_coefficient_requires_target_error"])
        self.assertTrue(payload["direct_e1_target_dependent_contract_rejected"])
        self.assertFalse(payload["noncircular_actual_off_constant_coercive_witness_constructed"])
        self.assertFalse(payload["mathematical_nonexistence_proved"])
        self.assertFalse(payload["actual_chebyshev_mellin_contraction_present"])
        self.assertFalse(payload["rh_proved"])
        self.assertEqual(payload["next_positive_gate"], "NoncircularActualOffConstantCoerciveWitnessBeforeMellin")
```

- [ ] **Step 2: 运行证书测试，确认 `write_certificate` 缺失红灯**

```bash
python3 -m unittest experiments.prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test.MFACLcmOffConstantProjectionCircularityAuditTest.test_certificate_marks_direct_projection_circularity_not_global_nonexistence -v
```

Expected: `NotImplementedError` 指向尚未实现的证书写出，而不是断言或数学计算失败。

- [ ] **Step 3: 实现审计汇总、证书与 CLI**

```python
def audit_direct_projection_circularity(limit: int) -> dict[str, Any]:
    """汇总直接 e_1 投影唯一性、循环分类和未闭合出口。"""
    data = direct_projection_data(limit, alpha=0.0)
    circular = audit_direct_projection_contract({"alpha_uses": ("psi(X)-X",)})
    return {
        "limit": limit,
        "actual_lcm_e1_projection_identity_available": True,
        "unique_direct_e1_orthogonal_coefficient_requires_target_error": True,
        "direct_e1_target_dependent_contract_rejected": True,
        "noncircular_actual_off_constant_coercive_witness_constructed": False,
        "mathematical_nonexistence_proved": False,
        "actual_chebyshev_mellin_contraction_present": False,
        "rh_proved": False,
        "next_positive_gate": "NoncircularActualOffConstantCoerciveWitnessBeforeMellin",
        "projection_data": data,
        "circular_contract": circular,
    }
```

将任务二的 `write_certificate` 占位替换为功能实现，使其写出 JSON/Markdown 并返回两个 `Path`。Markdown 必须展示 `<g,e_1>_K=psi(X)-X`、`||e_1||_K^2=X`、`alpha=(psi(X)-X)/X` 与“仅直接秩一模板被拒绝”的边界。CLI 接受 `--limit`、`--output-directory`，默认写到 `docs/monograph`。

- [ ] **Step 4: 生成项目证书并更新索引**

```bash
python3 experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit.py --limit 60
```

在状态表和内部索引新增 `MFAC-LCOPC` 条目，明确这不是外部定理、不是 Mellin 收缩、不是零点排除、不是 RH；唯一正向出口为 `NoncircularActualOffConstantCoerciveWitnessBeforeMellin`。

- [ ] **Step 5: 全量验证并提交**

```bash
python3 -m unittest experiments.prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test -v
python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v
git diff --check
git add experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit.py
git add experiments/prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test.py
git add docs/monograph/prime-matrix-mfac-lcm-offconstant-projection-circularity-audit.json
git add docs/monograph/prime-matrix-mfac-lcm-offconstant-projection-circularity-audit.md
git add docs/monograph/claim-status-table.md
git add docs/monograph/external-theorem-index.md
git commit -m "归档 MFAC LCM 去常数投影循环证书"
```

Expected: 定向与全族测试通过，证书字段显示“直接投影循环已审计、非循环 witness 仍未构造、RH 未证明”。

## 自检结果

- **规格覆盖：** 实际投影恒等式和唯一性由任务 1--2 覆盖；目标依赖拒绝及独立性未证实分类由任务 2 覆盖；证书、CLI、索引与非 RH 边界由任务 3 覆盖。
- **占位符扫描：** 已按计划技能要求扫描禁用占位符模式；每个测试、API、命令、字段和提交动作均明确给出。
- **类型一致性：** `limit` 为正整数，`alpha` 为非布尔有限 `int|float`，向量为有限 `Mapping[int,float]`，合同的 `alpha_uses` 为非裸字符串的 `Iterable[str]`；任务间 API 名称完全一致。
