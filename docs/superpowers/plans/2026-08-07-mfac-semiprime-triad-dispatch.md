# MFAC 半素数三项 Dispatch 审计实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 审计 offdiagonal 半素数三项 Möbius payload 是否已有前向 actual primitive-row dispatch，并严格区分语料缺口与同-row 零和 collapse。

**Architecture:** 新审计器复用 colored divisor-word record 的 `p`、`q`、`p*q` 三项 global payload。dispatch 判据独立要求 pre-Cauchy、无下游依赖、origin selector、actual registration、row、orientation、local factor 与 prepushforward identity；语料适配器仅读既有证书。

**Tech Stack:** Python 3 标准库、`unittest`、JSON、Markdown。

---

### Task 1: 建立 triad 与 dispatch 判据

**Files:**
- Create: `experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit.py`
- Create: `experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit_test.py`

- [ ] **Step 1: 写入失败测试**

```python
def test_offdiagonal_triad_has_exact_zero_global_payload(self) -> None:
    triad = build_semiprime_triad(2, 3)
    self.assertEqual([(row["divisor"], row["cofactor"]) for row in triad], [(2, 3), (3, 2), (6, 1)])
    self.assertTrue(math.isclose(sum(row["global_payload"] for row in triad), 0.0, abs_tol=1e-12))

def test_same_row_synthetic_triad_is_zero_sum_collapse(self) -> None:
    certificate = audit_triad_dispatch(same_row_zero_sum_dispatch())
    self.assertTrue(certificate["canonical_zero_sum_collapse"])
    self.assertFalse(certificate["actual_dispatch_present"])

def test_complete_synthetic_dispatch_is_admissible(self) -> None:
    certificate = audit_triad_dispatch(complete_synthetic_dispatch())
    self.assertTrue(certificate["actual_dispatch_present"])
    self.assertFalse(certificate["canonical_zero_sum_collapse"])

def test_payment_dependent_dispatch_is_rejected(self) -> None:
    dispatch = complete_synthetic_dispatch()
    dispatch["entries"][0]["independent_of_downstream"] = False
    certificate = audit_triad_dispatch(dispatch)
    self.assertIn("independent_of_downstream", certificate["entries"][0]["missing_fields"])
```

- [ ] **Step 2: 运行失败测试，确认红色阶段**

Run: `python3 -m unittest experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit_test.py -v`  
Expected: FAIL，因为 triad 审计模块尚不存在。

- [ ] **Step 3: 实现最小 triad 与判据**

```python
REQUIRED_DISPATCH_FIELDS = (
    "pre_cauchy", "independent_of_downstream", "origin_selector",
    "actual_emitter_registered", "row_key", "orientation",
    "local_factor", "prepushforward_identity",
)

def build_semiprime_triad(p: int, q: int) -> list[dict[str, Any]]:
    assert p < q
    return [
        {"divisor": divisor, "cofactor": (p * q) // divisor, "global_payload": source_payload(build_colored_record(p * q, divisor))}
        for divisor in (p, q, p * q)
    ]

def audit_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    audited = []
    for entry in entries:
        missing = [field for field in REQUIRED_DISPATCH_FIELDS if entry.get(field) is not True and not entry.get(field)]
        audited.append({**entry, "missing_fields": missing, "admissible": not missing})
    return audited

def audit_triad_dispatch(dispatch: dict[str, Any]) -> dict[str, Any]:
    entries = audit_entries(dispatch["entries"])
    same_row = len({row.get("row_key") for row in entries}) == 1
    zero_sum = math.isclose(sum(row["global_payload"] for row in entries), 0.0, abs_tol=1e-12)
    actual = all(row["admissible"] for row in entries) and any(row.get("source_class") == "actual_noncanonical" for row in entries)
    return {"entries": entries, "canonical_zero_sum_collapse": same_row and zero_sum and not actual, "actual_dispatch_present": actual}
```

- [ ] **Step 4: 运行单元测试，确认绿色阶段**

Run: `python3 -m unittest experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit_test.py -v`  
Expected: PASS；验证精确 triad、collapse、synthetic actual dispatch 与下游依赖拒绝。

- [ ] **Step 5: 提交判据核心**

```bash
git add experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit.py experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit_test.py
git commit -m "审计 MFAC 半素数三项 dispatch 判据"
```

### Task 2: 接入当前语料与生成证书

**Files:**
- Modify: `experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit.py`
- Modify: `experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-semiprime-triad-dispatch-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-semiprime-triad-dispatch-audit.md`

- [ ] **Step 1: 写入语料负例与边界的失败测试**

```python
def test_current_corpus_reconstructs_triad_but_has_no_actual_dispatch(self) -> None:
    certificate = audit_current_corpus(DOCS)
    self.assertTrue(certificate["global_triad_reconstructed"])
    self.assertFalse(certificate["actual_dispatch_present"])
    self.assertEqual(certificate["earliest_missing_field"], "origin_selector")
    self.assertFalse(certificate["canonical_zero_sum_collapse"])

def test_writer_keeps_nonexistence_and_rh_boundary(self) -> None:
    certificate = audit_current_corpus(DOCS)
    with tempfile.TemporaryDirectory() as directory:
        json_out = Path(directory) / "certificate.json"
        markdown_out = Path(directory) / "certificate.md"
        write_certificate(certificate, json_out, markdown_out)
        markdown = markdown_out.read_text(encoding="utf-8")
    self.assertIn("当前语料未提交", markdown)
    self.assertIn("不表示数学上不可能", markdown)
    self.assertIn("rh_proved=false", markdown)
```

- [ ] **Step 2: 运行测试，确认新增断言失败**

Run: `python3 -m unittest experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit_test.py -v`  
Expected: FAIL，因为语料适配器与证书写出函数尚未实现。

- [ ] **Step 3: 实现只读语料适配器、Markdown 与 CLI**

```python
def audit_current_corpus(docs: Path) -> dict[str, Any]:
    colored = load_json(docs / "prime-matrix-mfac-colored-divisor-word-transport-audit.json")
    triad = build_semiprime_triad(2, 3)
    result = audit_triad_dispatch({"entries": triad})
    return {**result, "global_triad_reconstructed": colored["record_reconstruction_verified"], "earliest_missing_field": "origin_selector", "next_positive_gate": "OffDiagonalSemiprimeTriadActualDispatchBeforePushforward", "mathematical_nonexistence_proved": False, "rh_proved": False, "row_column_unconditional_closed": False}
```

- [ ] **Step 4: 运行定向测试并生成证书**

Run: `python3 -m unittest experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit_test.py -v && python3 experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit.py`  
Expected: PASS；证书确认 triad 已重构、actual dispatch 尚缺且不误报 collapse。

- [ ] **Step 5: 提交语料适配器与证书**

```bash
git add experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit.py experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit_test.py docs/monograph/prime-matrix-mfac-semiprime-triad-dispatch-audit.json docs/monograph/prime-matrix-mfac-semiprime-triad-dispatch-audit.md
git commit -m "审计 MFAC 半素数三项来源缺口"
```

### Task 3: 同步前沿并做全族回归

**Files:**
- Modify: `docs/monograph/claim-status-table.md`
- Modify: `docs/monograph/external-theorem-index.md`

- [ ] **Step 1: 写入状态索引边界**

状态条目必须说明：当前仅重构 global triad，未构造 actual dispatch；不表示数学不存在，
不闭合 signed transport、`ψ` 平滑误差、零点排除、行/列命题或 RH。

- [ ] **Step 2: 运行定向与全族回归**

Run: `python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v`  
Expected: PASS；MFAC 审计族包含新 triad dispatch 测试且全绿。

- [ ] **Step 3: 提交索引同步**

```bash
git add docs/monograph/claim-status-table.md docs/monograph/external-theorem-index.md
git commit -m "记录 MFAC 半素数三项审计结论"
```

## 计划自检

- 覆盖精确 triad、synthetic collapse、synthetic actual dispatch、下游拒绝、当前语料负例和 non-RH 边界。
- 不含未决实施项或未定义函数占位。
- 所有修改集中在新审计、其测试、生成证书与既有状态索引。
