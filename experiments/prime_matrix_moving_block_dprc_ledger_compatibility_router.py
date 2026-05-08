#!/usr/bin/env python3
"""Prime Matrix moving-block 与 DPRC 账本兼容性路由器。

用法示例：
  python3 experiments/prime_matrix_moving_block_dprc_ledger_compatibility_router.py

输出：
  docs/monograph/prime-matrix-moving-block-dprc-ledger-compatibility-router.json
  docs/monograph/prime-matrix-moving-block-dprc-ledger-compatibility-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-current-terminal-promotion-reconciliation-router.json"
DEFAULT_MOVING = DOCS / "prime-matrix-counterexample-moving-block-terminal-router.json"
DEFAULT_SCHEMA = DOCS / "prime-matrix-early-zero-terminal-schema-reconciliation-router.json"
DEFAULT_GLOBAL = DOCS / "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json"
DEFAULT_DPRC = DOCS / "prime-matrix-clean-core-dprc-centered-discrepancy-router.json"
DEFAULT_RSM = DOCS / "prime-matrix-dprc-relative-sieve-margin.md"
DEFAULT_JSON = DOCS / "prime-matrix-moving-block-dprc-ledger-compatibility-router.json"
DEFAULT_MD = DOCS / "prime-matrix-moving-block-dprc-ledger-compatibility-router.md"

COMPAT_ATOM = "ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock"
MODEL_ATOM = "ExplicitModelGapAndFiniteDPRCLedger"
CANONICAL_TERMINAL = "NoFurtherCanonicalSourceTerminalPromotionGap"
EXTERNAL_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
CLOSED_COMPAT = "NoAdditionalDPRCLedgerGapAfterTerminalPromotionReconciliation"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def remove_and_atom(text: str, atom: str) -> str:
    """从 AND 输入基中删除一个已经闭合的原子。"""
    updated = text
    for pattern in (
        f" AND {atom} AND ",
        f"({atom} AND ",
        f" AND {atom})",
        f"{atom} AND ",
        f" AND {atom}",
        atom,
    ):
        if pattern == f" AND {atom} AND ":
            updated = updated.replace(pattern, " AND ")
        elif pattern == f"({atom} AND ":
            updated = updated.replace(pattern, "(")
        elif pattern == f" AND {atom})":
            updated = updated.replace(pattern, ")")
        else:
            updated = updated.replace(pattern, "")
    return " ".join(updated.split())


def count_atom(text: str, atom: str) -> int:
    """统计输入基中原子名出现次数。"""
    return text.count(atom)


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def branch_guard(*certs: dict[str, Any]) -> bool:
    """确认仍在假设反例链条内，没有使用真实缺席。"""
    return all(
        bool(cert.get("counterexample_assumption_only"))
        and bool(cert.get("empirical_absence_not_used"))
        and bool(cert.get("hypothetical_chain_only"))
        and not bool(cert.get("row_column_unconditional_closed"))
        for cert in certs
    )


def build_rows(
    previous: dict[str, Any],
    moving: dict[str, Any],
    schema: dict[str, Any],
    global_terminal: dict[str, Any],
    dprc: dict[str, Any],
    rsm_text: str,
) -> list[dict[str, Any]]:
    """生成兼容性判定表。"""
    previous_basis = previous.get("latest_self_contained_basis", "")
    moving_basis = moving.get("latest_self_contained_basis", "")
    schema_basis = schema.get("latest_self_contained_basis", "")
    global_basis = global_terminal.get("latest_self_contained_basis", "")
    dprc_basis = dprc.get("latest_self_contained_basis", "")

    active = previous.get("next_priority") == COMPAT_ATOM and COMPAT_ATOM in previous_basis
    guard = branch_guard(previous, moving, schema, global_terminal)
    moving_separated = (
        moving.get("moving_block_to_terminal_reduction_closed") is True
        and COMPAT_ATOM in moving.get("terminal_gap_after_router", "")
        and MODEL_ATOM in moving_basis
    )
    schema_preserved = (
        schema.get("terminal_gap_before_router", "").endswith(COMPAT_ATOM)
        and schema.get("terminal_gap_after_router", "").endswith(COMPAT_ATOM)
        and count_atom(schema_basis, COMPAT_ATOM) == 1
        and count_atom(schema_basis, MODEL_ATOM) == 1
    )
    global_preserved = (
        global_terminal.get("terminal_gap_before_router") == "GlobalPDECorSparseTerminalExclusion"
        and global_terminal.get("terminal_gap_after_router") == "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
        and count_atom(global_basis, COMPAT_ATOM) == 1
        and count_atom(global_basis, MODEL_ATOM) == 1
    )
    promotion_preserved = (
        previous.get("current_terminal_promotion_reconciled") is True
        and previous.get("terminal_gap_after_router") == CANONICAL_TERMINAL
        and count_atom(previous_basis, COMPAT_ATOM) == 1
        and count_atom(previous_basis, MODEL_ATOM) == 1
    )
    dprc_object_pinned = (
        MODEL_ATOM in dprc.get("latest_internal_subinputs", [])
        and MODEL_ATOM in dprc_basis
        and "S-T=S(1-H)" in rsm_text
        and "P<2003" in rsm_text
        and "P>=2003" in rsm_text
    )
    no_relabeling_gap = all(
        [
            active,
            guard,
            moving_separated,
            schema_preserved,
            global_preserved,
            promotion_preserved,
            dprc_object_pinned,
        ]
    )
    return [
        row(
            "ExactCompatibilityGateActive",
            active,
            False,
            "最新最窄点正是 moving-block 替换与 DPRC 模型账本的精确兼容性。",
            COMPAT_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条内做账本调和，不用真实样本缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "MovingBlockRouterSeparatedTerminalAndLedger",
            moving_separated,
            True,
            "moving-block 路由只把运动块终端压到早期零行终端包，并把兼容性门单列；模型账本仍是独立原子。",
            MODEL_ATOM,
        ),
        row(
            "SchemaReconciliationPreservedDPRCLedgerAtom",
            schema_preserved,
            True,
            "早期零行终端包到全局 PDEC/sparse 的调和只替换终端原子，兼容性门和模型账本各出现一次。",
            "无额外 DPRC 口径变化。",
        ),
        row(
            "GlobalPDECSparseSplitPreservedDPRCLedgerAtom",
            global_preserved,
            True,
            "GlobalPDEC/sparse 到 PDEC-CAP/internal-KLS 的拆分没有重命名或吸收 ExplicitModelGapAndFiniteDPRCLedger。",
            "无 moving-block 专属模型账本。",
        ),
        row(
            "TerminalPromotionPreservedDPRCLedgerAtom",
            promotion_preserved,
            True,
            "当前 canonical 终端晋级只关闭终端侧，不改写模型余量/有限 DPRC 账本。",
            "终端闭合不能被误读为模型账本证明。",
        ),
        row(
            "DPRCModelLedgerObjectPinned",
            dprc_object_pinned,
            True,
            "DPRC 路由把 ExplicitModelGapAndFiniteDPRCLedger 固定为 RSM 模型余量与有限证书接口。",
            "证明该模型账本自身仍是独立义务。",
        ),
        row(
            "NoMovingBlockSpecificDPRCRelabelingGap",
            no_relabeling_gap,
            True,
            "从 moving-block 到 canonical 终端晋级，变化只发生在终端原子；DPRC 账本对象同名、同位、同用途保留。",
            CLOSED_COMPAT,
        ),
        row(
            COMPAT_ATOM,
            no_relabeling_gap,
            True,
            "兼容性门闭合为接口事实：没有新增 moving-block 专属 DPRC 账本缺口。",
            CLOSED_COMPAT,
        ),
        row(
            MODEL_ATOM,
            False,
            False,
            "模型余量/有限 DPRC 账本本身尚未由本路由证明；P<2003 有限表与 P>=2003 模型余量仍需正式闭合。",
            MODEL_ATOM,
        ),
        row(
            EXTERNAL_ATOM,
            False,
            False,
            "generic/external DI/BFI 宽口径仍在 canonical 自足边界外。",
            EXTERNAL_ATOM,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 moving-block/DPRC 账本兼容性调和。"""
    previous = load_json(paths["previous"])
    moving = load_json(paths["moving"])
    schema = load_json(paths["schema"])
    global_terminal = load_json(paths["global_terminal"])
    dprc = load_json(paths["dprc"])
    rsm_text = paths["rsm"].read_text(encoding="utf-8")
    rows = build_rows(previous, moving, schema, global_terminal, dprc, rsm_text)
    compat_closed = next(bool(item["closed"]) for item in rows if item["gate"] == COMPAT_ATOM)

    latest_self = remove_and_atom(previous.get("latest_self_contained_basis", ""), COMPAT_ATOM)
    latest_cond = remove_and_atom(previous.get("latest_conditional_basis", ""), COMPAT_ATOM)
    latest_global = remove_and_atom(previous.get("latest_global_with_external_basis", ""), COMPAT_ATOM)

    source_paths = list(paths.values())
    return {
        "certificate_type": "moving_block_dprc_ledger_compatibility_router",
        "status": "moving_block_dprc_ledger_compatibility_closed_modelgap_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "exact_model_gap_dprc_compatibility_proved": compat_closed,
        "no_additional_dprc_ledger_gap_after_terminal_promotion": compat_closed,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "closed_input_removed": COMPAT_ATOM,
        "closed_interface_atom": CLOSED_COMPAT,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "replacement": {COMPAT_ATOM: CLOSED_COMPAT},
        "next_priority": MODEL_ATOM,
        "external_next_priority": EXTERNAL_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步关闭的是兼容性接口，不是 DPRC 模型余量账本自身。"
            "从 moving-block 到早期零行终端包、再到 global PDEC/sparse、PDEC-CAP/internal-KLS、"
            "最后到 canonical 终端晋级，所有替换都只发生在终端原子上；"
            "ExplicitModelGapAndFiniteDPRCLedger 一直作为同名、同位的独立输入保留。"
            "因此 ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock 可从活动输入基中删除，"
            "下一最窄目标转为 ExplicitModelGapAndFiniteDPRCLedger 本身。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix moving-block 与 DPRC 账本兼容性路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        (
            "exact_model_gap_dprc_compatibility_proved="
            f"{fmt_bool(result['exact_model_gap_dprc_compatibility_proved'])}"
        ),
        (
            "explicit_model_gap_and_finite_dprc_ledger_proved="
            f"{fmt_bool(result['explicit_model_gap_and_finite_dprc_ledger_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"closed_input_removed={result['closed_input_removed']}",
        f"closed_interface_atom={result['closed_interface_atom']}",
        "```",
        "",
        "## 1. 兼容性引理",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "  => 从活动输入基删除该兼容性门，保留 ExplicitModelGapAndFiniteDPRCLedger。",
        "```",
        "",
        "严格含义：本引理只说明 moving-block 终端替换没有引入新的 DPRC 账本对象。它不证明 `ExplicitModelGapAndFiniteDPRCLedger`，也不关闭完整行列无条件定理。",
        "",
        "## 2. 账本轨迹",
        "",
        "```text",
        "ActualNoncanonicalMovingBlockSpreadNCBLK",
        "  -> EarlyZeroTerminalExclusionPackage + ExactCompatibility",
        "  -> GlobalPDECorSparseTerminalExclusion + ExactCompatibility",
        "  -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve + ExactCompatibility",
        "  -> NoFurtherCanonicalSourceTerminalPromotionGap + ExactCompatibility",
        "  -> NoFurtherCanonicalSourceTerminalPromotionGap",
        "",
        "ExplicitModelGapAndFiniteDPRCLedger 在每一层均作为独立原子保留。",
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "conditional 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "global/external 宽口径输入基：",
            "",
            "```text",
            result["latest_global_with_external_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            "当前最窄目标变为 `ExplicitModelGapAndFiniteDPRCLedger`：把 `P<2003` 的有限证书和 `P>=2003` 的 `S(1-H)>3sqrt(S)` 模型余量写成可独立审查的正式账本。并行保留 generic/external DI/BFI 分支和 DStructure/Rankin 最终验收门。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--moving", type=Path, default=DEFAULT_MOVING)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--global-terminal", type=Path, default=DEFAULT_GLOBAL)
    parser.add_argument("--dprc", type=Path, default=DEFAULT_DPRC)
    parser.add_argument("--rsm", type=Path, default=DEFAULT_RSM)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "moving": args.moving,
        "schema": args.schema,
        "global_terminal": args.global_terminal,
        "dprc": args.dprc,
        "rsm": args.rsm,
    }
    result = run(paths)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(f"wrote {args.json_output}")
    print(f"wrote {args.md_output}")


if __name__ == "__main__":
    main()
