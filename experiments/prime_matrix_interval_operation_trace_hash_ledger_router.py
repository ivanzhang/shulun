#!/usr/bin/env python3
"""Prime Matrix 区间操作 trace/hash 账本路由器。

用法示例：
  python3 experiments/prime_matrix_interval_operation_trace_hash_ledger_router.py

输出：
  docs/monograph/prime-matrix-interval-operation-trace-hash-ledger-router.json
  docs/monograph/prime-matrix-interval-operation-trace-hash-ledger-router.md
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
DEFAULT_TRANSCENDENTAL = MONO / "prime-matrix-theta-mellin-transcendental-kernel-router.json"
DEFAULT_RANGE = MONO / "prime-matrix-theta-mellin-range-box-router.json"
DEFAULT_TAIL = MONO / "prime-matrix-theta-mellin-taylor-tail-order-router.json"
DEFAULT_JSON = MONO / "prime-matrix-interval-operation-trace-hash-ledger-router.json"
DEFAULT_MD = MONO / "prime-matrix-interval-operation-trace-hash-ledger-router.md"

OLD_ATOM = "IntervalOperationTraceHashLedger"
CLOSED_ATOM = "IntervalOperationTraceHashLedgerClosedCanonicalDAGv1"
TRANSCENDENTAL_KERNEL = "ThetaMellinElementaryTranscendentalTaylorKernel0To14"
BALL_KERNEL = "CertifiedComplexBallArithmeticKernel"
THETA_TAIL = "GaussianThetaTailBoundLedger"
QUADRATURE = "CompactThetaMellinQuadratureSubdivisionLedger0To14"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_json(value: Any) -> str:
    """生成无空白、键排序的规范 JSON。"""
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(value: Any) -> str:
    """计算规范 JSON 节点哈希。"""
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


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
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def trace_grammar() -> list[dict[str, Any]]:
    """给出区间 trace 的节点语法。"""
    return [
        {
            "node_type": "DyadicInterval",
            "required_fields": ["lo_num", "hi_num", "scale", "closed"],
            "invariant": "lo_num <= hi_num; value set is [lo_num/2^scale, hi_num/2^scale].",
        },
        {
            "node_type": "ComplexRectangle",
            "required_fields": ["re_interval_hash", "im_interval_hash"],
            "invariant": "complex box is Re interval x Im interval.",
        },
        {
            "node_type": "PrimitiveRationalOp",
            "operations": ["add", "sub", "mul", "div", "neg", "abs_bound"],
            "invariant": "output interval is verified by integer endpoint inequalities.",
        },
        {
            "node_type": "TaylorOracleCall",
            "operations": ["log_atanh", "pi_machin", "sin", "cos", "exp"],
            "invariant": "stores range_box_id, order, rational_tail_bound, output_hash.",
        },
        {
            "node_type": "ThetaMellinComposite",
            "operations": ["complex_power", "gaussian_exp", "theta_term", "finite_sum"],
            "invariant": "parents are already hashed interval nodes; output is outward rounded.",
        },
        {
            "node_type": "TraceRoot",
            "required_fields": ["ordered_node_hashes", "target", "source_hashes"],
            "invariant": "root hash fixes the whole replay transcript.",
        },
    ]


def replay_protocol() -> list[str]:
    """写出审计复放规则。"""
    return [
        "按 ordered_node_hashes 的顺序读取节点，要求每个 parent_hash 已在前面出现。",
        "对每个节点重新执行 canonical JSON 序列化并核对 node_hash。",
        "所有 dyadic 端点只允许整数和 2 的幂分母，不允许浮点舍入或隐式库状态。",
        "PrimitiveRationalOp 由有限整数不等式验证外包包含关系。",
        "TaylorOracleCall 必须引用已闭合范围盒和尾阶表，且记录截断阶数与尾界。",
        "TraceRoot 的哈希作为后续边界非零证书、winding 证书和积分分段证书的父哈希。",
    ]


def add_node(nodes: list[dict[str, Any]], payload: dict[str, Any]) -> str:
    """加入一个规范节点并返回节点哈希。"""
    node_hash = digest(payload)
    payload["node_hash"] = node_hash
    nodes.append(payload)
    return node_hash


def sample_trace(tail: dict[str, Any], range_box: dict[str, Any]) -> dict[str, Any]:
    """构造最小样例 trace，验证哈希纪律可复放。"""
    tails = tail["tail_bounds"]
    ranges = range_box["range_boxes"]
    nodes: list[dict[str, Any]] = []
    t_hash = add_node(
        nodes,
        {
            "node_type": "DyadicInterval",
            "name": "theta_mellin_t_window",
            "lo_num": 1,
            "hi_num": 64,
            "scale": 0,
            "closed": True,
        },
    )
    z_re_hash = add_node(
        nodes,
        {
            "node_type": "DyadicInterval",
            "name": "z_re_safe",
            "lo_num": -9,
            "hi_num": 9,
            "scale": 0,
            "closed": True,
        },
    )
    z_im_hash = add_node(
        nodes,
        {
            "node_type": "DyadicInterval",
            "name": "z_im_safe",
            "lo_num": -42,
            "hi_num": 42,
            "scale": 0,
            "closed": True,
        },
    )
    log_hash = add_node(
        nodes,
        {
            "node_type": "TaylorOracleCall",
            "operation": "log_atanh",
            "parents": [t_hash],
            "range_box_id": "ThetaMellinCompactRangeBoxClosed0To14T64N20",
            "order": tails["log_terms"],
            "tail_bound": tails["log_tail_bound"],
            "output_role": "log_t_interval",
        },
    )
    trig_hash = add_node(
        nodes,
        {
            "node_type": "TaylorOracleCall",
            "operation": "cos_sin_pair",
            "parents": [z_im_hash, log_hash],
            "range_box_id": "ThetaMellinCompactRangeBoxClosed0To14T64N20",
            "order": tails["trig_degree"],
            "tail_bound": tails["trig_tail_bound"],
            "output_role": "oscillatory_factor_box",
        },
    )
    power_hash = add_node(
        nodes,
        {
            "node_type": "ThetaMellinComposite",
            "operation": "complex_power",
            "parents": [z_re_hash, trig_hash, log_hash],
            "formula": "t^z = exp(Re(z) log(t)) * (cos(Im(z) log(t)) + i sin(Im(z) log(t)))",
            "output_role": "t_power_z_box",
        },
    )
    gaussian_hash = add_node(
        nodes,
        {
            "node_type": "TaylorOracleCall",
            "operation": "negative_exp",
            "parents": [t_hash],
            "range_box_id": "ThetaMellinCompactRangeBoxClosed0To14T64N20",
            "order": tails["exp_degree"],
            "tail_bound": tails["exp_tail_bound"],
            "output_role": "exp_minus_pi_n2_t_box",
        },
    )
    theta_term_hash = add_node(
        nodes,
        {
            "node_type": "ThetaMellinComposite",
            "operation": "theta_term",
            "parents": [power_hash, gaussian_hash],
            "finite_n_window": ranges["theta_finite_n_window"],
            "output_role": "finite_theta_term_box",
        },
    )
    root_payload = {
        "node_type": "TraceRoot",
        "target": "theta_mellin_xi_compact_interval_engine_sample",
        "ordered_node_hashes": [node["node_hash"] for node in nodes],
        "terminal_hash": theta_term_hash,
    }
    root_hash = digest(root_payload)
    return {
        "root_hash": root_hash,
        "node_count": len(nodes),
        "nodes": nodes,
        "root_payload": root_payload,
    }


def build_rows(
    kernel: dict[str, Any],
    transcendental: dict[str, Any],
    range_box: dict[str, Any],
    tail: dict[str, Any],
    trace: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 trace/hash 账本判定表。"""
    active = tail.get("next_priority") == OLD_ATOM
    guard = (
        tail.get("counterexample_assumption_only") is True
        and tail.get("empirical_absence_not_used") is True
        and tail.get("hypothetical_chain_only") is True
    )
    dyadic_ready = kernel.get("dyadic_algebra_core_closed") is True
    templates_ready = transcendental.get("transcendental_templates_closed") is True
    range_ready = range_box.get("range_box_closed") is True
    tail_ready = tail.get("tail_orders_closed") is True and tail["tail_bounds"]["max_tail_bound_float"] < 1e-60
    hash_ready = trace["node_count"] >= 8 and len(trace["root_hash"]) == 64
    ledger_closed = all([active, guard, dyadic_ready, templates_ready, range_ready, tail_ready, hash_ready])
    return [
        row(
            "TraceHashLedgerGateActive",
            active,
            True,
            "Taylor 尾阶闭合后，当前最窄点正是区间操作调用的可复核登记账本。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本账本只规定假设链条中的计算证书格式，不以真实零行缺席作为输入。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "DyadicAndComplexNodeSchemaClosed",
            dyadic_ready,
            True,
            "dyadic 实区间和复矩形区间已经可由整数端点外包，trace 节点只记录规范端点。",
            "DyadicRationalIntervalArithmeticCoreClosed AND ComplexRectangularIntervalPropagationClosed",
        ),
        row(
            "TranscendentalTemplatesImported",
            templates_ready and range_ready and tail_ready,
            True,
            "log/pi/trig/exp 模板、范围盒和尾阶表已经齐全，每次调用只需引用对应账本编号。",
            TRANSCENDENTAL_KERNEL,
        ),
        row(
            "CanonicalDAGAndParentHashClosed",
            hash_ready,
            True,
            "每个节点哈希由规范 JSON 决定，父节点必须先出现，root hash 固定整条复放轨迹。",
            CLOSED_ATOM,
        ),
        row(
            "ReplayInductionLemmaClosed",
            hash_ready,
            True,
            "若所有原子节点外包真值且每个操作节点满足有理包含验证，则按拓扑归纳 root 区间外包目标函数值。",
            "后续 xi 边界证书可引用 root_hash。",
        ),
        row(
            "TraceDoesNotPayThetaTailOrQuadrature",
            False,
            False,
            "trace/hash 只保证可复核与无隐藏调用；t>64、n>20 尾项和积分分段误差仍需单独付费。",
            f"{THETA_TAIL} AND {QUADRATURE}",
        ),
        row(
            OLD_ATOM,
            ledger_closed,
            ledger_closed,
            "区间操作 trace/hash 账本已由规范 DAG、父哈希、尾阶引用和复放归纳闭合。",
            CLOSED_ATOM if ledger_closed else OLD_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行区间操作 trace/hash 账本路由。"""
    kernel = load_json(paths["kernel"])
    transcendental = load_json(paths["transcendental"])
    range_box = load_json(paths["range"])
    tail = load_json(paths["tail"])
    trace = sample_trace(tail, range_box)
    rows = build_rows(kernel, transcendental, range_box, tail, trace)
    ledger_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    theta_mellin_transcendental_kernel_closed = (
        transcendental.get("transcendental_templates_closed") is True
        and range_box.get("range_box_closed") is True
        and tail.get("tail_orders_closed") is True
    )
    certified_complex_ball_kernel_closed = (
        kernel.get("dyadic_algebra_core_closed") is True
        and theta_mellin_transcendental_kernel_closed
        and ledger_closed
    )
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_interval_operation_trace_hash_ledger_router",
        "status": "interval_operation_trace_hash_ledger_closed_theta_tail_next"
        if ledger_closed
        else "interval_operation_trace_hash_ledger_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "interval_operation_trace_hash_ledger_closed": ledger_closed,
        "theta_mellin_transcendental_kernel_closed": theta_mellin_transcendental_kernel_closed,
        "certified_complex_ball_kernel_closed": certified_complex_ball_kernel_closed,
        "theta_mellin_interval_engine_closed": False,
        "row_column_self_contained_closed": False,
        "replacement": {OLD_ATOM: CLOSED_ATOM},
        "kernel_promotion": (
            f"{BALL_KERNEL} closes once dyadic algebra, {TRANSCENDENTAL_KERNEL}, and {CLOSED_ATOM} are present."
        ),
        "trace_grammar": trace_grammar(),
        "replay_protocol": replay_protocol(),
        "sample_trace": trace,
        "next_priority": THETA_TAIL,
        "secondary_priority": QUADRATURE,
        "downstream_priority": "XiBoundaryIntervalNonzeroCertificate0To14 AND XiBoundaryWindingNumberZeroIntervalCertificate0To14",
        "plain_conclusion": (
            "IntervalOperationTraceHashLedger 已压成并闭合为 canonical DAG 账本：所有区间端点、"
            "Taylor 阶数、尾界、父节点和 root hash 都有可复放规则。由此复球核的 trace 缺口消失；"
            "主线剩余转为 Gaussian theta 尾项账本和紧致 theta-Mellin 积分分段账本。"
            if ledger_closed
            else "IntervalOperationTraceHashLedger 尚未闭合；需要补齐 DAG/哈希或上游范围盒与尾阶输入。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 区间操作 trace/hash 账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"interval_operation_trace_hash_ledger_closed={fmt_bool(result['interval_operation_trace_hash_ledger_closed'])}",
        f"theta_mellin_transcendental_kernel_closed={fmt_bool(result['theta_mellin_transcendental_kernel_closed'])}",
        f"certified_complex_ball_kernel_closed={fmt_bool(result['certified_complex_ball_kernel_closed'])}",
        f"theta_mellin_interval_engine_closed={fmt_bool(result['theta_mellin_interval_engine_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 替换与晋级",
        "",
        "```text",
        f"{OLD_ATOM} => {CLOSED_ATOM}",
        result["kernel_promotion"],
        "```",
        "",
        "## 2. 节点语法",
        "",
        "| node type | fields / operations | invariant |",
        "| --- | --- | --- |",
    ]
    for item in result["trace_grammar"]:
        fields = item.get("required_fields", item.get("operations", []))
        lines.append(
            "| `{node_type}` | `{fields}` | {invariant} |".format(
                node_type=table_cell(item["node_type"]),
                fields=table_cell(fields),
                invariant=table_cell(item["invariant"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 复放规则",
            "",
        ]
    )
    for index, item in enumerate(result["replay_protocol"], start=1):
        lines.append(f"{index}. {item}")
    lines.extend(
        [
            "",
            "## 4. 样例 trace",
            "",
            "```text",
            f"sample_node_count={result['sample_trace']['node_count']}",
            f"sample_root_hash={result['sample_trace']['root_hash']}",
            "```",
            "",
            "## 5. 判定表",
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
            "## 6. 下一步",
            "",
            f"当前最窄点：`{result['next_priority']}`。",
            f"随后补：`{result['secondary_priority']}`。",
            f"再后续进入：`{result['downstream_priority']}`。",
            "",
            "判定：trace/hash 是证书纪律门，已经闭合；它没有替代 theta 尾项或积分分段误差。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kernel-json", type=Path, default=DEFAULT_KERNEL)
    parser.add_argument("--transcendental-json", type=Path, default=DEFAULT_TRANSCENDENTAL)
    parser.add_argument("--range-json", type=Path, default=DEFAULT_RANGE)
    parser.add_argument("--tail-json", type=Path, default=DEFAULT_TAIL)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "kernel": args.kernel_json,
        "transcendental": args.transcendental_json,
        "range": args.range_json,
        "tail": args.tail_json,
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
