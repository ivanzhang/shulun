#!/usr/bin/env python3
"""把 residual-prime 单等号原子登记为 formal-unit PDEC 候选。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_equality_atom_pdec_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-pdec-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-pdec-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-pdec-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-pdec-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

MARGIN_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-residual-prime-margin-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-pdec-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-pdec-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-pdec-router.md"

COMPANION_LOSS_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py"
)
EVEN_LAYER_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_even_layer_interval_router.py"

MAIN_TARGET = "ResidualPrimePairSingleEqualityAtomOrMarginJumpPDEC"
NEXT_TARGET = "ResidualPrimeEqualityAtomPDECExclusionOrGlobalMarginJump"


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


def least_prime_factor(value: int) -> int:
    """返回 value 的最小素因子；若 value 为素数则返回自身。"""
    if value % 2 == 0:
        return 2
    factor = 3
    while factor * factor <= value:
        if value % factor == 0:
            return factor
        factor += 2
    return value


def slot_signature(slot: dict[str, Any]) -> dict[str, Any]:
    """生成槽的可审查签名。"""
    m_value = int(slot["m"])
    return {
        "b": int(slot["b"]),
        "u": int(slot["u"]),
        "q": int(slot["q"]),
        "m": m_value,
        "s": int(slot["s"]),
        "r": int(slot["r"]),
        "m_mod_3": m_value % 3,
        "m_mod_5": m_value % 5,
        "m_mod_7": m_value % 7,
    }


def classify_slots(p_value: int, side: str) -> dict[str, Any]:
    """把等号原子的 cap 槽分成低小模合数、高因子合数、真素对。"""
    loss = load_module(COMPANION_LOSS_ROUTER, "equality_atom_loss")
    even = load_module(EVEN_LAYER_ROUTER, "equality_atom_even")
    prime_flags = even.sieve(2 * p_value + 1000)
    low357 = []
    highfactor = []
    prime_pairs = []
    for slot in loss.cap_slots(even, p_value, side, prime_flags):
        if slot["m_is_prime"]:
            prime_pairs.append(slot_signature(slot))
            continue
        lpf = least_prime_factor(int(slot["m"]))
        signed = {**slot_signature(slot), "least_prime_factor_m": lpf}
        if lpf <= 7:
            low357.append(signed)
        else:
            highfactor.append(signed)
    return {
        "low357_composite_slots": low357,
        "highfactor_composite_slots": highfactor,
        "residual_prime_pair_slots": prime_pairs,
        "partition_counts": {
            "low357_composite": len(low357),
            "highfactor_composite": len(highfactor),
            "residual_prime_pair": len(prime_pairs),
            "total_cap": len(low357) + len(highfactor) + len(prime_pairs),
        },
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "single_equality_atom_formal_unit_registered",
            "status": "closed",
            "statement": "The unique current equality atom is registered as a formal unit with side, rho, template, cap partition, prime-pair slots, and absorber slots.",
        },
        {
            "name": "equality_atom_partition_identity",
            "status": "closed",
            "statement": "For the equality atom, cap=low357 composites + highfactor composites + residual prime pairs, and residual prime pairs equal Bcrit-1.",
        },
        {
            "name": "global_equality_atom_nonpersistence",
            "status": "open",
            "statement": "A global proof must exclude persistent recurrence of this formal equality pattern or prove a positive residual-prime margin away from it.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "EqualityAtomPDECRegistrationClosed",
            "closed": agg["equality_atom_pdec_registration_closed"],
            "proved": True,
            "meaning": "唯一等号原子已登记为 formal-unit PDEC 候选。",
            "remaining": "closed",
        },
        {
            "gate": "EqualityAtomPartitionIdentityClosed",
            "closed": agg["partition_identity_closed"],
            "proved": True,
            "meaning": "等号原子的 cap 分区与 margin=0 身份闭合。",
            "remaining": "closed",
        },
        {
            "gate": "EqualityAtomPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需排斥该等号 formal unit 的持久复现。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "GlobalMarginJumpProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明全局正 margin 或 12 跳跃余量。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只登记等号原子，不关闭全局命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(margin_ledger: Path) -> dict[str, Any]:
    """构造等号原子 PDEC 登记结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(margin_ledger)
    exact = source["equality_atom_records"]
    if len(exact) != 1:
        raise RuntimeError(f"expected one equality atom, got {len(exact)}")
    atom = exact[0]
    p_value = int(atom["p"])
    side = str(atom["side"])
    slots = classify_slots(p_value, side)
    partition = slots["partition_counts"]
    bcrit = int(atom["failure_loaded_b_breakpoint"])
    residual_cap_count = int(atom["small_sieve_357_residual_cap_count"])
    partition_identity = (
        partition["highfactor_composite"] + partition["residual_prime_pair"] == residual_cap_count
        and partition["total_cap"] == partition["low357_composite"] + residual_cap_count
        and partition["residual_prime_pair"] == int(atom["residual_prime_pair_count"])
        and partition["residual_prime_pair"] == bcrit - 1
    )
    formal_unit = {
        "unit_id": (
            f"residual-prime-equality|p={p_value}|side={side}|rho={atom['rho']}|"
            f"template={atom['template_index']}|Bcrit={bcrit}|margin=0"
        ),
        "p": p_value,
        "side": side,
        "rho": atom["rho"],
        "template_index": atom["template_index"],
        "Bcrit": bcrit,
        "bound": int(atom["small_sieve_357_residual_bound"]),
        "margin": int(atom["residual_prime_pair_margin_to_bound"]),
    }
    aggregate = {
        "margin_ledger": str(margin_ledger.relative_to(ROOT)),
        "equality_atom_count": len(exact),
        "equality_atom_pdec_registration_closed": True,
        "partition_identity_closed": partition_identity,
        "residual_prime_pair_count": partition["residual_prime_pair"],
        "highfactor_absorber_count": partition["highfactor_composite"],
        "low357_composite_count": partition["low357_composite"],
        "total_cap_count": partition["total_cap"],
        "equality_atom_pdec_excluded": False,
        "global_margin_jump_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {"source_ledger": str(margin_ledger.relative_to(ROOT))},
        "aggregate": aggregate,
        "formal_unit": formal_unit,
        **slots,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_equality_atom_pdec_router",
        "status": "residual_prime_single_equality_atom_registered_as_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_equality_atom_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "formal_unit": formal_unit,
        "partition_counts": partition,
        "residual_prime_pair_slots": slots["residual_prime_pair_slots"],
        "highfactor_composite_slots": slots["highfactor_composite_slots"],
        "low357_composite_slots_sample": slots["low357_composite_slots"][:12],
        "equality_atom_pdec_excluded": False,
        "global_margin_jump_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_equality_atom_pdec_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py": sha256(
                COMPANION_LOSS_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-residual-prime-margin-ledger.json": sha256(
                margin_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-pdec-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把唯一 residual-prime 等号原子登记为 formal-unit PDEC 候选。"
            f"该原子为 `P={p_value}, {side}, rho={atom['rho']}`，"
            f"cap 分区为 low357={partition['low357_composite']}、"
            f"highfactor={partition['highfactor_composite']}、prime_pairs={partition['residual_prime_pair']}；"
            "其中 residual prime pairs 恰等于 `Bcrit-1`，所以 margin=0。"
            "这仍不是全局闭合；下一步必须排斥该等号相位持久复现，或证明全局正 margin。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    unit = result["formal_unit"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower equality atom PDEC router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unit_id={unit['unit_id']}",
        f"equality_atom_count={agg['equality_atom_count']}",
        f"low357_composite_count={agg['low357_composite_count']}",
        f"highfactor_absorber_count={agg['highfactor_absorber_count']}",
        f"residual_prime_pair_count={agg['residual_prime_pair_count']}",
        f"total_cap_count={agg['total_cap_count']}",
        f"partition_identity_closed={fmt_bool(agg['partition_identity_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Formal Unit",
        "",
        "```json",
        json.dumps(unit, ensure_ascii=False, indent=2, sort_keys=True),
        "```",
        "",
        "## 2. 真素对槽",
        "",
        "| b | u | q | m | s | r | m mod 3 | m mod 5 | m mod 7 |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for slot in result["residual_prime_pair_slots"]:
        lines.append(
            f"| {slot['b']} | {slot['u']} | {slot['q']} | {slot['m']} | {slot['s']} | {slot['r']} | "
            f"{slot['m_mod_3']} | {slot['m_mod_5']} | {slot['m_mod_7']} |"
        )
    lines.extend(
        [
            "",
            "## 3. 高因子吸收槽",
            "",
            "| b | u | q | m | lpf(m) | s | r |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for slot in result["highfactor_composite_slots"]:
        lines.append(
            f"| {slot['b']} | {slot['u']} | {slot['q']} | {slot['m']} | "
            f"{slot['least_prime_factor_m']} | {slot['s']} | {slot['r']} |"
        )
    lines.extend(
        [
            "",
            "## 4. 结构判断",
            "",
            "- 等号原子要求 6 个 residual prime-pair 槽全部保留，任何一个转为合数都会产生正 margin。",
            "- 同一原子还需要 8 个高因子吸收槽精确吸收 357 残余超界；这是一个高度刚性的相位配置。",
            "- 下一步要证明这种 formal unit 不能在高处持久复现，或给出全局 margin 正下界。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 5. 命题行",
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
            "## 6. 决策表",
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
            "## 7. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 具体目标：排斥该 equality formal unit 的持久复现，或证明 residual prime margin 全局正下界。",
            "",
            "## 8. 依赖哈希",
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
    parser.add_argument("--margin-ledger", type=Path, default=MARGIN_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    margin_ledger = args.margin_ledger if args.margin_ledger.is_absolute() else ROOT / args.margin_ledger
    result = build_result(margin_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-equality-atom-pdec-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "unit_id": result["formal_unit"]["unit_id"],
                "partition_counts": result["partition_counts"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
