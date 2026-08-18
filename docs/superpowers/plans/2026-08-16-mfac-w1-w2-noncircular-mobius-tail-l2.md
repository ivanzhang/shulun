# MFAC W1→W2 非循环 Möbius 尾和 L² 桥审计实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development`（推荐）或 `superpowers:executing-plans` 逐任务实施。所有步骤采用复选框跟踪。

**Goal:** 构建一个将 W1→W2 三项解析缺口显式保持为开放状态、同时核验有限 Möbius--Euler--φ 重排的非循环审计器。

**Architecture:** 新模块独立于既有条件化 Mertens、W1→W2 解析桥和 Chebyshev 桥。合同层只允许有限算术来源并拒绝循环依赖；模型层以精确 `Fraction` 计算有限互素限制尾和及 Euler--φ 能量恒等式；证书层永远将解析义务报告为 `open` 与主链报告为 `unproved`。

**Tech Stack:** Python 3 标准库（`argparse`、`fractions`、`json`、`math`、`pathlib`、`unittest`）；复用 `mobius_value` 与 `euler_phi` 的既有有限算术实现。

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit.py` — 合同验证、精确有限模型、证书写入和 CLI。
- Create: `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.py` — 合同、循环拒绝、有限恒等式和 CLI 端到端测试。
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-noncircular-mobius-tail-l2-audit.json` — 默认机器证书。
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-noncircular-mobius-tail-l2-audit.md` — 默认人读证书。

本计划不修改既有审计器、外部定理索引或当前工作树中任何已有未提交文件。按照仓库操作约束，实施结束后不创建 Git 提交。

### Task 1: 写出非循环合同的红灯测试

**Files:**
- Create: `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.py`

- [ ] **Step 1: 写出合法合同必须保持三项义务开放的测试**

```python
from experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit import (
    REQUIRED_OBLIGATIONS,
    audit_noncircular_mobius_tail_l2,
    default_contract,
)

def test_valid_contract_keeps_every_analytic_obligation_open(self) -> None:
    payload = audit_noncircular_mobius_tail_l2(default_contract(), limit=12)

    self.assertEqual(REQUIRED_OBLIGATIONS, (
        "coprime_restricted_tail_bound",
        "euler_phi_l2_aggregation",
        "chebyshev_energy_transfer",
    ))
    self.assertEqual(payload["w1_to_w2_status"], "unproved")
    self.assertEqual(payload["coprime_restricted_tail_bound_status"], "open")
    self.assertEqual(payload["euler_phi_l2_aggregation_status"], "open")
    self.assertEqual(payload["chebyshev_energy_transfer_status"], "open")
    self.assertFalse(payload["rh_proved"])
```

- [ ] **Step 2: 运行测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.MFACW1W2NoncircularMobiusTailL2AuditTest.test_valid_contract_keeps_every_analytic_obligation_open -v`

Expected: FAIL，原因是审计模块尚不存在。

### Task 2: 实现合同防火墙并使首个测试转绿

**Files:**
- Create: `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit.py`
- Modify: `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.py`

- [ ] **Step 1: 定义稳定的合同常量和严格验证器**

```python
REQUIRED_OBLIGATIONS = (
    "coprime_restricted_tail_bound",
    "euler_phi_l2_aggregation",
    "chebyshev_energy_transfer",
)
FORBIDDEN_INPUTS = frozenset({
    "RH", "Mertens", "PNT", "zeta_zero", "zero_free_region",
    "explicit_formula", "Mellin", "Chebyshev_error",
    "target_energy_bridge", "chebyshev_energy_bridge",
    "finite_profile", "numerical_experiment",
})
FORBIDDEN_CONCLUSION_FIELDS = frozenset({
    "w1_to_w2_proved", "w2_closed", "chebyshev_energy_bridge_proved",
    "rh_proved", "rh_consequence",
})

def _checked_string_tuple(value: object, field_name: str) -> tuple[str, ...]:
    """验证字符串序列，拒绝裸字符串和非字符串元素。"""
    if type(value) not in (tuple, list):
        raise ValueError(f"{field_name} 必须是字符串 tuple 或 list")
    if any(type(item) is not str or not item for item in value):
        raise ValueError(f"{field_name} 必须只含非空字符串")
    return tuple(value)

def _validate_contract(contract: Mapping[str, object]) -> dict[str, object]:
    """验证只允许有限输入的 W1→W2 缺口登记合同。"""
    # 验证 Mapping、禁止结论、uses、每项 claimed_uses、统一变量和常数依赖。
```

`_validate_contract` 必须要求：`obligations` 精确等于 `REQUIRED_OBLIGATIONS`；每个义务在
`claimed_uses` 映射中都有字符串序列；每项 `claimed_uses` 是顶层 `uses` 的子集；
`uniformity_variable == "truncation"`；`constant_dependency == "fixed_test_function"`。
默认 `uses` 只列 `finite_arithmetic`、`mobius_definition`、`coprimality_relation`、
`finite_sum_identity`，不含任何解析假设。

- [ ] **Step 2: 实现最小审计入口和默认合同**

```python
def audit_noncircular_mobius_tail_l2(
    contract: Mapping[str, object], limit: object,
) -> dict[str, object]:
    """登记非循环缺口并附加有限模型，绝不生成解析证明结论。"""
    checked = _validate_contract(contract)
    return {
        **checked,
        "coprime_restricted_tail_bound_status": "open",
        "euler_phi_l2_aggregation_status": "open",
        "chebyshev_energy_transfer_status": "open",
        "w1_to_w2_status": "unproved",
        "rh_proved": False,
    }

def default_contract() -> dict[str, object]:
    """返回只含有限算术来源的默认合同。"""
    return {
        "uses": (
            "finite_arithmetic", "mobius_definition",
            "coprimality_relation", "finite_sum_identity",
        ),
        "obligations": REQUIRED_OBLIGATIONS,
        "claimed_uses": {
            obligation: ("finite_arithmetic", "finite_sum_identity")
            for obligation in REQUIRED_OBLIGATIONS
        },
        "uniformity_variable": "truncation",
        "constant_dependency": "fixed_test_function",
    }
```

- [ ] **Step 3: 运行 Task 1 测试确认转绿**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.MFACW1W2NoncircularMobiusTailL2AuditTest.test_valid_contract_keeps_every_analytic_obligation_open -v`

Expected: PASS。

### Task 3: 增加反循环负向测试并完成防御性校验

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.py`
- Modify: `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit.py`

- [ ] **Step 1: 写出禁止来源、未声明依赖和结论提升的红灯测试**

```python
def test_contract_rejects_circular_inputs_missing_quantifiers_and_promotions(self) -> None:
    base = default_contract()
    for source in ("RH", "Mertens", "PNT", "zeta_zero", "Mellin"):
        broken = deepcopy(base)
        broken["uses"] += (source,)
        with self.assertRaisesRegex(ValueError, "禁止"):
            audit_noncircular_mobius_tail_l2(broken, limit=12)

    undeclared = deepcopy(base)
    undeclared["claimed_uses"] = dict(base["claimed_uses"])
    undeclared["claimed_uses"]["euler_phi_l2_aggregation"] = ("Mellin",)
    with self.assertRaisesRegex(ValueError, "未声明|禁止"):
        audit_noncircular_mobius_tail_l2(undeclared, limit=12)

    for field, value in (
        ("uniformity_variable", "scale"),
        ("constant_dependency", "truncation"),
        ("rh_proved", True),
        ("w2_closed", True),
    ):
        broken = deepcopy(base)
        broken[field] = value
        with self.assertRaises(ValueError):
            audit_noncircular_mobius_tail_l2(broken, limit=12)
```

- [ ] **Step 2: 运行新增测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.MFACW1W2NoncircularMobiusTailL2AuditTest.test_contract_rejects_circular_inputs_missing_quantifiers_and_promotions -v`

Expected: FAIL，直到验证器检查每条 `claimed_uses`、全部禁止来源和禁止结论字段。

- [ ] **Step 3: 补齐负向验证并运行合同测试组**

在 `_validate_contract` 中先拒绝任何禁止结论字段，再检查顶层与逐义务来源中的禁止元素，随后拒绝未在 `uses` 中声明的逐义务来源。对 `obligations`、`claimed_uses`、统一变量和常数依赖分别给出含字段名的 `ValueError`。

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test -v`

Expected: 合同测试 PASS；有限模型和 CLI 测试可暂未添加。

### Task 4: 以精确有理数实现有限可证伪模型

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit.py`
- Modify: `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.py`

- [ ] **Step 1: 写出小截断 Möbius--Euler--φ 恒等式红灯测试**

```python
def test_finite_model_matches_direct_and_euler_phi_energies(self) -> None:
    payload = finite_coprime_mobius_tail_model(12)

    self.assertEqual(payload["finite_model_status"], "verified_finite")
    self.assertEqual(payload["limit"], 12)
    self.assertEqual(payload["candidate_moduli"], tuple(range(2, 12)))
    self.assertEqual(payload["energy_identity_residual"], "0")
    self.assertEqual(
        payload["direct_finite_energy"], payload["euler_phi_finite_energy"]
    )

def test_finite_model_rejects_invalid_limits(self) -> None:
    for limit in (True, 1, 2.0, "12"):
        with self.assertRaisesRegex(ValueError, "limit"):
            finite_coprime_mobius_tail_model(limit)
```

- [ ] **Step 2: 运行有限模型测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.MFACW1W2NoncircularMobiusTailL2AuditTest.test_finite_model_matches_direct_and_euler_phi_energies -v`

Expected: FAIL，因为 `finite_coprime_mobius_tail_model` 尚不存在。

- [ ] **Step 3: 实现精确 Möbius 尾和、直接能量和 Euler--φ 分解**

```python
from fractions import Fraction
from math import gcd

from experiments.prime_matrix_mfac_mobius_tail_l2_audit import euler_phi
from experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit import mobius_value

def _require_limit(limit: object) -> int:
    """验证有限模型截断长度。"""
    if type(limit) is not int or limit < 3:
        raise ValueError("limit 必须是至少为 3 的内建整数")
    return limit

def finite_coprime_mobius_tail_model(limit: object) -> dict[str, object]:
    """核验有限 Möbius 尾和的 Euler--φ 重排，不声明渐近界。"""
    checked_limit = _require_limit(limit)
    coefficients = {index: Fraction(mobius_value(index), 1)
                    for index in range(2, checked_limit)}
    divisor_tails = {
        modulus: sum(value / index for index, value in coefficients.items()
                     if index % modulus == 0)
        for modulus in range(2, checked_limit)
    }
    coprime_tails = {
        modulus: Fraction(mobius_value(modulus), modulus) * sum(
            Fraction(mobius_value(multiplier), multiplier)
            for multiplier in range(1, checked_limit // modulus + 1)
            if modulus * multiplier < checked_limit and gcd(modulus, multiplier) == 1
        ) if mobius_value(modulus) != 0 else Fraction(0, 1)
        for modulus in range(2, checked_limit)
    }
    direct_energy = sum(
        left * right * Fraction(gcd(left_index, right_index) - 1,
                                left_index * right_index)
        for left_index, left in coefficients.items()
        for right_index, right in coefficients.items()
    )
    euler_phi_energy = sum(
        Fraction(euler_phi(modulus), 1) * tail * tail
        for modulus, tail in divisor_tails.items()
    )
    residual = direct_energy - euler_phi_energy
    coprime_residual = max(
        (abs(divisor_tails[modulus] - coprime_tails[modulus])
         for modulus in divisor_tails),
        default=Fraction(0, 1),
    )
    return {
        "finite_model_status": (
            "verified_finite" if residual == 0 and coprime_residual == 0 else "failed"
        ),
        "limit": checked_limit,
        "candidate_moduli": tuple(divisor_tails),
        "direct_finite_energy": str(direct_energy),
        "euler_phi_finite_energy": str(euler_phi_energy),
        "energy_identity_residual": str(residual),
        "coprime_tail_identity_residual": str(coprime_residual),
    }
```

直接能量必须采用与 `experiments/prime_matrix_mfac_mobius_tail_l2_audit.py` 的
`limit_kernel_energy` 相同核 `Fraction(gcd(d, e) - 1, d * e)`。`divisor_tails` 使用
`sum(a_d / d)`；`coprime_tails` 是其按 `d=r m` 展开的互素限制形式。两种尾和及
Euler--φ 重排均须精确相等；所有 `Fraction` 结果以字符串写入 JSON 安全字段。

- [ ] **Step 4: 运行有限模型测试确认转绿**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.MFACW1W2NoncircularMobiusTailL2AuditTest.test_finite_model_matches_direct_and_euler_phi_energies -v`

Expected: PASS，残差精确为 `0`。

### Task 5: 实现证书、CLI 与端到端边界测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit.py`
- Modify: `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-noncircular-mobius-tail-l2-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-noncircular-mobius-tail-l2-audit.md`

- [ ] **Step 1: 写出脚本路径 CLI 与证书边界红灯测试**

```python
def test_script_path_cli_writes_finite_but_unproved_certificate(self) -> None:
    with TemporaryDirectory() as directory:
        root = Path(directory)
        json_path = root / "audit.json"
        markdown_path = root / "audit.md"
        result = subprocess.run(
            [sys.executable,
             "experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit.py",
             "--limit", "12", "--json-out", str(json_path),
             "--markdown-out", str(markdown_path)],
            cwd=Path.cwd(), capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(json_path.read_text(encoding="utf-8"))
        self.assertEqual(payload["finite_model_status"], "verified_finite")
        self.assertEqual(payload["w1_to_w2_status"], "unproved")
        self.assertFalse(payload["rh_proved"])
        markdown = markdown_path.read_text(encoding="utf-8")
        self.assertIn("euler_phi_l2_aggregation_status=open", markdown)
        self.assertIn("不证明", markdown)
```

- [ ] **Step 2: 运行 CLI 测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.MFACW1W2NoncircularMobiusTailL2AuditTest.test_script_path_cli_writes_finite_but_unproved_certificate -v`

Expected: FAIL，因为证书写入器、Markdown 渲染器和 CLI 尚不存在。

- [ ] **Step 3: 实现证书写入、Markdown 边界与 CLI**

```python
def write_certificate(
    payload: Mapping[str, object], json_out: Path, markdown_out: Path,
) -> None:
    """写出机器证书和明确未证明边界的人读证书。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    markdown_out.write_text(render_markdown(payload), encoding="utf-8")

def main() -> None:
    """运行默认有限模型并生成不升级结论的审计证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC W1→W2 非循环尾和审计证书")
    parser.add_argument("--limit", type=int, default=512)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    payload = audit_noncircular_mobius_tail_l2(default_contract(), args.limit)
    write_certificate(payload, args.json_out, args.markdown_out)
```

`render_markdown` 必须同时显示有限模型数值、精确残差、三个 `open` 状态、
`w1_to_w2_status=unproved`、`rh_proved=false` 与脚本路径使用示例；必须明确说明
有限重排不产生 L²--Upper、Chebyshev 桥、Mellin 收缩或 RH 证明。

- [ ] **Step 4: 运行完整新模块测试并生成默认产物**

Run:

```bash
python3 -m unittest experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test -v
python3 experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit.py --limit 512
```

Expected: 全部 PASS；默认 JSON/Markdown 存在，有限层为 `verified_finite`，解析层保持 `open` 与 `unproved`。

### Task 6: 执行相邻回归、范围检查与证书复核

**Files:**
- Verify: `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit.py`
- Verify: `experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test.py`
- Verify: `docs/monograph/prime-matrix-mfac-w1-w2-noncircular-mobius-tail-l2-audit.json`
- Verify: `docs/monograph/prime-matrix-mfac-w1-w2-noncircular-mobius-tail-l2-audit.md`

- [ ] **Step 1: 运行相邻 W1/W2、Möbius 与 LCM 审计回归**

Run:

```bash
python3 -m unittest \
  experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit_test \
  experiments.prime_matrix_mfac_w1_w2_analytic_bridge_audit_test \
  experiments.prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit_test \
  experiments.prime_matrix_mfac_mobius_tail_l2_audit_test -v
```

Expected: 全部 PASS；既有模块仍报告自身未证明边界。

- [ ] **Step 2: 审核默认产物和改动范围**

Run:

```bash
git diff --check
git status --short
```

Expected: 无空白错误；除本任务新模块、测试、默认两份证书、设计规格和本计划外，不新增或修改其他文件。

- [ ] **Step 3: 手动复核结论边界**

确认 JSON 与 Markdown 同时包含：

```text
finite_model_status=verified_finite
w1_to_w2_status=unproved
coprime_restricted_tail_bound_status=open
euler_phi_l2_aggregation_status=open
chebyshev_energy_transfer_status=open
rh_proved=false
```

Expected: 任何有限读数都未被描述为解析 L² 上界、Chebyshev 能量桥或 RH 证明。

## 计划自检

- **规格覆盖：** Task 1--3 覆盖依赖账本、量词与常数依赖、防循环边界；Task 4 覆盖精确有限模型；Task 5 覆盖 JSON/Markdown/CLI；Task 6 覆盖相邻回归与范围控制。
- **边界覆盖：** 每项解析义务保持 `open`，主链保持 `unproved`，有限层唯一允许的正状态为 `verified_finite`。
- **占位符检查：** 本计划没有 `TBD`、`TODO`、泛化的“适当处理”或未指定测试命令。
- **执行约束：** 不创建 Git 提交；不修改已有审计器或用户当前未提交文件。
