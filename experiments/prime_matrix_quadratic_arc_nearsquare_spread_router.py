#!/usr/bin/env python3
"""Prime Matrix 二次圆弧到近平方条带扩散路由器。

用法示例：
  python3 experiments/prime_matrix_quadratic_arc_nearsquare_spread_router.py

输出：
  docs/monograph/prime-matrix-quadratic-arc-nearsquare-spread-router.json
  docs/monograph/prime-matrix-quadratic-arc-nearsquare-spread-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-exact-residue-sawtooth-normal-form-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-quadratic-arc-nearsquare-spread-router.json"
DEFAULT_MD = DOCS / "prime-matrix-quadratic-arc-nearsquare-spread-router.md"

OLD_ATOM = "RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000"
STRIP_ATOM = "SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000"
WEIGHT_SUPPORT_ATOM = "RosserWeightQuotientResidueSupportLedgerAlpha043"
EXTERNAL_DISPERSION_ATOM = "ExternalWellFactorableSawtoothDispersionBoundAlpha043"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def replace_atom(text: str, old: str, new: str) -> str:
    """替换输入基中的二次圆弧原子。"""
    return text.replace(old, new)


def replace_atom_or_external(text: str, old: str, external: str, new: str) -> str:
    """优先替换已有的 old OR external 包，避免重复外部原子。"""
    wrapped = f"({old} OR {external})"
    if wrapped in text:
        return text.replace(wrapped, new)
    return replace_atom(text, old, new)


def lower_event(p: int, d: int) -> dict[str, Any]:
    """minus 侧：rho=t^2 mod d 落入开弧 (0,t)。"""
    t = p % d
    h = p // d
    square = t * t
    a = square // d
    rho = square % d
    delta = h * square - a * (p - t)
    return {
        "side": "minus/lower",
        "P": p,
        "d": d,
        "h=floor(P/d)": h,
        "t=P mod d": t,
        "a=floor(t^2/d)": a,
        "rho": rho,
        "arc_event": 0 < rho < t,
        "near_square_event": 0 < square - a * d < t,
        "strip_delta": delta,
        "strip_event": 0 < delta < h * t,
    }


def upper_event(p: int, d: int) -> dict[str, Any]:
    """plus 侧：rho=-t^2 mod d 落入开弧 (0,t)。"""
    t = p % d
    h = p // d
    square = t * t
    a = (square + d - 1) // d
    rho = (-square) % d
    delta = a * (p - t) - h * square
    return {
        "side": "plus/upper",
        "P": p,
        "d": d,
        "h=floor(P/d)": h,
        "t=P mod d": t,
        "a=ceil(t^2/d)": a,
        "rho": rho,
        "arc_event": 0 < rho < t,
        "near_square_event": 0 < a * d - square < t,
        "strip_delta": delta,
        "strip_event": 0 < delta < h * t,
    }


def identity_samples() -> list[dict[str, Any]]:
    """给出样本，核验圆弧事件、近平方事件和商余条带事件等价。"""
    rows: list[dict[str, Any]] = []
    for p, d in [(101, 7), (101, 13), (103, 11), (107, 15), (109, 28), (127, 45)]:
        for item in (lower_event(p, d), upper_event(p, d)):
            item["all_equivalent"] = item["arc_event"] == item["near_square_event"] == item["strip_event"]
            rows.append(item)
    return rows


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


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成近平方扩散路由判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = OLD_ATOM in basis or previous.get("next_priority") == OLD_ATOM
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    exact_identity_closed = True
    quotient_lift_closed = True
    compression_closed = active and guard and exact_identity_closed and quotient_lift_closed
    return [
        row(
            "QuadraticArcDiscrepancyGateActive",
            active,
            False,
            "最新内部最窄点是 Rosser 权重下的二次圆弧偏差。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条内改写余项，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ArcHitIffNearSquareMultipleClosed",
            exact_identity_closed,
            True,
            "rho=±t^2 mod d 落入开弧 (0,t) 等价于 t^2 距某个 d 的倍数小于 t。",
            "无剩余。",
        ),
        row(
            "NearSquareLiftToQuotientResidueStripClosed",
            quotient_lift_closed,
            True,
            "再写 P=hd+t，近平方事件等价于 |h t^2-a(P-t)|<h t 的有向窄条带。",
            "无剩余。",
        ),
        row(
            "QuadraticArcCompressedToSignedNearSquareStrip",
            compression_closed,
            False,
            "旧二次圆弧偏差原子被压成带 Rosser 权重支撑账本的有符号近平方条带非集中。",
            f"{WEIGHT_SUPPORT_ATOM} AND {STRIP_ATOM}",
        ),
        row(
            WEIGHT_SUPPORT_ATOM,
            False,
            False,
            "需要把 lower weights 在 (h,t,a) 商余坐标中的支撑、符号和 well-factorable 分块登记清楚。",
            WEIGHT_SUPPORT_ATOM,
        ),
        row(
            STRIP_ATOM,
            False,
            False,
            "证明有符号 Rosser 质量不能在 |h t^2-a(P-t)|<h t 的窄条带上产生 0.90M 级负偏差。",
            STRIP_ATOM,
        ),
        row(
            EXTERNAL_DISPERSION_ATOM,
            False,
            False,
            "外部解析路线仍可直接给 well-factorable sawtooth/条带分散估计。",
            EXTERNAL_DISPERSION_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "短区间 rough-number 下界仍可绕过内部 sawtooth 与条带分析。",
            EXTERNAL_ROUGH_ATOM,
        ),
        row(
            EXTERNAL_DIBFI_ATOM,
            False,
            False,
            "generic/external DI/BFI 宽口径仍在 canonical 自足边界外。",
            EXTERNAL_DIBFI_ATOM,
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
    """执行二次圆弧到近平方条带扩散路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    compressed = next(
        bool(item["closed"]) for item in rows if item["gate"] == "QuadraticArcCompressedToSignedNearSquareStrip"
    )
    self_replacement = f"({WEIGHT_SUPPORT_ATOM} AND {STRIP_ATOM})"
    external_replacement = f"({self_replacement} OR {EXTERNAL_DISPERSION_ATOM})"
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), OLD_ATOM, self_replacement)
    latest_cond = replace_atom_or_external(
        previous.get("latest_conditional_basis", ""), OLD_ATOM, EXTERNAL_DISPERSION_ATOM, external_replacement
    )
    latest_global = replace_atom_or_external(
        previous.get("latest_global_with_external_basis", ""), OLD_ATOM, EXTERNAL_DISPERSION_ATOM, external_replacement
    )

    source_paths = list(paths.values())
    return {
        "certificate_type": "quadratic_arc_nearsquare_spread_router",
        "status": "quadratic_arc_discrepancy_compressed_to_signed_nearsquare_strip_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "arc_hit_iff_nearsquare_multiple_proved": True,
        "nearsquare_lift_to_quotient_residue_strip_proved": True,
        "quadratic_arc_discrepancy_compressed": compressed,
        "rosser_weight_quotient_residue_support_ledger_proved": False,
        "signed_nearsquare_strip_discrepancy_proved": False,
        "external_well_factorable_sawtooth_dispersion_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: self_replacement},
        "replacement_with_external_dispersion": {OLD_ATOM: external_replacement},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": WEIGHT_SUPPORT_ATOM,
        "secondary_priority": STRIP_ATOM,
        "external_next_priority": EXTERNAL_DISPERSION_ATOM,
        "rough_fallback_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "normal_forms": {
            "minus_lower": "0 < t^2-floor(t^2/d)d < t",
            "plus_upper": "0 < ceil(t^2/d)d-t^2 < t",
            "quotient_residue_lift": "P=hd+t, d=(P-t)/h, so both sides become 0<±(h t^2-a(P-t))<h t",
            "geometric_meaning": "圆柱斜线端点偏差等价于商余平面中的近平方窄条带穿越。",
        },
        "identity_samples": identity_samples(),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把二次圆弧偏差进一步压成近平方条带扩散。"
            "对 minus 侧，rho=t^2 mod d 落入 (0,t) 等价于 t^2 在某个 d 倍数上方距离小于 t；"
            "对 plus 侧，-t^2 mod d 落入 (0,t) 等价于 t^2 在某个 d 倍数下方距离小于 t。"
            "再用 P=hd+t 提升后，危险事件就是商余坐标中的有向窄条带 "
            "|h t^2-a(P-t)|<h t。"
            "因此剩余不是抽象相消，而是 Rosser 权重支撑在这些窄条带上的有符号非集中。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    self_replacement = next(iter(result["replacement_self_contained"].items()))
    external_replacement = next(iter(result["replacement_with_external_dispersion"].items()))
    nf = result["normal_forms"]
    lines = [
        "# Prime Matrix 二次圆弧到近平方条带扩散路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"arc_hit_iff_nearsquare_multiple_proved={fmt_bool(result['arc_hit_iff_nearsquare_multiple_proved'])}",
        (
            "nearsquare_lift_to_quotient_residue_strip_proved="
            f"{fmt_bool(result['nearsquare_lift_to_quotient_residue_strip_proved'])}"
        ),
        f"quadratic_arc_discrepancy_compressed={fmt_bool(result['quadratic_arc_discrepancy_compressed'])}",
        (
            "rosser_weight_quotient_residue_support_ledger_proved="
            f"{fmt_bool(result['rosser_weight_quotient_residue_support_ledger_proved'])}"
        ),
        f"signed_nearsquare_strip_discrepancy_proved={fmt_bool(result['signed_nearsquare_strip_discrepancy_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确等价",
        "",
        "令 `t=P mod d`，`P=hd+t`。对 `d>1`：",
        "",
        "```text",
        f"minus/lower: {nf['minus_lower']}",
        f"plus/upper:  {nf['plus_upper']}",
        f"lift:        {nf['quotient_residue_lift']}",
        "```",
        "",
        nf["geometric_meaning"],
        "",
        "## 2. 拆分律",
        "",
        "自足路线：",
        "",
        "```text",
        self_replacement[0],
        "  =>",
        self_replacement[1],
        "```",
        "",
        "允许外部分散输入：",
        "",
        "```text",
        external_replacement[0],
        "  =>",
        external_replacement[1],
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
            "## 4. 样本验算",
            "",
            "| P | d | side | h | t | a | rho | arc | near-square | strip | all |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |",
        ]
    )
    for item in result["identity_samples"]:
        a_key = "a=floor(t^2/d)" if "a=floor(t^2/d)" in item else "a=ceil(t^2/d)"
        lines.append(
            "| {P} | {d} | {side} | {h} | {t} | {a} | {rho} | `{arc}` | `{near}` | `{strip}` | `{all_eq}` |".format(
                P=item["P"],
                d=item["d"],
                side=item["side"],
                h=item["h=floor(P/d)"],
                t=item["t=P mod d"],
                a=item[a_key],
                rho=item["rho"],
                arc=fmt_bool(item["arc_event"]),
                near=fmt_bool(item["near_square_event"]),
                strip=fmt_bool(item["strip_event"]),
                all_eq=fmt_bool(item["all_equivalent"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 最新输入基",
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
            "## 6. 下一步",
            "",
            (
                f"先攻 `{result['next_priority']}`，把 Rosser 权重实际支撑搬到 `(h,t,a)` 条带坐标；"
                f"随后攻 `{result['secondary_priority']}` 的有符号非集中。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
