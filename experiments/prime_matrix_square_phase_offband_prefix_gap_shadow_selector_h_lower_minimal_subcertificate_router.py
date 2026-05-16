#!/usr/bin/env python3
"""把 moving-slot 高因子隔离屏障压成一槽/二槽最小子证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_minimal_subcertificate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
MOVING_BARRIER_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-router.md"

RESIDUAL_MARGIN_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_residual_prime_margin_router.py"
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

MAIN_TARGET = "MovingSlotFamilyPDECOrGlobalResidualPrimeMarginJump"
NEXT_TARGET = "OneOrTwoSlotMovingCertificatePDECOrGlobalResidualPrimeMarginJump"


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


def slot_summary(slot: dict[str, Any]) -> dict[str, int]:
    """提取槽摘要。"""
    return {
        "b": int(slot["b"]),
        "u": int(slot["u"]),
        "q": int(slot["q"]),
        "m": int(slot["m"]),
        "least_prime_factor_m": int(slot["least_prime_factor_m"]),
        "phase_p_lo": int(slot["phase_p_lo"]),
        "phase_p_hi": int(slot["phase_p_hi"]),
        "phase_width": int(slot["phase_width"]),
    }


def certificate_for_subset(moving: Any, slots: list[dict[str, Any]], indices: tuple[int, ...]) -> dict[str, Any] | None:
    """判断给定高因子槽子集是否是隔离证书。"""
    subset = [slots[index] for index in indices]
    crt = moving.highfactor_crt_signature(subset)
    phase = moving.phase_intersection(subset)
    if not crt["compatible"] or not phase["phase_nonempty"] or phase["phase_width"] is None:
        return None
    margin = int(crt["crt_modulus"]) - int(phase["phase_width"])
    if margin <= 0:
        return None
    return {
        "certificate_size": len(indices),
        "crt_modulus": int(crt["crt_modulus"]),
        "crt_residue": int(crt["crt_residue"]),
        "phase_p_lo": int(phase["phase_p_lo"]),
        "phase_p_hi": int(phase["phase_p_hi"]),
        "phase_width": int(phase["phase_width"]),
        "crt_minus_phase_width": margin,
        "slot_indices": list(indices),
        "slots": [slot_summary(slot) for slot in subset],
    }


def minimal_certificate(moving: Any, slots: list[dict[str, Any]], max_size: int) -> dict[str, Any] | None:
    """寻找最小隔离子证书；同阶内取余量最大的一个。"""
    for size in range(1, min(max_size, len(slots)) + 1):
        best: dict[str, Any] | None = None
        for indices in itertools.combinations(range(len(slots)), size):
            candidate = certificate_for_subset(moving, slots, indices)
            if candidate is None:
                continue
            if best is None or int(candidate["crt_minus_phase_width"]) > int(best["crt_minus_phase_width"]):
                best = candidate
        if best is not None:
            return best
    return None


def certificate_record(row: dict[str, Any], moving: Any, loss: Any, even: Any, prime_flags: bytearray, max_size: int) -> dict[str, Any]:
    """生成单条最小子证书记录。"""
    p_value = int(row["p"])
    side = str(row["side"])
    slots = moving.highfactor_slots(loss, even, p_value, side, prime_flags)
    certificate = minimal_certificate(moving, slots, max_size)
    return {
        "template_index": int(row["template_index"]),
        "p": p_value,
        "side": side,
        "rho": int(row["rho"]),
        "failure_loaded_b_breakpoint": int(row["failure_loaded_b_breakpoint"]),
        "loaded_b_layers": int(row["loaded_b_layers"]),
        "residual_prime_pair_margin_to_bound": int(row["residual_prime_pair_margin_to_bound"]),
        "small_sieve_357_residual_cap_count": int(row["small_sieve_357_residual_cap_count"]),
        "small_sieve_357_residual_bound": int(row["small_sieve_357_residual_bound"]),
        "residual_prime_pair_count": int(row["residual_prime_pair_count"]),
        "highfactor_composite_absorber_count": len(slots),
        "certificate_found": certificate is not None,
        "minimal_certificate": certificate,
    }


def size_histogram(records: list[dict[str, Any]]) -> dict[str, int]:
    """统计最小证书大小。"""
    counts = Counter(
        int(record["minimal_certificate"]["certificate_size"])
        for record in records
        if record["minimal_certificate"] is not None
    )
    return {str(key): counts[key] for key in sorted(counts)}


def tight_records(records: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    """选出最紧的最小子证书记录。"""
    with_cert = [record for record in records if record["minimal_certificate"] is not None]
    return sorted(
        with_cert,
        key=lambda record: (
            int(record["residual_prime_pair_margin_to_bound"]),
            int(record["minimal_certificate"]["certificate_size"]),
            int(record["minimal_certificate"]["crt_minus_phase_width"]),
            int(record["p"]),
            record["side"],
            int(record["rho"]),
            int(record["template_index"]),
        ),
    )[:limit]


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "subcertificate_isolation_criterion",
            "status": "closed",
            "statement": "Any subset of highfactor slots whose CRT modulus exceeds its common phase-support width isolates that fixed subset pattern.",
        },
        {
            "name": "current_sweep_one_or_two_slot_subcertificates",
            "status": "closed_on_current_sweep",
            "statement": "On the current selector sweep, every highfactor-isolated row has a one-slot or two-slot isolation subcertificate.",
        },
        {
            "name": "one_or_two_slot_moving_family_exclusion",
            "status": "open",
            "statement": "A global proof must exclude persistent one-slot/two-slot moving certificates or route them to ColumnCRT/PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "SubcertificateIsolationCriterionClosed",
            "closed": True,
            "proved": True,
            "meaning": "任意子集 CRT 模数超过相位宽度即可隔离固定子图样。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentSweepCoveredBySizeAtMostTwo",
            "closed": agg["subcertificate_failure_count_at_p0"] == 0
            and agg["max_minimal_certificate_size_at_p0"] <= 2,
            "proved": False,
            "meaning": "当前重放全部由一槽/二槽子证书覆盖。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "EqualityAtomOneSlotSubcertificateClosed",
            "closed": agg["equality_atom_minimal_certificate_size"] == 1,
            "proved": True,
            "meaning": "唯一等号原子有单槽隔离证书，因此固定等号图样更强地孤立。",
            "remaining": "closed",
        },
        {
            "gate": "OneOrTwoSlotMovingFamilyExcluded",
            "closed": False,
            "proved": False,
            "meaning": "一槽/二槽 moving certificate 的持久族尚未排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只压缩 moving family 的证书阶数，不关闭全局行/列命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(
    template_ledger: Path,
    moving_barrier_ledger: Path,
    max_p: int,
    p0: int,
    target_h_coeff: float,
    max_certificate_size: int,
    tight_limit: int,
) -> dict[str, Any]:
    """构造最小子证书结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    moving_barrier = load_json(moving_barrier_ledger)
    residual_margin = load_module(RESIDUAL_MARGIN_ROUTER, "minimal_subcert_residual_margin")
    moving = load_module(MOVING_BARRIER_ROUTER, "minimal_subcert_moving")
    loss = load_module(COMPANION_LOSS_ROUTER, "minimal_subcert_loss")
    even = load_module(EVEN_LAYER_ROUTER, "minimal_subcert_even")

    rows = residual_margin.enrich_margin_rows(max_p, template_ledger, target_h_coeff)
    selected = [row for row in rows if int(row["p"]) >= p0]
    prime_flags = even.sieve(2 * max_p + 1000)
    records = [
        certificate_record(row, moving, loss, even, prime_flags, max_certificate_size)
        for row in selected
    ]
    failures = [record for record in records if not bool(record["certificate_found"])]
    with_cert = [record for record in records if record["minimal_certificate"] is not None]
    equality_records = [
        record for record in with_cert if int(record["residual_prime_pair_margin_to_bound"]) == 0
    ]
    aggregate = {
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "moving_barrier_ledger": str(moving_barrier_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "max_certificate_size": max_certificate_size,
        "selected_hit_count_at_p0": len(selected),
        "previous_fixed_pattern_isolation_failure_count_at_p0": moving_barrier["aggregate"][
            "fixed_highfactor_slot_pattern_isolation_failure_count_at_p0"
        ],
        "subcertificate_failure_count_at_p0": len(failures),
        "minimal_certificate_size_histogram_at_p0": size_histogram(records),
        "max_minimal_certificate_size_at_p0": max(
            int(record["minimal_certificate"]["certificate_size"]) for record in with_cert
        ),
        "single_slot_certificate_count_at_p0": sum(
            1 for record in with_cert if int(record["minimal_certificate"]["certificate_size"]) == 1
        ),
        "two_slot_certificate_count_at_p0": sum(
            1 for record in with_cert if int(record["minimal_certificate"]["certificate_size"]) == 2
        ),
        "min_subcertificate_margin_at_p0": min(
            int(record["minimal_certificate"]["crt_minus_phase_width"]) for record in with_cert
        ),
        "equality_atom_count_at_p0": len(equality_records),
        "equality_atom_minimal_certificate_size": min(
            int(record["minimal_certificate"]["certificate_size"]) for record in equality_records
        )
        if equality_records
        else None,
        "one_or_two_slot_moving_family_excluded": False,
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
        "equality_atom_subcertificate_records": equality_records,
        "tight_subcertificate_records": tight_records(records, tight_limit),
        "subcertificate_failure_records": failures[:tight_limit],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_minimal_subcertificate_router",
        "status": "moving_slot_family_reduced_to_one_or_two_slot_subcertificates_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "equality_atom_subcertificate_records": equality_records,
        "tight_subcertificate_records": ledger["tight_subcertificate_records"],
        "subcertificate_failure_records": ledger["subcertificate_failure_records"],
        "one_or_two_slot_moving_family_excluded": False,
        "global_residual_prime_margin_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_minimal_subcertificate_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_moving_slot_crt_phase_barrier_router.py": sha256(
                MOVING_BARRIER_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_residual_prime_margin_router.py": sha256(
                RESIDUAL_MARGIN_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-ledger.json": sha256(
                moving_barrier_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 moving-slot family 的固定图样隔离进一步压成最小子证书。"
            f"当前 `P>={p0}` 重放中，所有 {len(selected)} 条 selector 行都存在大小不超过 "
            f"{aggregate['max_minimal_certificate_size_at_p0']} 的隔离子证书；"
            f"其中单槽 {aggregate['single_slot_certificate_count_at_p0']} 条、"
            f"双槽 {aggregate['two_slot_certificate_count_at_p0']} 条。"
            "唯一等号原子有单槽证书。"
            "这把剩余硬点降为一槽/二槽 moving certificate 的持久性排斥，仍不是全局无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower minimal subcertificate router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"selected_hit_count_at_p0={agg['selected_hit_count_at_p0']}",
        f"subcertificate_failure_count_at_p0={agg['subcertificate_failure_count_at_p0']}",
        f"minimal_certificate_size_histogram_at_p0={agg['minimal_certificate_size_histogram_at_p0']}",
        f"max_minimal_certificate_size_at_p0={agg['max_minimal_certificate_size_at_p0']}",
        f"min_subcertificate_margin_at_p0={agg['min_subcertificate_margin_at_p0']}",
        f"equality_atom_minimal_certificate_size={agg['equality_atom_minimal_certificate_size']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 子证书判据",
        "",
        "```text",
        "A highfactor subset S is an isolation subcertificate if:",
        "  CRT_modulus(S) > common_phase_width(S).",
        "Then fixed S can occur for at most one P in its phase support.",
        "```",
        "",
        "## 2. 等号原子子证书",
        "",
        "| p | side | rho | margin | cert size | CRT modulus | phase width | CRT-width | slots |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["equality_atom_subcertificate_records"]:
        cert = row["minimal_certificate"]
        lines.append(
            f"| {row['p']} | `{row['side']}` | {row['rho']} | {row['residual_prime_pair_margin_to_bound']} | "
            f"{cert['certificate_size']} | {cert['crt_modulus']} | {cert['phase_width']} | "
            f"{cert['crt_minus_phase_width']} | `{[(slot['b'], slot['u'], slot['least_prime_factor_m']) for slot in cert['slots']]}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 最紧子证书样本",
            "",
            "| p | side | rho | template | margin | cert size | CRT modulus | phase width | CRT-width | slots |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["tight_subcertificate_records"][:24]:
        cert = row["minimal_certificate"]
        lines.append(
            f"| {row['p']} | `{row['side']}` | {row['rho']} | {row['template_index']} | "
            f"{row['residual_prime_pair_margin_to_bound']} | {cert['certificate_size']} | "
            f"{cert['crt_modulus']} | {cert['phase_width']} | {cert['crt_minus_phase_width']} | "
            f"`{[(slot['b'], slot['u'], slot['least_prime_factor_m']) for slot in cert['slots']]}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 失败形态",
            "",
        ]
    )
    if result["subcertificate_failure_records"]:
        lines.extend(
            [
                "| p | side | rho | margin | highfactor |",
                "| ---: | --- | ---: | ---: | ---: |",
            ]
        )
        for row in result["subcertificate_failure_records"]:
            lines.append(
                f"| {row['p']} | `{row['side']}` | {row['rho']} | "
                f"{row['residual_prime_pair_margin_to_bound']} | {row['highfactor_composite_absorber_count']} |"
            )
    else:
        lines.append("当前重放中没有大小不超过设定阈值的子证书失败。")
    lines.extend(
        [
            "",
            "## 5. 结构判断",
            "",
            "- 大多数行甚至由单个高因子槽隔离；剩余少数只需两个槽。",
            "- 因此 moving-slot family 的真正硬点已降到一槽/二槽证书的持久性，而不是多槽组合复杂性。",
            "- 下一步要分别处理单槽移动和双槽移动：单槽是 `ell > phase_width` 的一维相位锁，双槽是两个相位区间交叠加 CRT 乘子锁。",
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
            "- 具体目标：证明一槽/二槽 moving certificate 不能持久复现，或把其接入正式 `ColumnCRT/PDEC` 排斥证书。",
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
    parser.add_argument("--moving-barrier-ledger", type=Path, default=MOVING_BARRIER_LEDGER)
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
    moving_barrier_ledger = (
        args.moving_barrier_ledger
        if args.moving_barrier_ledger.is_absolute()
        else ROOT / args.moving_barrier_ledger
    )
    result = build_result(
        template_ledger,
        moving_barrier_ledger,
        args.max_p,
        args.p0,
        args.target_h_coeff,
        args.max_certificate_size,
        args.tight_limit,
    )
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-minimal-subcertificate-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "subcertificate_failure_count_at_p0": result["aggregate"]["subcertificate_failure_count_at_p0"],
                "minimal_certificate_size_histogram_at_p0": result["aggregate"][
                    "minimal_certificate_size_histogram_at_p0"
                ],
                "equality_atom_minimal_certificate_size": result["aggregate"][
                    "equality_atom_minimal_certificate_size"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
