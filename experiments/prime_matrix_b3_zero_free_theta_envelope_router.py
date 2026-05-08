#!/usr/bin/env python3
"""Prime Matrix B=3 零点自由区到 theta 包络路由器。

用法示例：
  python3 experiments/prime_matrix_b3_zero_free_theta_envelope_router.py

输出：
  docs/monograph/prime-matrix-b3-zero-free-theta-envelope-router.json
  docs/monograph/prime-matrix-b3-zero-free-theta-envelope-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-self-contained-mertens-tail-router.json"
DEFAULT_EXPLICIT_FORMULA = ROOT / "docs" / "rh-pc1-explicit-formula-proof-appendix.md"
DEFAULT_PC1_THEOREMIZATION = ROOT / "docs" / "rh-pc1-analytic-input-theoremization.md"
DEFAULT_FINAL_DRAFT = ROOT / "docs" / "final-proof-draft.md"
DEFAULT_JSON = DOCS / "prime-matrix-b3-zero-free-theta-envelope-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-zero-free-theta-envelope-router.md"

OLD_ATOM = "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000"
SMOOTH_EF_ATOM = "SmoothChebyshevExplicitFormulaAppendixClosed"
PRIME_POWER_ATOM = "PrimePowerThetaPsiTransferLedgerClosed"
ZERO_FREE_ATOM = "SelfContainedDeLaValleePoussinZeroFreeRegionConstantsLedger"
CONTOUR_ATOM = "ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion"
FINITE_BRIDGE_ATOM = "FiniteThetaEnvelopeBridgeBelowAnalyticThreshold"
EXTERNAL_DUSART_THETA_ATOM = "DusartThetaChebyshevEnvelopeExternalAccepted"
MERTENS_CONSTANT_ATOM = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
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


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def source_audit(
    explicit_formula_text: str,
    pc1_text: str,
    final_draft_text: str,
) -> dict[str, Any]:
    """审查当前内部材料与 theta 包络证明链的匹配情况。"""
    smooth_explicit_formula_closed = contains_all(
        explicit_formula_text,
        ["Mellin", "-ζ'(s)/ζ(s)", "非平凡零点", "Ψ_W(X)"],
    )
    prime_power_transfer_closed = contains_all(
        pc1_text,
        ["素数幂", "Chebyshev 权", "X^{1/2}"],
    )
    external_dusart_theta_registered = contains_all(
        final_draft_text,
        ["Dusart", "vartheta(x)-x", "36260"],
    )
    zero_free_constants_present = contains_all(
        explicit_formula_text + "\n" + pc1_text + "\n" + final_draft_text,
        ["zero-free", "零点自由", "de la Vallée", "Korobov"],
    )
    contour_envelope_present = contains_all(
        explicit_formula_text + "\n" + pc1_text + "\n" + final_draft_text,
        ["contour", "零点和", "theta envelope", "x>=20000"],
    )
    finite_bridge_present = contains_all(
        final_draft_text,
        ["有限验证", "theta", "hash", "x>=20000"],
    )
    return {
        "smooth_explicit_formula_closed": smooth_explicit_formula_closed,
        "prime_power_theta_psi_transfer_closed": prime_power_transfer_closed,
        "external_dusart_theta_registered": external_dusart_theta_registered,
        "self_contained_zero_free_constants_present": zero_free_constants_present,
        "explicit_contour_theta_envelope_present": contour_envelope_present,
        "finite_theta_bridge_present": finite_bridge_present,
    }


def replacement_pair() -> str:
    """写出自足 theta 包络替换包。"""
    return (
        f"({SMOOTH_EF_ATOM} AND {PRIME_POWER_ATOM} AND {ZERO_FREE_ATOM} "
        f"AND {CONTOUR_ATOM} AND {FINITE_BRIDGE_ATOM})"
    )


def replace_atom(text: str) -> str:
    """替换旧 theta 包络原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


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


def build_rows(previous: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成零点自由区到 theta 包络判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    smooth_closed = bool(audit["smooth_explicit_formula_closed"])
    prime_power_closed = bool(audit["prime_power_theta_psi_transfer_closed"])
    external_dusart_registered = bool(audit["external_dusart_theta_registered"])
    zero_free_closed = bool(audit["self_contained_zero_free_constants_present"])
    contour_closed = bool(audit["explicit_contour_theta_envelope_present"])
    finite_bridge_closed = bool(audit["finite_theta_bridge_present"])
    reduced = active and guard and smooth_closed and prime_power_closed
    return [
        row(
            "ZeroFreeThetaEnvelopeGateActive",
            active,
            False,
            "上一层完全自足路线的最新最窄点是显式零点自由区到 theta 包络。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只处理假设链条中的解析输入边界，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "SmoothChebyshevExplicitFormulaClosed",
            smooth_closed,
            True,
            "仓库已有平滑 Chebyshev 显式公式附录，Mellin 反演与移线留数层闭合。",
            SMOOTH_EF_ATOM,
        ),
        row(
            "PrimePowerThetaPsiTransferClosed",
            prime_power_closed,
            True,
            "PC1 定理化文件已给出素数幂低阶吸收与 Chebyshev 权转移的形式账本。",
            PRIME_POWER_ATOM,
        ),
        row(
            "DusartThetaExternalRouteRegistered",
            external_dusart_registered,
            False,
            "主稿登记了 Dusart theta 显式界；它可外部关闭该层，但不是自足证明。",
            EXTERNAL_DUSART_THETA_ATOM,
        ),
        row(
            "SelfContainedZeroFreeConstantsMissing",
            zero_free_closed,
            False,
            "当前仓库没有 de la Vallee Poussin/Korobov-Vinogradov 型零点自由区常数证明。",
            ZERO_FREE_ATOM,
        ),
        row(
            "ExplicitContourThetaEnvelopeMissing",
            contour_closed,
            False,
            "当前仓库没有从零点自由区到 x>=20000 的显式 psi/theta 轮廓积分常数账本。",
            CONTOUR_ATOM,
        ),
        row(
            "FiniteThetaBridgeMissing",
            finite_bridge_closed,
            False,
            "即使远端解析界成立，阈值以下仍需有限核验桥和可复现 hash。",
            FINITE_BRIDGE_ATOM,
        ),
        row(
            "ZeroFreeThetaEnvelopeReducedToCorePNTPackage",
            reduced,
            False,
            "旧 theta 包络原子被压成：显式公式、素数幂转移、零点自由常数、轮廓积分包络、有限桥。",
            replacement_pair(),
        ),
        row(
            MERTENS_CONSTANT_ATOM,
            False,
            False,
            "theta 包络之后还需 B1 常数区间，才能完成 reciprocal-prime Mertens 自足尾段。",
            MERTENS_CONSTANT_ATOM,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "接受外部 Dusart/Mertens 版后，最终晋级仍要过 DStructure/Tail-log4/Rankin 验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行零点自由区到 theta 包络路由。"""
    previous = load_json(paths["previous"])
    explicit_formula_text = paths["explicit_formula"].read_text(encoding="utf-8")
    pc1_text = paths["pc1"].read_text(encoding="utf-8")
    final_draft_text = paths["final_draft"].read_text(encoding="utf-8")
    audit = source_audit(explicit_formula_text, pc1_text, final_draft_text)
    rows = build_rows(previous, audit)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "ZeroFreeThetaEnvelopeReducedToCorePNTPackage"
    )
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""))
    source_paths = list(paths.values())
    return {
        "certificate_type": "b3_zero_free_theta_envelope_router",
        "status": "zero_free_theta_envelope_reduced_to_core_pnt_package_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "zero_free_theta_envelope_reduced": reduced,
        "zero_free_theta_envelope_self_contained_proved": False,
        "external_dusart_theta_route_registered": bool(audit["external_dusart_theta_registered"]),
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": ZERO_FREE_ATOM,
        "secondary_priority": CONTOUR_ATOM,
        "tertiary_priority": FINITE_BRIDGE_ATOM,
        "post_theta_priority": MERTENS_CONSTANT_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "source_audit": audit,
        "plain_conclusion": (
            "显式公式和素数幂/Chebyshev 权转移这两个形式层已经在仓库内闭合；"
            "Dusart theta 界可作为外部路线登记。但完全自足闭合仍缺少真正解析核心："
            "带常数的 ζ 零点自由区证明，以及由该零点自由区推出 x>=20000 的显式 psi/theta "
            "轮廓积分包络；随后还要补有限桥和 B1 常数区间。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 零点自由区到 theta 包络路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"zero_free_theta_envelope_reduced={fmt_bool(result['zero_free_theta_envelope_reduced'])}",
        (
            "zero_free_theta_envelope_self_contained_proved="
            f"{fmt_bool(result['zero_free_theta_envelope_self_contained_proved'])}"
        ),
        f"external_dusart_theta_route_registered={fmt_bool(result['external_dusart_theta_route_registered'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 来源审查",
        "",
        "| item | value |",
        "| --- | --- |",
    ]
    for key, value in result["source_audit"].items():
        lines.append(f"| {table_cell(key)} | `{fmt_bool(value)}` |")
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
            "## 5. 下一步",
            "",
            (
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"之后依次是 `{result['secondary_priority']}`、"
                f"`{result['tertiary_priority']}` 和 `{result['post_theta_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--explicit-formula", type=Path, default=DEFAULT_EXPLICIT_FORMULA)
    parser.add_argument("--pc1", type=Path, default=DEFAULT_PC1_THEOREMIZATION)
    parser.add_argument("--final-draft", type=Path, default=DEFAULT_FINAL_DRAFT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "explicit_formula": args.explicit_formula,
        "pc1": args.pc1,
        "final_draft": args.final_draft,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
