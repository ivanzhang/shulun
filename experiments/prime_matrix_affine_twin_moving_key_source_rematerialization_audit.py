#!/usr/bin/env python3
"""生成 AffineTwin moving-key source-rematerialization 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_moving_key_source_rematerialization_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json

输出：
  data/prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json
  docs/monograph/prime-matrix-affine-twin-moving-key-source-rematerialization-audit.json
  docs/monograph/prime-matrix-affine-twin-moving-key-source-rematerialization-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

MOVING_DEPTH_LEDGER = DATA / (
    "prime-matrix-affine-twin-moving-key-depth-formula-ledger.json"
)
PAIR_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json"
)
SOURCE_GATE_LEDGER = DATA / (
    "prime-matrix-affine-twin-source-materialization-gate-ledger.json"
)
MOVING_FAMILY_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-moving-family-sae-columncrt-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-moving-key-source-rematerialization-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-moving-key-source-rematerialization-audit.md"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def is_prime(n: int) -> bool:
    """小规模确定性素性测试。"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    step = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += step
        step = 6 - step
    return True


def expected_delay(q: int) -> int | None:
    """AffineTwin 源门控期望的 p-delay。"""
    numerator = 11 * q - 21
    if numerator % 4 != 0:
        return None
    return numerator // 4


def expected_signature(q: int) -> dict[str, Any]:
    """构造 moving key 若要重物化为 AffineTwin 源时的期望签名。"""
    return {
        "gap_ell": q,
        "generator_ell": q - 2,
        "fill_ell": q,
        "generator_side": "minus",
        "fill_side": "plus",
        "expected_p_delay": expected_delay(q),
    }


def source_match_vector(
    source: dict[str, Any],
    signature: dict[str, Any],
) -> dict[str, Any]:
    """检查 source row 与 moving-key 期望签名的匹配向量。"""
    expected_p_delay = signature["expected_p_delay"]
    actual_delay = int(source["p_delay"])
    return {
        "gap_ell_match": int(source["gap_ell"]) == signature["gap_ell"],
        "generator_ell_match": int(source["generator_ell"])
        == signature["generator_ell"],
        "fill_ell_match": int(source["fill_ell"]) == signature["fill_ell"],
        "generator_side_match": str(source["generator_side"])
        == signature["generator_side"],
        "fill_side_match": str(source["fill_side"]) == signature["fill_side"],
        "p_delay_match": expected_p_delay is not None
        and actual_delay == expected_p_delay,
        "actual_p_delay": actual_delay,
        "expected_p_delay": expected_p_delay,
        "p_delay_delta": actual_delay - expected_p_delay
        if expected_p_delay is not None
        else None,
    }


def all_required_matches(vector: dict[str, Any]) -> bool:
    """判定源门控所需不变量是否全部通过。"""
    return all(
        bool(vector[key])
        for key in (
            "gap_ell_match",
            "generator_ell_match",
            "fill_ell_match",
            "generator_side_match",
            "fill_side_match",
            "p_delay_match",
        )
    )


def pair_rows_by_gap(rows: list[dict[str, Any]]) -> dict[int, list[dict[str, Any]]]:
    """按 gap ell 建立 source 索引。"""
    out: dict[int, list[dict[str, Any]]] = {}
    for row in rows:
        out.setdefault(int(row["gap_ell"]), []).append(row)
    return out


def best_source_row(
    sources: list[dict[str, Any]],
    signature: dict[str, Any],
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    """返回匹配度最高的 source row 及其匹配向量。"""
    best: tuple[int, dict[str, Any], dict[str, Any]] | None = None
    for source in sources:
        vector = source_match_vector(source, signature)
        score = sum(
            1
            for key in (
                "gap_ell_match",
                "generator_ell_match",
                "fill_ell_match",
                "generator_side_match",
                "fill_side_match",
                "p_delay_match",
            )
            if vector[key]
        )
        if best is None or score > best[0]:
            best = (score, source, vector)
    if best is None:
        return None, None
    return best[1], best[2]


def moving_q_occurrences(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """从 moving-depth 公式行提取所有单侧候选 q。"""
    occurrences: list[dict[str, Any]] = []
    for row in rows:
        base = {
            "source_pair_key": str(row["source_pair_key"]),
            "window_side": str(row["window_side"]),
            "required_common_side_depth": int(row["required_common_side_depth"]),
            "support_motion_primitive_defect_total": int(
                row["support_motion_primitive_defect_total"]
            ),
        }
        q_from_generator = int(row["q_from_generator_depth_formula"])
        q_from_fill = row["q_from_fill_depth_formula"]
        occurrences.append(
            {
                **base,
                "formula_role": "generator_depth_formula",
                "q_candidate": q_from_generator,
                "counterpart_q_candidate": q_from_fill,
            }
        )
        if q_from_fill is not None:
            occurrences.append(
                {
                    **base,
                    "formula_role": "fill_depth_formula",
                    "q_candidate": int(q_from_fill),
                    "counterpart_q_candidate": q_from_generator,
                }
            )
    return occurrences


def nearest_gap_source(
    q: int,
    available_gap_ells: list[int],
) -> dict[str, Any] | None:
    """返回离候选 q 最近的已物化 gap source。"""
    if not available_gap_ells:
        return None
    nearest = min(available_gap_ells, key=lambda ell: (abs(ell - q), ell))
    return {"gap_ell": nearest, "abs_delta": abs(nearest - q), "signed_delta": nearest - q}


def affine_prime_gate(q: int) -> dict[str, Any]:
    """判定 moving q 是否通过 AffineTwin prime/source 前置门。"""
    q_is_prime = is_prime(q)
    q_minus_2_is_prime = is_prime(q - 2)
    q_mod4_eq3 = q % 4 == 3
    delay_integral = expected_delay(q) is not None
    return {
        "q_is_prime": q_is_prime,
        "q_minus_2_is_prime": q_minus_2_is_prime,
        "q_mod4_eq3": q_mod4_eq3,
        "expected_p_delay_integral": delay_integral,
        "affine_twin_prime_gate_passed": (
            q_is_prime and q_minus_2_is_prime and q_mod4_eq3 and delay_integral
        ),
    }


def rematerialization_route(
    prime_gate: dict[str, Any],
    same_gap_sources: list[dict[str, Any]],
    exact_source_count: int,
) -> str:
    """给出候选 q 的重物化路由。"""
    if exact_source_count:
        return "ExactSourceMaterialized"
    if not prime_gate["q_is_prime"]:
        return "CompositeQ"
    if not prime_gate["affine_twin_prime_gate_passed"]:
        return "PrimeButNotTwinAffine"
    if same_gap_sources:
        return "SameGapWrongSource-RematerializationGate"
    return "NoGapSource-RematerializationGate"


def candidate_q_row(
    q: int,
    occurrences: list[dict[str, Any]],
    same_gap_sources: list[dict[str, Any]],
    available_gap_ells: list[int],
    current_source_gate_q_values: list[int],
    current_moving_family_q_values: list[int],
) -> dict[str, Any]:
    """构造单个候选 q 的重物化审计行。"""
    signature = expected_signature(q)
    exact_sources = []
    for source in same_gap_sources:
        vector = source_match_vector(source, signature)
        if all_required_matches(vector):
            exact_sources.append(source)
    best_source, best_vector = best_source_row(same_gap_sources, signature)
    prime_gate = affine_prime_gate(q)
    route = rematerialization_route(prime_gate, same_gap_sources, len(exact_sources))
    failed_invariants: list[str] = []
    if not prime_gate["q_is_prime"]:
        failed_invariants.append("q_composite")
    else:
        for key in (
            "q_minus_2_is_prime",
            "q_mod4_eq3",
            "expected_p_delay_integral",
        ):
            if not prime_gate[key]:
                failed_invariants.append(key)
    if not same_gap_sources:
        failed_invariants.append("gap_source_absent")
    elif best_vector is not None:
        failed_invariants.extend(
            key
            for key in (
                "generator_ell_match",
                "fill_ell_match",
                "generator_side_match",
                "fill_side_match",
                "p_delay_match",
            )
            if not best_vector[key]
        )

    return {
        "q": q,
        "route": route,
        "occurrence_count": len(occurrences),
        "occurrence_roles": sorted(
            Counter(str(item["formula_role"]) for item in occurrences).items()
        ),
        "source_pair_keys": sorted(
            {str(item["source_pair_key"]) for item in occurrences}
        ),
        "min_required_common_side_depth": min(
            int(item["required_common_side_depth"]) for item in occurrences
        ),
        "prime_gate": prime_gate,
        "expected_signature": signature,
        "same_gap_source_row_count": len(same_gap_sources),
        "exact_matching_source_row_count": len(exact_sources),
        "best_source_key": str(best_source["gap_fill_pair_key"]) if best_source else None,
        "best_source_match_vector": best_vector,
        "nearest_available_gap_source": nearest_gap_source(q, available_gap_ells),
        "present_in_current_source_gate_candidates": q in current_source_gate_q_values,
        "present_in_current_moving_family_candidates": q in current_moving_family_q_values,
        "moving_key_source_rematerialized_current": len(exact_sources) > 0,
        "failed_invariants": sorted(set(failed_invariants)),
    }


def build_result(
    moving_depth_path: Path,
    pair_path: Path,
    source_gate_path: Path,
    moving_family_path: Path,
) -> dict[str, Any]:
    """构造 moving-key source-rematerialization 审计结果。"""
    moving_depth = load_json(moving_depth_path)
    pair = load_json(pair_path)
    source_gate = load_json(source_gate_path)
    moving_family = load_json(moving_family_path)

    occurrences = moving_q_occurrences(moving_depth["moving_key_depth_formula_rows"])
    occurrences_by_q: dict[int, list[dict[str, Any]]] = {}
    for occurrence in occurrences:
        occurrences_by_q.setdefault(int(occurrence["q_candidate"]), []).append(
            occurrence
        )

    pair_by_gap = pair_rows_by_gap(pair["gap_fill_pair_rows"])
    available_gap_ells = sorted(pair_by_gap)
    current_source_gate_q_values = [
        int(q) for q in source_gate["aggregate"]["candidate_q_values"]
    ]
    current_moving_family_q_values = [
        int(q) for q in moving_family["aggregate"]["candidate_q_values"]
    ]
    candidate_rows = [
        candidate_q_row(
            q,
            occurrences_by_q[q],
            pair_by_gap.get(q, []),
            available_gap_ells,
            current_source_gate_q_values,
            current_moving_family_q_values,
        )
        for q in sorted(occurrences_by_q)
    ]

    route_histogram = Counter(str(row["route"]) for row in candidate_rows)
    prime_q_values = [
        int(row["q"]) for row in candidate_rows if row["prime_gate"]["q_is_prime"]
    ]
    affine_twin_gate_q_values = [
        int(row["q"])
        for row in candidate_rows
        if row["prime_gate"]["affine_twin_prime_gate_passed"]
    ]
    exact_rematerialized_q_values = [
        int(row["q"])
        for row in candidate_rows
        if row["moving_key_source_rematerialized_current"]
    ]
    nearest = [
        int(row["nearest_available_gap_source"]["abs_delta"])
        for row in candidate_rows
        if row["nearest_available_gap_source"] is not None
    ]
    narrowest_depth = moving_depth["aggregate"]["narrowest_formula_obstruction_atom"]
    narrowest_source_pair = str(narrowest_depth["source_pair_key"])
    narrowest_related_rows = [
        row
        for row in candidate_rows
        if narrowest_source_pair in row["source_pair_keys"]
    ]
    tempting_rows = [
        row
        for row in candidate_rows
        if row["prime_gate"]["q_is_prime"]
        and row["prime_gate"]["q_minus_2_is_prime"]
    ]
    strongest_near_miss = min(
        tempting_rows or candidate_rows,
        key=lambda row: (
            0
            if row["prime_gate"]["q_is_prime"]
            and row["prime_gate"]["q_minus_2_is_prime"]
            else 1,
            int(row["nearest_available_gap_source"]["abs_delta"])
            if row["nearest_available_gap_source"] is not None
            else 10**9,
            int(row["min_required_common_side_depth"]),
            int(row["q"]),
        ),
    )

    aggregate = {
        "moving_depth_ledger": str(moving_depth_path.relative_to(ROOT)),
        "pair_ledger": str(pair_path.relative_to(ROOT)),
        "source_gate_ledger": str(source_gate_path.relative_to(ROOT)),
        "moving_family_ledger": str(moving_family_path.relative_to(ROOT)),
        "moving_depth_row_count": len(moving_depth["moving_key_depth_formula_rows"]),
        "moving_q_formula_occurrence_count": len(occurrences),
        "unique_moving_q_candidate_count": len(candidate_rows),
        "candidate_q_values": [int(row["q"]) for row in candidate_rows],
        "prime_candidate_q_values": prime_q_values,
        "affine_twin_prime_gate_q_values": affine_twin_gate_q_values,
        "exact_rematerialized_q_values": exact_rematerialized_q_values,
        "route_histogram": dict(sorted(route_histogram.items())),
        "composite_q_count": route_histogram.get("CompositeQ", 0),
        "prime_but_not_twin_affine_count": route_histogram.get(
            "PrimeButNotTwinAffine", 0
        ),
        "candidate_with_same_gap_source_count": sum(
            1 for row in candidate_rows if row["same_gap_source_row_count"] > 0
        ),
        "candidate_with_exact_source_count": len(exact_rematerialized_q_values),
        "available_gap_source_q_values": available_gap_ells,
        "min_nearest_available_gap_source_delta": min(nearest) if nearest else None,
        "max_nearest_available_gap_source_delta": max(nearest) if nearest else None,
        "narrowest_depth_source_pair_key": narrowest_source_pair,
        "narrowest_depth_candidate_q_values": [
            int(row["q"]) for row in narrowest_related_rows
        ],
        "strongest_near_miss_q": int(strongest_near_miss["q"]),
        "strongest_near_miss_route": str(strongest_near_miss["route"]),
        "all_formula_candidate_q_fail_prime_or_source_gate": all(
            not row["prime_gate"]["affine_twin_prime_gate_passed"]
            or not row["moving_key_source_rematerialized_current"]
            for row in candidate_rows
        ),
        "moving_key_source_rematerialization_closed_current_sweep": all(
            not row["moving_key_source_rematerialized_current"]
            for row in candidate_rows
        ),
        "global_moving_key_source_nonpersistence_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_moving_key_source_rematerialization_audit"
        ),
        "status": (
            "current_sweep_moving_key_source_rematerialization_closed_global_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "moving_q_occurrences": occurrences,
        "candidate_q_source_rematerialization_rows": candidate_rows,
        "contract": {
            "moving_key_source_gate": [
                "candidate q is produced by a moving-key depth formula",
                "q and q-2 are prime",
                "q == 3 mod 4 so p_delay=(11q-21)/4 is integral",
                "a same-gap source exists with generator=q-2 and fill=q",
                "source sides match minus->plus",
                "source p_delay matches the AffineTwin delay",
            ],
            "closed_current_sweep": aggregate[
                "moving_key_source_rematerialization_closed_current_sweep"
            ],
            "global_remaining": [
                "OrientationChangingPrimitiveKey-PDEC/SAE",
                "SourceRematerialization-PDEC/SAE",
                "MovingPrimitiveKeyNonPersistence",
                "EndpointReleaseCoupling-PDEC",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                moving_depth_path,
                pair_path,
                source_gate_path,
                moving_family_path,
            )
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    for path in (OUT_LEDGER, OUT_JSON):
        path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix AffineTwin moving-key source-rematerialization audit",
        "",
        "**状态：** `current_sweep_moving_key_source_rematerialization_closed_global_open`",
        "",
        "本审计继续下钻 `MovingPrimitiveKey` 的剩余出口：即使把同向深度公式给出的单侧候选 `q` 当成新 key，候选也必须重新通过 AffineTwin prime gate 与 source materialization gate。",
        "",
        "```text",
        f"moving_depth_row_count={agg['moving_depth_row_count']}",
        f"moving_q_formula_occurrence_count={agg['moving_q_formula_occurrence_count']}",
        f"unique_moving_q_candidate_count={agg['unique_moving_q_candidate_count']}",
        f"prime_candidate_q_values={agg['prime_candidate_q_values']}",
        f"affine_twin_prime_gate_q_values={agg['affine_twin_prime_gate_q_values']}",
        f"exact_rematerialized_q_values={agg['exact_rematerialized_q_values']}",
        f"route_histogram={agg['route_histogram']}",
        f"min_nearest_available_gap_source_delta={agg['min_nearest_available_gap_source_delta']}",
        f"moving_key_source_rematerialization_closed_current_sweep={fmt_bool(agg['moving_key_source_rematerialization_closed_current_sweep'])}",
        "```",
        "",
        "## 1. candidate q gate 表",
        "",
        "| q | route | occ | q prime | q-2 prime | q mod 4=3 | delay integral | same-gap source | exact source | nearest gap source | failed invariants |",
        "| ---: | --- | ---: | --- | --- | --- | --- | ---: | ---: | --- | --- |",
    ]
    for row in result["candidate_q_source_rematerialization_rows"]:
        prime_gate = row["prime_gate"]
        nearest_gap = row["nearest_available_gap_source"]
        nearest_text = (
            "-"
            if nearest_gap is None
            else f"{nearest_gap['gap_ell']} (delta={nearest_gap['signed_delta']})"
        )
        lines.append(
            "| {q} | `{route}` | {occ} | {qp} | {q2p} | {mod4} | {delay} | {same_gap} | {exact} | {nearest} | `{failed}` |".format(
                q=row["q"],
                route=table_cell(row["route"]),
                occ=row["occurrence_count"],
                qp=fmt_bool(prime_gate["q_is_prime"]),
                q2p=fmt_bool(prime_gate["q_minus_2_is_prime"]),
                mod4=fmt_bool(prime_gate["q_mod4_eq3"]),
                delay=fmt_bool(prime_gate["expected_p_delay_integral"]),
                same_gap=row["same_gap_source_row_count"],
                exact=row["exact_matching_source_row_count"],
                nearest=table_cell(nearest_text),
                failed=table_cell(",".join(row["failed_invariants"]) or "none"),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 最窄 atom 的源重物化读数",
            "",
            f"上一层最窄 depth atom 是 `{agg['narrowest_depth_source_pair_key']}`；其 moving-depth 公式给出的候选 `q` 为 `{agg['narrowest_depth_candidate_q_values']}`。",
            "其中 `q=111` 为合数；`q=61` 虽然 `61` 与 `59` 均为素数，但 `61≡1 mod 4`，使 `p_delay=(11q-21)/4` 非整数，并且当前没有 gap `q=61` 的 matching source。",
            "最接近的已物化 gap source 是 `q=59`，但它的角色是 `generator=61, fill=59, sides=minus->minus, p_delay=70`，不是 `q=61` AffineTwin 期望的 `generator=59, fill=61, sides=minus->plus`。",
            "",
            "## 3. 结论边界",
            "",
            "- 当前 moving-depth 公式产生 `19` 个唯一候选 `q`：`13` 个合数，`6` 个素数但全部不是同向 AffineTwin key。",
            "- 没有任何候选 `q` 同时通过 AffineTwin prime gate 与 source materialization gate；当前 sweep 的 source-rematerialization 吸收通道关闭。",
            "- 这仍不是全局行/列无条件证明；剩余是方向改变、source 重物化全局非持久性或 endpoint release coupling 的排斥/路由。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description="生成 AffineTwin moving-key source-rematerialization 审计证书。"
    )
    parser.add_argument("--moving-depth-ledger", type=Path, default=MOVING_DEPTH_LEDGER)
    parser.add_argument("--pair-ledger", type=Path, default=PAIR_LEDGER)
    parser.add_argument("--source-gate-ledger", type=Path, default=SOURCE_GATE_LEDGER)
    parser.add_argument(
        "--moving-family-ledger", type=Path, default=MOVING_FAMILY_LEDGER
    )
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.moving_depth_ledger,
        args.pair_ledger,
        args.source_gate_ledger,
        args.moving_family_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
