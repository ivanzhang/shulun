#!/usr/bin/env python3
"""生成 stable ladder Fourier cap 的 pivot-fiber PDEC 输入证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_pivot_fiber_pdec_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap"

IMPORT = "StableActualLadderFourierCapImportedLedger"
CHAR_FACTOR = "StableLadderCharacterFactorizationLedger"
PIVOT = "StableLadderNontrivialPivotCoordinateLedger"
FIBERS = "StableLadderComplementFiberPartitionLedger"
LOCALIZATION = "StableLadderGlobalCharacterToPivotFiberLocalizationLedger"
PRIMITIVE = "StableLadderPrimitivePivotCharacterCorrelationLedger"
NO_ANON = "NoAnonymousStableLadderFourierCapLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterPivotFiberLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {CHAR_FACTOR} AND {PIVOT} AND {FIBERS} "
    f"AND {LOCALIZATION} AND {PRIMITIVE} AND {NO_ANON} "
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
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
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
    """把旧活动基中的 Fourier cap 硬点替换成 pivot-fiber 分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 pivot-fiber PDEC 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableActualLadderFourierCapImported",
            imported,
            False,
            "上一层把稳定实际 ladder 的匿名 ColumnCRT 出口改写为非平凡 Fourier/PDEC cap。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderCharacterFactorizationClosed",
            True,
            True,
            "有限乘积群 G=prod_i Z/q_iZ 的每个角色可分解为 chi(g)=prod_i chi_i(g_i)。",
            CHAR_FACTOR,
        ),
        row(
            "StableLadderNontrivialPivotCoordinateClosed",
            True,
            True,
            "若 chi 非平凡，则至少一个坐标 chi_j 非平凡；选择这样的 pivot 坐标 j。",
            PIVOT,
        ),
        row(
            "StableLadderComplementFiberPartitionClosed",
            True,
            True,
            "按其余坐标 h=tau_{-j}(n) 分割支撑 S，得到互不相交纤维 S_h。",
            FIBERS,
        ),
        row(
            "StableLadderGlobalCharacterToPivotFiberLocalizationClosed",
            True,
            True,
            "若 |S_chi|>=Lambda，则存在补坐标纤维 h 使 |sum_{n in S_h}chi_j(n mod q_j)|>=Lambda/|G_{-j}|。",
            LOCALIZATION,
        ),
        row(
            "StableLadderPrimitivePivotCharacterCorrelationClosed",
            True,
            True,
            "代入 Lambda=N*E/(N-1) 与 |G_{-j}|=N/q_j，得到单坐标阈值 q_j*E/(N-1)。",
            PRIMITIVE,
        ),
        row(
            "NoAnonymousStableLadderFourierCap",
            True,
            True,
            "稳定 ladder 的全局 Fourier cap 不再匿名；它必落到某个 pivot 坐标和补坐标纤维的原子相位相关。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterPivotFiber",
            True,
            False,
            "非持久实际 ladder 事件继续登记为 sparse scale-ladder SAE；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "StableActualLadderPrimitiveFiberPDECCapStillOpen",
            False,
            False,
            "仍未证明所有 pivot-fiber 原子相位相关都低于阈值，也未证明 sparse scale-ladder SAE 全局可求和。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需给出 primitive fiber PDEC cap，或证明 sparse scale-ladder SAE 全局可控。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 stable ladder pivot-fiber PDEC 证书。"""
    previous = load_json(PREVIOUS_CERT)
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "稳定实际 ladder 的非平凡 Fourier cap 可按角色分解和补坐标纤维分割进一步局部化。"
        "对任意非平凡角色 chi=prod_i chi_i，选取非平凡 pivot 坐标 j；按其余坐标 h 分割支撑。"
        "若全局角色和 |S_chi| 至少为 Lambda，则三角不等式强制存在某个纤维 h，使单坐标角色和至少为 Lambda/|G_{-j}|。"
        "代入上一层 Lambda=N*E/(N-1) 与 |G_{-j}|=N/q_j，得到原子阈值 q_j*E/(N-1)。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_pivot_fiber_pdec_router",
        "status": "stable_ladder_fourier_cap_reduced_to_pivot_fiber_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "stable_ladder_fourier_cap_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "character_factorization_closed": True,
        "nontrivial_pivot_coordinate_closed": True,
        "complement_fiber_partition_closed": True,
        "global_character_to_pivot_fiber_localization_closed": True,
        "primitive_pivot_character_correlation_closed": True,
        "anonymous_fourier_cap_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "primitive_fiber_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "pivot_fiber_formulas": {
            "character_factorization": "chi(g)=prod_i chi_i(g_i)",
            "pivot": "choose j with chi_j != 1",
            "complement_group": "G_{-j}=prod_{i!=j} Z/q_iZ, |G_{-j}|=N/q_j",
            "fiber": "S_h={n in S: tau_{-j}(n)=h}",
            "global_sum": "S_chi=sum_h chi_{-j}(h) * A_h",
            "fiber_sum": "A_h=sum_{n in S_h} chi_j(n mod q_j)",
            "localization": "|S_chi|<=sum_h |A_h|<=|G_{-j}| max_h |A_h|",
            "threshold": "|S_chi|>=Lambda => exists h with |A_h|>=Lambda/|G_{-j}|",
            "ladder_threshold": "Lambda=N*E/(N-1) => |A_h|>=q_j*E/(N-1)",
            "new_failure": "primitive pivot-fiber PDEC cap or sparse scale-ladder SAE summability",
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
        "# Prime Matrix stable-ladder pivot-fiber PDEC 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"stable_ladder_fourier_cap_imported={fmt_bool(cert['stable_ladder_fourier_cap_imported'])}",
        f"character_factorization_closed={fmt_bool(cert['character_factorization_closed'])}",
        f"nontrivial_pivot_coordinate_closed={fmt_bool(cert['nontrivial_pivot_coordinate_closed'])}",
        f"complement_fiber_partition_closed={fmt_bool(cert['complement_fiber_partition_closed'])}",
        (
            "global_character_to_pivot_fiber_localization_closed="
            f"{fmt_bool(cert['global_character_to_pivot_fiber_localization_closed'])}"
        ),
        f"primitive_pivot_character_correlation_closed={fmt_bool(cert['primitive_pivot_character_correlation_closed'])}",
        f"anonymous_fourier_cap_removed={fmt_bool(cert['anonymous_fourier_cap_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"primitive_fiber_pdec_cap_proved={fmt_bool(cert['primitive_fiber_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 角色分解与 pivot 坐标",
        "",
        "稳定 ladder 的有限群为：",
        "",
        "```text",
        "G=prod_i Z/q_iZ,  N=|G|=prod_i q_i.",
        "```",
        "",
        "任一角色都分解为：",
        "",
        "```text",
        "chi(g)=prod_i chi_i(g_i).",
        "```",
        "",
        "若 `chi` 非平凡，则存在 `j` 使 `chi_j` 非平凡；固定这样的 `j` 作为 pivot 坐标。",
        "",
        "## 2. 补坐标纤维分割",
        "",
        "令：",
        "",
        "```text",
        "G_{-j}=prod_{i!=j} Z/q_iZ,",
        "|G_{-j}|=N/q_j,",
        "S_h={n in S: tau_{-j}(n)=h}.",
        "```",
        "",
        "对每个纤维定义单坐标角色和：",
        "",
        "```text",
        "A_h=sum_{n in S_h} chi_j(n mod q_j).",
        "```",
        "",
        "则全局角色和精确分解为：",
        "",
        "```text",
        "S_chi=sum_h chi_{-j}(h) * A_h.",
        "```",
        "",
        "## 3. 全局异常到单坐标异常",
        "",
        "由三角不等式：",
        "",
        "```text",
        "|S_chi|<=sum_h |A_h|<=|G_{-j}| max_h |A_h|.",
        "```",
        "",
        "因此若 `|S_chi|>=Lambda`，则存在补坐标纤维 `h` 使：",
        "",
        "```text",
        "|A_h|>=Lambda/|G_{-j}|.",
        "```",
        "",
        "代入上一层 Fourier 桥给出的 `Lambda=N*E_a(S)/(N-1)`，得到：",
        "",
        "```text",
        "|A_h|>=q_j*E_a(S)/(N-1).",
        "```",
        "",
        "这把 stable ladder Fourier cap 改写成一个单素数模数 `q_j` 上、固定补坐标纤维中的原子相位相关 cap。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从全局 Fourier cap 变成 primitive pivot-fiber PDEC cap，或 sparse scale-ladder SAE 全局求和问题。",
        "",
        "## 5. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
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
            "- 本证书没有证明 primitive pivot-fiber PDEC cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 stable ladder 的全局 Fourier cap 局部化为单坐标纤维相位相关输入。",
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
    """生成 JSON、ledger 与 Markdown 归档。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    write_md(cert)
    print(json.dumps({
        "status": cert["status"],
        "next_direct_attack_target": cert["next_direct_attack_target"],
        "row_column_unconditional_closed": cert["row_column_unconditional_closed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
