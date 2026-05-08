#!/usr/bin/env python3
"""Prime Matrix 早期零行假设的矛盾矩阵路由器。

用法示例：
  python3 experiments/prime_matrix_early_zero_contradiction_matrix_router.py

输出：
  docs/monograph/prime-matrix-early-zero-contradiction-matrix-router.json
  docs/monograph/prime-matrix-early-zero-contradiction-matrix-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PHASE = DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json"
DEFAULT_CARRY = DOCS / "prime-matrix-early-zero-carry-shell-router.json"
DEFAULT_DEPTH = DOCS / "prime-matrix-early-zero-cofactor-depth-router.json"
DEFAULT_COLLAR = DOCS / "prime-matrix-early-zero-anchor-collar-router.json"
DEFAULT_NEAR = DOCS / "prime-matrix-near-zero-mirror-contradiction-router.json"
DEFAULT_CLB = DOCS / "prime-matrix-cylindrical-completion-line-barrier.md"
DEFAULT_PAW = DOCS / "prime-matrix-pcolumn-anchor-wheel-field.md"
DEFAULT_LAYERED = DOCS / "prime-matrix-dprc-cylindrical-layered-wheel-clamp.md"
DEFAULT_GEOMETRY = DOCS / "prime-matrix-clean-core-geometric-variation-branch-budget-router.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_SAE = DOCS / "prime-matrix-sae-to-local-survivor-pdec-absorption-router.md"
DEFAULT_COLUMN = DOCS / "prime-matrix-columncrt-to-pdec-sae-absorption-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-early-zero-contradiction-matrix-router.json"
DEFAULT_MD = DOCS / "prime-matrix-early-zero-contradiction-matrix-router.md"


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


def contradiction_rows(
    phase: dict[str, Any],
    carry: dict[str, Any],
    depth: dict[str, Any],
    collar: dict[str, Any],
    near: dict[str, Any],
    clb_text: str,
    paw_text: str,
    layered_text: str,
    geometry_text: str,
    pdec_text: str,
    sae_text: str,
    column_text: str,
) -> list[dict[str, Any]]:
    """生成早期零行与已有成果的矛盾矩阵。"""
    return [
        {
            "result": "CLB 完成斜线屏障",
            "forced_by_early_zero": "U_x=empty，因此 R_x=F_x。",
            "closed_fact": "CLB-1/2 分解与素数洞判别已闭合。",
            "contradiction_if": "CLB-FillerBound: |F_x|<|R_x|。",
            "current_status": "conditional_contradiction",
            "evidence": "CLB-FillerBound" in clb_text,
            "remaining": "全局 |F_x|<|R_x| 仍未证明。",
        },
        {
            "result": "近邻零行/镜像路线",
            "forced_by_early_zero": "早期零行会给 CRT 周期内短首尾镜像间隔。",
            "closed_fact": "直接镜像矛盾已被否定；保留路线是 BoundaryPhaseNoncoverageOrStableRecurrencePDEC。",
            "contradiction_if": "若能证明稳定短复现必排斥，或边界相位缺陷必排斥。",
            "current_status": "direct_contradiction_rejected_named_return",
            "evidence": near.get("retained_route") == "BoundaryPhaseNoncoverageOrStableRecurrencePDEC",
            "remaining": "不能再把镜像对称单独当最终矛盾。",
        },
        {
            "result": "同 formal unit 相位缺陷准入",
            "forced_by_early_zero": "R_x=F_x 可登记为 Omega=R_x, tau(c)=q(c), w(c)=1。",
            "closed_fact": "EarlyZeroPhaseDefectSchemaAdmission 已闭合。",
            "contradiction_if": "EarlyZeroTerminalExclusionPackage 全部闭合。",
            "current_status": "schema_closed_terminal_exclusion_open",
            "evidence": phase.get("early_zero_phase_defect_schema_admission_closed") is True,
            "remaining": phase.get("early_zero_branch_remaining", "EarlyZeroTerminalExclusionPackage"),
        },
        {
            "result": "carry-shell 精确支撑",
            "forced_by_early_zero": "每个高补洞满足 h=a+b-floor(ab/P), c=ab mod P。",
            "closed_fact": "ExactCarryShellIdentity 已闭合，底部带是 k=0 特例。",
            "contradiction_if": "CarryShellPrimitiveCapacityBound，或失败给 PDEC/SAE/ColumnCRT 回流。",
            "current_status": "support_geometry_closed_capacity_open",
            "evidence": carry.get("exact_carry_shell_identity_closed") is True,
            "remaining": carry.get("terminal_gap_after_router", "CarryShellPrimitiveCapacityBoundOrPDECReturn"),
        },
        {
            "result": "cofactor 深度门",
            "forced_by_early_zero": "m 是 x-rough cofactor；x>=sqrt(P) 时 m 必为素数。",
            "closed_fact": "SqrtGatePrimeCofactor 与复合 cofactor 递归回流已闭合。",
            "contradiction_if": "PrimePairCarryShellCapacityBound 与 CompositeCofactorDepthDescent 均闭合。",
            "current_status": "branch_split_closed_two_capacities_open",
            "evidence": depth.get("sqrt_gate_prime_cofactor_closed") is True,
            "remaining": depth.get("terminal_gap_after_router"),
        },
        {
            "result": "canonical anchor collar",
            "forced_by_early_zero": "真双素分支中最小高素锚满足 x<q<sqrt((x+1)P)，每条 q-fiber 长度 <sqrt(P)。",
            "closed_fact": "canonical_anchor_collar_closed 与 fiber_short_interval_reduction_closed 已闭合。",
            "contradiction_if": "AnchorCollarShortPrimeFiberUpperBound，或过载回流 PDEC/SAE/ColumnCRT。",
            "current_status": "strongest_current_narrow_frontier",
            "evidence": collar.get("canonical_anchor_collar_closed") is True,
            "remaining": collar.get("terminal_gap_after_router"),
        },
        {
            "result": "P 列锚与层叠轮",
            "forced_by_early_zero": "高补洞支付必须沿 P 列/圆柱相位转写为同一 payment/Phi 支撑。",
            "closed_fact": "P-column anchor、layered wheel 和几何 payment 字母表已登记。",
            "contradiction_if": "DPRC/FixedWheel/NewLayer/FlatDLS 输入全部闭合，或早期零行支付过载生成 PDEC。",
            "current_status": "geometry_ledger_closed_signed_budget_open",
            "evidence": "pcolumn_anchor_phi_skeleton" in geometry_text
            and "LayeredClamp" in layered_text
            and "P列" in paw_text,
            "remaining": "DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn",
        },
        {
            "result": "PDEC/SAE/ColumnCRT 终端家族",
            "forced_by_early_zero": "若覆盖压力集中、孤立或固定列位移复用，必须分别进入 PDEC、SAE/LocalSurvivor、ColumnCRT 吸收。",
            "closed_fact": "ColumnCRT 和 SAE 均不再是独立第四出口；PDEC 需要同 formal unit primitive schema。",
            "contradiction_if": "所有准入后的 primitive PDEC 容量不等式和 LocalSurvivor/SAE 证书闭合。",
            "current_status": "no_unnamed_exit_terminal_exclusion_open",
            "evidence": "未来 PDEC schema 准入条件" in pdec_text
            and "SAE 不是独立终端族" in sae_text
            and "ColumnCRT is not an independent terminal" in column_text,
            "remaining": "Primitive/Persistent PDEC budget + LocalSurvivor/SAE + displacement PDEC 排斥。",
        },
    ]


def run(
    phase_path: Path,
    carry_path: Path,
    depth_path: Path,
    collar_path: Path,
    near_path: Path,
    clb_path: Path,
    paw_path: Path,
    layered_path: Path,
    geometry_path: Path,
    pdec_path: Path,
    sae_path: Path,
    column_path: Path,
) -> dict[str, Any]:
    """执行早期零行矛盾矩阵路由。"""
    phase = load_json(phase_path)
    carry = load_json(carry_path)
    depth = load_json(depth_path)
    collar = load_json(collar_path)
    near = load_json(near_path)
    clb_text = clb_path.read_text(encoding="utf-8")
    paw_text = paw_path.read_text(encoding="utf-8")
    layered_text = layered_path.read_text(encoding="utf-8")
    geometry_text = geometry_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    sae_text = sae_path.read_text(encoding="utf-8")
    column_text = column_path.read_text(encoding="utf-8")
    rows = contradiction_rows(
        phase=phase,
        carry=carry,
        depth=depth,
        collar=collar,
        near=near,
        clb_text=clb_text,
        paw_text=paw_text,
        layered_text=layered_text,
        geometry_text=geometry_text,
        pdec_text=pdec_text,
        sae_text=sae_text,
        column_text=column_text,
    )
    paths = [
        phase_path,
        carry_path,
        depth_path,
        collar_path,
        near_path,
        clb_path,
        paw_path,
        layered_path,
        geometry_path,
        pdec_path,
        sae_path,
        column_path,
    ]
    open_rows = [row for row in rows if row["current_status"].endswith("_open") or "open" in row["current_status"]]
    contradiction_fronts = [
        {
            "front": "CLB residual-filler front",
            "early_zero_pressure": "早期零行把 CLB 的剩余洞集合压成 R_x=F_x。",
            "structural_conflict": "这与 CLB 的预期容量方向 |F_x|<|R_x| 正面冲突。",
            "closure_need": "证明全局 CLB-FillerBound，或把等量补完解释为 PDEC/SAE/ColumnCRT。",
        },
        {
            "front": "same-formal-unit front",
            "early_zero_pressure": "所有补洞必须登记在同一个 Omega=R_x、tau(c)=q(c)、w(c)=1 的 formal unit 中。",
            "structural_conflict": "任意拼接不同窗口、不同 q 层或不同重复口径的补洞不能再计入同一证明账本。",
            "closure_need": "关闭 EarlyZeroTerminalExclusionPackage。",
        },
        {
            "front": "carry-shell front",
            "early_zero_pressure": "每个高补洞必须满足 h=a+b-floor(ab/P), c=ab mod P。",
            "structural_conflict": "高素斜线不是自由扫过整行，而只能落在有限带进位壳；底部带还退化为 a+b=h。",
            "closure_need": "证明 carry-shell 容量不足，或持久/稀疏/位移失败回流命名终端。",
        },
        {
            "front": "cofactor-depth front",
            "early_zero_pressure": "m=P-b 是 x-rough cofactor，且 x>=sqrt(P) 时必为素数。",
            "structural_conflict": "复合 cofactor 只能躲在 x<sqrt(P) 的浅层递归壳里，不能作为大行段自由容量来源。",
            "closure_need": "关闭 CompositeCofactorDepthDescentOrNamedReturn 与 EarlyBandLocalSurvivorOrSAEExclusion。",
        },
        {
            "front": "anchor-collar short-fiber front",
            "early_zero_pressure": "真双素分支中最小锚满足 x<q<sqrt((x+1)P)，固定 q 后 m 的窗口长度 <sqrt(P)。",
            "structural_conflict": "全行补完要求大量极短素数纤维协同满载；集中则不是随机补洞，而是 PDEC/SAE/ColumnCRT 证据。",
            "closure_need": "当前最窄目标 AnchorCollarPrimeFiberCapacityBoundOrPDECReturn。",
        },
        {
            "front": "mirror-stability front",
            "early_zero_pressure": "完整 CRT 周期镜像只给边界短间隔，不能自动给独立矛盾。",
            "structural_conflict": "若强制短复现，则进入稳定位移缺陷；若无短复现，则进入边界相位非覆盖缺陷。",
            "closure_need": "排斥 stable recurrence PDEC/ColumnCRT 或 boundary phase defect PDEC/SAE。",
        },
        {
            "front": "P-column layered-wheel front",
            "early_zero_pressure": "补洞支付必须通过 P 列锚、圆柱相位和 layered wheel 的同一 Phi/payment 字母表转写。",
            "structural_conflict": "斜线覆盖的几何自由度被列锚和层叠轮筛锁住；任何同步失败必须命名回流。",
            "closure_need": "DPRC/FixedWheel/NewLayer/FlatDLS 与 signed geometric ledger 仍需最终排斥。",
        },
        {
            "front": "terminal no-fourth-exit front",
            "early_zero_pressure": "覆盖压力若集中、孤立或固定列位移复用，分别进入 PDEC、SAE/LocalSurvivor、ColumnCRT 吸收。",
            "structural_conflict": "早期零行没有未命名逃逸口；剩余只可能是已登记终端未排斥。",
            "closure_need": "Primitive/Persistent PDEC budget + LocalSurvivor/SAE + displacement PDEC 排斥。",
        },
    ]
    return {
        "certificate_type": "early_zero_contradiction_matrix_router",
        "status": "early_zero_forced_into_named_contradiction_matrix_unconditional_closure_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths},
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "no_unnamed_exit_for_early_zero": True,
        "strongest_current_frontier": "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn",
        "final_closure_package": [
            "AnchorCollarShortPrimeFiberUpperBound",
            "CompositeCofactorDepthDescentOrNamedReturn",
            "EarlyBandLocalSurvivorOrSAEExclusion",
            "PrimitivePDECBudgetForPersistentConcentration",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ],
        "rows": rows,
        "open_rows": [row["result"] for row in open_rows],
        "contradiction_fronts": contradiction_fronts,
        "usable_chain": [
            "EarlyZeroRowWithinP",
            "CLB residual equality R_x=F_x",
            "same-formal-unit phase ledger",
            "ExactCarryShellIdentity",
            "CofactorDepth split",
            "CanonicalAnchorCollar short prime fibers for x>=sqrt(P)",
            "AnchorCollar capacity deficit OR PDEC/SAE/ColumnCRT named return",
        ],
        "not_valid_as_final_contradictions": [
            "真实样本中未见早期零行不能替代假设分支证明。",
            "完整 CRT 镜像对称只给等价边界短间隔，不能单独推出矛盾。",
            "从一个零行自动推出下一个零行很近没有已证机制。",
            "P^2±k 或层叠轮同余刚性只提供补洞通道限制，单独还不是全局容量排斥。",
        ],
        "structural_law": (
            "An assumed early zero row is now incompatible with the existing theory except "
            "through named terminal inputs. CLB forces R_x=F_x; schema admission registers "
            "that equality in one formal unit; carry-shell and cofactor-depth collapse high "
            "fillers to finite shells; in the large branch, canonical anchors live in a short "
            "collar and each fiber has length <sqrt(P). Mirror symmetry does not give a direct "
            "contradiction, but it routes to stable recurrence or boundary phase defect. Thus "
            "there is no unnamed escape, while unconditional closure still needs the listed "
            "capacity/terminal exclusions."
        ),
        "plain_conclusion": (
            "假设早期零行目前已经被所有已建模型夹到命名终端里：它不再能作为自由覆盖现象存在。"
            "但现有成果还没有给出无条件矛盾；真正未闭合的是 anchor-collar 短素数纤维容量、"
            "早期复合 cofactor 递归下降、LocalSurvivor/SAE 与 primitive PDEC 容量排斥。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 早期零行假设的矛盾矩阵路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"no_unnamed_exit_for_early_zero={fmt_bool(result['no_unnamed_exit_for_early_zero'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"strongest_current_frontier={result['strongest_current_frontier']}",
        "```",
        "",
        "## 1. 矛盾矩阵",
        "",
        "| existing result | forced by early zero | closed fact | contradiction if | status | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| {result_name} | {forced} | {closed} | {contradiction_if} | `{status}` | {remaining} |".format(
                result_name=table_cell(row["result"]),
                forced=table_cell(row["forced_by_early_zero"]),
                closed=table_cell(row["closed_fact"]),
                contradiction_if=table_cell(row["contradiction_if"]),
                status=table_cell(row["current_status"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 已形成的结构夹击",
            "",
            "| front | early-zero pressure | structural conflict | closure need |",
            "| --- | --- | --- | --- |",
        ]
    )
    for front in result["contradiction_fronts"]:
        lines.append(
            "| {front} | {pressure} | {conflict} | {need} |".format(
                front=table_cell(front["front"]),
                pressure=table_cell(front["early_zero_pressure"]),
                conflict=table_cell(front["structural_conflict"]),
                need=table_cell(front["closure_need"]),
            )
        )
    lines.extend(
        [
            "",
            "这些不是八个彼此独立的新假设，而是同一反例分支被连续压缩后的八个夹击面：",
            "CLB 先把零行变成 `R_x=F_x`，formal unit 规定只能在同一账本计量，carry-shell 和 cofactor-depth 把补洞支撑压成有限壳，anchor collar 再把大行段压到极短素数纤维。",
            "因此早期零行若存在，已经不是自由的斜线覆盖现象；它必须表现为短纤维满载、持久低模集中、孤立 survivor 或固定列位移复用。",
            "",
            "## 3. 当前最强结论",
            "",
            "早期零行假设已经与以下结构同时绑定：",
            "",
            "```text",
        ]
    )
    lines.extend(f"  => {step}" if index else step for index, step in enumerate(result["usable_chain"]))
    lines.extend(
        [
            "```",
            "",
            "所以它已经和“任意斜线覆盖”直觉矛盾：高补洞必须同时满足同 formal unit、带进位壳、cofactor 深度、canonical collar 和短素数纤维五层刚性。",
            "但这些刚性本身还没有自动给出 `R_x` 不可全覆盖的最终容量不等式。",
            "",
            "## 4. 不能再作为最终矛盾的路线",
            "",
        ]
    )
    for item in result["not_valid_as_final_contradictions"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "这些路线仍可作为路由器和证据来源，但不能在正文中直接写成无条件终局矛盾。",
            "",
            "## 5. 剩余闭合包",
            "",
            "要把上述命名夹击升级为无条件矛盾，还需要关闭：",
            "",
            "```text",
        ]
    )
    lines.extend(result["final_closure_package"])
    lines.extend(
        [
            "```",
            "",
            "当前最窄优先级仍是：",
            "",
            "```text",
            result["strongest_current_frontier"],
            "```",
            "",
            "也就是证明 anchor collar 中所有长度 `<sqrt(P)` 的短素数纤维总容量不能覆盖整个 `R_x`，或证明任何覆盖级过载都会进入已命名且可排斥的 PDEC/SAE/ColumnCRT。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase-json", type=Path, default=DEFAULT_PHASE)
    parser.add_argument("--carry-json", type=Path, default=DEFAULT_CARRY)
    parser.add_argument("--depth-json", type=Path, default=DEFAULT_DEPTH)
    parser.add_argument("--collar-json", type=Path, default=DEFAULT_COLLAR)
    parser.add_argument("--near-json", type=Path, default=DEFAULT_NEAR)
    parser.add_argument("--clb-md", type=Path, default=DEFAULT_CLB)
    parser.add_argument("--paw-md", type=Path, default=DEFAULT_PAW)
    parser.add_argument("--layered-md", type=Path, default=DEFAULT_LAYERED)
    parser.add_argument("--geometry-md", type=Path, default=DEFAULT_GEOMETRY)
    parser.add_argument("--pdec-md", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sae-md", type=Path, default=DEFAULT_SAE)
    parser.add_argument("--column-md", type=Path, default=DEFAULT_COLUMN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()
    result = run(
        phase_path=args.phase_json,
        carry_path=args.carry_json,
        depth_path=args.depth_json,
        collar_path=args.collar_json,
        near_path=args.near_json,
        clb_path=args.clb_md,
        paw_path=args.paw_md,
        layered_path=args.layered_md,
        geometry_path=args.geometry_md,
        pdec_path=args.pdec_md,
        sae_path=args.sae_md,
        column_path=args.column_md,
    )
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)


if __name__ == "__main__":
    main()
