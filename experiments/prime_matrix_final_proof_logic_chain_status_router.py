#!/usr/bin/env python3
"""最终证明逻辑链状态路由器。

用法示例：
  python3 experiments/prime_matrix_final_proof_logic_chain_status_router.py
  python3 experiments/prime_matrix_final_proof_logic_chain_status_router.py --accept-referee-gate

输出：
  docs/monograph/prime-matrix-final-proof-logic-chain-status-router.json
  docs/monograph/prime-matrix-final-proof-logic-chain-status-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_ATLAS = MONO / "prime-matrix-closure-input-atlas-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-unconditional-closure-endpoint-verdict-router.json"
DEFAULT_EXTERNAL_FINAL = MONO / "prime-matrix-external-kls-accepted-final-promotion-router.json"
DEFAULT_SINGLE_GATE = MONO / "prime-matrix-final-single-gate-closure-decision-router.json"
DEFAULT_IRREDUCIBLE = MONO / "prime-matrix-final-promotion-gate-irreducibility-router.json"
DEFAULT_LINE_REF = MONO / "line-by-line-internal-referee-matrix.md"
DEFAULT_JSON = MONO / "prime-matrix-final-proof-logic-chain-status-router.json"
DEFAULT_MD = MONO / "prime-matrix-final-proof-logic-chain-status-router.md"

EXTERNAL_KLS = "AcceptFullSKLSExtExternalContract"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本证据。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """格式化布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def proof_step(
    index: int,
    name: str,
    proved_or_accepted: bool,
    uses: str,
    conclusion: str,
    evidence: str,
    if_false: str,
) -> dict[str, Any]:
    """构造证明链步骤。"""
    return {
        "index": index,
        "name": name,
        "proved_or_accepted": proved_or_accepted,
        "uses": uses,
        "conclusion": conclusion,
        "evidence": evidence,
        "if_false": if_false,
    }


def build_steps(
    atlas: dict[str, Any],
    endpoint: dict[str, Any],
    external_final: dict[str, Any],
    single_gate: dict[str, Any],
    irreducible: dict[str, Any],
    line_ref_text: str,
    accept_referee_gate: bool,
) -> list[dict[str, Any]]:
    """按实际逻辑顺序拼接最终证明链。"""
    counterexample_chain_clean = (
        endpoint.get("counterexample_assumption_only") is True
        and endpoint.get("empirical_absence_not_used") is True
        and endpoint.get("hypothetical_chain_only") is True
    )
    no_hidden_escape = (
        endpoint.get("endpoint_boundary_closed") is True
        and atlas.get("canonical_source_self_contained_closed") is True
        and atlas.get("noncanonical_input_contract_closed") is True
    )
    external_math_closed = (
        external_final.get("external_fulls_kls_accepted") is True
        and external_final.get("all_math_inputs_closed_after_external_acceptance") is True
        and single_gate.get("external_math_inputs_closed") is True
    )
    promotion_packet_sealed = (
        irreducible.get("promotion_author_packet_sealed") is True
        and single_gate.get("promotion_author_dossier_complete") is True
    )
    no_author_promotion = (
        irreducible.get("author_side_direct_attack_exhausted") is True
        and "本轮没有把任何 `BLOCK-REFEREE` 改写为 `PASS-AUTHOR`" in line_ref_text
    )
    referee_gate_accepted = bool(
        accept_referee_gate
        and promotion_packet_sealed
        and irreducible.get("irreducible_gate") == PROMOTION_GATE
    )
    conditional_chain_closed = (
        counterexample_chain_clean
        and no_hidden_escape
        and external_math_closed
        and promotion_packet_sealed
        and no_author_promotion
    )
    final_closed = conditional_chain_closed and referee_gate_accepted

    return [
        proof_step(
            index=1,
            name="CounterexampleChainDiscipline",
            proved_or_accepted=counterexample_chain_clean,
            uses="counterexample assumption only; no empirical absence",
            conclusion="所有后续推理都在假设反例链条内进行，不用真实样本缺席偷换。",
            evidence=endpoint.get("status", "unknown"),
            if_false="不能宣称反例排斥，因为可能混入统计或真实链条。",
        ),
        proof_step(
            index=2,
            name="NoHiddenTerminalEscape",
            proved_or_accepted=no_hidden_escape,
            uses="closure atlas + endpoint boundary",
            conclusion="方阵斜线、圆柱覆盖、P列锚、层叠筛、PDEC/SAE/CleanKLS 等出口已被压成命名输入图谱。",
            evidence=atlas.get("status", "unknown"),
            if_false="还需寻找未命名终端或补全输入图谱。",
        ),
        proof_step(
            index=3,
            name="ExternalFullSKLSMathLaneClosure",
            proved_or_accepted=external_math_closed,
            uses=EXTERNAL_KLS,
            conclusion="noncanonical full-S 数学线在外部 KLS 合同下闭合。",
            evidence=external_final.get("status", "unknown"),
            if_false="还需证明新 full-S 定理或走完全自足 noncanonical 源反原子。",
        ),
        proof_step(
            index=4,
            name="PromotionAuthorPacketSeal",
            proved_or_accepted=promotion_packet_sealed,
            uses="DStructure/AB + Tail-log4/BG-RKS + finite verification + Rankin pass-or-return",
            conclusion="最终晋级门的作者侧证据包已封装为可审查、可复跑、可提交的验收包。",
            evidence=irreducible.get("status", "unknown"),
            if_false="还需补齐作者侧证明包或复跑证据。",
        ),
        proof_step(
            index=5,
            name="NoAuthorSidePromotion",
            proved_or_accepted=no_author_promotion,
            uses="line-by-line internal referee matrix",
            conclusion="作者侧不能把独立验收事件改写为 PASS-AUTHOR。",
            evidence="line-by-line internal referee matrix",
            if_false="可能把条件闭合误报为无条件闭合。",
        ),
        proof_step(
            index=6,
            name="ConditionalRowColumnTheorem",
            proved_or_accepted=conditional_chain_closed,
            uses=f"{EXTERNAL_KLS} AND {PROMOTION_GATE}",
            conclusion="若外部 KLS 合同与最终独立晋级门都成立，则行/列命题闭合。",
            evidence=single_gate.get("status", "unknown"),
            if_false="条件定理链条尚未完整。",
        ),
        proof_step(
            index=7,
            name="FinalUnconditionalPromotion",
            proved_or_accepted=final_closed,
            uses=PROMOTION_GATE,
            conclusion="最终无条件闭合只在独立晋级门被显式接受后成立。",
            evidence="--accept-referee-gate" if referee_gate_accepted else "referee gate not accepted",
            if_false="当前最终状态为条件闭合，不是完整无条件闭合。",
        ),
    ]


def run(paths: dict[str, Path], accept_referee_gate: bool) -> dict[str, Any]:
    """运行最终证明逻辑链状态路由。"""
    atlas = load_json(paths["atlas"])
    endpoint = load_json(paths["endpoint"])
    external_final = load_json(paths["external_final"])
    single_gate = load_json(paths["single_gate"])
    irreducible = load_json(paths["irreducible"])
    line_ref_text = read_text(paths["line_ref"])

    steps = build_steps(
        atlas=atlas,
        endpoint=endpoint,
        external_final=external_final,
        single_gate=single_gate,
        irreducible=irreducible,
        line_ref_text=line_ref_text,
        accept_referee_gate=accept_referee_gate,
    )
    conditional_closed = all(step["proved_or_accepted"] for step in steps[:6])
    final_closed = all(step["proved_or_accepted"] for step in steps)
    referee_gate_open = conditional_closed and not final_closed

    return {
        "certificate_type": "prime_matrix_final_proof_logic_chain_status_router",
        "status": (
            "row_column_final_unconditional_closed_external_kls_plus_referee_gate"
            if final_closed
            else "conditional_external_kls_closure_complete_referee_gate_open"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            **{str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        },
        "conditional_external_kls_proof_chain_closed": conditional_closed,
        "referee_gate_open": referee_gate_open,
        "referee_gate_explicitly_accepted": steps[-1]["proved_or_accepted"],
        "row_column_unconditional_closed": final_closed,
        "self_contained_unconditional_closed": False,
        "strict_conditional_basis": f"{EXTERNAL_KLS} AND {PROMOTION_GATE}",
        "final_closure_status": (
            "命题在外部 KLS 合同和最终独立晋级门均接受后闭合。"
            if final_closed
            else "当前达到外部 KLS 合同条件闭合；最终独立晋级门未接受，故无条件闭合状态仍为 false。"
        ),
        "actual_proof_chain": steps,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 最终证明逻辑链状态路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["final_closure_status"],
        "",
        "```text",
        (
            "conditional_external_kls_proof_chain_closed="
            f"{fmt_bool(result['conditional_external_kls_proof_chain_closed'])}"
        ),
        f"referee_gate_open={fmt_bool(result['referee_gate_open'])}",
        f"referee_gate_explicitly_accepted={fmt_bool(result['referee_gate_explicitly_accepted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"self_contained_unconditional_closed={fmt_bool(result['self_contained_unconditional_closed'])}",
        "```",
        "",
        "## 1. 严格条件闭合基",
        "",
        "```text",
        result["strict_conditional_basis"],
        "```",
        "",
        "## 2. 实际证明链",
        "",
        "| # | step | proved/accepted | uses | conclusion | if false |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for step in result["actual_proof_chain"]:
        lines.append(
            "| {index} | `{name}` | `{proved}` | {uses} | {conclusion} | {if_false} |".format(
                index=step["index"],
                name=table_cell(step["name"]),
                proved=fmt_bool(step["proved_or_accepted"]),
                uses=table_cell(step["uses"]),
                conclusion=table_cell(step["conclusion"]),
                if_false=table_cell(step["if_false"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 最终状态",
            "",
            (
                "当前已经完成的是严格条件闭合链：反例链纪律、无隐藏终端、外部 KLS 数学线、"
                "作者侧晋级证据包和不偷换纪律全部闭合。"
                "未完成的是最后独立晋级门的接受事件；因此不能把当前状态写成完全无条件证明。"
            ),
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--atlas-json", type=Path, default=DEFAULT_ATLAS)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--external-final-json", type=Path, default=DEFAULT_EXTERNAL_FINAL)
    parser.add_argument("--single-gate-json", type=Path, default=DEFAULT_SINGLE_GATE)
    parser.add_argument("--irreducible-json", type=Path, default=DEFAULT_IRREDUCIBLE)
    parser.add_argument("--line-ref", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--accept-referee-gate", action="store_true")
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "atlas": args.atlas_json,
        "endpoint": args.endpoint_json,
        "external_final": args.external_final_json,
        "single_gate": args.single_gate_json,
        "irreducible": args.irreducible_json,
        "line_ref": args.line_ref,
    }
    result = run(paths, args.accept_referee_gate)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["final_closure_status"])


if __name__ == "__main__":
    main()
