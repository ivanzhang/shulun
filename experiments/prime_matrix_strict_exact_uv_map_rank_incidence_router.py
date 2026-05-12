#!/usr/bin/env python3
"""生成 strict exact-UV map rank/incidence 路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_exact_uv_map_rank_incidence_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-exact-uv-map-rank-incidence-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-exact-uv-map-rank-incidence-router.json"
OUT_MD = DOCS / "prime-matrix-strict-exact-uv-map-rank-incidence-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-emitter-multiplicity-rank-attack-router.json",
    "prime-matrix-triad-a1-factor-residue-incidence-router.json",
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json",
    "prime-matrix-clean-core-alpha-delta-disintegration-router.json",
    "prime-matrix-registered-capacity-multiplier-discipline-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典，兼容旧归档。"""
    if not path.exists():
        return {}
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


def build_rows(
    rank_router: dict[str, Any],
    incidence: dict[str, Any],
    dls: dict[str, Any],
    disintegration: dict[str, Any],
    multiplier: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 exact-UV map rank/incidence 判定表。"""
    target = "PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem"
    next_atom = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
    return [
        {
            "gate": "MapRankNoCollapseTargetActive",
            "closed": rank_router.get("terminal_gap_after_router") == target,
            "proved": False,
            "meaning": "上一层已把 primitive emitter multiplicity 压成 exact `(u,v)` map rank/no-collapse。",
            "remaining": target,
        },
        {
            "gate": "NaiveFactorResidueIncidenceBlocked",
            "closed": incidence.get("naive_incidence_bridge_valid") is False,
            "proved": True,
            "meaning": "一个 moving `(u,v)` 块可含大量内部 atom；内部平坦不推出 factor-pair 支撑。",
            "remaining": next_atom,
        },
        {
            "gate": "DLSInvertibleVariablesPostCompletionOnly",
            "closed": dls.get("phase_invertible_variable_ledger_closed") is True,
            "proved": True,
            "meaning": "相位/可逆变量账本服务窗口化谱估计，不证明 pre-Cauchy emitter 到 exact `(u,v)` 的有界重数。",
            "remaining": next_atom,
        },
        {
            "gate": "DisintegrationDictionaryNotIncidenceBound",
            "closed": disintegration.get("lift_equivalent_to_signed_disintegration_dictionary")
            is True,
            "proved": True,
            "meaning": "解积分字典给源测度和推前恒等式；仍需证明字典原像在 exact `(u,v)` 上不坍缩。",
            "remaining": next_atom,
        },
        {
            "gate": "CapacityMultipliersDoNotCreateRank",
            "closed": multiplier.get("registered_capacity_multiplier_discipline_closed")
            is True,
            "proved": True,
            "meaning": "容量乘子纪律只约束权重放大，不产生 image support 或 map rank。",
            "remaining": next_atom,
        },
        {
            "gate": "RankEquivalentToBoundedMultiplicityIncidence",
            "closed": True,
            "proved": False,
            "meaning": "map rank/no-collapse 的正面内容正是 actual emitter 源参数与 exact `(u,v)` 的有界重数 incidence。",
            "remaining": next_atom,
        },
        {
            "gate": "ActualEmitterExactUVBoundedMultiplicityIncidenceCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前语料尚未证明适用于 actual noncanonical pre-Cauchy emitter 的有界重数 incidence。",
            "remaining": next_atom,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict exact-UV map rank/incidence 证书。"""
    rank_router = load_json(DOCS / "prime-matrix-strict-emitter-multiplicity-rank-attack-router.json")
    incidence = load_json(DOCS / "prime-matrix-triad-a1-factor-residue-incidence-router.json")
    dls = load_json(DOCS / "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json")
    disintegration = load_json(DOCS / "prime-matrix-clean-core-alpha-delta-disintegration-router.json")
    multiplier = load_json(DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json")

    target = "PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem"
    next_atom = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
    rows = build_rows(
        rank_router=rank_router,
        incidence=incidence,
        dls=dls,
        disintegration=disintegration,
        multiplier=multiplier,
    )
    return {
        "certificate_type": "prime_matrix_strict_exact_uv_map_rank_incidence_router",
        "status": "strict_exact_uv_map_rank_reduced_to_actual_emitter_bounded_multiplicity_incidence_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "exact_uv_map_rank_incidence_router_closed": True,
        "naive_factor_residue_incidence_blocked": True,
        "dls_invertible_variables_not_precauchy_rank": True,
        "capacity_multiplier_not_rank_source": True,
        "pre_cauchy_emitter_exact_uv_map_rank_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": next_atom,
        "next_direct_attack_target": next_atom,
        "incidence_contract": (
            "For the actual noncanonical pre-Cauchy emitter, prove a bounded-multiplicity "
            "incidence theorem between primitive source parameters and exact balanced factor "
            "pairs (u,v): each exact pair has at most |Domain|/L^K preimages, after registered "
            "branch/sign/local-factor refinement."
        ),
        "hard_law": (
            "exact-UV map rank 的正面内容不是相位可逆性，也不是谱估计变量可逆性；"
            "它是一个 source-level incidence 定理。旧的朴素 FactorResidueIncidence 已被内部 fiber "
            "反模型阻断，所以这里需要 actual emitter 专用的有界重数 incidence，而不是复用 K4/K6 或 DLS 账本。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem` 继续压缩为 "
            "`ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem`。这一步保持同一源熵目标，"
            "只是把“map rank”翻译成真正需要证明的 source-level 有界重数 incidence。"
            "当前语料尚未证明该 incidence，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict exact-UV map rank/incidence 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"exact_uv_map_rank_incidence_router_closed={fmt_bool(result['exact_uv_map_rank_incidence_router_closed'])}",
        f"naive_factor_residue_incidence_blocked={fmt_bool(result['naive_factor_residue_incidence_blocked'])}",
        f"dls_invertible_variables_not_precauchy_rank={fmt_bool(result['dls_invertible_variables_not_precauchy_rank'])}",
        f"actual_emitter_exact_uv_bounded_multiplicity_incidence_proved={fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 压缩",
        "",
        "压缩前：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "压缩后：",
        "",
        "```text",
        result["terminal_gap_after_router"],
        "```",
        "",
        "incidence 合同：",
        "",
        "```text",
        result["incidence_contract"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 结构结论",
            "",
            result["hard_law"],
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
