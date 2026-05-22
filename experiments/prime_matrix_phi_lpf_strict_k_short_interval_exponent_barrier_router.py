#!/usr/bin/env python3
"""生成 1<k<P Phi-LPF 行端点差分的短区间指数屏障证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_short_interval_exponent_barrier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.md
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json",
    DOCS / "prime-matrix-strict-brun-titchmarsh-short-interval-input-router.json",
]


THETA_CASES = [
    ("theta_0_525", Fraction(21, 40), "Baker-Harman-Pintz 型 theta=0.525 量级"),
    ("theta_0_51", Fraction(51, 100), "任意固定 theta=0.51 示例"),
    ("theta_0_5001", Fraction(5001, 10000), "非常接近 1/2 的 theta=0.5001 示例"),
    ("theta_0_5", Fraction(1, 2), "平方根尺度 theta=1/2 临界口径"),
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
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


def fraction_text(value: Fraction) -> str:
    """格式化分数。"""
    return f"{value.numerator}/{value.denominator}"


def decimal_text(value: Fraction, digits: int = 12) -> str:
    """用固定精度显示分数。"""
    return f"{float(value):.{digits}f}"


def theta_row(name: str, theta: Fraction, label: str) -> dict[str, Any]:
    """计算短区间指数 theta 对 strict k<P 行可覆盖的 k 指数。"""
    if theta <= 0 or theta >= 1:
        raise ValueError("theta 必须在 (0,1) 内")
    if theta > Fraction(1, 2):
        covered_k_exponent = (1 - theta) / theta
        asymptotic_all_rows_covered = False
        top_band_remains = True
        needed_statement = "theta<=1/2, or a separate structural top-band argument"
    elif theta == Fraction(1, 2):
        covered_k_exponent = Fraction(1, 1)
        asymptotic_all_rows_covered = True
        top_band_remains = False
        needed_statement = "sqrt-scale interval with constant <=1"
    else:
        covered_k_exponent = Fraction(1, 1)
        asymptotic_all_rows_covered = True
        top_band_remains = False
        needed_statement = "stronger than sqrt-scale"
    return {
        "name": name,
        "label": label,
        "theta_fraction": fraction_text(theta),
        "theta_decimal": decimal_text(theta),
        "covered_k_exponent_fraction": fraction_text(covered_k_exponent),
        "covered_k_exponent_decimal": decimal_text(covered_k_exponent),
        "condition_constant_one": (
            "P >= (kP)^theta iff k <= P^((1-theta)/theta)"
            if theta > Fraction(1, 2)
            else "P >= sqrt(kP) covers all strict k<P when the constant is <=1"
        ),
        "asymptotic_all_strict_k_rows_covered": asymptotic_all_rows_covered,
        "top_band_k_near_p_remains": top_band_remains,
        "needed_statement": needed_statement,
    }


def sample_rows() -> list[dict[str, Any]]:
    """生成样本 P 下的覆盖比例；仅作尺度审计，不作证明输入。"""
    samples: list[dict[str, Any]] = []
    for p_size in [10**6, 10**12, 10**24]:
        for name, theta, _label in THETA_CASES[:3]:
            exponent = (1 - theta) / theta
            covered_estimate = p_size ** float(exponent)
            total = p_size
            samples.append(
                {
                    "P_scale": p_size,
                    "theta_name": name,
                    "covered_k_approx": int(covered_estimate),
                    "total_strict_k_approx": total,
                    "covered_fraction_approx": covered_estimate / total,
                    "uncovered_fraction_approx": 1 - (covered_estimate / total),
                }
            )
    return samples


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "PhiLPFStrictKEndpointDifferenceAlreadyClosed",
            True,
            True,
            "Phi-LPF 已给出 [kP,kP+P] 与内部行的精确端点差分。",
            "use as exact count, not positivity",
        ),
        row(
            "ThetaGreaterThanHalfCoversOnlyLowK",
            True,
            True,
            "若外部输入只保证 [x,x+C x^theta] 内有素数且 theta>1/2，则常数不改覆盖指数。",
            "k <= const * P^((1-theta)/theta)",
        ),
        row(
            "FiniteVerificationPlusThetaGreaterThanHalfCannotCloseAllLargeP",
            True,
            True,
            "任何固定 theta>1/2 留下随 P 增长的顶端 k 带；有限验证不能覆盖无限顶端带。",
            "top band k near P",
        ),
        row(
            "SquareRootScaleInputIdentifiedAsNecessaryForThisLane",
            True,
            True,
            "要靠纯短区间输入覆盖所有 1<k<P，至少需要 sqrt(x) 尺度且常数不超过 1。",
            "Legendre-scale or structural substitute",
        ),
        row(
            "SquareRootScaleInputAvailableInCurrentCorpus",
            False,
            False,
            "当前语料没有无条件 sqrt-scale strict row 素数输入。",
            "PositiveRejectionExcess or external Legendre-scale theorem",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层关闭的是阈值+有限验证路线的指数适配，不是行/列命题。",
            "signed/transport strict imbalance or square-root interval theorem",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    theta_rows = [theta_row(name, theta, label) for name, theta, label in THETA_CASES]
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path) for path in DEPENDENCIES if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_strict_k_short_interval_exponent_barrier_router",
        "status": "strict_k_phi_lpf_endpoint_difference_short_interval_exponent_barrier_closed",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "strict_k_range": "1<k<P",
        "interval": "[kP,kP+P]",
        "endpoint_difference_available": True,
        "theta_greater_than_half_barrier_proved": True,
        "finite_verification_plus_theta_gt_half_cannot_close_all_large_p": True,
        "sqrt_scale_input_needed_for_pure_short_interval_lane": True,
        "sqrt_scale_input_available_in_current_corpus": False,
        "positive_rejection_excess_proved": False,
        "row_column_unconditional_closed": False,
        "main_calculation": "P >= C*(kP)^theta implies k <= C^(-1/theta)*P^((1-theta)/theta)",
        "theta_rows": theta_rows,
        "sample_scale_rows": sample_rows(),
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "Phi-LPF 端点差分可以精确给出 strict 1<k<P 行的素数个数，但若尝试用"
            "充分大阈值后的普通短区间素数定理来直接推出正性，任何 theta>1/2 的长度"
            "只覆盖低 k<=P^((1-theta)/theta)；顶端 k 接近 P 的无限带仍未覆盖。"
            "因此该路线要完全闭合，必须输入 sqrt-scale 常数<=1 的短区间定理，"
            "或者回到 raw/rejection 的结构性严格失衡证明。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF strict k short interval exponent barrier 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. 指数适配计算",
        "",
        "对 `x=kP`，strict 行目标需要在长度 `P` 内得到素数。若外部定理只给出",
        "`[x, x + C x^theta]` 内有素数，则必须满足：",
        "",
        "```text",
        result["main_calculation"],
        "```",
        "",
        "常数 `C` 只改变前因子；当 `theta>1/2` 时，指数 `(1-theta)/theta<1`，",
        "所以只覆盖 `k` 的低幂次段，不能覆盖全部 `1<k<P`。",
        "",
        "## 2. theta 对照表",
        "",
        "| name | theta | covered k exponent | all strict k covered | top band remains | needed |",
        "| --- | ---: | ---: | --- | --- | --- |",
    ]
    for item in result["theta_rows"]:
        lines.append(
            f"| `{cell(item['name'])}` | `{item['theta_decimal']}` | "
            f"`{item['covered_k_exponent_decimal']}` | "
            f"`{fmt_bool(item['asymptotic_all_strict_k_rows_covered'])}` | "
            f"`{fmt_bool(item['top_band_k_near_p_remains'])}` | {cell(item['needed_statement'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 尺度样本",
            "",
            "| P scale | theta | covered k approx | covered fraction | uncovered fraction |",
            "| ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for item in result["sample_scale_rows"]:
        lines.append(
            f"| {item['P_scale']} | `{item['theta_name']}` | {item['covered_k_approx']} | "
            f"{item['covered_fraction_approx']:.6e} | {item['uncovered_fraction_approx']:.6e} |"
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 5. 结论",
            "",
            "这层不是否定 Phi-LPF 端点差分；相反，它说明端点差分已经足够精确，问题只剩正性来源。",
            "若正性来源选用“充分大阈值以上的短区间素数存在 + 有限验证”，则任意 `theta>1/2`",
            "都会留下无限顶端带 `P^((1-theta)/theta) < k < P`。因此有限验证只能处理固定初段，",
            "不能替代顶端带的一般证明。下一步必须二选一：提交 sqrt-scale 常数 `<=1` 的外部/内部输入，",
            "或证明上一层的 `PositiveRejectionExcessForStrictKRawLPFIncidence`。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 ledger、JSON 与 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
