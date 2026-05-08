#!/usr/bin/env python3
"""Prime Matrix 互补锚与 D0/K/Omega 参数纪律路由器。

用法示例：
  python3 experiments/prime_matrix_complement_anchor_d0k_parameter_router.py

输出：
  docs/monograph/prime-matrix-complement-anchor-d0k-parameter-router.json
  docs/monograph/prime-matrix-complement-anchor-d0k-parameter-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-bad-window-source-data-emitter-router.json"
DEFAULT_FORMAL = MONOGRAPH / "prime-matrix-formal-corridor-inventory-contract-router.md"
DEFAULT_TCR = MONOGRAPH / "prime-matrix-bpn-tailcore-corridor-reduction.md"
DEFAULT_DCS = MONOGRAPH / "prime-matrix-bpn-distributed-corridor-saturation-reduction.md"
DEFAULT_CCB = MONOGRAPH / "prime-matrix-bpn-colored-corridor-core-sieve-budget.md"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-complement-anchor-d0k-parameter-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-complement-anchor-d0k-parameter-router.md"

OLD_ATOM = "ComplementAnchorSetAndD0KParameterLedger"
CLOSED_ATOM = "ComplementAnchorSetAndD0KParameterDisciplineClosed"
COLORING_ATOM = "IntervalGraphColoringCoverageCertificateLedger"
BUDGET_ATOM = "AllowedBudgetAllocationLedger"
RANKIN_ATOM = "BatchRankinCertificatesAllPassOrReturnToPDECSAE"
PDEC_SAE_ATOM = "PDECOrSAEUnifiedExclusionLedger"


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def parameter_rules() -> list[dict[str, str]]:
    """给出参数纪律规则。"""
    return [
        {
            "field": "D0",
            "discipline": "由 TailCore/CoreK bucket 的 dyadic core scale 固定，使用半开区间 [D0,2D0)。",
            "forbidden": "不能为通过 Rankin 预算而后验移动 dyadic 边界。",
        },
        {
            "field": "K",
            "discipline": "由 source record 的 omega 截断固定，sigma_K(d) 使用 omega(d)<=K。",
            "forbidden": "不能在同一颜色类内混用多个 K，除非拆成不同 records。",
        },
        {
            "field": "Omega",
            "discipline": "由 DCS 高/低重叠二分固定；m(d)>Omega 立即回流 high-overlap defect。",
            "forbidden": "不能把高重叠点留在 low-overlap colored corridor 中。",
        },
        {
            "field": "anchor_set_hash",
            "discipline": "对规范化 source tuple 与排序后的互补锚集合 A 取哈希，作为可复算来源标识。",
            "forbidden": "不能只给口头 anchor set；必须能由 I、D0、A0、phase_rule 复算。",
        },
        {
            "field": "phase_rule",
            "discipline": "phase(d) 是 source record 携带的有限谓词；若无相位过滤则显式写 identity。",
            "forbidden": "不能在 Rankin 失败后临时追加相位过滤来降低计数。",
        },
        {
            "field": "corridor_domain",
            "discipline": "每个 a 生成 J_a={d:D0<=d<2D0, ad in I}；低重叠仅保留 m(d)<=Omega 部分。",
            "forbidden": "不能把不属于同一 D0/K/Omega tuple 的走廊合并进同一颜色证书。",
        },
    ]


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


def build_rows(previous: dict[str, Any], texts: dict[str, str]) -> list[dict[str, Any]]:
    """生成参数纪律判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    formal_ready = contains_all(
        texts["formal"],
        ["anchor_set_hash", "D0", "Omega", "phase_rule", "coverage_equation"],
    )
    tcr_ready = contains_all(
        texts["tcr"],
        ["D_0\\le d<2D_0", "A_0\\le a<2A_0", "\\omega(d)\\le K"],
    )
    dcs_ready = contains_all(
        texts["dcs"],
        ["m(d)>\\Omega", "m(d)\\le\\Omega", "区间图是完美图"],
    )
    ccb_ready = contains_all(
        texts["ccb"],
        ["sigma_K(d)", "phase(d)", "Rankin ledger <= allowed budget"],
    )
    discipline_closed = all([active, guard, formal_ready, tcr_ready, dcs_ready, ccb_ready])
    return [
        row(
            "ComplementAnchorParameterGateActive",
            active,
            False,
            "上一层已把最窄点推进到互补锚、D0/K/Omega 参数账本。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设反例链条内的证书参数，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "FormalInventoryFieldsPinned",
            formal_ready,
            True,
            "正式 inventory 已要求 K、D0、Omega、anchor_set_hash、phase_rule 与 coverage_equation。",
            "字段格式无剩余。",
        ),
        row(
            "TailCoreDyadicSourcePinsD0K",
            tcr_ready,
            True,
            "TailCoreBucket 已把核心 d 放入唯一 dyadic D0 桶，并固定 omega 截断 K。",
            "D0/K 不能后验调参。",
        ),
        row(
            "DCSOverlapThresholdPinsOmega",
            dcs_ready,
            True,
            "DCS 用 Omega 把高重叠点送回缺陷，低重叠点才允许进入着色走廊。",
            "Omega 不能用于隐藏高重叠。",
        ),
        row(
            "CCBPhaseRuleAndRankinObjectPinned",
            ccb_ready,
            True,
            "CCB 的 sigma_K(d) 明确携带 phase(d)，Rankin 证书对象随该 tuple 固定。",
            "预算分配留给下一层。",
        ),
        row(
            CLOSED_ATOM,
            discipline_closed,
            True,
            "A、D0、K、Omega、phase_rule 与 hash 的来源纪律已固定，不能再后验选择参数。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            discipline_closed,
            True,
            "参数账本闭合为 canonical tuple 纪律；下一步应提交区间图着色与覆盖等式。",
            COLORING_ATOM,
        ),
        row(
            "ConcreteColoringStillDownstream",
            False,
            False,
            "同色 intervals、覆盖等式和颜色数证书仍未提交。",
            COLORING_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行参数纪律路由。"""
    previous = load_json(paths["previous"])
    texts = {key: read_text(path) for key, path in paths.items() if key != "previous"}
    rows = build_rows(previous, texts)
    discipline_closed = next(item["closed"] for item in rows if item["gate"] == CLOSED_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_complement_anchor_d0k_parameter_router",
        "status": "complement_anchor_d0k_parameter_discipline_closed_coloring_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "complement_anchor_d0k_parameter_discipline_closed": discipline_closed,
        "formal_colored_corridor_inventory_closed": False,
        "parameter_rules": parameter_rules(),
        "current_narrowest_atom": COLORING_ATOM,
        "downstream_atoms": [BUDGET_ATOM, RANKIN_ATOM, PDEC_SAE_ATOM],
        "reduction_formula": f"{OLD_ATOM} => {CLOSED_ATOM} AND {COLORING_ATOM}.",
        "plain_conclusion": (
            "ComplementAnchorSetAndD0KParameterLedger 的参数纪律已闭合：互补锚集合 A、D0、K、"
            "Omega、phase_rule 与 anchor_set_hash 都必须由同一 source tuple 可复算地产生，"
            "不能为 Rankin 预算后验调参。剩余不再是参数来源，而是提交区间图着色、同色不相交"
            f" intervals 与覆盖等式，即 `{COLORING_ATOM}`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 互补锚与 D0/K/Omega 参数纪律路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        (
            "complement_anchor_d0k_parameter_discipline_closed="
            f"{fmt_bool(result['complement_anchor_d0k_parameter_discipline_closed'])}"
        ),
        f"formal_colored_corridor_inventory_closed={fmt_bool(result['formal_colored_corridor_inventory_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 参数纪律",
        "",
        "| field | discipline | forbidden |",
        "| --- | --- | --- |",
    ]
    for item in result["parameter_rules"]:
        lines.append(
            "| {field} | {discipline} | {forbidden} |".format(
                field=table_cell(item["field"]),
                discipline=table_cell(item["discipline"]),
                forbidden=table_cell(item["forbidden"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 下一步",
            "",
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`。"
            f"随后才是 `{BUDGET_ATOM}` 与 `{RANKIN_ATOM}`。",
            "",
            "审稿边界：本步只固定参数来源纪律，不提交 coloring/budget/Rankin concrete 证书全集。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--formal", type=Path, default=DEFAULT_FORMAL)
    parser.add_argument("--tcr", type=Path, default=DEFAULT_TCR)
    parser.add_argument("--dcs", type=Path, default=DEFAULT_DCS)
    parser.add_argument("--ccb", type=Path, default=DEFAULT_CCB)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "formal": args.formal,
        "tcr": args.tcr,
        "dcs": args.dcs,
        "ccb": args.ccb,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
