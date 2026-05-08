#!/usr/bin/env python3
"""Prime Matrix 全 Rankin 走廊证书全集清单路由器。

用法示例：
  python3 experiments/prime_matrix_full_rankin_ledger_inventory_router.py

输出：
  docs/monograph/prime-matrix-full-rankin-ledger-inventory-router.json
  docs/monograph/prime-matrix-full-rankin-ledger-inventory-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_ACCEPTANCE = MONOGRAPH / "prime-matrix-bpn-rankin-ledger-acceptance-theorem.md"
DEFAULT_SAMPLE = MONOGRAPH / "prime-matrix-bpn-rankin-ledger-certificate-audit.json"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-full-rankin-ledger-inventory-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-full-rankin-ledger-inventory-router.md"

DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
OPEN_GATE = "FullRankinLedgerStillOpen"
INVENTORY_ATOM = "FormalColoredCorridorInventoryLedger"
BATCH_ATOM = "BatchRankinCertificatesAllPassOrReturnToPDECSAE"
PDEC_SAE_ATOM = "PDECOrSAEUnifiedExclusionLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def is_rankin_certificate_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像一个 Rankin 走廊证书或证书审计。"""
    required = {"p", "k", "intervals", "allowed_budget"}
    return required.issubset(payload.keys())


def is_formal_inventory_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像正式着色走廊全集清单。"""
    keys = set(payload.keys())
    return (
        "formal_colored_corridor_inventory" in keys
        or "colored_corridor_inventory" in keys
        or "corridor_certificates" in keys
        or payload.get("certificate_type") == "prime_matrix_formal_colored_corridor_inventory"
    )


def scan_json_corpus(root: Path) -> dict[str, Any]:
    """扫描仓库内 JSON，寻找 Rankin 样本和正式全集清单。"""
    rankin_like: list[dict[str, Any]] = []
    inventory_like: list[dict[str, Any]] = []
    parse_errors: list[str] = []
    for path in sorted(root.rglob("*.json")):
        if "__pycache__" in path.parts:
            continue
        try:
            payload = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError):
            parse_errors.append(str(path.relative_to(ROOT)))
            continue
        if not isinstance(payload, dict):
            continue
        rel = str(path.relative_to(ROOT))
        if is_rankin_certificate_like(payload):
            rankin_like.append(
                {
                    "path": rel,
                    "p": payload.get("p"),
                    "k": payload.get("k"),
                    "interval_count": len(payload.get("intervals", [])),
                    "allowed_budget": payload.get("allowed_budget"),
                    "rankin_budget_pass": payload.get("rankin_budget_pass"),
                    "exact_budget_pass": payload.get("exact_budget_pass"),
                    "status": payload.get("status"),
                }
            )
        if is_formal_inventory_like(payload):
            inventory_like.append({"path": rel, "status": payload.get("status")})
    return {
        "rankin_like": rankin_like,
        "inventory_like": inventory_like,
        "parse_errors": parse_errors,
    }


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


def build_rows(
    previous: dict[str, Any],
    acceptance_text: str,
    sample: dict[str, Any],
    scan: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成全 Rankin 证书全集清单判定表。"""
    gate_active = (
        previous.get("promotion_package_boundary_closed") is True
        and previous.get("promotion_package_independently_accepted") is False
        and any(item.get("gate") == OPEN_GATE for item in previous.get("rows", []))
    )
    acceptance_theorem_ready = all(
        token in acceptance_text
        for token in [
            "Theorem RLA-1",
            "Rankin certificates for all colored corridors",
            "low-mod core CRTDefect",
        ]
    )
    sample_ready = (
        sample.get("rankin_budget_pass") is True
        and sample.get("exact_budget_pass") is True
        and sample.get("status") == "finite_rankin_ledger_computable_with_lowmod_residue_report"
    )
    inventory_exists = bool(scan["inventory_like"])
    rankin_like_count = len(scan["rankin_like"])
    all_seen_pass = rankin_like_count > 0 and all(
        item.get("rankin_budget_pass") is True and item.get("exact_budget_pass") is True
        for item in scan["rankin_like"]
        if item.get("rankin_budget_pass") is not None
    )
    batch_closed = inventory_exists and all_seen_pass
    return [
        row(
            "FullRankinLedgerGateActive",
            gate_active,
            False,
            "DStructure/Rankin 晋级门已收缩到正式 Rankin 证书全集。",
            OPEN_GATE,
        ),
        row(
            "RankinAcceptanceTheoremReady",
            acceptance_theorem_ready,
            True,
            "RLA-1/RLA-2 已把单颜色与多颜色 Rankin 验收写成可检查定理。",
            "无验收格式剩余。",
        ),
        row(
            "ExecutableSampleCertificatePasses",
            sample_ready,
            True,
            "当前样本证书通过 exact 与 Rankin 预算，证明脚本格式可复现。",
            "样本不是正式全集。",
        ),
        row(
            "FormalColoredCorridorInventoryMissing",
            not inventory_exists,
            False,
            "仓库未发现正式着色走廊全集清单；没有它就无法定义 all colored corridors 的批量验收域。",
            INVENTORY_ATOM,
        ),
        row(
            "CandidateRankinAuditFilesFound",
            rankin_like_count > 0,
            False,
            "仓库能找到 Rankin-like JSON，但它们目前只是样本/局部证书，不构成全集。",
            f"rankin_like_count={rankin_like_count}",
        ),
        row(
            "BatchRankinPassOrReturnNotExecutableYet",
            batch_closed,
            False,
            "只有正式清单存在且清单内每个证书通过，或失败者全部回流 PDEC/SAE 后，批量门才关闭。",
            f"{BATCH_ATOM} AND {PDEC_SAE_ATOM}",
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 独立接受仍不能关闭；当前最小缺口是 formal corridor inventory。",
            INVENTORY_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行全 Rankin 走廊证书全集清单路由。"""
    previous = load_json(paths["previous"])
    acceptance_text = read_text(paths["acceptance"])
    sample = load_json(paths["sample"])
    scan = scan_json_corpus(DOCS)
    rows = build_rows(previous, acceptance_text, sample, scan)
    evidence_paths = [paths["previous"], paths["acceptance"], paths["sample"]]
    return {
        "certificate_type": "prime_matrix_full_rankin_ledger_inventory_router",
        "status": "full_rankin_ledger_narrowed_to_formal_inventory_missing",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "dstructure_rankin_full_acceptance_closed": False,
        "formal_colored_corridor_inventory_found": bool(scan["inventory_like"]),
        "rankin_like_json_count": len(scan["rankin_like"]),
        "rankin_like_json": scan["rankin_like"],
        "inventory_like_json": scan["inventory_like"],
        "parse_error_count": len(scan["parse_errors"]),
        "current_narrowest_atom": INVENTORY_ATOM,
        "next_after_inventory": BATCH_ATOM,
        "failure_return_atom": PDEC_SAE_ATOM,
        "reduction_formula": (
            f"{OPEN_GATE} => {INVENTORY_ATOM} AND {BATCH_ATOM}; "
            f"failed certificates must return to {PDEC_SAE_ATOM}."
        ),
        "plain_conclusion": (
            "DStructure/Rankin 门的当前最窄缺口已从泛称“正式 Rankin 证书全集未提交”"
            "压缩为 `FormalColoredCorridorInventoryLedger`：必须先给出正式着色走廊全集清单，"
            "才能对每个颜色类运行现有 Rankin 证书审计。仓库当前只发现样本/局部证书，"
            "没有发现全集清单，因此不能关闭最终晋级门。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 全 Rankin 走廊证书全集清单路由器",
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
            "formal_colored_corridor_inventory_found="
            f"{fmt_bool(result['formal_colored_corridor_inventory_found'])}"
        ),
        f"rankin_like_json_count={result['rankin_like_json_count']}",
        (
            "dstructure_rankin_full_acceptance_closed="
            f"{fmt_bool(result['dstructure_rankin_full_acceptance_closed'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "这一步没有尝试用样本证书替代全集。正式清单必须包含每个颜色类的 `P,K,intervals,phase_moduli,allowed_budget`，并给出清单覆盖所有着色走廊的来源证明。",
        "",
        "## 2. 扫描结果",
        "",
        "| path | P | K | intervals | allowed | rankin pass | exact pass |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for item in result["rankin_like_json"]:
        lines.append(
            "| {path} | {p} | {k} | {intervals} | {allowed} | `{rpass}` | `{epass}` |".format(
                path=table_cell(item["path"]),
                p=item.get("p"),
                k=item.get("k"),
                intervals=item.get("interval_count"),
                allowed=item.get("allowed_budget"),
                rpass=fmt_bool(item.get("rankin_budget_pass")),
                epass=fmt_bool(item.get("exact_budget_pass")),
            )
        )
    if not result["rankin_like_json"]:
        lines.append("| none |  |  |  |  |  |  |")
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
            f"新的唯一最窄点是 `{result['current_narrowest_atom']}`。补齐它之后，"
            f"下一步才是 `{result['next_after_inventory']}`；任一失败证书必须回流 `{result['failure_return_atom']}`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--acceptance", type=Path, default=DEFAULT_ACCEPTANCE)
    parser.add_argument("--sample", type=Path, default=DEFAULT_SAMPLE)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "acceptance": args.acceptance,
        "sample": args.sample,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
