#!/usr/bin/env python3
"""生成 strict-k 行正性外部短区间引理桥接证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_external_gap_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-external-gap-bridge-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-external-gap-bridge"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-smooth-owner-quotient-window-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-beatty-euclidean-source-window-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化成小写文本。"""
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


def sample_bridge_rows() -> list[dict[str, Any]]:
    """给出代表性 strict 边界样本的外部引理覆盖读数。"""
    samples = [
        (101, 100),
        (1009, 1008),
        (10007, 10006),
        (1000003, 1000002),
    ]
    rows: list[dict[str, Any]] = []
    for p_len, k in samples:
        x = k * p_len
        dusart_h = x / (25.0 * math.log(x) ** 2)
        bhp_h = x**0.525
        dusart_band = k <= 25.0 * math.log(x) ** 2
        rows.append(
            {
                "P": p_len,
                "k": k,
                "x": x,
                "P_over_sqrt_x": p_len / math.sqrt(x),
                "dusart_threshold_x_gt_396738": x > 396738,
                "dusart_band_condition_k_le_25log2x": dusart_band,
                "dusart_direct_coverage": x > 396738 and dusart_band,
                "dusart_H_over_P": dusart_h / p_len,
                "bhp_condition_k_le_x_0_475": k <= x**0.475,
                "bhp_H_over_P": bhp_h / p_len,
            }
        )
    return rows


def build_rows() -> list[dict[str, Any]]:
    """生成外部引理桥接判定表。"""
    return [
        row(
            "PhiLPFDualWindowValueImported",
            True,
            True,
            "上一层已把 strict 行素数个数写成 N_P(k)=(P-1)-B_P(k)-S_P(k)。",
            "dual value imported",
        ),
        row(
            "ExternalIntervalLemmaBridgeCriterionClosed",
            True,
            True,
            "任一外部引理 prime in [x,x+H(x)] 可用于 x=kP 当且仅当 H(kP)<=P。",
            "bridge criterion",
        ),
        row(
            "Dusart2010CoversLogBandOnly",
            True,
            True,
            "Dusart 的显式区间给 H=x/(25 log^2 x)，只覆盖 k<=25 log^2(kP) 的子带。",
            "k beyond logarithmic band",
        ),
        row(
            "BakerHarmanPintzCoversExponent0475BandOnly",
            True,
            True,
            "BHP 的 x^0.525 区间只覆盖 k<=x^0.475；strict 边界允许 k 接近 x^0.5。",
            "sqrt-edge band",
        ),
        row(
            "KnownExternalGapBoundsCloseAllStrictRows",
            False,
            False,
            "当前接入的无条件外部短区间引理不能覆盖 k≈P≈sqrt(x) 的最坏边界。",
            "sqrt-scale or dual-window anti-tiling input",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层明确外部引理的可用范围，没有证明 strict 行正性。",
            "DualWindowAntiTilingInequality OR SqrtGapInputAfterX",
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
    """输出样本表 Markdown。"""
    lines = [
        "| P | k | P/sqrt(x) | Dusart H/P | Dusart covers | BHP H/P | BHP covers |",
        "| ---: | ---: | ---: | ---: | --- | ---: | --- |",
    ]
    for item in samples:
        lines.append(
            f"| {item['P']} | {item['k']} | {item['P_over_sqrt_x']:.9f} | "
            f"{item['dusart_H_over_P']:.6f} | "
            f"`{fmt_bool(item['dusart_direct_coverage'])}` | "
            f"{item['bhp_H_over_P']:.6f} | "
            f"`{fmt_bool(item['bhp_condition_k_le_x_0_475'])}` |"
        )
    return "\n".join(lines)


def build_payload() -> dict[str, Any]:
    """生成证书 payload。"""
    samples = sample_bridge_rows()
    rows = build_rows()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "status": "external_gap_lemmas_screened_against_strict_k_interval",
        "strict_interval": {
            "x": "x=kP",
            "length": "P=x/k",
            "strict_range": "1<k<P, hence P>sqrt(x) but can be arbitrarily close to sqrt(x)",
            "bridge_criterion": "prime in [x,x+H(x)] implies row positivity when H(x)<=P",
        },
        "external_sources": [
            {
                "name": "Dusart 2010",
                "url": "https://arxiv.org/abs/1002.0442",
                "used_fact": "for x>396738, [x, x+x/(25 log^2 x)] contains at least one prime",
                "strict_k_coverage": "k<=25 log^2(kP)",
            },
            {
                "name": "Baker-Harman-Pintz 2001",
                "url": "https://doi.org/10.1112/plms/83.3.532",
                "used_fact": "for large x, [x, x+x^0.525] contains a prime",
                "strict_k_coverage": "k<=x^0.475, not all k<sqrt(x)",
            },
        ],
        "sample_bridge_rows": samples,
        "gates": rows,
        "dependency_hashes": dependency_hashes,
        "plain_conclusion": (
            "外部短区间引理可精确桥接到 Phi-LPF strict 行：只要 H(kP)<=P，"
            "端点差 N_P(k) 就为正。Dusart 2010 给显式 log-band，BHP 2001 给"
            "指数 0.475 的 k-band；二者都不能覆盖 k 接近 P 的 sqrt-edge。"
            "因此当前真剩余是 sqrt-scale 输入或内部双窗口反铺满不等式。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF strict k external gap bridge 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "设 `x=kP`。目标区间为 `[kP,kP+P]`，内部槽长度为 `P-1`。",
        "任一外部短区间引理若保证 `[x,x+H(x)]` 内有素数，则在 strict 行中可用的充要桥接条件是：",
        "",
        "```text",
        "H(kP) <= P = x/k.",
        "```",
        "",
        "## 1. 外部引理筛查",
        "",
        "- Dusart 2010: `x>396738` 时 `[x,x+x/(25 log^2 x)]` 有素数，桥接条件为 `k<=25 log^2(kP)`。",
        "- Baker-Harman-Pintz 2001: 充分大 `x` 时 `[x,x+x^0.525]` 有素数，桥接条件为 `k<=x^0.475`。",
        "",
        "strict 条件只给 `k<P`，即 `k<sqrt(x)`。所以 BHP 的 `0.475` 指数仍低于最坏边界 `0.5`，",
        "Dusart 的显式相对界只覆盖对数宽的低 `k` 子带。",
        "",
        "## 2. 边界样本",
        "",
        sample_markdown(payload["sample_bridge_rows"]),
        "",
        "## 3. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 4. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "这不是负结论，而是精确定位：若继续走外部引理路线，需要 Legendre 强度的",
        "`H(x)<=sqrt(x)` 右侧短区间输入并配合有限验证；否则必须从 Phi-LPF 双窗口",
        "`B_P(k)+S_P(k)<=P-2` 的内部反铺满结构突破。",
        "",
        "## 5. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
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
    print(f"wrote {OUT_LEDGER}")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
