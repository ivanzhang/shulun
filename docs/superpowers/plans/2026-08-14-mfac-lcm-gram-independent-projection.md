# MFAC LCM Gram 独立投影恒等式实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` task-by-task. Steps use checkbox syntax for tracking.

**Goal:** 注册独立正交投影—LCM Gram 恒等式接口，拒绝目标/解析循环输入，并保持 W2、RH 未证明。

**Architecture:** 新模块只验证 `projection_contract` 与 `gram_contract` 的结构、量词和来源；不计算投影或 Gram。两个合同以相同 `constant_projection` 绑定，所有来源统一作反循环检查。

**Tech Stack:** Python 3 标准库（`argparse`、`json`、`pathlib`、`typing`、`unittest`）。

**Design Source:** `docs/superpowers/specs/2026-08-14-mfac-lcm-gram-independent-projection-design.md`

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit.py`
- Create: `experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-lcm-gram-independent-projection-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-lcm-gram-independent-projection-audit.md`

不计算具体投影、Chebyshev 数据或残差；不改动既有 LCM 审计器；阶段结束仅提交以上文件和本规格/计划。

### Task 1: 写合法合同的红灯测试

**Files:**
- Create: `experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit_test.py`

- [ ] **Step 1: 写入最小合法合同测试**

```python
import unittest

from experiments.prime_matrix_mfac_lcm_gram_independent_projection_audit import (
    audit_lcm_gram_independent_projection_contract,
)


class MFACLCMGramIndependentProjectionAuditTest(unittest.TestCase):
    def test_valid_contract_only_registers_unproved_projection_identity(self) -> None:
        audit = audit_lcm_gram_independent_projection_contract(
            {
                "uses": ("finite_lcm_overlap_identity", "independent_feature_registration"),
                "projection_contract": {
                    "space": "L2([X,2X])",
                    "quantifier": "exists_X0_for_all_real_X_ge_X0_and_all_f_in_HX",
                    "feature_family": "independent_divisibility_features",
                    "feature_independence": "registered_independent_of_chebyshev_target",
                    "closed_subspace": True,
                    "orthogonal_projection": True,
                    "constant_projection": "off_constant_projection",
                    "uses": ("finite_lcm_overlap_identity",),
                },
                "gram_contract": {
                    "kernel": "registered_lcm_gram_kernel",
                    "coefficient_coordinates": "projection_coordinates",
                    "normalization": "dyadic_L2_normalization",
                    "lcm_overlap": "registered_lcm_divisibility_overlap",
                    "constant_projection": "off_constant_projection",
                    "uses": ("finite_lcm_overlap_identity",),
                },
                "claimed_identity_uses": ("finite_lcm_overlap_identity",),
            }
        )
        self.assertEqual(audit["projection_space_status"], "registered_unproved")
        self.assertEqual(audit["lcm_gram_identity_status"], "registered_unproved")
        self.assertEqual(audit["actual_chebyshev_projection_status"], "not_started")
        self.assertFalse(audit["rh_proved"])
```

- [ ] **Step 2: 确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_lcm_gram_independent_projection_audit_test.MFACLCMGramIndependentProjectionAuditTest.test_valid_contract_only_registers_unproved_projection_identity -v`

Expected: FAIL，目标模块不存在。

### Task 2: 实现语义验证与未证明状态

**Files:**
- Create: `experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit.py`
- Modify: `experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit_test.py`

- [ ] **Step 1: 实现最小合同验证器**

```python
def audit_lcm_gram_independent_projection_contract(contract: Mapping[str, object]) -> dict[str, object]:
    """登记独立投影—LCM Gram 接口，绝不把它升级为证明。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须是 Mapping")
    uses = _checked_string_tuple(contract.get("uses"), "uses")
    projection = _require_mapping(contract.get("projection_contract"), "projection_contract")
    gram = _require_mapping(contract.get("gram_contract"), "gram_contract")
    required_projection = {
        "space": "L2([X,2X])",
        "quantifier": "exists_X0_for_all_real_X_ge_X0_and_all_f_in_HX",
        "feature_independence": "registered_independent_of_chebyshev_target",
    }
    if any(projection.get(key) != value for key, value in required_projection.items()):
        raise ValueError("projection_contract 含错误空间、量词或独立性声明")
    for field in ("feature_family", "constant_projection"):
        if type(projection.get(field)) is not str or not projection[field]:
            raise ValueError("projection_contract 缺少非空语义字段")
    if projection.get("closed_subspace") is not True or projection.get("orthogonal_projection") is not True:
        raise ValueError("projection_contract 必须声明闭子空间和正交投影")
    projection_uses = _checked_string_tuple(projection.get("uses"), "projection_contract.uses")
    for field in ("kernel", "coefficient_coordinates", "normalization", "constant_projection"):
        if type(gram.get(field)) is not str or not gram[field]:
            raise ValueError("gram_contract 缺少非空语义字段")
    if gram.get("lcm_overlap") != "registered_lcm_divisibility_overlap":
        raise ValueError("gram_contract.lcm_overlap 必须登记实际 LCM overlap")
    if gram["constant_projection"] != projection["constant_projection"]:
        raise ValueError("两个 constant_projection 必须一致")
    gram_uses = _checked_string_tuple(gram.get("uses"), "gram_contract.uses")
    return {
        "uses": uses,
        "projection_uses": projection_uses,
        "gram_uses": gram_uses,
        "projection_space_status": "registered_unproved",
        "lcm_gram_identity_status": "registered_unproved",
        "finite_normalization_status": "not_used_as_proof",
        "actual_chebyshev_projection_status": "not_started",
        "residual_control_status": "not_started",
        "w2_actual_chebyshev_energy_bridge_status": "unproved",
        "rh_proved": False,
    }
```

- [ ] **Step 2: 确认首个测试转绿**

Run: `python3 -m unittest experiments.prime_matrix_mfac_lcm_gram_independent_projection_audit_test -v`

Expected: PASS。

### Task 3: 写反循环与对齐红灯测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit_test.py`

- [ ] **Step 1: 添加禁止来源、去常数错配和未声明来源测试**

```python
    def test_contract_rejects_cycles_alignment_errors_and_undeclared_sources(self) -> None:
        base = valid_contract()
        for location, forbidden in (
            ("uses", "Chebyshev_error"),
            ("projection_contract.uses", "Mellin"),
            ("gram_contract.uses", "RH"),
            ("uses", "PNT"),
        ):
            broken = copy_contract(base)
            assign_uses(broken, location, forbidden)
            with self.assertRaisesRegex(ValueError, "禁止"):
                audit_lcm_gram_independent_projection_contract(broken)
        mismatch = copy_contract(base)
        mismatch["gram_contract"]["constant_projection"] = "constant_projection"
        with self.assertRaisesRegex(ValueError, "一致"):
            audit_lcm_gram_independent_projection_contract(mismatch)
        undeclared = copy_contract(base)
        undeclared["claimed_identity_uses"] = ("unregistered_source",)
        with self.assertRaisesRegex(ValueError, "未声明"):
            audit_lcm_gram_independent_projection_contract(undeclared)
        cyclic = copy_contract(base)
        cyclic["projection_identity_proved"] = False
        with self.assertRaisesRegex(ValueError, "目标结论"):
            audit_lcm_gram_independent_projection_contract(cyclic)
```

测试文件用 `copy.deepcopy` 定义 `valid_contract()`、`copy_contract()` 和 `assign_uses()`。

- [ ] **Step 2: 确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_lcm_gram_independent_projection_audit_test.MFACLCMGramIndependentProjectionAuditTest.test_contract_rejects_cycles_alignment_errors_and_undeclared_sources -v`

Expected: FAIL，禁止集合、来源子集和目标结论循环检查缺失。

### Task 4: 实现反循环、证书和 CLI

**Files:**
- Modify: `experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit.py`
- Modify: `experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-lcm-gram-independent-projection-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-lcm-gram-independent-projection-audit.md`

- [ ] **Step 1: 实现来源检查**

```python
FORBIDDEN_INPUTS = frozenset({
    "Chebyshev_error", "psi(X)-X", "Lambda(n)-1", "target_energy", "Mellin",
    "zero_free_region", "zeta_zero", "explicit_formula", "RH", "PNT", "Mertens_cancellation",
})
FORBIDDEN_CONCLUSION_FIELDS = frozenset({
    "actual_chebyshev_projection", "residual_control", "w2_closed", "rh_proved",
    "projection_identity_proved",
})

def _check_sources(uses, projection_uses, gram_uses, claimed):
    """拒绝循环输入，并要求恒等式来源已预先声明。"""
    declared = uses + projection_uses + gram_uses
    forbidden = tuple(item for item in declared if item in FORBIDDEN_INPUTS)
    if forbidden:
        raise ValueError(f"uses 含禁止输入：{', '.join(forbidden)}")
    undeclared = tuple(item for item in claimed if item not in declared)
    if undeclared:
        raise ValueError(f"claimed_identity_uses 含未声明依赖：{', '.join(undeclared)}")
```

主函数拒绝任何目标结论字段；成功时输出 `forbidden_input_check="passed"` 和 `claimed_identity_uses`，但不改变未证明状态。

- [ ] **Step 2: 实现默认合同、证书和 CLI**

```python
DEFAULT_JSON = Path("docs/monograph/prime-matrix-mfac-lcm-gram-independent-projection-audit.json")
DEFAULT_MARKDOWN = Path("docs/monograph/prime-matrix-mfac-lcm-gram-independent-projection-audit.md")

def main() -> None:
    """生成独立投影—LCM Gram 合同证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC LCM Gram 独立投影合同")
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    write_certificate(
        audit_lcm_gram_independent_projection_contract(default_contract()),
        args.json_out,
        args.markdown_out,
    )
```

Markdown 必须写入 `lcm_gram_identity_status=registered_unproved`、`actual_chebyshev_projection_status=not_started`、`w2_actual_chebyshev_energy_bridge_status=unproved` 和 `rh_proved=false`，并声明不证明投影、恒等式、Chebyshev 映射、残差、W2 或 RH。

- [ ] **Step 3: 添加 CLI 边界测试**

```python
    def test_certificate_and_cli_keep_projection_and_rh_unproved(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            json_path = root / "projection.json"
            markdown_path = root / "projection.md"
            result = subprocess.run(
                [sys.executable, "experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit.py", "--json-out", str(json_path), "--markdown-out", str(markdown_path)],
                cwd=Path.cwd(), capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["lcm_gram_identity_status"], "registered_unproved")
            self.assertEqual(payload["actual_chebyshev_projection_status"], "not_started")
            self.assertFalse(payload["rh_proved"])
            self.assertIn("不证明", markdown_path.read_text(encoding="utf-8"))
```

Run: `python3 -m unittest experiments.prime_matrix_mfac_lcm_gram_independent_projection_audit_test -v`

Expected: PASS；不存在 `proved`、`w2_closed` 或 `rh_proved=true`。

### Task 5: 生成证书、回归与提交

- [ ] **Step 1: 生成并验证默认产物**

Run: `python3 experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit.py && python3 -m unittest experiments.prime_matrix_mfac_lcm_gram_independent_projection_audit_test -v && python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v && git diff --check`

Expected: 默认 JSON/Markdown 存在；新测试和全量 MFAC 测试通过；状态保持未证明。

- [ ] **Step 2: 仅提交阶段 4 文件**

Run: `git add docs/superpowers/specs/2026-08-14-mfac-lcm-gram-independent-projection-design.md docs/superpowers/plans/2026-08-14-mfac-lcm-gram-independent-projection.md experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit.py experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit_test.py docs/monograph/prime-matrix-mfac-lcm-gram-independent-projection-audit.json docs/monograph/prime-matrix-mfac-lcm-gram-independent-projection-audit.md && git commit -m "审计 MFAC LCM Gram 独立投影合同"`

Expected: 不混入 `AGENTS.md` 或既有未提交文件。

## 计划自检

- **规格覆盖：** 覆盖空间、全称量词、独立性、LCM overlap、去常数绑定、反循环、证书与全量回归。
- **边界：** 只登记接口；不执行投影、不读取 Chebyshev 数据、不生成 W2/RH 证明。
- **占位符检查：** 不含 `TBD`、`TODO` 或泛化“适当处理”步骤。
