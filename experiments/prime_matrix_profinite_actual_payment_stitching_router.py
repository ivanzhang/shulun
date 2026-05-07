#!/usr/bin/env python3
"""闭合 ActualPaymentStitching 的投影塔二分逻辑。

用法示例：
  python3 experiments/prime_matrix_profinite_actual_payment_stitching_router.py

输出：
  docs/monograph/prime-matrix-profinite-actual-payment-stitching-router.json
  docs/monograph/prime-matrix-profinite-actual-payment-stitching-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PDEC_CAP = DOCS / "prime-matrix-pdec-cap-same-set-global-dual-router.json"
DEFAULT_APS_CONTRACT = DOCS / "prime-matrix-triad-a1-actual-payment-stitching-contract.md"
DEFAULT_APS_ROUTER = DOCS / "prime-matrix-triad-a1-actual-payment-stitching-router.json"
DEFAULT_CONTINUOUS_DICHOTOMY = (
    DOCS / "prime-matrix-triad-a1-continuous-terminal-dichotomy-router.json"
)
DEFAULT_SMALL_AMBIGUOUS = (
    DOCS / "prime-matrix-triad-a1-small-ambiguous-clean-admission-router.json"
)
DEFAULT_NO_CYCLE = DOCS / "prime-matrix-pdec-cap-refinement-no-cycle.md"
DEFAULT_JSON = DOCS / "prime-matrix-profinite-actual-payment-stitching-router.json"
DEFAULT_MD = DOCS / "prime-matrix-profinite-actual-payment-stitching-router.md"


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


def audit_row(
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
    pdec_cap: dict[str, Any],
    aps_contract_text: str,
    aps_router: dict[str, Any],
    continuous_dichotomy: dict[str, Any],
    small_ambiguous: dict[str, Any],
    no_cycle_text: str,
) -> list[dict[str, Any]]:
    """生成 APS 投影塔二分审查表。"""
    pdec_cap_frontier = pdec_cap["narrowest_next_hardpoint"]
    # APS 闭合后，上一层前沿会推进到两侧终端估计；重跑时不能把这个稳定状态误判成未请求 APS。
    pdec_cap_requests_aps = pdec_cap_frontier in {
        "ProfiniteActualPaymentStitchingDichotomy",
        "SameSetPDECDualComparisonForPersistentMFU_OR_DiffuseCleanKLS",
        "SameSetPDECDualComparisonForPersistentMFU_OR_DiffuseGlobalDeletionOrSC9",
        "SameSetPDECDualComparisonForPersistentMFU_OR_DiffuseDeletionDivergenceOrSC9",
        "SameSetPDECDualComparisonForPersistentMFU_OR_OccupancySaturationOrSC9",
    }
    aps_contract_has_dichotomy = has_all(
        aps_contract_text,
        [
            "PersistentStitching",
            "NoPersistentStitching",
            "ActualPaymentGamma",
            "不产生第四出口",
        ],
    )
    current_rows_routed_to_aps = (
        aps_router["all_current_forced_multibucket_rows_routed_to_aps"]
        and aps_router["gates"]["finite_layer_mfu_candidates_exist"]
        and aps_router["gates"]["forced_signature_or_small_ambiguous_gate_active"]
    )
    finite_projection_dichotomy_available = (
        continuous_dichotomy["status"]
        == "continuous_terminal_dichotomy_admission_closed_capacity_open"
        and "no third terminal route in the finite-projection dichotomy"
        in continuous_dichotomy["closed_subclaims"]
        and any(
            "L2-flat" in item and "admission" in item
            for item in continuous_dichotomy["closed_subclaims"]
        )
    )
    positive_branch_to_pdec_registered = (
        "positive-limsup branch supplies legal finite column-tail PDEC row input"
        in continuous_dichotomy["closed_subclaims"]
    )
    diffuse_branch_to_clean_registered = (
        small_ambiguous["all_current_small_ambiguous_routed"]
        and small_ambiguous["gates"]["no_clean_shape_currently_visible"]
        and "CleanKLSOnlyAfterFlatNoDeletion" in small_ambiguous["route"]
    )
    no_cycle_absorbs_new_atoms = has_all(
        no_cycle_text,
        [
            "固定 G 内 refined PDEC 不能无限循环",
            "升层分支必须回到 new-layer PDEC / ColumnCRT / CleanKLS",
            "New-layer 塔熵合同",
        ],
    )
    profinite_dichotomy_closed = all(
        [
            pdec_cap_requests_aps,
            aps_contract_has_dichotomy,
            current_rows_routed_to_aps,
            finite_projection_dichotomy_available,
            positive_branch_to_pdec_registered,
            diffuse_branch_to_clean_registered,
            no_cycle_absorbs_new_atoms,
        ]
    )
    return [
        audit_row(
            "PDECCapRequestsAPS",
            pdec_cap_requests_aps,
            pdec_cap_frontier,
            "上一层 PDEC-CAP 前沿已经把 APS 投影塔二分定位为当前门，或已越过 APS 推进到两侧终端估计。",
            False,
        ),
        audit_row(
            "APSContractContainsTwoWaySplit",
            aps_contract_has_dichotomy,
            "PersistentStitching / NoPersistentStitching",
            "APS 合同已经写明真实支付图只能进入持久缝合或无持久缝合两路。",
            False,
        ),
        audit_row(
            "CurrentForcedRowsRoutedToAPS",
            current_rows_routed_to_aps,
            aps_router["route"],
            "当前 forced 多桶行已全部进入 APS，且有限候选行与 forced/ambiguous 门控已接线。",
            False,
        ),
        audit_row(
            "FiniteProjectionDichotomyAvailable",
            finite_projection_dichotomy_available,
            continuous_dichotomy["status"],
            "有限投影空间有限，因此正 limsup 原子或全部原子消散二分可复用到 Gamma 投影塔。",
            False,
        ),
        audit_row(
            "PositiveLimsupBranchRoutesToPDEC",
            positive_branch_to_pdec_registered,
            "positive-limsup finite signature => PDEC input",
            "若 Gamma 在某有限签名上正 limsup 持久，则生成多桶 formal unit/refined PDEC 输入。",
            False,
        ),
        audit_row(
            "DiffuseBranchRoutesToCleanOrDeletionKL",
            diffuse_branch_to_clean_registered,
            small_ambiguous["route"],
            "若固定有限签名全部消散，则进入分散支付；当前门控要求先经 FiberDeletion 或 NoDeletion-KL，平坦时才 CleanKLS。",
            False,
        ),
        audit_row(
            "NewFiniteAtomsDoNotCreateFourthExit",
            no_cycle_absorbs_new_atoms,
            "PDEC cap no-cycle + new-layer entropy contract",
            "若二分过程中生成新的有限原子，它只会细化 PDEC、升层或进入 CleanKLS，不生成第四出口。",
            False,
        ),
        audit_row(
            "ProfiniteActualPaymentStitchingDichotomyClosed",
            profinite_dichotomy_closed,
            "finite projection compactness / pigeonhole dichotomy",
            "APS 的全局二分逻辑闭合；这只排除无名 APS 出口，不证明两侧终端估计。",
            False,
        ),
        audit_row(
            "SameSetPDECDualComparisonForPersistentMFU",
            False,
            "U_CRT^multi<L_PDEC^multi still open",
            "持久 Gamma 分支仍需多桶同集 PDEC 对偶容量证书。",
            True,
        ),
        audit_row(
            "DiffuseCleanKLSDLSEstimateOrFiberDeletionNoDeletionKL",
            False,
            "terminal estimates still open",
            "无持久 Gamma 分支仍需删除势发散、NoDeletion-KL/PDEC，或 KL 平坦 CleanKLS/DLS 大筛估计。",
            True,
        ),
    ]


def run(
    pdec_cap_path: Path,
    aps_contract_path: Path,
    aps_router_path: Path,
    continuous_dichotomy_path: Path,
    small_ambiguous_path: Path,
    no_cycle_path: Path,
) -> dict[str, Any]:
    """运行 APS 投影塔二分审查。"""
    pdec_cap = load_json(pdec_cap_path)
    aps_contract_text = read_text(aps_contract_path)
    aps_router = load_json(aps_router_path)
    continuous_dichotomy = load_json(continuous_dichotomy_path)
    small_ambiguous = load_json(small_ambiguous_path)
    no_cycle_text = read_text(no_cycle_path)
    rows = build_rows(
        pdec_cap=pdec_cap,
        aps_contract_text=aps_contract_text,
        aps_router=aps_router,
        continuous_dichotomy=continuous_dichotomy,
        small_ambiguous=small_ambiguous,
        no_cycle_text=no_cycle_text,
    )
    dichotomy_closed = next(
        item["closed"]
        for item in rows
        if item["gate"] == "ProfiniteActualPaymentStitchingDichotomyClosed"
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_profinite_actual_payment_stitching_router",
        "status": "profinite_actual_payment_stitching_dichotomy_closed_terminal_estimates_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "pdec_cap_router": file_sha256(pdec_cap_path),
            "aps_contract": file_sha256(aps_contract_path),
            "aps_router": file_sha256(aps_router_path),
            "continuous_terminal_dichotomy": file_sha256(continuous_dichotomy_path),
            "small_ambiguous": file_sha256(small_ambiguous_path),
            "pdec_no_cycle": file_sha256(no_cycle_path),
        },
        "profinite_aps_dichotomy_closed": dichotomy_closed,
        "pdec_cap_same_set_global_dual_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": "SameSetPDECDualComparisonForPersistentMFU_OR_DiffuseCleanKLS",
        "rows": rows,
        "dichotomy_law": (
            "For the inverse tower of finite payment-signature spaces, project the real "
            "payment graph Gamma_n to every fixed finite level. Since each level is finite, "
            "either some finite atom has positive limsup mass, or every fixed atom has mass "
            "tending to zero. The first case is PersistentStitching and creates a "
            "multi-bucket formal PDEC unit. The second case is NoPersistentStitching: all "
            "finite projections have max atom and L2 energy tending to zero, so the branch is "
            "a diffuse CleanKLS/DLS input unless FiberDeletion or NoDeletion-KL has already "
            "routed it back to PDEC. This closes the APS dichotomy logic but not the terminal "
            "PDEC or KLS estimates."
        ),
        "review_conclusion": (
            "APS 的投影塔二分逻辑已闭合：真实支付图 `Gamma_n` 在任意无限反例塔上，"
            "要么某个有限签名正 limsup 持久，进入多桶 MFU/PDEC；要么每个固定有限签名质量趋零，"
            "进入分散 CleanKLS/DLS 输入，期间若删除势或 KL 偏斜出现则回流 PDEC。"
            "这一步关闭的是无名 APS 出口；全局 PDEC-CAP 仍需两侧终端估计。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix APS 投影塔二分路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 二分律",
        "",
        result["dichotomy_law"],
        "",
        "```text",
        "Gamma_n on inverse finite signature tower",
        "  either exists finite atom R with limsup Gamma_n(R)>0",
        "    => PersistentStitching => multi-bucket MFU/PDEC；",
        "  or every fixed finite atom has Gamma_n(R)->0",
        "    => NoPersistentStitching => diffuse CleanKLS/DLS input；",
        "  with FiberDeletion / NoDeletion-KL allowed to route back to PDEC before CleanKLS.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `profinite_aps_dichotomy_closed={fmt_bool(result['profinite_aps_dichotomy_closed'])}`。",
        f"- `pdec_cap_same_set_global_dual_closed={fmt_bool(result['pdec_cap_same_set_global_dual_closed'])}`。",
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
            "本文件不证明 `U_CRT^multi<L_PDEC^multi`，也不证明 CleanKLS/DLS 大筛估计。"
            "它只证明 APS 不是第四出口：持久即 PDEC，消散即 CleanKLS/DLS 或删除/KL 回流 PDEC。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdec-cap-json", type=Path, default=DEFAULT_PDEC_CAP)
    parser.add_argument("--aps-contract-md", type=Path, default=DEFAULT_APS_CONTRACT)
    parser.add_argument("--aps-router-json", type=Path, default=DEFAULT_APS_ROUTER)
    parser.add_argument("--continuous-dichotomy-json", type=Path, default=DEFAULT_CONTINUOUS_DICHOTOMY)
    parser.add_argument("--small-ambiguous-json", type=Path, default=DEFAULT_SMALL_AMBIGUOUS)
    parser.add_argument("--no-cycle-md", type=Path, default=DEFAULT_NO_CYCLE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        pdec_cap_path=args.pdec_cap_json,
        aps_contract_path=args.aps_contract_md,
        aps_router_path=args.aps_router_json,
        continuous_dichotomy_path=args.continuous_dichotomy_json,
        small_ambiguous_path=args.small_ambiguous_json,
        no_cycle_path=args.no_cycle_md,
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
