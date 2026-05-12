#!/usr/bin/env python3
"""生成 strict 直接内部 Dusart theta/PNT 包络路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_direct_internal_dusart_pnt_envelope_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-direct-internal-dusart-pnt-envelope-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-direct-internal-dusart-pnt-envelope-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-direct-internal-dusart-pnt-envelope-router.md"

FEASIBILITY = MONOGRAPH / "prime-matrix-strict-sharp-theta-contour-feasibility-router.json"
FINITE_THETA = MONOGRAPH / "prime-matrix-strict-finite-theta-bridge-self-contained-router.json"
LOW_HEIGHT_EXTERNAL = MONOGRAPH / "prime-matrix-strict-finite-low-height-external-match-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [FEASIBILITY, FINITE_THETA, LOW_HEIGHT_EXTERNAL, CLAIM_STATUS]

TARGET = "DirectInternalDusartThetaPNTEnvelopeLedger"
DUSART_SKELETON = "DusartProposition51ProofSkeletonFormalizationLedger"
DUSART_ANALYTIC = "DusartThetaAnalyticKernelAndThresholdLedger"
DUSART_MIDDLE = "DusartThetaMiddleRangeFiniteVerificationLedger"
LOW_HEIGHT_SELF = "CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger"
FINITE_THETA_CLOSED = "FiniteThetaBridgeBelow20000SelfContainedClosedByPrimeLogCertificate"
EXTERNAL_DUSART = "ThetaEnvelopeTargetAt20000StrictExternalMatchedDusartOneOver36260"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ARXIV_URL = "https://arxiv.org/abs/1002.0442"
ARXIV_ID = "arXiv:1002.0442"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


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


def build_rows(feasibility: dict[str, Any], finite: dict[str, Any], low_external: dict[str, Any]) -> list[dict[str, Any]]:
    """生成直接内部 Dusart/PNT 包络判定表。"""
    guard = (
        feasibility.get("counterexample_assumption_only") is True
        and feasibility.get("direct_unconditional_contradiction_found") is False
        and feasibility.get("row_column_unconditional_closed") is False
    )
    active = feasibility.get("next_direct_attack_target") == TARGET
    finite_ready = finite.get("finite_theta_bridge_below_20000_self_contained_closed") is True
    shallow_tuning_ruled_out = feasibility.get("shallow_constant_tuning_possible") is False
    external_low_ready = low_external.get("finite_low_height_strict_external_matched") is True
    low_self_open = low_external.get("finite_low_height_self_contained_closed") is False
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理统一矛盾场中的解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "DirectInternalDusartGateActive",
            active,
            True,
            "尖锐 contour 可行性证书排除了常数微调后，下一主攻点就是直接内化 Dusart 型 theta/PNT。",
            TARGET,
        ),
        row(
            "FiniteThetaInterfaceAlreadyClosed",
            finite_ready,
            True,
            "0<x<=20000 的有限 theta 桥已由素数 log 证书自足关闭，可作为内部化证明的左端接口。",
            FINITE_THETA_CLOSED,
        ),
        row(
            "ShallowContourTuningRuledOut",
            shallow_tuning_ruled_out,
            True,
            "沿当前 C_Z/C_region 模板微调无法达到 1/36260 目标，必须换成直接 PNT/theta 机制。",
            TARGET,
        ),
        row(
            "ExternalDusartStatementIdentified",
            True,
            False,
            "外部目标是 Dusart 型显式 theta 上界；仓库可引用但不能当作自足证明。",
            f"{ARXIV_ID}: {ARXIV_URL}",
        ),
        row(
            "LowHeightStillExternalOnly",
            external_low_ready and low_self_open,
            False,
            "低高度零点核验已有外部匹配，但要内化 Dusart 证明仍需文内 Turing/无零证书。",
            LOW_HEIGHT_SELF,
        ),
        row(
            "DirectInternalDusartThetaPNTEnvelopeClosed",
            False,
            False,
            "当前仓库尚无完整内化的 Dusart 证明骨架、解析阈值包和中段有限表。",
            f"{DUSART_SKELETON} AND {DUSART_ANALYTIC} AND {DUSART_MIDDLE} AND {LOW_HEIGHT_SELF}",
        ),
        row(
            "ExternalLaneRemainsConditional",
            True,
            False,
            "外部 Dusart 仍可作为条件路线输入，但不改变自足状态。",
            EXTERNAL_DUSART,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "内部化拆包不产生最终反例矛盾。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造直接内部 Dusart/PNT 包络路由证书。"""
    feasibility = load_json(FEASIBILITY)
    finite = load_json(FINITE_THETA)
    low_external = load_json(LOW_HEIGHT_EXTERNAL)
    rows = build_rows(feasibility, finite, low_external)
    replacement = f"{DUSART_SKELETON} AND {DUSART_ANALYTIC} AND {DUSART_MIDDLE} AND {LOW_HEIGHT_SELF}"
    return {
        "certificate_type": "prime_matrix_strict_direct_internal_dusart_pnt_envelope_router",
        "status": "direct_internal_dusart_theta_pnt_envelope_reduced_to_four_author_side_packages",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "direct_internal_dusart_theta_pnt_envelope_closed": False,
        "finite_theta_interface_ready": finite.get("finite_theta_bridge_below_20000_self_contained_closed") is True,
        "shallow_contour_tuning_ruled_out": feasibility.get("shallow_constant_tuning_possible") is False,
        "external_dusart_statement_identified": True,
        "finite_low_height_self_contained_closed": False,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "external_reference": {
            "id": ARXIV_ID,
            "url": ARXIV_URL,
            "role": "external theorem target only; not counted as self-contained proof",
        },
        "replacement_self_contained": {TARGET: replacement},
        "next_direct_attack_target": DUSART_SKELETON,
        "parallel_attack_targets": [DUSART_ANALYTIC, DUSART_MIDDLE, LOW_HEIGHT_SELF],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "直接内化 Dusart 型 theta/PNT 包络已被拆成四个作者侧包：证明骨架形式化、解析核与阈值、"
            "中段有限验证表、低高度 Turing/无零证书。有限 theta 桥已经提供 `x<=20000` 接口，"
            "但仓库内尚无完整 Dusart Proposition 5.1 级证明；外部 arXiv 定理只能维持外部条件路线。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix strict 直接内部 Dusart theta/PNT 包络路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"direct_internal_dusart_theta_pnt_envelope_closed={fmt_bool(result['direct_internal_dusart_theta_pnt_envelope_closed'])}",
        f"finite_theta_interface_ready={fmt_bool(result['finite_theta_interface_ready'])}",
        f"shallow_contour_tuning_ruled_out={fmt_bool(result['shallow_contour_tuning_ruled_out'])}",
        f"finite_low_height_self_contained_closed={fmt_bool(result['finite_low_height_self_contained_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"b3_tv_strict_self_contained_closed={fmt_bool(result['b3_tv_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部目标边界",
        "",
        f"- 外部目标：`{result['external_reference']['id']}`",
        f"- 链接：{result['external_reference']['url']}",
        f"- 角色：{result['external_reference']['role']}",
        "",
        "## 2. 自足替换",
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
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
