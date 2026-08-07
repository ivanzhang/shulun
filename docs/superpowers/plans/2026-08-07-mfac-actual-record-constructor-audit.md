# MFAC Actual Record Constructor Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 生成一个可重复的审计证书，区分 schema/router 元数据闭合与从假设 witness 到 actual noncanonical atomic source record 的前向构造，并给出首个缺失字段。

**Architecture:** 新脚本只读取机器可读证书和已登记构造器 manifest；它不会从 `closed/proved` 布尔值推断构造器存在。审计器将 constructor、record、禁止下游依赖和 branch-alphabet 定义域拆开检查，并以当前语料的负例及一个临时合成的完整 manifest 验证判据。

**Tech Stack:** Python 3 标准库（`argparse`、`json`、`pathlib`、`unittest`），现有 monograph JSON/Markdown 证书格式。

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_actual_record_constructor_audit.py` — 发现 manifest、校验构造器与 record 字段、生成 JSON/Markdown 证书。
- Create: `experiments/prime_matrix_mfac_actual_record_constructor_audit_test.py` — 当前语料负例、完整合成 manifest 正例、下游依赖拒绝测试。
- Create: `docs/monograph/prime-matrix-mfac-actual-record-constructor-audit.json` — 当前语料的机器可读审计证书。
- Create: `docs/monograph/prime-matrix-mfac-actual-record-constructor-audit.md` — 当前语料的人工可读审计结论。
- Modify: `docs/monograph/claim-status-table.md` — 登记该审计的边界与下一个数学门。

### Task 1: 先建立审计判据与红色测试

**Files:**
- Create: `experiments/prime_matrix_mfac_actual_record_constructor_audit_test.py`
- Create: `experiments/prime_matrix_mfac_actual_record_constructor_audit.py`

- [ ] **Step 1: 写入失败测试，固定当前语料与完整 manifest 的边界**

```python
from prime_matrix_mfac_actual_record_constructor_audit import (
    audit_constructor_evidence,
    complete_manifest,
)


def test_current_corpus_has_no_actual_atomic_constructor() -> None:
    certificate = audit_constructor_evidence(DOCS / "monograph")
    assert certificate["witness_to_record_constructor_present"] is False
    assert certificate["actual_noncanonical_atomic_record_present"] is False
    assert certificate["earliest_missing_field"] == "origin_selector"
    assert certificate["branch_alphabet_domain_defined"] is False


def test_complete_synthetic_manifest_defines_branch_alphabet(tmp_path: Path) -> None:
    (tmp_path / "complete.json").write_text(json.dumps(complete_manifest()))
    certificate = audit_constructor_evidence(tmp_path)
    assert certificate["witness_to_record_constructor_present"] is True
    assert certificate["actual_noncanonical_atomic_record_present"] is True
    assert certificate["branch_alphabet_domain_defined"] is True
```

- [ ] **Step 2: 运行测试，确认模块尚不存在**

Run:

```bash
python3 -m unittest experiments/prime_matrix_mfac_actual_record_constructor_audit_test.py -v
```

Expected: FAIL，原因是 `prime_matrix_mfac_actual_record_constructor_audit` 尚不存在。

- [ ] **Step 3: 提交红色测试**

```bash
git add experiments/prime_matrix_mfac_actual_record_constructor_audit_test.py
git commit -m "测试 MFAC 实际记录构造审计"
```

### Task 2: 实现最小非循环 evidence 审计器

**Files:**
- Create: `experiments/prime_matrix_mfac_actual_record_constructor_audit.py`
- Modify: `experiments/prime_matrix_mfac_actual_record_constructor_audit_test.py`

- [ ] **Step 1: 定义严格字段集与 manifest 发现规则**

```python
REQUIRED_RECORD_FIELDS = (
    "witness_id", "formal_unit_id", "source_family_id", "origin_selector",
    "source_class", "pre_cauchy_timestamp", "basis_word", "divisor_history",
    "branch_key", "orientation", "local_factor", "signed_coefficient",
    "exact_u", "exact_v", "row_key", "named_return",
)
FORBIDDEN_DEPENDENCIES = {
    "payment", "Gamma", "pushforward_image", "cauchy_output",
    "dispersion_output", "terminal_table", "origin_table",
    "zero_row_coverage", "external_spectral_estimate",
}


def is_constructor_manifest(payload: dict[str, object]) -> bool:
    return payload.get("certificate_type") == (
        "prime_matrix_actual_noncanonical_atomic_record_constructor"
    )
```

- [ ] **Step 2: 实现逐 manifest 审计，不接受布尔路由替代**

```python
def audit_manifest(payload: dict[str, object], path: Path) -> dict[str, object]:
    constructor = payload.get("constructor", {})
    records = payload.get("atomic_records", [])
    witness_inputs = constructor.get("witness_input_fields", [])
    dependencies = set(constructor.get("dependencies", []))
    return {
        "path": str(path),
        "witness_constructor": bool(witness_inputs),
        "forbidden_dependency": sorted(dependencies & FORBIDDEN_DEPENDENCIES),
        "records": [audit_record(record) for record in records],
    }


def audit_record(record: dict[str, object]) -> dict[str, object]:
    missing = [field for field in REQUIRED_RECORD_FIELDS if field not in record]
    actual_noncanonical = record.get("source_class") == "actual_noncanonical"
    return {"missing_fields": missing, "actual_noncanonical": actual_noncanonical}
```

- [ ] **Step 3: 聚合当前语料结果，并以最早字段顺序给出负面证书**

```python
def audit_constructor_evidence(root: Path) -> dict[str, object]:
    manifests = discover_manifests(root)
    audits = [audit_manifest(payload, path) for path, payload in manifests]
    valid = [audit for audit in audits if audit["witness_constructor"]]
    atomic = [record for audit in valid for record in audit["records"]
              if not record["missing_fields"] and record["actual_noncanonical"]]
    return {
        "witness_to_record_constructor_present": bool(valid),
        "actual_noncanonical_atomic_record_present": bool(atomic),
        "earliest_missing_field": earliest_missing_field(audits),
        "branch_alphabet_domain_defined": bool(atomic),
        "downstream_recovery_used": any(audit["forbidden_dependency"] for audit in audits),
    }
```

`earliest_missing_field` 必须在没有任何 manifest 或没有 record 时返回 `origin_selector`，因为 schema 字段在此之前只标识 formal unit/source family，未前向选择 primitive origin。

- [ ] **Step 4: 增加禁止下游依赖的失败断言并运行测试**

```python
def test_manifest_using_payment_is_rejected(tmp_path: Path) -> None:
    payload = complete_manifest()
    payload["constructor"]["dependencies"].append("payment")
    (tmp_path / "leak.json").write_text(json.dumps(payload))
    certificate = audit_constructor_evidence(tmp_path)
    assert certificate["actual_noncanonical_atomic_record_present"] is False
    assert certificate["downstream_recovery_used"] is True
```

Run:

```bash
python3 -m unittest experiments/prime_matrix_mfac_actual_record_constructor_audit_test.py -v
```

Expected: PASS，3 个测试通过。

- [ ] **Step 5: 提交最小审计器**

```bash
git add experiments/prime_matrix_mfac_actual_record_constructor_audit.py \
  experiments/prime_matrix_mfac_actual_record_constructor_audit_test.py
git commit -m "审计 MFAC 实际原子记录构造缺口"
```

### Task 3: 生成证书并同步状态表

**Files:**
- Modify: `experiments/prime_matrix_mfac_actual_record_constructor_audit.py`
- Create: `docs/monograph/prime-matrix-mfac-actual-record-constructor-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-actual-record-constructor-audit.md`
- Modify: `docs/monograph/claim-status-table.md`

- [ ] **Step 1: 添加 CLI 输出与 Markdown 渲染**

```python
parser.add_argument(
    "--root", type=Path, default=ROOT / "docs" / "monograph"
)
parser.add_argument("--json-out", type=Path, default=DOCS / f"{SLUG}.json")
parser.add_argument("--md-out", type=Path, default=DOCS / f"{SLUG}.md")
```

Markdown 必须明确写出：该结果表示“当前语料未提交构造器证据”，不是实际数学上的不可能性；不得出现 RH 已证或数值反例存在的表述。

- [ ] **Step 2: 运行审计器生成当前语料证书**

Run:

```bash
python3 experiments/prime_matrix_mfac_actual_record_constructor_audit.py
```

Expected: JSON/Markdown 均写入 `docs/monograph/`，且包含：

```text
witness_to_record_constructor_present=false
actual_noncanonical_atomic_record_present=false
earliest_missing_field=origin_selector
branch_alphabet_domain_defined=false
```

- [ ] **Step 3: 在状态表添加边界明确的一行**

新增内容必须说明：该审计否定的是“schema/router 已足以定义 actual atomic record”的说法；下一门是 `PreCauchyActualNoncanonicalAtomicRecordConstructorOrNamedReturn`；未推出 RH、psi 误差或零点排除。

- [ ] **Step 4: 运行完整验证**

Run:

```bash
python3 -m unittest \
  experiments/prime_matrix_mfac_actual_record_constructor_audit_test.py \
  experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit_test.py \
  experiments/prime_matrix_mfac_colored_divisor_word_transport_audit_test.py \
  experiments/prime_matrix_mfac_square_base_seed_binding_audit_test.py \
  experiments/prime_matrix_mfac_primitive_normalization_underdetermination_audit_test.py -v
git diff --check
```

Expected: 全部通过且 diff 无空白错误。

- [ ] **Step 5: 提交证书与文档**

```bash
git add experiments/prime_matrix_mfac_actual_record_constructor_audit.py \
  docs/monograph/prime-matrix-mfac-actual-record-constructor-audit.json \
  docs/monograph/prime-matrix-mfac-actual-record-constructor-audit.md \
  docs/monograph/claim-status-table.md
git commit -m "记录 MFAC 实际原子来源构造缺口"
```

## 自审

- 覆盖性：三个任务分别覆盖判据、当前语料审计、合成正例、下游泄漏、证书与状态同步。
- 无占位符：所有创建文件、函数名、断言、命令与预期结果均已明确。
- 类型一致性：manifest 使用 `constructor` 与 `atomic_records`；record 字段由 `REQUIRED_RECORD_FIELDS` 统一定义；所有聚合输出均来自 `audit_constructor_evidence`。
