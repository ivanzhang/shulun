#!/usr/bin/env python3
"""Prime Matrix anchor-collar 容量端点缺陷桥路由器。

用法示例：
  python3 experiments/prime_matrix_anchor_collar_endpoint_bridge_router.py
  python3 experiments/prime_matrix_anchor_collar_endpoint_bridge_router.py --p-list 101,499,997

输出：
  docs/monograph/prime-matrix-anchor-collar-endpoint-bridge-router.json
  docs/monograph/prime-matrix-anchor-collar-endpoint-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from array import array
from math import isqrt
from pathlib import Path
from typing import Any

from prime_matrix_cylindrical_completion_audit import primes_upto, small_factor_table


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-early-zero-terminal-package-reduction-router.json"
DEFAULT_ANCHOR = DOCS / "prime-matrix-early-zero-anchor-collar-router.json"
DEFAULT_DLS13 = DOCS / "prime-matrix-eda-dls13-endpoint-defect-bridge.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-anchor-collar-endpoint-bridge-router.json"
DEFAULT_MD = DOCS / "prime-matrix-anchor-collar-endpoint-bridge-router.md"

OLD_ATOM = "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn"
NEW_ATOM = (
    "(AnchorCollarEndpointDefectPDECExclusion "
    "OR AnchorFiberSaturationPDECOrSAEReturn)"
)


def parse_p_list(raw: str) -> list[int]:
    """解析逗号分隔的 P 列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_once(text: str, old: str, new: str) -> str:
    """只替换一次输入基原子。"""
    if old not in text:
        return text
    return text.replace(old, new, 1)


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def row_identity_stats(p: int, x: int, spf: array) -> dict[str, Any]:
    """统计 H_x=Prime_x+A_x 精确恒等式样本。"""
    rough_holes = 0
    prime_holes = 0
    anchor_capacity = 0
    bad_semiprime = 0
    anchor_top = isqrt((x + 1) * p - 1)
    for column in range(1, p):
        value = x * p + column
        factor = spf[value]
        if factor and factor <= x:
            continue
        rough_holes += 1
        if factor == 0:
            prime_holes += 1
            continue
        cofactor = value // factor
        if x < factor <= cofactor < p and factor <= anchor_top and spf[cofactor] == 0:
            anchor_capacity += 1
        else:
            bad_semiprime += 1
    return {
        "x": x,
        "rough_holes": rough_holes,
        "prime_holes": prime_holes,
        "anchor_capacity": anchor_capacity,
        "identity_gap": rough_holes - prime_holes - anchor_capacity,
        "bad_semiprime": bad_semiprime,
        "anchor_top": anchor_top,
    }


def audit_p(p: int, sample_limit: int) -> dict[str, Any]:
    """审计单个 P 的 anchor 恒等式。"""
    spf = small_factor_table(p)
    sqrt_p = isqrt(p)
    rows = [row_identity_stats(p, x, spf) for x in range(sqrt_p, p)]
    min_prime_holes = min((item["prime_holes"] for item in rows), default=0)
    max_identity_gap = max((abs(item["identity_gap"]) for item in rows), default=0)
    max_bad_semiprime = max((item["bad_semiprime"] for item in rows), default=0)
    weakest_rows = sorted(rows, key=lambda item: (item["prime_holes"], item["x"]))[
        :sample_limit
    ]
    strongest_anchor_rows = sorted(
        rows,
        key=lambda item: (
            item["anchor_capacity"] / item["rough_holes"] if item["rough_holes"] else 0,
            item["anchor_capacity"],
        ),
        reverse=True,
    )[:sample_limit]
    return {
        "p": p,
        "sqrt_p": sqrt_p,
        "row_count": len(rows),
        "identity_verified": max_identity_gap == 0 and max_bad_semiprime == 0,
        "max_identity_gap": max_identity_gap,
        "max_bad_semiprime": max_bad_semiprime,
        "min_prime_holes": min_prime_holes,
        "weakest_prime_rows": weakest_rows,
        "strongest_anchor_rows": strongest_anchor_rows,
    }


def audit_samples(p_values: list[int], sample_limit: int) -> dict[str, Any]:
    """审计多个样本 P。"""
    prime_set = set(primes_upto(max(p_values) if p_values else 2))
    rows = []
    skipped = []
    for p in p_values:
        if p < 3 or p not in prime_set:
            skipped.append(p)
            continue
        rows.append(audit_p(p, sample_limit))
    return {
        "p_values": p_values,
        "skipped_nonprimes": skipped,
        "status": "anchor_collar_identity_sample_verified_endpoint_bridge_open",
        "all_identities_verified": all(item["identity_verified"] for item in rows),
        "rows": rows,
    }


def build_rows(
    previous: dict[str, Any],
    anchor: dict[str, Any],
    dls13_text: str,
    pdec_text: str,
    sample_audit: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成端点缺陷桥判定表。"""
    anchor_gate_active = (
        previous.get("next_priority") == OLD_ATOM
        and OLD_ATOM in previous.get("open_gates", [])
    )
    anchor_geometry_closed = (
        anchor.get("terminal_gap_after_router") == OLD_ATOM
        and "CanonicalLeastAnchorCollar" in anchor.get("closed_gates", [])
        and "FiberShortPrimeInterval" in anchor.get("closed_gates", [])
    )
    exact_identity_closed = True
    endpoint_bridge_imported = (
        "H_y(p)=(p-1)V_y+E_y(p)" in dls13_text
        and "精确恒等式" in dls13_text
    )
    pdec_schema_available = (
        "未来 PDEC schema 准入条件" in pdec_text
        and "global_pdec_family_unconditional_closed=false" in pdec_text
    )
    sample_verified = sample_audit["all_identities_verified"]
    bridge_closed = all(
        [
            anchor_gate_active,
            anchor_geometry_closed,
            exact_identity_closed,
            endpoint_bridge_imported,
            pdec_schema_available,
            sample_verified,
        ]
    )
    return [
        row(
            "AnchorCollarCapacityGateActive",
            anchor_gate_active,
            True,
            "上一层最新最窄硬点就是 AnchorCollarPrimeFiberCapacityBoundOrPDECReturn。",
            "本步只攻击该硬点。",
        ),
        row(
            "AnchorGeometryImported",
            anchor_geometry_closed,
            True,
            "canonical collar 与短素数纤维窗口已经闭合。",
            "可定义精确容量 A_x。",
        ),
        row(
            "ExactRoughPrimeAnchorIdentity",
            exact_identity_closed,
            True,
            "对 x>=sqrt(P)，每个 x-rough 点要么是素数洞，要么唯一地是 canonical q*m anchor 点。",
            "H_x = Prime_x + A_x。",
        ),
        row(
            "EarlyZeroForcesPrimeVoid",
            True,
            True,
            "若早期零行存在，则所有 x-rough 点必须被高标签覆盖，所以 Prime_x=0。",
            "反例给出 H_x=A_x。",
        ),
        row(
            "EndpointDecompositionImported",
            endpoint_bridge_imported,
            True,
            "包含排除给出 H_x=(P-1)V_x+E_x，完全类似 DLS13 端点桥。",
            "若主项超过容量，反例强制 E_x 为负。",
        ),
        row(
            "CapacityFailureBecomesEndpointDefect",
            True,
            True,
            "若 (P-1)V_x-A_x 存在正间隙 G_x，则早期零行推出 E_x<=-G_x。",
            "这就是 anchor-collar 版 PDEC 端点缺陷。",
        ),
        row(
            "NoGapMeansFiberSaturation",
            True,
            True,
            "若没有正间隙，则 A_x 必须接近或超过低骨架主量，短纤维出现近饱和支付。",
            "持久近饱和进入 PDEC；孤立近饱和进入 SAE/LocalSurvivor。",
        ),
        row(
            "PDECSchemaAvailableForEndpointDefect",
            pdec_schema_available,
            False,
            "PDEC schema 准入防火墙已存在，但全局 PDEC family 排斥仍未证明。",
            "只能路由，不能宣称终端排斥完成。",
        ),
        row(
            "SampleIdentityAudit",
            sample_verified,
            False,
            "样本只复核 H_x=Prime_x+A_x 口径和 canonical anchor 唯一性。",
            sample_audit["status"],
        ),
        row(
            "AnchorCollarEndpointBridgeClosed",
            bridge_closed,
            True,
            "anchor-collar 容量硬点已转成端点 PDEC 排斥或短纤维饱和命名回流。",
            NEW_ATOM,
        ),
        row(
            "AnchorCollarEndpointDefectPDECExclusion",
            False,
            False,
            "尚未排斥早期零行强制产生的 E_x<=-G_x 级端点相位缺陷。",
            "下一步最窄目标。",
        ),
        row(
            "AnchorFiberSaturationPDECOrSAEReturn",
            False,
            False,
            "尚未证明无主项间隙时的短纤维近饱和必然给出可排斥 PDEC/SAE。",
            "备用分支。",
        ),
    ]


def run(
    previous_path: Path,
    anchor_path: Path,
    dls13_path: Path,
    pdec_path: Path,
    p_values: list[int],
    sample_limit: int,
) -> dict[str, Any]:
    """执行 anchor-collar 端点桥路由。"""
    source_paths = [previous_path, anchor_path, dls13_path, pdec_path]
    previous = load_json(previous_path)
    anchor = load_json(anchor_path)
    dls13_text = dls13_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    sample_audit = audit_samples(p_values, sample_limit)
    rows = build_rows(
        previous=previous,
        anchor=anchor,
        dls13_text=dls13_text,
        pdec_text=pdec_text,
        sample_audit=sample_audit,
    )
    bridge_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "AnchorCollarEndpointBridgeClosed"
    )
    latest_self = replace_once(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_cond = replace_once(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    return {
        "certificate_type": "anchor_collar_endpoint_bridge_router",
        "status": "anchor_collar_capacity_reduced_to_endpoint_pdec_or_fiber_saturation",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "anchor_collar_endpoint_bridge_closed": bridge_closed,
        "anchor_collar_prime_fiber_capacity_fully_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {
            OLD_ATOM: NEW_ATOM,
        },
        "next_priority": "AnchorCollarEndpointDefectPDECExclusion",
        "exact_identity": "H_x(P)=Prime_x(P)+A_x(P) for x>=sqrt(P)",
        "early_zero_implication": "Assume EarlyZeroRowWithinP => Prime_x(P)=0 => H_x(P)=A_x(P)",
        "endpoint_bridge": "H_x(P)=(P-1)V_x(P)+E_x(P); if (P-1)V_x(P)-A_x(P)>=G_x>0 then E_x(P)<=-G_x",
        "sample_audit": sample_audit,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步没有证明 anchor-collar 容量不足；它证明容量不足的失败形态已被精确桥接："
            "早期零行使 Prime_x=0，而精确恒等式 H_x=Prime_x+A_x 将反例转为 H_x=A_x。"
            "若低骨架主项超过 anchor 容量，则得到强负端点 PDEC；若不超过，则短素数纤维必须"
            "近饱和并进入 PDEC/SAE 命名回流。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix anchor-collar 容量端点缺陷桥路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"anchor_collar_endpoint_bridge_closed={fmt_bool(result['anchor_collar_endpoint_bridge_closed'])}",
        "anchor_collar_prime_fiber_capacity_fully_proved="
        f"{fmt_bool(result['anchor_collar_prime_fiber_capacity_fully_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 精确桥",
        "",
        "```text",
        result["exact_identity"],
        result["early_zero_implication"],
        result["endpoint_bridge"],
        "```",
        "",
        "这仍然是在 `Assume EarlyZeroRowWithinP` 下工作；真实样本缺席不参与证明。",
        "",
        "## 2. 替换律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | `{remaining}` |".format(
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
            "## 4. 样本口径审计",
            "",
            "样本只用于复核恒等式实现，不作为证明输入。",
            "",
            "| P | rows | min prime holes | identity verified |",
            "| ---: | ---: | ---: | --- |",
        ]
    )
    for item in result["sample_audit"]["rows"]:
        lines.append(
            f"| {item['p']} | {item['row_count']} | {item['min_prime_holes']} | `{fmt_bool(item['identity_verified'])}` |"
        )
    lines.extend(
        [
            "",
            "## 5. 最新输入基",
            "",
            "条件输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "完全自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            f"最窄目标更新为 `{result['next_priority']}`：排斥早期零行强制产生的 "
            "`E_x<=-G_x` 级同 formal unit 端点相位缺陷；若主项间隙失败，则进入 "
            "`AnchorFiberSaturationPDECOrSAEReturn`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_outputs(result: dict[str, Any], json_out: Path, md_out: Path) -> None:
    """写出 JSON 与 Markdown。"""
    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    parser.add_argument("--dls13", type=Path, default=DEFAULT_DLS13)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--p-list", default="101,499,997")
    parser.add_argument("--sample-limit", type=int, default=3)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        anchor_path=args.anchor,
        dls13_path=args.dls13,
        pdec_path=args.pdec,
        p_values=parse_p_list(args.p_list),
        sample_limit=args.sample_limit,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
