#!/usr/bin/env python3
"""推进 RKS2/RKS3 阶无关 Kummer 签名选择器的内部化边界。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_order_free_signature_selector_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-order-free-signature-selector-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-order-free-signature-selector-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-order-free-signature-selector-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-stepanov-rank-signature-router.json"
SOURCE_FILES = [PREVIOUS]

PREVIOUS_TARGET = "OrderFreeKummerSignatureSelectorAndHasseJetRankLemma"
NEW_TARGET = "ThreeVisibleBranchOrderFreeJetPivotLemma"
SUPPORT_SUBATOM = "ProjectiveResidueSupportExpansionOrJetPivotLemma"
JET_SUBATOM = "BoundedBranchSignatureHasseJetIndependenceLemma"
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


def pgl2_low_support_audit(primes: list[int]) -> list[dict[str, Any]]:
    """验证二支撑 PGL2 坐标的组合覆盖形态；证明仍以正文代数论证为准。"""
    records: list[dict[str, Any]] = []
    for prime in primes:
        a = 1 % prime
        b = 2 % prime
        images = set()
        for x in range(prime):
            if x == b:
                continue
            images.add(((x - a) * pow(x - b, -1, prime)) % prime)
        expected = set(range(prime)) - {1}
        records.append(
            {
                "prime": prime,
                "map": "(x-a)/(x-b), a=1, b=2",
                "domain_size": prime - 1,
                "image_size": len(images),
                "missing_values": sorted(expected.symmetric_difference(images)),
                "is_bijection_to_Fp_without_1": images == expected,
                "max_fiber_size": max(sum(1 for x in range(prime) if x != b and ((x - a) * pow(x - b, -1, prime)) % prime == y) for y in images),
            }
        )
    return records


def build_result() -> dict[str, Any]:
    """构造 order-free selector 前沿证书。"""
    previous = load_json(PREVIOUS)
    active = (
        previous.get("next_direct_attack_target") == PREVIOUS_TARGET
        and previous.get("order_free_signature_selector_internalized") is False
        and previous.get("branch_signature_normal_form_closed") is True
        and previous.get("hasse_jet_bookkeeping_closed") is True
    )

    projective_support_normal_form = {
        "support_definition": "work on P^1 and include infinity; visible support S={v: ord_v(f) not congruent 0 mod d}",
        "degree_zero_constraint": "sum_v ord_v(f)=0, hence a non-dth-power residue pattern cannot have exactly one projective visible branch",
        "d_power_quotient": "multiplying f by a d-th power changes no character value and removes invisible branch coordinates",
        "constant_factor": "a nonzero constant only multiplies the complete character sum by chi(c), so it is irrelevant to the rank gate",
        "scope_gain": "the selector problem only needs projective visible support size at least three",
    }

    low_support_exact_closure = {
        "support_size_0": "all residues vanish; this is a d-th power case and is excluded by the Kummer nonpower hypothesis",
        "support_size_1": "impossible on P^1 because the divisor degree is zero modulo d",
        "support_size_2": "after a PGL2 change sending the two visible branches to 0 and infinity, f=c*phi(x)^e*h(x)^d with e not congruent 0 mod d",
        "complete_sum": "on the regular affine locus the sum is a full nontrivial F_p^* character sum with at most O_m(1) PGL2 coordinate values deleted, hence O_m(1)",
        "order_free_status": "this closes the degenerate selector cases without using the y^0,...,y^{d-1} ladder and with constants independent of d",
    }

    remaining_non_degenerate_selector = {
        "old_atom": PREVIOUS_TARGET,
        "new_atom": NEW_TARGET,
        "projective_support_condition": "|S|>=3",
        "required_selector_output": "construct a bounded-pole pivot family of size >= c_m*D after Kummer relations, with c_m independent of d,P,chi and branch positions",
        "required_jet_output": "prove the Hasse-jet evaluation matrix on that pivot family loses at most C_m*T*N rank",
        "why_this_is_narrower": "all zero-, one-, and two-visible-branch residue patterns are now exact PGL2 degeneracies; only genuine three-branch interaction remains",
        "why_not_closed": "the corpus still lacks a uniform proof that three visible branch residues force an order-free pivot block for every residue pattern and every branch configuration",
    }

    rejected_shortcuts = {
        "support_count_only": "support size >=3 is necessary for the hard case but does not itself prove Hasse-jet rank independence",
        "generic_position": "the proof must allow collisions and special cross-ratios; it cannot assume branch positions are generic",
        "full_d_ladder": "using O(d) Kummer powers would reintroduce d-dependent genus/dimension and is still rejected",
        "finite_audit": "the finite PGL2 audit records the exact low-support map shape only; it is not used as empirical proof of the three-branch gate",
    }

    low_support_closed = active
    selector_reduced = active and low_support_closed
    selector_internalized = False
    rank_surjectivity_closed = selector_internalized
    stepanov_closed = rank_surjectivity_closed

    rows = [
        row(
            "PreviousSelectorTargetActive",
            active,
            active,
            "上一证书的唯一剩余确认为阶无关 Kummer 签名选择器与 Hasse-jet 秩问题。",
            PREVIOUS_TARGET,
        ),
        row(
            "ProjectiveResidueSupportNormalFormClosed",
            active,
            active,
            "把有限分支残基提升到 P^1，并用 d 次幂商掉不可见坐标。",
            "closed",
        ),
        row(
            "ProjectiveLowVisibleSupportExactPGL2Closure",
            low_support_closed,
            low_support_closed,
            "投影可见支撑小于三的退化情形由 PGL2 单坐标精确求和关闭。",
            "closed",
        ),
        row(
            "SelectorScopeRestrictedToThreeVisibleBranches",
            selector_reduced,
            selector_reduced,
            "全局 selector 原子已缩窄为三可见分支以上的非退化 jet 枢轴问题。",
            NEW_TARGET,
        ),
        row(
            NEW_TARGET,
            False,
            False,
            "仍需给出三可见分支下的阶无关 pivot 族和 Hasse-jet 独立性证明。",
            SUPPORT_SUBATOM,
        ),
        row(
            JET_SUBATOM,
            False,
            False,
            "Hasse-jet 记账接口已固定，但非退化 pivot 块的实际秩下界仍未证明。",
            SUPPORT_SUBATOM,
        ),
        row(
            PREVIOUS_TARGET,
            False,
            False,
            "低支撑退化已关闭，但完整阶无关 selector 还等待三分支 pivot 引理。",
            NEW_TARGET,
        ),
        row(
            RANK_TARGET,
            rank_surjectivity_closed,
            rank_surjectivity_closed,
            "Stepanov-Kummer 非零秩仍等待完整 selector。",
            PREVIOUS_TARGET,
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
            "秩一 Kummer 迹界仍等待 Stepanov rank gate。",
            STEPANOV_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只缩窄内部自足线，不声明行/列命题作者侧无条件闭合。",
            BURGESS_POINTWISE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_order_free_signature_selector_router",
        "status": "order_free_selector_reduced_to_three_visible_branch_jet_pivot",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "finite_audit_not_used_as_proof": True,
        "previous_selector_target_active": active,
        "projective_residue_support_normal_form_closed": active,
        "projective_low_visible_support_exact_pgl2_closure_proved": low_support_closed,
        "selector_scope_restricted_to_three_visible_branches": selector_reduced,
        "order_free_signature_selector_internalized": selector_internalized,
        "stepanov_kummer_auxiliary_rank_surjectivity_proved": rank_surjectivity_closed,
        "stepanov_auxiliary_polynomial_rank_bound_proved": stepanov_closed,
        "self_contained_kummer_trace_bound_internalized": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEW_TARGET,
        "next_subatom": SUPPORT_SUBATOM,
        "projective_support_normal_form": projective_support_normal_form,
        "low_support_exact_closure": low_support_exact_closure,
        "remaining_non_degenerate_selector": remaining_non_degenerate_selector,
        "rejected_shortcuts": rejected_shortcuts,
        "low_support_pgl2_audit": pgl2_low_support_audit([17, 29, 41, 53]),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "阶无关 Kummer 签名选择器没有整体闭合，但本轮把唯一内部自足剩余继续压窄："
            "先把分支残基放到投影直线 P^1 上，证明可见支撑小于三的退化情形不需要 Stepanov selector。"
            "支撑为零是 d 次幂而被排除；投影支撑为一与除子次数零矛盾；投影支撑为二可经 PGL2 变成 "
            "`c*phi(x)^e*h(x)^d`，仿射完整和退化为 `F_p^*` 上的非平凡角色和删去至多 `O_m(1)` 个坐标值，因而只有 `O_m(1)` "
            "边界项，常数不依赖角色阶 `d`。因此真正剩余从笼统的 "
            "`OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` 缩成 "
            "`ThreeVisibleBranchOrderFreeJetPivotLemma`：只需处理至少三处投影可见分支的非退化残基图，"
            "构造阶无关 pivot 族并证明 Hasse-jet 秩下界。未完成该三分支 pivot 引理前，"
            "Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。"
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
        "# Prime Matrix strict RKS2/RKS3 阶无关签名选择器前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_selector_target_active={fmt_bool(result['previous_selector_target_active'])}",
        f"projective_residue_support_normal_form_closed={fmt_bool(result['projective_residue_support_normal_form_closed'])}",
        f"projective_low_visible_support_exact_pgl2_closure_proved={fmt_bool(result['projective_low_visible_support_exact_pgl2_closure_proved'])}",
        f"selector_scope_restricted_to_three_visible_branches={fmt_bool(result['selector_scope_restricted_to_three_visible_branches'])}",
        f"order_free_signature_selector_internalized={fmt_bool(result['order_free_signature_selector_internalized'])}",
        f"stepanov_kummer_auxiliary_rank_surjectivity_proved={fmt_bool(result['stepanov_kummer_auxiliary_rank_surjectivity_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
    ]

    render_key_value_section(lines, "## 1. 投影支撑正规形", result["projective_support_normal_form"])
    render_key_value_section(lines, "## 2. 低支撑精确闭合", result["low_support_exact_closure"])
    render_key_value_section(lines, "## 3. 非退化剩余", result["remaining_non_degenerate_selector"])
    render_key_value_section(lines, "## 4. 禁止捷径", result["rejected_shortcuts"])

    lines.extend(
        [
            "",
            "## 5. PGL2 低支撑覆盖审计",
            "",
            "| prime | map | domain_size | image_size | missing_values | is_bijection_to_Fp_without_1 | max_fiber_size |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["low_support_pgl2_audit"]:
        lines.append(
            "| `{prime}` | {map} | `{domain_size}` | `{image_size}` | `{missing_values}` | `{is_bijection_to_Fp_without_1}` | `{max_fiber_size}` |".format(
                **{key: table_cell(value) for key, value in item.items()}
            )
        )

    lines.extend(
        [
            "",
            "## 6. 判定表",
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
            "## 7. 下一最窄目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "审稿边界：本证书只闭合投影低支撑退化情形，",
            "没有证明三可见分支的阶无关 pivot 引理；",
            "因此不声明 Stepanov、Kummer 迹界或行/列命题作者侧无条件闭合。",
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
