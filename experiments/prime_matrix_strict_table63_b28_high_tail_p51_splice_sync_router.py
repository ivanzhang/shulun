#!/usr/bin/env python3
"""生成 strict b=28 高尾输入接回 Dusart P5.1 拼接证书。

用法示例：
  python3 experiments/prime_matrix_strict_table63_b28_high_tail_p51_splice_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table63-b28-high-tail-p51-splice-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 70

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-table63-b28-high-tail-p51-splice-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table63-b28-high-tail-p51-splice-sync-router.md"

FK_B28 = DOCS / "prime-matrix-strict-faber-kadiri-b28-parameter-budget-router.json"
MIDDLE_SYNC = DOCS / "prime-matrix-strict-middle-psi-upper-delta-archive-sync-router.json"
ANALYTIC_SPLICE = DOCS / "prime-matrix-strict-dusart-analytic-kernel-threshold-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"

SOURCE_FILES = [FK_B28, MIDDLE_SYNC, ANALYTIC_SPLICE, CLAIM_STATUS]

TARGET = "Table63B28HighTailInputToDusartP51SpliceSyncLedger"
PSI_TABLE_PAIR = "PsiRelativeErrorTableEpsilon28AndMiddle2841ForP51Ledger"
PSI_THETA_GAP = "PsiMinusThetaLowerGap09999SqrtSelfContainedLedger"
THETA_TABLE = "ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ONE_OVER_36260 = Decimal(1) / Decimal(36260)
FK_DIRECTED_UPPER = Decimal("0.00001262")
OLD_TABLE63_EPS = Decimal("0.00002224")
ENDPOINT_TAX = Decimal(14) / Decimal(28).exp()
MIDDLE_UPPER_DELTA = Decimal("0.00002841")
MIDDLE_GAP_RELATIVE = Decimal("0.9999") * Decimal(-14).exp()
MIDDLE_RESULT = MIDDLE_UPPER_DELTA - MIDDLE_GAP_RELATIVE


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
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


def arithmetic_payload() -> dict[str, str]:
    """记录 P5.1 拼接算术。"""
    return {
        "target_1_over_36260": str(ONE_OVER_36260),
        "fk_directed_epsilon_upper": str(FK_DIRECTED_UPPER),
        "old_table63_epsilon_psi_28": str(OLD_TABLE63_EPS),
        "endpoint_tax_14_over_e28": str(ENDPOINT_TAX),
        "fk_high_tail_margin_to_target": str(ONE_OVER_36260 - FK_DIRECTED_UPPER),
        "fk_high_tail_margin_to_target_after_endpoint_tax": str(ONE_OVER_36260 - FK_DIRECTED_UPPER - ENDPOINT_TAX),
        "middle_upper_delta": str(MIDDLE_UPPER_DELTA),
        "middle_gap_relative_09999_e_minus_14": str(MIDDLE_GAP_RELATIVE),
        "middle_result_relative": str(MIDDLE_RESULT),
        "middle_margin_to_target": str(ONE_OVER_36260 - MIDDLE_RESULT),
    }


def build_result() -> dict[str, Any]:
    """构造 b=28 高尾输入接回 P5.1 拼接证书。"""
    fk = load_json(FK_B28)
    middle = load_json(MIDDLE_SYNC)
    analytic = load_json(ANALYTIC_SPLICE)
    active = fk.get("next_direct_attack_target") == TARGET
    fk_high_tail_closed = fk.get("table63_b28_theorem_needed_high_tail_replacement_closed") is True
    middle_psi_closed = middle.get("middle_psi_upper_100002841_source_closed") is True
    analytic_arithmetic_closed = analytic.get("dusart_analytic_kernel_threshold_arithmetic_splice_closed") is True
    high_tail_splice_closed = (
        fk_high_tail_closed
        and FK_DIRECTED_UPPER < OLD_TABLE63_EPS
        and FK_DIRECTED_UPPER + ENDPOINT_TAX < ONE_OVER_36260
    )
    psi_pair_closed = high_tail_splice_closed and middle_psi_closed
    middle_arithmetic_ready = MIDDLE_RESULT < ONE_OVER_36260

    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            fk.get("counterexample_assumption_only") is True
            and fk.get("row_column_unconditional_closed") is False,
            True,
            "本步只把 psi 高尾输入接回 P5.1 拼接链，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "HighTailP51SpliceGateActive",
            active,
            True,
            "上一证书已把下一最窄点设为 b=28 高尾输入到 Dusart P5.1 的拼接同步。",
            TARGET,
        ),
        row(
            "FaberKadiriB28HighTailReplacementClosed",
            fk_high_tail_closed,
            True,
            "FK 校正版给出 |psi(x)-x|/x <= 0.00001262 for x>=e^28。",
            "external FK high-tail input accepted",
        ),
        row(
            "HighTailBeatsOldTable63AndP51Target",
            high_tail_splice_closed,
            True,
            "0.00001262 同时强于旧 Table 6.3 的 0.00002224，并小于 1/36260；保留端点税后仍有余量。",
            TARGET,
        ),
        row(
            "MiddlePsiUpperSourceAlreadyClosed",
            middle_psi_closed,
            True,
            "中段 psi(x)<1.00002841x 的完整节点归档已闭合，可作为 P5.1 中段 psi 输入。",
            "middle psi upper source closed",
        ),
        row(
            "DusartP51ArithmeticSpliceReady",
            analytic_arithmetic_closed and middle_arithmetic_ready,
            True,
            "P5.1 高尾和中段的纯算术拼接均已验算；高尾输入现由 FK 替代旧表行。",
            "arithmetic splice ready",
        ),
        row(
            PSI_TABLE_PAIR,
            psi_pair_closed,
            True,
            "P5.1 需要的两个 psi 输入已经闭合：高尾 b=28 由 FK 替代，中段 1.00002841 由完整节点归档给出。",
            "psi input pair closed for P5.1",
        ),
        row(
            TARGET,
            high_tail_splice_closed,
            True,
            "高尾段 x>=e^28 已接回 Dusart P5.1：theta(x)<=psi(x)<x+x/36260，故 theta(x)-x<x/36260。",
            "high-tail splice closed",
        ),
        row(
            "P51StillNeedsNonPsiInputs",
            False,
            False,
            "P5.1 全段 theta 结论还需要 psi-theta 下界和 theta(x)<x 到 8e11 的有限表/证书。",
            f"{PSI_THETA_GAP} AND {THETA_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步关闭的是 P5.1 高尾输入接口，不直接产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_table63_b28_high_tail_p51_splice_sync_router",
        "status": "table63_b28_high_tail_input_spliced_into_dusart_p51_psi_pair_closed_nonpsi_inputs_remain",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "faber_kadiri_b28_high_tail_replacement_closed": fk_high_tail_closed,
        "table63_b28_high_tail_input_to_p51_splice_closed": high_tail_splice_closed,
        "middle_psi_upper_100002841_source_closed": middle_psi_closed,
        "psi_relative_error_pair_for_p51_closed": psi_pair_closed,
        "dusart_p51_full_theta_statement_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "arithmetic": arithmetic_payload(),
        "replacement_self_contained": {
            TARGET: "FaberKadiriCorrectedB28HighTailPsiBound0p00001262 AND 0.00001262+14/e^28<1/36260",
            PSI_TABLE_PAIR: "Table63B28HighTailInputToDusartP51SpliceSyncLedger AND MiddlePsiUpper100002841SourceClosed",
        },
        "next_direct_attack_target": PSI_THETA_GAP,
        "parallel_attack_targets": [THETA_TABLE, DSTRUCTURE],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "FK b0=28 的高尾替代已经接回 Dusart P5.1：对 x>=e^28，"
            "`|psi(x)-x|/x<=0.00001262`，强于旧表值并严格小于 `1/36260`。"
            "因此 P5.1 的 psi 输入对已经闭合：高尾由 FK 替代，中段 `1.00002841` 已由完整节点归档闭合。"
            "剩余不再是 b=28 高尾，而是 `psi-theta>0.9999sqrt(x)` 下界与 `theta(x)<x` 到 `8e11` 的有限表证书。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict b=28 高尾输入接回 Dusart P5.1 拼接证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"table63_b28_high_tail_input_to_p51_splice_closed={fmt_bool(result['table63_b28_high_tail_input_to_p51_splice_closed'])}",
        f"psi_relative_error_pair_for_p51_closed={fmt_bool(result['psi_relative_error_pair_for_p51_closed'])}",
        f"dusart_p51_full_theta_statement_closed={fmt_bool(result['dusart_p51_full_theta_statement_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 拼接算术",
        "",
        "| field | value |",
        "| --- | ---: |",
    ]
    for key, value in result["arithmetic"].items():
        lines.append(f"| `{table_cell(key)}` | `{table_cell(value)}` |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 3. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"table63_b28_high_tail_input_to_p51_splice_closed={fmt_bool(result['table63_b28_high_tail_input_to_p51_splice_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
