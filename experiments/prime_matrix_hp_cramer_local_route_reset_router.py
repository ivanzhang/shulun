#!/usr/bin/env python3
"""生成 H_P/Cramér-local 路线重置证书。

用法示例：
  python3 experiments/prime_matrix_hp_cramer_local_route_reset_router.py
  python3 -m json.tool docs/monograph/prime-matrix-hp-cramer-local-route-reset-router.json

输出：
  data/prime-matrix-hp-cramer-local-route-reset-ledger.json
  docs/monograph/prime-matrix-hp-cramer-local-route-reset-router.json
  docs/monograph/prime-matrix-hp-cramer-local-route-reset-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-hp-cramer-local-route-reset"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-combinatorial-exactness-parity-barrier-review-router.json",
    DOCS / "prime-matrix-phi-lpf-punctured-endpoint-parity-capacity-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.json",
    DOCS / "prime-matrix-prime-base-exponent-half-barrier-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-nogo-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-variable-translation-router.json",
    DOCS / "prime-matrix-strict-structured-ehpd-final-interface-audit-router.json",
    DOCS / "external-theorem-index.md",
    ROOT / "docs" / "generalized_framework.md",
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


def route(name: str, status: str, role: str, risk: str, next_action: str) -> dict[str, str]:
    """构造路线表行。"""
    return {
        "route": name,
        "status": status,
        "role": role,
        "risk": risk,
        "next_action": next_action,
    }


def build_gates() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        gate(
            "HPRecognizedAsCramerLocalScale",
            True,
            True,
            "strict 顶端带 k≈P 等价于 x≈P^2 后长度 P≈sqrt(x) 的局部素数存在问题。",
            "not closed by Phi-LPF exactness",
        ),
        gate(
            "PhiLPFEratosthenesEquivalenceClassDemotedToReductionLibrary",
            True,
            True,
            "LPF/Phi/Eratosthenes 型公式保留为精确 reduction，不再被标为正性闭合。",
            "positive input required",
        ),
        gate(
            "CapacityOnlyRenamingRejectedAsClosure",
            True,
            True,
            "继续重排无符号桶、窗口、孔容量只是在等价类内移动未证口。",
            "parity barrier",
        ),
        gate(
            "FiniteVerificationPlusKnownThetaGtHalfRejected",
            True,
            True,
            "有限验证配合 0.525 或 0.52 级短区间定理仍留下无限 k≈P 顶端带。",
            "sqrt-scale theorem needed",
        ),
        gate(
            "ExistingFIMaynardAutomorphicSourcesDoNotDirectlyCloseHP",
            True,
            True,
            "FI/DI/BFI/Maynard/自守工具是可攻技术族；现有仓库没有 ready-made theorem 覆盖 H_P 主命题。",
            "exact theorem-match or new theorem",
        ),
        gate(
            "UnconditionalHPClosureClaimAllowed",
            False,
            False,
            "当前数学和当前仓库都不允许宣称 H_P 主命题无条件闭合。",
            "ExternalSqrtScaleOrNewDispersionAutomorphicInput",
        ),
    ]


def build_routes() -> list[dict[str, str]]:
    """列出重置后的路线优先级。"""
    return [
        route(
            "Route A: exact external theorem-match",
            "primary",
            "把 H_P 需要的对象写成精确可引用定理：sqrt-scale short interval 或 full-S non-AP WFD KLS/dispersion。",
            "高；多数现有定理只给平均或 AP/平滑/投影版本，未必匹配。",
            "建立 theorem-match checklist：变量、权重、模数范围、窗口、投影、误差保存逐项验收。",
        ),
        route(
            "Route B: DI/BFI/Kuznetsov self-contained appendix",
            "primary_high_risk",
            "直接证明当前 full-S non-AP WFD Kloosterman/dispersion 估计，产生带符号取消。",
            "极高；相当于重证深层自守/谱大筛技术。",
            "先只证明足够的模型 BE2-3K/KLS-window 命题；不再声称完整自足闭合。",
        ),
        route(
            "Route C: Maynard/GPY transference",
            "secondary",
            "尝试把每个 H_P 窗口转为可控 admissible tuple 与分布估计问题。",
            "高；仓库已有 Maynard-S compression no-go，不能直接移植 bounded gaps。",
            "只保留为新变量翻译研究，不作为当前主闭合路线。",
        ),
        route(
            "Route D: automorphic L-functions / trace formula",
            "primary_high_risk",
            "用 Kuznetsov/GL(2) 或更高阶谱技术处理 windowed Kloosterman、Type-II balanced convolution。",
            "极高；需要证明精确窗口和权重下的任意对数节省。",
            "把目标拆成 KLS-window theorem statement 与可引用文献匹配。",
        ),
        route(
            "Route E: Phi-LPF/Eratosthenes capacity rewriting",
            "demoted",
            "保留为证书化 reduction、有限审计、反例结构定位。",
            "不能突破奇偶屏障。",
            "停止把该类步骤命名为闭合；只用于定义待证 analytic object。",
        ),
        route(
            "Route F: finite verification + theta>1/2",
            "rejected",
            "验证有限前缀，尾段用 BHP/Li 0.525/0.52。",
            "留下无限顶端带。",
            "仅保留为有限范围定理，不作为 H_P 无条件闭合路线。",
        ),
    ]


def build_external_sources() -> list[dict[str, str]]:
    """记录本层依赖的外部前沿入口。"""
    return [
        {
            "name": "Baker--Harman--Pintz 2001",
            "role": "通用短区间素数，指数 0.525 级；不达 sqrt 尺度。",
            "url": "https://doi.org/10.1112/plms/83.3.532",
        },
        {
            "name": "Runbo Li 2025 arXiv v8",
            "role": "通用短区间素数改进到 0.52 级；仍大于 1/2。",
            "url": "https://arxiv.org/abs/2308.04458",
        },
        {
            "name": "Friedlander--Iwaniec x^2+y^4 prime values",
            "role": "parity-sensitive sieve/深层分布技术代表；不是 H_P 直接闭合定理。",
            "url": "https://annals.math.princeton.edu/1998/148-3/p04",
        },
        {
            "name": "Maynard 2015 small gaps",
            "role": "多维筛/GPY-Maynard 技术代表；证明 bounded gaps infinitely often，不给 every sqrt-window。",
            "url": "https://annals.math.princeton.edu/2015/181-1/p07",
        },
        {
            "name": "Deshouillers--Iwaniec / BFI dispersion class",
            "role": "Kloosterman/dispersion/autorphic 技术族；需精确匹配当前 full-S non-AP WFD 对象。",
            "url": "https://link.springer.com/article/10.1007/BF01458321",
        },
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
    lines = ["| route | status | role | risk | next action |", "| --- | --- | --- | --- | --- |"]
    for item in routes:
        lines.append(
            f"| {cell(item['route'])} | `{cell(item['status'])}` | {cell(item['role'])} | "
            f"{cell(item['risk'])} | {cell(item['next_action'])} |"
        )
    return "\n".join(lines)


def sources_markdown(sources: list[dict[str, str]]) -> str:
    """输出外部来源表。"""
    lines = ["| source | role | url |", "| --- | --- | --- |"]
    for item in sources:
        lines.append(f"| {cell(item['name'])} | {cell(item['role'])} | {item['url']} |")
    return "\n".join(lines)


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_hp_cramer_local_route_reset_router",
        "status": "hp_cramer_local_route_reset_after_parity_barrier_review",
        "review_core_accepted": True,
        "hp_direct_unconditional_closure_claim_allowed": False,
        "same_target_not_proved": True,
        "mathematical_position": {
            "top_strict_band": "k≈P, x=kP≈P^2, target interval length P≈sqrt(x)",
            "hp_scale": "Legendre/Cramer-local short interval scale",
            "phi_lpf_role": "exact Eratosthenes-equivalent combinatorial count/reduction",
            "missing_input": "positive lower bound beyond unsigned sieve parity barrier",
        },
        "current_frontier_after_reset": (
            "ExactExternalSqrtScaleOrFullSNonAPWFDKLSTheoremMatch "
            "OR NewAutomorphicDispersionProof "
            "OR SpecialSquarePhaseStructuralLowerBoundBeyondParity"
        ),
        "gates": build_gates(),
        "routes": build_routes(),
        "external_sources": build_external_sources(),
        "dependency_hashes": dependency_hashes,
        "plain_conclusion": (
            "本层接受评审核心结论：H_P 的最坏 strict 顶端带就是 sqrt(x) 局部短区间素数问题，"
            "Phi-LPF/LPF/Eratosthenes 恒等式只能提供组合精确 reduction，不能提供正性。"
            "此前所有无符号重排成果保留为 reduction library 和反例结构定位，不再被当成闭合。"
            "后续主攻必须转到精确外部 theorem-match、DI/BFI/Kuznetsov/自守 dispersion 新输入，"
            "或真正 special square-phase 结构下界。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    lines = [
        "# Prime Matrix H_P/Cramér-local 路线重置证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 核心结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"top_strict_band={payload['mathematical_position']['top_strict_band']}",
        f"hp_scale={payload['mathematical_position']['hp_scale']}",
        f"phi_lpf_role={payload['mathematical_position']['phi_lpf_role']}",
        f"missing_input={payload['mathematical_position']['missing_input']}",
        "```",
        "",
        "这意味着：直接宣称 H_P 主命题无条件闭合，在当前仓库和当前数学前沿下都不允许。",
        "能闭合的是 reduction、有限范围、条件性定理，或外部深定理精确匹配后的条件链。",
        "",
        "## 2. 路线重置表",
        "",
        routes_markdown(payload["routes"]),
        "",
        "## 3. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 4. 新主攻口",
        "",
        "```text",
        payload["current_frontier_after_reset"],
        "```",
        "",
        "该主攻口的含义不是继续改写 Phi-LPF，而是提交能真正越过奇偶屏障的带符号分布输入。",
        "",
        "## 5. 外部来源入口",
        "",
        sources_markdown(payload["external_sources"]),
        "",
        "## 6. 依赖哈希",
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
    print(
        json.dumps(
            {
                "status": payload["status"],
                "review_core_accepted": payload["review_core_accepted"],
                "hp_direct_unconditional_closure_claim_allowed": payload[
                    "hp_direct_unconditional_closure_claim_allowed"
                ],
                "current_frontier_after_reset": payload["current_frontier_after_reset"],
                "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
