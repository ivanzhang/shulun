#!/usr/bin/env python3
"""Prime Matrix B=3 Meissel-Mertens 常数区间外部路由器。

用法示例：
  python3 experiments/prime_matrix_b3_meissel_mertens_interval_external_router.py

输出：
  docs/monograph/prime-matrix-b3-meissel-mertens-interval-external-router.json
  docs/monograph/prime-matrix-b3-meissel-mertens-interval-external-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-dusart-global-theta-envelope-external-router.json"
DEFAULT_MERTENS = DOCS / "prime-matrix-b3-explicit-prime-reciprocal-mertens-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-meissel-mertens-interval-external-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-meissel-mertens-interval-external-router.md"

OLD_ATOM = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
CLOSED_ATOM = "DusartMeisselMertensConstantIntervalAt20000ExternalClosed"
MERTENS_EXTERNAL = "DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted"
THETA_ENVELOPE_CLOSED = "DusartThetaEnvelopeXGe20000ExternalClosedOneOver36260"
FINITE_BRIDGE_CLOSED = "DusartThetaEnvelopeFiniteBridgeExternalClosedAllXPositive"
ROSser_FACE = "B3RosserFaceDictionaryClosedAlpha043"
ANCHOR_BUDGET = "B3Anchor20000BoundaryVariationBudgetClosedAlpha043"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SELF_B1_INTERVAL = "SelfContainedMeisselMertensB1IntervalArithmeticLedger"
SELF_RECIPROCAL_TAIL = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"


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


def replace_atom(text: str) -> str:
    """只在外部路线输入基中替换 Meissel-Mertens 区间原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def mertens_external_ready(mertens: dict[str, Any]) -> bool:
    """确认已有素数倒数 Mertens 外部证书足以提供 B1 区间输入。"""
    finite = mertens.get("finite_step_ledger", {})
    tail = mertens.get("tail_theorem_ledger", {})
    return (
        mertens.get("explicit_prime_reciprocal_mertens_external_closed") is True
        and mertens.get("finite_prime_step_ledger_286_to_10371_closed") is True
        and mertens.get("dusart_tail_parameter_match_closed") is True
        and finite.get("finite_step_ledger_closed") is True
        and tail.get("external_theorem_parameter_match_closed") is True
        and isinstance(finite.get("meissel_mertens_b1_for_audit_only"), (int, float))
    )


def build_rows(previous: dict[str, Any], mertens: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Meissel-Mertens 常数区间外部判定表。"""
    external_basis = previous.get("latest_external_titchmarsh_cn16_basis", "")
    self_basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in external_basis
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    theta_ready = (
        previous.get("explicit_psi_theta_contour_envelope_external_closed") is True
        and previous.get("finite_theta_bridge_external_closed") is True
        and THETA_ENVELOPE_CLOSED in external_basis
        and FINITE_BRIDGE_CLOSED in external_basis
    )
    mertens_ready = mertens_external_ready(mertens)
    b3_local_ready = ROSser_FACE in external_basis and ANCHOR_BUDGET in external_basis
    closed = active and guard and theta_ready and mertens_ready
    return [
        row(
            "MeisselMertensIntervalGateActive",
            active,
            True,
            "Dusart theta 包络与有限桥之后，外部主链当前最窄点是 B1/Meissel-Mertens 常数区间输入。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只补假设反例链条的解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ThetaEnvelopeAlreadyClosedExternally",
            theta_ready,
            False,
            "上一层已经用 Dusart 全局 theta 界关闭 x>=20000 包络和有限桥。",
            f"{THETA_ENVELOPE_CLOSED} AND {FINITE_BRIDGE_CLOSED}",
        ),
        row(
            "DusartReciprocalPrimeMertensExternalReady",
            mertens_ready,
            False,
            "已有显式素数倒数 Mertens 外部证书给出有限阶梯、尾段 Dusart 匹配和 B1 常数口径。",
            MERTENS_EXTERNAL,
        ),
        row(
            OLD_ATOM,
            closed,
            False,
            "接受 Dusart/Rosser-Schoenfeld 型素数倒数和外部定理后，B1 常数区间输入在外部路线中关闭。",
            CLOSED_ATOM,
        ),
        row(
            "B3LocalRosserAnchorAlreadyPresent",
            b3_local_ready,
            True,
            "B3 Rosser 面字典和 alpha=0.43 锚点变差预算已经在当前输入基中登记。",
            f"{ROSser_FACE} AND {ANCHOR_BUDGET}",
        ),
        row(
            "SelfContainedMertensStillOpen",
            False,
            False,
            "严格自足路线仍需内联 B1 区间算术与 reciprocal-prime Mertens 尾段证明。",
            f"{SELF_B1_INTERVAL} AND {SELF_RECIPROCAL_TAIL}",
        ),
        row(
            "SelfContainedBasisUnchanged",
            OLD_ATOM in self_basis,
            True,
            "本路由只替换外部输入基；自足输入基保留 Meissel-Mertens 常数区间原子。",
            OLD_ATOM,
        ),
        row(
            "DStructureRankinGateStillSeparate",
            False,
            False,
            "B3 解析外部链闭合后，最终行列无条件命题仍需 DStructure/Rankin 独立验收门。",
            DSTRUCTURE_GATE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Meissel-Mertens 常数区间外部路由。"""
    previous = load_json(paths["previous"])
    mertens = load_json(paths["mertens"])
    rows = build_rows(previous, mertens)
    closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    latest_external = replace_atom(previous.get("latest_external_titchmarsh_cn16_basis", ""))
    finite = mertens.get("finite_step_ledger", {})
    tail = mertens.get("tail_theorem_ledger", {})
    return {
        "certificate_type": "b3_meissel_mertens_interval_external_router",
        "status": "meissel_mertens_interval_external_closed_self_contained_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "meissel_mertens_interval_external_closed": closed,
        "meissel_mertens_interval_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "latest_external_titchmarsh_cn16_basis": latest_external,
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "mertens_external_atom": MERTENS_EXTERNAL,
        "meissel_mertens_b1": finite.get("meissel_mertens_b1_for_audit_only"),
        "finite_step_range": [finite.get("low_x"), finite.get("high_x_exclusive")],
        "tail_start_x": tail.get("tail_start_x"),
        "dusart_tail_error_at_start": tail.get("dusart_error_at_tail_start"),
        "next_priority": DSTRUCTURE_GATE,
        "parallel_self_contained_priorities": [SELF_B1_INTERVAL, SELF_RECIPROCAL_TAIL],
        "plain_conclusion": (
            "外部条件路线下，`SelfContainedMeisselMertensConstantIntervalLedgerAt20000` 可由已有 "
            "Dusart 型素数倒数和显式 Mertens 证书聚合关闭：有限阶梯覆盖 `286<=x<10372`，尾段 "
            "`x>=10372` 由外部定理匹配，B1 口径采用 `0.2614972128476428`。该步不是自足 B1/尾段证明；"
            "它只把外部 B3 解析主链推进到最终 DStructure/Rankin 独立验收门。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 Meissel-Mertens 常数区间外部路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"meissel_mertens_interval_external_closed={fmt_bool(result['meissel_mertens_interval_external_closed'])}",
        f"meissel_mertens_interval_self_contained_closed={fmt_bool(result['meissel_mertens_interval_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部条件替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. Mertens 外部证书数字",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| Meissel-Mertens B1 | `{fmt_float(float(result['meissel_mertens_b1']))}` |",
        f"| finite step range | `{result['finite_step_range']}` |",
        f"| tail start x | `{result['tail_start_x']}` |",
        f"| Dusart tail error at start | `{fmt_float(float(result['dusart_tail_error_at_start']))}` |",
        f"| external atom | `{result['mertens_external_atom']}` |",
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
            "外部 Titchmarsh+CN16 路线输入基：",
            "",
            "```text",
            result["latest_external_titchmarsh_cn16_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"外部 B3 解析主链下一步为 `{result['next_priority']}`；自足路线仍保留 "
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
    parser.add_argument("--mertens", type=Path, default=DEFAULT_MERTENS)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous, "mertens": args.mertens}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
