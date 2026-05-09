#!/usr/bin/env python3
"""Prime Matrix Backlund signed crossing 配对 involution 路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_signed_pairing_involution_router.py

输出：
  docs/monograph/prime-matrix-backlund-signed-pairing-involution-router.json
  docs/monograph/prime-matrix-backlund-signed-pairing-involution-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-backlund-crossing-trace-capacity-router.json"
DEFAULT_THETA = MONO / "prime-matrix-b3-theta-mellin-functional-equation-router.json"
DEFAULT_XI = MONO / "prime-matrix-b3-xi-entire-order-router.json"
DEFAULT_HADAMARD = MONO / "prime-matrix-b3-hadamard-factorization-router.json"
DEFAULT_WINDING = MONO / "prime-matrix-xi-boundary-polygon-winding-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-signed-pairing-involution-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-signed-pairing-involution-router.md"

PAIRING_ATOM = "BacklundSignedCrossingPairingInvolutionLedger"
TRANSPORT_ATOM = "BacklundZetaXiBranchJumpTransportLedger"
FORMAL_UNIT_ATOM = "BacklundXiSymmetricFormalUnitContourLedger"
MIRROR_HASH_ATOM = "BacklundMirrorOrbitMultiplicityHashLedger"
RESIDUAL_ATOM = "BacklundResidualIndentCoefficientZeroLedger"
CLUSTER_ATOM = "BacklundCanonicalNearZeroClusterBoxLedger"
EXTERNAL_ATOM = "ClassicalBacklundZeroIndentationCostExternalAccepted"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


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


def lower_atoms() -> list[dict[str, str]]:
    """配对 involution 的下层原子。"""
    return [
        {
            "atom": TRANSPORT_ATOM,
            "role": "把 Backlund 原始 arg zeta 的 branch jump 无损搬运到 xi 语言，并把 Gamma/初等项列为无零确定相位。",
        },
        {
            "atom": FORMAL_UNIT_ATOM,
            "role": "登记同一 formal unit 内的 contour/homotopy 对 s->1-s 与共轭对称封闭。",
        },
        {
            "atom": MIRROR_HASH_ATOM,
            "role": "对每个近零 cluster 生成 rho,1-rho,conj rho,1-conj rho 的重数 orbit hash。",
        },
    ]


def direct_pairing_barriers() -> list[dict[str, str]]:
    """说明不能直接把低高度 winding 配对搬到 Backlund trace。"""
    return [
        {
            "barrier": "object_mismatch",
            "detail": "低高度绕数证书处理 xi 边界角变化；Backlund 凹口 trace 的原始硬项是 arg zeta。",
        },
        {
            "barrier": "contour_mismatch",
            "detail": "低高度是固定矩形且边界非零；Backlund 是随 T 移动的近零缩进/避让同伦。",
        },
        {
            "barrier": "budget_mismatch",
            "detail": "低高度绕数只证明总 winding；这里需要每个近零 crossing 的局部跳变量和残余成本 hash。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    theta: dict[str, Any],
    xi: dict[str, Any],
    hadamard: dict[str, Any],
    winding: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 signed pairing 判定表。"""
    active = previous.get("next_priority") == PAIRING_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    xi_symmetry_ready = (
        theta.get("theta_mellin_zeta_functional_equation_closed") is True
        and xi.get("xi_entire_order_one_growth_closed") is True
        and hadamard.get("hadamard_factorization_log_derivative_closed") is True
    )
    lowheight_pairing_model = winding.get("polygon_winding_zero_closed") is True
    direct_portability_blocked = True
    reduction_closed = active and guard and xi_symmetry_ready and lowheight_pairing_model
    return [
        row(
            "SignedPairingGateActive",
            active,
            True,
            "容量收缩后，当前下层最窄点是带符号 crossing 的配对 involution。",
            PAIRING_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在早期零行反例假设链条内处理解析 trace，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "XiSymmetricZeroOrbitAvailable",
            xi_symmetry_ready,
            True,
            "theta-Mellin 函数方程、xi 整函数性和 Hadamard 乘积给出零点 mirror orbit 的结构底座。",
            MIRROR_HASH_ATOM,
        ),
        row(
            "LowHeightWindingPairingImportedAsModelOnly",
            lowheight_pairing_model,
            True,
            "低高度 xi 多边形已用函数方程/共轭对称完成角变化配平，但它只能作为结构模型。",
            "不能直接替代高高度 Backlund trace。",
        ),
        row(
            "DirectLowHeightPairingPortabilityBlocked",
            direct_portability_blocked,
            True,
            "对象、轮廓和预算三重不匹配，直接套用低高度 winding 会混淆假设链条。",
            TRANSPORT_ATOM,
        ),
        row(
            "SignedPairingReducedToTransportAndFormalUnit",
            reduction_closed,
            False,
            "配对 involution 已压成 zeta->xi 跳变搬运、xi 对称 formal unit、mirror orbit hash 三包。",
            f"{TRANSPORT_ATOM} AND {FORMAL_UNIT_ATOM} AND {MIRROR_HASH_ATOM}",
        ),
        row(
            TRANSPORT_ATOM,
            False,
            False,
            "尚未证明 arg zeta 的局部 branch jump 可无损改写为 xi 零点跳变加显式无零相位。",
            TRANSPORT_ATOM,
        ),
        row(
            FORMAL_UNIT_ATOM,
            False,
            False,
            "尚未登记 Backlund 移动凹口 contour 在 s->1-s 与共轭下封闭。",
            FORMAL_UNIT_ATOM,
        ),
        row(
            MIRROR_HASH_ATOM,
            False,
            False,
            "尚未给出每个近零 cluster 的 mirror orbit multiplicity hash。",
            MIRROR_HASH_ATOM,
        ),
        row(
            PAIRING_ATOM,
            False,
            False,
            "三包闭合后才可证明 branch_jump 在同一 formal unit 内成对抵消。",
            RESIDUAL_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 signed pairing 路由。"""
    previous = load_json(paths["previous"])
    theta = load_json(paths["theta"])
    xi = load_json(paths["xi"])
    hadamard = load_json(paths["hadamard"])
    winding = load_json(paths["winding"])
    rows = build_rows(previous, theta, xi, hadamard, winding)
    reduction_closed = next(
        item["closed"] for item in rows if item["gate"] == "SignedPairingReducedToTransportAndFormalUnit"
    )
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_signed_pairing_involution_router",
        "status": "backlund_signed_pairing_reduced_to_zeta_xi_transport_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "signed_pairing_reduction_closed": reduction_closed,
        "backlund_signed_pairing_involution_closed": False,
        "backlund_local_crossing_trace_closed": False,
        "row_column_self_contained_closed": False,
        "direct_pairing_barriers": direct_pairing_barriers(),
        "lower_atoms": lower_atoms(),
        "replacement_self_contained": {
            PAIRING_ATOM: f"({TRANSPORT_ATOM} AND {FORMAL_UNIT_ATOM} AND {MIRROR_HASH_ATOM})"
        },
        "next_priority": TRANSPORT_ATOM,
        "support_priority": FORMAL_UNIT_ATOM,
        "hash_priority": MIRROR_HASH_ATOM,
        "post_pairing_priority": RESIDUAL_ATOM,
        "cluster_support_priority": CLUSTER_ATOM,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "signed crossing 配对不能直接从低高度 xi 绕数证书搬来。"
            "低高度证书证明固定非零边界的总角变化配平；当前 Backlund trace 处理的是高高度移动凹口中的 arg zeta 局部跳变。"
            "因此真正下层最窄点是先闭合 `BacklundZetaXiBranchJumpTransportLedger`："
            "把 zeta 分支跳变搬运到 xi 对称零点 orbit，再注册 formal unit 配对。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix Backlund signed crossing 配对 involution 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"signed_pairing_reduction_closed={fmt_bool(result['signed_pairing_reduction_closed'])}",
        (
            "backlund_signed_pairing_involution_closed="
            f"{fmt_bool(result['backlund_signed_pairing_involution_closed'])}"
        ),
        f"backlund_local_crossing_trace_closed={fmt_bool(result['backlund_local_crossing_trace_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 直接搬运障碍",
        "",
        "| barrier | detail |",
        "| --- | --- |",
    ]
    for item in result["direct_pairing_barriers"]:
        lines.append(f"| `{table_cell(item['barrier'])}` | {table_cell(item['detail'])} |")
    lines.extend(
        [
            "",
            "## 2. 自足替换",
            "",
            "```text",
            replacement[0],
            "  =>",
            replacement[1],
            "```",
            "",
            "| atom | role |",
            "| --- | --- |",
        ]
    )
    for item in result["lower_atoms"]:
        lines.append(f"| `{table_cell(item['atom'])}` | {table_cell(item['role'])} |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
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
            "## 4. 下一步",
            "",
            f"当前真正最窄点：`{result['next_priority']}`。",
            f"同时需要 formal unit 支撑：`{result['support_priority']}`。",
            f"cluster 哈希支撑：`{result['hash_priority']}`。",
            f"配对完成后验收：`{result['post_pairing_priority']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            "",
            "判定：配对 involution 已下压到 zeta-xi 跳变搬运；命题尚未自足闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--theta-json", type=Path, default=DEFAULT_THETA)
    parser.add_argument("--xi-json", type=Path, default=DEFAULT_XI)
    parser.add_argument("--hadamard-json", type=Path, default=DEFAULT_HADAMARD)
    parser.add_argument("--winding-json", type=Path, default=DEFAULT_WINDING)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "theta": args.theta_json,
        "xi": args.xi_json,
        "hadamard": args.hadamard_json,
        "winding": args.winding_json,
        "json_out": args.json_out,
        "md_out": args.md_out,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["next_priority"])


if __name__ == "__main__":
    main()
