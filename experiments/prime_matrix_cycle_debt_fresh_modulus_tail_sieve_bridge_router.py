#!/usr/bin/env python3
"""生成 cycle-debt fresh-modulus 到 tail-sieve 稳定对象的桥接证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_fresh_modulus_tail_sieve_bridge_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-ledger.json

输出：
  data/prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-ledger.json
  docs/monograph/prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-router.json
  docs/monograph/prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

FRESH = DATA / "prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-ledger.json"
TAIL_B3 = DOCS / "prime-matrix-strict-dynamic-skeleton-tail-b3-bridge-router.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-router.md"

PREVIOUS_TARGET = "UnboundedFreshModulusEscalationPDECOrTailSieveStabilityContradiction"
NEXT_TARGET = "FreshLayerPDECColumnCRTExclusionOrSelfContainedTailSieveStabilityClosure"
FRESH_PDEC = "FreshLayerPDECColumnCRTExclusion"
SELF_MERTENS = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
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


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定门。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_gates(fresh: dict[str, Any], tail_b3: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 fresh-modulus 到尾段筛的桥接判定表。"""
    agg = fresh["aggregate"]
    finite_terminal_excluded = bool(agg["finite_crt_terminal_description_excluded"])
    persistent_requires_escalation = bool(agg["persistent_family_requires_unbounded_modulus_or_pdec"])
    tail_interface = bool(tail_b3["tail_object_interface_closed"])
    external_tail_closed = bool(tail_b3["tail_ledger_external_or_standard_closed"])
    strict_tail_closed = bool(tail_b3["tail_ledger_strict_self_contained_proved"])

    return [
        gate(
            "FreshModulusEscalationImported",
            persistent_requires_escalation,
            True,
            "上一证书已证明固定有限 ColumnCRT replay 类不能成为无限反例链的终端稳定结构。",
            PREVIOUS_TARGET,
        ),
        gate(
            "FiniteColumnCRTTerminalExcluded",
            finite_terminal_excluded,
            True,
            "有限原子分支已关闭，且固定登记模数在新素数层下必被互素 CRT 坐标继续扩张。",
            "closed for registered finite terminal classes",
        ),
        gate(
            "NonPDECUnboundedFreshLayersForceRoughObject",
            persistent_requires_escalation,
            False,
            "若每个 fresh layer 都不触发 PDEC/ColumnCRT，则每个新素数层只留下一个被禁止的相位，持久族必须落入一维避单余类粗筛对象。",
            "one-residue-per-prime tail rough object",
        ),
        gate(
            "TailObjectInterfaceMatchedToB3",
            tail_interface,
            True,
            "该避单余类对象与既有 B3 lower-sieve 账本同口径：squarefree d 的计数为 (P-1)/d 加端点误差。",
            "B3 lower-sieve rough-object interface",
        ),
        gate(
            "ExternalOrStandardTailSieveClosesStabilityBranch",
            external_tail_closed,
            False,
            "若允许外部显式 Mertens/Dusart 或标准 beta-sieve 输入，tail-sieve stability 分支可条件关闭。",
            "external/standard beta-sieve input",
        ),
        gate(
            "StrictSelfContainedTailSieveStillOpen",
            not strict_tail_closed,
            False,
            "严格自足路线不能借用外部筛定理；仍需内联 Mertens/PNT/Dusart 倒素数尾段证明。",
            SELF_MERTENS,
        ),
        gate(
            "FreshLayerPDECExitStillRequiresExclusion",
            False,
            False,
            "若 fresh layer 中出现相位复用、投影碰撞、moving support 逃逸或 ColumnCRT 缺陷，还必须给出 PDEC 排斥证书。",
            FRESH_PDEC,
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把无界扩模分支接到尾段筛稳定接口；尚未完成严格自足尾段证明和 fresh-layer PDEC 排斥。",
            NEXT_TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造桥接证书。"""
    fresh = load_json(FRESH)
    tail_b3 = load_json(TAIL_B3)
    gates = build_gates(fresh, tail_b3)
    gate_map = {item["gate"]: item for item in gates}
    constants = tail_b3.get("constants", {})
    agg = fresh["aggregate"]

    strict_branch_basis = f"{FRESH_PDEC} AND {SELF_MERTENS}"
    external_branch_basis = FRESH_PDEC

    return {
        "certificate_type": "prime_matrix_cycle_debt_fresh_modulus_tail_sieve_bridge_router",
        "status": "fresh_modulus_escalation_routed_to_tail_sieve_interface_strict_self_contained_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "previous_hardpoint": PREVIOUS_TARGET,
        "fresh_modulus_escalation_registered": gate_map["FreshModulusEscalationImported"]["closed"],
        "finite_columncrt_terminal_excluded": gate_map["FiniteColumnCRTTerminalExcluded"]["closed"],
        "non_pdec_unbounded_fresh_layers_force_tail_rough_object": gate_map[
            "NonPDECUnboundedFreshLayersForceRoughObject"
        ]["closed"],
        "tail_object_interface_closed": gate_map["TailObjectInterfaceMatchedToB3"]["closed"],
        "conditional_external_tail_sieve_closed": gate_map[
            "ExternalOrStandardTailSieveClosesStabilityBranch"
        ]["closed"],
        "strict_self_contained_tail_sieve_closed": False,
        "fresh_layer_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "registered_replay_block_count": agg["registered_replay_block_count"],
        "minimum_first_fresh_log10_gain": agg["minimum_first_fresh_log10_gain"],
        "minimum_sample_log10_gain": agg["minimum_sample_log10_gain"],
        "tail_sieve_alpha": constants.get("alpha"),
        "tail_sieve_model_main_at_100000": constants.get("model_main_at_tail_start"),
        "tail_sieve_ten_percent_surplus_over_401": constants.get("ten_percent_surplus_over_401"),
        "strict_branch_remaining_basis": strict_branch_basis,
        "external_or_standard_branch_remaining_basis": external_branch_basis,
        "inherited_global_strict_remaining_basis": tail_b3.get("strict_self_contained_remaining_basis"),
        "inherited_global_external_remaining_basis": tail_b3.get("external_or_standard_remaining_basis"),
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "固定有限 ColumnCRT 终端已经被排除后，持久 branch replay 若不在新素数层触发 PDEC/ColumnCRT，"
            "就必须把每个 fresh prime 变成一个被禁止的相位条件；这正是 B3 尾段避单余类粗筛对象。"
            "因此无界扩模分支被路由到 tail-sieve stability 接口。接受外部或标准 beta-sieve 输入时该尾段分支条件关闭；"
            "严格自足路线仍剩 Mertens/PNT/Dusart 尾段内联证明与 fresh-layer PDEC 排斥。"
        ),
        "dependency_hashes": {
            str(FRESH.relative_to(ROOT)): sha256(FRESH),
            str(TAIL_B3.relative_to(ROOT)): sha256(TAIL_B3),
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix cycle-debt fresh-modulus 到 tail-sieve 桥接路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        f"fresh_modulus_escalation_registered={fmt_bool(result['fresh_modulus_escalation_registered'])}",
        f"finite_columncrt_terminal_excluded={fmt_bool(result['finite_columncrt_terminal_excluded'])}",
        "non_pdec_unbounded_fresh_layers_force_tail_rough_object="
        f"{fmt_bool(result['non_pdec_unbounded_fresh_layers_force_tail_rough_object'])}",
        f"tail_object_interface_closed={fmt_bool(result['tail_object_interface_closed'])}",
        f"conditional_external_tail_sieve_closed={fmt_bool(result['conditional_external_tail_sieve_closed'])}",
        f"strict_self_contained_tail_sieve_closed={fmt_bool(result['strict_self_contained_tail_sieve_closed'])}",
        f"fresh_layer_pdec_excluded={fmt_bool(result['fresh_layer_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 桥接引理",
        "",
        "设持久 replay 在有限登记模数 `Q` 上已经不能终止。任一后续 fresh prime `ell` 满足 `gcd(ell,Q)=1`，"
        "因此 `ell` 层是旧 CRT 周期之外的新坐标。若该层不触发 PDEC/ColumnCRT，则反例链在 `ell` 层只能记录一个被禁止的相位；"
        "对无界多个 fresh primes 重复此过程，就得到区间 `1<=k<P` 内避开每个素数 `q<=P^0.43` 的一个指定余类的粗筛对象。",
        "",
        "该对象与既有 B3 尾段接口一致：对 squarefree `d<P`，CRT 只留下一个模 `d` 的禁余类集合，"
        "其计数为 `(P-1)/d` 加不超过 `1` 的端点误差。",
        "",
        "## 2. 读数",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| registered replay blocks | {result['registered_replay_block_count']} |",
        f"| min first fresh log10 gain | {result['minimum_first_fresh_log10_gain']:.3f} |",
        f"| min 8-fresh sample log10 gain | {result['minimum_sample_log10_gain']:.3f} |",
        f"| tail alpha | {result['tail_sieve_alpha']:.6f} |",
        f"| model main at P=100000 | {result['tail_sieve_model_main_at_100000']:.6f} |",
        f"| 10% surplus over 401 | {result['tail_sieve_ten_percent_surplus_over_401']:.6f} |",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["gates"]:
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
            "## 4. 剩余基",
            "",
            "严格自足 branch-replay 路线：",
            "",
            "```text",
            result["strict_branch_remaining_basis"],
            "```",
            "",
            "接受外部或标准筛输入的 branch-replay 路线：",
            "",
            "```text",
            result["external_or_standard_branch_remaining_basis"],
            "```",
            "",
            "继承的全局 strict 剩余基：",
            "",
            "```text",
            result["inherited_global_strict_remaining_basis"],
            "```",
            "",
            "本证书不宣称行/列命题已无条件闭合；它只把无界 fresh-modulus 分支压入 tail-sieve/PDEC 双出口。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    result = build_result()
    write_outputs(result)
    print(f"wrote {OUT_LEDGER}")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
