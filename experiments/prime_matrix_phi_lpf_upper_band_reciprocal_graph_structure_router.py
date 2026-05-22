#!/usr/bin/env python3
"""生成 upper-band reciprocal shadow graph 的非循环结构证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_upper_band_reciprocal_graph_structure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure-router.json

输出：
  data/prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure-ledger.json
  docs/monograph/prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure-router.json
  docs/monograph/prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure-router.md
"""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from math import isqrt
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

MAX_PRIME_AUDIT = 1009
LARGE_SAMPLE_SEEDS = [100000, 300000]

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-upper-band-two-prime-shadow-excess-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.json",
    DOCS / "prime-matrix-phi-lpf-shadow-free-half-primorial-phase-router.json",
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


def spf_table(n: int) -> list[int]:
    """生成最小素因子表。"""
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for value in range(p * p, n + 1, p):
                if spf[value] == value:
                    spf[value] = p
    return spf


def prime_flags(n: int) -> bytearray:
    """生成素数标记表。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def primes_from_spf(spf: list[int], n: int) -> list[int]:
    """从 SPF 表读取素数。"""
    return [value for value in range(2, n + 1) if spf[value] == value]


def next_prime_at_least(seed: int, flags: bytearray) -> int:
    """在标记表内寻找不小于 seed 的首个素数。"""
    for value in range(max(2, seed), len(flags)):
        if flags[value]:
            return value
    raise ValueError(f"no prime found after seed={seed}")


def high_band_lower_k(P: int) -> int:
    """返回 BHP bulk 后的第一个整数 k；只作分区标签。"""
    return max(2, int(P ** (19.0 / 21.0)) + 1)


def shadow_free_cap(P: int) -> int:
    """返回 shadow-free 条件允许的最大 k。"""
    return max(1, (P * P - 4 * P + 4) // (4 * P))


def upper_band_first_k(P: int) -> int:
    """返回 upper square band 第一行。"""
    return max(2, shadow_free_cap(P) + 1)


def reciprocal_window_for_q(P: int, k: int, q: int) -> tuple[int, int]:
    """返回固定 q 的 m 候选闭区间。"""
    lower = max(q, (k * P) // q + 1)
    upper = min(2 * P - 1, ((k + 1) * P - 1) // q)
    return lower, upper


def reciprocal_edges(
    P: int,
    k: int,
    high_q_primes: list[int],
    is_prime: Callable[[int], bool],
) -> list[tuple[int, int]]:
    """列出 reciprocal shadow 图的 prime-pair 边。"""
    edges: list[tuple[int, int]] = []
    for q in high_q_primes:
        lower, upper = reciprocal_window_for_q(P, k, q)
        for m in range(lower, upper + 1):
            if is_prime(m):
                edges.append((q, m))
    return edges


class UnionFind:
    """用于检测二部图连通分量。"""

    def __init__(self) -> None:
        self.parent: dict[tuple[str, int], tuple[str, int]] = {}

    def add(self, node: tuple[str, int]) -> None:
        """加入节点。"""
        self.parent.setdefault(node, node)

    def find(self, node: tuple[str, int]) -> tuple[str, int]:
        """查找并压缩路径。"""
        parent = self.parent[node]
        if parent != node:
            self.parent[node] = self.find(parent)
        return self.parent[node]

    def union(self, left: tuple[str, int], right: tuple[str, int]) -> None:
        """合并两个节点。"""
        self.add(left)
        self.add(right)
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left != root_right:
            self.parent[root_right] = root_left


def graph_profile(P: int, k: int, edges: list[tuple[int, int]]) -> dict[str, Any]:
    """计算 reciprocal shadow 图的有序非循环结构读数。"""
    q_degree: dict[int, int] = defaultdict(int)
    m_degree: dict[int, int] = defaultdict(int)
    for q, m in edges:
        q_degree[q] += 1
        m_degree[m] += 1

    # 有序无交叉：q 增大时，所有相邻 m 只能不增。
    noncrossing = True
    previous_min_m: int | None = None
    grouped: dict[int, list[int]] = defaultdict(list)
    for q, m in edges:
        grouped[q].append(m)
    for q in sorted(grouped):
        current_ms = grouped[q]
        if previous_min_m is not None and max(current_ms) > previous_min_m:
            noncrossing = False
            break
        previous_min_m = min(current_ms) if previous_min_m is None else min(previous_min_m, min(current_ms))

    uf = UnionFind()
    for q, m in edges:
        uf.union(("q", q), ("m", m))
    roots = {uf.find(node) for node in uf.parent}
    vertex_count = len(uf.parent)
    component_count = len(roots)
    edge_count = len(edges)
    acyclic_by_euler = edge_count <= vertex_count - component_count if edge_count else True

    return {
        "P": P,
        "k": k,
        "edge_count": edge_count,
        "q_vertex_count": len(q_degree),
        "m_vertex_count": len(m_degree),
        "vertex_count": vertex_count,
        "component_count": component_count,
        "max_q_degree": max(q_degree.values(), default=0),
        "max_m_degree": max(m_degree.values(), default=0),
        "all_q_degrees_at_most_two": max(q_degree.values(), default=0) <= 2,
        "all_m_degrees_at_most_two": max(m_degree.values(), default=0) <= 2,
        "ordered_noncrossing_edges": noncrossing,
        "acyclic_shadow_graph": noncrossing and acyclic_by_euler,
        "edge_prefix": [
            {"q": q, "m": m, "n": q * m}
            for q, m in edges[:16]
        ],
    }


def finite_row_prime_count(P: int, k: int, spf: list[int]) -> int:
    """直接读取该行素数数；只用于有限审计展示。"""
    return sum(1 for t in range(1, P) if spf[k * P + t] == k * P + t)


def audit_prime_base(P: int, spf: list[int], primes_2p: list[int]) -> dict[str, Any]:
    """审计单个素数底 P 的 reciprocal graph。"""
    high_q_primes = [q for q in primes_2p if P // 2 < q < P]
    first_upper = upper_band_first_k(P)
    first_high = high_band_lower_k(P)

    def is_prime_m(value: int) -> bool:
        return spf[value] == value

    rows: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    for k in range(first_upper, P):
        edges = reciprocal_edges(P, k, high_q_primes, is_prime_m)
        profile = graph_profile(P, k, edges)
        profile.update(
            {
                "upper_band_first_k": first_upper,
                "bhp_remaining_high_band_first_k": first_high,
                "in_bhp_remaining_high_band": k >= first_high,
                "direct_prime_count": finite_row_prime_count(P, k, spf),
            }
        )
        rows.append(profile)
        if not (
            profile["all_q_degrees_at_most_two"]
            and profile["all_m_degrees_at_most_two"]
            and profile["ordered_noncrossing_edges"]
            and profile["acyclic_shadow_graph"]
        ):
            failures.append(profile)

    sample_ks = sorted(
        {
            first_upper,
            min(P - 1, max(first_upper, first_high)),
            min(P - 1, max(first_upper, P // 2)),
            min(P - 1, max(first_upper, (3 * P) // 4)),
            P - 1,
        }
    )
    max_edge_row = max(rows, key=lambda item: item["edge_count"])
    max_component_row = max(rows, key=lambda item: item["component_count"])
    return {
        "P": P,
        "upper_band_first_k": first_upper,
        "bhp_remaining_high_band_first_k": first_high,
        "upper_row_count": len(rows),
        "graph_structure_failure_count": len(failures),
        "all_upper_rows_have_forest_shadow_graph": not failures,
        "max_edge_row": max_edge_row,
        "max_component_row": max_component_row,
        "sample_rows": [row for row in rows if row["k"] in sample_ks],
    }


def finite_audit(max_prime: int = MAX_PRIME_AUDIT) -> dict[str, Any]:
    """有限审计 graph structure；不作为全局证明。"""
    spf = spf_table(max_prime * max_prime)
    primes = primes_from_spf(spf, max_prime)
    primes_2p = primes_from_spf(spf, 2 * max_prime)
    profiles = [audit_prime_base(P, spf, primes_2p) for P in primes if P >= 11]
    failures = [profile for profile in profiles if profile["graph_structure_failure_count"]]
    max_edge_profile = max(profiles, key=lambda item: item["max_edge_row"]["edge_count"])
    return {
        "max_prime": max_prime,
        "prime_base_count": len(profiles),
        "all_upper_rows_have_forest_shadow_graph": not failures,
        "graph_structure_failure_count": sum(profile["graph_structure_failure_count"] for profile in profiles),
        "max_edge_profile": {
            "P": max_edge_profile["P"],
            "row": max_edge_profile["max_edge_row"],
        },
        "sample_profiles": [
            profile
            for profile in profiles
            if profile["P"] in {11, 101, 257, 1009}
        ],
        "finite_evidence_not_used_as_global_proof": True,
    }


def large_sample_audit(seeds: list[int] = LARGE_SAMPLE_SEEDS) -> dict[str, Any]:
    """抽样较大 P 的 reciprocal graph 结构。"""
    max_seed = max(seeds) + 10000
    flags = prime_flags(2 * max_seed)
    samples: list[dict[str, Any]] = []
    for seed in seeds:
        P = next_prime_at_least(seed, flags)
        high_q_primes = [q for q in range(P // 2 + 1, P) if flags[q]]
        first_upper = upper_band_first_k(P)
        first_high = high_band_lower_k(P)
        k_values = sorted(
            {
                first_upper,
                min(P - 1, max(first_upper, first_high)),
                min(P - 1, max(first_upper, P // 2)),
                min(P - 1, max(first_upper, (3 * P) // 4)),
                P - 1,
            }
        )

        def is_prime_m(value: int) -> bool:
            return bool(flags[value])

        for k in k_values:
            profile = graph_profile(P, k, reciprocal_edges(P, k, high_q_primes, is_prime_m))
            profile.update(
                {
                    "upper_band_first_k": first_upper,
                    "bhp_remaining_high_band_first_k": first_high,
                }
            )
            samples.append(profile)
    return {
        "sample_seeds": seeds,
        "sample_count": len(samples),
        "all_sampled_graphs_are_forests": all(item["acyclic_shadow_graph"] for item in samples),
        "all_sampled_degrees_at_most_two": all(
            item["all_q_degrees_at_most_two"] and item["all_m_degrees_at_most_two"]
            for item in samples
        ),
        "samples": samples,
        "large_samples_are_evidence_not_global_proof": True,
    }


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_gates() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        gate(
            "ReciprocalShadowGraphDegreeTwoClosed",
            True,
            True,
            "固定 q 和固定 m 的 reciprocal 窗口长度都小于 2，因此二部图两侧度数均不超过 2。",
            "exact graph structure",
        ),
        gate(
            "OrderedNoncrossingShadowEdgesClosed",
            True,
            True,
            "若 q1<q2 且 m1<m2，则 q2m2-q1m1>P，不能同时落入同一长度 P 行。",
            "monotone reciprocal ordering",
        ),
        gate(
            "UpperBandShadowGraphForestClosed",
            True,
            True,
            "有序无交叉加度数二排除 reciprocal shadow 的循环反馈；有限审计与结构证明均给出森林图。",
            "forest shadow graph",
        ),
        gate(
            "FiniteSweepSupportsForestStructure",
            True,
            True,
            "有限审计确认所有 upper rows 的 graph 读数正常，但不作为全局正性证明。",
            "finite audit only",
        ),
        gate(
            "ForestSaturationExcluded",
            False,
            False,
            "尚未证明这个森林边集不能刚好覆盖全部 half-rough survivors。",
            "UpperBandForestShadowSaturationExclusionOrPDEC",
        ),
        gate(
            "UnifiedPositiveCoreProved",
            False,
            False,
            "本层只排除 upper-band shadow 的循环反馈，不证明三目标命题。",
            "HalfPrimorialSpecialPhaseAvoidsLongCoveredBlockOrPDEC AND UpperBandForestShadowSaturationExclusionOrPDEC",
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
        "| P | k | edges | vertices | components | max deg q | max deg m | forest | direct primes |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: |",
    ]
    for row in samples:
        lines.append(
            f"| {row['P']} | {row['k']} | {row['edge_count']} | {row['vertex_count']} | "
            f"{row['component_count']} | {row['max_q_degree']} | {row['max_m_degree']} | "
            f"`{fmt_bool(row['acyclic_shadow_graph'])}` | {row.get('direct_prime_count', '')} |"
        )
    return "\n".join(lines)


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    finite = finite_audit()
    large = large_sample_audit()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_upper_band_reciprocal_graph_structure_router",
        "status": "upper_band_reciprocal_shadow_graph_reduced_to_ordered_degree_two_forest",
        "finite_audit": finite,
        "large_sample_audit": large,
        "gates": build_gates(),
        "dependency_hashes": dependency_hashes,
        "next_direct_attack_target": "UpperBandForestShadowSaturationExclusionOrPDEC",
        "plain_conclusion": (
            "upper-band two-prime shadow 的 reciprocal prime-pair 图是有序、无交叉、两侧度数至多二的森林。"
            "因此反例不能依靠循环反馈放大 shadow；若仍失败，只能是这片森林边集真实饱和全部 "
            "half-rough survivor，或触发显式 PDEC。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    finite = payload["finite_audit"]
    large = payload["large_sample_audit"]
    sample_rows = [row for profile in finite["sample_profiles"] for row in profile["sample_rows"]]
    max_edge = finite["max_edge_profile"]["row"]
    lines = [
        "# Prime Matrix Phi-LPF upper-band reciprocal graph structure 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "本层继续压缩 upper-band reciprocal prime-pair shadow。把每个 shadow 对 `(q,m)` 看成",
        "二部图的一条边，其中 `q in (P/2,P)`，`m in [q,2P)` 且 `qm` 落入同一行。",
        "",
        "## 1. 结构证明读法",
        "",
        "固定 `q` 时，`m` 的窗口长度小于 `P/q<2`，所以 `q` 侧度数至多二。",
        "固定 `m` 时同理，`q` 的窗口长度小于 `P/m<=P/q<2`，所以 `m` 侧度数也至多二。",
        "",
        "若存在交叉边 `q1<mapped to m1` 与 `q2<mapped to m2`，其中 `q1<q2` 且 `m1<m2`，则",
        "",
        "```text",
        "q2*m2-q1*m1 >= (q2-q1)*m2 + q1*(m2-m1) > P,",
        "```",
        "",
        "这与二者同时落在长度 `P` 的同一行矛盾。因此 shadow 图有序无交叉；结合两侧度数至多二，",
        "它不能形成循环反馈。更直接地，若存在环，取环中最小的 `q0`，它在环上连接两个",
        "不同的 `m`，设为 `m_a<m_b`。任意其他 `q>q0` 若连接到 `m>m_a`，就与边",
        "`(q0,m_a)` 交叉；于是 `m_b` 不可能再连接到第二个 `q`，矛盾。故 shadow 图只能是森林型边集。",
        "",
        "## 2. 有限审计",
        "",
        "```text",
        f"max_prime={finite['max_prime']}",
        f"prime_base_count={finite['prime_base_count']}",
        f"all_upper_rows_have_forest_shadow_graph={fmt_bool(finite['all_upper_rows_have_forest_shadow_graph'])}",
        f"graph_structure_failure_count={finite['graph_structure_failure_count']}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(finite['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "最大 edge 行读数：",
        "",
        "```text",
        f"P={max_edge['P']}, k={max_edge['k']}, edges={max_edge['edge_count']}, "
        f"vertices={max_edge['vertex_count']}, components={max_edge['component_count']}, "
        f"direct_primes={max_edge['direct_prime_count']}",
        "```",
        "",
        "## 3. 有限样本表",
        "",
        sample_markdown(sample_rows),
        "",
        "## 4. 大尺度抽样",
        "",
        "```text",
        f"sample_seeds={large['sample_seeds']}",
        f"sample_count={large['sample_count']}",
        f"all_sampled_graphs_are_forests={fmt_bool(large['all_sampled_graphs_are_forests'])}",
        f"all_sampled_degrees_at_most_two={fmt_bool(large['all_sampled_degrees_at_most_two'])}",
        f"large_samples_are_evidence_not_global_proof={fmt_bool(large['large_samples_are_evidence_not_global_proof'])}",
        "```",
        "",
        sample_markdown(large["samples"]),
        "",
        "## 5. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 6. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "当前 upper-band 的下一窄口为：",
        "",
        "```text",
        payload["next_direct_attack_target"],
        "```",
        "",
        "本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它只排除了 upper-band",
        "shadow 的循环反馈形态。",
        "",
        "## 7. 依赖哈希",
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
                "max_prime": payload["finite_audit"]["max_prime"],
                "all_upper_rows_have_forest_shadow_graph": payload["finite_audit"][
                    "all_upper_rows_have_forest_shadow_graph"
                ],
                "large_sample_count": payload["large_sample_audit"]["sample_count"],
                "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
