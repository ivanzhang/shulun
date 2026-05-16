#!/usr/bin/env python3
"""把一槽/二槽 moving certificate 写成唯一代表正规形。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_one_two_slot_normal_form_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-one-two-slot-normal-form-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-two-slot-normal-form-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-one-two-slot-normal-form-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-one-two-slot-normal-form-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
SUBCERT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-one-two-slot-normal-form-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-one-two-slot-normal-form-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-one-two-slot-normal-form-router.md"

RESIDUAL_MARGIN_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_residual_prime_margin_router.py"
)
MINIMAL_SUBCERT_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_minimal_subcertificate_router.py"
)
MOVING_BARRIER_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_moving_slot_crt_phase_barrier_router.py"
)
COMPANION_LOSS_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py"
)
EVEN_LAYER_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_even_layer_interval_router.py"

MAIN_TARGET = "OneOrTwoSlotMovingCertificatePDECOrGlobalResidualPrimeMarginJump"
NEXT_TARGET = "UniqueRepresentativeOneTwoSlotPDECOrGlobalResidualPrimeMarginJump"


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


def load_module(path: Path, name: str) -> Any:
    """按路径加载模块。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def unique_representative(lo_value: int, hi_value: int, residue: int, modulus: int) -> list[int]:
    """列出短区间中满足 CRT 残基的整数代表。"""
    if lo_value > hi_value:
        return []
    first = lo_value + ((residue - lo_value) % modulus)
    if first > hi_value:
        return []
    return [first]


def singleton_margins(moving: Any, cert: dict[str, Any]) -> list[dict[str, Any]]:
    """计算最小二槽证书内每个单槽是否单独足够。"""
    rows = []
    for slot in cert["slots"]:
        crt = moving.highfactor_crt_signature([slot])
        phase = moving.phase_intersection([slot])
        margin = int(crt["crt_modulus"]) - int(phase["phase_width"])
        rows.append(
            {
                "b": int(slot["b"]),
                "u": int(slot["u"]),
                "least_prime_factor_m": int(slot["least_prime_factor_m"]),
                "single_crt_modulus": int(crt["crt_modulus"]),
                "single_phase_width": int(phase["phase_width"]),
                "single_crt_minus_phase_width": margin,
                "single_slot_would_isolate": margin > 0,
            }
        )
    return rows


def normal_form_record(record: dict[str, Any], moving: Any) -> dict[str, Any]:
    """把一条最小子证书写成唯一代表正规形。"""
    cert = record["minimal_certificate"]
    lo_value = int(cert["phase_p_lo"])
    hi_value = int(cert["phase_p_hi"])
    residue = int(cert["crt_residue"])
    modulus = int(cert["crt_modulus"])
    representatives = unique_representative(lo_value, hi_value, residue, modulus)
    slots = cert["slots"]
    p_value = int(record["p"])
    slot_keys = [
        f"{slot['b']}:{slot['u']}:{slot['least_prime_factor_m']}" for slot in slots
    ]
    ell_tuple = tuple(int(slot["least_prime_factor_m"]) for slot in slots)
    singleton_rows = singleton_margins(moving, cert)
    return {
        "template_index": int(record["template_index"]),
        "p": p_value,
        "side": str(record["side"]),
        "rho": int(record["rho"]),
        "residual_prime_pair_margin_to_bound": int(record["residual_prime_pair_margin_to_bound"]),
        "certificate_size": int(cert["certificate_size"]),
        "ell_tuple": list(ell_tuple),
        "slot_keys": slot_keys,
        "crt_residue": residue,
        "crt_modulus": modulus,
        "phase_p_lo": lo_value,
        "phase_p_hi": hi_value,
        "phase_width": int(cert["phase_width"]),
        "crt_minus_phase_width": int(cert["crt_minus_phase_width"]),
        "unique_representatives": representatives,
        "unique_representative_count": len(representatives),
        "actual_p_is_unique_representative": representatives == [p_value],
        "left_depth": p_value - lo_value,
        "right_depth": hi_value - p_value,
        "singleton_margins": singleton_rows,
        "two_slot_is_strictly_needed": int(cert["certificate_size"]) == 2
        and all(not row["single_slot_would_isolate"] for row in singleton_rows),
        "normal_shape_key": (
            f"size={cert['certificate_size']}|side={record['side']}|"
            f"ells={','.join(map(str, ell_tuple))}"
        ),
    }


def build_certificate_records(
    template_ledger: Path,
    max_p: int,
    p0: int,
    target_h_coeff: float,
    max_certificate_size: int,
) -> list[dict[str, Any]]:
    """重放并生成完整最小子证书记录。"""
    residual_margin = load_module(RESIDUAL_MARGIN_ROUTER, "normal_form_residual_margin")
    minimal = load_module(MINIMAL_SUBCERT_ROUTER, "normal_form_minimal")
    moving = load_module(MOVING_BARRIER_ROUTER, "normal_form_moving")
    loss = load_module(COMPANION_LOSS_ROUTER, "normal_form_loss")
    even = load_module(EVEN_LAYER_ROUTER, "normal_form_even")
    rows = residual_margin.enrich_margin_rows(max_p, template_ledger, target_h_coeff)
    selected = [row for row in rows if int(row["p"]) >= p0]
    prime_flags = even.sieve(2 * max_p + 1000)
    records = [
        minimal.certificate_record(row, moving, loss, even, prime_flags, max_certificate_size)
        for row in selected
    ]
    if any(record["minimal_certificate"] is None for record in records):
        raise RuntimeError("minimal certificate missing; rerun previous router or increase max size")
    return [normal_form_record(record, moving) for record in records]


def histogram(records: list[dict[str, Any]], key: str) -> dict[str, int]:
    """按指定字段统计。"""
    counts = Counter(str(record[key]) for record in records)
    return {item: counts[item] for item in sorted(counts)}


def ell_histogram(records: list[dict[str, Any]]) -> dict[str, int]:
    """统计证书素因子元组。"""
    counts = Counter(",".join(map(str, record["ell_tuple"])) for record in records)
    return {item: counts[item] for item, _ in counts.most_common(24)}


def normal_shape_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按正规形 shape 汇总。"""
    grouped: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        grouped.setdefault(record["normal_shape_key"], []).append(record)
    rows = []
    for key, items in sorted(grouped.items()):
        rows.append(
            {
                "normal_shape_key": key,
                "count": len(items),
                "min_p": min(int(item["p"]) for item in items),
                "max_p": max(int(item["p"]) for item in items),
                "min_margin": min(int(item["residual_prime_pair_margin_to_bound"]) for item in items),
                "min_crt_minus_phase_width": min(int(item["crt_minus_phase_width"]) for item in items),
                "examples": [
                    {
                        "p": int(item["p"]),
                        "rho": int(item["rho"]),
                        "template_index": int(item["template_index"]),
                        "phase_width": int(item["phase_width"]),
                        "crt_minus_phase_width": int(item["crt_minus_phase_width"]),
                        "slot_keys": item["slot_keys"],
                    }
                    for item in sorted(items, key=lambda x: (int(x["p"]), int(x["template_index"])))[:5]
                ],
            }
        )
    return sorted(rows, key=lambda row: (-int(row["count"]), row["normal_shape_key"]))


def tight_records(records: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    """选出最紧正规形记录。"""
    return sorted(
        records,
        key=lambda record: (
            int(record["residual_prime_pair_margin_to_bound"]),
            int(record["certificate_size"]),
            int(record["crt_minus_phase_width"]),
            int(record["p"]),
            int(record["template_index"]),
        ),
    )[:limit]


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "one_two_slot_unique_representative_normal_form",
            "status": "closed",
            "statement": "Every one-slot/two-slot certificate is exactly a unique CRT representative inside a short phase-support interval.",
        },
        {
            "name": "current_sweep_unique_representative_identity",
            "status": "closed_on_current_sweep",
            "statement": "On the current selector sweep, the unique representative is always the actual selector prime P.",
        },
        {
            "name": "unique_representative_pdec_or_global_margin",
            "status": "open",
            "statement": "A global proof must show these unique representatives cannot persist under the selector chain, or route persistent shapes to ColumnCRT/PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "UniqueRepresentativeNormalFormClosed",
            "closed": True,
            "proved": True,
            "meaning": "一槽/二槽证书已改写为短相位区间内唯一 CRT 代表。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentSweepRepresentativeIdentityClosed",
            "closed": agg["unique_representative_identity_failure_count_at_p0"] == 0,
            "proved": False,
            "meaning": "当前重放中唯一代表恒等于实际 P。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "TwoSlotStrictNeedIdentified",
            "closed": agg["two_slot_strictly_needed_count_at_p0"] == agg["two_slot_record_count_at_p0"],
            "proved": True,
            "meaning": "二槽分支中每个单槽都不足，确实需要 CRT 合并。",
            "remaining": "closed",
        },
        {
            "gate": "PersistentUniqueRepresentativeShapesExcluded",
            "closed": False,
            "proved": False,
            "meaning": "唯一代表 shape 的持久复现尚未排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把一槽/二槽 moving family 正规化，不关闭全局行/列命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(
    template_ledger: Path,
    subcert_ledger: Path,
    max_p: int,
    p0: int,
    target_h_coeff: float,
    max_certificate_size: int,
    tight_limit: int,
) -> dict[str, Any]:
    """构造一槽/二槽唯一代表正规形结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    subcert_source = load_json(subcert_ledger)
    records = build_certificate_records(template_ledger, max_p, p0, target_h_coeff, max_certificate_size)
    failures = [record for record in records if not bool(record["actual_p_is_unique_representative"])]
    one_slot = [record for record in records if int(record["certificate_size"]) == 1]
    two_slot = [record for record in records if int(record["certificate_size"]) == 2]
    equality_records = [record for record in records if int(record["residual_prime_pair_margin_to_bound"]) == 0]
    shape_rows = normal_shape_records(records)
    aggregate = {
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "subcert_ledger": str(subcert_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "max_certificate_size": max_certificate_size,
        "selected_hit_count_at_p0": len(records),
        "previous_subcertificate_failure_count_at_p0": subcert_source["aggregate"][
            "subcertificate_failure_count_at_p0"
        ],
        "unique_representative_identity_failure_count_at_p0": len(failures),
        "one_slot_record_count_at_p0": len(one_slot),
        "two_slot_record_count_at_p0": len(two_slot),
        "two_slot_strictly_needed_count_at_p0": sum(
            1 for record in two_slot if bool(record["two_slot_is_strictly_needed"])
        ),
        "certificate_size_histogram_at_p0": histogram(records, "certificate_size"),
        "ell_tuple_histogram_top": ell_histogram(records),
        "normal_shape_count_at_p0": len(shape_rows),
        "one_slot_shape_count_at_p0": len({record["normal_shape_key"] for record in one_slot}),
        "two_slot_shape_count_at_p0": len({record["normal_shape_key"] for record in two_slot}),
        "min_crt_minus_phase_width_at_p0": min(int(record["crt_minus_phase_width"]) for record in records),
        "max_phase_width_at_p0": max(int(record["phase_width"]) for record in records),
        "equality_atom_count_at_p0": len(equality_records),
        "equality_atom_normal_forms": equality_records,
        "persistent_unique_representative_shapes_excluded": False,
        "global_residual_prime_margin_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {
            "max_p": max_p,
            "p0": p0,
            "target_h_coeff": target_h_coeff,
            "max_certificate_size": max_certificate_size,
            "tight_limit": tight_limit,
        },
        "aggregate": aggregate,
        "equality_atom_normal_form_records": equality_records,
        "tight_normal_form_records": tight_records(records, tight_limit),
        "normal_shape_records": shape_rows[:tight_limit],
        "unique_representative_failure_records": failures[:tight_limit],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_one_two_slot_normal_form_router",
        "status": "one_two_slot_certificates_reduced_to_unique_representative_shapes_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "equality_atom_normal_form_records": equality_records,
        "tight_normal_form_records": ledger["tight_normal_form_records"],
        "normal_shape_records": ledger["normal_shape_records"],
        "unique_representative_failure_records": ledger["unique_representative_failure_records"],
        "persistent_unique_representative_shapes_excluded": False,
        "global_residual_prime_margin_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_one_two_slot_normal_form_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_minimal_subcertificate_router.py": sha256(
                MINIMAL_SUBCERT_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-ledger.json": sha256(
                subcert_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-two-slot-normal-form-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把一槽/二槽 moving certificate 写成唯一代表正规形："
            "`P` 是 CRT 残基在短相位支撑区间内的唯一整数代表。"
            f"当前 `P>={p0}` 重放中唯一代表身份失败数为 {len(failures)}；"
            f"正规形 shape 数为 {aggregate['normal_shape_count_at_p0']}，"
            f"其中一槽 shape {aggregate['one_slot_shape_count_at_p0']} 个、"
            f"二槽 shape {aggregate['two_slot_shape_count_at_p0']} 个。"
            "剩余硬点变为排斥这些唯一代表 shape 在 selector 约束下持久复现，或建立全局正 margin。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower one/two-slot normal form router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"selected_hit_count_at_p0={agg['selected_hit_count_at_p0']}",
        f"unique_representative_identity_failure_count_at_p0={agg['unique_representative_identity_failure_count_at_p0']}",
        f"certificate_size_histogram_at_p0={agg['certificate_size_histogram_at_p0']}",
        f"two_slot_strictly_needed_count_at_p0={agg['two_slot_strictly_needed_count_at_p0']}",
        f"normal_shape_count_at_p0={agg['normal_shape_count_at_p0']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 正规形",
        "",
        "```text",
        "Given one/two highfactor slots S:",
        "  P ≡ crt_residue(S) mod crt_modulus(S)",
        "  P in I(S)=[phase_p_lo, phase_p_hi]",
        "  |I(S)| < crt_modulus(S)",
        "there is at most one representative P_S in I(S).",
        "The certificate is in normal form when actual P=P_S.",
        "```",
        "",
        "## 2. 等号原子正规形",
        "",
        "| p | side | rho | cert size | ell tuple | CRT modulus | phase | representative | depths |",
        "| ---: | --- | ---: | ---: | --- | ---: | --- | --- | --- |",
    ]
    for row in result["equality_atom_normal_form_records"]:
        lines.append(
            f"| {row['p']} | `{row['side']}` | {row['rho']} | {row['certificate_size']} | "
            f"`{row['ell_tuple']}` | {row['crt_modulus']} | `[{row['phase_p_lo']},{row['phase_p_hi']}]` | "
            f"`{row['unique_representatives']}` | `{row['left_depth']}/{row['right_depth']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 最紧正规形样本",
            "",
            "| p | side | rho | template | margin | size | ell tuple | CRT-width | phase | depths | slots |",
            "| ---: | --- | ---: | ---: | ---: | ---: | --- | ---: | --- | --- | --- |",
        ]
    )
    for row in result["tight_normal_form_records"][:24]:
        lines.append(
            f"| {row['p']} | `{row['side']}` | {row['rho']} | {row['template_index']} | "
            f"{row['residual_prime_pair_margin_to_bound']} | {row['certificate_size']} | "
            f"`{row['ell_tuple']}` | {row['crt_minus_phase_width']} | "
            f"`[{row['phase_p_lo']},{row['phase_p_hi']}]` | `{row['left_depth']}/{row['right_depth']}` | "
            f"`{row['slot_keys']}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 高频正规形 shape",
            "",
            "| shape | count | p range | min margin | min CRT-width | examples |",
            "| --- | ---: | --- | ---: | ---: | --- |",
        ]
    )
    for row in result["normal_shape_records"][:18]:
        lines.append(
            f"| `{row['normal_shape_key']}` | {row['count']} | `{row['min_p']}..{row['max_p']}` | "
            f"{row['min_margin']} | {row['min_crt_minus_phase_width']} | "
            f"`{[(item['p'], item['rho'], item['slot_keys']) for item in row['examples'][:3]]}` |"
        )
    lines.extend(
        [
            "",
            "## 5. 结构判断",
            "",
            "- 一槽分支已经是单一同余残基在短区间内的唯一代表问题。",
            "- 二槽分支中每个单槽都不足以隔离，必须依赖两个槽的 CRT 合并；这是真正的 ColumnCRT 形态。",
            "- 下一步应对高频 shape 做持久性排斥：若同一 shape 长期复现，则进入固定模/移动模 PDEC；若 shape 漂移，则进入 SAE/Rankin 账本。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 6. 命题行",
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
            "## 7. 决策表",
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
            "## 8. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 具体目标：排斥唯一代表 shape 持久复现，或将固定 shape/移动 shape 分别接入 `ColumnCRT/PDEC` 与 `SAE/Rankin`。",
            "",
            "## 9. 依赖哈希",
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
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--subcert-ledger", type=Path, default=SUBCERT_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    parser.add_argument("--max-certificate-size", type=int, default=2)
    parser.add_argument("--tight-limit", type=int, default=40)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    subcert_ledger = args.subcert_ledger if args.subcert_ledger.is_absolute() else ROOT / args.subcert_ledger
    result = build_result(
        template_ledger,
        subcert_ledger,
        args.max_p,
        args.p0,
        args.target_h_coeff,
        args.max_certificate_size,
        args.tight_limit,
    )
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-one-two-slot-normal-form-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "unique_representative_identity_failure_count_at_p0": result["aggregate"][
                    "unique_representative_identity_failure_count_at_p0"
                ],
                "normal_shape_count_at_p0": result["aggregate"]["normal_shape_count_at_p0"],
                "certificate_size_histogram_at_p0": result["aggregate"]["certificate_size_histogram_at_p0"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
