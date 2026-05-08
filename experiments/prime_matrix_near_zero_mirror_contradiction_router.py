#!/usr/bin/env python3
"""Prime Matrix 近邻零行与 CRT 镜像矛盾路线审计。

用法示例：
  python3 experiments/prime_matrix_near_zero_mirror_contradiction_router.py

输出：
  docs/monograph/prime-matrix-near-zero-mirror-contradiction-router.json
  docs/monograph/prime-matrix-near-zero-mirror-contradiction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_CURRENT = DOCS / "prime-matrix-clean-core-newlayer-pdec-projection-router.json"
DEFAULT_P23 = DOCS / "prime-matrix-p23-zero-recurrence-audit.json"
DEFAULT_SHORT = DOCS / "prime-matrix-short-recurrence-gap-audit.json"
DEFAULT_RECURSIVE = DOCS / "prime-matrix-recursive-mirror-descent-audit.json"
DEFAULT_ANNULUS = DOCS / "prime-matrix-annulus-mirror-localization-audit.json"
DEFAULT_JSON = DOCS / "prime-matrix-near-zero-mirror-contradiction-router.json"
DEFAULT_MD = DOCS / "prime-matrix-near-zero-mirror-contradiction-router.md"


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


def gate_rows(
    p23: dict[str, Any],
    short_gap: dict[str, Any],
    recursive: dict[str, Any],
    annulus: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成近邻零行镜像路线的判定表。"""
    p23_summary = p23["summary"]
    rec_summary = recursive["summary"]
    ann_summary = annulus["summary"]
    return [
        {
            "gate": "FullPeriodMirrorSymmetry",
            "closed": bool(p23_summary.get("symmetry_ok")),
            "verdict": "usable_but_period_internal_only",
            "meaning": "完整 CRT 行周期内零行集合关于周期中心镜像对称。",
            "consequence": "给出镜像配对，但不限制中间还可有多少零行。",
        },
        {
            "gate": "AutomaticNearNextZeroFromOneEarlyZero",
            "closed": False,
            "verdict": "not_proved_and_p23_warns_against_short_step",
            "meaning": "从一个零行自动推出下一个零行很近，需要额外稳定性。",
            "consequence": (
                f"P=23 首零行 {p23['parameters']['first_zero_row']} 后首次复现为 "
                f"{p23_summary['first_recurrence_before_mirror']}，平移 "
                f"{p23_summary['first_recurrence_shift']}；row 118=2*59 不是零行。"
            ),
        },
        {
            "gate": "GlobalShortRecurrenceExclusion",
            "closed": False,
            "verdict": "false",
            "meaning": "任意两个零行都不能在 2P 内复现这一强命题为假。",
            "consequence": short_gap.get("structural_conclusion", ""),
        },
        {
            "gate": "BoundaryShortWrapExclusion",
            "closed": True,
            "verdict": "equivalent_to_target_not_independent",
            "meaning": "首尾跨周期间隔由镜像等于 2r0-1。",
            "consequence": "边界 2P 短复现禁止等价于首零行 r0>P，不能作为独立证明出口。",
        },
        {
            "gate": "MirrorRecursionToSmallerMatrix",
            "closed": False,
            "verdict": "blocked",
            "meaning": "完整周期镜像偶性不能递归推出更小素数方阵零行。",
            "consequence": (
                f"样本中有完整周期零行的顶层对 {len(rec_summary['pairs_with_top_full_period_zero_rows'])} 个，"
                f"实际较小方阵早期零行 {len(rec_summary['pairs_with_actual_smaller_matrix_zero_rows'])} 个。"
            ),
        },
        {
            "gate": "AnnulusTerminalMirrorToZeroRow",
            "closed": False,
            "verdict": "nonzero_class_terminal_not_zero_row",
            "meaning": "n -> q^2-n 落到早期区间时，覆盖条件变成 q^2 mod ell 非零类。",
            "consequence": (
                f"环带镜像行号命中 {ann_summary['total_annulus_crt_mirror_row_number_hits_smaller_matrix_rows']} 次，"
                f"实际成为更小方阵零行 {ann_summary['total_annulus_crt_mirror_actual_smaller_zero_hits']} 次。"
            ),
        },
        {
            "gate": "UsableWeakRoute",
            "closed": True,
            "verdict": "boundary_phase_noncoverage_or_stable_recurrence_return",
            "meaning": "可用方向是首端帽边界非覆盖，或证明早期零行强制稳定短复现后回流 PDEC/SAE/ColumnCRT。",
            "consequence": "若没有稳定性，零行复现只是稀疏 CRT 相位证书集；若有稳定性，则形成命名结构缺陷。",
        },
    ]


def run(
    current_path: Path,
    p23_path: Path,
    short_path: Path,
    recursive_path: Path,
    annulus_path: Path,
) -> dict[str, Any]:
    """执行近邻零行镜像矛盾路线审计。"""
    paths = [current_path, p23_path, short_path, recursive_path, annulus_path]
    current = load_json(current_path)
    p23 = load_json(p23_path)
    short_gap = load_json(short_path)
    recursive = load_json(recursive_path)
    annulus = load_json(annulus_path)
    rows = gate_rows(p23, short_gap, recursive, annulus)
    return {
        "certificate_type": "near_zero_mirror_contradiction_router",
        "status": "direct_near_zero_mirror_contradiction_rejected_boundary_phase_route_retained",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths},
        "current_remaining_basis": current.get("latest_self_contained_basis", ""),
        "current_terminal_gap": current.get("terminal_gap_after_router"),
        "row_column_unconditional_closed": False,
        "direct_contradiction_from_near_next_zero_and_mirror": False,
        "retained_route": "BoundaryPhaseNoncoverageOrStableRecurrencePDEC",
        "rows": rows,
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "blocked_gates": [row["gate"] for row in rows if not row["closed"]],
        "structural_law": (
            "A zero row is a CRT phase certificate, not a point in an arithmetic progression "
            "of zero rows. Full-period reflection pairs every certificate with its mirror, "
            "but it does not force a nearby second certificate. The strong global no-short-"
            "recurrence statement is false, while the boundary no-short-wrap statement is "
            "equivalent to the desired first-zero delay. Therefore the proposed contradiction "
            "can close only after an additional stability lemma: an early zero row must force "
            "a stable short recurrence or a same-formal-unit phase defect. Without that input "
            "the correct target is boundary phase noncoverage and high-prime patching delay."
        ),
        "plain_conclusion": (
            "不能直接从“P 行以内有非平凡零行”推出“下一个零行很近并与镜像对称矛盾”。"
            "镜像对称是真的，但只给周期内配对；近邻复现没有自动性。可保留的硬攻方向是："
            "证明早期零行若存在就必须产生稳定短复现/PDEC 缺陷，或直接证明首端帽边界相位非覆盖。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 近邻零行与 CRT 镜像矛盾路线审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"direct_contradiction_from_near_next_zero_and_mirror={fmt_bool(result['direct_contradiction_from_near_next_zero_and_mirror'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"retained_route={result['retained_route']}",
        "```",
        "",
        "## 1. 当前剩余",
        "",
        "当前完全自足剩余仍为：",
        "",
        "```text",
        result["current_remaining_basis"],
        "```",
        "",
        "本轮回顾不改变 new-layer/DLS/source 输入基；它只审查“近邻零行 + 镜像对称”能否成为独立闭合矛盾。",
        "",
        "## 2. 结构律",
        "",
        result["structural_law"],
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | verdict | meaning | consequence |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{verdict}` | {meaning} | {consequence} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                verdict=table_cell(row["verdict"]),
                meaning=table_cell(row["meaning"]),
                consequence=table_cell(row["consequence"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 对用户路线的精确结论",
            "",
            "用户路线中可严格保留的部分：",
            "",
            "- 完整 CRT 周期零行集合有镜像对称。",
            "- 若首零行行号为 `r0`，跨周期首尾镜像间隔为 `2r0-1`。",
            "- 因而 `r0<=P` 等价于边界跨周期出现 `<=2P-1` 的短间隔。",
            "",
            "不能直接使用的部分：",
            "",
            "- 周期内部存在短复现的全局禁止命题是假的；P=23 有多对间隔不超过 `2P` 的零行。",
            "- 从一个早期零行自动推出“下一个零行很近”没有已证机制；P=23 的首零行后首次复现平移为 `2553`，且 `2r0` 不是零行。",
            "- 镜像递归不会自动给出更小素数方阵零行；剥层会复活洞，`q^2-n` 反射变成非零类终端块。",
            "",
            "因此下一步若继续利用这条思路，最窄命题应改写为：",
            "",
            "```text",
            "EarlyZeroRowWithinP",
            "  => StableShortRecurrencePDEC/SAE/ColumnCRT",
            "     OR BoundaryPhaseNoncoverageFailure.",
            "```",
            "",
            "也就是说，必须额外证明早期零行会强制稳定短复现；否则应回到首端帽边界非覆盖和高素数补洞 CRT 延迟。"
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--current-json", type=Path, default=DEFAULT_CURRENT)
    parser.add_argument("--p23-json", type=Path, default=DEFAULT_P23)
    parser.add_argument("--short-json", type=Path, default=DEFAULT_SHORT)
    parser.add_argument("--recursive-json", type=Path, default=DEFAULT_RECURSIVE)
    parser.add_argument("--annulus-json", type=Path, default=DEFAULT_ANNULUS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()
    result = run(
        current_path=args.current_json,
        p23_path=args.p23_json,
        short_path=args.short_json,
        recursive_path=args.recursive_json,
        annulus_path=args.annulus_json,
    )
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)


if __name__ == "__main__":
    main()
