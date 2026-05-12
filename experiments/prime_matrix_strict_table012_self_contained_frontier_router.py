#!/usr/bin/env python3
"""生成 strict table_012 自足前沿下钻路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_table012_self_contained_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table012-self-contained-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 60

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"

OUT_JSON = DOCS / "prime-matrix-strict-table012-self-contained-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table012-self-contained-frontier-router.md"

THETA_8E11 = DOCS / "prime-matrix-strict-theta-less-than-identity-to-8e11-router.json"
P51_SYNC = DOCS / "prime-matrix-strict-dusart-p51-theta-upper-full-sync-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SOURCE_FILES = [THETA_8E11, P51_SYNC, CLAIM_STATUS]

DUSART_SOURCE = Path("/tmp/Estimates2.tex")

TARGET = "ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger"
TABLE012_ATOM = "Table012OriginalGeneratorOrIndependentThetaExtremalArchiveLedger"
GENERATOR = "PublishedTable012GeneratorArtifactAndHashLedger"
EXTREMAL = "IndependentThetaExtremalArchiveForTable012IntervalsLedger"
ROUNDING = "Table012DirectedRoundingAndIntervalPropagationLedger"
P51_SELF = "DusartP51ThetaUpperFullSelfContainedLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SMALL_LIMIT = Decimal("1e8")
TABLE_LIMIT = Decimal("8e11")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记仓库内依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def external_source_payload() -> dict[str, Any]:
    """定位 Dusart 源文件中的 table_012 边界。"""
    if not DUSART_SOURCE.exists():
        return {
            "available": False,
            "path": str(DUSART_SOURCE),
            "sha256": None,
            "table_012_label_found": False,
            "commented_input_reference_found": False,
            "interval_rule_found": False,
            "deleglise_rivat_dependency_found": False,
        }
    text = DUSART_SOURCE.read_text(encoding="utf-8", errors="replace")
    return {
        "available": True,
        "path": str(DUSART_SOURCE),
        "sha256": sha256(DUSART_SOURCE),
        "table_012_label_found": "\\label{table_012}" in text,
        "commented_input_reference_found": "theta_pk/tables/table_012.tex" in text,
        "interval_rule_found": "n\\cdot10^k\\leqs x\\leqs (n+1)\\cdot10^k" in text
        and "x+b_1 \\frac{x}{\\ln x}" in text,
        "deleglise_rivat_dependency_found": "deleglise:psi" in text and "exact values of $\\psi(x)$" in text,
    }


def repo_artifact_payload() -> dict[str, Any]:
    """检查仓库中是否已有 table_012 原始生成器或极值归档。"""
    candidate_paths = [
        ROOT / "theta_pk" / "tables" / "table_012.tex",
        ROOT / "data" / "table_012.jsonl",
        ROOT / "data" / "theta-table012-extremal-archive.jsonl",
        ROOT / "data" / "theta-table012-extremal-archive.json",
    ]
    existing = [path for path in candidate_paths if path.exists()]
    return {
        "candidate_paths": [str(path.relative_to(ROOT)) for path in candidate_paths],
        "existing_candidate_paths": [str(path.relative_to(ROOT)) for path in existing],
        "published_generator_artifact_present_in_repo": (ROOT / "theta_pk" / "tables" / "table_012.tex").exists(),
        "independent_extremal_archive_present": any(path.exists() for path in candidate_paths[1:]),
        "middle_psi_archive_present_but_wrong_scope": (DATA / "middle-psi-fine-mesh-node-table.jsonl").exists(),
    }


def scale_payload(theta_cert: dict[str, Any]) -> dict[str, Any]:
    """给出独立重算路线的规模边界；仅用于工程量定位，不作为数学证明。"""
    audit = theta_cert.get("dusart_table012_audit", {})
    width = TABLE_LIMIT - SMALL_LIMIT
    estimate = TABLE_LIMIT / TABLE_LIMIT.ln()
    worst = audit.get("worst_relative_margin_row", {})
    return {
        "interval_count": audit.get("interval_count"),
        "range_width_integer_count": str(width),
        "prime_jump_count_scale_estimate_x_over_logx": str(estimate),
        "scale_estimate_is_not_a_proof_input": True,
        "worst_published_margin_label": worst.get("label"),
        "worst_published_margin_right": worst.get("right"),
        "worst_published_relative_margin": worst.get("relative_margin_at_right"),
    }


def proof_obligations(source: dict[str, Any], artifacts: dict[str, Any], theta_cert: dict[str, Any]) -> list[dict[str, Any]]:
    """列出 table_012 自足化必须补齐的原子账本。"""
    audit = theta_cert.get("dusart_table012_audit", {})
    transcription_closed = (
        theta_cert.get("dusart_table012_negative_b1_cover_closed") is True
        and audit.get("continuous_cover_from_1e8_to_8e11") is True
        and audit.get("all_b1_negative") is True
    )
    return [
        {
            "name": "Table012StatementAndIntervalRuleLedger",
            "closed": source["table_012_label_found"] and source["interval_rule_found"],
            "role": "确认 table_012 的区间口径和 b1 上界公式。",
            "remaining": "none",
        },
        {
            "name": "Table012TranscriptionNegativeB1CoverLedger",
            "closed": transcription_closed,
            "role": "确认已发表表行若被接受，则 b1<0 连续覆盖 [1e8,8e11]。",
            "remaining": "none on external lane",
        },
        {
            "name": GENERATOR,
            "closed": artifacts["published_generator_artifact_present_in_repo"],
            "role": "取得原始 table_012 生成文件、算法说明、输入数据和 hash。",
            "remaining": "theta_pk/tables/table_012.tex or equivalent published artifact",
        },
        {
            "name": EXTREMAL,
            "closed": artifacts["independent_extremal_archive_present"],
            "role": "独立重算 34 个区间内 theta 极值，证明每个 b1 为外向上界。",
            "remaining": "per-interval extremal theta archive with hash",
        },
        {
            "name": ROUNDING,
            "closed": False,
            "role": "证明表值小数截断/舍入方向是外向安全的，而不是仅复录小数。",
            "remaining": f"{GENERATOR} OR {EXTREMAL}",
        },
    ]


def attack_routes() -> list[dict[str, str]]:
    """给出下一步可执行路线。"""
    return [
        {
            "route": "published_artifact_route",
            "target": GENERATOR,
            "action": "补入 table_012 的原始生成工件、输入文件、外向舍入日志和 hash。",
            "status": "open",
        },
        {
            "route": "independent_regeneration_route",
            "target": EXTREMAL,
            "action": "实现分段 theta 极值 runner，输出 34 个区间的最大归一化误差和可复现 hash。",
            "status": "open",
        },
        {
            "route": "analytic_bypass_route",
            "target": "DirectThetaLtIdentity1e8To8e11AnalyticLedger",
            "action": "用更强显式 PNT/零点自由区直接证明 theta(x)<x；这会回到内部 Dusart/PNT 包。",
            "status": "open but not narrower than table artifact route",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 table_012 自足前沿证书。"""
    theta_cert = load_json(THETA_8E11)
    p51 = load_json(P51_SYNC)
    source = external_source_payload()
    artifacts = repo_artifact_payload()
    obligations = proof_obligations(source, artifacts, theta_cert)

    external_closed = theta_cert.get("theta_less_than_identity_to_8e11_external_closed") is True
    theta_self_closed = theta_cert.get("theta_less_than_identity_to_8e11_self_contained_closed") is True
    p51_external_closed = p51.get("dusart_p51_full_theta_statement_external_closed") is True
    p51_self_closed = p51.get("dusart_p51_full_theta_statement_self_contained_closed") is True
    strict_gate_active = external_closed and p51_external_closed and not theta_self_closed and not p51_self_closed
    generator_or_archive_closed = (
        artifacts["published_generator_artifact_present_in_repo"]
        or artifacts["independent_extremal_archive_present"]
    )
    target_closed = theta_self_closed or generator_or_archive_closed

    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            theta_cert.get("counterexample_assumption_only") is True
            and theta_cert.get("row_column_unconditional_closed") is False,
            True,
            "本步只下钻 P5.1 低段有限表输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "P51ExternalLaneAlreadyClosed",
            p51_external_closed,
            True,
            "接受外部 FK/Dusart 表时，P5.1 theta 上界已闭合；本步只处理严格自足剩余。",
            P51_SELF,
        ),
        row(
            "StrictTable012SelfContainedGateActive",
            strict_gate_active,
            True,
            "P5.1 自足缺口唯一落在 table_012 原始有限计算/hash。",
            TARGET,
        ),
        row(
            "PublishedTable012StatementAndNegativeB1Cover",
            obligations[0]["closed"] and obligations[1]["closed"],
            True,
            "表陈述、区间规则和 b1<0 复录审计已闭合；这是外部表可用性，不是自足生成证明。",
            "external table lane closed",
        ),
        row(
            "Table012GeneratorArtifactPresent",
            artifacts["published_generator_artifact_present_in_repo"],
            False,
            "仓库没有 table_012 原始生成文件或可复现计算日志。",
            GENERATOR,
        ),
        row(
            "IndependentThetaExtremalArchivePresent",
            artifacts["independent_extremal_archive_present"],
            False,
            "仓库没有 34 区间 theta 极值归档；中段 psi 节点表从 8e11 开始，不能替代 [1e8,8e11] 的 theta 表。",
            EXTREMAL,
        ),
        row(
            TARGET,
            target_closed,
            False,
            "严格自足版必须补原始表生成器或独立极值归档，并证明外向舍入。",
            f"{TABLE012_ATOM} AND {ROUNDING}",
        ),
        row(
            "DirectUnconditionalContradictionFound",
            False,
            False,
            "table_012 自足化只是解析输入补强，不产生反例链与真实链终端矛盾。",
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
        "certificate_type": "prime_matrix_strict_table012_self_contained_frontier_router",
        "status": "table012_self_contained_frontier_reduced_to_generator_or_independent_theta_extremal_archive",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "theta_less_than_identity_to_8e11_external_closed": external_closed,
        "theta_less_than_identity_to_8e11_self_contained_closed": target_closed,
        "dusart_p51_full_theta_statement_external_closed": p51_external_closed,
        "dusart_p51_full_theta_statement_self_contained_closed": target_closed and p51_external_closed,
        "table012_generator_or_independent_archive_closed": generator_or_archive_closed,
        "published_table012_statement_cover_closed": obligations[0]["closed"] and obligations[1]["closed"],
        "published_generator_artifact_present_in_repo": artifacts["published_generator_artifact_present_in_repo"],
        "independent_extremal_archive_present": artifacts["independent_extremal_archive_present"],
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "external_source": source,
        "repo_artifacts": artifacts,
        "scale": scale_payload(theta_cert),
        "proof_obligations": obligations,
        "attack_routes": attack_routes(),
        "replacement_self_contained": {
            TARGET: f"{TABLE012_ATOM} AND {ROUNDING}",
            TABLE012_ATOM: f"{GENERATOR} OR {EXTREMAL}",
        },
        "next_direct_attack_target": TABLE012_ATOM,
        "parallel_attack_targets": [ROUNDING, DSTRUCTURE],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "严格自足线的 P5.1 低段剩余已压到 table_012 的来源证明：已发表表行的 b1<0 覆盖可以外部使用，"
            "但作者侧自足版还缺原始生成器/输入/hash，或一份独立重算的 34 区间 theta 极值归档。"
            "因此下一最窄点不是再拼接 P5.1，而是 `Table012OriginalGeneratorOrIndependentThetaExtremalArchiveLedger`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    scale = result["scale"]
    lines = [
        "# Prime Matrix strict table_012 自足前沿下钻证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"theta_less_than_identity_to_8e11_external_closed={fmt_bool(result['theta_less_than_identity_to_8e11_external_closed'])}",
        f"theta_less_than_identity_to_8e11_self_contained_closed={fmt_bool(result['theta_less_than_identity_to_8e11_self_contained_closed'])}",
        f"dusart_p51_full_theta_statement_external_closed={fmt_bool(result['dusart_p51_full_theta_statement_external_closed'])}",
        f"dusart_p51_full_theta_statement_self_contained_closed={fmt_bool(result['dusart_p51_full_theta_statement_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足缺口",
        "",
        "```text",
        f"{TARGET}",
        "  =>",
        result["replacement_self_contained"][TARGET],
        "",
        f"{TABLE012_ATOM}",
        "  =>",
        result["replacement_self_contained"][TABLE012_ATOM],
        "```",
        "",
        "## 2. 规模与边界",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| `interval_count` | `{scale['interval_count']}` |",
        f"| `range_width_integer_count` | `{scale['range_width_integer_count']}` |",
        f"| `prime_jump_count_scale_estimate_x_over_logx` | `{scale['prime_jump_count_scale_estimate_x_over_logx']}` |",
        f"| `worst_published_margin_label` | `{scale['worst_published_margin_label']}` |",
        f"| `worst_published_margin_right` | `{scale['worst_published_margin_right']}` |",
        f"| `worst_published_relative_margin` | `{scale['worst_published_relative_margin']}` |",
        "",
        "## 3. 必补账本",
        "",
        "| ledger | closed | role | remaining |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["proof_obligations"]:
        lines.append(
            f"| `{table_cell(item['name'])}` | `{fmt_bool(item['closed'])}` | "
            f"{table_cell(item['role'])} | {table_cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 可攻路线",
            "",
            "| route | target | status | action |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["attack_routes"]:
        lines.append(
            f"| `{table_cell(item['route'])}` | `{table_cell(item['target'])}` | "
            f"`{table_cell(item['status'])}` | {table_cell(item['action'])} |"
        )
    lines.extend(
        [
            "",
            "## 5. 判定表",
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
            "## 6. 下一最窄点",
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
        "theta_less_than_identity_to_8e11_self_contained_closed="
        f"{fmt_bool(result['theta_less_than_identity_to_8e11_self_contained_closed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
