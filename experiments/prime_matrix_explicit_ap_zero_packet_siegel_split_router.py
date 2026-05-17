#!/usr/bin/env python3
"""把显式 AP 零点包硬点拆成 Siegel 实零与非实相位集中两条分支。

用法示例：
  python3 experiments/prime_matrix_explicit_ap_zero_packet_siegel_split_router.py
  python3 -m json.tool docs/monograph/prime-matrix-explicit-ap-zero-packet-siegel-split-router.json

输出：
  data/prime-matrix-explicit-ap-zero-packet-siegel-split-ledger.json
  docs/monograph/prime-matrix-explicit-ap-zero-packet-siegel-split-router.json
  docs/monograph/prime-matrix-explicit-ap-zero-packet-siegel-split-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

OUT_LEDGER = DATA / "prime-matrix-explicit-ap-zero-packet-siegel-split-ledger.json"
OUT_JSON = DOCS / "prime-matrix-explicit-ap-zero-packet-siegel-split-router.json"
OUT_MD = DOCS / "prime-matrix-explicit-ap-zero-packet-siegel-split-router.md"

PREVIOUS_FRONTIER = "three-claims-frontier-rankone-explicit-formula-router.json"
RANKONE = "prime-matrix-linnik2-rankone-phase-capacity-router.json"
NONPRINCIPAL = "prime-matrix-linnik2-nonprincipal-character-obstruction-router.json"
STATUS_TABLE = "claim-status-table.md"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_VIII = ROOT / "docs" / "prime-density-waves-VIII.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

ZERO_PACKET = "ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2"
SIEGEL_SPLIT = "ExplicitAPZeroPacketSiegelNonrealDichotomyAtP2"
SIEGEL_BRANCH = "SiegelExceptionalBiasExclusionAtSquareScale"
NONREAL_BRANCH = "NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2"
TRIVIAL_BRANCH = "TrivialAndFiniteExplicitFormulaTermsBelowMainMarginAtP2"
PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
SIGNED_PAYLOAD_ATOM = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / PREVIOUS_FRONTIER,
    DOCS / RANKONE,
    DOCS / NONPRINCIPAL,
    DOCS / STATUS_TABLE,
    FINAL_PROOF_DRAFT,
    PRIME_DENSITY_WAVES_VIII,
    PRIME_DENSITY_WAVES_X,
    PAPER,
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希，保证本证书可复核。"""
    result: dict[str, str] = {}
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
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


def explicit_formula_split() -> list[dict[str, str]]:
    """给出零点包的精确分裂。"""
    return [
        {
            "component": "principal main term",
            "scale_at_x_p2": "P",
            "role": "必须被所有误差包严格小于，才能推出 theta(P^2;P,a)>0。",
        },
        {
            "component": "real exceptional / Siegel zero",
            "scale_at_x_p2": "P^(2 beta-1)/beta = P exp(-2 lambda)/beta when beta=1-lambda/log P",
            "role": "若 beta 距 1 只有 O(1/log P)，该项与主项同阶；危险半类不能靠平均或容量自动排除。",
        },
        {
            "component": "nonreal zero packet",
            "scale_at_x_p2": "signed sum of P^(2 rho-1)/rho over characters and ordinates",
            "role": "总绝对值或 L2 能量不足以闭合；需要逐 residue 的相位抵消，排除同向集中。",
        },
        {
            "component": "trivial zeros / imprimitive / finite terms",
            "scale_at_x_p2": "lower-order once the two genuine zero packets are controlled",
            "role": "不是当前主障碍，但必须保留在最终显式常数账本中。",
        },
    ]


def branch_ledger() -> list[dict[str, str]]:
    """列出两个主要分支和结构回流。"""
    return [
        {
            "branch": SIEGEL_BRANCH,
            "needed_input": "排除 square-scale 危险半类中的实零偏置，或接受已认证的无 Siegel 零点/强 Linnik-2 型输入。",
            "current_status": "not proved in corpus; no peer-accepted unconditional no-Siegel-zero theorem is available",
            "why_hard": "实零项在 x=P^2 仍可与主项同阶，Deuring-Heilbronn 排斥其它零点但不直接删除该偏置。",
        },
        {
            "branch": NONREAL_BRANCH,
            "needed_input": "证明所有非实零点包在每个 a mod P 上不能相位同向吃掉主项。",
            "current_status": "not proved in corpus; GRH-shape, BV, full CRT average, and energy capacity are insufficient",
            "why_hard": "点态 residue 方向是 character simplex 的 rank-one evaluation；平均估计可留下单个异常方向。",
        },
        {
            "branch": TRIVIAL_BRANCH,
            "needed_input": "在前两项给出主项余量后，用显式公式常数账本吸收低阶项。",
            "current_status": "isolated as bookkeeping, not the frontier blocker",
            "why_hard": "没有前两项的正余量时，低阶项账本无法单独产生正性。",
        },
        {
            "branch": "structural fallback",
            "needed_input": "若解析零包分裂失败，反例链必须回到 PDEC scope、signed payload、ExactUV、RatePreservation 或 DStructure。",
            "current_status": "named fallback only; not a proof of row/column theorem",
            "why_hard": "有限 CRT 周期只给位置相位约束，不能生成角色零点相位或 actual signed payload 的全局抵消。",
        },
    ]


def accepted_input_status() -> list[dict[str, str]]:
    """区分已知外部定理、开放输入与当前不足输入。"""
    return [
        {
            "input": "Dirichlet character explicit formula",
            "status": "standard external theorem",
            "effect_here": "提供零点包分解，但不自动给 P^2 阈值正性。",
        },
        {
            "input": "classical zero-free region and Deuring-Heilbronn repulsion",
            "status": "standard external theorem family",
            "effect_here": "可组织 Siegel 分裂，但常数尺度仍不足以证明每个 residue 在 P^2 前命中。",
        },
        {
            "input": "Bombieri-Vinogradov / complete CRT uniformity",
            "status": "standard external theorem or identity",
            "effect_here": "平均控制，不排除单个 rank-one residue evaluation 方向。",
        },
        {
            "input": "GRH",
            "status": "unproved conjecture",
            "effect_here": "即便使用 GRH-shape O(P log^2 P)，仍大于 P 级主项，不能直接闭合 sharp P^2 正性。",
        },
        {
            "input": "No Siegel zero for all prime moduli",
            "status": "open; not peer-certified as an unconditional theorem",
            "effect_here": "若加上强常数量化，能删除实例外偏置分支的一大部分，但仍需处理非实零包。",
        },
        {
            "input": "Linnik exponent 2 / pointwise least prime <= P^2",
            "status": "open-level target in this corpus",
            "effect_here": "等价闭合列侧 AP 分支；不能作为已证引理回用。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造判定表。"""
    imported = previous.get("next_direct_attack_target") == ZERO_PACKET
    return [
        row(
            "PreviousZeroPacketHardPointImported",
            imported,
            False,
            "上一层已把 rank-one AP 正性压成显式零点包小于主项。",
            ZERO_PACKET,
        ),
        row(
            "ZeroPacketSiegelNonrealSplitClosed",
            True,
            True,
            "零点包被拆成实例外/Siegel 偏置、非实相位集中和低阶项三块；没有保留无名误差。",
            SIEGEL_SPLIT,
        ),
        row(
            "SiegelExceptionalBiasBranchClosed",
            False,
            False,
            "当前语料没有证明 square-scale 危险半类的实零偏置不可能吃掉主项。",
            SIEGEL_BRANCH,
        ),
        row(
            "NonrealZeroPacketPhaseBranchClosed",
            False,
            False,
            "当前语料没有证明非实零点包在每个 residue 上必有足够相位抵消。",
            NONREAL_BRANCH,
        ),
        row(
            "TrivialFiniteTermBookkeepingIsolated",
            True,
            True,
            "低阶项已从主硬点分离；它依赖前两块给出正余量后再由显式常数账本吸收。",
            TRIVIAL_BRANCH,
        ),
        row(
            "ClassicalAverageOrGRHShapeInputsSufficient",
            False,
            False,
            "BV、完整 CRT 平均、能量容量和 GRH 形状误差均不足以推出 x=P^2 的逐类正性。",
            f"{SIEGEL_BRANCH} AND {NONREAL_BRANCH}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步没有完成行/列命题无条件闭合；只把解析 AP 分支的剩余接口精确化。",
            "global final inputs remain open",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造路由证书。"""
    previous = load_json(DOCS / PREVIOUS_FRONTIER)
    rows = build_rows(previous)
    latest_basis = (
        f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR "
        f"({SIEGEL_BRANCH} AND {NONREAL_BRANCH})) "
        f"AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_explicit_ap_zero_packet_siegel_split_router",
        "status": "explicit_ap_zero_packet_split_into_siegel_and_nonreal_phase_branches_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "previous_target": ZERO_PACKET,
        "next_direct_attack_target": SIEGEL_SPLIT,
        "siegel_branch_target": SIEGEL_BRANCH,
        "nonreal_branch_target": NONREAL_BRANCH,
        "trivial_branch_target": TRIVIAL_BRANCH,
        "explicit_formula_split": explicit_formula_split(),
        "branch_ledger": branch_ledger(),
        "accepted_input_status": accepted_input_status(),
        "siegel_branch_closed": False,
        "nonreal_branch_closed": False,
        "trivial_terms_isolated": True,
        "classical_inputs_sufficient": False,
        "row_column_unconditional_closed": False,
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续攻击 `ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2`，"
            "把它拆成两个不可混淆的解析硬分支：实例外/Siegel 零点在 square-scale 的危险半类偏置，"
            "以及非实零点包在单个 residue evaluation 方向上的相位同向集中。"
            "低阶项已被分离为后续显式常数账本。当前没有证明这两条主分支，"
            "因此行/列命题仍未无条件闭合；但无名零包出口已被替换为可审计的 Siegel/非实相位二分。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Explicit AP Zero-packet / Siegel Split Router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"siegel_branch_closed={fmt_bool(result['siegel_branch_closed'])}",
        f"nonreal_branch_closed={fmt_bool(result['nonreal_branch_closed'])}",
        f"trivial_terms_isolated={fmt_bool(result['trivial_terms_isolated'])}",
        f"classical_inputs_sufficient={fmt_bool(result['classical_inputs_sufficient'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 零点包分裂",
        "",
        "| component | scale at x=P^2 | role |",
        "| --- | --- | --- |",
    ]
    for item in result["explicit_formula_split"]:
        lines.append(
            f"| `{table_cell(item['component'])}` | `{table_cell(item['scale_at_x_p2'])}` | "
            f"{table_cell(item['role'])} |"
        )

    lines += [
        "",
        "## 2. 分支账本",
        "",
        "| branch | needed input | current status | why hard |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["branch_ledger"]:
        lines.append(
            f"| `{table_cell(item['branch'])}` | {table_cell(item['needed_input'])} | "
            f"{table_cell(item['current_status'])} | {table_cell(item['why_hard'])} |"
        )

    lines += [
        "",
        "## 3. 外部输入状态",
        "",
        "| input | status | effect here |",
        "| --- | --- | --- |",
    ]
    for item in result["accepted_input_status"]:
        lines.append(
            f"| `{table_cell(item['input'])}` | {table_cell(item['status'])} | "
            f"{table_cell(item['effect_here'])} |"
        )

    lines += [
        "",
        "## 4. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | {table_cell(item['remaining'])} |"
        )

    lines += [
        "",
        "## 5. 最新活动基",
        "",
        "```text",
        result["latest_strict_activity_basis"],
        "```",
        "",
        "审稿边界：本文件不证明 Linnik=2、无 Siegel 零点、GRH 或行/列命题；它只把最新 AP 零包硬点拆成可复核的两个主分支，并关闭平均/容量/完整 CRT 直接替代点态正性的误用。",
        "",
        "## 6. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出路由证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "siegel_branch_closed": result["siegel_branch_closed"],
                "nonreal_branch_closed": result["nonreal_branch_closed"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
