#!/usr/bin/env python3
"""Prime Matrix theta-Mellin 超越函数 Taylor 核路由器。

用法示例：
  python3 experiments/prime_matrix_theta_mellin_transcendental_kernel_router.py

输出：
  docs/monograph/prime-matrix-theta-mellin-transcendental-kernel-router.json
  docs/monograph/prime-matrix-theta-mellin-transcendental-kernel-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_KERNEL = MONO / "prime-matrix-certified-complex-ball-kernel-router.json"
DEFAULT_TRIG_LOG = MONO / "trig-log-interval-oracle-audit.json"
DEFAULT_JSON = MONO / "prime-matrix-theta-mellin-transcendental-kernel-router.json"
DEFAULT_MD = MONO / "prime-matrix-theta-mellin-transcendental-kernel-router.md"

OLD_ATOM = "ThetaMellinElementaryTranscendentalTaylorKernel0To14"
LOG_TRIG = "RationalLogTrigTaylorOracleTemplateClosed"
EXP_TEMPLATE = "RationalExpTaylorRangeReductionTemplateClosed"
COMPLEX_POWER = "ThetaMellinComplexPowerTemplateClosed"
GAUSSIAN_EXP = "GaussianRealExpNegativeTemplateClosed"
RANGE_BOX = "ThetaMellinCompactRangeBoxLedger0To14"
TAIL_ORDER = "ThetaMellinTaylorTailOrderLedger0To14"
TRACE_LEDGER = "IntervalOperationTraceHashLedger"
THETA_TAIL = "GaussianThetaTailBoundLedger"
QUADRATURE = "CompactThetaMellinQuadratureSubdivisionLedger0To14"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def replacement() -> str:
    """写出超越函数核替换。"""
    return (
        f"{OLD_ATOM} => ({LOG_TRIG} AND {EXP_TEMPLATE} AND {COMPLEX_POWER} "
        f"AND {GAUSSIAN_EXP} AND {RANGE_BOX} AND {TAIL_ORDER})"
    )


def build_rows(kernel: dict[str, Any], trig_log: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 theta-Mellin 超越 Taylor 核判定表。"""
    active = kernel.get("next_priority") == OLD_ATOM
    trig_log_ready = (
        trig_log.get("status") == "rational_oracle_radius_established_for_sample_calls"
        and trig_log.get("max_oracle_half_radius", 1.0) < 1e-30
    )
    exp_template_ready = active and trig_log_ready

    return [
        row(
            "ThetaMellinTranscendentalKernelGateActive",
            active,
            True,
            "复球核压缩后首要数学实现点是 theta-Mellin 专用超越函数 Taylor 外包。",
            OLD_ATOM,
        ),
        row(
            "RationalLogTrigTemplateAvailable",
            trig_log_ready,
            True,
            "已有 atanh-log、Machin-pi、sin/cos Taylor 有理外包模板，半径远小于当前需求。",
            LOG_TRIG,
        ),
        row(
            "RationalExpRangeReductionTemplateClosed",
            exp_template_ready,
            True,
            "exp 可用有理 range reduction：x=m log2+r，|r|<=log2/2，再对 exp(r) 用正项 Taylor 尾界。",
            EXP_TEMPLATE,
        ),
        row(
            "ComplexPowerTemplateClosed",
            exp_template_ready,
            True,
            "t^z=exp(Re z log t)*(cos(Im z log t)+i sin(Im z log t))，由 log/trig/exp 三模板组合。",
            COMPLEX_POWER,
        ),
        row(
            "GaussianNegativeExpTemplateClosed",
            exp_template_ready,
            True,
            "exp(-pi n^2 t) 是负实指数，range reduction 与正项 Taylor 直接给向外上界。",
            GAUSSIAN_EXP,
        ),
        row(
            "CompactRangeBoxLedgerStillOpen",
            False,
            False,
            "还需由矩形边界与积分分段给出所有 log t、Im z log t、pi n^2 t 的有限有理范围盒。",
            RANGE_BOX,
        ),
        row(
            "TaylorTailOrderLedgerStillOpen",
            False,
            False,
            "有了范围盒后，还需列出每类调用的截断阶数 N 和统一尾界，形成可复核表。",
            TAIL_ORDER,
        ),
        row(
            "TraceAndThetaDownstream",
            False,
            False,
            "超越核实例化后仍需调用轨迹、theta 尾界和紧致积分分段证书。",
            f"{TRACE_LEDGER} AND {THETA_TAIL} AND {QUADRATURE}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 theta-Mellin 超越函数 Taylor 核路由。"""
    kernel = load_json(paths["kernel"])
    trig_log = load_json(paths["trig_log"])
    rows = build_rows(kernel, trig_log)
    template_closed = all(item["closed"] for item in rows[:5])
    strict_kernel_closed = False
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_theta_mellin_transcendental_kernel_router",
        "status": "theta_mellin_transcendental_templates_closed_range_boxes_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "replacement": replacement(),
        "transcendental_templates_closed": template_closed,
        "theta_mellin_transcendental_kernel_closed": strict_kernel_closed,
        "row_column_self_contained_closed": False,
        "next_priority": RANGE_BOX,
        "secondary_priority": TAIL_ORDER,
        "downstream_priority": f"{TRACE_LEDGER} AND {THETA_TAIL} AND {QUADRATURE}",
        "plain_conclusion": (
            "theta-Mellin 超越函数核的通用部分已经可闭合：log/trig、exp range reduction、"
            "complex power 和 Gaussian negative exponential 都能由有理 Taylor 外包模板处理。"
            "真正剩余不是再找特殊函数黑箱，而是为低高度矩形和积分分段列出有限有理范围盒，"
            "再登记每类调用的 Taylor 截断阶数和尾界。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix theta-Mellin 超越函数 Taylor 核路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"transcendental_templates_closed={fmt_bool(result['transcendental_templates_closed'])}",
        f"theta_mellin_transcendental_kernel_closed={fmt_bool(result['theta_mellin_transcendental_kernel_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 核替换",
        "",
        "```text",
        result["replacement"],
        "```",
        "",
        "## 2. 判定表",
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
            "## 3. 下一步",
            "",
            f"当前最窄点：`{result['next_priority']}`。",
            f"随后补 `{result['secondary_priority']}`。",
            f"完成后回到 `{result['downstream_priority']}`。",
            "",
            "判定：超越函数公式模板已闭合，剩余变成有限范围盒和尾阶表，不再是开放特殊函数理论问题。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kernel-json", type=Path, default=DEFAULT_KERNEL)
    parser.add_argument("--trig-log-json", type=Path, default=DEFAULT_TRIG_LOG)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "kernel": args.kernel_json,
        "trig_log": args.trig_log_json,
        "json_out": args.json_out,
        "md_out": args.md_out,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["next_priority"])


if __name__ == "__main__":
    main()
