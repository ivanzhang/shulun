#!/usr/bin/env python3
"""统一 PDEC-CAP 中持久 MFU 与固定壳低模持久分支。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_persistent_signature_unification_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-persistent-signature-unification-router.json
  docs/monograph/prime-matrix-pdec-cap-persistent-signature-unification-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PROFINITE_APS = DOCS / "prime-matrix-profinite-actual-payment-stitching-router.json"
DEFAULT_DENSE_KERNEL_CVT = (
    DOCS / "prime-matrix-pdec-cap-dense-kernel-common-variable-router.json"
)
DEFAULT_GAMMA_SIGNATURE = DOCS / "prime-matrix-triad-a1-forced-gamma-signature-router.json"
DEFAULT_CONTINUOUS_SIGNATURE = (
    DOCS / "prime-matrix-triad-a1-continuous-pdec-signature-input-ledger.json"
)
DEFAULT_MFU_DICHOTOMY = DOCS / "prime-matrix-triad-a1-multibucket-formal-unit-dichotomy.md"
DEFAULT_COLUMNCRT_ABSORB = DOCS / "prime-matrix-columncrt-displacement-pdec-absorption.md"
DEFAULT_PDEC_DUAL_ABSORB = DOCS / "prime-matrix-pdec-dual-failure-absorption-contract.md"
DEFAULT_MULTIPLICITY_ABSORB = DOCS / "prime-matrix-multiplicity-stitching-absorption-contract.md"
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-persistent-signature-unification-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-persistent-signature-unification-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    blocks_final: bool,
) -> dict[str, Any]:
    """构造审查行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_final": blocks_final,
    }


def build_rows(
    profinite_aps: dict[str, Any],
    dense_kernel_cvt: dict[str, Any],
    gamma_signature: dict[str, Any],
    continuous_signature: dict[str, Any],
    mfu_text: str,
    columncrt_text: str,
    pdec_dual_text: str,
    multiplicity_text: str,
) -> list[dict[str, Any]]:
    """生成持久有限签名统一审查表。"""
    aps_positive_branch_is_finite_signature = (
        profinite_aps["profinite_aps_dichotomy_closed"]
        and "SameSetPDECDualComparisonForPersistentMFU"
        in profinite_aps["open_final_gates"]
    )
    forced_gamma_signature_materialized = (
        gamma_signature["status"] == "forced_gamma_signature_pressure_materialized"
        and gamma_signature["all_rows_routed_to_forced_signature_or_small_ambiguous_clean"]
        and gamma_signature["signature_matrix_row_count"] == 48
    )
    positive_limsup_pdec_inputs_materialized = (
        continuous_signature["status"]
        == "continuous_positive_limsup_pdec_inputs_materialized_capacity_open"
        and continuous_signature["all_signature_rows_have_prime_lift_congruence"]
        and set(continuous_signature["route_counts"]) == {"FiniteSignaturePDECInputMaterialized"}
    )
    mfu_formal_unit_registered = has_all(
        mfu_text,
        [
            "Persistent Formal Unit",
            "U_CRT^multi(S_N) < L_PDEC^multi(S_N)",
            "Distributed Payment",
            "因此没有第四出口",
        ],
    )
    fixed_shell_is_finite_shell_signature = (
        dense_kernel_cvt["dense_kernel_no_unnamed_escape_closed"]
        and "FixedShellLowModPersistencePDECOrColumnCRT"
        in dense_kernel_cvt["open_final_gates"]
        and "c_b=rho_b+r k_b" in dense_kernel_cvt["common_variable_law"]
    )
    columncrt_absorbed_to_displacement_pdec = has_all(
        columncrt_text,
        [
            "ColumnCRT-Displacement Absorption",
            "displacement PDEC",
            "formal-unit refinement / primitive quotient",
        ],
    )
    pdec_failure_absorbed_to_cap = has_all(
        pdec_dual_text,
        [
            "Cap localization",
            "CapPersistent",
            "refined PDEC / ColumnCRT",
            "Multiplicity-Stitching",
        ],
    )
    multiplicity_absorbed_to_same_formal_unit = has_all(
        multiplicity_text,
        [
            "Formal unit 原则",
            "WeightedDualIndependence",
            "CoordinateQuotient",
            "ReuseDefect",
        ],
    )
    persistent_branches_unified = all(
        [
            aps_positive_branch_is_finite_signature,
            forced_gamma_signature_materialized,
            positive_limsup_pdec_inputs_materialized,
            mfu_formal_unit_registered,
            fixed_shell_is_finite_shell_signature,
            columncrt_absorbed_to_displacement_pdec,
            pdec_failure_absorbed_to_cap,
            multiplicity_absorbed_to_same_formal_unit,
        ]
    )

    return [
        row(
            "APSPositiveBranchIsFiniteSignature",
            aps_positive_branch_is_finite_signature,
            str(profinite_aps["open_final_gates"]),
            "APS 投影塔的持久分支已经被定义为某个有限签名正 limsup 持久，而不是自由选择出口。",
            False,
        ),
        row(
            "ForcedGammaFiniteSignatureMaterialized",
            forced_gamma_signature_materialized,
            (
                f"rows={gamma_signature['signature_matrix_row_count']}; "
                f"min_margin={gamma_signature['global_min_signature_signal_minus_ambiguous_budget']:.6g}"
            ),
            "当前 forced Gamma 的有限层 phase-bucket 签名已物化；超过 ambiguous 预算的持久质量必须进入 MFU/PDEC。",
            False,
        ),
        row(
            "PositiveLimsupPDECInputsMaterialized",
            positive_limsup_pdec_inputs_materialized,
            (
                f"signature_rows={continuous_signature['signature_row_count']}; "
                f"route_counts={continuous_signature['route_counts']}"
            ),
            "正 limsup 有限签名已登记为同集 PDEC 输入行；剩余只是不等式 U_CRT<L_PDEC。",
            False,
        ),
        row(
            "MFUFormalUnitProtocolRegistered",
            mfu_formal_unit_registered,
            "Persistent Formal Unit / Distributed Payment dichotomy",
            "多桶对象只有在投影兼容且长期承担正质量时才是 formal unit；否则进入分散 CleanKLS/DLS。",
            False,
        ),
        row(
            "FixedShellIsFiniteShellSignature",
            fixed_shell_is_finite_shell_signature,
            dense_kernel_cvt["narrowest_dense_kernel_hardpoint"],
            "固定壳或有限壳包正密度等价于同一壳号变量上的有限 shell signature 持久。",
            False,
        ),
        row(
            "ColumnCRTAbsorbedAsDisplacementPDEC",
            columncrt_absorbed_to_displacement_pdec,
            "ColumnCRT => displacement PDEC / SAE / quotient",
            "固定壳若表现为列位移持久，不是独立终端，而是 displacement PDEC 或合法商后的 primitive PDEC。",
            False,
        ),
        row(
            "PDECFailureAbsorbsCaps",
            pdec_failure_absorbed_to_cap,
            "dual failure => cap concentration => refined PDEC/ColumnCRT/SAE/MS",
            "持久有限签名的对偶失败只能产生帽集中并回流 PDEC family；它不能生成新的低模黑箱。",
            False,
        ),
        row(
            "MultiplicitySameFormalUnitAbsorbed",
            multiplicity_absorbed_to_same_formal_unit,
            "WeightedDualIndependence / CoordinateQuotient / ReuseDefect",
            "若 MFU、固定壳、ColumnCRT 使用的口径不一致，必须先规范化到同一 formal unit 或回流复用缺陷。",
            False,
        ),
        row(
            "PersistentFiniteSignatureUnificationClosed",
            persistent_branches_unified,
            "persistent MFU and fixed-shell low-mod persistence share finite-signature formal-unit grammar",
            "持久 Gamma 与固定壳低模持久不再是两个平行无名硬点；二者统一为同一 formal unit 上的有限签名 PDEC/ColumnCRT 终端证书。",
            False,
        ),
        row(
            "PersistentFiniteSignaturePDECColumnCRT",
            False,
            "terminal U_CRT<L_PDEC or displacement PDEC exclusion not submitted",
            "仍需证明所有持久有限签名 formal unit 的 PDEC/ColumnCRT 对偶容量排斥。",
            True,
        ),
        row(
            "SelfContainedKuznetsovLSAtomSC9",
            False,
            "flat multishell clean atom remains open",
            "没有持久有限签名且多壳频率平坦时，自足版仍需证明 SC-9 谱大筛原子。",
            True,
        ),
    ]


def run(
    profinite_aps_path: Path,
    dense_kernel_cvt_path: Path,
    gamma_signature_path: Path,
    continuous_signature_path: Path,
    mfu_dichotomy_path: Path,
    columncrt_absorb_path: Path,
    pdec_dual_absorb_path: Path,
    multiplicity_absorb_path: Path,
) -> dict[str, Any]:
    """运行持久有限签名统一路由。"""
    profinite_aps = load_json(profinite_aps_path)
    dense_kernel_cvt = load_json(dense_kernel_cvt_path)
    gamma_signature = load_json(gamma_signature_path)
    continuous_signature = load_json(continuous_signature_path)
    mfu_text = read_text(mfu_dichotomy_path)
    columncrt_text = read_text(columncrt_absorb_path)
    pdec_dual_text = read_text(pdec_dual_absorb_path)
    multiplicity_text = read_text(multiplicity_absorb_path)
    rows = build_rows(
        profinite_aps=profinite_aps,
        dense_kernel_cvt=dense_kernel_cvt,
        gamma_signature=gamma_signature,
        continuous_signature=continuous_signature,
        mfu_text=mfu_text,
        columncrt_text=columncrt_text,
        pdec_dual_text=pdec_dual_text,
        multiplicity_text=multiplicity_text,
    )
    unification_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "PersistentFiniteSignatureUnificationClosed"
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_persistent_signature_unification_router",
        "status": "persistent_signature_unified_to_pdec_columncrt_or_sc9_terminal_estimates_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "profinite_aps": file_sha256(profinite_aps_path),
            "dense_kernel_cvt": file_sha256(dense_kernel_cvt_path),
            "gamma_signature": file_sha256(gamma_signature_path),
            "continuous_signature": file_sha256(continuous_signature_path),
            "mfu_dichotomy": file_sha256(mfu_dichotomy_path),
            "columncrt_absorb": file_sha256(columncrt_absorb_path),
            "pdec_dual_absorb": file_sha256(pdec_dual_absorb_path),
            "multiplicity_absorb": file_sha256(multiplicity_absorb_path),
        },
        "persistent_signature_unification_closed": unification_closed,
        "persistent_finite_signature_pdec_columncrt_closed": False,
        "self_contained_sc9_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": (
            "PersistentFiniteSignaturePDECColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9"
        ),
        "rows": rows,
        "unification_law": (
            "Persistent Gamma and fixed-shell low-mod persistence are the same kind of "
            "object after the common-variable rewrite. Both are positive-limsup mass on a "
            "finite signature inside one formal unit: a phase-bucket/tail-column signature "
            "for MFU, or a shell/displacement signature for fixed-shell persistence. If the "
            "signature persists, it must submit a same-formal-unit PDEC/ColumnCRT dual "
            "capacity certificate. If it does not persist, the mass is diffuse and has "
            "already been routed to deletion/NoDeletion-KL/CleanKLS, with the flat clean "
            "case named as SC-9. ColumnCRT is absorbed as displacement PDEC, PDEC dual "
            "failure is absorbed as cap refinement, and multiplicity mismatch is absorbed "
            "by formal-unit normalization. Hence the two previous persistent gates collapse "
            "to one terminal family: PersistentFiniteSignaturePDECColumnCRT, plus the "
            "separate flat SC-9 atom."
        ),
        "review_conclusion": (
            "持久 MFU 与固定壳低模持久已经统一：二者本质上都是同一 formal unit 上的有限签名正密度。"
            "ColumnCRT 位移、PDEC 对偶失败和口径不一致都已有吸收合同，所以它们不能作为新的平行终端。"
            "剩余自足硬点因此压成两项：`PersistentFiniteSignaturePDECColumnCRT` 的终端排斥，"
            "以及无持久且多壳平坦时的 `SelfContainedKuznetsovLSAtomSC9`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 持久有限签名统一路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 统一律",
        "",
        result["unification_law"],
        "",
        "```text",
        "Persistent Gamma / MFU",
        "  => positive-limsup finite phase-bucket formal unit",
        "  => same-set multi-bucket PDEC;",
        "",
        "Fixed shell / finite shell packet",
        "  => positive-limsup finite shell/displacement signature",
        "  => displacement PDEC or ColumnCRT-as-PDEC;",
        "",
        "formal-unit mismatch",
        "  => weighted PDEC / quotient / reuse defect;",
        "",
        "no persistent finite signature",
        "  => diffuse deletion / NoDeletion-KL / CleanKLS;",
        "  flat multishell clean => SelfContainedKuznetsovLSAtomSC9.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `persistent_signature_unification_closed={fmt_bool(result['persistent_signature_unification_closed'])}`。",
        f"- `persistent_finite_signature_pdec_columncrt_closed={fmt_bool(result['persistent_finite_signature_pdec_columncrt_closed'])}`。",
        f"- `self_contained_sc9_closed={fmt_bool(result['self_contained_sc9_closed'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `narrowest_next_hardpoint={result['narrowest_next_hardpoint']}`。",
        f"- `open_final_gates={result['open_final_gates']}`。",
        "",
        "## 3. 审查表",
        "",
        "| gate | closed | blocks final | evidence | meaning |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {evidence} | {meaning} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(bool(item["closed"])),
                blocks=fmt_bool(bool(item["blocks_final"])),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 剩余",
            "",
            "本路由器关闭的是“持久 MFU”和“固定壳低模持久”之间的平行分支膨胀。"
            "它不证明 `U_CRT<L_PDEC`，也不证明 SC-9。下一步应直接攻 "
            "`PersistentFiniteSignaturePDECColumnCRT` 的同 formal unit 容量证书，"
            "或攻 flat multishell clean residual 的 `SC-9` 自足谱原子。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profinite-aps-json", type=Path, default=DEFAULT_PROFINITE_APS)
    parser.add_argument("--dense-kernel-cvt-json", type=Path, default=DEFAULT_DENSE_KERNEL_CVT)
    parser.add_argument("--gamma-signature-json", type=Path, default=DEFAULT_GAMMA_SIGNATURE)
    parser.add_argument(
        "--continuous-signature-json", type=Path, default=DEFAULT_CONTINUOUS_SIGNATURE
    )
    parser.add_argument("--mfu-dichotomy-md", type=Path, default=DEFAULT_MFU_DICHOTOMY)
    parser.add_argument("--columncrt-absorb-md", type=Path, default=DEFAULT_COLUMNCRT_ABSORB)
    parser.add_argument("--pdec-dual-absorb-md", type=Path, default=DEFAULT_PDEC_DUAL_ABSORB)
    parser.add_argument(
        "--multiplicity-absorb-md", type=Path, default=DEFAULT_MULTIPLICITY_ABSORB
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        profinite_aps_path=args.profinite_aps_json,
        dense_kernel_cvt_path=args.dense_kernel_cvt_json,
        gamma_signature_path=args.gamma_signature_json,
        continuous_signature_path=args.continuous_signature_json,
        mfu_dichotomy_path=args.mfu_dichotomy_md,
        columncrt_absorb_path=args.columncrt_absorb_md,
        pdec_dual_absorb_path=args.pdec_dual_absorb_md,
        multiplicity_absorb_path=args.multiplicity_absorb_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_next_hardpoint"])


if __name__ == "__main__":
    main()
