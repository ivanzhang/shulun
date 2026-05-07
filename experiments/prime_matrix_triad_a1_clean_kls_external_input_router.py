#!/usr/bin/env python3
"""登记 A1 clean KLS/DLS 分支的外部 KLS 输入与自足版剩余原子。

用法示例：
  python3 experiments/prime_matrix_triad_a1_clean_kls_external_input_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-clean-kls-external-input-router.json
  docs/monograph/prime-matrix-triad-a1-clean-kls-external-input-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_TERMINAL_DICHOTOMY = (
    DOCS / "prime-matrix-triad-a1-continuous-terminal-dichotomy-router.json"
)
DEFAULT_ACTUAL_PAYMENT = (
    DOCS / "prime-matrix-triad-a1-continuous-actual-payment-selection.json"
)
DEFAULT_COLUMNTAIL_BRIDGE = (
    DOCS / "prime-matrix-triad-a1-continuous-columntail-bridge.json"
)
DEFAULT_PDEC_MASS = DOCS / "prime-matrix-triad-a1-pdec-mass-source-router.json"
DEFAULT_NODELETION_TERMINAL = (
    DOCS / "prime-matrix-triad-a1-continuous-nodeletion-terminal-router.json"
)
DEFAULT_SMALL_AMBIGUOUS = (
    DOCS / "prime-matrix-triad-a1-small-ambiguous-clean-admission-router.json"
)
DEFAULT_CLEAN_CONTRACT = DOCS / "prime-matrix-cleankls-dls-certificate-contract.md"
DEFAULT_HLC_EXTERNAL = DOCS / "prime-matrix-h3-dsb-hlc-kls-external-adaptation.md"
DEFAULT_HLC_CORE = DOCS / "prime-matrix-h3-dsb-hlc-kls-core-reduction.md"
DEFAULT_HLC_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kls-core-self-contained-spine.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-clean-kls-external-input-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-clean-kls-external-input-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def build_variable_map() -> list[dict[str, str]]:
    """给出 A1 clean residual 到 Kloosterman/dispersion 输入的变量适配表。"""
    return [
        {
            "a1_object": "Omega",
            "meaning": "同一 continuous actual-payment clean residual formal unit",
            "kls_object": "一个 clean dyadic/Type block 的 formal unit B",
            "status": "formal_unit_registered",
        },
        {
            "a1_object": "ell",
            "meaning": "支付尾素数或升层 promoted prime 的单位变量",
            "kls_object": "Kloosterman 可逆变量 x 或 prime-variable block",
            "status": "inverse_variable_ready",
        },
        {
            "a1_object": "m",
            "meaning": "互补因子，满足 Py-d=ell*m 的 completion 变量",
            "kls_object": "线性相位/Poisson 后的 m-block",
            "status": "linear_variable_ready",
        },
        {
            "a1_object": "d",
            "meaning": "列位移或 completion displacement",
            "kls_object": "频率/模数标签中的 residue datum",
            "status": "column_displacement_routed_or_clean",
        },
        {
            "a1_object": "R",
            "meaning": "低模 CRT、gcd/unit 剥离后的有效模数或 lcm 层",
            "kls_object": "Kloosterman 模数/dispersion level",
            "status": "external_level_template_registered",
        },
        {
            "a1_object": "h",
            "meaning": "非零 Fourier/Bohr 频率",
            "kls_object": "Kuznetsov/Bessel 频率参数",
            "status": "frequency_template_registered",
        },
        {
            "a1_object": "W(m,ell)",
            "meaning": "行窗口、尾标签与 dyadic 平滑权重",
            "kls_object": "smooth compact window with polylog derivative loss",
            "status": "smooth_partition_registered",
        },
        {
            "a1_object": "a_ell,b_m,gamma",
            "meaning": "diffuse payment residual 产生的 L2-flat 系数",
            "kls_object": "spectral large-sieve coefficient vectors",
            "status": "l2_flat_coefficients_ready_on_clean_branch",
        },
    ]


def build_admission_rows(
    terminal_dichotomy: dict[str, Any],
    actual_payment: dict[str, Any],
    columntail_bridge: dict[str, Any],
    pdec_mass: dict[str, Any],
    nodeletion_terminal: dict[str, Any],
    small_ambiguous: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造 K1--K9 准入核查表。"""
    diffuse_l2_ready = (
        "diffuse branch supplies L2-flat admission language"
        in terminal_dichotomy["closed_subclaims"]
    )
    payment_ready = bool(
        actual_payment["all_payment_counts_match_demand"]
        and columntail_bridge["all_cap_recomputations_match"]
    )
    pxp_exits_closed = bool(pdec_mass["all_current_dualcap_pxp_exits_closed"])
    nodeletion_ready = bool(nodeletion_terminal["no_independent_nodeletion_gap"])
    gates = nodeletion_terminal["nodeletion_gates"]
    small_ready = bool(small_ambiguous["all_current_small_ambiguous_routed"])

    return [
        {
            "key": "K1",
            "condition": "dyadic ranges for m, ell, d, R and h",
            "a1_source": "A1 clean residual is decomposed into dyadic formal units before KLS invocation",
            "status": "ExternalTemplateRegistered",
            "failure_route": "range/high-lcm failure returns to PDEC/SAE/gcd-stratum ledger",
            "verified": True,
        },
        {
            "key": "K2",
            "condition": "lowmod orthogonality; no fixed low residue atom persists",
            "a1_source": "finite-projection dichotomy: positive-limsup finite signature returns to PDEC; diffuse branch has all fixed atoms vanish",
            "status": "RoutedToPDECOrSatisfiedOnDiffuseBranch",
            "failure_route": "positive finite lowmod signature -> column-tail/refined PDEC",
            "verified": diffuse_l2_ready,
        },
        {
            "key": "K3",
            "condition": "no short-window cap or early P x P local survivor gap",
            "a1_source": "current P x P exits are closed by mass-source/LFTE routing; future short-window failure is a named LocalSurvivor/SAE/PDEC exit",
            "status": "CurrentExitsClosedFailureNamed",
            "failure_route": "short-window cap -> LocalSurvivor/SAE/refined PDEC",
            "verified": pxp_exits_closed,
        },
        {
            "key": "K4",
            "condition": "no column/tail displacement cap persists",
            "a1_source": "continuous column-tail bridge and actual-payment dichotomy: persistent column-tail signature returns to PDEC",
            "status": "RoutedToPDECOrCleanDiffuse",
            "failure_route": "column/tail displacement atom -> PDEC/ColumnCRT",
            "verified": payment_ready,
        },
        {
            "key": "K5",
            "condition": "coefficient L2-flat on all fixed finite projections",
            "a1_source": "diffuse terminal branch supplies max-atom and L2-flat admission language",
            "status": "L2FlatOnCleanBranch",
            "failure_route": "large coefficient atom -> finite signature PDEC/SAE",
            "verified": diffuse_l2_ready,
        },
        {
            "key": "K6",
            "condition": "gcd/unit strata and dyadic splitting are polylog-accounted",
            "a1_source": "external HLC-KLS template supplies the admissible unit/gcd bookkeeping; failure is not clean",
            "status": "ExternalTemplateRegistered",
            "failure_route": "gcd/unit overrun -> gcd-stratum PDEC or finite exception",
            "verified": True,
        },
        {
            "key": "K7",
            "condition": "same formal unit as PDEC/SAE/payment ledgers",
            "a1_source": "canonical actual payment measure and column-tail bridge share the same formal payment unit",
            "status": "FormalUnitVerified",
            "failure_route": "口径不一致 -> Multiplicity/Stitching absorption",
            "verified": payment_ready,
        },
        {
            "key": "K8",
            "condition": "no promotable top-prime or fixed promoted residue remains",
            "a1_source": "prime-lift deletion potential and NoDeletion terminal router exhaust promotable fixed residues",
            "status": "PromotionDeletedOrNoDeletionRouted",
            "failure_route": "promotable residue -> prime-lift deletion/PDEC/NoDeletion router",
            "verified": nodeletion_ready,
        },
        {
            "key": "K9",
            "condition": "no persistent phase-residue mutual information",
            "a1_source": "KL chain identity exact; persistent KL/MI returns to refined PDEC, flat KL/MI is the clean branch",
            "status": "MutualInformationRoutedOrFlat",
            "failure_route": "I(T;B) or KL(B||U_B) persists -> refined/new-layer PDEC",
            "verified": bool(
                nodeletion_ready
                and gates["kl_chain_identity_exact"]
                and gates["all_kl_shapes_named_pdec_or_clean"]
                and small_ready
            ),
        },
    ]


def build_external_reduction_rows() -> list[dict[str, str]]:
    """给出外部 KLS 版和自足版的剩余层级。"""
    return [
        {
            "stage": "A1-CleanKLS admission",
            "input": "K1--K9 all verified or failures routed",
            "output": "clean A1 dyadic formal unit",
            "status": "materialized_by_this_router",
        },
        {
            "stage": "A1 clean unit -> Kloosterman window",
            "input": "m, ell, d, R, h, smooth W and L2-flat coefficients",
            "output": "standard inverse-phase Kloosterman/dispersion block",
            "status": "external_template_registered",
        },
        {
            "stage": "External DI/BFI/Kuznetsov input",
            "input": "windowed Kloosterman spectral/dispersion large sieve",
            "output": "O(q/log^2 y) clean residual bound",
            "status": "closed_if_external_deep_theorem_is_accepted",
        },
        {
            "stage": "Self-contained version",
            "input": "do not cite external DI/BFI/Kuznetsov",
            "output": "prove Kuznetsov-LS atom (SC-9)",
            "status": "self_contained_atom_open",
        },
    ]


def run(
    terminal_dichotomy_path: Path,
    actual_payment_path: Path,
    columntail_bridge_path: Path,
    pdec_mass_path: Path,
    nodeletion_terminal_path: Path,
    small_ambiguous_path: Path,
    clean_contract_path: Path,
    hlc_external_path: Path,
    hlc_core_path: Path,
    hlc_spine_path: Path,
) -> dict[str, Any]:
    """运行 A1 clean KLS 外部输入路由。"""
    terminal_dichotomy = load_json(terminal_dichotomy_path)
    actual_payment = load_json(actual_payment_path)
    columntail_bridge = load_json(columntail_bridge_path)
    pdec_mass = load_json(pdec_mass_path)
    nodeletion_terminal = load_json(nodeletion_terminal_path)
    small_ambiguous = load_json(small_ambiguous_path)
    admission_rows = build_admission_rows(
        terminal_dichotomy,
        actual_payment,
        columntail_bridge,
        pdec_mass,
        nodeletion_terminal,
        small_ambiguous,
    )
    all_admission_verified_or_routed = all(row["verified"] for row in admission_rows)
    external_kls_input_registered = bool(all_admission_verified_or_routed)
    return {
        "certificate_type": "triad_a1_clean_kls_external_input_router",
        "status": "a1_clean_kls_external_input_registered_self_contained_atom_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "terminal_dichotomy_json": file_sha256(terminal_dichotomy_path),
            "actual_payment_json": file_sha256(actual_payment_path),
            "columntail_bridge_json": file_sha256(columntail_bridge_path),
            "pdec_mass_json": file_sha256(pdec_mass_path),
            "nodeletion_terminal_json": file_sha256(nodeletion_terminal_path),
            "small_ambiguous_json": file_sha256(small_ambiguous_path),
            "clean_contract_md": file_sha256(clean_contract_path),
            "hlc_external_adaptation_md": file_sha256(hlc_external_path),
            "hlc_core_reduction_md": file_sha256(hlc_core_path),
            "hlc_self_contained_spine_md": file_sha256(hlc_spine_path),
        },
        "admission_rows": admission_rows,
        "all_admission_verified_or_routed": all_admission_verified_or_routed,
        "external_variable_map": build_variable_map(),
        "external_reduction_rows": build_external_reduction_rows(),
        "external_kls_input_registered": external_kls_input_registered,
        "external_deep_theorem_version_status": (
            "closed_for_a1_clean_branch_if_windowed_kloosterman_spectral_dispersion_input_is_accepted"
        ),
        "self_contained_version_status": "open_at_kuznetsov_ls_atom_sc9",
        "terminal_gap_after_router": "KuznetsovLSAtomSC9OrExternalCitation",
        "current_numeric_context": {
            "terminal_route_counts": terminal_dichotomy["route_counts"],
            "global_max_actual_signature_share": terminal_dichotomy[
                "global_max_actual_signature_share"
            ],
            "global_min_inverse_l2_signature_support": terminal_dichotomy[
                "global_min_inverse_l2_signature_support"
            ],
            "current_nodeletion_triggered": nodeletion_terminal["nodeletion_gates"][
                "current_nodeletion_triggered"
            ],
            "nodeletion_shape_route_counts": nodeletion_terminal["nodeletion_gates"][
                "shape_route_counts"
            ],
        },
        "structural_law": (
            "A1 clean branch is invoked only after all finite signatures, column/tail caps, "
            "promotable prime residues, and phase-residue mutual-information peaks have been "
            "routed away. Under those K1--K9 admission conditions the residual is a dyadic "
            "L2-flat Kloosterman/dispersion formal unit. If a windowed DI/BFI/Kuznetsov "
            "large-sieve input is accepted, the clean branch is absorbed. Without external "
            "input, the remaining self-contained task is exactly the Kuznetsov-LS atom (SC-9)."
        ),
        "review_conclusion": (
            "A1 的 CleanKLS/DLS 口已经从泛泛的大筛缺口压成外部输入登记表："
            "K1--K9 的失败项都回流到 PDEC/SAE/Multiplicity/Promotion，全部通过时才调用 "
            "Kloosterman/dispersion 大筛。外部深定理版可在接受窗口化 DI/BFI/Kuznetsov 输入时闭合；"
            "完全自足版仍卡在单一 Kuznetsov-LS atom (SC-9)。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 CleanKLS 外部输入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "A1 clean residual",
        "  => K1--K9 admission;",
        "admission failure",
        "  => PDEC / SAE / Multiplicity / Promotion return;",
        "all K1--K9 pass",
        "  => L2-flat Kloosterman/dispersion block;",
        "external DI/BFI/Kuznetsov accepted",
        "  => A1 clean branch absorbed;",
        "self-contained version",
        "  => prove Kuznetsov-LS atom (SC-9).",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `all_admission_verified_or_routed={fmt_bool(result['all_admission_verified_or_routed'])}`。",
        f"- `external_kls_input_registered={fmt_bool(result['external_kls_input_registered'])}`。",
        f"- `external_deep_theorem_version_status={result['external_deep_theorem_version_status']}`。",
        f"- `self_contained_version_status={result['self_contained_version_status']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        f"- `current_numeric_context={result['current_numeric_context']}`。",
        "",
        "## 3. K1--K9 准入表",
        "",
        "| key | condition | status | verified | failure route |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["admission_rows"]:
        lines.append(
            "| `{key}` | {condition} | `{status}` | `{verified}` | {failure_route} |".format(
                key=row["key"],
                condition=row["condition"],
                status=row["status"],
                verified=fmt_bool(bool(row["verified"])),
                failure_route=row["failure_route"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 变量适配表",
            "",
            "| A1 object | meaning | KLS object | status |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["external_variable_map"]:
        lines.append(
            "| `{a1}` | {meaning} | {kls} | `{status}` |".format(
                a1=row["a1_object"],
                meaning=row["meaning"],
                kls=row["kls_object"],
                status=row["status"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 外部输入与自足边界",
            "",
            "| stage | input | output | status |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["external_reduction_rows"]:
        lines.append(
            "| {stage} | {input} | {output} | `{status}` |".format(
                stage=row["stage"],
                input=row["input"],
                output=row["output"],
                status=row["status"],
            )
        )

    lines.extend(
        [
            "",
            "## 6. 当前结论",
            "",
            "A1 clean 分支现在有明确审稿边界：",
            "",
            "```text",
            "外部深定理版：接受窗口化 DI/BFI/Kuznetsov 大筛输入，则 A1 clean branch 吸收；",
            "完全自足版：唯一剩余为证明 Kuznetsov-LS atom (SC-9)。",
            "```",
            "",
            "这不是无条件自足证明；它把 `CleanKLS/DLS` 的硬点压成一个单一谱大筛原子或明确外部引用。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--terminal-dichotomy-json", type=Path, default=DEFAULT_TERMINAL_DICHOTOMY
    )
    parser.add_argument("--actual-payment-json", type=Path, default=DEFAULT_ACTUAL_PAYMENT)
    parser.add_argument(
        "--columntail-bridge-json", type=Path, default=DEFAULT_COLUMNTAIL_BRIDGE
    )
    parser.add_argument("--pdec-mass-json", type=Path, default=DEFAULT_PDEC_MASS)
    parser.add_argument(
        "--nodeletion-terminal-json", type=Path, default=DEFAULT_NODELETION_TERMINAL
    )
    parser.add_argument(
        "--small-ambiguous-json", type=Path, default=DEFAULT_SMALL_AMBIGUOUS
    )
    parser.add_argument("--clean-contract-md", type=Path, default=DEFAULT_CLEAN_CONTRACT)
    parser.add_argument("--hlc-external-md", type=Path, default=DEFAULT_HLC_EXTERNAL)
    parser.add_argument("--hlc-core-md", type=Path, default=DEFAULT_HLC_CORE)
    parser.add_argument("--hlc-spine-md", type=Path, default=DEFAULT_HLC_SPINE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        terminal_dichotomy_path=args.terminal_dichotomy_json,
        actual_payment_path=args.actual_payment_json,
        columntail_bridge_path=args.columntail_bridge_json,
        pdec_mass_path=args.pdec_mass_json,
        nodeletion_terminal_path=args.nodeletion_terminal_json,
        small_ambiguous_path=args.small_ambiguous_json,
        clean_contract_path=args.clean_contract_md,
        hlc_external_path=args.hlc_external_md,
        hlc_core_path=args.hlc_core_md,
        hlc_spine_path=args.hlc_spine_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "external_kls_input_registered": result[
                    "external_kls_input_registered"
                ],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
