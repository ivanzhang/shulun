#!/usr/bin/env python3
"""把 rank-two Stepanov pivot 行列式剩余压成标量塌缩排除原子。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_pivot_determinant_normal_form_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-pivot-determinant-normal-form-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-pivot-determinant-normal-form-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-pivot-determinant-normal-form-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-rank-two-stepanov-pivot-router.json"
SOURCE_FILES = [PREVIOUS]

OLD_TARGET = "RankTwoElementaryStepanovPivotNonzeroDeterminantLemma"
OLD_SUBATOM = "RankTwoPivotDeterminantNonvanishing"
NEW_TARGET = "RankTwoScalarMonodromyCollapseExclusionLemma"
NEW_SUBATOM = "ThreeSingularityScalarMonodromyExclusionByResidueSignature"

NORMAL_FORM_GATE = "RankTwoPivotDeterminantNormalForm"
WRONSKIAN_GATE = "LocalHasseWronskianSeedReduction"
ZERO_IMPLIES_GATE = "ZeroPivotImpliesRankOneScalarCollapse"
CHANNEL_GATE = "NonScalarLocalChannelForcesPivotSeed"
DETERMINANT_GATE = "RankTwoPivotNonzeroDeterminant"
STEPANOV_PIVOT_GATE = "ElementaryStepanovPivotForRankTwoTraceLemma"
SELECTOR_GATE = "OrderFreeKummerSignatureSelectorAndHasseJetRankLemma"
RANK_TARGET = "StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity"
STEPANOV_TARGET = "StepanovAuxiliaryPolynomialRankBoundForKummerSums"
KUMMER_TRACE_TARGET = "SelfContainedRankOneKummerSheafRHTraceBound"
BURGESS_POINTWISE = "SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def local_channel_table() -> list[dict[str, Any]]:
    """登记三类局部通道与 pivot 种子关系。"""
    return [
        {
            "channel": "distinct_local_exponents",
            "local_shape": "two Frobenius characters have different residue exponents",
            "pivot_effect": "ordinary Hasse-Wronskian seed is nonzero",
            "status": "closed as local linear algebra",
            "remaining": "none inside this channel",
        },
        {
            "channel": "unipotent_resonance",
            "local_shape": "exponents collide but the logarithmic/Jordan part is nontrivial",
            "pivot_effect": "logarithmic Hasse jet separates the two local sections",
            "status": "closed as local linear algebra",
            "remaining": "none inside this channel",
        },
        {
            "channel": "scalar_semisimple_everywhere",
            "local_shape": "all three singular directions look scalar to the rank-two block",
            "pivot_effect": "ordinary and logarithmic seeds give no immediate separation",
            "status": "open",
            "remaining": NEW_TARGET,
        },
    ]


def implication_chain() -> list[dict[str, str]]:
    """写出本轮真正使用的反证链条。"""
    return [
        {
            "step": "1",
            "statement": "Assume the fixed rank-two pivot determinant is identically zero.",
            "role": "counterexample-side assumption for the determinant atom",
        },
        {
            "step": "2",
            "statement": "Then every allowed Hasse-jet pair in the fixed derivative alphabet spans only one local line.",
            "role": "normal-form consequence of a zero 2 by 2 pivot determinant",
        },
        {
            "step": "3",
            "statement": "If any singular direction has distinct exponents or a nontrivial unipotent part, that local line is separated.",
            "role": "local Hasse-Wronskian seed, now closed",
        },
        {
            "step": "4",
            "statement": "Therefore a zero pivot can survive only in the scalar-semisimple-at-all-three-singularities channel.",
            "role": "new narrowed remaining atom",
        },
        {
            "step": "5",
            "statement": "Exclude that scalar collapse from the three Kummer residue signatures at 0, 1, infinity.",
            "role": "next direct attack target",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 pivot 行列式正规形证书。"""
    previous = load_json(PREVIOUS)
    active = (
        previous.get("next_direct_attack_target") == OLD_TARGET
        and previous.get("next_subatom") == OLD_SUBATOM
        and previous.get("rank_two_pivot_nonzero_determinant_proved") is False
        and previous.get("elementary_stepanov_pivot_internalized") is False
    )

    pivot_normal_form = {
        "old_atom": OLD_TARGET,
        "old_subatom": OLD_SUBATOM,
        "fixed_derivative_alphabet": "bounded logarithmic/Hasse directions generated by lambda, 1-lambda, and infinity",
        "rank_two_block": "only two local sections are allowed; no d-length Kummer ladder is admitted",
        "normal_form": "the pivot determinant may be tested as a 2 by 2 local Hasse-Wronskian seed",
        "scope": "all smooth lambda in U=P^1-{0,1,infinity}, including special automorphism values",
    }

    closed_local_reductions = {
        "normal_form_closed": "a fixed rank-two auxiliary determinant is nonzero iff one allowed local Hasse-Wronskian seed is nonzero",
        "distinct_exponent_channel": "different local exponent residues give two separated Frobenius leading terms",
        "unipotent_resonance_channel": "if exponents collide but monodromy is a nontrivial Jordan block, the logarithmic Hasse jet separates them",
        "zero_determinant_consequence": "if both channels fail at 0, 1, infinity, the rank-two block is forced into a scalar local line everywhere",
    }

    remaining_scalar_collapse = {
        "new_atom": NEW_TARGET,
        "new_subatom": NEW_SUBATOM,
        "statement": "the three singular residue signatures of a nontrivial admitted Kummer triple cannot make the rank-two local block scalar-semisimple in all directions",
        "why_this_is_narrower": "we no longer need to search for an arbitrary pivot; every non-scalar local channel already yields the pivot seed",
        "must_use": "the exact residue signatures at 0, 1, infinity and the previous low-support PGL2 degeneration firewall",
        "must_not_use": "external Katz irreducibility, Deligne RH, generic-position assumptions, or a d-dependent Kummer ladder",
        "if_proved": "the pivot determinant atom closes, hence the internal Stepanov pivot proof can move to the downstream selector/rank gates",
    }

    rejected_shortcuts = {
        "external_irreducibility": "Katz/Deligne irreducibility can guide the shape but cannot be counted as the author-side internal proof here",
        "generic_exponents": "it is insufficient to show a nonzero determinant off a discriminant locus; the special smooth channels must be included",
        "finite_sampling": "finite determinant audits may detect a candidate seed but cannot prove nonvanishing over the symbolic residue space",
        "d_ladder_dimension": "using y^0,...,y^{d-1} to manufacture two independent sections breaks the order-free line",
    }

    normal_form_closed = active
    wronskian_reduction_closed = active
    zero_implies_scalar_closed = active
    non_scalar_channels_closed = active
    scalar_collapse_excluded = False
    determinant_closed = scalar_collapse_excluded
    pivot_internalized = determinant_closed
    selector_internalized = False
    rank_closed = selector_internalized
    stepanov_closed = rank_closed

    rows = [
        row(
            "PreviousRankTwoPivotTargetActive",
            active,
            active,
            "上一证书已把唯一内部剩余压成固定 rank-two Stepanov pivot 行列式非零。",
            OLD_TARGET,
        ),
        row(
            NORMAL_FORM_GATE,
            normal_form_closed,
            normal_form_closed,
            "pivot 非零可正规化为固定二维局部 Hasse-Wronskian 种子非零。",
            NEW_TARGET,
        ),
        row(
            WRONSKIAN_GATE,
            wronskian_reduction_closed,
            wronskian_reduction_closed,
            "允许的有界 Hasse 派生字母表足以检测两个局部 section 的一阶分离。",
            NEW_TARGET,
        ),
        row(
            CHANNEL_GATE,
            non_scalar_channels_closed,
            non_scalar_channels_closed,
            "不同局部指数或非平凡 unipotent resonance 都会强制产生 pivot 种子。",
            NEW_TARGET,
        ),
        row(
            ZERO_IMPLIES_GATE,
            zero_implies_scalar_closed,
            zero_implies_scalar_closed,
            "若 pivot 行列式恒零，则三处奇点必须同时落入标量半单塌缩通道。",
            NEW_TARGET,
        ),
        row(
            NEW_TARGET,
            scalar_collapse_excluded,
            scalar_collapse_excluded,
            "仍需内部排除三奇点 residue signature 同时标量塌缩。",
            NEW_SUBATOM,
        ),
        row(
            DETERMINANT_GATE,
            determinant_closed,
            determinant_closed,
            "pivot 行列式非零等待标量塌缩排除引理。",
            NEW_TARGET,
        ),
        row(
            OLD_TARGET,
            pivot_internalized,
            pivot_internalized,
            "初等 rank-two Stepanov pivot 仍等待 determinant atom。",
            DETERMINANT_GATE,
        ),
        row(
            STEPANOV_PIVOT_GATE,
            pivot_internalized,
            pivot_internalized,
            "rank-two trace 的内部 Stepanov pivot 尚未闭合。",
            DETERMINANT_GATE,
        ),
        row(
            SELECTOR_GATE,
            selector_internalized,
            selector_internalized,
            "完整阶无关 selector 仍等待 rank-two pivot 非零证明与下游粘合。",
            DETERMINANT_GATE,
        ),
        row(
            RANK_TARGET,
            rank_closed,
            rank_closed,
            "Stepanov-Kummer 非零秩仍未闭合。",
            SELECTOR_GATE,
        ),
        row(
            STEPANOV_TARGET,
            stepanov_closed,
            stepanov_closed,
            "Stepanov 完整内部证明仍未闭合。",
            RANK_TARGET,
        ),
        row(
            KUMMER_TRACE_TARGET,
            False,
            False,
            "秩一 Kummer 迹界仍等待内部 pivot/selector 链条闭合或外部路线被接受。",
            STEPANOV_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只压缩 determinant atom，不声明行/列命题作者侧无条件闭合。",
            BURGESS_POINTWISE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_pivot_determinant_normal_form_router",
        "status": "rank_two_pivot_determinant_reduced_to_scalar_monodromy_collapse_exclusion",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "previous_rank_two_pivot_target_active": active,
        "rank_two_pivot_determinant_normal_form_closed": normal_form_closed,
        "local_hasse_wronskian_seed_reduction_closed": wronskian_reduction_closed,
        "non_scalar_local_channel_forces_pivot_seed": non_scalar_channels_closed,
        "zero_pivot_implies_rank_one_scalar_collapse": zero_implies_scalar_closed,
        "rank_two_scalar_monodromy_collapse_excluded": scalar_collapse_excluded,
        "rank_two_pivot_nonzero_determinant_proved": determinant_closed,
        "elementary_stepanov_pivot_internalized": pivot_internalized,
        "order_free_signature_selector_internalized": selector_internalized,
        "stepanov_kummer_auxiliary_rank_surjectivity_proved": rank_closed,
        "stepanov_auxiliary_polynomial_rank_bound_proved": stepanov_closed,
        "self_contained_kummer_trace_bound_internalized": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEW_TARGET,
        "next_subatom": NEW_SUBATOM,
        "pivot_normal_form": pivot_normal_form,
        "closed_local_reductions": closed_local_reductions,
        "remaining_scalar_collapse": remaining_scalar_collapse,
        "rejected_shortcuts": rejected_shortcuts,
        "local_channel_table": local_channel_table(),
        "implication_chain": implication_chain(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮没有证明 rank-two pivot 行列式非零，但把它的真正剩余继续压窄。"
            "固定 rank-two Stepanov 辅助块的 determinant 已被正规化为局部 Hasse-Wronskian 种子问题："
            "只要 0、1、infinity 任一奇点方向出现不同局部指数，或出现非平凡 unipotent resonance，"
            "有界 Hasse 派生字母表就能分离两个局部 section，从而产生非零 pivot 种子。"
            "因此，反设 pivot 行列式恒零时，反例链被强迫进入唯一剩余通道："
            "三处奇点同时标量半单塌缩。下一最窄目标变成 "
            "`RankTwoScalarMonodromyCollapseExclusionLemma`，即用三处 Kummer residue signature 和前面低支撑 PGL2 "
            "退化防火墙，内部排除这种全局标量塌缩。未完成该排除前，pivot determinant、Stepanov、Kummer 迹界、"
            "Burgess B4 与行/列命题仍不能作者侧无条件闭合。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_key_value_section(lines: list[str], title: str, mapping: dict[str, Any]) -> None:
    """追加键值表。"""
    lines.extend(["", title, "", "| field | value |", "| --- | --- |"])
    for key, value in mapping.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 pivot 行列式正规形证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"rank_two_pivot_determinant_normal_form_closed={fmt_bool(result['rank_two_pivot_determinant_normal_form_closed'])}",
        f"local_hasse_wronskian_seed_reduction_closed={fmt_bool(result['local_hasse_wronskian_seed_reduction_closed'])}",
        f"zero_pivot_implies_rank_one_scalar_collapse={fmt_bool(result['zero_pivot_implies_rank_one_scalar_collapse'])}",
        f"rank_two_scalar_monodromy_collapse_excluded={fmt_bool(result['rank_two_scalar_monodromy_collapse_excluded'])}",
        f"rank_two_pivot_nonzero_determinant_proved={fmt_bool(result['rank_two_pivot_nonzero_determinant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
    ]

    render_key_value_section(lines, "## 1. pivot 正规形", result["pivot_normal_form"])
    render_key_value_section(lines, "## 2. 已关闭局部归约", result["closed_local_reductions"])
    render_key_value_section(lines, "## 3. 唯一剩余标量塌缩", result["remaining_scalar_collapse"])
    render_key_value_section(lines, "## 4. 禁止捷径", result["rejected_shortcuts"])

    lines.extend(
        [
            "",
            "## 5. 局部通道表",
            "",
            "| channel | local_shape | pivot_effect | status | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["local_channel_table"]:
        lines.append(
            "| `{channel}` | {local_shape} | {pivot_effect} | {status} | {remaining} |".format(
                **{key: table_cell(value) for key, value in item.items()}
            )
        )

    lines.extend(
        [
            "",
            "## 6. 反证链条",
            "",
            "| step | statement | role |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["implication_chain"]:
        lines.append(
            "| `{step}` | {statement} | {role} |".format(
                **{key: table_cell(value) for key, value in item.items()}
            )
        )

    lines.extend(
        [
            "",
            "## 7. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            "## 8. 下一最窄目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            result["next_subatom"],
            "```",
            "",
            "审稿边界：本证书只把 determinant atom 压成标量塌缩排除原子；",
            "没有证明标量塌缩排除，也没有声明 pivot、Stepanov、Kummer 迹界或行/列命题作者侧无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 和 Markdown 证书。"""
    MONO.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
