#!/usr/bin/env python3
"""把 BadPSet actual-prime avoidance 剩余登记为 PDEC/ColumnCRT 证书输入。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_pdec_schema_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-bad-p-set-pdec-schema-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-bad-p-set-pdec-schema-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-bad-p-set-pdec-schema-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-bad-p-set-pdec-schema-router.md
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

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-bad-p-set-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-bad-p-set-pdec-schema-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-bad-p-set-pdec-schema-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-bad-p-set-pdec-schema-router.md"

BAD_P_SET_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_router.py"
PDEC_TEMPLATE = DOCS / "h4-pdec-certificate-template.md"

MAIN_TARGET = "ActualPrimeAvoidsLocalBadPSetByColumnPhaseOrBadPSetPDEC"
NEXT_TARGET = "BadPSetPersistentHitPDECCertificateOrFormalUnitSelectorExclusion"


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


def low_mod_profile(values: list[int], modulus: int) -> dict[str, Any]:
    """计算坏值在低模上的桶分布。"""
    buckets: dict[int, int] = {}
    for value in values:
        residue = value % modulus
        buckets[residue] = buckets.get(residue, 0) + 1
    max_bucket = max(buckets.values(), default=0)
    return {
        "modulus": modulus,
        "occupied_residue_count": len(buckets),
        "max_bucket_count": max_bucket,
        "max_bucket_share": max_bucket / len(values) if values else 0.0,
        "residue_counts": dict(sorted((str(key), count) for key, count in buckets.items())),
    }


def normalized_pattern(row: dict[str, Any]) -> tuple[int, ...]:
    """把 BadPSet 写成相对相位窗口起点的 offset pattern。"""
    return tuple(int(value) - int(row["phase_p_lo"]) for value in row["bad_p_values"])


def pdec_schema_record(row: dict[str, Any]) -> dict[str, Any]:
    """生成单个 BadPSet 的 PDEC schema 记录。"""
    pattern = normalized_pattern(row)
    family_key = (
        f"side={row['side']}|atom={row['parent_atom_key']}|"
        f"L={row['cell_length']}|width={row['phase_p_width']}"
    )
    return {
        "index": row["index"],
        "p": row["p"],
        "side": row["side"],
        "family_key": family_key,
        "shape_key": row["shape_key"],
        "parent_atom_key": row["parent_atom_key"],
        "b_lo": row["b_lo"],
        "b_hi": row["b_hi"],
        "cell_length": row["cell_length"],
        "phase_p_lo": row["phase_p_lo"],
        "phase_p_hi": row["phase_p_hi"],
        "phase_p_width": row["phase_p_width"],
        "bad_p_values": row["bad_p_values"],
        "bad_p_offsets_from_phase_lo": list(pattern),
        "bad_p_value_count": row["bad_p_value_count"],
        "bad_prime_values": row["bad_prime_values"],
        "bad_prime_value_count": row["bad_prime_value_count"],
        "bad_p_density_in_phase_window": row["bad_p_density_in_phase_window"],
        "actual_p_in_bad_set": row["actual_p_in_bad_set"],
        "low_mod_profiles": [low_mod_profile(row["bad_p_values"], modulus) for modulus in (30, 210, 2310)],
        "pdec_input_object": {
            "Q": "one of {30,210,2310} or exact cover-word modulus chosen by the certificate",
            "X": "formal-unit index set producing this same BadPSet family",
            "tau": "actual P mapped to low modulus or exact cover-word residue",
            "S": "persistent actual-P hits inside BadPSet",
            "required_certificate": "PDEC-Explicit-Cert for finite family or PDEC-Dual-Cert for infinite family",
        },
        "schema_status": "registered_not_excluded",
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "bad_p_set_pdec_schema_registered",
            "status": "closed",
            "statement": "Every local BadPSet packet is registered as a concrete PDEC/ColumnCRT certificate input object.",
        },
        {
            "name": "finite_actual_hits_absent",
            "status": "finite_evidence",
            "statement": "The current finite frontier has no actual-P hit inside BadPSet.",
        },
        {
            "name": "bad_p_set_not_empty_or_prime_free",
            "status": "closed",
            "statement": "BadPSet may be nonempty and may contain primes, so avoidance cannot be replaced by local primality or empty-set claims.",
        },
        {
            "name": "persistent_hit_pdec_exclusion",
            "status": "open",
            "statement": "A global proof still needs a PDEC/ColumnCRT certificate excluding persistent actual-P hits, or a selector theorem proving they never occur.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "BadPSetPDECInputRegistered",
            "closed": True,
            "proved": True,
            "meaning": "BadPSet 命中已被登记为可审查的 PDEC/ColumnCRT 输入对象。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoActualBadPSetHit",
            "closed": result["actual_p_in_bad_set_count"] == 0,
            "proved": False,
            "meaning": "有限前沿无 actual P 命中，但这不是无限族证明。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "LocalEmptyOrPrimeFreeRouteRejected",
            "closed": True,
            "proved": True,
            "meaning": "BadPSet 非空且可含素数，局部空集/无素数路线已排除。",
            "remaining": "closed",
        },
        {
            "gate": "PersistentHitPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需真正提交 PDEC/ColumnCRT 证书或 formal-unit selector 排斥定理。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成证书输入标准化，不关闭全局命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造 BadPSet PDEC schema 路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    records = [pdec_schema_record(row) for row in source["bad_p_set_records"]]
    pattern_histogram: dict[str, int] = {}
    family_histogram: dict[str, int] = {}
    for row in records:
        pattern_key = ",".join(str(offset) for offset in row["bad_p_offsets_from_phase_lo"])
        pattern_histogram[pattern_key] = pattern_histogram.get(pattern_key, 0) + 1
        family_histogram[row["family_key"]] = family_histogram.get(row["family_key"], 0) + 1
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "actual_p_in_bad_set_count": source["aggregate"]["actual_p_in_bad_set_count"],
        "bad_prime_packet_count": source["aggregate"]["bad_prime_packet_count"],
        "unique_bad_offset_pattern_count": len(pattern_histogram),
        "unique_family_key_count": len(family_histogram),
        "max_bad_p_density_in_phase_window": source["aggregate"]["max_bad_p_density_in_phase_window"],
        "pattern_histogram": dict(sorted(pattern_histogram.items())),
        "family_histogram": dict(sorted(family_histogram.items())),
        "persistent_hit_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "pdec_schema_records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_pdec_schema_router",
        "status": "bad_p_set_pdec_schema_registered_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "pdec_schema_records": records,
        "actual_p_in_bad_set_count": source["aggregate"]["actual_p_in_bad_set_count"],
        "persistent_hit_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_pdec_schema_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_router.py": sha256(
                BAD_P_SET_ROUTER
            ),
            "docs/monograph/h4-pdec-certificate-template.md": sha256(PDEC_TEMPLATE),
            "data/square-phase-offband-prefix-gap-shadow-bad-p-set-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-bad-p-set-pdec-schema-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 actual P 避开 BadPSet 的剩余标准化为 PDEC/ColumnCRT 证书输入。"
            "有限前沿仍显示 actual P 命中数为 0，但 BadPSet 可非空且可含素数；因此不能靠局部空集"
            "或无素数断言闭合。若正式反例族中 actual P 持久命中 BadPSet，必须提交同一坏窗集合上的"
            "PDEC/ColumnCRT 证书；否则需要证明 formal-unit selector 全局避开 BadPSet。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow BadPSet PDEC schema router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"actual_p_in_bad_set_count={agg['actual_p_in_bad_set_count']}",
        f"bad_prime_packet_count={agg['bad_prime_packet_count']}",
        f"unique_bad_offset_pattern_count={agg['unique_bad_offset_pattern_count']}",
        f"unique_family_key_count={agg['unique_family_key_count']}",
        f"max_bad_p_density_in_phase_window={agg['max_bad_p_density_in_phase_window']:.6f}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. PDEC 输入对象",
        "",
        "若 actual `P` 持久命中 BadPSet，则证书对象按 H4-PDEC 模板登记：`X` 为同一 formal-unit 坏窗索引集，`tau` 为低模或精确覆盖词相位，`S` 为命中 BadPSet 的 actual `P` 集合。",
        "",
        "## 2. Schema 前沿",
        "",
        "| P | side | family | bad density | bad primes | actual hit | offsets |",
        "| ---: | --- | --- | ---: | --- | ---: | --- |",
    ]
    for row in result["pdec_schema_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{table_cell(row['family_key'])}`",
                    f"`{row['bad_p_density_in_phase_window']:.3f}`",
                    f"`{row['bad_prime_values']}`",
                    f"`{fmt_bool(row['actual_p_in_bad_set'])}`",
                    f"`{row['bad_p_offsets_from_phase_lo']}`",
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
            "- 二选一：证明 formal-unit selector 全局避开 BadPSet，或对 persistent hit 提交 H4-PDEC/ColumnCRT 证书。",
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
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-bad-p-set-pdec-schema-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "actual_p_in_bad_set_count": result["actual_p_in_bad_set_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
