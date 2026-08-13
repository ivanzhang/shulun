# MFAC W1→W2 最小无条件 Chebyshev 能量桥实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development（推荐）或 superpowers:executing-plans 逐任务执行。本计划用 checkbox（`- [ ]`）跟踪步骤。

**Goal:** 构建最小无条件 W1→W2 Chebyshev 二次能量桥合同审计器，严格登记 Gram/误差接口并拒绝所有循环或外部输入，同时保持 W2 和 RH 未证明。

**Architecture:** 新模块只验证结构化 `bridge_contract`，不导入、执行或选择任何现有 Gram 模块；桥接量词、非负 Gram 声明和误差吸收目标分别序列化。三个 `uses` 字段合并后与固定禁止集合比较，任何禁用或未声明来源都会直接拒绝；有效合同也只能生成 `registered_unproved_contract` 证书。

**Tech Stack:** Python 3 标准库（`argparse`、`json`、`math`、`pathlib`、`typing`、`unittest`、`tempfile`、`subprocess`）；现有 `experiments/` 合同与 `docs/monograph/` 证书模式。

**Design Source:** `docs/superpowers/specs/2026-08-13-mfac-w1-w2-chebyshev-energy-bridge-design.md`

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit.py`
  - 最小桥接合同验证、反循环检查、证书渲染与 CLI。
- Create: `experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit_test.py`
  - 合法合同、Gram/误差输入验证、禁止输入、证书与 CLI 回归。
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-chebyshev-energy-bridge-audit.json`
  - 默认最小桥接合同的机器证书。
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-chebyshev-energy-bridge-audit.md`
  - 默认人读证书，明确 W2/RH 未证明。

不计算 `psi`、`E(X)`、`G(X)` 或 `B(X)`；不连接现有 LCM/Möbius 模块；不修改主链图谱；阶段完成后只提交本规格、本计划、新模块、新测试和两种证书。

### Task 1: 写出合法最小桥接合同红灯测试

**Files:**
- Create: `experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit_test.py`

- [ ] **Step 1: 写出完整无条件合同的边界测试**

```python
import unittest

from experiments.prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit import (
    audit_chebyshev_energy_bridge_contract,
)


class MFACW1W2ChebyshevEnergyBridgeAuditTest(unittest.TestCase):
    """验证 W1 到 W2 最小无条件能量桥合同。"""

    def test_valid_bridge_contract_stays_registered_and_unproved(self) -> None:
        """完整合同只能登记桥接义务，不能升级 W2 或 RH。"""
        audit = audit_chebyshev_energy_bridge_contract(
            {
                "uses": ("finite_gram_identity", "independent_kernel_registration"),
                "absolute_constant": "exists_A_positive_independent_of_X_and_candidate",
                "large_scale_quantifier": "exists_X0_for_all_X_ge_X0",
                "gram_contract": {
                    "coefficient_family": "pre_registered_actual_coefficients",
                    "kernel": "pre_registered_nonnegative_gram_kernel",
                    "interval_correspondence": "dyadic_X_to_2X",
                    "constant_projection": "off_constant_projection",
                    "nonnegative": True,
                    "uses": ("finite_gram_identity",),
                },
                "error_contract": {
                    "source": "independent_remainder_decomposition",
                    "eta": 0.5,
                    "absorption_target": "B(X)<=eta*G(X)",
                    "uses": ("independent_remainder_decomposition",),
                },
                "claimed_bound_uses": ("finite_gram_identity",),
            }
        )
        self.assertEqual(audit["bridge_structure_status"], "registered_unproved_contract")
        self.assertEqual(audit["error_absorption_status"], "absorption_obligation_open")
        self.assertEqual(audit["w2_actual_chebyshev_energy_bridge_status"], "unproved")
        self.assertFalse(audit["rh_proved"])
```

- [ ] **Step 2: 运行测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit_test.MFACW1W2ChebyshevEnergyBridgeAuditTest.test_valid_bridge_contract_stays_registered_and_unproved -v`

Expected: FAIL，原因是桥接审计模块尚不存在。

### Task 2: 实现最小字段验证与未证明状态

**Files:**
- Create: `experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit.py`
- Modify: `experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit_test.py`

- [ ] **Step 1: 实现 Mapping、字符串序列、正数与 eta 验证器**

```python
from math import isfinite
from typing import Mapping


def _checked_string_tuple(value: object, field_name: str) -> tuple[str, ...]:
    """拒绝裸字符串、空字符串和非字符串依赖项。"""
    if type(value) not in (tuple, list):
        raise ValueError(f"{field_name} 必须是字符串 tuple 或 list")
    if any(type(item) is not str or not item for item in value):
        raise ValueError(f"{field_name} 必须只含非空字符串")
    return tuple(value)


def _require_eta(value: object) -> float:
    """验证预注册可吸收常数 eta 位于 [0, 1)。"""
    if type(value) not in (int, float) or not isfinite(float(value)):
        raise ValueError("eta 必须是有限内建实数")
    eta = float(value)
    if not 0.0 <= eta < 1.0:
        raise ValueError("eta 必须位于 [0, 1)")
    return eta
```

- [ ] **Step 2: 实现 Gram/误差合同和主桥接状态**

```python
def audit_chebyshev_energy_bridge_contract(contract: Mapping[str, object]) -> dict[str, object]:
    """登记 W1→W2 无条件桥接接口，绝不把合同升级为证明。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须是 Mapping")
    uses = _checked_string_tuple(contract.get("uses"), "uses")
    if contract.get("absolute_constant") != "exists_A_positive_independent_of_X_and_candidate":
        raise ValueError("absolute_constant 必须登记绝对常数 A")
    if contract.get("large_scale_quantifier") != "exists_X0_for_all_X_ge_X0":
        raise ValueError("large_scale_quantifier 必须登记所有充分大 X")
    gram = _require_mapping(contract.get("gram_contract"), "gram_contract")
    error = _require_mapping(contract.get("error_contract"), "error_contract")
    gram_fields = ("coefficient_family", "kernel", "interval_correspondence", "constant_projection")
    if any(type(gram.get(field)) is not str or not gram[field] for field in gram_fields):
        raise ValueError("gram_contract 缺少非空语义字段")
    if gram.get("nonnegative") is not True:
        raise ValueError("gram_contract.nonnegative 必须为 True")
    gram_uses = _checked_string_tuple(gram.get("uses"), "gram_contract.uses")
    if type(error.get("source")) is not str or not error["source"]:
        raise ValueError("error_contract.source 必须是非空字符串")
    eta = _require_eta(error.get("eta"))
    if error.get("absorption_target") != "B(X)<=eta*G(X)":
        raise ValueError("absorption_target 必须是 B(X)<=eta*G(X)")
    error_uses = _checked_string_tuple(error.get("uses"), "error_contract.uses")
    return {
        "bridge_uses": uses,
        "gram_uses": gram_uses,
        "error_uses": error_uses,
        "eta": eta,
        "bridge_structure_status": "registered_unproved_contract",
        "absolute_constant_status": "registered_unproved",
        "large_scale_quantifier_status": "registered_unproved",
        "gram_nonnegativity_status": "declared_not_proved",
        "error_absorption_status": "absorption_obligation_open",
        "w2_actual_chebyshev_energy_bridge_status": "unproved",
        "rh_proved": False,
    }
```

- [ ] **Step 3: 运行 Task 1 测试确认通过**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit_test -v`

Expected: PASS。

### Task 3: 写出反循环与误差参数红灯测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit_test.py`

- [ ] **Step 1: 添加禁止输入、非法 eta 与目标循环测试**

```python
    def test_contract_rejects_forbidden_inputs_invalid_eta_and_target_cycle(self) -> None:
        """桥接不得读取目标/外部输入，也不得接受非法 eta 或目标结论字段。"""
        base = valid_contract()
        for location, forbidden in (
            ("uses", "Chebyshev_error"),
            ("gram_contract.uses", "Mellin"),
            ("error_contract.uses", "RH"),
            ("uses", "PNT"),
            ("uses", "Mertens_cancellation"),
        ):
            broken = copy_contract(base)
            assign_uses(broken, location, forbidden)
            with self.assertRaisesRegex(ValueError, "禁止"):
                audit_chebyshev_energy_bridge_contract(broken)

        for eta in (-0.1, 1.0, float("nan"), True):
            broken = copy_contract(base)
            broken["error_contract"]["eta"] = eta
            with self.assertRaisesRegex(ValueError, "eta"):
                audit_chebyshev_energy_bridge_contract(broken)

        cyclic = copy_contract(base)
        cyclic["rh_proved"] = False
        with self.assertRaisesRegex(ValueError, "目标结论"):
            audit_chebyshev_energy_bridge_contract(cyclic)
```

在测试文件中定义 `valid_contract()`、`copy_contract()` 和 `assign_uses()`，使用标准库 `copy.deepcopy`，确保每个子例独立修改最小合同。

- [ ] **Step 2: 运行新增测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit_test.MFACW1W2ChebyshevEnergyBridgeAuditTest.test_contract_rejects_forbidden_inputs_invalid_eta_and_target_cycle -v`

Expected: FAIL，原因是禁止集合、`claimed_bound_uses` 和目标结论循环检查尚未实现。

### Task 4: 实现反循环检查、证书与 CLI

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit.py`
- Modify: `experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-chebyshev-energy-bridge-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-chebyshev-energy-bridge-audit.md`

- [ ] **Step 1: 实现禁止集合、来源子集和目标结论字段拒绝**

```python
FORBIDDEN_INPUTS = frozenset(
    {
        "Chebyshev_error", "psi(X)-X", "target_energy", "Mellin",
        "zero_free_region", "zeta_zero", "explicit_formula", "RH", "PNT",
        "Mertens_cancellation",
    }
)
FORBIDDEN_CONCLUSION_FIELDS = frozenset(
    {
        "w2_actual_chebyshev_energy_bridge", "w2_closed", "rh_proved",
        "target_energy_bound",
    }
)


def _check_noncyclic_sources(
    uses: tuple[str, ...], gram_uses: tuple[str, ...], error_uses: tuple[str, ...],
    claimed_bound_uses: tuple[str, ...],
) -> None:
    """拒绝目标/解析循环输入，并检查所有界来源已声明。"""
    declared = uses + gram_uses + error_uses
    forbidden = tuple(item for item in declared if item in FORBIDDEN_INPUTS)
    if forbidden:
        raise ValueError(f"uses 含禁止输入：{', '.join(forbidden)}")
    undeclared = tuple(item for item in claimed_bound_uses if item not in declared)
    if undeclared:
        raise ValueError(f"claimed_bound_uses 含未声明依赖：{', '.join(undeclared)}")
```

在 `audit_chebyshev_energy_bridge_contract` 的开头拒绝 `FORBIDDEN_CONCLUSION_FIELDS` 中任何
存在的字段；读取 `claimed_bound_uses`（缺省空 tuple）；成功输出
`forbidden_input_check="passed"` 与 `claimed_bound_uses`，但不改变任何未证明状态。

- [ ] **Step 2: 实现证书写出和 CLI**

```python
DEFAULT_JSON = Path("docs/monograph/prime-matrix-mfac-w1-w2-chebyshev-energy-bridge-audit.json")
DEFAULT_MARKDOWN = Path("docs/monograph/prime-matrix-mfac-w1-w2-chebyshev-energy-bridge-audit.md")


def main() -> None:
    """生成 W1→W2 最小无条件桥接合同证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC W1 到 W2 Chebyshev 能量桥合同")
    parser.add_argument("--eta", type=float, default=0.5)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    certificate = audit_chebyshev_energy_bridge_contract(default_contract(args.eta))
    write_certificate(certificate, args.json_out, args.markdown_out)
```

`default_contract(eta)` 必须使用最小的独立 `finite_gram_identity`/
`independent_kernel_registration` 来源；`write_certificate` 的 Markdown 固定写入
`w2_actual_chebyshev_energy_bridge_status=unproved` 与 `rh_proved=false`，并声明
不计算 \(\psi\)、不证明桥接、误差吸收、W2 或 RH。

- [ ] **Step 3: 添加证书/CLI 边界测试并运行模块测试**

```python
    def test_certificate_and_cli_never_promote_bridge_to_w2_or_rh(self) -> None:
        """CLI 产物必须保留桥接、W2 和 RH 均未证明的边界。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            json_path = root / "bridge.json"
            markdown_path = root / "bridge.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit.py",
                    "--eta", "0.5", "--json-out", str(json_path),
                    "--markdown-out", str(markdown_path),
                ],
                cwd=Path.cwd(), capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["w2_actual_chebyshev_energy_bridge_status"], "unproved")
            self.assertEqual(payload["error_absorption_status"], "absorption_obligation_open")
            self.assertFalse(payload["rh_proved"])
            self.assertIn("不证明 W2", markdown_path.read_text(encoding="utf-8"))
```

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit_test -v`

Expected: PASS；任意合法/非法输入都不会得到 `proved`、`w2_closed` 或 `rh_proved=true`。

### Task 5: 生成默认合同证书、回归并提交阶段 3

**Files:**
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-chebyshev-energy-bridge-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-chebyshev-energy-bridge-audit.md`

- [ ] **Step 1: 生成默认产物并核对未证明边界**

Run:

```bash
python3 experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit.py --eta 0.5
python3 - <<'PY'
import json
from pathlib import Path
payload = json.loads(Path("docs/monograph/prime-matrix-mfac-w1-w2-chebyshev-energy-bridge-audit.json").read_text())
assert payload["bridge_structure_status"] == "registered_unproved_contract"
assert payload["error_absorption_status"] == "absorption_obligation_open"
assert payload["w2_actual_chebyshev_energy_bridge_status"] == "unproved"
assert payload["rh_proved"] is False
PY
```

Expected: 默认 JSON/Markdown 存在；合同完整但桥接、W2 和 RH 均未证明。

- [ ] **Step 2: 运行桥接测试和全量 MFAC 回归**

Run:

```bash
python3 -m unittest experiments.prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit_test -v
python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v
git diff --check
```

Expected: 新桥接测试和全量 MFAC 测试通过；差异检查无输出。

- [ ] **Step 3: 仅提交阶段 3 文件**

Run:

```bash
git add \
  docs/superpowers/specs/2026-08-13-mfac-w1-w2-chebyshev-energy-bridge-design.md \
  docs/superpowers/plans/2026-08-13-mfac-w1-w2-chebyshev-energy-bridge.md \
  experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit.py \
  experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit_test.py \
  docs/monograph/prime-matrix-mfac-w1-w2-chebyshev-energy-bridge-audit.json \
  docs/monograph/prime-matrix-mfac-w1-w2-chebyshev-energy-bridge-audit.md
git commit -m "审计 MFAC W1 到 W2 能量桥合同"
```

Expected: 提交只包含阶段 3 的规格、计划、审计器、测试和证书；`AGENTS.md` 与既有未提交文件绝不进入暂存区。

## 计划自检

- **规格覆盖：** Task 1--2 覆盖绝对常数、充分大尺度、Gram 注册、误差吸收与未证明状态；Task 3--4 覆盖禁止输入、目标结论循环、证书和 CLI；Task 5 覆盖默认产物、回归和独立提交。
- **无条件边界：** 任何 `Chebyshev_error`、`psi(X)-X`、Mellin、零点、RH、PNT 或 Mertens 输入都会被拒绝，不能降级为条件性桥接。
- **范围控制：** 不计算数论对象、不选定具体 Gram 构造、不连接现有 W1 模块、不改变 RH 主链图。
- **占位符检查：** 本计划不含 `TBD`、`TODO`、未定义接口或泛化的“适当处理”步骤。
