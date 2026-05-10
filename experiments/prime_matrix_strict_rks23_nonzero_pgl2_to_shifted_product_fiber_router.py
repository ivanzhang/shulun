#!/usr/bin/env python3
"""把非零 PGL2 高谱改写为 shifted interval 模乘积纤维谱。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_nonzero_pgl2_to_shifted_product_fiber_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-nonzero-pgl2-to-shifted-product-fiber-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-nonzero-pgl2-to-shifted-product-fiber-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-nonzero-pgl2-to-shifted-product-fiber-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-affine-degenerate-phase-split-router.json"
AFFINE_FRONTIER = MONO / "prime-matrix-strict-rks23-mobius-to-affine-inverse-high-spectrum-router.json"

SOURCE_FILES = [PREVIOUS, AFFINE_FRONTIER]

TARGET = "NonzeroAffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23"
NEXT_ATOM = "ShiftedIntervalModularProductFiberHighSpectrumPowerSavingForSquareRootCollar"
POINTWISE_ATOM = "UniformShiftedIntervalModularProductFiberSublinearBound"
INCIDENCE_TARGET = "RudnevRNRSShiftedProductFiberIncidenceEstimate"
LATTICE_TARGET = "SelfContainedModularHyperbolaInShiftedIntervalsPointwiseBound"


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


def build_result() -> dict[str, Any]:
    """构造 shifted product fiber 证书。"""
    previous = load_json(PREVIOUS)
    affine = load_json(AFFINE_FRONTIER)

    active = previous.get("next_direct_attack_target") == TARGET
    s0_removed = previous.get("degenerate_phase_s0_energy_absorbed") is True
    affine_identity_imported = affine.get("affine_inverse_self_intersection_identity_closed") is True

    # 对 s!=0，令 c=s^{-1}。由 a^{-1}+b^{-1}=s 得 sab=a+b，
    # 即 ab=c(a+b)，于是 (a-c)(b-c)=c^2。这是等价变换。
    shifted_product_identity_closed = active and s0_removed and affine_identity_imported
    high_spectrum_bound_proved = False
    pointwise_bound_proved = False

    product_fiber = {
        "nonzero_phase": "s != 0",
        "change_of_variable": "c=s^(-1)",
        "original_equation": "a^(-1)+b^(-1)=s with a,b in J",
        "shifted_product_equation": "(a-c)(b-c)=c^2 mod P",
        "fiber_count": "r_J(s)=#{(a,b) in J^2: (a-c)(b-c)=c^2}",
        "high_spectrum_form": "control c with r_c>N^(1-eta), where c runs over F_P^*",
        "pointwise_sufficient_bound": "r_c<=N^(1-eta) for all c would kill the whole nonzero high spectrum",
        "if_pointwise_fails": "a failing c is a concrete shifted modular hyperbola with too many points in J x J",
        "remaining_tools": "finite-field incidence, modular hyperbola in shifted intervals, or PGL2 almost-stabilizer expansion",
    }

    rows = [
        row(
            "NonzeroPGL2TargetActive",
            active,
            True,
            "上一证书已吸收 `s=0`，剩余只含 `s!=0` 的非仿射 PGL2 高谱。",
            TARGET,
        ),
        row(
            "ShiftedProductFiberIdentityClosed",
            shifted_product_identity_closed,
            True,
            "对 `s!=0`，令 `c=s^{-1}`，高谱纤维等价于 shifted interval 模乘积方程。",
            NEXT_ATOM,
        ),
        row(
            "PointwiseFiberBoundWouldCloseSpectrum",
            shifted_product_identity_closed,
            True,
            "若每个 shifted modular hyperbola 在 `J x J` 中只有 `N^(1-eta)` 个点，非零高谱立即为空。",
            POINTWISE_ATOM,
        ),
        row(
            NEXT_ATOM,
            high_spectrum_bound_proved,
            False,
            "仓库内尚未证明 shifted product fiber 的高谱固定幂节省。",
            f"{INCIDENCE_TARGET} OR {LATTICE_TARGET}",
        ),
        row(
            POINTWISE_ATOM,
            pointwise_bound_proved,
            False,
            "更强的点态纤维上界尚未证明；它是当前最直接的硬攻版本。",
            LATTICE_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只闭合等价变换，未证明 shifted product fiber 上界。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_nonzero_pgl2_to_shifted_product_fiber_router",
        "status": "nonzero_pgl2_high_spectrum_rewritten_as_shifted_interval_modular_product_fiber_spectrum",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "nonzero_pgl2_target_active": active,
        "shifted_product_fiber_identity_closed": shifted_product_identity_closed,
        "pointwise_fiber_bound_would_close_spectrum": shifted_product_identity_closed,
        "shifted_product_fiber_high_spectrum_proved": high_spectrum_bound_proved,
        "uniform_shifted_product_fiber_pointwise_bound_proved": pointwise_bound_proved,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "stronger_pointwise_attack_target": POINTWISE_ATOM,
        "parallel_incidence_target": INCIDENCE_TARGET,
        "parallel_lattice_target": LATTICE_TARGET,
        "product_fiber": product_fiber,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "非零相位剩余继续算术化：对 `s!=0` 取 `c=s^{-1}`，"
            "`a^{-1}+b^{-1}=s` 精确等价于 shifted product fiber `(a-c)(b-c)=c^2 mod P`。"
            "因此当前最窄剩余不是一般 PGL2 语言，而是平方根颈部区间 `J` 上的 shifted modular "
            "hyperbola 纤维高谱。若能证明统一点态界 `r_c<=N^(1-eta)`，非零高谱会直接消失。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    product = result["product_fiber"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 非零 PGL2 到 shifted product fiber 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"shifted_product_fiber_identity_closed={fmt_bool(result['shifted_product_fiber_identity_closed'])}",
        f"shifted_product_fiber_high_spectrum_proved={fmt_bool(result['shifted_product_fiber_high_spectrum_proved'])}",
        f"uniform_shifted_product_fiber_pointwise_bound_proved={fmt_bool(result['uniform_shifted_product_fiber_pointwise_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. shifted product fiber 改写",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in product.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 下一最窄自足目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
