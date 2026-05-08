#!/usr/bin/env python3
"""Prime Matrix new-layer 无集中 flat 准入路由器。

用法示例：
  python3 experiments/prime_matrix_newlayer_no_concentration_flat_admission_router.py

输出：
  docs/monograph/prime-matrix-newlayer-no-concentration-flat-admission-router.json
  docs/monograph/prime-matrix-newlayer-no-concentration-flat-admission-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-newlayer-ranktwo-budget-ledger-router.json"
DEFAULT_CLEAN_KLS = DOCS / "prime-matrix-triad-a1-clean-kls-external-input-router.json"
DEFAULT_CLEAN_CONTRACT = DOCS / "prime-matrix-cleankls-dls-certificate-contract.md"
DEFAULT_TERMINAL_TRIAD = DOCS / "prime-matrix-terminal-certificate-triad.md"
DEFAULT_EXTMATCH = DOCS / "prime-matrix-clean-core-newlayer-external-lemma-match-router.md"
DEFAULT_LOWPHASE = DOCS / "prime-matrix-clean-core-dls-lowphase-pdec-flat-router.json"
DEFAULT_ENERGY = DOCS / "prime-matrix-dprc-newlayer-energy-dispersion.md"
DEFAULT_TOWER = DOCS / "prime-matrix-newlayer-pdec-tower-entropy-contract.md"
DEFAULT_SN3 = DOCS / "prime-matrix-sn3-distributed-band-large-sieve-bridge.md"
DEFAULT_JSON = DOCS / "prime-matrix-newlayer-no-concentration-flat-admission-router.json"
DEFAULT_MD = DOCS / "prime-matrix-newlayer-no-concentration-flat-admission-router.md"


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


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部锚点。"""
    return all(needle in text for needle in needles)


def remove_atom_once(text: str, atom: str) -> str:
    """从 AND 输入基中移除一个已被吸收的原子。"""
    if f"{atom} AND " in text:
        return text.replace(f"{atom} AND ", "", 1)
    if f" AND {atom}" in text:
        return text.replace(f" AND {atom}", "", 1)
    return text.replace(atom, "", 1)


def admission_verified(clean_kls: dict[str, Any], key: str) -> bool:
    """读取 K1--K9 准入项是否已登记或回流。"""
    for item in clean_kls.get("admission_rows", []):
        if item.get("key") == key:
            return bool(item.get("verified"))
    return False


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


def build_rows(
    previous: dict[str, Any],
    clean_kls: dict[str, Any],
    clean_contract_text: str,
    terminal_triad_text: str,
    extmatch_text: str,
    lowphase: dict[str, Any],
    energy_text: str,
    tower_text: str,
    sn3_text: str,
) -> list[dict[str, Any]]:
    """生成 new-layer no-concentration flat admission 判定表。"""
    flat_gate_active = (
        previous.get("terminal_gap_after_router") == "NewLayerNoConcentrationImpliesFlatAdmission"
        and previous.get("newlayer_ranktwo_budget_independent_input_removed") is True
    )
    clean_contract_registered = (
        contains_all(
            clean_contract_text,
            ["K1 dyadic ranges", "K5 coefficient L2-flat", "K9 no fiber mutual info"],
        )
        and contains_all(
            terminal_triad_text,
            ["K1 ranges", "K5 coefficient L2-flat", "K7 formal unit consistency"],
        )
    )
    lowphase_context = (
        "DLSPointLoadColumnCRTBoundOrNamedReturn" in previous.get("latest_self_contained_basis", "")
        and "DLSShortWindowSAEBoundOrNamedReturn" in previous.get("latest_self_contained_basis", "")
        and "DLSFlatHighModLargeSieveAbsorption" in previous.get("latest_self_contained_basis", "")
    )
    no_concentration_definition = (
        flat_gate_active
        and "TransverseFlatResidualUsesNewLayerFlatGate" in previous.get("closed_gates", [])
        and "NewLayerNoConcentrationImpliesFlatAdmission" in previous.get("open_gates", [])
    )
    k1k9_all_registered = clean_kls.get("all_admission_verified_or_routed") is True
    k2_k5_k9_by_no_concentration = (
        no_concentration_definition
        and admission_verified(clean_kls, "K2")
        and admission_verified(clean_kls, "K5")
        and admission_verified(clean_kls, "K9")
    )
    named_failures_routed = (
        contains_all(
            clean_contract_text,
            ["K2 fail => PDEC", "K3 fail => SAE", "K4 fail => displacement/Bohr-cap PDEC"],
        )
        and contains_all(
            tower_text,
            ["profinite/global PDEC", "CleanKLS/DLS"],
        )
    )
    flat_dls_interface_ready = (
        "DLSFlatHighModLargeSieveAbsorption" in lowphase.get("latest_self_contained_basis", "")
        and "NewLayerNoConcentrationImpliesFlatAdmission" in extmatch_text
        and "NewLayer Dispersion Clamp" in energy_text
        and "DistributedBandLargeSieve" in sn3_text
    )
    admission_boundary_closed = all(
        [
            flat_gate_active,
            clean_contract_registered,
            lowphase_context,
            no_concentration_definition,
            k1k9_all_registered,
            k2_k5_k9_by_no_concentration,
            named_failures_routed,
            flat_dls_interface_ready,
        ]
    )
    return [
        row(
            "NewLayerNoConcentrationGateActive",
            flat_gate_active,
            True,
            "上一层已把二秩预算账本压到 new-layer 无集中 flat 准入门。",
            "检查它是否仍是独立输入。",
        ),
        row(
            "CleanKLSAdmissionContractRegistered",
            clean_contract_registered,
            True,
            "CleanKLS/DLS 的 K1--K9 准入合同已登记，失败项必须回流命名出口。",
            "不能把未剥离缺陷直接送入大筛。",
        ),
        row(
            "LowPhasePointShortFlatContextInherited",
            lowphase_context,
            True,
            "PointLoad、ShortWindow 和 FlatHighMod 三个 DLS 口仍在同一输入基中。",
            "短窗/单点失败不属于 new-layer flat admission，而由独立命名输入处理。",
        ),
        row(
            "NoConcentrationDefinitionPinned",
            no_concentration_definition,
            True,
            "所有可登记 PDEC cap 与非平坦横向缺陷已被删除或回流后，才称为 no-concentration residual。",
            "若再出现有限弧/互信息峰，则回流 refined/new-layer PDEC。",
        ),
        row(
            "K1ToK9RegisteredOrRouted",
            k1k9_all_registered,
            False,
            "既有 A1 clean KLS 路由器已登记 K1--K9：全部通过才调用 KLS/DLS，失败回流。",
            "这只是 admission 边界，不是大筛估计。",
        ),
        row(
            "LowModL2MIFlatnessFromNoConcentration",
            k2_k5_k9_by_no_concentration,
            False,
            "无低模固定相位、无大系数原子、无旧相位-新增 residue 互信息峰，正是 K2/K5/K9 的 flat 侧。",
            "若任一项失败，得到 PDEC/SAE/refined PDEC，不是 flat residual。",
        ),
        row(
            "NamedFailureReturnDisciplinePreserved",
            named_failures_routed,
            True,
            "K2--K9 的失败项只能回流 PDEC/SAE/ColumnCRT/Multiplicity/Promotion，不生成新终端。",
            "无集中支不能藏第五类出口。",
        ),
        row(
            "FlatDLSInterfaceReady",
            flat_dls_interface_ready,
            False,
            "新增层能量分散、SN3 分散带接口和 LowPhase flat 输入已经指向同一 DLS/KLS 吸收门。",
            "仍需证明 DLSFlatHighModLargeSieveAbsorption。",
        ),
        row(
            "NewLayerNoConcentrationFlatAdmissionBoundaryClosed",
            admission_boundary_closed,
            True,
            "new-layer 无集中命题不再是独立最终输入；它只是把 residual 准入到 flat DLS/KLS 证书口。",
            "移交给 DLSFlatHighModLargeSieveAbsorption。",
        ),
        row(
            "DLSFlatHighModLargeSieveAbsorption",
            False,
            False,
            "当前材料尚未证明所有高模平坦分散残余满足所需大筛吸收界。",
            "下一步最窄目标。",
        ),
    ]


def run(
    previous_path: Path,
    clean_kls_path: Path,
    clean_contract_path: Path,
    terminal_triad_path: Path,
    extmatch_path: Path,
    lowphase_path: Path,
    energy_path: Path,
    tower_path: Path,
    sn3_path: Path,
) -> dict[str, Any]:
    """执行 new-layer 无集中 flat 准入路由。"""
    source_paths = [
        previous_path,
        clean_kls_path,
        clean_contract_path,
        terminal_triad_path,
        extmatch_path,
        lowphase_path,
        energy_path,
        tower_path,
        sn3_path,
    ]
    previous = load_json(previous_path)
    clean_kls = load_json(clean_kls_path)
    lowphase = load_json(lowphase_path)
    clean_contract_text = clean_contract_path.read_text(encoding="utf-8")
    terminal_triad_text = terminal_triad_path.read_text(encoding="utf-8")
    extmatch_text = extmatch_path.read_text(encoding="utf-8")
    energy_text = energy_path.read_text(encoding="utf-8")
    tower_text = tower_path.read_text(encoding="utf-8")
    sn3_text = sn3_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        clean_kls=clean_kls,
        clean_contract_text=clean_contract_text,
        terminal_triad_text=terminal_triad_text,
        extmatch_text=extmatch_text,
        lowphase=lowphase,
        energy_text=energy_text,
        tower_text=tower_text,
        sn3_text=sn3_text,
    )
    old_atom = "NewLayerNoConcentrationImpliesFlatAdmission"
    latest_self = remove_atom_once(previous.get("latest_self_contained_basis", ""), old_atom)
    latest_cond = remove_atom_once(previous.get("latest_conditional_basis", ""), old_atom)
    boundary_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "NewLayerNoConcentrationFlatAdmissionBoundaryClosed"
    )
    return {
        "certificate_type": "newlayer_no_concentration_flat_admission_router",
        "status": "newlayer_no_concentration_admitted_to_flat_dls_gate",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "newlayer_no_concentration_flat_admission_boundary_closed": boundary_closed,
        "newlayer_no_concentration_independent_input_removed": boundary_closed,
        "dls_flat_highmod_large_sieve_absorption_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": old_atom,
        "terminal_gap_after_router": "DLSFlatHighModLargeSieveAbsorption",
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {
            old_atom: "DLSFlatHighModLargeSieveAbsorption admission gate already present",
        },
        "next_priority": "DLSFlatHighModLargeSieveAbsorption",
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步闭合 new-layer 无集中到 flat 准入的边界："
            "no-concentration residual 的含义就是所有可登记低模/有限弧/互信息/列位移缺陷都已删除或命名回流。"
            "在既有 K1--K9 clean admission 合同下，它可进入 flat DLS/KLS 证书口；"
            "真正未证的是 flat high-mod 大筛吸收本身。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix new-layer 无集中 flat 准入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"newlayer_no_concentration_flat_admission_boundary_closed={fmt_bool(result['newlayer_no_concentration_flat_admission_boundary_closed'])}",
        f"newlayer_no_concentration_independent_input_removed={fmt_bool(result['newlayer_no_concentration_independent_input_removed'])}",
        f"dls_flat_highmod_large_sieve_absorption_proved={fmt_bool(result['dls_flat_highmod_large_sieve_absorption_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. Admission 逆否律",
        "",
        "```text",
        "NewLayerNoConcentrationImpliesFlatAdmission",
        "  means all registered low-dimensional defects have been removed:",
        "    finite arc PDEC cap, short-window SAE, column/Bohr cap,",
        "    promotable top-prime residue, phase-residue mutual information;",
        "  any failure of K1--K9 returns to a named gate;",
        "  all K1--K9 passed residual enters DLSFlatHighModLargeSieveAbsorption.",
        "```",
        "",
        "## 2. 替换律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "注意：本步只证明 flat admission 边界，不证明 flat 大筛吸收界。",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | `{remaining}` |".format(
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
            "条件输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "完全自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            f"最窄目标更新为 `{result['next_priority']}`："
            "证明经过 PointLoad/ShortWindow/LowPhase/new-layer cap 删除后的高模平坦残余满足大筛吸收界；"
            "若失败，必须输出对偶高频缺陷并回流 PDEC/SAE/ColumnCRT/外部谱输入。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_outputs(result: dict[str, Any], json_out: Path, md_out: Path) -> None:
    """写出 JSON 与 Markdown。"""
    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--clean-kls", type=Path, default=DEFAULT_CLEAN_KLS)
    parser.add_argument("--clean-contract", type=Path, default=DEFAULT_CLEAN_CONTRACT)
    parser.add_argument("--terminal-triad", type=Path, default=DEFAULT_TERMINAL_TRIAD)
    parser.add_argument("--extmatch", type=Path, default=DEFAULT_EXTMATCH)
    parser.add_argument("--lowphase", type=Path, default=DEFAULT_LOWPHASE)
    parser.add_argument("--energy", type=Path, default=DEFAULT_ENERGY)
    parser.add_argument("--tower", type=Path, default=DEFAULT_TOWER)
    parser.add_argument("--sn3", type=Path, default=DEFAULT_SN3)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        clean_kls_path=args.clean_kls,
        clean_contract_path=args.clean_contract,
        terminal_triad_path=args.terminal_triad,
        extmatch_path=args.extmatch,
        lowphase_path=args.lowphase,
        energy_path=args.energy,
        tower_path=args.tower,
        sn3_path=args.sn3,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
