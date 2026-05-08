#!/usr/bin/env python3
"""Full-S KLS 与 moving-block 内部路联合硬攻路由器。

用法示例：
  python3 experiments/prime_matrix_fulls_kls_movingblock_joint_attack_router.py

输出：
  docs/monograph/prime-matrix-fulls-kls-movingblock-joint-attack-router.json
  docs/monograph/prime-matrix-fulls-kls-movingblock-joint-attack-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_REFINED = DOCS / "prime-matrix-irreducible-math-input-refinement-router.json"
DEFAULT_NONCANONICAL = DOCS / "prime-matrix-noncanonical-final-narrowing-router.json"
DEFAULT_SOURCE_ENTROPY = (
    DOCS / "prime-matrix-triad-a1-dibfi-exact-full-s-source-entropy-reduction-router.json"
)
DEFAULT_EXACT_SUPPORT = DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
DEFAULT_CANONICAL_LAYER = DOCS / "prime-matrix-pdec-cap-canonical-layer-closure-router.json"
DEFAULT_NEW_FULL_S = DOCS / "prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json"
DEFAULT_PRIMARY_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.json"
)
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-fulls-kls-movingblock-joint-attack-router.json"
DEFAULT_MD = DOCS / "prime-matrix-fulls-kls-movingblock-joint-attack-router.md"


EXTERNAL_PRIMARY_SOURCES = [
    {
        "label": "BFI-II",
        "title": "Bombieri-Friedlander-Iwaniec, Primes in Arithmetic Progressions to Large Moduli. II",
        "url": "https://eudml.org/doc/164255",
        "usable_fact": "well-factorable AP discrepancy / dispersion method source class",
        "mismatch": "AP discrepancy target; current branch is full-S non-AP uncentered no-projection WFD",
    },
    {
        "label": "DI-Kloosterman",
        "title": "Deshouillers-Iwaniec, Kloosterman Sums and Fourier Coefficients of Cusp Forms",
        "url": "https://eudml.org/doc/142975",
        "usable_fact": "spectral/Kuznetsov Kloosterman mean-value technology",
        "mismatch": "technology backbone, not a ready-made theorem for the current c-dependent WFD weights",
    },
    {
        "label": "Maynard-II",
        "title": "Maynard, Primes in arithmetic progressions to large moduli II: Well-factorable estimates",
        "url": "https://arxiv.org/abs/2006.07088",
        "usable_fact": "well/triply factorable AP mean-value theorem, with moduli beyond square-root ranges",
        "mismatch": "AP fixed-residue theorem; does not by itself supply the non-AP no-projection WFD KLS atom",
    },
    {
        "label": "Maynard-I",
        "title": "Maynard, Primes in arithmetic progressions to large moduli I: Fixed residue classes",
        "url": "https://arxiv.org/abs/2006.06572",
        "usable_fact": "fixed residue AP framework using Kuznetsov/Weil/Deligne-type estimates",
        "mismatch": "fixed-residue AP framework, not the current completed c-dependent residue-weight object",
    },
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写字符串。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_rows(
    refined: dict[str, Any],
    noncanonical: dict[str, Any],
    source_entropy: dict[str, Any],
    exact_support: dict[str, Any],
    canonical_layer: dict[str, Any],
    new_full_s: dict[str, Any],
    primary_nogo: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成联合硬攻判定行。"""
    return [
        {
            "gate": "RefinedTwoLaneInputPinned",
            "closed": refined.get("refinement_boundary_closed") is True
            and refined.get("refined_math_input")
            == (
                "MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients "
                "OR FullSNonAPWFDKLSTheoremInput"
            ),
            "blocks_final": True,
            "meaning": "上一轮已经把数学二路压成 moving-block 内部路或 Full-S KLS 外部/新定理路。",
            "remaining": "继续判断二路是否能由当前材料或现有主来源推出。",
        },
        {
            "gate": "CanonicalBranchRemovedFromNoncanonicalDuty",
            "closed": noncanonical.get("noncanonical_narrowing_boundary_closed") is True
            and canonical_layer.get("self_contained_canonical_branch_closed") is True,
            "blocks_final": False,
            "meaning": "canonical RIW/Buchstab 分支已闭合并移出；不能把它偷渡到 noncanonical full-S 补集。",
            "remaining": "只审查 actual noncanonical source 或外部 Full-S KLS。",
        },
        {
            "gate": "InternalMovingBlockReducedToExactSupportPackage",
            "closed": source_entropy.get("terminal_gap_after_router")
            == "FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov",
            "blocks_final": True,
            "meaning": "内部 moving-block/SourceEntropy 路已降成精确因子支撑、balanced range 和 Type/Fourier 容量兼容包。",
            "remaining": "证明 actual noncanonical full-S 因子支撑包，或转外部定理。",
        },
        {
            "gate": "ExactSupportNotDerivableFromK4K6",
            "closed": exact_support.get("k4_k6_imply_exact_factor_support") is False
            and exact_support.get("terminal_gap_after_router")
            == "FactorResidueIncidenceBridgeOrCanonicalRIWFactorSupportOrExternalDIBFIOriginalDispersion",
            "blocks_final": True,
            "meaning": "K4 residue flatness 与 K6 dyadic bookkeeping 不能自动推出 moving factor-pair 支撑。",
            "remaining": "需要 factor-residue incidence 桥，或直接证明 exact factor support；canonical 支撑只服务 canonical 分支。",
        },
        {
            "gate": "ExternalFullSKLSAtomPinnedButNotMatched",
            "closed": new_full_s.get("terminal_gap_after_router") == "FullSNonAPWFDKLSTheoremInput"
            and primary_nogo.get("terminal_gap_after_router") == "NewFullSTheoremInputOrAPSourceLift",
            "blocks_final": True,
            "meaning": "外部路已精确成 FullSNonAPWFDKLSTheoremInput；现有 DI/BFI 主来源逐项推出该对象的路线被阻断。",
            "remaining": "新增证明或明确引用直接覆盖当前对象的 full-S KLS/dispersion 定理。",
        },
        {
            "gate": "ExternalSourceClassUsefulButInsufficient",
            "closed": True,
            "blocks_final": True,
            "meaning": "BFI/DI/Maynard 提供可用谱与 dispersion 技术来源，但对象仍是 AP 或一般 Kloosterman 技术类。",
            "remaining": "必须补变量同一化：c-dependent residue weights、未中心化、无投影、full-S、non-AP、任意对数节省。",
        },
        {
            "gate": "DStructureRankinPromotionStillSeparate",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "blocks_final": True,
            "meaning": "即使数学二选一路闭合，完整行/列定理还需 DStructure/Tail-log4/finite Rankin 独立验收。",
            "remaining": "提交正式全集 Rankin 证书与独立接受。",
        },
    ]


def run(
    refined_path: Path,
    noncanonical_path: Path,
    source_entropy_path: Path,
    exact_support_path: Path,
    canonical_layer_path: Path,
    new_full_s_path: Path,
    primary_nogo_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行二路联合硬攻。"""
    source_paths = [
        refined_path,
        noncanonical_path,
        source_entropy_path,
        exact_support_path,
        canonical_layer_path,
        new_full_s_path,
        primary_nogo_path,
        dstructure_path,
    ]
    refined = load_json(refined_path)
    noncanonical = load_json(noncanonical_path)
    source_entropy = load_json(source_entropy_path)
    exact_support = load_json(exact_support_path)
    canonical_layer = load_json(canonical_layer_path)
    new_full_s = load_json(new_full_s_path)
    primary_nogo = load_json(primary_nogo_path)
    dstructure = load_json(dstructure_path)

    rows = build_rows(
        refined=refined,
        noncanonical=noncanonical,
        source_entropy=source_entropy,
        exact_support=exact_support,
        canonical_layer=canonical_layer,
        new_full_s=new_full_s,
        primary_nogo=primary_nogo,
        dstructure=dstructure,
    )
    joint_attack_boundary_closed = all(row["closed"] for row in rows)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_fulls_kls_movingblock_joint_attack_router",
        "status": "fulls_kls_movingblock_joint_attack_reduced_to_exact_support_or_new_fulls_kls_open",
        "joint_attack_boundary_closed": joint_attack_boundary_closed,
        "internal_lane_proved_in_current_corpus": False,
        "external_lane_proved_or_cited_in_current_corpus": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "narrowest_internal_hardpoint": (
            "FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource"
        ),
        "narrowest_external_hardpoint": "FullSNonAPWFDKLSTheoremInput",
        "narrowest_math_hardpoint": (
            "FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource "
            "OR FullSNonAPWFDKLSTheoremInput"
        ),
        "final_promotion_hardpoint": (
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "full_closure_basis_after_joint_attack": (
            "(FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource OR "
            "FullSNonAPWFDKLSTheoremInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "internal_required_subatoms": [
            "FullSNonAPExactFactorSupportLowerBound",
            "FullSNonAPBalancedRangeThreshold",
            "FullSNonAPTypeFourierCapacityCompatibility",
            "FactorResidueIncidenceBridgeOrDirectExactSupport",
            "NoCanonicalBranchImportIntoNoncanonicalComplement",
        ],
        "external_required_clauses": [
            "current non-AP uncentered no-projection WFD window",
            "X≈P^2, C≈P/log^O(P), S≈P, 0<|h|<=P/log^O(P)",
            "c-dependent completed residue weights B_{c,x}",
            "well-factorable lambda and divisor-bounded beta/omega",
            "NaturalWFDScale/log^A(P) saving for every A>0",
            "dyadic/gcd/smoothing endpoint losses absorbed into B(A)",
        ],
        "external_primary_sources": EXTERNAL_PRIMARY_SOURCES,
        "plain_conclusion": (
            "本轮联合硬攻没有找到可诚实升级为无条件闭合的现有输入。内部路继续降到 actual "
            "noncanonical full-S 的精确因子支撑包；外部路继续降到必须新增或明确引用的 "
            "FullSNonAPWFDKLSTheoremInput。canonical 分支已闭合但不能再用于 noncanonical 补集；"
            "DStructure/Rankin 晋级门仍独立开放。"
        ),
        "rows": rows,
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths
        },
    }

    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 报告。"""
    lines: list[str] = [
        "# Prime Matrix Full-S KLS / Moving-Block 联合硬攻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"joint_attack_boundary_closed={fmt_bool(result['joint_attack_boundary_closed'])}",
        f"internal_lane_proved_in_current_corpus={fmt_bool(result['internal_lane_proved_in_current_corpus'])}",
        f"external_lane_proved_or_cited_in_current_corpus={fmt_bool(result['external_lane_proved_or_cited_in_current_corpus'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 联合硬攻判定表",
        "",
        "| gate | closed | blocks_final | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                blocks=fmt_bool(row["blocks_final"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 最新最窄输入基",
            "",
            "```text",
            result["full_closure_basis_after_joint_attack"],
            "```",
            "",
            "## 3. 内部路剩余子原子",
            "",
        ]
    )
    for atom in result["internal_required_subatoms"]:
        lines.append(f"- `{atom}`")

    lines.extend(
        [
            "",
            "## 4. 外部 Full-S KLS 输入条款",
            "",
        ]
    )
    for clause in result["external_required_clauses"]:
        lines.append(f"- {clause}")

    lines.extend(
        [
            "",
            "## 5. 外部主来源审查",
            "",
            "| source | useful fact | current mismatch | link |",
            "| --- | --- | --- | --- |",
        ]
    )
    for source in result["external_primary_sources"]:
        lines.append(
            "| `{label}` | {fact} | {mismatch} | {url} |".format(
                label=table_cell(source["label"]),
                fact=table_cell(source["usable_fact"]),
                mismatch=table_cell(source["mismatch"]),
                url=table_cell(source["url"]),
            )
        )

    lines.extend(
        [
            "",
            "## 6. 当前结论",
            "",
            "这一步继续压缩了命题边界：下一步不能再泛称“攻 KLS 或 NC-BLK”，而应精确攻下面二选一：",
            "",
            "```text",
            result["narrowest_math_hardpoint"],
            "```",
            "",
            "其中内部路是组合/支撑定理，外部路是新谱/dispersion 定理。二者至少一支成立后，仍需独立完成 DStructure/Rankin 晋级验收。",
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refined", type=Path, default=DEFAULT_REFINED)
    parser.add_argument("--noncanonical", type=Path, default=DEFAULT_NONCANONICAL)
    parser.add_argument("--source-entropy", type=Path, default=DEFAULT_SOURCE_ENTROPY)
    parser.add_argument("--exact-support", type=Path, default=DEFAULT_EXACT_SUPPORT)
    parser.add_argument("--canonical-layer", type=Path, default=DEFAULT_CANONICAL_LAYER)
    parser.add_argument("--new-full-s", type=Path, default=DEFAULT_NEW_FULL_S)
    parser.add_argument("--primary-nogo", type=Path, default=DEFAULT_PRIMARY_NOGO)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        refined_path=args.refined,
        noncanonical_path=args.noncanonical,
        source_entropy_path=args.source_entropy,
        exact_support_path=args.exact_support,
        canonical_layer_path=args.canonical_layer,
        new_full_s_path=args.new_full_s,
        primary_nogo_path=args.primary_nogo,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["full_closure_basis_after_joint_attack"])


if __name__ == "__main__":
    main()
