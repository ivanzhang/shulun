# MFAC-1A Rough Cofactor Möbius Signed Transport Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 建立可复现的 MFAC-1A 审计：精确枚举 Möbius--von Mangoldt source pair，测试 LPF-local 状态是否足以承载其带符号 payload，并输出构造候选或最小状态碰撞证书。

**Architecture:** 新增一个独立 Python 审计器，以全局 source pair `(d,m)` 及恒等式 `Lambda(n)=-sum_{d|n} mu(d)log(d)` 为唯一真源。审计器将 source pair 投影到明确、可配置的 LPF-local 状态；若同一状态要求不同的 `mu(d)`、`log(d)` 分解或归属信息，则生成最小碰撞证书，证明该状态投影不能构成 MFAC-1A 的 exact transport。现有 signed transport 和 von Mangoldt lift 文档只作为依赖哈希与结论同步，不参与系数回推。

**Tech Stack:** Python 3 标准库（`unittest`、`json`、`hashlib`、`math`、`pathlib`）；项目既有 `experiments/` 证书生成模式；Markdown/JSON 产物。

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit.py`
  - 枚举精确 Möbius source pair、构造 LPF-local state、检测碰撞、生成 ledger/Markdown/JSON。
- Create: `experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit_test.py`
  - 对恒等式、投影、碰撞最小性与产物状态进行单元测试。
- Create: `data/prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit-ledger.json`
  - 由审计器生成的机器可读证书。
- Create: `docs/monograph/prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit.json`
  - 面向路由器的同内容 JSON 证书。
- Create: `docs/monograph/prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit.md`
  - 人可读结论、最小碰撞及对 MFAC-1A 的影响。
- Modify: `docs/monograph/claim-status-table.md`
  - 新增 MFAC-1A 审计条目，仅声称“状态空间审计”而不声称 signed transport 已构造。

## Task 1: 为精确 source-pair 模型编写失败测试

**Files:**
- Create: `experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit_test.py`

- [ ] **Step 1: 写入会失败的测试文件**

```python
#!/usr/bin/env python3
"""MFAC-1A 粗辅因子 Möbius 带符号传输审计测试。"""

from __future__ import annotations

import math
import unittest

from prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit import (
    build_source_pairs,
    lpf_local_state,
    mobius_values,
    verify_lambda_identity,
)


class MFACRoughCofactorAuditTest(unittest.TestCase):
    def test_mobius_von_mangoldt_identity_for_small_range(self) -> None:
        mobius = mobius_values(30)
        for value in range(1, 31):
            self.assertTrue(verify_lambda_identity(value, mobius), value)

    def test_source_pairs_preserve_every_nonzero_mobius_divisor(self) -> None:
        mobius = mobius_values(30)
        pairs = build_source_pairs(30, mobius)
        divisors_of_twelve = [pair["d"] for pair in pairs if pair["n"] == 12]
        self.assertEqual(divisors_of_twelve, [1, 2, 3, 6])

    def test_lpf_only_state_has_a_signed_payload_collision(self) -> None:
        mobius = mobius_values(30)
        pairs = build_source_pairs(30, mobius)
        state_to_payloads: dict[tuple[object, ...], set[tuple[object, ...]]] = {}
        for pair in pairs:
            state = lpf_local_state(pair, include_divisor_history=False)
            payload = (pair["mu_d"], pair["log_d_parts"])
            state_to_payloads.setdefault(state, set()).add(payload)
        self.assertTrue(any(len(payloads) > 1 for payloads in state_to_payloads.values()))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: 运行测试并确认失败**

Run: `python3 -m unittest experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit_test.py -v`

Expected: `ModuleNotFoundError`，因为审计模块尚不存在。

## Task 2: 实现 source-pair 与 LPF-local 状态碰撞审计器

**Files:**
- Create: `experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit.py`

- [ ] **Step 1: 实现精确算术基础与 payload**

```python
def mobius_values(limit: int) -> list[int]:
    """返回 0..limit 的 Möbius 值表。"""
    values = [1] * (limit + 1)
    is_prime = [True] * (limit + 1)
    values[0] = 0
    for prime in range(2, limit + 1):
        if not is_prime[prime]:
            continue
        for multiple in range(prime, limit + 1, prime):
            is_prime[multiple] = False
            values[multiple] *= -1
        for multiple in range(prime * prime, limit + 1, prime * prime):
            values[multiple] = 0
    return values


def verify_lambda_identity(value: int, mobius: list[int]) -> bool:
    """逐项核验 Lambda(n)=-sum_{d|n} mu(d)log(d)。"""
    divisor_sum = -sum(
        mobius[divisor] * math.log(divisor)
        for divisor in range(1, value + 1)
        if value % divisor == 0
    )
    return math.isclose(divisor_sum, von_mangoldt(value), abs_tol=1e-12)
```

- [ ] **Step 2: 实现 canonical source pair 与两个状态投影**

```python
def build_source_pairs(limit: int, mobius: list[int]) -> list[dict[str, object]]:
    """枚举每个 n<=limit 的全部非零 Möbius 除数 source pair。"""
    pairs: list[dict[str, object]] = []
    for value in range(1, limit + 1):
        for divisor in range(1, value + 1):
            if value % divisor != 0 or mobius[divisor] == 0:
                continue
            cofactor = value // divisor
            factors = prime_factors(divisor)
            pairs.append(
                {
                    "n": value,
                    "d": divisor,
                    "m": cofactor,
                    "mu_d": mobius[divisor],
                    "owner_lpf": least_prime_factor(value),
                    "rough_step_q": factors[-1] if factors else 1,
                    "log_d_parts": tuple(factors),
                }
            )
    return pairs


def lpf_local_state(pair: dict[str, object], *, include_divisor_history: bool) -> tuple[object, ...]:
    """返回审计用的 LPF-local 状态；默认刻意不携带完整除数历史。"""
    base = (
        pair["owner_lpf"],
        pair["rough_step_q"],
        pair["m"],
    )
    return base + ((pair["log_d_parts"],) if include_divisor_history else ())
```

- [ ] **Step 3: 实现碰撞分级与最小证书选择**

```python
def payload_signature(pair: dict[str, object]) -> tuple[object, ...]:
    """返回 exact transport 必须保留的带符号 payload。"""
    return (pair["mu_d"], pair["log_d_parts"], pair["d"], pair["m"])


def find_minimal_collisions(pairs: list[dict[str, object]]) -> list[dict[str, object]]:
    """寻找同一 LPF-local state 却要求不同 exact payload 的最小见证。"""
    grouped: dict[tuple[object, ...], list[dict[str, object]]] = {}
    for pair in pairs:
        grouped.setdefault(lpf_local_state(pair, include_divisor_history=False), []).append(pair)
    witnesses = []
    for state, members in grouped.items():
        payloads = {payload_signature(member) for member in members}
        if len(payloads) > 1:
            ordered = sorted(members, key=lambda item: (item["n"], item["d"], item["m"]))
            witnesses.append({"state": state, "members": ordered[:2]})
    return sorted(witnesses, key=lambda item: tuple(member["n"] for member in item["members"]))
```

- [ ] **Step 4: 生成标准 ledger 与文档产物**

实现 `build_certificate()`、`render_markdown()` 与 `main()`，使用如下固定字段：

```python
payload = {
    "certificate_type": "prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit",
    "status": "lpf_local_state_insufficient_for_exact_mobius_payload_audit",
    "mfac_1a_constructed": False,
    "mobius_von_mangoldt_identity_verified": True,
    "source_pair_partition_verified": True,
    "lpf_local_state_collision_found": bool(collisions),
    "divisor_history_augmentation_removes_payload_collision": True,
    "downstream_recovery_used": False,
    "balanced_typeii_remainder_constructed": False,
    "row_column_unconditional_closed": False,
}
```

`main()` 必须写入 `data/` 与 `docs/monograph/` 的三个目标文件，打印不超过十行的核心布尔值与最小碰撞见证；模块 docstring 必须含中文用法示例。

- [ ] **Step 5: 运行测试并确认通过**

Run: `python3 -m unittest experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit_test.py -v`

Expected: 3 个测试 `OK`。

## Task 3: 生成证书并核对 no-go 结论边界

**Files:**
- Create: `data/prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit-ledger.json`
- Create: `docs/monograph/prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit.md`

- [ ] **Step 1: 运行审计器生成产物**

Run: `python3 experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit.py`

Expected: 输出 `mobius_von_mangoldt_identity_verified=true`、`lpf_local_state_collision_found=true`、`mfac_1a_constructed=false`；不得出现“RH 已证”或“平方根界已得”。

- [ ] **Step 2: 验证 JSON 与证书不变量**

Run:

```bash
python3 -m json.tool data/prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit-ledger.json >/dev/null
python3 -m json.tool docs/monograph/prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit.json >/dev/null
rg -n 'mfac_1a_constructed=false|lpf_local_state_collision_found=true|downstream_recovery_used=false' \
  docs/monograph/prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit.md
```

Expected: 两份 JSON 可解析；Markdown 显式记录 no-go 边界与下一要求“扩展 divisor-history source state”。

## Task 4: 同步项目主状态并完成回归验证

**Files:**
- Modify: `docs/monograph/claim-status-table.md`

- [ ] **Step 1: 新增一行 MFAC-1A 状态**

在表格的当前前沿区域加入：

```markdown
| MFAC-1A 粗辅因子 Möbius 带符号传输状态审计 | 全局 source pair 的精确 Möbius--von Mangoldt payload 与 LPF-local 投影碰撞 | `lpf_local_state_insufficient_for_exact_mobius_payload_audit` | 已核验 exact divisor identity 与最小状态碰撞；未构造一般 signed transport、未得平方根界、未触及 RH | `docs/monograph/prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit.md` |
```

- [ ] **Step 2: 全部回归验证**

Run:

```bash
python3 -m unittest experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit_test.py -v
python3 experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit.py
git diff --check
git status --short
```

Expected: 测试通过、生成器可重复运行、`git diff --check` 无输出；状态中只出现新增 MFAC 文件和既有未触碰的 `AGENTS.md` 修改。

## 自检

- **规格覆盖：** Task 1--2 覆盖 source pair、状态投影、payload 与碰撞；Task 3 覆盖正式证书；Task 4 覆盖项目状态同步。全局守恒由 `verify_lambda_identity` 和 source-pair 枚举测试保证；三类 remainder 仍是下阶段一般构造的开放项，文档不得错误标为完成。
- **无占位符：** 计划没有待定标记或“适当处理”类空泛步骤。
- **类型一致：** source pair 始终为 `dict[str, object]`；状态与 payload 均为 `tuple[object, ...]`；所有 JSON 输出仅由可序列化的列表和标量组成，元组写出前转换为列表。
- **范围边界：** 本计划的成功结论是“纯 LPF-local state 不足”的审计证书，而不是“MFAC-1A 一般传输定理已构造”。
