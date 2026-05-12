#!/usr/bin/env python3
"""生成 strict table_012 theta 极值 runner 前沿证书。

用法示例：
  python3 experiments/prime_matrix_strict_table012_extremal_runner_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table012-extremal-runner-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"

OUT_JSON = DOCS / "prime-matrix-strict-table012-extremal-runner-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table012-extremal-runner-frontier-router.md"

PREVIOUS = DOCS / "prime-matrix-strict-table012-self-contained-frontier-router.json"
RUNNER = ROOT / "experiments" / "prime_matrix_table012_theta_extremal_runner.cpp"
SAMPLE = DATA / "theta-table012-extremal-sample-first-row.jsonl"
PREFIX9 = DATA / "theta-table012-extremal-prefix-9rows.jsonl"
PREFIX18 = DATA / "theta-table012-extremal-prefix-18rows.jsonl"
FULL_ARCHIVE = DATA / "theta-table012-extremal-archive.jsonl"
CLAIM_STATUS = DOCS / "claim-status-table.md"
ARCHIVE_AUDIT = ROOT / "experiments" / "prime_matrix_table012_theta_extremal_archive_audit.py"
SOURCE_FILES = [PREVIOUS, RUNNER, ARCHIVE_AUDIT, SAMPLE, PREFIX9, PREFIX18, FULL_ARCHIVE, CLAIM_STATUS]
FULL_ARCHIVE_ROWS = 34

TABLE012_ATOM = "Table012OriginalGeneratorOrIndependentThetaExtremalArchiveLedger"
RUNNER_ALGO = "Table012ThetaExtremalRunnerAlgorithmLedger"
FIRST_ROW_SAMPLE = "Table012FirstRowExtremalSmokeCertificateLedger"
PREFIX9_LEDGER = "Table012Prefix9RowsTo1e9ArchiveAuditLedger"
PREFIX18_LEDGER = "Table012Prefix18RowsTo1e10ArchiveAuditLedger"
FULL_ARCHIVE_LEDGER = "FullTable012ThetaExtremalArchiveRunAndHashLedger"
LOG_INTERVAL = "CertifiedLogSummationIntervalArithmeticForThetaLedger"
ROUNDING = "Table012DirectedRoundingAndIntervalPropagationLedger"
INDEPENDENT_ARCHIVE = "IndependentThetaExtremalArchiveForTable012IntervalsLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl_single(path: Path) -> dict[str, Any]:
    """读取单行 JSONL 样本。"""
    if not path.exists():
        return {}
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(rows) != 1:
        return {"error": f"expected 1 JSONL row, got {len(rows)}"}
    return rows[0]


def load_jsonl_rows(path: Path) -> list[dict[str, Any]]:
    """读取 JSONL 多行。"""
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def sample_summary(sample: dict[str, Any]) -> dict[str, Any]:
    """抽取第一行样本摘要。"""
    if not sample:
        return {"present": False}
    return {
        "present": True,
        "label": sample.get("label"),
        "left": sample.get("left"),
        "right": sample.get("right"),
        "passed_raw": sample.get("passed_raw"),
        "passed_with_guard": sample.get("passed_with_guard"),
        "raw_margin": sample.get("raw_margin"),
        "margin_after_guard": sample.get("margin_after_guard"),
        "max_x": sample.get("max_x"),
        "max_kind": sample.get("max_kind"),
        "max_required_b1": sample.get("max_required_b1"),
        "b1_minus_max_required_b1": sample.get("b1_minus_max_required_b1"),
        "row_prime_count": sample.get("row_prime_count"),
        "global_prime_count": sample.get("global_prime_count"),
        "sha256": sha256(SAMPLE) if SAMPLE.exists() else None,
    }


def prefix_summary(path: Path, expected_rows: int) -> dict[str, Any]:
    """抽取前缀归档摘要。"""
    rows = load_jsonl_rows(path)
    if not rows:
        return {"present": False, "expected_rows": expected_rows}
    passed = len(rows) == expected_rows and all(item.get("passed_with_guard") is True for item in rows)
    min_guard = min(rows, key=lambda item: float(item["margin_after_guard"]))
    min_raw = min(rows, key=lambda item: float(item["raw_margin"]))
    return {
        "present": True,
        "expected_rows": expected_rows,
        "row_count": len(rows),
        "passed_with_guard": passed,
        "first_label": rows[0].get("label"),
        "last_label": rows[-1].get("label"),
        "last_right": rows[-1].get("right"),
        "min_guard_margin": min_guard.get("margin_after_guard"),
        "min_guard_margin_label": min_guard.get("label"),
        "min_raw_margin": min_raw.get("raw_margin"),
        "min_raw_margin_label": min_raw.get("label"),
        "sha256": sha256(path),
    }


def build_result() -> dict[str, Any]:
    """构造 table_012 极值 runner 前沿证书。"""
    previous = load_json(PREVIOUS)
    sample = load_jsonl_single(SAMPLE)
    sample_info = sample_summary(sample)
    prefix9_info = prefix_summary(PREFIX9, 9)
    prefix18_info = prefix_summary(PREFIX18, 18)
    full_archive_info = prefix_summary(FULL_ARCHIVE, FULL_ARCHIVE_ROWS)
    runner_present = RUNNER.exists()
    audit_present = ARCHIVE_AUDIT.exists()
    sample_passed = sample_info.get("passed_with_guard") is True
    prefix9_passed = prefix9_info.get("passed_with_guard") is True
    prefix18_passed = prefix18_info.get("passed_with_guard") is True
    full_archive_passed = full_archive_info.get("passed_with_guard") is True
    if full_archive_passed:
        status = "table012_full_extremal_archive_closed_interval_arithmetic_open"
        plain_conclusion = (
            "table_012 自足路线继续推进：独立 theta 极值扫描器已经物化，"
            "第一行、前 9 行、前 18 行以及完整 34 行归档均已通过工程审计并登记 hash。"
            "但严格 log 区间舍入仍未闭合；尤其第一行绝对余量只有约 76，"
            "不能把普通浮点/Kahan 归档冒充为最终自足证明。"
        )
        full_remaining = full_archive_info.get("sha256") or "full archive hash missing"
    else:
        status = "table012_extremal_runner_algorithm_and_first_row_sample_closed_full_archive_interval_arithmetic_open"
        plain_conclusion = (
            "table_012 自足路线向前推进了一层：独立 theta 极值扫描器已经物化，"
            "第一行 [1e8,2e8] 样本通过并给出最危险点 p=179845447。"
            "前 9 行与前 18 行前缀归档均已通过审计。"
            "但完整 34 行归档和严格 log 区间舍入仍未闭合；尤其第一行绝对余量只有约 76，"
            "不能把普通浮点样本冒充为最终自足证明。"
        )
        full_remaining = "run /tmp/table012_theta_extremal --max-rows 34 and audit all rows"

    next_target = LOG_INTERVAL if full_archive_passed else FULL_ARCHIVE_LEDGER
    parallel_targets = [LOG_INTERVAL, ROUNDING, DSTRUCTURE]
    if not full_archive_passed:
        parallel_targets = [FULL_ARCHIVE_LEDGER, LOG_INTERVAL, ROUNDING, DSTRUCTURE]

    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            previous.get("counterexample_assumption_only") is True
            and previous.get("row_column_unconditional_closed") is False,
            True,
            "本步只推进 table_012 自足计算输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "Table012SelfContainedFrontierImported",
            previous.get("next_direct_attack_target") == TABLE012_ATOM,
            True,
            "上一证书已把 P5.1 低段自足缺口压成 table_012 原始生成器或独立 theta 极值归档。",
            TABLE012_ATOM,
        ),
        row(
            RUNNER_ALGO,
            runner_present,
            True,
            "已物化独立扫描器：从 theta(1e8) 开始，按 table_012 区间扫描素数跳点并记录最大缺陷。",
            sha256(RUNNER) if runner_present else "runner missing",
        ),
        row(
            FIRST_ROW_SAMPLE,
            sample_passed,
            True,
            "第一行 [1e8,2e8] 样本已跑通；最危险点与余量已落盘，验证极值口径可执行。",
            sample_info.get("sha256") or "sample missing",
        ),
        row(
            "Table012ExtremalArchiveAuditToolLedger",
            audit_present,
            True,
            "已新增归档审计器，检查行数、区间、b1、最大点、原始余量、保护余量和 hash。",
            sha256(ARCHIVE_AUDIT) if audit_present else "audit tool missing",
        ),
        row(
            PREFIX9_LEDGER,
            prefix9_passed,
            True,
            "前 9 行 [1e8,1e9] 已生成并通过归档审计。",
            prefix9_info.get("sha256") or "prefix archive missing",
        ),
        row(
            PREFIX18_LEDGER,
            prefix18_passed,
            True,
            "前 18 行 [1e8,1e10] 已生成并通过归档审计；仍只是完整归档前缀。",
            prefix18_info.get("sha256") or "prefix archive missing",
        ),
        row(
            "ThinFirstRowMarginDetected",
            sample_passed and sample_info.get("raw_margin") is not None,
            True,
            "第一行 published b1 的绝对余量只有约 76，说明后续必须补严格 log 区间舍入纪律。",
            LOG_INTERVAL,
        ),
        row(
            FULL_ARCHIVE_LEDGER,
            full_archive_passed,
            full_archive_passed,
            "完整 34 行极值归档需读满 table_012 全部区间，且每行通过工程保护余量检查并登记 hash。",
            full_remaining,
        ),
        row(
            LOG_INTERVAL,
            False,
            False,
            "当前样本使用 long double/Kahan 与工程保护，不等同于严格外向 log 区间算术证明。",
            "interval log table or directed MPFR/arb-style summation certificate",
        ),
        row(
            INDEPENDENT_ARCHIVE,
            full_archive_passed and False,
            False,
            "独立归档需要完整运行/hash与区间舍入同时闭合；当前仍卡在严格 log 区间舍入。",
            f"{FULL_ARCHIVE_LEDGER} AND {LOG_INTERVAL}",
        ),
        row(
            "DirectUnconditionalContradictionFound",
            False,
            False,
            "本步仍只是解析输入自足化，不产生早期零行反例链终端矛盾。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "行/列命题仍未作者侧无条件闭合。",
            DSTRUCTURE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_table012_extremal_runner_frontier_router",
        "status": status,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "table012_theta_extremal_runner_algorithm_closed": runner_present,
        "table012_extremal_archive_audit_tool_closed": audit_present,
        "table012_first_row_extremal_smoke_certificate_closed": sample_passed,
        "table012_prefix9_rows_to_1e9_archive_audit_closed": prefix9_passed,
        "table012_prefix18_rows_to_1e10_archive_audit_closed": prefix18_passed,
        "full_table012_theta_extremal_archive_run_hash_closed": full_archive_passed,
        "certified_log_summation_interval_arithmetic_closed": False,
        "independent_theta_extremal_archive_closed": False,
        "theta_less_than_identity_to_8e11_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "sample_first_row": sample_info,
        "prefix9_archive": prefix9_info,
        "prefix18_archive": prefix18_info,
        "full_archive": full_archive_info,
        "source_hashes": source_hashes(),
        "replacement_self_contained": {
            INDEPENDENT_ARCHIVE: f"{FULL_ARCHIVE_LEDGER} AND {LOG_INTERVAL} AND {ROUNDING}",
            TABLE012_ATOM: f"PublishedTable012GeneratorArtifactAndHashLedger OR {INDEPENDENT_ARCHIVE}",
        },
        "next_direct_attack_target": next_target,
        "parallel_attack_targets": parallel_targets,
        "plain_conclusion": plain_conclusion,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    sample = result["sample_first_row"]
    lines = [
        "# Prime Matrix strict table_012 theta 极值 runner 前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"table012_theta_extremal_runner_algorithm_closed={fmt_bool(result['table012_theta_extremal_runner_algorithm_closed'])}",
        f"table012_extremal_archive_audit_tool_closed={fmt_bool(result['table012_extremal_archive_audit_tool_closed'])}",
        f"table012_first_row_extremal_smoke_certificate_closed={fmt_bool(result['table012_first_row_extremal_smoke_certificate_closed'])}",
        f"table012_prefix9_rows_to_1e9_archive_audit_closed={fmt_bool(result['table012_prefix9_rows_to_1e9_archive_audit_closed'])}",
        f"table012_prefix18_rows_to_1e10_archive_audit_closed={fmt_bool(result['table012_prefix18_rows_to_1e10_archive_audit_closed'])}",
        f"full_table012_theta_extremal_archive_run_hash_closed={fmt_bool(result['full_table012_theta_extremal_archive_run_hash_closed'])}",
        f"certified_log_summation_interval_arithmetic_closed={fmt_bool(result['certified_log_summation_interval_arithmetic_closed'])}",
        f"theta_less_than_identity_to_8e11_self_contained_closed={fmt_bool(result['theta_less_than_identity_to_8e11_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 第一行样本",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key in [
        "label",
        "left",
        "right",
        "passed_raw",
        "passed_with_guard",
        "raw_margin",
        "margin_after_guard",
        "max_x",
        "max_kind",
        "max_required_b1",
        "b1_minus_max_required_b1",
        "row_prime_count",
        "global_prime_count",
        "sha256",
    ]:
        lines.append(f"| `{key}` | `{table_cell(sample.get(key))}` |")
    lines.extend(
        [
            "",
        "## 2. 前缀归档",
        "",
        "| archive | closed | rows | last_right | min_guard_margin | min_guard_label | sha256 |",
        "| --- | --- | ---: | ---: | ---: | --- | --- |",
        "| `prefix9` | `{}` | `{}` | `{}` | `{}` | `{}` | `{}` |".format(
            fmt_bool(result["prefix9_archive"].get("passed_with_guard")),
            table_cell(result["prefix9_archive"].get("row_count")),
            table_cell(result["prefix9_archive"].get("last_right")),
            table_cell(result["prefix9_archive"].get("min_guard_margin")),
            table_cell(result["prefix9_archive"].get("min_guard_margin_label")),
            table_cell(result["prefix9_archive"].get("sha256")),
        ),
        "| `prefix18` | `{}` | `{}` | `{}` | `{}` | `{}` | `{}` |".format(
            fmt_bool(result["prefix18_archive"].get("passed_with_guard")),
            table_cell(result["prefix18_archive"].get("row_count")),
            table_cell(result["prefix18_archive"].get("last_right")),
            table_cell(result["prefix18_archive"].get("min_guard_margin")),
            table_cell(result["prefix18_archive"].get("min_guard_margin_label")),
            table_cell(result["prefix18_archive"].get("sha256")),
        ),
        "| `full34` | `{}` | `{}` | `{}` | `{}` | `{}` | `{}` |".format(
            fmt_bool(result["full_archive"].get("passed_with_guard")),
            table_cell(result["full_archive"].get("row_count")),
            table_cell(result["full_archive"].get("last_right")),
            table_cell(result["full_archive"].get("min_guard_margin")),
            table_cell(result["full_archive"].get("min_guard_margin_label")),
            table_cell(result["full_archive"].get("sha256")),
        ),
        "",
        "## 3. 自足替换",
            "",
            "```text",
            f"{INDEPENDENT_ARCHIVE}",
            "  =>",
            result["replacement_self_contained"][INDEPENDENT_ARCHIVE],
            "",
            f"{TABLE012_ATOM}",
            "  =>",
            result["replacement_self_contained"][TABLE012_ATOM],
            "```",
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(
        "table012_first_row_extremal_smoke_certificate_closed="
        f"{fmt_bool(result['table012_first_row_extremal_smoke_certificate_closed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
