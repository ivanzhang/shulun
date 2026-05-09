#!/usr/bin/env python3
"""Prime Matrix B=3 Dusart 全局 theta 包络外部路由器。

用法示例：
  python3 experiments/prime_matrix_b3_dusart_global_theta_envelope_external_router.py

输出：
  docs/monograph/prime-matrix-b3-dusart-global-theta-envelope-external-router.json
  docs/monograph/prime-matrix-b3-dusart-global-theta-envelope-external-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-finite-low-height-external-router.json"
DEFAULT_THETA_TARGET = DOCS / "prime-matrix-b3-theta-target-dusart-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-dusart-global-theta-envelope-external-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-dusart-global-theta-envelope-external-router.md"

CONTOUR_ATOM = "ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion"
CONTOUR_CLOSED = "DusartThetaEnvelopeXGe20000ExternalClosedOneOver36260"
BRIDGE_ATOM = "FiniteThetaEnvelopeBridgeBelowAnalyticThreshold"
BRIDGE_CLOSED = "DusartThetaEnvelopeFiniteBridgeExternalClosedAllXPositive"
LOW_HEIGHT_CLOSED = "FiniteLowHeightZeroCheckExternalClosedFirstZeroGT14TuringComplete"
THETA_TARGET_CLOSED = "DusartThetaEnvelopeTargetAt20000ExternalClosedOneOver36260"
MERTENS_INTERVAL = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
INTERNAL_CONTOUR = "InternalZeroFreeRegionToThetaContourEnvelopeLedger"
INTERNAL_BRIDGE = "InternalFiniteThetaEnvelopeBridgeHashLedger"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ANCHOR_X = 20_000
TARGET_DENOMINATOR = 36_260
TARGET_RELATIVE_ERROR = 1.0 / TARGET_DENOMINATOR


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


def fmt_float(value: float) -> str:
    """固定小数格式。"""
    return f"{value:.12f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_external_atoms(text: str) -> str:
    """在外部路线输入基中替换 contour 与 finite bridge 两个原子。"""
    return text.replace(CONTOUR_ATOM, CONTOUR_CLOSED).replace(BRIDGE_ATOM, BRIDGE_CLOSED)


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def dusart_global_ready(theta_target: dict[str, Any]) -> bool:
    """确认 Dusart 外部 theta 全局界可复用到本层。"""
    statement = theta_target.get("external_theorem_statement", "")
    budget = theta_target.get("target_anchor_budget", {})
    return (
        theta_target.get("theta_target_external_closed") is True
        and "x>0" in statement
        and "x/36260" in statement
        and budget.get("matches_target_exactly") is True
    )


def build_rows(previous: dict[str, Any], theta_target: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Dusart 全局 theta 包络判定表。"""
    external_basis = previous.get("latest_external_titchmarsh_cn16_basis", "")
    self_basis = previous.get("latest_self_contained_basis", "")
    contour_active = previous.get("next_priority") == CONTOUR_ATOM and CONTOUR_ATOM in external_basis
    bridge_present = BRIDGE_ATOM in external_basis
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    low_height_ready = (
        previous.get("finite_low_height_external_closed") is True and LOW_HEIGHT_CLOSED in external_basis
    )
    dusart_ready = dusart_global_ready(theta_target) and THETA_TARGET_CLOSED in external_basis
    contour_closed = contour_active and guard and low_height_ready and dusart_ready
    bridge_closed = bridge_present and contour_closed
    return [
        row(
            "ExplicitContourEnvelopeGateActive",
            contour_active,
            True,
            "低高度核验之后，外部主链当前最窄点是 x>=20000 的显式 psi/theta 包络。",
            CONTOUR_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只补假设反例链条的解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "LowHeightAlreadyClosedExternally",
            low_height_ready,
            False,
            "上一层已用首零点/Turing 完备性关闭 T<=14 低高度核验。",
            LOW_HEIGHT_CLOSED,
        ),
        row(
            "DusartGlobalThetaEnvelopeAvailable",
            dusart_ready,
            False,
            "Dusart Proposition 5.1 的 theta 界对所有 x>0 成立，因此强于 x>=20000 的目标区间。",
            THETA_TARGET_CLOSED,
        ),
        row(
            CONTOUR_ATOM,
            contour_closed,
            False,
            "外部条件路线可用 Dusart 全局 theta 界旁路关闭该 x>=20000 包络；这不是内部 contour 常数证明。",
            CONTOUR_CLOSED,
        ),
        row(
            BRIDGE_ATOM,
            bridge_closed,
            False,
            "同一 Dusart 界对所有 x>0 成立，因此有限桥在外部路线中成为冗余并可关闭。",
            BRIDGE_CLOSED,
        ),
        row(
            "SelfContainedContourStillOpen",
            False,
            False,
            "严格自足路线仍需从零点自由区推导非平滑 psi/theta 轮廓常数。",
            INTERNAL_CONTOUR,
        ),
        row(
            "SelfContainedFiniteBridgeStillOpen",
            False,
            False,
            "严格自足路线仍需阈值以下 theta 包络有限核验和可复现 hash。",
            INTERNAL_BRIDGE,
        ),
        row(
            "SelfContainedBasisUnchanged",
            CONTOUR_ATOM in self_basis and BRIDGE_ATOM in self_basis,
            True,
            "本路由只替换外部输入基；自足输入基仍保留 contour 与 finite bridge 原子。",
            f"{CONTOUR_ATOM} AND {BRIDGE_ATOM}",
        ),
        row(
            "DStructureRankinGateStillSeparate",
            False,
            False,
            "theta 包络外部闭合不触动最终行列命题的 DStructure/Rankin 独立验收门。",
            DSTRUCTURE_GATE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Dusart 全局 theta 包络外部路由。"""
    previous = load_json(paths["previous"])
    theta_target = load_json(paths["theta_target"])
    rows = build_rows(previous, theta_target)
    contour_closed = next(item["closed"] for item in rows if item["gate"] == CONTOUR_ATOM)
    bridge_closed = next(item["closed"] for item in rows if item["gate"] == BRIDGE_ATOM)
    latest_external = replace_external_atoms(previous.get("latest_external_titchmarsh_cn16_basis", ""))
    return {
        "certificate_type": "b3_dusart_global_theta_envelope_external_router",
        "status": "dusart_global_theta_envelope_external_closed_self_contained_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "explicit_psi_theta_contour_envelope_external_closed": contour_closed,
        "finite_theta_bridge_external_closed": bridge_closed,
        "explicit_psi_theta_contour_envelope_self_contained_closed": False,
        "finite_theta_bridge_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "external_source": theta_target.get("external_source"),
        "external_url": theta_target.get("external_url"),
        "external_theorem_statement": theta_target.get("external_theorem_statement"),
        "target_denominator": TARGET_DENOMINATOR,
        "target_relative_error": TARGET_RELATIVE_ERROR,
        "anchor_x": ANCHOR_X,
        "replacement_external": {CONTOUR_ATOM: CONTOUR_CLOSED, BRIDGE_ATOM: BRIDGE_CLOSED},
        "latest_external_titchmarsh_cn16_basis": latest_external,
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "next_priority": MERTENS_INTERVAL,
        "parallel_self_contained_priorities": [INTERNAL_CONTOUR, INTERNAL_BRIDGE],
        "final_independent_acceptance_gate": DSTRUCTURE_GATE,
        "plain_conclusion": (
            "外部条件路线下，Dusart Proposition 5.1 的全局 theta 界 "
            "`vartheta(x)-x < x/36260 (x>0)` 同时关闭 `x>=20000` 的 theta 包络目标和阈值以下有限桥。"
            "这一步是外部定理旁路：不等于仓库内已经证明了零点自由区到非平滑 psi/theta 的轮廓常数，"
            "也不关闭严格自足路线或最终 DStructure/Rankin 守门项。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix B=3 Dusart 全局 theta 包络外部路由器",
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
            "explicit_psi_theta_contour_envelope_external_closed="
            f"{fmt_bool(result['explicit_psi_theta_contour_envelope_external_closed'])}"
        ),
        f"finite_theta_bridge_external_closed={fmt_bool(result['finite_theta_bridge_external_closed'])}",
        (
            "explicit_psi_theta_contour_envelope_self_contained_closed="
            f"{fmt_bool(result['explicit_psi_theta_contour_envelope_self_contained_closed'])}"
        ),
        f"finite_theta_bridge_self_contained_closed={fmt_bool(result['finite_theta_bridge_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部条件替换",
        "",
        "| old | new |",
        "| --- | --- |",
    ]
    for old, new in result["replacement_external"].items():
        lines.append(f"| `{old}` | `{new}` |")
    lines.extend(
        [
            "",
            "## 2. 外部引理内容",
            "",
            (
                "接受的外部引理为 Dusart Proposition 5.1："
                "`vartheta(x)-x < x/36260` 对所有 `x>0` 成立。"
            ),
            "",
            f"来源：{result['external_source']}。公共入口：{result['external_url']}。",
            "",
            "## 3. 目标常数",
            "",
            "| item | value |",
            "| --- | ---: |",
            f"| anchor x | `{result['anchor_x']}` |",
            f"| denominator | `{result['target_denominator']}` |",
            f"| relative error | `{result['target_relative_error']:.15f}` |",
            f"| Chebyshev multiplier | `{fmt_float(1.0 + result['target_relative_error'])}` |",
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            "## 5. 最新输入基",
            "",
            "外部 Titchmarsh+CN16 路线输入基：",
            "",
            "```text",
            result["latest_external_titchmarsh_cn16_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            (
                f"下一步攻 `{result['next_priority']}`。自足路线仍保留 "
                f"`{', '.join(result['parallel_self_contained_priorities'])}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--theta-target", type=Path, default=DEFAULT_THETA_TARGET)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous, "theta_target": args.theta_target}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
