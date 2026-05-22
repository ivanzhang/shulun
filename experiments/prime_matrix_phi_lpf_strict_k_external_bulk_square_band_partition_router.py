#!/usr/bin/env python3
"""生成 strict-k 外部 bulk 覆盖与平方边界带分区证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_external_bulk_square_band_partition_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-external-bulk-square-band-partition-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-external-bulk-square-band-partition-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-external-bulk-square-band-partition-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-external-bulk-square-band-partition-router.md
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-external-bulk-square-band-partition"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

FINITE_SQRT_X_MAX = 10**18
DUSART_X_MIN = 396_738
BHP_THETA = Fraction(21, 40)
BHP_K_EXPONENT = (1 - BHP_THETA) / BHP_THETA

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json",
    DOCS / "prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow-router.json",
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


def dusart_cap_for_p(p_scale: int) -> int:
    """计算样本 P 下 Dusart 显式窗口可直接覆盖的最大 k。

    条件是 kP>DUSART_X_MIN 且 k <= 25 log(kP)^2。函数只用于尺度审计。
    """
    if p_scale <= 2:
        return 0
    lo = 2
    hi = p_scale - 1
    if lo * p_scale <= DUSART_X_MIN:
        lo = max(lo, DUSART_X_MIN // p_scale + 1)
    if lo > hi:
        return 0

    def ok(k_value: int) -> bool:
        x_value = k_value * p_scale
        return x_value > DUSART_X_MIN and k_value <= 25.0 * math.log(x_value) ** 2

    if not ok(lo):
        return 0
    if ok(hi):
        return hi
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if ok(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


def scale_samples() -> list[dict[str, Any]]:
    """生成外部覆盖分区的尺度样本。"""
    samples: list[dict[str, Any]] = []
    for p_scale in [10**9, 10**12, 10**18, 10**24]:
        bhp_bulk_cap = int(p_scale ** float(BHP_K_EXPONENT))
        dusart_cap = dusart_cap_for_p(p_scale)
        finite_sqrt_cap = min(p_scale - 1, FINITE_SQRT_X_MAX // p_scale)
        samples.append(
            {
                "P_scale": p_scale,
                "finite_sqrt_k_cap_from_x_le_1e18": finite_sqrt_cap,
                "dusart_explicit_log_band_k_cap": dusart_cap,
                "bhp_asymptotic_bulk_k_cap_constant_one": bhp_bulk_cap,
                "bhp_bulk_fraction": bhp_bulk_cap / p_scale,
                "bhp_remaining_top_band_size": max(0, p_scale - 1 - bhp_bulk_cap),
                "bhp_remaining_top_band_fraction": max(0.0, (p_scale - 1 - bhp_bulk_cap) / p_scale),
            }
        )
    return samples


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "PhiLPFEndpointDifferenceImportedForAllStrictRows",
            True,
            True,
            "对 1<k<P，Phi-LPF 端点差分已经给出 N_P(k)=pi((k+1)P-1)-pi(kP) 的精确计数对象。",
            "positivity source still needed",
        ),
        row(
            "FiniteSqrtInitialSegmentClosed",
            True,
            True,
            "已接入有限 sqrt-gap 输入：kP<=10^18 的 strict 行由外部有限引理和小 x 直接核查覆盖。",
            "x>10^18",
        ),
        row(
            "DusartExplicitLogBandPartitionClosed",
            True,
            True,
            "Dusart 2010 的显式区间可覆盖 k<=25 log^2(kP) 的低 k 带；这是可验证 log-band，不触及顶端平方边界。",
            "k beyond explicit logarithmic band",
        ),
        row(
            "BHPAsymptoticBulkBandPartitionClosed",
            True,
            True,
            "Baker--Harman--Pintz 的 x^(21/40) 短区间若用于 x=kP，则覆盖 k<=P^(19/21) 的 bulk 子带。",
            "asymptotic threshold and high-k band",
        ),
        row(
            "RemainingRowsForcedIntoHighKSquareBand",
            True,
            True,
            "排除有限 sqrt 初段、Dusart log-band 和 BHP bulk 后，任何剩余反例必须满足 x>10^18 且 P^(19/21)<k<P。",
            "P^(19/21)<k<P, especially top row k=P-1",
        ),
        row(
            "TopBandConvertedToHalfRoughSemiprimeShadow",
            True,
            True,
            "顶行 k=P-1 已进一步化为 R_{1/2}(P)>T_{1/2}(P) 的 half-rough semiprime-shadow excess。",
            "general high-k band still needs analogous excess",
        ),
        row(
            "HighKSquareBandPositivityProved",
            False,
            False,
            "尚未证明高 k 平方边界带的 Phi-LPF 端点差分恒为正，也未证明 top-row half-rough excess 的全局下界。",
            "HighKSquareBandPhiLPFExcess OR HalfRoughSurvivorExcessOverReciprocalSemiprimeShadow",
        ),
        row(
            "UnifiedPositiveCoreProved",
            False,
            False,
            "本层是分区和剩余定位，不是三目标命题的无条件闭合。",
            "sqrt-scale theorem, high-k structural excess, or semiprime-shadow PDEC exclusion",
        ),
    ]


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出判定表 Markdown。"""
    lines = ["| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def sample_markdown(samples: list[dict[str, Any]]) -> str:
    """输出尺度样本 Markdown。"""
    lines = [
        "| P scale | finite sqrt k cap | Dusart k cap | BHP k cap | BHP bulk fraction | remaining top fraction |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in samples:
        lines.append(
            f"| {item['P_scale']} | {item['finite_sqrt_k_cap_from_x_le_1e18']} | "
            f"{item['dusart_explicit_log_band_k_cap']} | "
            f"{item['bhp_asymptotic_bulk_k_cap_constant_one']} | "
            f"{item['bhp_bulk_fraction']:.6e} | "
            f"{item['bhp_remaining_top_band_fraction']:.6e} |"
        )
    return "\n".join(lines)


def build_payload() -> dict[str, Any]:
    """生成证书 payload。"""
    rows = build_rows()
    samples = scale_samples()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "status": "strict_k_external_bulk_covered_remaining_forced_to_high_k_square_band",
        "interval": {
            "x": "kP",
            "target": "pi((k+1)P-1)-pi(kP)>0",
            "strict_range": "1<k<P",
            "Phi_LPF_role": "exact endpoint count; positivity must come from an external short interval theorem or internal excess",
        },
        "external_inputs": [
            {
                "name": "finite sqrt-gap input",
                "source": "https://link.springer.com/article/10.1007/s00208-023-02574-1 Lemma 2.7; uses Oliveira e Silva--Herzog--Pardi prime-gap computation, https://doi.org/10.1090/S0025-5718-2013-02787-1",
                "usable_range": "117<=x<=10^18, plus direct small-x audit in the repository",
                "strict_k_effect": "closes every strict row with kP<=10^18",
            },
            {
                "name": "Dusart 2010",
                "source": "https://arxiv.org/abs/1002.0442",
                "usable_statement": "for x>396738, an interval of length x/(25 log^2 x) suffices",
                "strict_k_effect": "covers k<=25 log^2(kP)",
            },
            {
                "name": "Baker--Harman--Pintz 2001",
                "source": "https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/difference-between-consecutive-primes-ii/2EF13261B3B25458A25F41ED74AA2FC2",
                "usable_statement": "for sufficiently large x, [x,x+x^(21/40)] contains primes",
                "strict_k_effect": "with constant-one exponent arithmetic, covers k<=P^(19/21); threshold is asymptotic, not an explicit finite ledger",
            },
        ],
        "bhp_theta": fraction_text(BHP_THETA),
        "bhp_strict_k_exponent": fraction_text(BHP_K_EXPONENT),
        "samples": samples,
        "gates": rows,
        "dependency_hashes": dependency_hashes,
        "plain_conclusion": (
            "Phi-LPF 端点差分已经能精确计算 [kP,kP+P] 的素数个数；外部引理路线现在被分成三块："
            "有限 sqrt 初段、Dusart 显式 log-band、BHP 渐近 bulk。它们之后的真剩余不是全域未知，"
            "而是 x>10^18 且 P^(19/21)<k<P 的平方边界高 k 带；顶行已经进一步压成 half-rough "
            "semiprime-shadow excess。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF strict-k external bulk square-band partition 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "本层把 `[kP,kP+P]`、`1<k<P` 的 Phi-LPF 端点差分与三个外部输入统一成一个分区账本。",
        "端点差分本身是精确计数；正性来源只能来自外部短区间输入，或来自内部 LPF/平方相位 excess。",
        "",
        "```text",
        "N_P(k)=pi((k+1)P-1)-pi(kP).",
        "```",
        "",
        "## 1. 外部输入适配",
        "",
        "- 有限 sqrt-gap 输入：`kP<=10^18` 的 strict 行已经由已接入的 Lemma 2.7 与小 `x` 审计覆盖。",
        "- Dusart 2010：`x>396738` 时长度 `x/(25 log^2 x)` 可用，在 strict 行中只覆盖 `k<=25 log^2(kP)`。",
        "- Baker--Harman--Pintz 2001：充分大 `x` 时长度 `x^(21/40)` 可用；代入 `x=kP` 得",
        "",
        "```text",
        "P >= (kP)^(21/40)  iff  k <= P^(19/21).",
        "```",
        "",
        "因此 BHP 能给渐近 bulk 子带，但仍留下 `P^(19/21)<k<P` 的顶端平方边界带。",
        "",
        "## 2. 尺度样本",
        "",
        sample_markdown(payload["samples"]),
        "",
        "## 3. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 4. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "换言之，继续走外部引理路线必须拿到真正 `sqrt(x)` 尺度且常数不超过 1 的无条件短区间定理；",
        "否则就必须在高 `k` 平方边界带内部证明 Phi-LPF excess，顶行最窄形式就是",
        "`R_{1/2}(P)>T_{1/2}(P)`。",
        "",
        "本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它只把真剩余定位到更窄的",
        "高 `k` 平方边界带与 half-rough semiprime-shadow excess。",
        "",
        "## 5. 外部来源",
        "",
        "| input | source | repository use |",
        "| --- | --- | --- |",
    ]
    for item in payload["external_inputs"]:
        lines.append(f"| {cell(item['name'])} | {cell(item['source'])} | {cell(item.get('strict_k_effect', item.get('usable_range', '')))} |")
    lines.extend(
        [
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in payload["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(
        json.dumps(
            {
                "status": payload["status"],
                "bhp_strict_k_exponent": payload["bhp_strict_k_exponent"],
                "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
