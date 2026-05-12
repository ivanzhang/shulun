#!/usr/bin/env python3
"""生成 strict 大高度有限 RH 验证输入路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_large_finite_rh_verification_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-large-finite-rh-verification-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-large-finite-rh-verification-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-large-finite-rh-verification-router.md"

ZERO_INPUT = MONOGRAPH / "prime-matrix-strict-verified-zero-zero-free-tail-input-router.json"
LOW_HEIGHT = MONOGRAPH / "prime-matrix-lowheight-backlund-self-contained-package-router.md"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [ZERO_INPUT, LOW_HEIGHT, CLAIM_STATUS]

TARGET = "LargeFiniteRHVerificationForPsiEpsilonTableLedger"
EXTERNAL_GOURDON = "Gourdon10^13FiniteRHVerificationExternalAcceptedForTableInput"
DATA = "LargeZeroDatasetAndChecksumLedger"
ALGORITHM = "RiemannSiegelLargeHeightZeroComputationAlgorithmLedger"
TURING = "LargeHeightTuringCompletenessLedger"
COUNT_MAP = "ZeroIndexToHeightRangeMappingLedger"
TABLE_INTERFACE = "FiniteRHVerificationToPsiEpsilonTableInterfaceLedger"
LOW_HEIGHT_SELF = "RiemannSiegelIntervalArithmetic0To14Ledger AND CriticalLineSignSeparationFiniteLedger0To14 AND TuringArgumentPrincipleBoxCount0To14Ledger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

GOURDON_URL = "http://numbers.computation.free.fr/Constants/Miscellaneous/zetazeros1e13-1e24.pdf"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
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


def build_result() -> dict[str, Any]:
    """构造大高度有限 RH 验证输入证书。"""
    zero_input = load_json(ZERO_INPUT)
    active = zero_input.get("next_direct_attack_target") == TARGET
    source_extraction_ready = zero_input.get("zero_input_source_extraction_closed") is True
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            zero_input.get("counterexample_assumption_only") is True
            and zero_input.get("row_column_unconditional_closed") is False,
            True,
            "本步只审计 epsilon 表的大高度有限 RH 输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "LargeFiniteRHGateActive",
            active,
            True,
            "上一证书把下一最窄点设为 epsilon 表所需的大高度有限 RH 验证。",
            TARGET,
        ),
        row(
            "GourdonExternalSourceIdentified",
            source_extraction_ready,
            False,
            "Dusart 文中登记 Gourdon 10^13 非平凡零点验证作为外部来源；这可作外部条件输入。",
            EXTERNAL_GOURDON,
        ),
        row(
            "LowHeightSelfContainedPackageNotScalableSubstitute",
            True,
            True,
            "0<t<=14 的自足 Riemann-Siegel/Turing 包即使完成，也只覆盖低高度；不能替代 10^13 零点级大证书。",
            LOW_HEIGHT_SELF,
        ),
        row(
            DATA,
            False,
            False,
            "作者侧自足需要原始或可压缩验证数据、分块校验和、版本和独立复算入口。",
            "zero block data/hash/checksum archive",
        ),
        row(
            ALGORITHM,
            False,
            False,
            "需要说明大高度 Riemann-Siegel/ Odlyzko-Schönhage 等计算算法、舍入控制和误差界。",
            "large-height zero computation proof",
        ),
        row(
            TURING,
            False,
            False,
            "需要 Turing 方法或等价 argument-principle 计数，证明没有漏零且所有零在临界线上。",
            "large-height Turing completeness certificate",
        ),
        row(
            COUNT_MAP,
            False,
            False,
            "需要把前 10^13 零点数量转成表生成算法实际使用的高度区间和覆盖阈值。",
            TABLE_INTERFACE,
        ),
        row(
            TABLE_INTERFACE,
            False,
            False,
            "需要证明该有限 RH 验证高度足以支撑 eps_psi(28) 和中段 psi 表值的具体常数。",
            "table generator uses finite RH height plus zero-free tail",
        ),
        row(
            TARGET,
            False,
            False,
            "大高度有限 RH 输入尚未作者侧闭合；外部 Gourdon 可登记，但不是仓库自足证书。",
            f"{DATA} AND {ALGORITHM} AND {TURING} AND {COUNT_MAP} AND {TABLE_INTERFACE}",
        ),
        row(
            "ExternalConditionalLaneAvailable",
            True,
            False,
            "若接受 Gourdon 外部证书，可把该输入作为外部条件推进到零点自由尾项和桥接审查。",
            EXTERNAL_GOURDON,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "大高度有限 RH 输入审计不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_large_finite_rh_verification_router",
        "status": "large_finite_rh_verification_external_gourdon_available_self_contained_data_algorithm_turing_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "large_finite_rh_external_source_identified": source_extraction_ready,
        "large_finite_rh_verification_self_contained_closed": False,
        "external_gourdon_conditional_lane_available": True,
        "large_zero_dataset_checksum_closed": False,
        "large_zero_algorithm_closed": False,
        "large_height_turing_completeness_closed": False,
        "zero_index_to_height_mapping_closed": False,
        "finite_rh_to_psi_table_interface_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "external_reference": {
            "id": "Gourdon 2004",
            "url": GOURDON_URL,
            "claim_boundary": "first 10^13 nontrivial zeros verified on the critical line",
            "role": "external conditional source, not repository self-contained data/hash",
        },
        "replacement_self_contained": {
            TARGET: f"{DATA} AND {ALGORITHM} AND {TURING} AND {COUNT_MAP} AND {TABLE_INTERFACE}",
            EXTERNAL_GOURDON: "accepted external certificate only; does not close self-contained route",
        },
        "next_direct_attack_target": "ExplicitZeroFreeRegionForTableTailLedger",
        "parallel_attack_targets": [DATA, ALGORITHM, TURING, COUNT_MAP, TABLE_INTERFACE],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "大高度有限 RH 输入的边界已明确：外部路线可登记 Gourdon `10^13` 零点验证；"
            "作者侧自足路线则需要数据/hash、计算算法、Turing 完备性、零点编号到高度映射和表生成接口。"
            "`T<=14` 低高度包不能替代该输入。本步仍不关闭 epsilon 表，只把该项分成外部条件通道和自足五包。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 大高度有限 RH 验证输入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"large_finite_rh_external_source_identified={fmt_bool(result['large_finite_rh_external_source_identified'])}",
        f"large_finite_rh_verification_self_contained_closed={fmt_bool(result['large_finite_rh_verification_self_contained_closed'])}",
        f"external_gourdon_conditional_lane_available={fmt_bool(result['external_gourdon_conditional_lane_available'])}",
        f"large_zero_dataset_checksum_closed={fmt_bool(result['large_zero_dataset_checksum_closed'])}",
        f"large_zero_algorithm_closed={fmt_bool(result['large_zero_algorithm_closed'])}",
        f"large_height_turing_completeness_closed={fmt_bool(result['large_height_turing_completeness_closed'])}",
        f"zero_index_to_height_mapping_closed={fmt_bool(result['zero_index_to_height_mapping_closed'])}",
        f"finite_rh_to_psi_table_interface_closed={fmt_bool(result['finite_rh_to_psi_table_interface_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部边界",
        "",
        f"- `{result['external_reference']['id']}`：{result['external_reference']['url']}",
        f"- claim boundary：{result['external_reference']['claim_boundary']}",
        f"- role：{result['external_reference']['role']}",
        "",
        "## 2. 自足替换",
        "",
        "```text",
    ]
    for key, value in result["replacement_self_contained"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 3. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
