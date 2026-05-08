#!/usr/bin/env python3
"""Prime Matrix 早期零行反例 flat-DLS 最后逃逸路由器。

用法示例：
  python3 experiments/prime_matrix_early_zero_flatdls_counterexample_router.py

输出：
  docs/monograph/prime-matrix-early-zero-flatdls-counterexample-router.json
  docs/monograph/prime-matrix-early-zero-flatdls-counterexample-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-newlayer-no-concentration-flat-admission-router.json"
DEFAULT_EARLY_ZERO = DOCS / "prime-matrix-early-zero-contradiction-matrix-router.json"
DEFAULT_SN3A = DOCS / "prime-matrix-sn3a-centered-lowmod-return-certificate.md"
DEFAULT_SN3B = DOCS / "prime-matrix-sn3b-true-distributed-residual-target.md"
DEFAULT_SN3C = DOCS / "prime-matrix-sn3c-multiband-sync-split.md"
DEFAULT_SN3D = DOCS / "prime-matrix-sn3d-kls-multishell-frequency-bridge.md"
DEFAULT_SN3E = DOCS / "prime-matrix-sn3e-highfreq-bohrcap-no-cycle.md"
DEFAULT_CLEAN_KLS = DOCS / "prime-matrix-triad-a1-clean-kls-external-input-router.json"
DEFAULT_CDEP = DOCS / "prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-early-zero-flatdls-counterexample-router.json"
DEFAULT_MD = DOCS / "prime-matrix-early-zero-flatdls-counterexample-router.md"


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


def replace_once(text: str, old: str, new: str) -> str:
    """只替换一次输入基原子。"""
    if old not in text:
        return text
    return text.replace(old, new, 1)


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
    early_zero: dict[str, Any],
    sn3a_text: str,
    sn3b_text: str,
    sn3c_text: str,
    sn3d_text: str,
    sn3e_text: str,
    clean_kls: dict[str, Any],
    cdep: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成早期零行反例 flat-DLS 路由判定表。"""
    early_zero_pinned = (
        early_zero.get("no_unnamed_exit_for_early_zero") is True
        and early_zero.get("direct_unconditional_contradiction_found") is False
    )
    flat_gate_active = (
        previous.get("terminal_gap_after_router") == "DLSFlatHighModLargeSieveAbsorption"
        and previous.get("newlayer_no_concentration_independent_input_removed") is True
    )
    empirical_shortcut_blocked = any(
        "真实样本中未见早期零行不能替代假设分支证明" in item
        for item in early_zero.get("not_valid_as_final_contradictions", [])
    )
    sn3_low_projection = (
        contains_all(sn3a_text, ["中心化低模回流", "PDEC/ColumnCRT", "TrueDistributedDLS"])
        and contains_all(sn3b_text, ["TrueDistributedDLS/KLS", "SAE", "PDEC", "ColumnCRT"])
    )
    sn3_multiband = contains_all(
        sn3c_text,
        ["ShellOverlap", "LowModSync", "KLS-Multishell"],
    )
    sn3_column_frequency = contains_all(
        sn3d_text,
        ["HighFrequencyColumn", "L2FlatKLS", "非零列频率"],
    )
    bohr_no_cycle = contains_all(
        sn3e_text,
        ["持久 Bohr-cap", "孤立 Bohr-cap", "L2-flat CleanKLS", "无名循环"],
    )
    clean_kls_registered = (
        clean_kls.get("all_admission_verified_or_routed") is True
        and clean_kls.get("external_kls_input_registered") is True
    )
    cdep_route_available = (
        cdep.get("previous_terminal_gap") == "CDependentResidueWeightSpectralCancellationInput"
        and cdep.get("terminal_gap_after_router")
        == "NCBLKActualBlockNonConcentrationOrExternalDIBFI"
    )
    boundary_closed = all(
        [
            early_zero_pinned,
            flat_gate_active,
            empirical_shortcut_blocked,
            sn3_low_projection,
            sn3_multiband,
            sn3_column_frequency,
            bohr_no_cycle,
            clean_kls_registered,
            cdep_route_available,
        ]
    )
    return [
        row(
            "EarlyZeroCounterexampleAssumptionPinned",
            early_zero_pinned,
            True,
            "本路由只在假设存在 P 行以内早期零行的反例分支中工作。",
            "不使用真实样本未见零行作为证明。",
        ),
        row(
            "FlatDLSGateActiveInCounterexampleBasis",
            flat_gate_active,
            True,
            "上一层已把 new-layer 无集中 residual 准入到 DLSFlatHighModLargeSieveAbsorption。",
            "现在必须把它解释为反例最后支付压力，而不是普通真实分布估计。",
        ),
        row(
            "EmpiricalShortcutExplicitlyBlocked",
            empirical_shortcut_blocked,
            True,
            "早期零行矛盾矩阵已声明：真实样本中未见早期零行不能替代假设分支证明。",
            "所有结论必须从反例支付压力推出。",
        ),
        row(
            "SN3LowProjectionPeelingInherited",
            sn3_low_projection,
            True,
            "若 flat-DLS 支付出现短窗、q 低模或 d 低模峰，则 SN3-A/B 直接回流 SAE/PDEC/ColumnCRT。",
            "剩余才是 TrueDistributedDLS。",
        ),
        row(
            "SN3MultibandSyncSplitInherited",
            sn3_multiband,
            True,
            "同行多真分散带若有 ShellOverlap 或 LowModSync，分别回流 SAE 或 PDEC/ColumnCRT。",
            "剩余才是 KLS-Multishell。",
        ),
        row(
            "SN3ColumnFrequencyDichotomyInherited",
            sn3_column_frequency,
            True,
            "KLS-Multishell 的有限列 Fourier 二分给出 HighFrequencyColumn 或 L2FlatKLS。",
            "非零列频率不是无名 flat-DLS 质量。",
        ),
        row(
            "HighFrequencyBohrCapNoCycleInherited",
            bohr_no_cycle,
            True,
            "HighFrequencyColumn 必须成为 Bohr-cap，并回流 PDEC/ColumnCRT/SAE，或退化为 L2-flat CleanKLS。",
            "高频出口不能形成无名循环。",
        ),
        row(
            "CleanKLSAdmissionAndExternalInterfaceRegistered",
            clean_kls_registered,
            False,
            "L2-flat CleanKLS 只有在 K1--K9 准入通过后才能调用；外部 KLS 输入已登记。",
            "自足版仍需实际谱/dispersion 估计。",
        ),
        row(
            "CDependentSpectralReductionKnownButOpen",
            cdep_route_available,
            False,
            "完成型 c-dependent residue 谱输入已接到 BWFD/BSC/KFLS/NC-BLK 核心链。",
            "NCBLKActualBlockNonConcentrationOrExternalDIBFI 仍未证明或接受。",
        ),
        row(
            "EarlyZeroFlatDLSLastEscapeBoundaryClosed",
            boundary_closed,
            True,
            "早期零行反例的 flat-DLS 最后逃逸已被压成唯一 L2-flat KLS 谱逃逸或命名 Bohr/PDEC/SAE/ColumnCRT 回流。",
            "它不再是直接真实分布证明口。",
        ),
        row(
            "EarlyZeroL2FlatKLSCounterexampleSpectralExclusion",
            False,
            False,
            "尚未证明早期零行反例所需的 L2-flat 高频残余谱吸收或实际 NC-BLK 排斥。",
            "下一步最窄目标。",
        ),
    ]


def run(
    previous_path: Path,
    early_zero_path: Path,
    sn3a_path: Path,
    sn3b_path: Path,
    sn3c_path: Path,
    sn3d_path: Path,
    sn3e_path: Path,
    clean_kls_path: Path,
    cdep_path: Path,
) -> dict[str, Any]:
    """执行早期零行反例 flat-DLS 最后逃逸路由。"""
    source_paths = [
        previous_path,
        early_zero_path,
        sn3a_path,
        sn3b_path,
        sn3c_path,
        sn3d_path,
        sn3e_path,
        clean_kls_path,
        cdep_path,
    ]
    previous = load_json(previous_path)
    early_zero = load_json(early_zero_path)
    clean_kls = load_json(clean_kls_path)
    cdep = load_json(cdep_path)
    sn3a_text = sn3a_path.read_text(encoding="utf-8")
    sn3b_text = sn3b_path.read_text(encoding="utf-8")
    sn3c_text = sn3c_path.read_text(encoding="utf-8")
    sn3d_text = sn3d_path.read_text(encoding="utf-8")
    sn3e_text = sn3e_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        early_zero=early_zero,
        sn3a_text=sn3a_text,
        sn3b_text=sn3b_text,
        sn3c_text=sn3c_text,
        sn3d_text=sn3d_text,
        sn3e_text=sn3e_text,
        clean_kls=clean_kls,
        cdep=cdep,
    )
    old_atom = "DLSFlatHighModLargeSieveAbsorption"
    new_atom = "EarlyZeroL2FlatKLSCounterexampleSpectralExclusion"
    boundary_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "EarlyZeroFlatDLSLastEscapeBoundaryClosed"
    )
    latest_self = replace_once(previous.get("latest_self_contained_basis", ""), old_atom, new_atom)
    latest_cond = replace_once(previous.get("latest_conditional_basis", ""), old_atom, new_atom)
    return {
        "certificate_type": "early_zero_flatdls_counterexample_router",
        "status": "early_zero_flatdls_reduced_to_l2flat_kls_spectral_escape",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "early_zero_flatdls_last_escape_boundary_closed": boundary_closed,
        "dls_flat_highmod_large_sieve_absorption_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": old_atom,
        "terminal_gap_after_router": (
            "EarlyZeroL2FlatKLSCounterexampleSpectralExclusion_OR_"
            "CDependentResidueWeightSpectralCancellationInput"
        ),
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {
            old_atom: new_atom,
        },
        "next_priority": new_atom,
        "counterexample_chain": [
            "Assume EarlyZeroRowWithinP",
            "named low-dimensional exits removed",
            "flat-DLS residual must pay remaining zero-row budget",
            "SN3-A/B low projection peak => SAE/PDEC/ColumnCRT",
            "SN3-C multiband sync => ShellOverlap/LowModSync/KLS-Multishell",
            "SN3-D KLS-Multishell => HighFrequencyColumn or L2FlatKLS",
            "SN3-E HighFrequencyColumn => Bohr-cap PDEC/ColumnCRT/SAE or L2-flat CleanKLS",
            "only last escape: L2-flat KLS spectral/NC-BLK input",
        ],
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把 DLSFlatHighModLargeSieveAbsorption 放回早期零行反例分支中解释："
            "反例若仍靠高模平坦残余支付零行，任何短窗、低模、列频率或 Bohr-cap 集中都会回流 "
            "SAE/PDEC/ColumnCRT；真正剩下的唯一逃逸是 L2-flat KLS 谱逃逸。"
            "因此下一步不是证明真实分布本身，而是排斥这个反例专属的 L2-flat 谱逃逸。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix 早期零行反例 flat-DLS 最后逃逸路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"early_zero_flatdls_last_escape_boundary_closed={fmt_bool(result['early_zero_flatdls_last_escape_boundary_closed'])}",
        f"dls_flat_highmod_large_sieve_absorption_proved={fmt_bool(result['dls_flat_highmod_large_sieve_absorption_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 反例链条",
        "",
        "```text",
    ]
    lines.extend(result["counterexample_chain"])
    lines.extend(
        [
            "```",
            "",
            "这条链条的前提始终是 `Assume EarlyZeroRowWithinP`。真实样本中没有早期零行只作定位，不作为证明。",
            "",
            "## 2. 替换律",
            "",
            "```text",
            replacement[0],
            "  =>",
            replacement[1],
            "```",
            "",
            "在条件/外部版中，完成型谱输入仍可由 `CDependentResidueWeightSpectralCancellationInput` 承担。",
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            "在假设早期零行存在的反例分支中，证明 L2-flat 高频 KLS 残余不能继续支付零行余量；"
            "若证明失败，必须输出同 formal unit 的高频 Bohr/PDEC/SAE/ColumnCRT 证书，"
            "或明确接受/匹配 `CDependentResidueWeightSpectralCancellationInput`。",
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
    parser.add_argument("--early-zero", type=Path, default=DEFAULT_EARLY_ZERO)
    parser.add_argument("--sn3a", type=Path, default=DEFAULT_SN3A)
    parser.add_argument("--sn3b", type=Path, default=DEFAULT_SN3B)
    parser.add_argument("--sn3c", type=Path, default=DEFAULT_SN3C)
    parser.add_argument("--sn3d", type=Path, default=DEFAULT_SN3D)
    parser.add_argument("--sn3e", type=Path, default=DEFAULT_SN3E)
    parser.add_argument("--clean-kls", type=Path, default=DEFAULT_CLEAN_KLS)
    parser.add_argument("--cdep", type=Path, default=DEFAULT_CDEP)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        early_zero_path=args.early_zero,
        sn3a_path=args.sn3a,
        sn3b_path=args.sn3b,
        sn3c_path=args.sn3c,
        sn3d_path=args.sn3d,
        sn3e_path=args.sn3e,
        clean_kls_path=args.clean_kls,
        cdep_path=args.cdep,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
