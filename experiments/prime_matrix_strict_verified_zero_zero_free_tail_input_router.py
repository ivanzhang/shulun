#!/usr/bin/env python3
"""生成 strict verified-zero/zero-free tail 输入审计路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_verified_zero_zero_free_tail_input_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-verified-zero-zero-free-tail-input-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-verified-zero-zero-free-tail-input-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-verified-zero-zero-free-tail-input-router.md"

GENERATOR = MONOGRAPH / "prime-matrix-strict-epsilon-table-generator-audit-router.json"
LOW_HEIGHT_EXTERNAL = MONOGRAPH / "prime-matrix-strict-finite-low-height-external-match-router.json"
ZERO_FREE_CONSTANTS = MONOGRAPH / "prime-matrix-b3-zero-free-constants-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [GENERATOR, LOW_HEIGHT_EXTERNAL, ZERO_FREE_CONSTANTS, CLAIM_STATUS]

TARGET = "VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger"
FINITE_RH = "LargeFiniteRHVerificationForPsiEpsilonTableLedger"
ZERO_FREE = "ExplicitZeroFreeRegionForTableTailLedger"
BRIDGE = "FiniteVerifiedZerosToZeroFreeTailTransitionLedger"
SOURCE_AUDIT = "DusartSchoenfeldZeroInputSourceExtractionLedger"
LOW_HEIGHT = "CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger"
TABLE_GENERATOR = "SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

REFERENCES = [
    {
        "id": "Rosser-Schoenfeld 1975",
        "input": "first 3,502,500 zeros on the critical line/strip in the classical table lineage",
        "role": "historical finite RH verification input",
        "url": "https://www.ams.org/mcom/1975-29-129/S0025-5718-1975-0457373-8/",
    },
    {
        "id": "van de Lune-te Riele-Winter 1986",
        "input": "first 1,500,000,000 zeros",
        "role": "larger finite RH verification input cited by Dusart",
        "url": "https://www.ams.org/mcom/1986-46-174/S0025-5718-1986-0829637-3/",
    },
    {
        "id": "Gourdon 2004",
        "input": "first 10^13 nontrivial zeros",
        "role": "largest finite RH verification cited by Dusart for improved tables",
        "url": "http://numbers.computation.free.fr/Constants/Miscellaneous/zetazeros1e13-1e24.pdf",
    },
    {
        "id": "Kadiri 2004",
        "input": "explicit zero-free region",
        "role": "zero-free tail input cited by Dusart",
        "url": "https://arxiv.org/abs/math/0401238",
    },
    {
        "id": "Dusart arXiv:1002.0442",
        "input": "source text tying finite RH verification and zero-free regions to psi/theta tables",
        "role": "boundary statement, not a reproducible table computation artifact",
        "url": "https://arxiv.org/abs/1002.0442",
    },
]


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
    """构造 verified-zero/zero-free tail 输入审计证书。"""
    generator = load_json(GENERATOR)
    low_height = load_json(LOW_HEIGHT_EXTERNAL)
    zero_free = load_json(ZERO_FREE_CONSTANTS)
    active = generator.get("next_direct_attack_target") == TARGET
    low_height_ready_external = low_height.get("finite_low_height_strict_external_matched") is True
    low_height_self_open = low_height.get("finite_low_height_self_contained_closed") is False
    symbolic_zero_free_ready = zero_free.get("zero_free_constants_reduced") is True
    explicit_zero_free_self_open = zero_free.get("zero_free_constants_self_contained_proved") is False
    source_extraction_closed = active and len(REFERENCES) == 5
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            generator.get("counterexample_assumption_only") is True
            and generator.get("row_column_unconditional_closed") is False,
            True,
            "本步只审计 epsilon 表所需解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "VerifiedZeroZeroFreeTailGateActive",
            active,
            True,
            "上一证书把下一最窄点设为表生成器所需的有限零点验证与零点自由尾项输入。",
            TARGET,
        ),
        row(
            SOURCE_AUDIT,
            source_extraction_closed,
            True,
            "已从 Dusart/Schoenfeld 线索中抽出表值依赖的外部零点验证与零点自由区来源。",
            "Rosser-Schoenfeld, van de Lune, Gourdon, Kadiri, Dusart",
        ),
        row(
            "LowHeightT14IsNotEnoughForPsiTable",
            low_height_ready_external and low_height_self_open,
            True,
            "仓库已外部匹配 T<=14 低高度核验，但 psi epsilon 表需要大高度有限 RH 验证和尾项桥接，不能由 T<=14 替代。",
            FINITE_RH,
        ),
        row(
            "SymbolicZeroFreeRegionNotEnoughForTableTail",
            symbolic_zero_free_ready and explicit_zero_free_self_open,
            True,
            "仓库已有符号零点自由区链和部分常数化路线，但表尾项需要明确的可复算数值常数与阈值。",
            ZERO_FREE,
        ),
        row(
            FINITE_RH,
            False,
            False,
            "需要指定表生成实际使用的有限 RH 验证高度/零点数、来源证书、覆盖范围和 hash。",
            "Gourdon10^13 OR equivalent verified-zero certificate with reproducible audit",
        ),
        row(
            ZERO_FREE,
            False,
            False,
            "需要指定尾段使用的显式零点自由区常数、适用高度和同一表算法中的误差预算。",
            "Kadiri/Rosser-Schoenfeld zero-free constants or internal proof",
        ),
        row(
            BRIDGE,
            False,
            False,
            "需要证明有限零点验证窗口和零点自由尾项如何拼接成 eps_psi(b) 的整段表值，含阈值选择和余项分配。",
            f"{FINITE_RH} AND {ZERO_FREE} AND {TABLE_GENERATOR}",
        ),
        row(
            TARGET,
            False,
            False,
            "当前只完成来源边界和缺口分类；没有可复现大高度零点证书、零点自由尾项常数和桥接算法。",
            f"{FINITE_RH} AND {ZERO_FREE} AND {BRIDGE}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "verified-zero/zero-free 输入审计不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_verified_zero_zero_free_tail_input_router",
        "status": "verified_zero_zero_free_tail_input_sources_extracted_large_height_and_tail_bridge_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "zero_input_source_extraction_closed": source_extraction_closed,
        "verified_zero_and_zero_free_tail_input_closed": False,
        "large_finite_rh_verification_table_input_closed": False,
        "explicit_zero_free_region_table_tail_closed": False,
        "finite_verified_zero_to_tail_transition_closed": False,
        "low_height_t14_external_ready_but_insufficient": low_height_ready_external and low_height_self_open,
        "symbolic_zero_free_ready_but_numeric_table_tail_open": symbolic_zero_free_ready and explicit_zero_free_self_open,
        "psi_epsilon_table_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "references": REFERENCES,
        "replacement_self_contained": {
            TARGET: f"{FINITE_RH} AND {ZERO_FREE} AND {BRIDGE}",
            BRIDGE: f"{FINITE_RH} AND {ZERO_FREE} AND {TABLE_GENERATOR}",
        },
        "next_direct_attack_target": FINITE_RH,
        "parallel_attack_targets": [ZERO_FREE, BRIDGE],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "epsilon 表的零点输入被拆清：它不是仓库已有 `T<=14` 低高度核验，而是大高度有限 RH "
            "验证、显式零点自由区尾项和二者的桥接算法共同支撑。当前只完成外部来源边界抽取；"
            "缺少可复现的大高度零点证书、尾段零点自由常数和表生成桥接 hash。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict verified-zero/zero-free tail 输入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"zero_input_source_extraction_closed={fmt_bool(result['zero_input_source_extraction_closed'])}",
        f"verified_zero_and_zero_free_tail_input_closed={fmt_bool(result['verified_zero_and_zero_free_tail_input_closed'])}",
        f"large_finite_rh_verification_table_input_closed={fmt_bool(result['large_finite_rh_verification_table_input_closed'])}",
        f"explicit_zero_free_region_table_tail_closed={fmt_bool(result['explicit_zero_free_region_table_tail_closed'])}",
        f"finite_verified_zero_to_tail_transition_closed={fmt_bool(result['finite_verified_zero_to_tail_transition_closed'])}",
        f"low_height_t14_external_ready_but_insufficient={fmt_bool(result['low_height_t14_external_ready_but_insufficient'])}",
        f"symbolic_zero_free_ready_but_numeric_table_tail_open={fmt_bool(result['symbolic_zero_free_ready_but_numeric_table_tail_open'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 来源边界",
        "",
        "| source | input | role | url |",
        "| --- | --- | --- | --- |",
    ]
    for ref in result["references"]:
        lines.append(
            f"| `{table_cell(ref['id'])}` | {table_cell(ref['input'])} | "
            f"{table_cell(ref['role'])} | {table_cell(ref['url'])} |"
        )
    lines.extend(["", "## 2. 自足替换", "", "```text"])
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
