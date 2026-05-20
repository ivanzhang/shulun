#!/usr/bin/env python3
"""生成 source-atom multiplicity cap 到 ExactUV fixed-key 原子的桥接证书。

用法示例：
  python3 experiments/prime_matrix_source_atom_multiplicity_cap_exactuv_fixed_key_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-source-atom-multiplicity-cap-exactuv-fixed-key-bridge-router.json

输出：
  data/prime-matrix-source-atom-multiplicity-cap-exactuv-fixed-key-bridge-ledger.json
  docs/monograph/prime-matrix-source-atom-multiplicity-cap-exactuv-fixed-key-bridge-router.json
  docs/monograph/prime-matrix-source-atom-multiplicity-cap-exactuv-fixed-key-bridge-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-source-atom-multiplicity-cap-exactuv-fixed-key-bridge"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-endpoint-pivot-duplicate-same-slot-multiplicity-cap-import-router.json"
MULTIPLICITY_FIBER_CERT = DOCS / (
    "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-"
    "signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-router.json"
)
EXACTUV_SYNC_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"
SOURCE_ATOMIZATION_CERT = DOCS / "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json"
COMPLETE_KEY_CERT = DOCS / "prime-matrix-strict-complete-emitter-key-partition-router.json"
SOURCE_TABLE_CERT = DOCS / "prime-matrix-strict-actual-emitter-source-table-router.json"

SOURCE_CAP = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityCapPDECCap"
)
SOURCE_TABLE = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
BRIDGE_TARGET = f"({SOURCE_TABLE} AND {COMPLETE_KEY} AND {FIXED_KEY})"

IMPORT = "StableLadderEndpointOrbitSourceAtomMultiplicityCapImportedForExactUVFixedKeyBridgeLedger"
KEY_FIELD = "StableLadderEndpointOrbitSourceAtomMultiplicitySameSourceKeyFieldLedger"
SOURCE_TABLE_GATE = "StableLadderEndpointOrbitSourceAtomMultiplicityActualEmitterSourceTableGateLedger"
COMPLETE_KEY_GATE = "StableLadderEndpointOrbitSourceAtomMultiplicityCompleteKeyPartitionGateLedger"
FIXED_KEY_GATE = "StableLadderEndpointOrbitSourceAtomMultiplicityFixedKeyLocalMultiplicityGateLedger"
NO_INDEPENDENT = "NoIndependentSourceAtomMultiplicityCapAfterExactUVFixedKeyBridgeLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def source_hashes() -> dict[str, str]:
    """登记本脚本与桥接上游证书哈希。"""
    paths = [
        Path(__file__).resolve(),
        PREVIOUS_CERT,
        MULTIPLICITY_FIBER_CERT,
        EXACTUV_SYNC_CERT,
        SOURCE_ATOMIZATION_CERT,
        COMPLETE_KEY_CERT,
        SOURCE_TABLE_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def replace_cap(target: str) -> str:
    """把 source-atom multiplicity cap 替换成 ExactUV fixed-key 原子合取。"""
    if SOURCE_CAP not in target:
        return f"{target} AND {BRIDGE_TARGET}" if target else BRIDGE_TARGET
    return target.replace(SOURCE_CAP, BRIDGE_TARGET)


def replace_latest_basis(previous: dict[str, Any], reduced: str) -> str:
    """更新活动基，把上一层直接目标替换为本层 bridge 目标。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    old = previous.get("next_direct_attack_target", "")
    if basis and old and old in basis:
        return basis.replace(old, reduced)
    return reduced


def build_rows(
    previous: dict[str, Any],
    fiber: dict[str, Any],
    exactuv: dict[str, Any],
    atomization: dict[str, Any],
    complete_key: dict[str, Any],
    source_table: dict[str, Any],
    new_target: str,
) -> list[dict[str, Any]]:
    """构造 bridge 判定表。"""
    imported = SOURCE_CAP in previous.get("next_direct_attack_target", "")
    packet_registered = fiber.get(
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_packet_registered"
    ) is True
    exactuv_imported = exactuv.get("deterministic_source_atom_implication_closed") is True
    atomization_imported = atomization.get("deterministic_source_atom_implication_closed") is True
    source_table_open = source_table.get("actual_noncanonical_primitive_emitter_source_table_proved") is False
    complete_key_open = complete_key.get("registered_complete_primitive_emitter_key_partition_polylog_proved") is False
    fixed_key_open = atomization.get("fixed_key_exact_uv_local_multiplicity_o1_ledger_proved") is False
    return [
        row(
            "SourceAtomMultiplicityCapImported",
            imported,
            False,
            "导入 source-atom multiplicity-cap PDEC/cap 硬点。",
            SOURCE_CAP,
        ),
        row(
            "SourceAtomMultiplicityCapPacketRegistered",
            packet_registered,
            False,
            "multiplicity-fiber 层已把超过局部 cap 的同源重数登记为独立 cap packet。",
            IMPORT,
        ),
        row(
            "SourceAtomMultiplicitySameSourceKeyField",
            imported and packet_registered,
            True,
            "cap 的重数单位共享同一 source atom 字段；若字段不一致，则回到 source-table/key mismatch 命名出口。",
            KEY_FIELD,
        ),
        row(
            "ExactUVSourceAtomImplicationImported",
            exactuv_imported and atomization_imported,
            True,
            "ExactUV source-rank 链已记录：actual source table、complete key、fixed-key 局部 O(1) 重数合取即可给出固定 key 无坍缩。",
            f"{SOURCE_TABLE} AND {COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "ActualEmitterSourceTableGate",
            source_table_open,
            False,
            "没有 actual noncanonical primitive emitter source table 时，source atom 只是后验标签，cap 不能被固定 key 账本支付。",
            SOURCE_TABLE,
        ),
        row(
            "CompleteKeyPartitionGate",
            complete_key_open,
            False,
            "没有 complete key 分区时，同一 source atom 的重数无法与 fixed exact-UV key 对齐。",
            COMPLETE_KEY,
        ),
        row(
            "FixedKeyLocalMultiplicityGate",
            fixed_key_open,
            False,
            "真正排斥 fixed source atom 大重数需要固定 key exact-UV local multiplicity O(1) 账本。",
            FIXED_KEY,
        ),
        row(
            "NoIndependentSourceAtomMultiplicityCapAfterExactUVBridge",
            imported and packet_registered,
            True,
            "source-atom multiplicity cap 不再作为 endpoint 局部独立出口保留；它被桥接到 ExactUV source-rank 三原子。",
            NO_INDEPENDENT,
        ),
        row(
            "SourceAtomMultiplicityCapReducedToExactUVFixedKeyAtoms",
            imported and packet_registered,
            False,
            "本步只完成桥接归约；三原子本身仍未证明。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 source-atom multiplicity cap bridge 证书。"""
    previous = load_json(PREVIOUS_CERT)
    fiber = load_json(MULTIPLICITY_FIBER_CERT)
    exactuv = load_json(EXACTUV_SYNC_CERT)
    atomization = load_json(SOURCE_ATOMIZATION_CERT)
    complete_key = load_json(COMPLETE_KEY_CERT)
    source_table = load_json(SOURCE_TABLE_CERT)
    new_target = replace_cap(previous.get("next_direct_attack_target", ""))
    reduced = " AND ".join(
        [
            IMPORT,
            KEY_FIELD,
            SOURCE_TABLE_GATE,
            COMPLETE_KEY_GATE,
            FIXED_KEY_GATE,
            NO_INDEPENDENT,
            new_target,
        ]
    )
    rows = build_rows(previous, fiber, exactuv, atomization, complete_key, source_table, new_target)
    imported = any(item["gate"] == "SourceAtomMultiplicityCapImported" and item["closed"] for item in rows)
    bridge_closed = any(
        item["gate"] == "NoIndependentSourceAtomMultiplicityCapAfterExactUVBridge" and item["closed"]
        for item in rows
    )
    plain = (
        "source-atom multiplicity cap 已桥接到 ExactUV source-rank/no-collapse 三原子："
        "actual emitter source table、complete key partition、fixed-key exact-UV local multiplicity O(1)。"
        "本步只移除 endpoint 局部独立 cap 口径；不证明三原子，也不证明行/列命题。"
    )
    return {
        "certificate_type": "prime_matrix_source_atom_multiplicity_cap_exactuv_fixed_key_bridge_router",
        "status": "source_atom_multiplicity_cap_bridged_to_exactuv_fixed_key_atoms_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "multiplicity_fiber_certificate": str(MULTIPLICITY_FIBER_CERT.relative_to(ROOT)),
        "exactuv_sync_certificate": str(EXACTUV_SYNC_CERT.relative_to(ROOT)),
        "source_atomization_certificate": str(SOURCE_ATOMIZATION_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "source_atom_multiplicity_cap_imported": imported,
        "source_atom_multiplicity_cap_packet_registered": fiber.get(
            "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_packet_registered"
        )
        is True,
        "source_atom_multiplicity_same_source_key_field_closed": imported,
        "exactuv_source_atom_implication_imported": exactuv.get("deterministic_source_atom_implication_closed") is True,
        "strict_source_atomization_imported": atomization.get("deterministic_source_atom_implication_closed") is True,
        "actual_noncanonical_primitive_emitter_source_table_proved": False,
        "complete_primitive_emitter_key_partition_ledger_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_ledger_proved": False,
        "source_atom_multiplicity_cap_reduced_to_exactuv_fixed_key_atoms": bridge_closed,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "row_column_unconditional_closed": False,
        "old_exits": [SOURCE_CAP],
        "new_exits": [SOURCE_TABLE, COMPLETE_KEY, FIXED_KEY],
        "hardpoint_before_router": SOURCE_CAP,
        "hardpoint_after_router": BRIDGE_TARGET,
        "parallel_open_exits": [
            "SparseScaleLadderSAESummability",
            "StableLadderEndpointSingletonAtomSAE",
            "EndpointOrbitFullCycleMeanAtomSAE",
            "EndpointOrbitAlternatingCyclePivotPrimeDuplicatePaymentSparseSAESummability",
            "EndpointOrbitAlternatingCyclePivotPrimeSameAPTablePaymentInjectionLock",
            "EndpointOrbitAlternatingCyclePivotPrimeCrossTableSwitchPDECOrMovingPivot",
        ],
        "gates": rows,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "next_direct_attack_target": new_target,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def write_markdown(cert: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    lines = [
        "# Prime Matrix source-atom multiplicity cap ExactUV fixed-key bridge 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"source_atom_multiplicity_cap_imported={fmt_bool(cert['source_atom_multiplicity_cap_imported'])}",
        f"source_atom_multiplicity_cap_packet_registered={fmt_bool(cert['source_atom_multiplicity_cap_packet_registered'])}",
        f"source_atom_multiplicity_same_source_key_field_closed={fmt_bool(cert['source_atom_multiplicity_same_source_key_field_closed'])}",
        f"exactuv_source_atom_implication_imported={fmt_bool(cert['exactuv_source_atom_implication_imported'])}",
        f"strict_source_atomization_imported={fmt_bool(cert['strict_source_atomization_imported'])}",
        f"actual_noncanonical_primitive_emitter_source_table_proved={fmt_bool(cert['actual_noncanonical_primitive_emitter_source_table_proved'])}",
        f"complete_primitive_emitter_key_partition_ledger_proved={fmt_bool(cert['complete_primitive_emitter_key_partition_ledger_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_o1_ledger_proved={fmt_bool(cert['fixed_key_exact_uv_local_multiplicity_o1_ledger_proved'])}",
        f"source_atom_multiplicity_cap_reduced_to_exactuv_fixed_key_atoms={fmt_bool(cert['source_atom_multiplicity_cap_reduced_to_exactuv_fixed_key_atoms'])}",
        f"source_atom_multiplicity_cap_pdec_cap_proved={fmt_bool(cert['source_atom_multiplicity_cap_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 桥接公式",
        "",
        "```text",
        f"{SOURCE_CAP}",
        "  ->",
        f"{SOURCE_TABLE}",
        f"AND {COMPLETE_KEY}",
        f"AND {FIXED_KEY}",
        "```",
        "",
        "含义：同一 source atom 的大重数若要成为真实反例，必须先有 actual emitter source table，"
        "再有 complete key 分区，最后由 fixed-key exact-UV local multiplicity O(1) 排斥固定 key 下的大原像坍缩。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | {cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 4. 诚实边界",
            "",
            "- 本证书没有证明 actual emitter source table。",
            "- 本证书没有证明 complete key partition。",
            "- 本证书没有证明 fixed-key exact-UV local multiplicity O(1)。",
            "- 本证书没有证明 duplicate sparse SAE、payment injection、cross-table switch 或其他 endpoint 并行出口。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_MD.write_text(write_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
