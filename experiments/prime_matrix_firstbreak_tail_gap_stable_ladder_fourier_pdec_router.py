#!/usr/bin/env python3
"""生成 stable actual ladder 的有限群 Fourier/PDEC 输入证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_fourier_pdec_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.json",
]

PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderColumnCRTPDEC"
IMPORT = "StableActualLadderOrSparseSAEImportedLedger"
FINITE_GROUP = "StableActualLadderFiniteGroupLedger"
CELL_FUNCTION = "StableActualLadderZeroMeanCellFunctionLedger"
EXCESS_IDENTITY = "StableActualLadderExactExcessIdentityLedger"
FOURIER_BRIDGE = "StableActualLadderFourierPDECBridgeLedger"
LOWER_BOUND = "StableActualLadderNontrivialCharacterLowerBoundLedger"
NO_ANON = "NoAnonymousStableActualLadderColumnCRTExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterFourierBridgeLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {FINITE_GROUP} AND {CELL_FUNCTION} AND {EXCESS_IDENTITY} "
    f"AND {FOURIER_BRIDGE} AND {LOWER_BOUND} AND {NO_ANON} "
    f"AND {SPARSE} AND {NEW_TARGET}"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve()] + SOURCE_FILES
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
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


def replace_latest_basis(previous: dict[str, Any]) -> str:
    """把旧活动基中的 stable ladder/SAE 硬点替换成 Fourier/PDEC 分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 stable ladder Fourier/PDEC 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableActualLadderOrSparseSAEImported",
            imported,
            False,
            "上一层把固定尺度词内持久漂移压成稳定实际 ladder ColumnCRT/PDEC 或 sparse scale-ladder SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableActualLadderFiniteGroupClosed",
            True,
            True,
            "稳定实际 ladder 给出有限乘积群 G=prod_i Z/q_iZ 与固定点位 a=(a_i)。",
            FINITE_GROUP,
        ),
        row(
            "StableActualLadderZeroMeanCellFunctionClosed",
            True,
            True,
            "定义 F_a=1_{g=a}-1/|G|，其均值为 0；稳定 ladder 超额正是 F_a 在支撑上的相关。",
            CELL_FUNCTION,
        ),
        row(
            "StableActualLadderExactExcessIdentityClosed",
            True,
            True,
            "E_a(S)=sum_{n in S}F_a(tau(n))=|{n in S: tau(n)=a}|-|S|/|G| 精确成立。",
            EXCESS_IDENTITY,
        ),
        row(
            "StableActualLadderFourierPDECBridgeClosed",
            True,
            True,
            "有限群 Fourier 展开把 E_a(S) 写成非平凡角色和；若 E_a>0，则存在非平凡角色相关非零。",
            FOURIER_BRIDGE,
        ),
        row(
            "StableActualLadderNontrivialCharacterLowerBoundClosed",
            True,
            True,
            "若 |G|=N>1 且 E_a>0，则存在 chi!=1 使 |sum_{n in S}chi(tau(n))|>=N*E_a/(N-1)。",
            LOWER_BOUND,
        ),
        row(
            "NoAnonymousStableActualLadderColumnCRTExit",
            True,
            True,
            "稳定实际 ladder ColumnCRT 出口被改写成显式 Fourier/PDEC 输入；不再保留黑箱 ColumnCRT 口径。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterFourierBridge",
            True,
            False,
            "非持久实际 ladder 事件继续登记为 sparse scale-ladder SAE；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "StableActualLadderFourierPDECCapStillOpen",
            False,
            False,
            "仍未排斥该 Fourier/PDEC 下界，也未证明 sparse scale-ladder SAE 全局可求和。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需给出 stable ladder Fourier/PDEC cap，或证明 sparse scale-ladder SAE 全局可控。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 stable ladder Fourier/PDEC 证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "稳定实际 ladder 被写成有限乘积群 G=prod_i Z/q_iZ 上的固定点位 a。"
        "零均值函数 F_a=1_a-1/|G| 的支撑相关精确等于 ladder 超额。"
        "若超额 E_a>0，则有限群 Fourier 展开给出非平凡角色下界 "
        "max_{chi!=1}|sum chi(tau(n))|>=|G|E_a/(|G|-1)。"
        "因此 stable ladder ColumnCRT 出口被改写成显式 Fourier/PDEC 输入。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_fourier_pdec_router",
        "status": "stable_actual_ladder_columncrt_reduced_to_fourier_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "stable_ladder_or_sparse_sae_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "finite_group_closed": True,
        "zero_mean_cell_function_closed": True,
        "exact_excess_identity_closed": True,
        "fourier_pdec_bridge_closed": True,
        "nontrivial_character_lower_bound_closed": True,
        "anonymous_stable_ladder_columncrt_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "stable_ladder_fourier_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "fourier_formulas": {
            "finite_group": "G=prod_i Z/q_iZ, N=|G|=prod_i q_i",
            "tau": "tau(n)=(n mod q_i)_i",
            "cell": "C_a={g in G:g=a}",
            "zero_mean": "F_a(g)=1_{C_a}(g)-1/N",
            "excess": "E_a(S)=sum_{n in S}F_a(tau(n))=count_S(C_a)-|S|/N",
            "fourier_coefficients": "hat F_a(1)=0, |hat F_a(chi)|=1/N for chi!=1 under normalized Fourier",
            "lower_bound": "E_a>0 => exists chi!=1 with |sum_{n in S}chi(tau(n))|>=N*E_a/(N-1)",
            "new_failure": "stable actual ladder Fourier/PDEC cap or sparse scale-ladder SAE summability",
        },
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix stable-ladder Fourier/PDEC 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"stable_ladder_or_sparse_sae_imported={fmt_bool(cert['stable_ladder_or_sparse_sae_imported'])}",
        f"finite_group_closed={fmt_bool(cert['finite_group_closed'])}",
        f"zero_mean_cell_function_closed={fmt_bool(cert['zero_mean_cell_function_closed'])}",
        f"exact_excess_identity_closed={fmt_bool(cert['exact_excess_identity_closed'])}",
        f"fourier_pdec_bridge_closed={fmt_bool(cert['fourier_pdec_bridge_closed'])}",
        f"nontrivial_character_lower_bound_closed={fmt_bool(cert['nontrivial_character_lower_bound_closed'])}",
        f"anonymous_stable_ladder_columncrt_removed={fmt_bool(cert['anonymous_stable_ladder_columncrt_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"stable_ladder_fourier_pdec_cap_proved={fmt_bool(cert['stable_ladder_fourier_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 稳定实际 ladder 的有限群",
        "",
        "稳定实际 ladder 给出固定素数-相位词 `((q_i,a_i))`。定义：",
        "",
        "```text",
        "G=prod_i Z/q_iZ,",
        "N=|G|=prod_i q_i,",
        "tau(n)=(n mod q_i)_i,",
        "a=(a_i)_i.",
        "```",
        "",
        "这个乘积群表述不要求 `q_i` 两两不同，因此比单一 CRT 模数写法更稳健。",
        "",
        "## 2. 零均值点位函数",
        "",
        "令：",
        "",
        "```text",
        "F_a(g)=1_{g=a}-1/N.",
        "```",
        "",
        "则 `sum_{g in G}F_a(g)=0`，且对任意支撑 `S` 有精确超额恒等式：",
        "",
        "```text",
        "E_a(S)=sum_{n in S}F_a(tau(n))",
        "      =#{n in S:tau(n)=a}-|S|/N.",
        "```",
        "",
        "## 3. Fourier/PDEC 桥",
        "",
        "在有限群 `G` 上取归一化 Fourier 变换。`F_a` 的平凡角色系数为 `0`，每个非平凡角色的系数模为 `1/N`。因此：",
        "",
        "```text",
        "E_a(S)=sum_{chi!=1} hat F_a(chi) * S_chi,",
        "S_chi=sum_{n in S}chi(tau(n)).",
        "```",
        "",
        "若 `E_a(S)>0`，则：",
        "",
        "```text",
        "max_{chi!=1}|S_chi| >= N*E_a(S)/(N-1).",
        "```",
        "",
        "这就是 stable actual ladder 的显式 Fourier/PDEC 输入。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        PREVIOUS_TARGET,
        "  -> " + IMPORT,
        "  AND " + FINITE_GROUP,
        "  AND " + CELL_FUNCTION,
        "  AND " + EXCESS_IDENTITY,
        "  AND " + FOURIER_BRIDGE,
        "  AND " + LOWER_BOUND,
        "  AND " + NO_ANON,
        "  AND " + SPARSE,
        "  AND " + NEW_TARGET,
        "```",
        "",
        "剩余从稳定实际 ladder ColumnCRT 黑箱出口变成显式 Fourier/PDEC cap，或 sparse scale-ladder SAE 全局求和问题。",
        "",
        "## 5. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(item["gate"]),
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 6. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 7. 诚实边界",
            "",
            "- 本证书没有证明 stable actual ladder Fourier/PDEC cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把稳定实际 ladder ColumnCRT 出口桥接为显式 Fourier/PDEC 输入。",
            f"- `{NEW_TARGET}` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 8. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """生成全部证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    OUT_LEDGER.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
