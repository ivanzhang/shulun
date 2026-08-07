# MFAC 取向来源 No-Go 审计实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 生成可复核证书，严格判定当前语料是否已提交可前向追溯的 actual primitive orientation 来源。

**Architecture:** 新审计器读取四份既有证书，将 actual record、LPF support、rough-cofactor split 与 Möbius/parity shadow 归一为候选来源条目。候选必须同时具有 pre-Cauchy 独立性、`origin_selector`、orientation bit、local-factor product、prepushforward identity 与 actual-emitter registration 才能通过；否则只报告语料缺口。

**Tech Stack:** Python 3 标准库、`unittest`、JSON、Markdown。

---

### Task 1: 建立失败测试与候选判据

**Files:**
- Create: `experiments/prime_matrix_mfac_orientation_provenance_no_go_audit.py`
- Create: `experiments/prime_matrix_mfac_orientation_provenance_no_go_audit_test.py`

- [ ] **Step 1: 写入失败测试**

```python
def test_current_corpus_has_no_admissible_orientation_source(self) -> None:
    certificate = audit_orientation_provenance(DOCS)
    self.assertFalse(certificate["admissible_orientation_source_present"])
    self.assertEqual(certificate["earliest_missing_forward_field"], "origin_selector")
    self.assertEqual(certificate["next_positive_gate"], "PrimitiveOrientationLocalFactorProductLawBeforePushforward")
    self.assertFalse(certificate["mathematical_nonexistence_proved"])

def test_complete_synthetic_source_is_admissible(self) -> None:
    certificate = audit_candidate_sources([complete_synthetic_source()])
    self.assertTrue(certificate["admissible_orientation_source_present"])

def test_mobius_shadow_without_emitter_identity_is_rejected(self) -> None:
    certificate = audit_candidate_sources([mobius_parity_shadow_source()])
    self.assertFalse(certificate["admissible_orientation_source_present"])
    self.assertIn("actual_emitter_registered", certificate["candidate_sources"][0]["missing_fields"])

def test_downstream_dependent_source_is_rejected(self) -> None:
    source = complete_synthetic_source()
    source["independent_of_downstream"] = False
    certificate = audit_candidate_sources([source])
    self.assertFalse(certificate["admissible_orientation_source_present"])
    self.assertIn("independent_of_downstream", certificate["candidate_sources"][0]["missing_fields"])
```

- [ ] **Step 2: 运行失败测试，确认红色阶段**

Run: `python3 -m unittest experiments/prime_matrix_mfac_orientation_provenance_no_go_audit_test.py -v`  
Expected: FAIL，因为模块和 `audit_orientation_provenance` 尚不存在。

- [ ] **Step 3: 最小实现候选判定核心**

```python
REQUIRED_SOURCE_FIELDS = (
    "pre_cauchy",
    "independent_of_downstream",
    "provides_origin_selector",
    "provides_orientation_bit",
    "provides_local_factor_product",
    "provides_prepushforward_sum_identity",
    "actual_emitter_registered",
)

def audit_candidate_sources(candidates: list[dict[str, object]]) -> dict[str, object]:
    audited = []
    for candidate in candidates:
        missing = [field for field in REQUIRED_SOURCE_FIELDS if candidate.get(field) is not True]
        audited.append({**candidate, "missing_fields": missing, "admissible": not missing})
    return {"candidate_sources": audited, "admissible_orientation_source_present": any(row["admissible"] for row in audited)}
```

- [ ] **Step 4: 运行单元测试，确认绿色阶段**

Run: `python3 -m unittest experiments/prime_matrix_mfac_orientation_provenance_no_go_audit_test.py -v`  
Expected: PASS；覆盖当前负例、完整正例、Möbius shadow 与下游泄漏。

- [ ] **Step 5: 提交测试与判据核心**

```bash
git add experiments/prime_matrix_mfac_orientation_provenance_no_go_audit.py experiments/prime_matrix_mfac_orientation_provenance_no_go_audit_test.py
git commit -m "审计 MFAC 取向来源判据"
```

### Task 2: 接入既有证书并生成可读证据

**Files:**
- Modify: `experiments/prime_matrix_mfac_orientation_provenance_no_go_audit.py`
- Modify: `experiments/prime_matrix_mfac_orientation_provenance_no_go_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-orientation-provenance-no-go-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-orientation-provenance-no-go-audit.md`

- [ ] **Step 1: 增加证书来源与渲染的失败断言**

```python
def test_current_corpus_classifies_all_four_sources(self) -> None:
    certificate = audit_orientation_provenance(DOCS)
    self.assertEqual([row["name"] for row in certificate["candidate_sources"]], [
        "actual_atomic_record_constructor", "phi_lpf_owner_support",
        "rough_cofactor_domain_split", "mobius_parity_shadow",
    ])
    self.assertFalse(certificate["mathematical_nonexistence_proved"])
    self.assertFalse(certificate["row_column_unconditional_closed"])

def test_writer_distinguishes_corpus_gap_from_mathematical_no_go(self) -> None:
    write_certificate(certificate, json_out, markdown_out)
    markdown = markdown_out.read_text(encoding="utf-8")
    self.assertIn("当前语料未提交", markdown)
    self.assertIn("不表示数学上不可能", markdown)
```

- [ ] **Step 2: 运行测试，确认新增断言失败**

Run: `python3 -m unittest experiments/prime_matrix_mfac_orientation_provenance_no_go_audit_test.py -v`  
Expected: FAIL，因为证书读取、四候选分类与写出函数尚未实现。

- [ ] **Step 3: 实现语料适配器与证书写出**

```python
def audit_orientation_provenance(docs: Path) -> dict[str, object]:
    actual = load_json(docs / "prime-matrix-mfac-actual-record-constructor-audit.json")
    support = load_json(docs / "prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json")
    transport = load_json(docs / "prime-matrix-phi-lpf-bucket-signed-transport-router.json")
    orientation = load_json(docs / "prime-matrix-strict-row-level-noncircular-orientation-law-router.json")
    result = audit_candidate_sources(build_current_corpus_candidates(actual, support, transport, orientation))
    return {**result, "earliest_missing_forward_field": "origin_selector", "next_positive_gate": "PrimitiveOrientationLocalFactorProductLawBeforePushforward", "mathematical_nonexistence_proved": False, "row_column_unconditional_closed": False}
```

- [ ] **Step 4: 运行全量新审计测试并生成证书**

Run: `python3 -m unittest experiments/prime_matrix_mfac_orientation_provenance_no_go_audit_test.py -v && python3 experiments/prime_matrix_mfac_orientation_provenance_no_go_audit.py`  
Expected: PASS；默认 `docs/monograph/` 下生成 JSON 与 Markdown，结论为当前语料无 admissible orientation source。

- [ ] **Step 5: 提交审计器与生成证书**

```bash
git add experiments/prime_matrix_mfac_orientation_provenance_no_go_audit.py experiments/prime_matrix_mfac_orientation_provenance_no_go_audit_test.py docs/monograph/prime-matrix-mfac-orientation-provenance-no-go-audit.json docs/monograph/prime-matrix-mfac-orientation-provenance-no-go-audit.md
git commit -m "审计 MFAC 取向来源缺口"
```

### Task 3: 回归 MFAC 审计族并固定边界

**Files:**
- Modify: `docs/monograph/claim-status-table.md`
- Modify: `docs/monograph/external-theorem-index.md`
- Modify: `experiments/prime_matrix_mfac_orientation_provenance_no_go_audit_test.py`

- [ ] **Step 1: 写入边界检查测试**

```python
def test_markdown_keeps_nonclosure_boundary(self) -> None:
    write_certificate(certificate, json_out, markdown_out)
    markdown = markdown_out.read_text(encoding="utf-8")
    self.assertIn("row_column_unconditional_closed=false", markdown)
    self.assertIn("RH", markdown)
    self.assertIn("未证明", markdown)
```

- [ ] **Step 2: 同步状态索引，不升级数学主张**

```markdown
| MFAC orientation provenance no-go audit | 当前语料无 admissible pre-Cauchy orientation source；最早缺 `origin_selector` | 不表示数学不存在；不闭合 signed transport、行/列命题或 RH | `PrimitiveOrientationLocalFactorProductLawBeforePushforward` |
```

- [ ] **Step 3: 运行定向与全族回归**

Run: `python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v`  
Expected: PASS；所有 MFAC 审计测试通过。

- [ ] **Step 4: 提交索引同步与回归证据**

```bash
git add docs/monograph/claim-status-table.md docs/monograph/external-theorem-index.md experiments/prime_matrix_mfac_orientation_provenance_no_go_audit_test.py
git commit -m "记录 MFAC 取向来源审计结论"
```

## 计划自检

- 覆盖规格中的四类候选、当前语料负例、synthetic 正例、Möbius shadow、下游依赖拒绝和证书边界。
- 不含未决实施项或未定义函数占位。
- 所有写入路径、测试命令和提交范围均固定；无关文件不在计划内。
