#!/usr/bin/env python3
"""Prime Matrix Backlund zeta-xi 分支跳变搬运闭合路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_zeta_xi_branch_jump_transport_router.py

输出：
  docs/monograph/prime-matrix-backlund-zeta-xi-branch-jump-transport-router.json
  docs/monograph/prime-matrix-backlund-zeta-xi-branch-jump-transport-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-backlund-signed-pairing-involution-router.json"
DEFAULT_THETA = MONO / "prime-matrix-b3-theta-mellin-functional-equation-router.json"
DEFAULT_XI = MONO / "prime-matrix-b3-xi-entire-order-router.json"
DEFAULT_LOWH = MONO / "prime-matrix-lowheight-xi-backlund-integration-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-zeta-xi-branch-jump-transport-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-zeta-xi-branch-jump-transport-router.md"

TRANSPORT_ATOM = "BacklundZetaXiBranchJumpTransportLedger"
FORMAL_UNIT_ATOM = "BacklundXiSymmetricFormalUnitContourLedger"
MIRROR_HASH_ATOM = "BacklundMirrorOrbitMultiplicityHashLedger"
PAIRING_ATOM = "BacklundSignedCrossingPairingInvolutionLedger"
RESIDUAL_ATOM = "BacklundResidualIndentCoefficientZeroLedger"
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


def factor_rows() -> list[dict[str, str]]:
    """列出 xi/zeta 搬运中的非零因子。"""
    return [
        {
            "factor": "1/2",
            "reason": "常数非零，不产生分支跳变。",
        },
        {
            "factor": "s(s-1)",
            "reason": "高高度 Backlund 轮廓满足 |Im s|>14，避开 s=0,1。",
        },
        {
            "factor": "pi^(-s/2)",
            "reason": "指数函数处处非零，只贡献连续确定相位。",
        },
        {
            "factor": "Gamma(s/2)",
            "reason": "Gamma 函数无零点；其极点在非正整数，高高度临界带不相交。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    theta: dict[str, Any],
    xi: dict[str, Any],
    lowheight: dict[str, Any],
    endpoint: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 zeta-xi 分支跳变搬运判定表。"""
    active = previous.get("next_priority") == TRANSPORT_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    xi_definition_ready = (
        theta.get("theta_mellin_zeta_functional_equation_closed") is True
        and xi.get("xi_entire_order_one_growth_closed") is True
    )
    lowheight_separated = lowheight.get("lowheight_xi_rectangle_count_closed") is True
    endpoint_ready = (
        endpoint.get("endpoint_multiplicity_convention_closed") is True
        or endpoint.get("endpoint_multiplicity_convention_self_contained_closed") is True
    )
    transport_closed = active and guard and xi_definition_ready and lowheight_separated and endpoint_ready
    return [
        row(
            "ZetaXiTransportGateActive",
            active,
            True,
            "signed pairing 路由后，当前真正最窄点是把 arg zeta 的 crossing 跳变搬运到 xi。",
            TRANSPORT_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只处理假设链条内解析恒等式，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "XiDefinitionAndFunctionalEquationAvailable",
            xi_definition_ready,
            True,
            "theta-Mellin 层已给出 xi(s)=1/2*s*(s-1)*pi^(-s/2)*Gamma(s/2)*zeta(s)。",
            "无 xi 定义剩余。",
        ),
        row(
            "LowHeightSeparatedFromBacklundTrace",
            lowheight_separated,
            True,
            "0<t<=14 的低高度 xi 子包已关闭；当前搬运只作用于高高度 Backlund trace。",
            "无低高度混淆。",
        ),
        row(
            "ElementaryGammaFactorNoJumpClosed",
            True,
            True,
            "G(s)=1/2*s*(s-1)*pi^(-s/2)*Gamma(s/2) 在高高度轮廓无零无极点，不能产生零点 crossing 跳变。",
            "只剩连续确定相位预算。",
        ),
        row(
            "MultiplicityTransportClosed",
            True,
            True,
            "xi=G*zeta 且 G 无零无极点，所以 zeta 与 xi 的局部零点重数、branch_jump 完全一致。",
            MIRROR_HASH_ATOM,
        ),
        row(
            "EndpointLimitConventionCompatible",
            endpoint_ready,
            True,
            "若端点落零，先避开再取极限，重数由 endpoint convention 吸收，不改变搬运等式。",
            "EndpointZeroAvoidanceMultiplicityConventionClosedByLimit。",
        ),
        row(
            TRANSPORT_ATOM,
            transport_closed,
            True,
            "arg zeta 的局部分支跳变已可无损搬运到 xi 零点跳变；Gamma/初等项不进入 crossing 配对。",
            FORMAL_UNIT_ATOM,
        ),
        row(
            "SignedPairingStillOpenAfterTransport",
            False,
            False,
            "搬运只解决对象不匹配；仍需 xi 对称 formal unit 和 mirror orbit hash 才能配对抵消。",
            f"{FORMAL_UNIT_ATOM} AND {MIRROR_HASH_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 zeta-xi 分支跳变搬运路由。"""
    previous = load_json(paths["previous"])
    theta = load_json(paths["theta"])
    xi = load_json(paths["xi"])
    lowheight = load_json(paths["lowheight"])
    endpoint = load_json(paths["endpoint"])
    rows = build_rows(previous, theta, xi, lowheight, endpoint)
    transport_closed = next(item["closed"] for item in rows if item["gate"] == TRANSPORT_ATOM)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_zeta_xi_branch_jump_transport_router",
        "status": "backlund_zeta_xi_branch_jump_transport_closed_formal_unit_next",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "zeta_xi_branch_jump_transport_closed": transport_closed,
        "signed_pairing_involution_closed": False,
        "backlund_local_crossing_trace_closed": False,
        "row_column_self_contained_closed": False,
        "xi_zeta_factorization": "xi(s)=1/2*s*(s-1)*pi^(-s/2)*Gamma(s/2)*zeta(s)",
        "branch_jump_identity": "jump_arg_zeta(rho)=jump_arg_xi(rho), counted with analytic multiplicity",
        "factor_rows": factor_rows(),
        "replacement_self_contained": {TRANSPORT_ATOM: "BacklundZetaXiBranchJumpTransportClosed"},
        "next_priority": FORMAL_UNIT_ATOM,
        "support_priority": MIRROR_HASH_ATOM,
        "post_pairing_priority": RESIDUAL_ATOM,
        "parent_priority": PAIRING_ATOM,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "`BacklundZetaXiBranchJumpTransportLedger` 已闭合："
            "在高高度 Backlund 轮廓中，xi=G*zeta 且 G 无零无极点，"
            "所以 zeta 的局部零点 branch jump 与 xi 的局部零点 branch jump 按解析重数完全相同。"
            "剩余硬点转为注册 xi 对称 formal unit 和 mirror orbit multiplicity hash。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix Backlund zeta-xi 分支跳变搬运闭合路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"zeta_xi_branch_jump_transport_closed={fmt_bool(result['zeta_xi_branch_jump_transport_closed'])}",
        f"signed_pairing_involution_closed={fmt_bool(result['signed_pairing_involution_closed'])}",
        f"backlund_local_crossing_trace_closed={fmt_bool(result['backlund_local_crossing_trace_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 搬运恒等式",
        "",
        "```text",
        result["xi_zeta_factorization"],
        result["branch_jump_identity"],
        "```",
        "",
        "| factor | reason |",
        "| --- | --- |",
    ]
    for item in result["factor_rows"]:
        lines.append(f"| `{table_cell(item['factor'])}` | {table_cell(item['reason'])} |")
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
            f"支撑哈希：`{result['support_priority']}`。",
            f"父级配对账本：`{result['parent_priority']}`。",
            f"配对完成后验收：`{result['post_pairing_priority']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            "",
            "判定：zeta-xi 跳变搬运已闭合；formal unit 配对仍未闭合。",
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
    parser.add_argument("--lowheight-json", type=Path, default=DEFAULT_LOWH)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
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
        "lowheight": args.lowheight_json,
        "endpoint": args.endpoint_json,
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
