#!/usr/bin/env python3
"""把仿射平方集自交压成非平凡斜率的二次曲线束。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_slope_conic_bundle_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-slope-conic-bundle-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-slope-conic-bundle-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-slope-conic-bundle-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-affine-square-set-intersection-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "NontrivialAffineSelfIntersectionEnergyOfShortSquareSetPowerSaving"
NEXT_ATOM = "NontrivialSlopeLocalizedTernaryConicBundlePowerSaving"
CONIC_ATOM = "RootBoxSlopeConicIncidencePowerSaving"


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
    """构造斜率二次曲线束证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    affine_closed = previous.get("affine_square_set_linearization_closed") is True

    # 仿射式 v=(u/x)y+u(u-x)。令 lambda=u/x，
    # 则 u=lambda*x 且平移项 u(u-x)=lambda(lambda-1)x^2。
    # 所以剩余不是任意仿射族，而是每个 lambda 上的
    #   d2^2=lambda*d1^2+lambda(lambda-1)*x^2。
    slope_conic_closed = active and affine_closed
    nonsingular_closed = active and affine_closed

    conic_bundle = {
        "slope": "lambda=u/x",
        "nontrivial_scope": "lambda not in {0,1}; lambda=1 is t-diagonal and lambda=0 is impossible because u=t2!=0",
        "root_box_restriction": "x in T and lambda*x in T",
        "affine_translation_identity": "u(u-x)=lambda(lambda-1)x^2",
        "conic_equation": "d2^2=lambda*d1^2+lambda(lambda-1)*x^2 mod P",
        "bundle_form": "sum over nontrivial slopes lambda of localized solutions (x,d1,d2)",
        "nonsingularity": "for lambda not in {0,1}, the ternary quadratic form has three nonzero coefficients",
        "why_narrower": "the affine maps are tied to square translations from the same t-box, not arbitrary affine maps",
    }

    rows = [
        row(
            "AffineSquareSetTargetActive",
            active,
            True,
            "上一证书已把剩余压成短平方集的非平凡仿射自交能量。",
            TARGET,
        ),
        row(
            "SlopeParameterizationClosed",
            slope_conic_closed,
            True,
            "令 `lambda=u/x` 后，仿射平移项强制等于 `lambda(lambda-1)x^2`。",
            NEXT_ATOM,
        ),
        row(
            "ConicBundleIdentityClosed",
            slope_conic_closed,
            True,
            "剩余自交等价嵌入斜率局部二次曲线束 `d2^2=lambda d1^2+lambda(lambda-1)x^2`。",
            NEXT_ATOM,
        ),
        row(
            "NontrivialSlopesNonsingular",
            nonsingular_closed,
            True,
            "`lambda` 不为 `0,1` 时二次型非退化；已排除恒等/零斜率退化。",
            CONIC_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明该局部斜率二次曲线束的总解数固定幂节省。",
            CONIC_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只把仿射自交族缩成斜率二次曲线束，未证明曲线束估计。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_slope_conic_bundle_router",
        "status": "affine_square_set_frontier_reduced_to_nontrivial_slope_localized_conic_bundle",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "affine_square_set_target_active": active,
        "slope_parameterization_closed": slope_conic_closed,
        "conic_bundle_identity_closed": slope_conic_closed,
        "nontrivial_slopes_nonsingular": nonsingular_closed,
        "slope_conic_bundle_power_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": CONIC_ATOM,
        "conic_bundle": conic_bundle,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "仿射平方集自交族还能继续缩窄。斜率 `lambda=u/x` 一旦固定，"
            "平移项不是自由参数，而是 `lambda(lambda-1)x^2`。"
            "因此剩余等价嵌入非平凡斜率上的局部二次曲线束 "
            "`d2^2=lambda*d1^2+lambda(lambda-1)*x^2`，并带有 `x,lambda*x in T` 的根盒限制。"
            "下一唯一内部输入是该非退化曲线束的总解数固定幂节省。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    bundle = result["conic_bundle"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 斜率二次曲线束前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"conic_bundle_identity_closed={fmt_bool(result['conic_bundle_identity_closed'])}",
        f"slope_conic_bundle_power_saving_proved={fmt_bool(result['slope_conic_bundle_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 斜率曲线束正规形",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in bundle.items():
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
