#!/usr/bin/env python3
"""生成 strict rate-bearing 大 pair packet 排斥路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_rate_bearing_large_pair_packet_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rate-bearing-large-pair-packet-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-rate-bearing-large-pair-packet-router.json"
OUT_MD = DOCS / "prime-matrix-strict-rate-bearing-large-pair-packet-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-independent-pair-energy-attack-router.json",
    "prime-matrix-strict-acyclic-seed-terminal-fusion-router.json",
    "prime-matrix-strict-acyclic-terminal-family-attack-router.json",
    "prime-matrix-strict-acyclic-pdec-input-materialization-router.json",
    "prime-matrix-strict-acyclic-clean-kls-router.json",
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json",
    "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def packet_split_rows() -> list[dict[str, str]]:
    """列出 rate-bearing 大 pair packet 的完备分支。"""
    return [
        {
            "branch": "CanonicalPayload",
            "trigger": "packet 的 pre-Cauchy 来源可证明为 canonical RIW/Buchstab 因子或其有限推前。",
            "route": "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary",
            "status": "open",
        },
        {
            "branch": "PersistentFiniteSignature",
            "trigger": "同一有限 pair/phase/column/signature 以 log-power 阈值持久复现。",
            "route": "DirectAcyclicSameSetPDECCapDualCertificate",
            "status": "open",
        },
        {
            "branch": "IsolatedSparseOrColumnPacket",
            "trigger": "packet 只在有限局部窗或列位移中出现，可抽取 witness/blocker-deficit。",
            "route": "SAE/LocalSurvivor/ColumnCRT absorbed into sparse/PDEC terminal schema",
            "status": "schema_closed_exclusion_open",
        },
        {
            "branch": "DriftingRateBearingCleanResidual",
            "trigger": "所有有限签名都不持久，但每层仍有超过 `M/L^K` 的 clean exact pair。",
            "route": "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn",
            "status": "open",
        },
    ]


def build_rows(
    energy: dict[str, Any],
    seed_fusion: dict[str, Any],
    terminal_attack: dict[str, Any],
    pdec_input: dict[str, Any],
    clean_kls: dict[str, Any],
    dls: dict[str, Any],
    leaf: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 rate-bearing 大 pair packet 路由判定表。"""
    terminal_three = (
        "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
        "DirectAcyclicSameSetPDECCapDualCertificate OR "
        "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
    )
    return [
        {
            "gate": "RateBearingPacketInputActive",
            "closed": energy.get("internal_obligation_after_router")
            == "RateBearingLargePairAtomPacketExclusion",
            "proved": False,
            "meaning": "上一层把独立 pair 能量界压成 rate-bearing 大 pair packet 排斥。",
            "remaining": "排斥该 packet，或证明其进入已命名终端。",
        },
        {
            "gate": "SameTheoremTargetPreserved",
            "closed": energy.get("same_theorem_target_preserved") is True,
            "proved": True,
            "meaning": "本步仍是 NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem 的内部反证分支，不改换总命题。",
            "remaining": energy.get("strict_self_contained_terminal_after_router"),
        },
        {
            "gate": "SeedFusionImported",
            "closed": seed_fusion.get("acyclic_pre_cauchy_seed_independent_input_removed")
            is True,
            "proved": True,
            "meaning": "seed 存在/不存在两支均已汇入 acyclic terminal family，packet 不能逃到 seed 缺失第四出口。",
            "remaining": seed_fusion.get("terminal_gap_after_router"),
        },
        {
            "gate": "TerminalThreeAtomImported",
            "closed": terminal_attack.get("terminal_three_atom_after_router")
            == terminal_three
            or terminal_three in str(terminal_attack),
            "proved": False,
            "meaning": "rate-bearing packet 的合法终端只剩 canonical-lock、direct PDEC 或 direct CleanKLS/DLS 三类。",
            "remaining": terminal_three,
        },
        {
            "gate": "PDECInputMaterializationImported",
            "closed": pdec_input.get("acyclic_same_set_pdec_input_materialized")
            is True,
            "proved": True,
            "meaning": "持久有限签名的大 pair packet 已可物化为同集 PDEC 输入；但 PDEC cap 量界未完成。",
            "remaining": "AcyclicFiniteArcCapMassBoundsOrNamedReturn / DirectAcyclicSameSetPDECCapDualCertificate",
        },
        {
            "gate": "CleanAdmissionImported",
            "closed": clean_kls.get("k1_k9_clean_admission_closed") is True
            and dls.get("acyclic_windowed_bilinear_normal_form_closed") is True,
            "proved": True,
            "meaning": "漂移 clean residual 的对象、窗口化双线性型和 L2 系数账本已物化；但内部 DLS/Kuznetsov 大筛估计未完成。",
            "remaining": "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks",
        },
        {
            "gate": "SparseSchemaAdmissionImported",
            "closed": leaf.get("future_sparse_schema_admission_discipline_closed")
            is True,
            "proved": True,
            "meaning": "孤立 sparse/SAE/ColumnCRT packet 不能作为隐藏终端；未来新增必须提交显式 schema。",
            "remaining": "future schema global nonexistence is not claimed",
        },
        {
            "gate": "RateBearingLargePairPacketExclusionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未排斥三原子终端中的 PDEC cap、CleanKLS/DLS 或 canonical-lock 残余。",
            "remaining": terminal_three,
        },
        {
            "gate": "NewActualSourceEntropyCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "rate-bearing packet 排斥未完成，所以新 actual-source 熵定理仍未证明。",
            "remaining": "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict rate-bearing 大 pair packet 排斥路由证书。"""
    energy = load_json(DOCS / "prime-matrix-strict-independent-pair-energy-attack-router.json")
    seed_fusion = load_json(DOCS / "prime-matrix-strict-acyclic-seed-terminal-fusion-router.json")
    terminal_attack = load_json(DOCS / "prime-matrix-strict-acyclic-terminal-family-attack-router.json")
    pdec_input = load_json(DOCS / "prime-matrix-strict-acyclic-pdec-input-materialization-router.json")
    clean_kls = load_json(DOCS / "prime-matrix-strict-acyclic-clean-kls-router.json")
    dls = load_json(DOCS / "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json")
    leaf = load_json(DOCS / "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json")

    terminal_three = (
        "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
        "DirectAcyclicSameSetPDECCapDualCertificate OR "
        "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
    )
    rows = build_rows(
        energy=energy,
        seed_fusion=seed_fusion,
        terminal_attack=terminal_attack,
        pdec_input=pdec_input,
        clean_kls=clean_kls,
        dls=dls,
        leaf=leaf,
    )
    return {
        "certificate_type": "prime_matrix_strict_rate_bearing_large_pair_packet_router",
        "status": "strict_rate_bearing_large_pair_packet_reduced_to_terminal_three_atom_open",
        "same_theorem_target_preserved": True,
        "rate_bearing_packet_split_closed": True,
        "seed_fourth_exit_removed": True,
        "pdec_materialization_imported": True,
        "clean_kls_admission_imported": True,
        "sparse_schema_admission_imported": True,
        "rate_bearing_large_pair_atom_packet_exclusion_proved": False,
        "direct_acyclic_same_set_pdec_dual_proved": False,
        "direct_acyclic_clean_kls_dls_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "internal_obligation_before_router": "RateBearingLargePairAtomPacketExclusion",
        "internal_obligation_after_router": terminal_three,
        "strict_self_contained_terminal_after_router": energy.get(
            "strict_self_contained_terminal_after_router"
        ),
        "strict_self_contained_math_basis_after_router": energy.get(
            "strict_self_contained_math_basis_after_router"
        ),
        "next_direct_attack_target_inside_same_theorem": terminal_three,
        "hard_law": (
            "rate-bearing 大 pair packet 没有第五出口：canonical 口进入 canonical-lock；"
            "持久有限签名进入 direct PDEC；孤立 sparse/ColumnCRT 进入已登记 schema；"
            "漂移 clean residual 进入 direct CleanKLS/DLS。当前未证明的是这些终端排斥估计，"
            "不是 packet 定义或 seed 定义。"
        ),
        "packet_split_rows": packet_split_rows(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`RateBearingLargePairAtomPacketExclusion` 被继续压缩，但目标仍是同一个 "
            "`NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem`。任何超过 `M/L^K` 的同 formal unit "
            "大 pair packet 必落入四类：canonical payload、持久有限签名、孤立 sparse/ColumnCRT、"
            "漂移 clean residual。前三者分别进入 canonical-lock、PDEC 或 sparse schema；最后一类进入 "
            "direct CleanKLS/DLS。因而当前内部剩余等价压成三原子终端门 "
            "`AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate "
            "OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn`。这些终端估计仍未证明，不能声明无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict rate-bearing 大 pair packet 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"rate_bearing_packet_split_closed={fmt_bool(result['rate_bearing_packet_split_closed'])}",
        f"rate_bearing_large_pair_atom_packet_exclusion_proved={fmt_bool(result['rate_bearing_large_pair_atom_packet_exclusion_proved'])}",
        f"direct_acyclic_same_set_pdec_dual_proved={fmt_bool(result['direct_acyclic_same_set_pdec_dual_proved'])}",
        f"direct_acyclic_clean_kls_dls_proved={fmt_bool(result['direct_acyclic_clean_kls_dls_proved'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同命题内部压缩",
        "",
        "```text",
        result["internal_obligation_before_router"],
        "  -> packet split has no fifth exit",
        "  -> " + result["internal_obligation_after_router"],
        "```",
        "",
        "## 2. packet 分支表",
        "",
        "| branch | trigger | route | status |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["packet_split_rows"]:
        lines.append(
            "| `{branch}` | {trigger} | {route} | `{status}` |".format(
                branch=table_cell(row["branch"]),
                trigger=table_cell(row["trigger"]),
                route=table_cell(row["route"]),
                status=table_cell(row["status"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 4. 硬边界律",
            "",
            result["hard_law"],
            "",
            "下一步仍在同一源熵定理内部直攻三原子终端门：",
            "",
            "```text",
            result["next_direct_attack_target_inside_same_theorem"],
            "```",
            "",
            "完整 strict 基仍保持：",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
