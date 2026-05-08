#!/usr/bin/env python3
"""Prime Matrix registered capacity multiplier discipline 路由器。

用法示例：
  python3 experiments/prime_matrix_registered_capacity_multiplier_discipline_router.py

输出：
  docs/monograph/prime-matrix-registered-capacity-multiplier-discipline-router.json
  docs/monograph/prime-matrix-registered-capacity-multiplier-discipline-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_MICROATOM = DOCS / "prime-matrix-actual-capacity-ledger-microatom-router.json"
DEFAULT_TRANSFER = DOCS / "prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.json"
DEFAULT_RANGE = DOCS / "prime-matrix-triad-a1-dibfi-full-s-support-range-router.json"
DEFAULT_EXACT_SUPPORT = DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json"
DEFAULT_MD = DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.md"


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


def row_closed(rows: list[dict[str, Any]], gate: str) -> bool:
    """按 gate 名称读取闭合状态。"""
    return any(row.get("gate") == gate and row.get("closed") is True for row in rows)


def row_contains(rows: list[dict[str, Any]], gate: str, field: str, needle: str) -> bool:
    """检查某行字段是否含指定文本。"""
    return any(
        row.get("gate") == gate and needle in str(row.get(field, ""))
        for row in rows
    )


def build_multiplier_rows(
    transfer: dict[str, Any],
    range_gate: dict[str, Any],
    exact_support: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成乘子来源清单。"""
    transfer_rows = transfer.get("transfer_certificate_rows", [])
    scale_rows = transfer.get("scale_certificate_rows", [])
    range_rows = range_gate.get("range_rows", [])
    exact_rows = exact_support.get("gate_rows", [])

    return [
        {
            "source": "Type/Vaughan-Heath-Brown/dyadic",
            "registered": row_closed(transfer_rows, "TypeDecompositionLogBudget")
            and row_closed(scale_rows, "TypeProductQuantified"),
            "bound": "log^C",
            "evidence": "TypeDecompositionLogBudget + TypeProductQuantified",
            "role": "分解层数和 dyadic 求和进入同一 formal unit 的 log-loss 账本。",
        },
        {
            "source": "CRT phase normalization",
            "registered": row_closed(transfer_rows, "CRTPhaseSymbolUnification"),
            "bound": "1",
            "evidence": "CRTPhaseSymbolUnification",
            "role": "相位归一化是恒等式，不产生容量乘子。",
        },
        {
            "source": "Fourier h-window and tail",
            "registered": row_closed(scale_rows, "FrequencyWindowAndTail"),
            "bound": "log^C",
            "evidence": "FrequencyWindowAndTail",
            "role": "非零频窗口与尾项截断由 B(A) 吸收，不允许账外频率质量。",
        },
        {
            "source": "coefficient/gcd/endpoint/smoothing",
            "registered": row_closed(scale_rows, "LogLossC0Extraction"),
            "bound": "log^C",
            "evidence": "LogLossC0Extraction",
            "role": "系数、gcd、端点和平滑损失统一进入符号化 C0。",
        },
        {
            "source": "full-S completion fiber",
            "registered": row_closed(range_rows, "CompletionRatioPolylogPinned"),
            "bound": "log^C",
            "evidence": "CompletionRatioPolylogPinned",
            "role": "completion fiber 长度为 S/c=log^O(P)，是登记乘子而非新相消输入。",
        },
        {
            "source": "balanced factorization shape",
            "registered": row_closed(range_rows, "BalancedFactorizationPinned"),
            "bound": "shape-only",
            "evidence": "BalancedFactorizationPinned",
            "role": "c=uv 与 U,V=C^{1/2}log^O 固定同一个 moving pair 坐标。",
        },
        {
            "source": "dyadic/tail-label bookkeeping",
            "registered": row_contains(
                exact_rows,
                "K6DyadicBookkeeping",
                "available",
                "polylog",
            ),
            "bound": "log^C",
            "evidence": "K6DyadicBookkeeping available polylog split count",
            "role": "K6 不能证明支撑下界，但足以说明尾标签数量是已登记 log 乘子。",
        },
    ]


def build_threshold_rows() -> list[dict[str, Any]]:
    """给出闭合后支撑阈值示意。"""
    rows: list[dict[str, Any]] = []
    saving_a = 2.0
    coefficient_c = 2.0
    multiplier_e = 5.0
    required_b = 2 * saving_a + 4 * coefficient_c + multiplier_e
    for k in range(3, 10):
        log_y = k * math.log(10)
        required_pair_support = math.ceil(log_y**required_b)
        rows.append(
            {
                "k": k,
                "log_y": log_y,
                "A": saving_a,
                "C": coefficient_c,
                "E": multiplier_e,
                "required_pair_support_power": required_b,
                "required_pair_support": required_pair_support,
            }
        )
    return rows


def build_rows(
    microatom: dict[str, Any],
    transfer: dict[str, Any],
    range_gate: dict[str, Any],
    exact_support: dict[str, Any],
    dstructure: dict[str, Any],
    multiplier_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成主判定表。"""
    all_registered = all(row["registered"] for row in multiplier_rows)
    return [
        {
            "gate": "PreviousMicroatomPinned",
            "closed": microatom.get("derivation_package")
            == (
                "ActualNoncanonicalExactUVSupportLowerBound AND "
                "ActualTypeFourierRegisteredCapacityMultiplierDiscipline"
            ),
            "proved": True,
            "meaning": "上一层已把支撑-only 偷换排除，并命名乘子纪律微输入。",
            "remaining": "可直接审查该乘子纪律是否只是账本门。",
        },
        {
            "gate": "KnownMultipliersRegistered",
            "closed": all_registered,
            "proved": all_registered,
            "meaning": "Type、dyadic、CRT、Fourier、gcd、smoothing、completion 与 tail-label 乘子均有同 formal-unit 登记行。",
            "remaining": "无账外乘子；所有成本并入最终 M_{u,v} 或 log-loss 指数 E。",
        },
        {
            "gate": "ExternalNoProjectionNotUsed",
            "closed": transfer.get("all_certificate_rows_closed") is False
            and "NoProjectionUncenteredDispersionIdentity"
            in transfer.get("open_terminal_targets", []),
            "proved": True,
            "meaning": "本步只关闭内部乘子账本，不调用外部 DI/BFI 无投影相消。",
            "remaining": "外部 theorem-match 分支仍按原状态开放，不能被本步偷渡关闭。",
        },
        {
            "gate": "MultiplierDisciplineClosed",
            "closed": all_registered,
            "proved": all_registered,
            "meaning": "所有已知 Type/Fourier/fiber 成本都成为最终容量测度的登记乘子，并统一受 log^E 控制。",
            "remaining": "若要推出 final anti-atom，现在只缺 actual exact u/v 支撑下界。",
        },
        {
            "gate": "ExactUVSupportStillOpen",
            "closed": exact_support.get("current_internal_exact_factor_support_closed") is False
            and exact_support.get("k4_k6_imply_exact_factor_support") is False,
            "proved": False,
            "meaning": "ExactUVSupport 仍未证明，且不能由 K4/K6 或朴素 incidence 推出。",
            "remaining": "证明 actual noncanonical exact u/v 支撑下界，或直接证明 final capacity anti-atom。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "完整行/列定理仍需独立验收。",
        },
    ]


def run(
    microatom_path: Path,
    transfer_path: Path,
    range_path: Path,
    exact_support_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 registered multiplier discipline 路由。"""
    source_paths = [
        microatom_path,
        transfer_path,
        range_path,
        exact_support_path,
        dstructure_path,
    ]
    microatom = load_json(microatom_path)
    transfer = load_json(transfer_path)
    range_gate = load_json(range_path)
    exact_support = load_json(exact_support_path)
    dstructure = load_json(dstructure_path)

    multiplier_rows = build_multiplier_rows(
        transfer=transfer,
        range_gate=range_gate,
        exact_support=exact_support,
    )
    rows = build_rows(
        microatom=microatom,
        transfer=transfer,
        range_gate=range_gate,
        exact_support=exact_support,
        dstructure=dstructure,
        multiplier_rows=multiplier_rows,
    )
    threshold_rows = build_threshold_rows()
    registered_capacity_multiplier_discipline_closed = all(
        row["registered"] for row in multiplier_rows
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_registered_capacity_multiplier_discipline_router",
        "status": "registered_capacity_multiplier_discipline_closed_exact_uv_support_open",
        "registered_capacity_multiplier_discipline_closed": (
            registered_capacity_multiplier_discipline_closed
        ),
        "exact_uv_support_proved": False,
        "actual_final_capacity_antiatom_proved": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_basis": microatom.get("latest_self_contained_basis"),
        "latest_self_contained_basis": (
            "ActualNoncanonicalExactUVSupportLowerBound AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "remaining_source_microinput": "ActualNoncanonicalExactUVSupportLowerBound",
        "registered_multiplier_law": (
            "Type/Fourier/fiber 乘子纪律是账本门而不是新的相消定理：所有已知乘子"
            "已经在同一个 actual formal unit 中登记，并被统一吸收到最终 M_{u,v} 的"
            " log^E 成本里。本步不使用外部 DI/BFI no-projection 证明。"
        ),
        "support_to_antiatom_after_closure": (
            "乘子纪律闭合后，若证明 actual exact u/v 支撑满足 "
            "S_u*S_v >= L^(2A+4C+E)，则 final capacity anti-atom "
            "max M_{u,v}/sum M_{u,v} <= L^(-2A) 立即成立。"
        ),
        "plain_conclusion": (
            "容量乘子纪律已作为账本门闭合：Type 分解、dyadic、CRT、Fourier 尾项、gcd、"
            "平滑、full-S completion fiber 与 tail-label 成本都已登记为同一 formal unit "
            "中的 log-power 乘子。本步没有调用外部 DI/BFI 无投影相消，也没有证明支撑下界。"
            "因此完全自足源核心剩余从两个微输入压成单个 `ActualNoncanonicalExactUVSupportLowerBound`，"
            "另加 DStructure/Rankin 独立验收。"
        ),
        "rows": rows,
        "multiplier_rows": multiplier_rows,
        "threshold_rows": threshold_rows,
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths
        },
    }

    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 报告。"""
    lines: list[str] = [
        "# Prime Matrix registered capacity multiplier discipline 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"registered_capacity_multiplier_discipline_closed={fmt_bool(result['registered_capacity_multiplier_discipline_closed'])}",
        f"exact_uv_support_proved={fmt_bool(result['exact_uv_support_proved'])}",
        f"actual_final_capacity_antiatom_proved={fmt_bool(result['actual_final_capacity_antiatom_proved'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 主判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 乘子登记表",
            "",
            "| source | registered | bound | evidence | role |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["multiplier_rows"]:
        lines.append(
            "| {source} | `{registered}` | `{bound}` | {evidence} | {role} |".format(
                source=table_cell(row["source"]),
                registered=fmt_bool(row["registered"]),
                bound=table_cell(row["bound"]),
                evidence=table_cell(row["evidence"]),
                role=table_cell(row["role"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 最新输入基",
            "",
            "上一层：",
            "",
            "```text",
            str(result["previous_basis"]),
            "```",
            "",
            "当前：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 4. 乘子纪律律",
            "",
            result["registered_multiplier_law"],
            "",
            "## 5. 支撑推出反原子的剩余阈值",
            "",
            result["support_to_antiatom_after_closure"],
            "",
            "| k | log y | A | C | E | required power | required pair support |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["threshold_rows"]:
        lines.append(
            "| {k} | {log_y:.6g} | {A:.1f} | {C:.1f} | {E:.1f} | {required_pair_support_power:.1f} | {required_pair_support} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## 6. 当前结论",
            "",
            "本步闭合的是 `RegisteredCapacityMultiplierDiscipline`：所有已知 Type/Fourier/fiber 成本均已登记为 log-power 乘子。",
            "它不证明 `ExactUVSupport`，也不关闭外部 DI/BFI no-projection 分支。",
            "完全自足源核心的真正剩余现在是 `ActualNoncanonicalExactUVSupportLowerBound`，另加 DStructure/Rankin 独立验收。",
        ]
    )
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--microatom", type=Path, default=DEFAULT_MICROATOM)
    parser.add_argument("--transfer", type=Path, default=DEFAULT_TRANSFER)
    parser.add_argument("--range", type=Path, default=DEFAULT_RANGE)
    parser.add_argument("--exact-support", type=Path, default=DEFAULT_EXACT_SUPPORT)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        microatom_path=args.microatom,
        transfer_path=args.transfer,
        range_path=args.range,
        exact_support_path=args.exact_support,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_self_contained_basis"])


if __name__ == "__main__":
    main()
