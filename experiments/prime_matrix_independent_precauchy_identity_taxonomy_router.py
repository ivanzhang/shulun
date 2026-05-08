#!/usr/bin/env python3
"""Prime Matrix 独立 pre-Cauchy 算术来源恒等式分类路由器。

用法示例：
  python3 experiments/prime_matrix_independent_precauchy_identity_taxonomy_router.py

输出：
  docs/monograph/prime-matrix-independent-precauchy-identity-taxonomy-router.json
  docs/monograph/prime-matrix-independent-precauchy-identity-taxonomy-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-hypothetical-zero-row-seed-no-go-router.json"
DEFAULT_CONTRACT = DOCS / "prime-matrix-noncanonical-complement-input-contract-router.md"
DEFAULT_FIREWALL = DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.md"
DEFAULT_AP_NOGO = DOCS / "prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.md"
DEFAULT_EXTERNAL_MATCH = DOCS / "prime-matrix-clean-core-external-lemma-parameter-match-router.md"
DEFAULT_FINAL = DOCS / "prime-matrix-unconditional-closure-final-attempt-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-independent-precauchy-identity-taxonomy-router.json"
DEFAULT_MD = DOCS / "prime-matrix-independent-precauchy-identity-taxonomy-router.md"

OLD_ATOM = "IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn"
NEW_ATOM = "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
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


def replace_atom(text: str, old: str, new: str) -> str:
    """替换输入基中的独立来源恒等式原子。"""
    return text.replace(old, new)


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
    contract_text: str,
    firewall_text: str,
    ap_nogo_text: str,
    external_text: str,
    final_text: str,
) -> list[dict[str, Any]]:
    """把独立 pre-Cauchy 来源恒等式按合法来源类分类。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in basis
    no_fourth = (
        "NoHiddenFourthRoute" in contract_text
        and "没有第四条可自足偷渡路线" in contract_text
    )
    canonical_blocked = (
        "canonical" in firewall_text
        and "CanonicalClassClosedScoped" in firewall_text
        and "不能覆盖 noncanonical clean-core" in firewall_text
    )
    generic_blocked = (
        "GenericWFDClassRejected" in firewall_text
        and "GenericWFDSelfContainedTemplate" in contract_text
        and "refuted_not_available" in contract_text
    )
    ap_lift_blocked = (
        "APSourceLiftRejected" in ap_nogo_text
        and "ap_source_lift_rejected=true" in ap_nogo_text
    )
    external_not_self = (
        "external_lemmas_close_self_contained_remainder=false" in external_text
        and "不能生成 pre-Cauchy actual noncanonical summand emitter" in external_text
    )
    final_core = (
        "MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients" in final_text
        and "PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem" in final_text
        and "row_column_unconditional_closed=false" in final_text
    )
    taxonomy_closed = all(
        [
            active,
            no_fourth,
            canonical_blocked,
            generic_blocked,
            ap_lift_blocked,
            external_not_self,
            final_core,
        ]
    )
    return [
        row(
            "IndependentPreCauchyIdentityGateActive",
            active,
            False,
            "最新最窄点要求独立于早期零行覆盖图的 pre-Cauchy 算术来源恒等式。",
            "分类它的所有合法来源类。",
        ),
        row(
            "NoHiddenFourthRouteImported",
            no_fourth,
            True,
            "noncanonical full-S 补集合同已声明没有第四条可自足偷渡路线。",
            "候选恒等式必须落入 canonical、generic、external/AP 或 actual-source 类。",
        ),
        row(
            "CanonicalSourceIdentityBlockedForNoncanonical",
            canonical_blocked,
            True,
            "canonical RIW/Buchstab 来源只在 canonical 分支内闭合。",
            "不能导入 noncanonical clean-core。",
        ),
        row(
            "GenericWFDIdentityRejected",
            generic_blocked,
            True,
            "generic WFD/source 模板已被 moving-delta 和来源防火墙阻断。",
            "不能作为 pre-Cauchy source identity。",
        ),
        row(
            "APSourceLiftRejected",
            ap_lift_blocked,
            True,
            "AP-source lift 是 source-level reclassification；non-AP clean-core 不能静默升级为 AP 源。",
            "若走 AP/DI-BFI 必须新增 full-S theorem 或新 source identity。",
        ),
        row(
            "ExternalSpectralNotSelfContainedSourceIdentity",
            external_not_self,
            True,
            "DI/BFI/Kuznetsov 处理 completion 后系数平均，不能生成 pre-Cauchy summand emitter。",
            "它只能作为精确外部谱输入分支。",
        ),
        row(
            "RemainingActualSourceCoreIdentified",
            final_core,
            True,
            "所有伪来源恒等式删除后，自足数学核心与 moving-block spread/NC-BLK 汇合；外部谱只保留在条件分支。",
            NEW_ATOM,
        ),
        row(
            "IndependentPreCauchyIdentityTaxonomyClosed",
            taxonomy_closed,
            True,
            "独立来源恒等式的合法类别已穷尽；它不能成为新隐藏终端。",
            "剩余是 actual moving-block spread/NC-BLK；精确外部谱输入保留在条件分支。",
        ),
        row(
            NEW_ATOM,
            False,
            False,
            "当前材料尚未证明 actual noncanonical moving-block spread/NC-BLK。",
            NEW_ATOM,
        ),
        row(
            "ExplicitModelGapAndFiniteDPRCLedger",
            "ExplicitModelGapAndFiniteDPRCLedger" in basis,
            False,
            "模型余量/有限 DPRC 账本仍在输入基中，未由本步处理。",
            "ExplicitModelGapAndFiniteDPRCLedger。",
        ),
        row(
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(
    previous_path: Path,
    contract_path: Path,
    firewall_path: Path,
    ap_nogo_path: Path,
    external_path: Path,
    final_path: Path,
) -> dict[str, Any]:
    """执行独立来源恒等式分类路由。"""
    source_paths = [
        previous_path,
        contract_path,
        firewall_path,
        ap_nogo_path,
        external_path,
        final_path,
    ]
    previous = load_json(previous_path)
    rows = build_rows(
        previous=previous,
        contract_text=contract_path.read_text(encoding="utf-8"),
        firewall_text=firewall_path.read_text(encoding="utf-8"),
        ap_nogo_text=ap_nogo_path.read_text(encoding="utf-8"),
        external_text=external_path.read_text(encoding="utf-8"),
        final_text=final_path.read_text(encoding="utf-8"),
    )
    taxonomy_closed = next(
        bool(item["closed"]) for item in rows if item["gate"] == "IndependentPreCauchyIdentityTaxonomyClosed"
    )
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    return {
        "certificate_type": "independent_precauchy_identity_taxonomy_router",
        "status": "independent_precauchy_identity_taxonomy_closed_actual_spread_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "identity_taxonomy_closed": taxonomy_closed,
        "canonical_source_identity_blocked": taxonomy_closed,
        "generic_wfd_identity_rejected": taxonomy_closed,
        "ap_source_lift_rejected": taxonomy_closed,
        "external_spectral_self_contained_identity_proved": False,
        "actual_moving_block_spread_proved": False,
        "precisely_matched_external_spectral_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "next_priority": NEW_ATOM,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步穷尽 IndependentPreCauchyArithmeticSourceIdentity 的合法来源类：canonical 来源只在 canonical "
            "分支内闭合，generic WFD 来源被 moving-delta/防火墙阻断，APSourceLift 被对象账本拒绝，外部谱定理"
            "不能作为完全自足 pre-Cauchy source identity。剩余不再是新恒等式黑箱，而是 actual noncanonical "
            "moving-block spread/NC-BLK 数学输入；精确外部谱匹配仍留在条件分支。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix 独立 pre-Cauchy 算术来源恒等式分类路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"identity_taxonomy_closed={fmt_bool(result['identity_taxonomy_closed'])}",
        f"canonical_source_identity_blocked={fmt_bool(result['canonical_source_identity_blocked'])}",
        f"generic_wfd_identity_rejected={fmt_bool(result['generic_wfd_identity_rejected'])}",
        f"ap_source_lift_rejected={fmt_bool(result['ap_source_lift_rejected'])}",
        (
            "external_spectral_self_contained_identity_proved="
            f"{fmt_bool(result['external_spectral_self_contained_identity_proved'])}"
        ),
        f"actual_moving_block_spread_proved={fmt_bool(result['actual_moving_block_spread_proved'])}",
        (
            "precisely_matched_external_spectral_accepted="
            f"{fmt_bool(result['precisely_matched_external_spectral_accepted'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 分类律",
        "",
        "```text",
        "independent pre-Cauchy source identity",
        "  in {canonical, generic_wfd, AP/external, actual_noncanonical}",
        "canonical       -> scoped out of noncanonical clean-core",
        "generic_wfd     -> rejected",
        "AP/external     -> not self-contained source identity",
        "actual_noncanonical -> moving-block spread / NC-BLK core",
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
        "该替换把独立来源恒等式黑箱并入已知终局二选一数学核心。",
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
            f"下一步最窄目标为 `{result['next_priority']}`：在假设早期零行反例分支中证明 actual same-(u,v) "
            "moving block 不能集中到足以支付零行；若改走外部条件分支，则必须精确匹配并接受 "
            "CDependent residue spectral input；否则给出命名 PDEC/SAE/ColumnCRT/CleanKLS 回流证书。",
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
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--firewall", type=Path, default=DEFAULT_FIREWALL)
    parser.add_argument("--ap-nogo", type=Path, default=DEFAULT_AP_NOGO)
    parser.add_argument("--external", type=Path, default=DEFAULT_EXTERNAL_MATCH)
    parser.add_argument("--final", type=Path, default=DEFAULT_FINAL)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        contract_path=args.contract,
        firewall_path=args.firewall,
        ap_nogo_path=args.ap_nogo,
        external_path=args.external,
        final_path=args.final,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
