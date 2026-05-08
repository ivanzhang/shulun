#!/usr/bin/env python3
"""Prime Matrix clean-core exact entropy 原子路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_exact_entropy_atom_router.py

输出：
  docs/monograph/prime-matrix-clean-core-exact-entropy-atom-router.json
  docs/monograph/prime-matrix-clean-core-exact-entropy-atom-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_TERMINAL = DOCS / "prime-matrix-clean-core-terminal-normal-form-router.json"
DEFAULT_EXACT_WFD = DOCS / "prime-matrix-triad-a1-exact-wfd-source-entropy-router.json"
DEFAULT_SOURCE_CORE = DOCS / "prime-matrix-noncanonical-source-core-atomization-router.json"
DEFAULT_REGISTERED = DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json"
DEFAULT_EXACT_UV = DOCS / "prime-matrix-exact-uv-support-terminal-attack-router.json"
DEFAULT_PACKET = DOCS / "prime-matrix-exact-uv-support-failure-packetization-router.json"
DEFAULT_RETURN = DOCS / "prime-matrix-support-failure-packet-return-dichotomy-router.json"
DEFAULT_MOVING = DOCS / "prime-matrix-clean-core-moving-atom-sharp-input-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-exact-entropy-atom-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-exact-entropy-atom-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def atom_rows(
    terminal: dict[str, Any],
    exact_wfd: dict[str, Any],
    source_core: dict[str, Any],
    registered: dict[str, Any],
    exact_uv: dict[str, Any],
    packet: dict[str, Any],
    return_router: dict[str, Any],
    moving: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 exact entropy 原子化判定表。"""
    registered_closed = registered.get("registered_capacity_multiplier_discipline_closed") is True
    support_implication_closed = (
        exact_wfd.get("conditional_factor_support_implies_exact_source_entropy") is True
    )
    balanced_closed = source_core.get("balanced_range_threshold_closed") is True
    return_closed = return_router.get("support_failure_packet_return_dichotomy_closed") is True

    return [
        {
            "gate": "TerminalExactEntropyPinned",
            "closed": terminal.get("internal_normal_form")
            == "ExactCleanCoreFullSNonAPWFDSourceEntropy",
            "proved": False,
            "meaning": "上一层已把内部终局标准形固定为 exact clean-core source entropy。",
            "remaining": "审查该熵命题失败时的最小原子。",
        },
        {
            "gate": "EntropyFailureIsCleanCoreMovingAtom",
            "closed": moving.get("new_source_microinput")
            == "ActualNoncanonicalCleanCoreMovingAtomExclusion",
            "proved": False,
            "meaning": "exact entropy 失败等价于存在 clean-core moving same-(u,v) 大原子。",
            "remaining": "排除这个大原子，或给出可回流证书。",
        },
        {
            "gate": "BroadSupportContradictsMovingAtom",
            "closed": support_implication_closed and balanced_closed and registered_closed,
            "proved": False,
            "meaning": (
                "已有条件链说明：balanced range、divisor bound、registered multiplier 与 exact u/v "
                "支撑下界合在一起会推出 source entropy。"
            ),
            "remaining": "真正未证的是 clean-core 内部的 exact u/v 支撑-关联下界。",
        },
        {
            "gate": "RegisteredMultiplierEscapeRemoved",
            "closed": registered_closed,
            "proved": registered_closed,
            "meaning": "Type/Fourier/fiber 乘子已登记进同一 formal unit 的 log-power 账本。",
            "remaining": "熵失败不能再归咎于账外容量乘子。",
        },
        {
            "gate": "ExactUVSupportStillNotProved",
            "closed": exact_uv.get("exact_uv_support_terminal_boundary_closed") is True,
            "proved": False,
            "meaning": "ExactUVSupport 已被审查为源侧终端输入，不能由 K4/K6、formal WFD 或 canonical 支撑偷渡推出。",
            "remaining": "需要新的 clean-core 支撑-关联定理。",
        },
        {
            "gate": "SupportFailurePacketizationAvailable",
            "closed": packet.get("failure_packetization_closed") is True,
            "proved": False,
            "meaning": "若支撑下界失败，必须生成带 source class、formal unit、block key 和容量剖面的 packet。",
            "remaining": "packet 仍可能是 clean-core 终端 packet。",
        },
        {
            "gate": "NonCleanCoreReturnClosed",
            "closed": return_closed,
            "proved": return_closed,
            "meaning": "非 clean-core packet 已回流到有限孤立、持久签名、ColumnCRT/位移、漂移 CleanKLS/DLS 或已阻断逃逸。",
            "remaining": "只剩通过全部回流测试的 clean-core 终端原子。",
        },
        {
            "gate": "CleanCoreTerminalSupportIncidenceCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有证明 clean-core 内部每个正质量 block 都有足够 exact u/v 支撑扩散。",
            "remaining": "证明 CleanCoreTerminalSupportIncidenceTheorem。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "源侧输入完成后仍需独立验收。",
        },
    ]


def run(
    terminal_path: Path,
    exact_wfd_path: Path,
    source_core_path: Path,
    registered_path: Path,
    exact_uv_path: Path,
    packet_path: Path,
    return_path: Path,
    moving_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 clean-core exact entropy 原子路由。"""
    source_paths = [
        terminal_path,
        exact_wfd_path,
        source_core_path,
        registered_path,
        exact_uv_path,
        packet_path,
        return_path,
        moving_path,
        dstructure_path,
    ]
    terminal = load_json(terminal_path)
    exact_wfd = load_json(exact_wfd_path)
    source_core = load_json(source_core_path)
    registered = load_json(registered_path)
    exact_uv = load_json(exact_uv_path)
    packet = load_json(packet_path)
    return_router = load_json(return_path)
    moving = load_json(moving_path)
    dstructure = load_json(dstructure_path)

    rows = atom_rows(
        terminal=terminal,
        exact_wfd=exact_wfd,
        source_core=source_core,
        registered=registered,
        exact_uv=exact_uv,
        packet=packet,
        return_router=return_router,
        moving=moving,
        dstructure=dstructure,
    )
    route_closed = all(
        row["closed"]
        for row in rows
        if row["gate"] != "CleanCoreTerminalSupportIncidenceCurrentCorpusProved"
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_exact_entropy_atom_router",
        "status": "clean_core_exact_entropy_reduced_to_terminal_support_incidence_open",
        "clean_core_exact_entropy_atom_boundary_closed": route_closed,
        "broad_support_contradiction_schema_closed": True,
        "registered_multiplier_escape_closed": registered.get(
            "registered_capacity_multiplier_discipline_closed"
        )
        is True,
        "non_clean_core_return_closed": return_router.get(
            "support_failure_packet_return_dichotomy_closed"
        )
        is True,
        "clean_core_terminal_support_incidence_proved": False,
        "exact_clean_core_entropy_proved": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_internal_input": terminal.get("internal_normal_form"),
        "latest_actionable_self_contained_input": "CleanCoreTerminalSupportIncidenceTheorem",
        "latest_self_contained_proof_package": (
            "CleanCoreTerminalSupportIncidenceTheorem AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "support_incidence_theorem": (
            "每个通过全部回流测试的正质量 actual clean-core full-S non-AP WFD block，"
            "在同一 formal unit 内必须给出 exact u/v 支撑乘积的对数幂下界，足以抵消 "
            "divisor bound 与所有 registered capacity multipliers；否则它就是一个可复现的 "
            "clean-core terminal support atom。"
        ),
        "atom_law": (
            "若 ExactCleanCoreFullSNonAPWFDSourceEntropy 失败，则存在 clean-core moving 大原子。"
            "由于乘子逃逸已登记、非 clean-core packet 已回流，失败只能落到通过全部回流测试的 "
            "clean-core terminal support atom。"
        ),
        "plain_conclusion": (
            "最新终局输入的可行动证明包继续向内压到一个可审查的支撑-关联定理：必须证明 "
            "clean-core 内部不能存在正质量、无回流、同一 moving (u,v) 承载过大容量的终端支撑原子。"
            "当前材料仍未证明该定理，所以 exact entropy 和无条件行/列命题仍未闭合。"
        ),
        "rows": rows,
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths
        },
    }
    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 研究证书。"""
    lines: list[str] = [
        "# Prime Matrix clean-core exact entropy 原子路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"clean_core_exact_entropy_atom_boundary_closed={fmt_bool(result['clean_core_exact_entropy_atom_boundary_closed'])}",
        f"clean_core_terminal_support_incidence_proved={fmt_bool(result['clean_core_terminal_support_incidence_proved'])}",
        f"exact_clean_core_entropy_proved={fmt_bool(result['exact_clean_core_entropy_proved'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 原子律",
            "",
            result["atom_law"],
            "",
            "## 3. 最新可行动自足输入",
            "",
            "```text",
            result["latest_actionable_self_contained_input"],
            "```",
            "",
            result["support_incidence_theorem"],
            "",
            "连同独立晋级门，形成可行动证明包：",
            "",
            "```text",
            result["latest_self_contained_proof_package"],
            "```",
            "",
            "## 4. 当前结论",
            "",
            "本步没有证明 `CleanCoreTerminalSupportIncidenceTheorem`。它完成的是原子化：",
            "exact clean-core entropy 的失败不再是无名失败，只能表现为通过全部回流测试的 clean-core",
            "terminal support atom。",
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(
        description="Route clean-core exact entropy to its terminal support atom."
    )
    parser.add_argument("--terminal", type=Path, default=DEFAULT_TERMINAL)
    parser.add_argument("--exact-wfd", type=Path, default=DEFAULT_EXACT_WFD)
    parser.add_argument("--source-core", type=Path, default=DEFAULT_SOURCE_CORE)
    parser.add_argument("--registered", type=Path, default=DEFAULT_REGISTERED)
    parser.add_argument("--exact-uv", type=Path, default=DEFAULT_EXACT_UV)
    parser.add_argument("--packet", type=Path, default=DEFAULT_PACKET)
    parser.add_argument("--return-router", type=Path, default=DEFAULT_RETURN)
    parser.add_argument("--moving", type=Path, default=DEFAULT_MOVING)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        terminal_path=args.terminal,
        exact_wfd_path=args.exact_wfd,
        source_core_path=args.source_core,
        registered_path=args.registered,
        exact_uv_path=args.exact_uv,
        packet_path=args.packet,
        return_path=args.return_router,
        moving_path=args.moving,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_actionable_self_contained_input"])


if __name__ == "__main__":
    main()
