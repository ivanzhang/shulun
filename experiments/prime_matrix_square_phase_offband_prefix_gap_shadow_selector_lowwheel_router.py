#!/usr/bin/env python3
"""审计 BadPSet actual-prime selector 的低轮相位分离。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-lowwheel-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-lowwheel-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-lowwheel-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-lowwheel-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-bad-p-set-pdec-schema-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-lowwheel-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-lowwheel-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-lowwheel-router.md"

SCHEMA_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_pdec_schema_router.py"
)

MAIN_TARGET = "BadPSetPersistentHitPDECCertificateOrFormalUnitSelectorExclusion"
NEXT_TARGET = "FormalUnitSelectorLowWheel15LiftOrPersistentHitPDEC"
LOW_WHEEL_MODULI = [2, 3, 5, 6, 10, 15, 30, 210, 2310]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def residue_set(values: list[int], modulus: int) -> list[int]:
    """计算一组整数的模 residue 集。"""
    return sorted({int(value) % modulus for value in values})


def separates_actual(row: dict[str, Any], modulus: int) -> bool:
    """判断给定模数是否把 actual P 与 BadPSet 分离。"""
    return int(row["p"]) % modulus not in residue_set(row["bad_p_values"], modulus)


def smallest_separator(row: dict[str, Any], limit: int = 300) -> int | None:
    """寻找该包的最小模分离器。"""
    for modulus in range(2, limit + 1):
        if separates_actual(row, modulus):
            return modulus
    return None


def global_separators(rows: list[dict[str, Any]], limit: int = 300) -> list[int]:
    """寻找所有包共同适用的模分离器。"""
    return [
        modulus
        for modulus in range(2, limit + 1)
        if all(separates_actual(row, modulus) for row in rows)
    ]


def lowwheel_profile(row: dict[str, Any], modulus: int) -> dict[str, Any]:
    """生成单模低轮分离画像。"""
    bad_residues = residue_set(row["bad_p_values"], modulus)
    actual_residue = int(row["p"]) % modulus
    return {
        "modulus": modulus,
        "actual_residue": actual_residue,
        "bad_residues": bad_residues,
        "separates_actual": actual_residue not in bad_residues,
    }


def selector_record(row: dict[str, Any]) -> dict[str, Any]:
    """生成 selector 低轮审计记录。"""
    bad_values = [int(value) for value in row["bad_p_values"]]
    phase_lo = int(row["phase_p_lo"])
    actual_p = int(row["p"])
    bad_offsets = [value - phase_lo for value in bad_values]
    nearest_distance = min((abs(actual_p - value) for value in bad_values), default=None)
    actual_offset = actual_p - phase_lo
    bad_hull_min = min(bad_values) if bad_values else None
    bad_hull_max = max(bad_values) if bad_values else None
    inside_bad_hull = bool(bad_values and bad_hull_min <= actual_p <= bad_hull_max)
    q15_profile = lowwheel_profile(row, 15)
    return {
        "index": row["index"],
        "p": actual_p,
        "side": row["side"],
        "family_key": row["family_key"],
        "shape_key": row["shape_key"],
        "parent_atom_key": row["parent_atom_key"],
        "cell_length": row["cell_length"],
        "phase_p_lo": phase_lo,
        "phase_p_hi": row["phase_p_hi"],
        "phase_p_width": row["phase_p_width"],
        "actual_offset_from_phase_lo": actual_offset,
        "bad_p_values": bad_values,
        "bad_p_offsets_from_phase_lo": bad_offsets,
        "bad_p_value_count": len(bad_values),
        "bad_prime_values": row["bad_prime_values"],
        "nearest_bad_p_distance": nearest_distance,
        "actual_inside_bad_value_hull": inside_bad_hull,
        "smallest_local_separator_modulus_le_300": smallest_separator(row),
        "lowwheel_profiles": [lowwheel_profile(row, modulus) for modulus in LOW_WHEEL_MODULI],
        "q15_selector_certificate": {
            "modulus": 15,
            "actual_residue": q15_profile["actual_residue"],
            "bad_residues": q15_profile["bad_residues"],
            "separates_actual": q15_profile["separates_actual"],
            "meaning": "actual P mod 15 is not in the local BadPSet residue support mod 15",
        },
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "finite_selector_lowwheel15_separator",
            "status": "closed_on_current_frontier",
            "statement": "On every registered BadPSet packet, actual P is separated from BadPSet by residue modulo 15.",
        },
        {
            "name": "single_prime_or_parity_separator",
            "status": "rejected",
            "statement": "Modulo 2, 3, 5, 6, and 10 do not separate all packets; the first uniform separator is the coupled 3*5 wheel.",
        },
        {
            "name": "endpoint_or_offset_hull_separator",
            "status": "rejected",
            "statement": "Several actual P values lie inside the BadPSet value hull, so endpoint or interval-hull location is not the invariant.",
        },
        {
            "name": "global_formal_unit_lowwheel15_lift",
            "status": "open",
            "statement": "A global proof must derive the modulo-15 separation from the formal-unit selector formulas, or route persistent overlaps to PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FiniteQ15SelectorCertificate",
            "closed": agg["all_packets_separated_by_q15"],
            "proved": True,
            "meaning": "当前 11 个 BadPSet schema 均由 Q=15 分离 actual P 与坏集。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "LowerModulusLocalInvariantsSuffice",
            "closed": True,
            "proved": True,
            "meaning": "2,3,5,6,10 均非共同分离器，单素模/奇偶路线不能闭合。",
            "remaining": "closed as rejected",
        },
        {
            "gate": "GlobalQ15FormalUnitLiftProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明任意 formal unit 的 actual selector 总避开 BadPSet 的 mod 15 支撑。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "PersistentHitPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "若存在 Q=15 重叠的持久族，仍需提交 PDEC/ColumnCRT 证书排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把 selector 侧缩窄到低轮 15 提升或 PDEC，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造 selector 低轮审计结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    source_rows = source["pdec_schema_records"]
    records = [selector_record(row) for row in source_rows]
    shared_separators = global_separators(source_rows)
    lowwheel_gate_results = {
        str(modulus): all(separates_actual(row, modulus) for row in source_rows)
        for modulus in LOW_WHEEL_MODULI
    }
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "actual_p_in_bad_set_count": source["aggregate"]["actual_p_in_bad_set_count"],
        "q15_separator_packet_count": sum(
            1 for row in records if row["q15_selector_certificate"]["separates_actual"]
        ),
        "all_packets_separated_by_q15": all(
            row["q15_selector_certificate"]["separates_actual"] for row in records
        ),
        "first_global_separator_modulus_le_300": shared_separators[0] if shared_separators else None,
        "global_separator_moduli_le_300_prefix": shared_separators[:32],
        "lowwheel_gate_results": lowwheel_gate_results,
        "actual_inside_bad_value_hull_count": sum(
            1 for row in records if row["actual_inside_bad_value_hull"]
        ),
        "parity_separator_packet_count": sum(
            1 for row in records if next(p for p in row["lowwheel_profiles"] if p["modulus"] == 2)["separates_actual"]
        ),
        "mod3_separator_packet_count": sum(
            1 for row in records if next(p for p in row["lowwheel_profiles"] if p["modulus"] == 3)["separates_actual"]
        ),
        "mod5_separator_packet_count": sum(
            1 for row in records if next(p for p in row["lowwheel_profiles"] if p["modulus"] == 5)["separates_actual"]
        ),
        "q15_formal_unit_lift_proved": False,
        "persistent_hit_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "selector_lowwheel_records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_router",
        "status": "selector_lowwheel15_finite_separator_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_global_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "selector_lowwheel_records": records,
        "q15_formal_unit_lift_proved": False,
        "persistent_hit_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_pdec_schema_router.py": sha256(
                SCHEMA_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-bad-p-set-pdec-schema-ledger.json": sha256(
                input_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-lowwheel-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步在 selector 侧找到当前前沿的最小共同低模分离器：Q=15。"
            "所有登记 BadPSet 包中，actual P 的 mod 15 残基均不落入坏集的 mod 15 支撑；"
            "而 2、3、5、6、10 都不能统一分离，说明有效刚性来自 3*5 低轮联动相位，"
            "不是奇偶、单素模、端点或素性本身。该结论只闭合当前有限前沿；全局仍需把"
            "Q=15 分离提升为 formal-unit selector 定理，或对持久重叠提交 PDEC/ColumnCRT 证书。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector lowwheel router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"actual_p_in_bad_set_count={agg['actual_p_in_bad_set_count']}",
        f"q15_separator_packet_count={agg['q15_separator_packet_count']}",
        f"first_global_separator_modulus_le_300={agg['first_global_separator_modulus_le_300']}",
        f"actual_inside_bad_value_hull_count={agg['actual_inside_bad_value_hull_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 低轮分离结论",
        "",
        "当前 11 个 BadPSet schema 上，`Q=15` 是 `<=300` 搜索范围内第一个共同分离模数：",
        "",
        "| modulus | separates all packets |",
        "| ---: | ---: |",
    ]
    for modulus, passed in agg["lowwheel_gate_results"].items():
        lines.append(f"| `{modulus}` | `{fmt_bool(passed)}` |")
    lines.extend(
        [
            "",
            "这说明本层真正可攻的 selector 结构是 `3*5` 联动相位；单独的奇偶、`mod 3`、`mod 5` 或 `mod 10` 都不足以解释 actual `P` 避开坏集。",
            "",
            "## 2. 前沿记录",
            "",
            "| idx | P | side | width | actual off | P mod 15 | BadPSet mod 15 | min sep | nearest bad | inside bad hull |",
            "| ---: | ---: | --- | ---: | ---: | ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for row in result["selector_lowwheel_records"]:
        q15 = row["q15_selector_certificate"]
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["index"]),
                    str(row["p"]),
                    f"`{row['side']}`",
                    str(row["phase_p_width"]),
                    str(row["actual_offset_from_phase_lo"]),
                    str(q15["actual_residue"]),
                    f"`{q15['bad_residues']}`",
                    str(row["smallest_local_separator_modulus_le_300"]),
                    str(row["nearest_bad_p_distance"]),
                    f"`{fmt_bool(row['actual_inside_bad_value_hull'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 4. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 直接证明目标：从 fixed band/k 与 BadPSet 覆盖词公式中符号推出 actual `P mod 15` 不在坏残基支撑内。",
            "- 若出现 `mod 15` 重叠族，则不再转题，直接登记为 persistent-hit `PDEC/ColumnCRT` 证书对象。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-ledger", type=Path, default=INPUT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    result = build_result(input_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-lowwheel-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "first_global_separator_modulus_le_300": result["aggregate"][
                    "first_global_separator_modulus_le_300"
                ],
                "q15_separator_packet_count": result["aggregate"]["q15_separator_packet_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
