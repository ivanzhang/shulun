"""生成 MFAC 审计模块的保守项目库存。"""

import argparse
import json
from pathlib import Path
from typing import Mapping


DEFAULT_JSON = Path("docs/monograph/prime-matrix-mfac-project-inventory-audit.json")
DEFAULT_MARKDOWN = Path("docs/monograph/prime-matrix-mfac-project-inventory-audit.md")


OPEN_MARKERS = ("open", "unproved", "unresolved", "not_closed")
CONDITIONAL_MARKERS = ("conditional", "external", "assumed")


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
                    f"docs/monograph/prime-matrix-mfac-"
                    f"{module_name.replace('_', '-')}-audit.json"
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


def classify_certificate(
    payload: dict[str, object] | None, error: str | None
) -> tuple[str, tuple[str, ...]]:
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
    rh_proved = payload.get("rh_proved")
    if type(rh_proved) is not bool:
        return "open_or_unresolved", ("rh_proved_missing_or_invalid",)
    if rh_proved is False or any(
        marker in status_text for marker in OPEN_MARKERS
    ):
        return "open_or_unresolved", ("rh_not_proved_or_open_marker",)
    if rh_proved is True:
        return "requires_manual_rh_review", ("unverified_rh_proved_claim",)
    return "finite_verified_only", ("no_machine_checkable_rh_closure",)


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
                    key: value
                    for key, value in (payload or {}).items()
                    if key == "status" or "status" in key
                },
                "classification": classification,
                "rh_blockers": blockers,
            }
        )
    classification_counts: dict[str, int] = {}
    for record in modules:
        classification = record["classification"]
        classification_counts[classification] = (
            classification_counts.get(classification, 0) + 1
        )
    return {
        "certificate_type": "prime_matrix_mfac_project_inventory_audit",
        "inventory_status": "conservative_index_only",
        "module_count": len(modules),
        "classification_counts": dict(sorted(classification_counts.items())),
        "modules": modules,
        "rh_proved": False,
        "rh_closed_module_count": 0,
    }


def render_markdown(certificate: Mapping[str, object]) -> str:
    """将保守库存渲染为可人工审阅的 Markdown。"""
    lines = [
        "# MFAC 全项目保守库存审计",
        "",
        f"- 模块总数：`{certificate['module_count']}`",
        "- 库存状态：`conservative_index_only`",
        "- `rh_proved=false`",
        "- `rh_closed_module_count=0`",
        "",
        "## 分类汇总",
        "",
    ]
    for classification, count in certificate["classification_counts"].items():
        lines.append(f"- `{classification}`：`{count}`")
    lines.extend(
        [
            "",
            "## 模块索引",
            "",
            "| 模块 | 分类 | 证书 | RH 阻断理由 |",
            "| --- | --- | --- | --- |",
        ]
    )
    for module in certificate["modules"]:
        blockers = ", ".join(module["rh_blockers"])
        lines.append(
            f"| `{module['module_name']}` | `{module['classification']}` | "
            f"`{module['certificate_available']}` | `{blockers}` |"
        )
    lines.extend(
        [
            "",
            "该库存只索引已有 JSON 顶层字段，不导入或执行模块；不构成 RH 证明。",
            "",
        ]
    )
    return "\n".join(lines)


def write_certificate(
    certificate: Mapping[str, object], json_path: Path, markdown_path: Path
) -> None:
    """写出机器可读和人工可读的保守库存证书。"""
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(render_markdown(certificate), encoding="utf-8")


def main() -> None:
    """生成 MFAC 全项目保守库存证书。"""
    parser = argparse.ArgumentParser(description="生成 MFAC 全项目保守库存审计")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    certificate = build_inventory(args.repo_root.resolve())
    write_certificate(certificate, args.json_out, args.markdown_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.markdown_out}")


if __name__ == "__main__":
    main()
