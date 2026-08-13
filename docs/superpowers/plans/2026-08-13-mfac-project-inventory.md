# MFAC 全项目保守库存审计实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development（推荐）或 superpowers:executing-plans 逐任务执行。本计划用 checkbox（`- [ ]`）跟踪步骤。

**Goal:** 生成可复现的全项目 MFAC 模块/证书索引，并以保守规则标注 RH 阻断理由，而不从文本或有限证据推断 RH 闭合。

**Architecture:** 新扫描器只枚举 `experiments/prime_matrix_mfac_*_audit.py`，按照确定性 stem 变换匹配 `docs/monograph/prime-matrix-mfac-*-audit.json`。它仅读取顶层 JSON 字段，按固定优先级分类；JSON/Markdown 证书保持 `rh_proved=false`，即使单个输入声称 `true` 也只进入人工复核。

**Tech Stack:** Python 3 标准库（`argparse`、`json`、`pathlib`、`typing`、`unittest`、`tempfile`、`subprocess`）；现有 `experiments/` 和 `docs/monograph/` 证书约定。

**Design Source:** `docs/superpowers/specs/2026-08-13-mfac-project-inventory-design.md`

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_project_inventory_audit.py`
  - 确定性模块发现、证书读取、保守分类、渲染和 CLI。
- Create: `experiments/prime_matrix_mfac_project_inventory_audit_test.py`
  - 临时文件树的路径匹配、分类、RH 边界和 CLI 测试。
- Create: `docs/monograph/prime-matrix-mfac-project-inventory-audit.json`
  - 当前仓库的机器可读 MFAC 库存。
- Create: `docs/monograph/prime-matrix-mfac-project-inventory-audit.md`
  - 当前仓库的人读库存和分类汇总。

不修改任何已有 MFAC 审计器或既有证书；不导入/执行被扫描模块；阶段完成后只提交本计划列出的四个新文件以及本规格和本计划，且不得把用户已有未提交文件混入暂存区。

### Task 1: 写出模块发现与路径匹配红灯测试

**Files:**
- Create: `experiments/prime_matrix_mfac_project_inventory_audit_test.py`

- [ ] **Step 1: 在临时树写出确定性发现测试**

```python
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from experiments.prime_matrix_mfac_project_inventory_audit import discover_modules


class MFACProjectInventoryAuditTest(unittest.TestCase):
    """验证 MFAC 模块库存的保守索引规则。"""

    def test_discover_modules_matches_sorted_expected_json_paths(self) -> None:
        """模块 stem 必须稳定映射到预期 JSON 证书路径。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            experiments = root / "experiments"
            monograph = root / "docs" / "monograph"
            experiments.mkdir(parents=True)
            monograph.mkdir(parents=True)
            (experiments / "prime_matrix_mfac_zeta_audit.py").write_text("", encoding="utf-8")
            (experiments / "prime_matrix_mfac_alpha_audit.py").write_text("", encoding="utf-8")

            records = discover_modules(root)

            self.assertEqual([record["module_name"] for record in records], ["alpha", "zeta"])
            self.assertEqual(
                records[0]["certificate_path"],
                "docs/monograph/prime-matrix-mfac-alpha-audit.json",
            )
```

- [ ] **Step 2: 运行测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_project_inventory_audit_test.MFACProjectInventoryAuditTest.test_discover_modules_matches_sorted_expected_json_paths -v`

Expected: FAIL，原因是扫描模块尚不存在。

### Task 2: 实现发现、只读加载与保守分类

**Files:**
- Create: `experiments/prime_matrix_mfac_project_inventory_audit.py`
- Modify: `experiments/prime_matrix_mfac_project_inventory_audit_test.py`

- [ ] **Step 1: 实现确定性发现与 JSON 读取**

```python
from pathlib import Path
import json


def discover_modules(repo_root: Path) -> list[dict[str, str]]:
    """按字典序发现 MFAC 审计模块及其预期 JSON 证书。"""
    prefix = "prime_matrix_mfac_"
    suffix = "_audit.py"
    records = []
    for module_path in sorted((repo_root / "experiments").glob(f"{prefix}*{suffix}")):
        module_name = module_path.name.removeprefix(prefix).removesuffix(suffix)
        records.append(
            {
                "module_name": module_name,
                "module_path": module_path.relative_to(repo_root).as_posix(),
                "certificate_path": (
                    f"docs/monograph/prime-matrix-mfac-{module_name.replace('_', '-')}-audit.json"
                ),
            }
        )
    return records


def _load_certificate(path: Path) -> tuple[dict[str, object] | None, str | None]:
    """只读取顶层 JSON object，并把失败原因交给保守分类。"""
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        return None, type(error).__name__
    if not isinstance(payload, dict):
        return None, "top_level_not_object"
    return payload, None
```

- [ ] **Step 2: 实现关键词提取和固定优先级分类**

```python
OPEN_MARKERS = ("open", "unproved", "unresolved", "not_closed")
CONDITIONAL_MARKERS = ("conditional", "external", "assumed")


def classify_certificate(payload: dict[str, object] | None, error: str | None) -> tuple[str, tuple[str, ...]]:
    """按缺失、条件、开放、有限、人工 RH 复核的优先级保守分类。"""
    if payload is None:
        return "missing_or_unreadable_certificate", (error or "missing",)
    status_text = " ".join(
        f"{key}={value}".lower()
        for key, value in payload.items()
        if key == "status" or "status" in key or isinstance(value, str)
    )
    if any(marker in status_text for marker in CONDITIONAL_MARKERS):
        return "conditional_or_external_dependency", ("conditional_or_external_marker",)
    if payload.get("rh_proved") is False or any(marker in status_text for marker in OPEN_MARKERS):
        return "open_or_unresolved", ("rh_not_proved_or_open_marker",)
    if payload.get("rh_proved") is True:
        return "requires_manual_rh_review", ("unverified_rh_proved_claim",)
    return "finite_verified_only", ("no_machine_checkable_rh_closure",)
```

- [ ] **Step 3: 运行 Task 1 测试确认通过**

Run: `python3 -m unittest experiments.prime_matrix_mfac_project_inventory_audit_test -v`

Expected: PASS。

### Task 3: 写出保守边界与坏证书红灯测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_project_inventory_audit_test.py`

- [ ] **Step 1: 添加合成证书的分类与顶层 RH 边界测试**

```python
    def test_inventory_keeps_false_rh_for_open_conditional_and_claimed_true_inputs(self) -> None:
        """任何输入组合都不得把库存顶层升级为 RH 闭合。"""
        from experiments.prime_matrix_mfac_project_inventory_audit import build_inventory

        with TemporaryDirectory() as directory:
            root = Path(directory)
            experiments = root / "experiments"
            monograph = root / "docs" / "monograph"
            experiments.mkdir(parents=True)
            monograph.mkdir(parents=True)
            for name in ("conditional", "open", "claimed_true", "missing"):
                (experiments / f"prime_matrix_mfac_{name}_audit.py").write_text("", encoding="utf-8")
            (monograph / "prime-matrix-mfac-conditional-audit.json").write_text(
                '{"status":"conditional_external_input","rh_proved":false}', encoding="utf-8"
            )
            (monograph / "prime-matrix-mfac-open-audit.json").write_text(
                '{"l2_upper_status":"unproved","rh_proved":false}', encoding="utf-8"
            )
            (monograph / "prime-matrix-mfac-claimed-true-audit.json").write_text(
                '{"rh_proved":true}', encoding="utf-8"
            )

            inventory = build_inventory(root)

            self.assertFalse(inventory["rh_proved"])
            self.assertEqual(inventory["rh_closed_module_count"], 0)
            self.assertEqual(inventory["classification_counts"]["missing_or_unreadable_certificate"], 1)
            by_name = {record["module_name"]: record for record in inventory["modules"]}
            self.assertEqual(by_name["conditional"]["classification"], "conditional_or_external_dependency")
            self.assertEqual(by_name["open"]["classification"], "open_or_unresolved")
            self.assertEqual(by_name["claimed_true"]["classification"], "requires_manual_rh_review")
```

- [ ] **Step 2: 运行新增测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_project_inventory_audit_test.MFACProjectInventoryAuditTest.test_inventory_keeps_false_rh_for_open_conditional_and_claimed_true_inputs -v`

Expected: FAIL，原因是 `build_inventory` 尚未实现。

### Task 4: 实现库存证书、渲染和 CLI

**Files:**
- Modify: `experiments/prime_matrix_mfac_project_inventory_audit.py`
- Modify: `experiments/prime_matrix_mfac_project_inventory_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-project-inventory-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-project-inventory-audit.md`

- [ ] **Step 1: 实现库存构造与证书写出**

```python
from collections import Counter


def build_inventory(repo_root: Path) -> dict[str, object]:
    """构造全项目保守索引，顶层永远不认证 RH。"""
    modules = []
    for record in discover_modules(repo_root):
        payload, error = _load_certificate(repo_root / record["certificate_path"])
        classification, blockers = classify_certificate(payload, error)
        modules.append(
            {
                **record,
                "certificate_available": payload is not None,
                "rh_proved_field": payload.get("rh_proved") if payload else None,
                "status_fields": {
                    key: value for key, value in (payload or {}).items() if key == "status" or "status" in key
                },
                "classification": classification,
                "rh_blockers": blockers,
            }
        )
    counts = Counter(record["classification"] for record in modules)
    return {
        "certificate_type": "prime_matrix_mfac_project_inventory_audit",
        "inventory_status": "conservative_index_only",
        "module_count": len(modules),
        "classification_counts": dict(sorted(counts.items())),
        "modules": modules,
        "rh_proved": False,
        "rh_closed_module_count": 0,
    }
```

实现 `render_markdown` 与 `write_certificate`：表格逐行显示模块、分类、证书状态和 RH 阻断理由；文末固定写明“库存只索引已有字段，不执行模块，也不构成 RH 证明”。

- [ ] **Step 2: 实现 CLI 并生成默认产物**

```python
DEFAULT_JSON = Path("docs/monograph/prime-matrix-mfac-project-inventory-audit.json")
DEFAULT_MARKDOWN = Path("docs/monograph/prime-matrix-mfac-project-inventory-audit.md")


def main() -> None:
    """生成 MFAC 全项目保守库存证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC 全项目保守库存审计")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    certificate = build_inventory(args.repo_root.resolve())
    write_certificate(certificate, args.json_out, args.markdown_out)
```

- [ ] **Step 3: 添加 CLI/坏 JSON 测试并运行模块测试**

```python
    def test_cli_writes_inventory_and_bad_json_stays_unreadable(self) -> None:
        """CLI 必须可执行，坏 JSON 必须保守登记而非崩溃或推断。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "experiments").mkdir()
            monograph = root / "docs" / "monograph"
            monograph.mkdir(parents=True)
            (root / "experiments" / "prime_matrix_mfac_bad_audit.py").write_text("", encoding="utf-8")
            (monograph / "prime-matrix-mfac-bad-audit.json").write_text("{", encoding="utf-8")
            certificate = build_inventory(root)
            self.assertEqual(certificate["modules"][0]["classification"], "missing_or_unreadable_certificate")
```

Run: `python3 -m unittest experiments.prime_matrix_mfac_project_inventory_audit_test -v`

Expected: PASS，且测试中所有顶层 `rh_proved` 都为 `false`。

### Task 5: 生成库存、验证并提交阶段 1

**Files:**
- Create: `docs/monograph/prime-matrix-mfac-project-inventory-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-project-inventory-audit.md`

- [ ] **Step 1: 生成默认库存并检查保守顶层字段**

Run:

```bash
python3 experiments/prime_matrix_mfac_project_inventory_audit.py --repo-root .
python3 - <<'PY'
import json
from pathlib import Path
payload = json.loads(Path("docs/monograph/prime-matrix-mfac-project-inventory-audit.json").read_text())
assert payload["inventory_status"] == "conservative_index_only"
assert payload["rh_proved"] is False
assert payload["rh_closed_module_count"] == 0
assert payload["module_count"] == len(payload["modules"])
PY
```

Expected: 默认 JSON/Markdown 存在，且无论扫描到何种证书声明，库存不认证 RH。

- [ ] **Step 2: 运行新测试和全量 MFAC 回归**

Run:

```bash
python3 -m unittest experiments.prime_matrix_mfac_project_inventory_audit_test -v
python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v
git diff --check
```

Expected: 新测试和全量 MFAC 测试通过；差异检查无输出。

- [ ] **Step 3: 仅提交阶段 1 文件**

Run:

```bash
git add \
  docs/superpowers/specs/2026-08-13-mfac-project-inventory-design.md \
  docs/superpowers/plans/2026-08-13-mfac-project-inventory.md \
  experiments/prime_matrix_mfac_project_inventory_audit.py \
  experiments/prime_matrix_mfac_project_inventory_audit_test.py \
  docs/monograph/prime-matrix-mfac-project-inventory-audit.json \
  docs/monograph/prime-matrix-mfac-project-inventory-audit.md
git commit -m "审计 MFAC 全项目保守库存"
```

Expected: 提交只包含阶段 1 的规格、计划、模块、测试和库存证书；`AGENTS.md` 及用户原有未提交文件绝不进入暂存区。

## 计划自检

- **规格覆盖：** Task 1--2 覆盖扫描范围、确定性匹配和只读 JSON；Task 3--4 覆盖优先级分类、顶层 RH 边界、Markdown/CLI；Task 5 覆盖默认产物、回归与阶段提交。
- **保守性：** `rh_proved=true` 仅进入 `requires_manual_rh_review`；任何输入都不输出 `rh_closed` 或顶层 RH 成立。
- **范围控制：** 不导入或执行被扫描模块，不读取 Markdown/源代码/Git 历史推断状态，不修改已有证书。
- **占位符检查：** 本计划不含 `TBD`、`TODO`、未定义接口或泛化的“适当处理”步骤。
