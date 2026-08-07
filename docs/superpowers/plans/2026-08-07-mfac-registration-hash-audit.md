# MFAC Registration Hash Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 审计 formal-unit/source-tuple/source-record hash 是否前向编码 actual emitter registration，并禁止由 hash、payload 或下游数据补写 registration。

**Architecture:** 审计器独立检查 hash-layer 公式、actual source-table 状态与 explicit registration manifest。只有 registration 三元组同时出现在 hash 层、已构造源表与无下游依赖 manifest 中时，才报告 `registration_recoverable_from_hash=true`。

**Tech Stack:** Python 3 标准库与现有 monograph JSON/Markdown 证书。

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_registration_hash_audit.py` — 审计并生成证书。
- Create: `experiments/prime_matrix_mfac_registration_hash_audit_test.py` — 当前语料、正例、缺字段和泄漏测试。
- Create: `docs/monograph/prime-matrix-mfac-registration-hash-audit.json` — 机器证书。
- Create: `docs/monograph/prime-matrix-mfac-registration-hash-audit.md` — 人工报告。
- Modify: `docs/monograph/claim-status-table.md` — 状态同步。

### Task 1: 红色测试

**Files:**
- Create: `experiments/prime_matrix_mfac_registration_hash_audit_test.py`
- Create: `experiments/prime_matrix_mfac_registration_hash_audit.py`

- [ ] **Step 1: 写入所需行为**

```python
def test_current_hashes_do_not_recover_registration(self) -> None:
    certificate = audit_registration_evidence(DEFAULT_PATHS)
    self.assertFalse(certificate["hash_contains_registration_fields"])
    self.assertFalse(certificate["actual_source_table_constructed"])
    self.assertFalse(certificate["registration_recoverable_from_hash"])
    self.assertEqual(certificate["earliest_missing_registration_field"], "emitter_id")

def test_complete_explicit_registration_fixture_passes(self) -> None:
    with tempfile.TemporaryDirectory() as directory:
        certificate = audit_registration_evidence(complete_registration_fixture(Path(directory)))
    self.assertTrue(certificate["registration_recoverable_from_hash"])
```

- [ ] **Step 2: 加入边界测试**

```python
def test_missing_same_unit_certificate_blocks_registration(self) -> None:
    paths = complete_registration_fixture(self.temp_path)
    remove_registration_field(paths["manifest"], "same_formal_unit_certificate")
    certificate = audit_registration_evidence(paths)
    self.assertFalse(certificate["registration_recoverable_from_hash"])
    self.assertEqual(certificate["earliest_missing_registration_field"], "same_formal_unit_certificate")

def test_payment_dependent_registration_is_rejected(self) -> None:
    paths = complete_registration_fixture(self.temp_path)
    append_dependency(paths["manifest"], "payment")
    certificate = audit_registration_evidence(paths)
    self.assertTrue(certificate["downstream_recovery_used"])
    self.assertFalse(certificate["registration_recoverable_from_hash"])
```

- [ ] **Step 3: 确认红色失败**

Run: `python3 -m unittest experiments/prime_matrix_mfac_registration_hash_audit_test.py -v`

Expected: FAIL，模块 `prime_matrix_mfac_registration_hash_audit` 尚不存在。

- [ ] **Step 4: 提交测试**

Run: `git add experiments/prime_matrix_mfac_registration_hash_audit_test.py && git commit -m "测试 MFAC registration 哈希审计"`

### Task 2: 最小 evidence 审计器

**Files:**
- Create: `experiments/prime_matrix_mfac_registration_hash_audit.py`
- Modify: `experiments/prime_matrix_mfac_registration_hash_audit_test.py`

- [ ] **Step 1: 固定 registration 判据**

```python
REGISTRATION_FIELDS = (
    "emitter_id",
    "primitive_slot",
    "same_formal_unit_certificate",
)
FORBIDDEN_DEPENDENCIES = {
    "payment", "Gamma", "pushforward_image", "cauchy_output",
    "dispersion_output", "terminal_table", "origin_table",
    "zero_row_coverage", "external_spectral_estimate",
}

def hash_contains_registration_fields(certificate: dict[str, object]) -> bool:
    formulas = "\n".join(
        str(layer.get("formula", ""))
        for layer in certificate.get("hash_layers", [])
        if isinstance(layer, dict)
    )
    return all(field in formulas for field in REGISTRATION_FIELDS)
```

- [ ] **Step 2: 审计显式 manifest registration**

```python
def audit_manifest_registration(payload: dict[str, object]) -> dict[str, object]:
    constructor = payload.get("constructor", {})
    registration = payload.get("registration", {})
    dependencies = set(constructor.get("dependencies", []))
    missing = [field for field in REGISTRATION_FIELDS if not registration.get(field)]
    return {
        "missing_registration_fields": missing,
        "forbidden_dependencies": sorted(dependencies & FORBIDDEN_DEPENDENCIES),
    }
```

- [ ] **Step 3: 合取三类证据**

```python
def audit_registration_evidence(paths: dict[str, Path]) -> dict[str, object]:
    hash_ok = hash_contains_registration_fields(load_json(paths["hash"]))
    table_ok = load_json(paths["source_table"]).get(
        "actual_noncanonical_primitive_emitter_source_table_proved"
    ) is True
    manifests = discover_constructor_manifests(paths["manifest_root"])
    audits = [audit_manifest_registration(payload) for _, payload in manifests]
    valid = [audit for audit in audits if not audit["missing_registration_fields"] and not audit["forbidden_dependencies"]]
    return {"registration_recoverable_from_hash": hash_ok and table_ok and bool(valid)}
```

`earliest_missing_registration_field` 的顺序固定为 `emitter_id`、`primitive_slot`、`same_formal_unit_certificate`；没有 manifest 时为 `emitter_id`。

- [ ] **Step 4: 验证与提交**

Run: `python3 -m unittest experiments/prime_matrix_mfac_registration_hash_audit_test.py -v && git diff --check`

Expected: PASS，4 个测试通过。

Run: `git add experiments/prime_matrix_mfac_registration_hash_audit.py experiments/prime_matrix_mfac_registration_hash_audit_test.py && git commit -m "审计 MFAC registration 哈希缺口"`

### Task 3: 证书、状态与回归

**Files:**
- Modify: `experiments/prime_matrix_mfac_registration_hash_audit.py`
- Create: `docs/monograph/prime-matrix-mfac-registration-hash-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-registration-hash-audit.md`
- Modify: `docs/monograph/claim-status-table.md`

- [ ] **Step 1: 输出当前语料证书**

CLI 必须支持 `--hash`、`--source-table`、`--manifest-root`、`--json-out`、`--md-out`。报告必须写明“当前语料未提交 registration 前向证据”“不表示数学上不可能”，并将下一门写为 `PreCauchyCarrierColoredWordSameFormalUnitSourceRegistrationOrNamedReturn`。

Run: `python3 experiments/prime_matrix_mfac_registration_hash_audit.py`

Expected: `hash_contains_registration_fields=false`、`actual_source_table_constructed=false`、`registration_recoverable_from_hash=false`、`earliest_missing_registration_field=emitter_id`。

- [ ] **Step 2: 同步状态表**

新增行只排除“把 hash 当作 emitter registration”的循环捷径；不得宣称 hash 不可逆、零点排除、`ψ` 误差或 RH。

- [ ] **Step 3: 完整验证与提交**

Run: `python3 -m unittest experiments/prime_matrix_mfac_registration_hash_audit_test.py experiments/prime_matrix_mfac_actual_record_constructor_audit_test.py experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit_test.py experiments/prime_matrix_mfac_colored_divisor_word_transport_audit_test.py experiments/prime_matrix_mfac_square_base_seed_binding_audit_test.py experiments/prime_matrix_mfac_primitive_normalization_underdetermination_audit_test.py -v && git diff --check`

Expected: 全部测试通过且 diff 无空白错误。

Run: `git add experiments/prime_matrix_mfac_registration_hash_audit.py docs/monograph/prime-matrix-mfac-registration-hash-audit.json docs/monograph/prime-matrix-mfac-registration-hash-audit.md docs/monograph/claim-status-table.md && git commit -m "记录 MFAC registration 哈希审计结论"`

## 自审

- 覆盖当前语料负例、合成正例、缺字段、下游泄漏、可重现证书、状态同步与回归。
- 所有路径、字段、断言、命令和预期输出均已固定，无占位符。
- `REGISTRATION_FIELDS` 是 hash、manifest 与聚合结果的唯一三元组定义。
