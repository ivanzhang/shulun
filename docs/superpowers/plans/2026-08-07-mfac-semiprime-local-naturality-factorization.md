# MFAC 半素数局部自然性分解二分 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 审计最小半素数三项的既有候选族，区分 canonical factorization、rowwise cancellation 与需要独立新算术泛函的越界候选。

**Architecture:** 新模块只编码已声明的局部自然性模型及五个现有候选族；它对每个候选返回可追溯分类，不把有限分类当作一般数学定理。模块同时接受完整 synthetic collision，确保若某候选有非 canonical row、独立来源恒等式与实际 primitive-unit 字段，审计不会错误地把它压回 canonical。CLI 读取既有证书，输出 JSON/Markdown，并明确所有 RH 边界。

**Tech Stack:** Python 3 标准库、`unittest`、JSON、Markdown。

---

## 文件结构

- 新建 `experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit.py`：候选模型、最小 triad 分类、collision 检测、当前语料适配器、证书写入和 CLI。
- 新建 `experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py`：红绿单元测试，覆盖五个候选族、synthetic collision、下游依赖拒绝与证书边界。
- 新建 `docs/monograph/prime-matrix-mfac-semiprime-local-naturality-factorization-audit.json`：由 CLI 生成的机器证书。
- 新建 `docs/monograph/prime-matrix-mfac-semiprime-local-naturality-factorization-audit.md`：人读证书，区分条件模型、当前语料和 RH 未闭合结论。
- 修改 `docs/monograph/claim-status-table.md`：登记仅限 MFAC 条件性候选审计的状态。
- 修改 `docs/monograph/external-theorem-index.md`：登记下一正向门，且禁止表述为外部定理、平方根界或 RH 进展。

### Task 1: 固定候选记录与最小分类器

**Files:**
- Create: `experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit.py`
- Test: `experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py`

- [ ] **Step 1: 写入候选记录和 triad 分类的失败测试**

```python
from prime_matrix_mfac_semiprime_local_naturality_factorization_audit import (
    build_candidate_families,
    classify_candidate,
)


def test_known_families_are_not_actual_noncanoical_declarations(self) -> None:
    results = {
        row["name"]: classify_candidate(row)
        for row in build_candidate_families(2, 3)
    }
    self.assertEqual(results["canonical_riw_buchstab_t1"]["classification"], "canonical_factorization")
    self.assertEqual(results["global_mobius_lambda"]["classification"], "global_only_zero_sum")
    self.assertEqual(results["de_colored_divisor_word"]["classification"], "global_only_transport")
    self.assertEqual(results["lpf_phi_factor_word"]["classification"], "unsigned_or_canonical_support")
    self.assertEqual(results["square_base_parity"]["classification"], "posterior_state_only")
    self.assertTrue(all(not value["actual_noncanonical_declaration"] for value in results.values()))


def test_same_row_local_log_triad_is_rowwise_zero_sum(self) -> None:
    candidate = {
        "name": "same-row-local-log",
        "pre_cauchy": True,
        "independent_of_downstream": True,
        "local_data_only": True,
        "prime_renaming_natural": True,
        "local_coefficient_law": True,
        "adds_primitive_arithmetic_functional": False,
        "row_kind": "same_row",
    }
    result = classify_candidate(candidate)
    self.assertEqual(result["classification"], "rowwise_cancellation")
    self.assertEqual(result["row_coefficient"], 0.0)
```

- [ ] **Step 2: 运行测试，确认红色阶段**

Run: `python3 -m unittest experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py -v`  
Expected: FAIL，因为候选族构造器和分类器尚不存在。

- [ ] **Step 3: 实现最小候选模型和纯分类函数**

```python
def classify_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    """在显式局部自然性模型内分类候选，不声称一般数学定理。"""
    if not candidate.get("pre_cauchy") or not candidate.get("independent_of_downstream"):
        return {**candidate, "classification": "downstream_dependent_rejected", "actual_noncanonical_declaration": False}
    if candidate.get("row_kind") == "canonical":
        return {**candidate, "classification": "canonical_factorization", "actual_noncanonical_declaration": False}
    if candidate.get("row_kind") == "same_row" and candidate.get("local_coefficient_law"):
        return {**candidate, "classification": "rowwise_cancellation", "row_coefficient": 0.0, "actual_noncanonical_declaration": False}
    return {**candidate, "classification": candidate["fallback_classification"], "actual_noncanonical_declaration": False}
```

`build_candidate_families(2, 3)` 必须构造且仅构造：`global_mobius_lambda`、
`de_colored_divisor_word`、`lpf_phi_factor_word`、`square_base_parity`、
`canonical_riw_buchstab_t1`。每条记录都写明其缺失的独立字段，不把它们虚构为 actual row。

- [ ] **Step 4: 运行单元测试，确认绿色阶段**

Run: `python3 -m unittest experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py -v`  
Expected: PASS；五个候选族分类稳定，same-row 局部对数 triad 仅返回严格零和。

- [ ] **Step 5: 提交分类器核心（仅在获得提交授权后）**

```bash
git add experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit.py experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py
git commit -m "审计 MFAC 半素数局部自然性分解"
```

### Task 2: 以 synthetic 反例固定 collision 证书合同

**Files:**
- Modify: `experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit.py`
- Modify: `experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py`

- [ ] **Step 1: 写入 collision 和下游拒绝的失败测试**

```python
from prime_matrix_mfac_semiprime_local_naturality_factorization_audit import (
    find_minimal_collision_certificate,
)


def test_complete_synthetic_noncanoical_record_is_collision_certificate(self) -> None:
    candidate = {
        "name": "synthetic-independent-functional",
        "pre_cauchy": True,
        "independent_of_downstream": True,
        "local_data_only": False,
        "prime_renaming_natural": True,
        "local_coefficient_law": True,
        "adds_primitive_arithmetic_functional": True,
        "row_kind": "noncanonical",
        "origin_selector": "synthetic-origin",
        "actual_emitter_registered": True,
        "orientation": 1,
        "local_factor": 1.0,
        "exact_uv": [1, 1],
        "prepushforward_identity": "synthetic-independent-identity",
    }
    certificate = find_minimal_collision_certificate([candidate])
    self.assertIsNotNone(certificate)
    self.assertEqual(certificate["candidate_name"], "synthetic-independent-functional")
    self.assertFalse(certificate["mathematical_nonexistence_proved"])


def test_payment_dependent_candidate_is_rejected_before_collision(self) -> None:
    candidate = {"name": "payment-derived", "pre_cauchy": False, "independent_of_downstream": False}
    result = classify_candidate(candidate)
    self.assertEqual(result["classification"], "downstream_dependent_rejected")
    self.assertFalse(result["actual_noncanonical_declaration"])
```

- [ ] **Step 2: 运行测试，确认 collision 合同尚未实现**

Run: `python3 -m unittest experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py -v`  
Expected: FAIL，因为 `find_minimal_collision_certificate` 尚未实现。

- [ ] **Step 3: 实现严格字段检查和最小反例选择**

```python
REQUIRED_INDEPENDENT_FIELDS = (
    "origin_selector", "actual_emitter_registered", "orientation", "local_factor",
    "exact_uv", "prepushforward_identity",
)


def find_minimal_collision_certificate(candidates: list[dict[str, Any]]) -> dict[str, Any] | None:
    """返回首个完整越界候选；缺字段或下游依赖均不是 collision。"""
    for candidate in candidates:
        classified = classify_candidate(candidate)
        if classified["classification"] == "downstream_dependent_rejected":
            continue
        if not classified.get("adds_primitive_arithmetic_functional"):
            continue
        if any(not candidate.get(field) for field in REQUIRED_INDEPENDENT_FIELDS):
            continue
        if candidate.get("row_kind") != "noncanonical":
            continue
        return {
            "candidate_name": candidate["name"],
            "reason": "complete_independent_noncanonical_candidate",
            "mathematical_nonexistence_proved": False,
        }
    return None
```

不得把 synthetic 反例写为 current-corpus record；它只验证审计器不会把真正完整的越界字段误分类。

- [ ] **Step 4: 运行单元测试，确认 collision 与拒绝路径绿色**

Run: `python3 -m unittest experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py -v`  
Expected: PASS；完整 synthetic 记录被捕获，payment 派生候选被拒绝。

- [ ] **Step 5: 提交 collision 合同（仅在获得提交授权后）**

```bash
git add experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit.py experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py
git commit -m "固定 MFAC 半素数最小碰撞证书"
```

### Task 3: 接入当前语料、生成证书并同步状态

**Files:**
- Modify: `experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit.py`
- Modify: `experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-semiprime-local-naturality-factorization-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-semiprime-local-naturality-factorization-audit.md`
- Modify: `docs/monograph/claim-status-table.md`
- Modify: `docs/monograph/external-theorem-index.md`

- [ ] **Step 1: 写入当前语料与证书边界的失败测试**

```python
def test_current_corpus_has_no_independent_semiprime_declaration_line(self) -> None:
    certificate = audit_current_corpus(DOCS)
    self.assertFalse(certificate["current_corpus_has_independent_semiprime_declaration_line"])
    self.assertFalse(certificate["minimal_collision_certificate_present"])
    self.assertFalse(certificate["mathematical_nonexistence_proved"])
    self.assertFalse(certificate["rh_proved"])
    self.assertEqual(
        certificate["next_positive_gate"],
        "SemiprimeTriadDeclarationLineFromIndependentArithmeticIdentity",
    )


def test_writer_states_conditional_scope_and_non_rh_boundary(self) -> None:
    certificate = audit_current_corpus(DOCS)
    with tempfile.TemporaryDirectory() as directory:
        markdown_path = Path(directory) / "certificate.md"
        write_certificate(certificate, Path(directory) / "certificate.json", markdown_path)
        markdown = markdown_path.read_text(encoding="utf-8")
    self.assertIn("仅在显式局部自然性模型内", markdown)
    self.assertIn("不表示数学上不存在", markdown)
    self.assertIn("rh_proved=false", markdown)
```

- [ ] **Step 2: 运行测试，确认语料适配器与写出函数失败**

Run: `python3 -m unittest experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py -v`  
Expected: FAIL，因为 `audit_current_corpus`、`write_certificate` 与 CLI 尚未实现。

- [ ] **Step 3: 实现只读证书适配、输出和 CLI**

`audit_current_corpus` 只读取下列既有 JSON：

```text
prime-matrix-mfac-colored-divisor-word-transport-audit.json
prime-matrix-mfac-orientation-provenance-no-go-audit.json
prime-matrix-mfac-semiprime-triad-dispatch-audit.json
```

它必须输出：

```python
{
    "current_corpus_has_independent_semiprime_declaration_line": False,
    "minimal_collision_certificate_present": False,
    "conditional_scope": "explicit_local_naturality_model_only",
    "mathematical_nonexistence_proved": False,
    "rh_proved": False,
    "row_column_unconditional_closed": False,
    "next_positive_gate": "SemiprimeTriadDeclarationLineFromIndependentArithmeticIdentity",
}
```

`write_certificate` 必须在 Markdown 中分开陈述“候选族分类结果”“条件模型范围”“当前语料缺口”与“非 RH 边界”。CLI 默认写入本计划列出的两个 monograph 文件，并支持 `--json-out`、`--markdown-out` 覆盖输出路径。

- [ ] **Step 4: 运行定向测试、生成证书并检查格式**

Run: `python3 -m unittest experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py -v && python3 experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit.py && git diff --check`  
Expected: PASS；证书明确没有 independent declaration line、没有 collision、没有 RH 结论。

- [ ] **Step 5: 同步状态文件与全族回归**

在 `claim-status-table.md` 和 `external-theorem-index.md` 新增一行：这只是“显式局部自然性模型中的候选分类审计”；它不证明条件二分对所有可能公式成立，也不提供 signed transport、`ψ` 误差、零点排除或 RH。

Run: `python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v`  
Expected: PASS；所有 MFAC 审计测试全绿。

- [ ] **Step 6: 提交证书与状态同步（仅在获得提交授权后）**

```bash
git add experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit.py experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py docs/monograph/prime-matrix-mfac-semiprime-local-naturality-factorization-audit.json docs/monograph/prime-matrix-mfac-semiprime-local-naturality-factorization-audit.md docs/monograph/claim-status-table.md docs/monograph/external-theorem-index.md
git commit -m "审计 MFAC 半素数局部自然性分解结论"
```

## 计划自检

- 覆盖规格中的五个候选族、same-row 零和、完整 synthetic collision、下游拒绝、当前语料负例、机器/人读证书与索引边界。
- 程序输出不包含“普遍定理已证明”的字段；条件性命题仅以 `explicit_local_naturality_model_only` 标识。
- 所有 actual noncanonical 结论都要求独立 origin、登记、orientation、local factor、exact `(u,v)` 与 prepushforward identity；缺字段不能通过。
- 未新增任何与 RH、零点、`ψ`、Cauchy 或推前估计有关的证明声称。
