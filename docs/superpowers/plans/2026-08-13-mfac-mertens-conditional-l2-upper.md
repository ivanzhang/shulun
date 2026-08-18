# MFAC 全 ε Mertens 条件化 L²--Upper 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development（推荐）或 superpowers:executing-plans 逐任务执行。本计划用 checkbox（`- [ ]`）跟踪步骤。

**Goal:** 构建可机检的全 ε Mertens 条件链审计器与数学说明，严格区分条件链登记、开放解析义务、无条件 L²--Upper 和 RH。

**Architecture:** 新审计器保持独立，只复用既有 Möbius 尾和 L² 审计器中的有限代数身份名称，而不调用其数值剖面来证明全局结论。模块把全 ε 假设、单 ε 合法实例化、开放的互素分部求和/尾和/聚合义务，以及非循环结论分别序列化；CLI 生成 JSON、Markdown 和配套数学说明。

**Tech Stack:** Python 3 标准库（`argparse`、`json`、`math`、`pathlib`、`typing`、`unittest`）；既有 `experiments/` 审计与 `docs/monograph/` 证书模式。

**Design Source:** `docs/superpowers/specs/2026-08-13-mfac-mertens-conditional-l2-upper-design.md`

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_mertens_conditional_l2_upper_audit.py`
  - 全 ε Mertens 合同、单 ε 实例化检查、条件依赖图、证书写出和 CLI。
- Create: `experiments/prime_matrix_mfac_mertens_conditional_l2_upper_audit_test.py`
  - 合同防御性验证、条件链边界、证书与 CLI 回归测试。
- Create: `docs/monograph/prime-matrix-mfac-mertens-conditional-l2-upper-audit.json`
  - 默认 `epsilon=0.1` 的机器可读条件链证书。
- Create: `docs/monograph/prime-matrix-mfac-mertens-conditional-l2-upper-audit.md`
  - 默认人读证书，明示开放义务与非 RH 边界。
- Create: `docs/monograph/prime-matrix-mfac-mertens-conditional-l2-upper-notes.md`
  - 全 ε 量词、常数依赖与三项开放分析引理的数学说明。

不修改 `AGENTS.md`、不改变 `experiments/prime_matrix_mfac_mobius_tail_l2_audit.py` 的接口、不以有限样本验证 Mertens 假设、不创建提交。

### Task 1: 写出全 ε Mertens 合同红灯测试

**Files:**
- Create: `experiments/prime_matrix_mfac_mertens_conditional_l2_upper_audit_test.py`

- [ ] **Step 1: 写出合法合同与单 ε 参数的测试**

```python
import unittest

from experiments.prime_matrix_mfac_mertens_conditional_l2_upper_audit import (
    audit_mertens_all_epsilon_contract,
)


class MFACMertensConditionalL2UpperAuditTest(unittest.TestCase):
    """验证全 epsilon Mertens 条件链的合同和结论边界。"""

    def test_all_epsilon_mertens_contract_keeps_constant_nonuniform(self) -> None:
        """全 epsilon 假设只允许常数依赖当前 epsilon。"""
        audit = audit_mertens_all_epsilon_contract(
            {
                "uses": (
                    "finite_divisor_identity",
                    "euler_phi_identity",
                    "Mertens_cancellation",
                    "partial_summation",
                    "coprimality_inclusion_exclusion",
                ),
                "for_every_epsilon": True,
                "epsilon_domain": "positive_real",
                "assumption": "M(x)=O_epsilon(x^(1/2+epsilon))",
                "constant_dependency": "C_epsilon_depends_on_epsilon_only",
                "uniform_in_epsilon": False,
                "epsilon": 0.1,
                "mertens_constant": 3.0,
            }
        )
        self.assertEqual(audit["mertens_assumption_status"], "externally_assumed")
        self.assertEqual(audit["epsilon_instance"], 0.1)
        self.assertFalse(audit["constant_uniform_in_epsilon"])
        self.assertEqual(audit["unconditional_l2_upper_status"], "unproved")
        self.assertFalse(audit["rh_proved"])
```

- [ ] **Step 2: 运行测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_mertens_conditional_l2_upper_audit_test.MFACMertensConditionalL2UpperAuditTest.test_all_epsilon_mertens_contract_keeps_constant_nonuniform -v`

Expected: FAIL，原因是新审计模块尚不存在。

### Task 2: 实现全 ε 合同验证与开放义务图

**Files:**
- Create: `experiments/prime_matrix_mfac_mertens_conditional_l2_upper_audit.py`
- Modify: `experiments/prime_matrix_mfac_mertens_conditional_l2_upper_audit_test.py`

- [ ] **Step 1: 实现 Mapping、字符串序列和有限正数验证器**

```python
from math import isfinite
from typing import Mapping


def _require_positive_builtin_real(value: object, field_name: str) -> float:
    """验证单 epsilon 实例化使用的有限正内建实数。"""
    if type(value) not in (int, float) or not isfinite(float(value)):
        raise ValueError(f"{field_name} 必须是有限内建实数")
    checked = float(value)
    if checked <= 0.0:
        raise ValueError(f"{field_name} 必须严格为正")
    return checked


def _checked_string_tuple(value: object, field_name: str) -> tuple[str, ...]:
    """拒绝裸字符串、空字符串和非字符串依赖项。"""
    if type(value) not in (tuple, list):
        raise ValueError(f"{field_name} 必须是字符串 tuple 或 list")
    if any(type(item) is not str or not item for item in value):
        raise ValueError(f"{field_name} 必须只含非空字符串")
    return tuple(value)
```

- [ ] **Step 2: 实现全 ε 合同及不可省略的开放义务状态**

```python
REQUIRED_USES = frozenset(
    {
        "finite_divisor_identity",
        "euler_phi_identity",
        "Mertens_cancellation",
        "partial_summation",
        "coprimality_inclusion_exclusion",
    }
)
OPEN_OBLIGATIONS = (
    "CoprimeRestrictedPartialSummation",
    "TailBoundWithParameterDependence",
    "EulerPhiL2Aggregation",
)


def audit_mertens_all_epsilon_contract(contract: Mapping[str, object]) -> dict[str, object]:
    """登记全 epsilon Mertens 条件链，不把它升级为解析证明。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须是 Mapping")
    uses = _checked_string_tuple(contract.get("uses"), "uses")
    if not REQUIRED_USES.issubset(uses):
        raise ValueError("uses 缺少全 epsilon 条件链所需依赖")
    if contract.get("for_every_epsilon") is not True:
        raise ValueError("for_every_epsilon 必须为 True")
    if contract.get("epsilon_domain") != "positive_real":
        raise ValueError("epsilon_domain 必须是 positive_real")
    if contract.get("assumption") != "M(x)=O_epsilon(x^(1/2+epsilon))":
        raise ValueError("assumption 必须是标准全 epsilon Mertens 型界")
    if contract.get("constant_dependency") != "C_epsilon_depends_on_epsilon_only":
        raise ValueError("constant_dependency 必须限定为仅依赖 epsilon")
    if contract.get("uniform_in_epsilon") is not False:
        raise ValueError("uniform_in_epsilon 必须为 False")
    epsilon = _require_positive_builtin_real(contract.get("epsilon"), "epsilon")
    mertens_constant = _require_positive_builtin_real(
        contract.get("mertens_constant"), "mertens_constant"
    )
    return {
        "uses": uses,
        "mertens_assumption_status": "externally_assumed",
        "epsilon_quantifier": "for_every_positive_epsilon",
        "epsilon_instance": epsilon,
        "mertens_constant_instance": mertens_constant,
        "constant_uniform_in_epsilon": False,
        "open_obligations": OPEN_OBLIGATIONS,
        "conditional_l2_upper_status": "assumption_chain_registered",
        "unconditional_l2_upper_status": "unproved",
        "rh_proved": False,
    }
```

- [ ] **Step 3: 运行 Task 1 测试确认通过**

Run: `python3 -m unittest experiments.prime_matrix_mfac_mertens_conditional_l2_upper_audit_test -v`

Expected: PASS。

### Task 3: 写出防循环与量词缺失红灯测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_mertens_conditional_l2_upper_audit_test.py`

- [ ] **Step 1: 添加非法 epsilon、错误量词和循环输入测试**

```python
    def test_contract_rejects_missing_quantifier_uniform_constant_and_cycle(self) -> None:
        """条件链不得省略量词、伪造一致常数或引用 RH/目标结论。"""
        base = {
            "uses": (
                "finite_divisor_identity",
                "euler_phi_identity",
                "Mertens_cancellation",
                "partial_summation",
                "coprimality_inclusion_exclusion",
            ),
            "for_every_epsilon": True,
            "epsilon_domain": "positive_real",
            "assumption": "M(x)=O_epsilon(x^(1/2+epsilon))",
            "constant_dependency": "C_epsilon_depends_on_epsilon_only",
            "uniform_in_epsilon": False,
            "epsilon": 0.1,
            "mertens_constant": 3.0,
        }
        for field, value, message in (
            ("for_every_epsilon", False, "for_every_epsilon"),
            ("uniform_in_epsilon", True, "uniform_in_epsilon"),
            ("epsilon", 0.0, "epsilon"),
        ):
            broken = dict(base)
            broken[field] = value
            with self.assertRaisesRegex(ValueError, message):
                audit_mertens_all_epsilon_contract(broken)

        cyclic = dict(base)
        cyclic["uses"] = base["uses"] + ("RH", "target_l2_upper")
        with self.assertRaisesRegex(ValueError, "禁止"):
            audit_mertens_all_epsilon_contract(cyclic)
```

- [ ] **Step 2: 运行新增测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_mertens_conditional_l2_upper_audit_test.MFACMertensConditionalL2UpperAuditTest.test_contract_rejects_missing_quantifier_uniform_constant_and_cycle -v`

Expected: FAIL，原因是禁止依赖检查尚未实现。

### Task 4: 实现禁止依赖、证书和 CLI

**Files:**
- Modify: `experiments/prime_matrix_mfac_mertens_conditional_l2_upper_audit.py`
- Modify: `experiments/prime_matrix_mfac_mertens_conditional_l2_upper_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-mertens-conditional-l2-upper-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-mertens-conditional-l2-upper-audit.md`

- [ ] **Step 1: 加入禁止输入和 `claimed_bound_uses` 子集检查**

```python
FORBIDDEN_CYCLIC_USES = frozenset(
    {
        "RH",
        "zeta_zero",
        "zero_free_region",
        "explicit_formula",
        "Mellin",
        "target_l2_upper",
        "unconditional_l2_upper",
    }
)


def _check_noncyclic_dependencies(
    uses: tuple[str, ...], claimed_bound_uses: tuple[str, ...]
) -> None:
    """拒绝 RH/目标结论循环，并确保界的来源已经声明。"""
    forbidden = tuple(item for item in uses if item in FORBIDDEN_CYCLIC_USES)
    if forbidden:
        raise ValueError(f"uses 含禁止循环依赖：{', '.join(forbidden)}")
    undeclared = tuple(item for item in claimed_bound_uses if item not in uses)
    if undeclared:
        raise ValueError(f"claimed_bound_uses 含未声明依赖：{', '.join(undeclared)}")
```

在 `audit_mertens_all_epsilon_contract` 中读取 `claimed_bound_uses`；缺省时使用空 tuple，并在返回值加入 `forbidden_dependency_check="passed"`。保持 `OPEN_OBLIGATIONS` 不变，禁止通过这些字段把状态改成 `proved_under_mertens`。

- [ ] **Step 2: 实现证书写出和 CLI**

```python
DEFAULT_JSON = Path(
    "docs/monograph/prime-matrix-mfac-mertens-conditional-l2-upper-audit.json"
)
DEFAULT_MARKDOWN = Path(
    "docs/monograph/prime-matrix-mfac-mertens-conditional-l2-upper-audit.md"
)


def write_certificate(certificate: Mapping[str, object], json_path: Path, markdown_path: Path) -> None:
    """写出条件链证书，明确不构成无条件解析结论。"""
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(
        "# MFAC 全 epsilon Mertens 条件化 L2--Upper 审计\n\n"
        f"- 单实例：`epsilon={certificate['epsilon_instance']}`\n"
        "- 全称量词：`for_every_positive_epsilon`\n"
        "- 常数：`C_epsilon` 仅可依赖当前 epsilon，且不要求 epsilon 一致。\n\n"
        "```text\n"
        "mertens_assumption_status=externally_assumed\n"
        "conditional_l2_upper_status=assumption_chain_registered\n"
        "unconditional_l2_upper_status=unproved\n"
        "rh_proved=false\n"
        "```\n\n"
        "互素限制分部求和、带参数尾和界和 Euler--phi L2 聚合仍是开放证明义务；"
        "本证书不证明 Mertens 型界、Mass--Lower、Chebyshev 能量桥、Mellin 收缩、"
        "零自由区域或 RH。\n",
        encoding="utf-8",
    )


def main() -> None:
    """生成默认全 epsilon Mertens 条件链审计证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC 全 epsilon Mertens 条件化 L2 审计")
    parser.add_argument("--epsilon", type=float, default=0.1)
    parser.add_argument("--mertens-constant", type=float, default=1.0)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    certificate = audit_mertens_all_epsilon_contract(
        {
            "uses": (
                "finite_divisor_identity", "euler_phi_identity", "Mertens_cancellation",
                "partial_summation", "coprimality_inclusion_exclusion",
            ),
            "for_every_epsilon": True,
            "epsilon_domain": "positive_real",
            "assumption": "M(x)=O_epsilon(x^(1/2+epsilon))",
            "constant_dependency": "C_epsilon_depends_on_epsilon_only",
            "uniform_in_epsilon": False,
            "epsilon": args.epsilon,
            "mertens_constant": args.mertens_constant,
            "claimed_bound_uses": (),
        }
    )
    write_certificate(certificate, args.json_out, args.markdown_out)
```

- [ ] **Step 3: 添加证书/CLI 边界测试并运行完整模块测试**

```python
    def test_certificate_and_cli_never_claim_unconditional_l2_or_rh(self) -> None:
        """JSON、Markdown 和脚本路径 CLI 都必须保留条件性边界。"""
        from pathlib import Path
        from tempfile import TemporaryDirectory
        import json
        import subprocess
        import sys

        with TemporaryDirectory() as directory:
            root = Path(directory)
            json_path = root / "audit.json"
            markdown_path = root / "audit.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_mertens_conditional_l2_upper_audit.py",
                    "--epsilon", "0.1",
                    "--json-out", str(json_path),
                    "--markdown-out", str(markdown_path),
                ],
                cwd=Path.cwd(), capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["conditional_l2_upper_status"], "assumption_chain_registered")
            self.assertEqual(payload["unconditional_l2_upper_status"], "unproved")
            self.assertFalse(payload["rh_proved"])
            self.assertIn("开放证明义务", markdown_path.read_text(encoding="utf-8"))
```

Run: `python3 -m unittest experiments.prime_matrix_mfac_mertens_conditional_l2_upper_audit_test -v`

Expected: PASS，且不存在 `proved_under_mertens`、`unconditional_l2_upper_status=proved` 或 `rh_proved=true`。

### Task 5: 写出独立数学说明并完成范围验证

**Files:**
- Create: `docs/monograph/prime-matrix-mfac-mertens-conditional-l2-upper-notes.md`

- [ ] **Step 1: 写出全 ε 条件链数学说明**

文档必须包含以下可核对内容：

```markdown
# MFAC 全 ε Mertens 条件化 L²--Upper 说明

对每个 epsilon>0，假设存在 C_epsilon>0，使得对所有 x>=1 有
|M(x)| <= C_epsilon x^(1/2+epsilon)。C_epsilon 可以依赖 epsilon，
但不得依赖截断 D；本说明不声称这些常数对 epsilon 一致。

有限 Euler--phi 分解已独立验证。要从上式进入整体 L²--Upper，还必须分别证明：
1. 互素限制的 Möbius 和如何由 M(x) 控制；
2. 分部求和后对数权和的指数和常数依赖；
3. 各 r 的界如何在 sum phi(r)|T_D(r)|² 中聚合。

因此当前产物只登记条件链；它不证明 Mertens 假设、无条件 L²--Upper、
Mass--Lower、Chebyshev 能量桥、Mellin 收缩、零自由区域或 RH。
```

- [ ] **Step 2: 生成默认产物并运行相关回归**

Run:

```bash
python3 experiments/prime_matrix_mfac_mertens_conditional_l2_upper_audit.py --epsilon 0.1
python3 -m unittest experiments.prime_matrix_mfac_mertens_conditional_l2_upper_audit_test -v
python3 -m unittest experiments.prime_matrix_mfac_mobius_tail_l2_audit_test -v
python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v
git diff --check
```

Expected: 新条件证书与说明文档存在；新模块测试、既有 Möbius L² 测试和全量 MFAC 测试通过；默认 JSON/Markdown 均保留 `unconditional_l2_upper_status=unproved` 与 `rh_proved=false`；`git diff --check` 无输出。

- [ ] **Step 3: 检查范围，不提交**

Run: `git status --short && git diff --check`

Expected: 只出现本计划列出的新模块、测试、两种证书、说明文档和规划文件，以及用户已有的未提交变更；不执行 `git add` 或 `git commit`。

## 计划自检

- **规格覆盖：** Task 1--2 实现全 ε 假设、常数依赖和单 ε 实例化；Task 3--4 实现禁止 RH/目标循环、证书和 CLI；Task 5 写出数学说明并覆盖全量回归。
- **边界覆盖：** 每个证书和测试都断言条件链登记、无条件 L²--Upper 未证明、RH 未证明；开放义务不可被合同伪装为解析完成。
- **范围控制：** 不实现 Mertens 证明或三项开放引理，不修改既有有限 L² 审计器接口，不增加外部依赖。
- **占位符检查：** 本计划不含 `TBD`、`TODO`、未定义接口或“适当处理”式泛化步骤。
