# MFAC-1B Colored Divisor Word Transport Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构造并有限审计完整双色除数字词的 pre-pushforward 精确传输，证明其逐项保持 Möbius--von Mangoldt source payload，同时明确它尚未绑定到项目的 actual primitive unit。

**Architecture:** 新审计器以 `n=p*r` 的完整非降素因子词及 `d|n` 的 D/E 着色为 source record。追加粗辅因子 `q` 时，E 分支保持 `(mu(d),log d)`，D 分支在 `q` 未出现于 `d` 时更新为 `(-mu(d),log(d)+log(q))`，否则进入零 Möbius 分支。审计器验证 source 重构、一步传输、全局 payload 守恒和 record 唯一性；证书只声明全局 arithmetic transport，`actual_primitive_unit_binding=false`。

**Tech Stack:** Python 3 标准库（`unittest`、`json`、`hashlib`、`math`、`pathlib`）；项目既有 `experiments/` 证书生成模式。

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_colored_divisor_word_transport_audit.py`
  - 定义双色词 record、D/E 一步传输、有限全局守恒审计和证书渲染。
- Create: `experiments/prime_matrix_mfac_colored_divisor_word_transport_audit_test.py`
  - 以真实小整数验证重构、D/E 更新、零 Möbius 分支和证书边界。
- Create: `data/prime-matrix-mfac-colored-divisor-word-transport-audit-ledger.json`
  - 审计器生成的 ledger。
- Create: `docs/monograph/prime-matrix-mfac-colored-divisor-word-transport-audit.json`
  - 同步 JSON 证书。
- Create: `docs/monograph/prime-matrix-mfac-colored-divisor-word-transport-audit.md`
  - 人可读结论与 failure boundary。
- Modify: `docs/monograph/claim-status-table.md`
  - 登记 MFAC-1B 为全局 arithmetic transport 审计，不称 actual primitive binding 已闭合。

## Task 1: 写入双色词与一步传输的失败测试

**Files:**
- Create: `experiments/prime_matrix_mfac_colored_divisor_word_transport_audit_test.py`

- [ ] **Step 1: 写入期望 API 的测试**

```python
def test_colored_word_reconstructs_each_nonzero_source_pair(self) -> None:
    record = build_colored_record(n=12, divisor=6)
    self.assertEqual(record["owner_p"], 2)
    self.assertEqual(record["divisor"], 6)
    self.assertEqual(reconstruct_source_pair(record), (6, 2))

def test_append_q_has_exact_d_and_e_branches(self) -> None:
    record = build_colored_record(n=6, divisor=3)
    branches = append_rough_factor(record, 5)
    self.assertEqual(branches["E"]["divisor"], 3)
    self.assertEqual(branches["D"]["divisor"], 15)
    self.assertEqual(branches["D"]["mu_d"], 1)

def test_repeated_d_color_is_explicit_zero_mobius_branch(self) -> None:
    record = build_colored_record(n=6, divisor=3)
    branches = append_rough_factor(record, 3)
    self.assertIsNone(branches["D"])
    self.assertEqual(branches["D_return_tag"], "zero_mobius_repeated_divisor_prime")
```

- [ ] **Step 2: 运行并确认失败**

Run: `python3 experiments/prime_matrix_mfac_colored_divisor_word_transport_audit_test.py`

Expected: `ModuleNotFoundError`，因为 MFAC-1B 审计模块尚不存在。

## Task 2: 实现最小 exact colored-word transport

**Files:**
- Create: `experiments/prime_matrix_mfac_colored_divisor_word_transport_audit.py`

- [ ] **Step 1: 实现 canonical record 与重构**

```python
def build_colored_record(n: int, divisor: int) -> dict[str, object]:
    """构造保留完整 D/E 历史的 source record。"""
    factors = prime_factors(n)
    colors = color_factor_occurrences(factors, divisor)
    return {
        "n": n,
        "owner_p": factors[0],
        "factor_word": factors,
        "color_word": colors,
        "divisor": divisor,
        "cofactor": n // divisor,
        "mu_d": mobius(divisor),
        "log_d_parts": selected_d_factors(factors, colors),
    }
```

`color_factor_occurrences` 必须在重复素因子时按从左到右的唯一约定选择 D 色位置，并拒绝非 squarefree `divisor`。

- [ ] **Step 2: 实现粗辅因子 `q` 的两条精确分支**

```python
def append_rough_factor(record: dict[str, object], q: int) -> dict[str, object]:
    """把 q 追加到非降词末端，返回 E、D 与零 Möbius分支。"""
    e_branch = extend_record(record, q=q, color="E")
    if q in selected_d_factors(record["factor_word"], record["color_word"]):
        return {"E": e_branch, "D": None,
                "D_return_tag": "zero_mobius_repeated_divisor_prime"}
    return {"E": e_branch, "D": extend_record(record, q=q, color="D"),
            "D_return_tag": None}
```

`extend_record` 必须拒绝破坏非降词的 `q`，并逐项复算 `n`、`divisor`、`cofactor`、`mu_d`、`log_d_parts`，不得仅信任父 record 的缓存字段。

- [ ] **Step 3: 运行测试并确认通过**

Run: `python3 experiments/prime_matrix_mfac_colored_divisor_word_transport_audit_test.py`

Expected: 3 项测试 `OK`。

## Task 3: 添加有限守恒审计与证书

**Files:**
- Modify: `experiments/prime_matrix_mfac_colored_divisor_word_transport_audit.py`
- Modify: `experiments/prime_matrix_mfac_colored_divisor_word_transport_audit_test.py`
- Create: `data/prime-matrix-mfac-colored-divisor-word-transport-audit-ledger.json`
- Create: `docs/monograph/prime-matrix-mfac-colored-divisor-word-transport-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-colored-divisor-word-transport-audit.md`

- [ ] **Step 1: 为有限守恒写失败测试**

```python
def test_certificate_preserves_all_nonzero_mobius_payloads(self) -> None:
    certificate = build_certificate(120)
    self.assertTrue(certificate["record_reconstruction_verified"])
    self.assertTrue(certificate["one_step_transport_verified"])
    self.assertTrue(certificate["global_payload_conservation_verified"])
    self.assertFalse(certificate["actual_primitive_unit_binding_constructed"])
    self.assertFalse(certificate["mfac_1a_general_transport_constructed"])
```

- [ ] **Step 2: 实现有限审计**

对每个 `n<=limit` 和每个 squarefree `d|n`：

1. 构造并重构 source record；
2. 验证 payload `-mu(d)*log(d)`；
3. 对所有不小于词尾的有限候选素数 `q`，验证 E/D 分支同直接重建的 child record 一致；
4. 汇总所有 records，验证按 `n` 分组的 payload 和等于 `Lambda(n)`；
5. 写出最小 zero-Möbius D 分支见证及 `actual_primitive_unit_binding_constructed=false`。

- [ ] **Step 3: 运行生成器和 JSON 检查**

Run:

```bash
python3 experiments/prime_matrix_mfac_colored_divisor_word_transport_audit.py --limit 997
python3 -m json.tool data/prime-matrix-mfac-colored-divisor-word-transport-audit-ledger.json >/dev/null
python3 -m json.tool docs/monograph/prime-matrix-mfac-colored-divisor-word-transport-audit.json >/dev/null
```

Expected: 三个 exact transport 布尔值为 `true`；actual primitive binding、MFAC-1A general transport、平方根误差和 RH 均不被声明为已闭合。

## Task 4: 同步状态并作回归验证

**Files:**
- Modify: `docs/monograph/claim-status-table.md`

- [ ] **Step 1: 添加状态表行**

```markdown
| MFAC-1B 双色除数字词 pre-pushforward 传输审计 | 完整 D/E divisor-history 的逐步粗辅因子更新与有限 Möbius payload 守恒 | `colored_divisor_word_arithmetic_transport_closed_actual_primitive_binding_open` | 全局 arithmetic record 的重构、D/E 分支和有限守恒已审计；actual primitive unit 映射、remainder 分区、Type-II 控制、零点排除均未证明 | `docs/monograph/prime-matrix-mfac-colored-divisor-word-transport-audit.md` |
```

- [ ] **Step 2: 完整验证**

Run:

```bash
python3 experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit_test.py
python3 experiments/prime_matrix_mfac_colored_divisor_word_transport_audit_test.py
python3 experiments/prime_matrix_mfac_colored_divisor_word_transport_audit.py --limit 997
git diff --check
```

Expected: 两组测试通过、证书可重复生成、`git diff --check` 无输出。

## 自检

- 任务 1--2 只建立 global arithmetic record，任务 3 验证有限精确守恒，任务 4 仅同步诚实状态；没有任务把该记录等同于 actual primitive unit。
- 所有新增 Python 模块含中文注释和命令行用法示例。
- `actual_primitive_unit_binding_constructed=false` 与 `mfac_1a_general_transport_constructed=false` 是强制证书字段，防止越界结论。
