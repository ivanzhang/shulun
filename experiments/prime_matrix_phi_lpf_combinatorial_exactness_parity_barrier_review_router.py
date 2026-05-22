#!/usr/bin/env python3
"""生成 Phi-LPF 组合精确性与奇偶屏障评审吸收证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_combinatorial_exactness_parity_barrier_review_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-combinatorial-exactness-parity-barrier-review-router.json

输出：
  data/prime-matrix-phi-lpf-combinatorial-exactness-parity-barrier-review-ledger.json
  docs/monograph/prime-matrix-phi-lpf-combinatorial-exactness-parity-barrier-review-router.json
  docs/monograph/prime-matrix-phi-lpf-combinatorial-exactness-parity-barrier-review-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-combinatorial-exactness-parity-barrier-review"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-difference-router.json",
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-parity-capacity-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.json",
    DOCS / "prime-matrix-prime-base-exponent-half-barrier-router.json",
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


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def route(name: str, status: str, required_input: str, verdict: str) -> dict[str, str]:
    """构造路线判定。"""
    return {
        "route": name,
        "status": status,
        "required_input": required_input,
        "verdict": verdict,
    }


def build_gates() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        gate(
            "PhiLPFCombinatorialExactnessAccepted",
            True,
            True,
            "LPF 分桶和 Phi 端点差给出精确等式，不含误差项。",
            "positivity not included",
        ),
        gate(
            "ExactIdentityDoesNotImplyPositiveLowerBound",
            True,
            True,
            "从 exact count 表达式推出 >=1 需要额外下界，不是代数化简。",
            "positive source required",
        ),
        gate(
            "LinearSieveParityBarrierRecognized",
            True,
            True,
            "在 H=P、z≈P 的 strict 顶端带，自然线性筛 level 参数不超过临界区，lower sieve 不给正下界。",
            "requires non-sieve parity breaking input",
        ),
        gate(
            "ThetaGreaterThanHalfShortIntervalRouteRejectedAsClosure",
            True,
            True,
            "0.525 或 0.52 级短区间定理代入 X≈P^2 后仍长于 P，不能闭合 k≈P。",
            "sqrt-scale or structural substitute",
        ),
        gate(
            "ParityCapacityLayerClassifiedAsNarrowingNotProof",
            True,
            True,
            "奇偶容量扣除是真正上界改进，但剩余正性仍是 prime-pair saturation/奇偶屏障口。",
            "PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC",
        ),
        gate(
            "UnconditionalTargetClosureReached",
            False,
            False,
            "评审吸收后仍未得到三目标命题无条件闭合。",
            "LegendreScaleInput OR structural signed/dispersion/PDEC contradiction",
        ),
    ]


def build_routes() -> list[dict[str, str]]:
    """列出后续可继续硬攻的非循环路线。"""
    return [
        route(
            "External sqrt-scale short interval input",
            "open_external",
            "对所有相关 x=kP 给出长度 <=P≈sqrt(x) 的素数存在或计数下界。",
            "这等同于 Legendre-scale 输入；当前语料和通用外部定理没有给出。",
        ),
        route(
            "Special square-phase/CRT structural lower bound",
            "open_internal",
            "利用 P 为素数、端点相位 -P^2 mod q、reciprocal forest 的特殊结构证明 DeltaPhi_half>C_par。",
            "这是当前最有价值的自足方向；必须产生新分布/相关性信息，不能只重排 LPF 恒等式。",
        ),
        route(
            "Signed transport / dispersion source route",
            "open_internal_or_external",
            "提交 pointwise signed coefficient 表、Type-II/DI-BFI/Kloosterman 型取消，或把失败转成 PDEC/SAE。",
            "若能给出真正带符号取消，它可以绕过线性筛奇偶屏障。",
        ),
        route(
            "Finite verification after theta>1/2",
            "rejected_as_global_closure",
            "固定阈值以下全验证，上方引用 theta>1/2 短区间。",
            "仍留下无限顶端带，不能作为闭合路线。",
        ),
        route(
            "Capacity-only LPF/Phi rewriting",
            "rejected_as_global_closure",
            "继续把同一个 exact count 改写为新的无符号容量表达式。",
            "只能缩小剩余口；若没有新正性来源，就是同一奇偶屏障改名。",
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


def routes_markdown(routes: list[dict[str, str]]) -> str:
    """输出路线表 Markdown。"""
    lines = ["| route | status | required input | verdict |", "| --- | --- | --- | --- |"]
    for item in routes:
        lines.append(
            f"| {cell(item['route'])} | `{cell(item['status'])}` | "
            f"{cell(item['required_input'])} | {cell(item['verdict'])} |"
        )
    return "\n".join(lines)


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_combinatorial_exactness_parity_barrier_review_router",
        "status": "review_absorbed_phi_lpf_exactness_is_not_positivity",
        "review_core_verdict": {
            "accepted": True,
            "numeric_update": "BHP 0.525 has a newer 0.52 arXiv refinement, but both remain >1/2.",
            "main_correction": "Phi-LPF exactness is combinatorial exactness; positivity needs independent lower-bound/cancellation input.",
        },
        "barrier_geometry": {
            "strict_interval": "[kP,(k+1)P]",
            "worst_edge": "k≈P, x=kP≈P^2, target length P≈sqrt(x)",
            "lpf_sieve_scale": "sieving threshold z≈P/2 to P",
            "linear_sieve_issue": "available unsigned lower-bound level is at or below the parity-critical range; lower sieve gives no positive prime lower bound.",
        },
        "current_frontier_after_review": (
            "PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC"
        ),
        "gates": build_gates(),
        "routes": build_routes(),
        "external_source_notes": [
            {
                "name": "Baker-Harman-Pintz 2001",
                "fact": "[x,x+x^0.525] contains a prime for sufficiently large x.",
                "url": "https://doi.org/10.1112/plms/83.3.532",
            },
            {
                "name": "Runbo Li 2025 arXiv v8",
                "fact": "[x-x^0.52,x] contains primes for sufficiently large x, according to the arXiv abstract.",
                "url": "https://arxiv.org/abs/2308.04458",
            },
            {
                "name": "linear sieve lower function",
                "fact": "standard lower-bound function f(s) is zero in the initial parity-critical range.",
                "url": "https://www.sciencedirect.com/science/article/pii/S0022314X17303189",
            },
        ],
        "dependency_hashes": dependency_hashes,
        "plain_conclusion": (
            "评审结论应被吸收为硬约束：Phi-LPF/LPF 桶恒等式是组合精确，不是正性定理。"
            "刚生成的 parity capacity 证书是有效的非循环压缩，因为它把 forest holes 上界从整数窗"
            "压到奇偶窗；但它仍没有突破 Bombieri 奇偶屏障。当前真正剩余应表述为 "
            "DeltaPhi_half(P,k)>C_par(P,k) 的特殊 square-phase/reciprocal-forest 下界，"
            "或失败时的 reciprocal prime-pair saturation PDEC。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF 组合精确性与奇偶屏障评审吸收证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 评审结论",
        "",
        payload["plain_conclusion"],
        "",
        "需要修正的一点是数值前沿：Baker--Harman--Pintz 的 `0.525` 已有 Runbo Li",
        "`0.52` 级 arXiv 更新；但 `0.52>1/2`，所以对本项目的平方根尺度硬点没有本质改变。",
        "",
        "## 2. 屏障几何",
        "",
        "```text",
        f"strict_interval={payload['barrier_geometry']['strict_interval']}",
        f"worst_edge={payload['barrier_geometry']['worst_edge']}",
        f"lpf_sieve_scale={payload['barrier_geometry']['lpf_sieve_scale']}",
        f"linear_sieve_issue={payload['barrier_geometry']['linear_sieve_issue']}",
        "```",
        "",
        "因此，继续把 `N_P(k)` 改写成新的无符号 LPF/Phi 容量账本不会自动产生正性。",
        "正性必须来自以下之一：平方根尺度短区间输入、特殊 square-phase 结构下界、",
        "或真正带符号的 dispersion/transport 取消。",
        "",
        "## 3. 路线判定",
        "",
        routes_markdown(payload["routes"]),
        "",
        "## 4. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 5. 当前最窄口",
        "",
        "```text",
        payload["current_frontier_after_review"],
        "```",
        "",
        "本证书不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它防止把组合恒等式误读为",
        "正性证明，并把之后的硬攻方向限制到真正可能越过奇偶屏障的输入。",
        "",
        "## 6. 外部来源记录",
        "",
        "| name | fact | url |",
        "| --- | --- | --- |",
    ]
    for item in payload["external_source_notes"]:
        lines.append(f"| {cell(item['name'])} | {cell(item['fact'])} | {item['url']} |")
    lines.extend(
        [
            "",
            "## 7. 依赖哈希",
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
                "accepted_review_core": payload["review_core_verdict"]["accepted"],
                "current_frontier_after_review": payload["current_frontier_after_review"],
                "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
