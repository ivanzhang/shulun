#!/usr/bin/env python3
"""Prime Matrix 顶边临界半段 Euler-Maclaurin replay 路由器。

用法示例：
  python3 experiments/prime_matrix_top_critical_segment_em_replay_router.py

输出：
  docs/monograph/prime-matrix-top-critical-segment-em-replay-router.json
  docs/monograph/prime-matrix-top-critical-segment-em-replay-router.md
"""

from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-top-edge-symmetry-halfstrip-router.json"
DEFAULT_JSON = MONO / "prime-matrix-top-critical-segment-em-replay-router.json"
DEFAULT_MD = MONO / "prime-matrix-top-critical-segment-em-replay-router.md"

OLD_ATOM = "TopCriticalSegmentXiBoxCoverLedgerT14SigmaHalfToOne"
NEW_ATOM = "TopCriticalSegmentEulerMaclaurinDyadicReplayLedgerN32P8Mesh2048"
ROUNDING_ATOM = "DyadicComplexIntervalEulerMaclaurinReplayRoundingLedger"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"

HEIGHT = 14.0
MESH_DENOMINATOR = 2048
CELL_COUNT = 1024
EM_N = 32
EM_P = 8
CENTER_VALUE_FLOOR = 0.1
DERIVATIVE_BOUND_CONTRACT = 64.0

BERNOULLI = {
    2: Fraction(1, 6),
    4: Fraction(-1, 30),
    6: Fraction(1, 42),
    8: Fraction(-1, 30),
    10: Fraction(5, 66),
    12: Fraction(-691, 2730),
    14: Fraction(7, 6),
    16: Fraction(-3617, 510),
}


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
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
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def eta_euler_pair(s: complex, terms: int = 220) -> tuple[complex, complex]:
    """用 Euler 变换近似 eta(s) 与导数，仅作侦察审计。"""
    values = [cmath.exp(-s * math.log(n + 1)) for n in range(terms + 1)]
    derivs = [-math.log(n + 1) * values[n] for n in range(terms + 1)]
    total = 0j
    dtotal = 0j
    weight = 2.0
    for k in range(terms):
        total += values[0] / weight
        dtotal += derivs[0] / weight
        for i in range(terms - k):
            values[i] = values[i] - values[i + 1]
            derivs[i] = derivs[i] - derivs[i + 1]
        weight *= 2.0
    return total, dtotal


def zeta_eta_pair(s: complex) -> tuple[complex, complex]:
    """用 eta(s)/(1-2^(1-s)) 近似 zeta(s) 与导数，仅作侦察审计。"""
    eta, eta_prime = eta_euler_pair(s)
    two_power = cmath.exp((1 - s) * math.log(2))
    denominator = 1 - two_power
    denominator_prime = math.log(2) * two_power
    zeta = eta / denominator
    zeta_prime = (eta_prime * denominator - eta * denominator_prime) / (denominator * denominator)
    return zeta, zeta_prime


def zeta_euler_maclaurin(s: complex, n_cutoff: int = EM_N, p_terms: int = EM_P) -> tuple[complex, float]:
    """Euler-Maclaurin 近似与标准余项粗界，仅作交叉审计。"""
    total = sum(cmath.exp(-s * math.log(n)) for n in range(1, n_cutoff))
    total += cmath.exp((1 - s) * math.log(n_cutoff)) / (s - 1)
    total += 0.5 * cmath.exp(-s * math.log(n_cutoff))
    rising = 1 + 0j
    for k in range(1, p_terms + 1):
        if k == 1:
            rising = s
        else:
            rising *= (s + 2 * k - 3) * (s + 2 * k - 2)
        coeff = float(BERNOULLI[2 * k]) / math.factorial(2 * k)
        total += coeff * rising * cmath.exp(-(s + 2 * k - 1) * math.log(n_cutoff))
    prod = 1 + 0j
    for j in range(0, 2 * p_terms + 1):
        prod *= s + j
    remainder_bound = (
        abs(prod)
        * 2.0
        / ((2.0 * math.pi) ** (2 * p_terms + 1))
        * n_cutoff ** (-s.real - 2 * p_terms)
        / (s.real + 2 * p_terms)
    )
    return total, remainder_bound


def audit_grid() -> dict[str, Any]:
    """扫描 1024 段中心，估计最小模和最大导数。"""
    min_abs = float("inf")
    min_sigma = 0.0
    min_value = 0j
    max_derivative = 0.0
    max_derivative_sigma = 0.0
    max_em_remainder = 0.0
    max_cross_error = 0.0
    for j in range(CELL_COUNT):
        sigma = 0.5 + (j + 0.5) / MESH_DENOMINATOR
        s = sigma + HEIGHT * 1j
        zeta_eta, zeta_prime = zeta_eta_pair(s)
        zeta_em, em_remainder = zeta_euler_maclaurin(s)
        abs_value = abs(zeta_eta)
        derivative_abs = abs(zeta_prime)
        if abs_value < min_abs:
            min_abs = abs_value
            min_sigma = sigma
            min_value = zeta_eta
        if derivative_abs > max_derivative:
            max_derivative = derivative_abs
            max_derivative_sigma = sigma
        max_em_remainder = max(max_em_remainder, em_remainder)
        max_cross_error = max(max_cross_error, abs(zeta_eta - zeta_em))
    half_width = 1.0 / (2.0 * MESH_DENOMINATOR)
    propagation_loss = DERIVATIVE_BOUND_CONTRACT * half_width
    certified_margin_if_replay_passes = CENTER_VALUE_FLOOR - propagation_loss
    return {
        "height": HEIGHT,
        "sigma_range": ["1/2", "1"],
        "mesh_denominator": MESH_DENOMINATOR,
        "cell_count": CELL_COUNT,
        "center_value_floor_contract": CENTER_VALUE_FLOOR,
        "derivative_bound_contract": DERIVATIVE_BOUND_CONTRACT,
        "half_cell_width": half_width,
        "propagation_loss_contract": propagation_loss,
        "certified_margin_if_replay_passes": certified_margin_if_replay_passes,
        "audit_min_center_abs": min_abs,
        "audit_min_center_sigma": min_sigma,
        "audit_min_center_value_re": min_value.real,
        "audit_min_center_value_im": min_value.imag,
        "audit_max_derivative_abs": max_derivative,
        "audit_max_derivative_sigma": max_derivative_sigma,
        "audit_max_em_remainder_bound": max_em_remainder,
        "audit_max_eta_em_cross_error": max_cross_error,
        "audit_margin_over_floor": min_abs - CENTER_VALUE_FLOOR,
        "audit_derivative_slack_factor": DERIVATIVE_BOUND_CONTRACT / max_derivative,
        "replay_contract_n": EM_N,
        "replay_contract_p": EM_P,
    }


def proof_contract() -> list[str]:
    """写出顶边临界半段的有限 replay 证明合同。"""
    return [
        "把 [1/2,1] 分成 1024 个 dyadic 小段，中心 c_j=1/2+(j+1/2)/2048。",
        "对每个中心 s_j=c_j+14i，用 Euler-Maclaurin 公式 N=32, p=8 给 zeta(s_j) 的复区间盒。",
        "每个中心盒必须证明 |zeta(s_j)|>=1/10；xi 的其他因子在顶边上非零，所以 zeta 非零等价于 xi 非零。",
        "同时用同一 Euler-Maclaurin replay 或 Cauchy 盒证明整段水平导数 |d zeta/d sigma|<=64。",
        "任意点离中心距离至多 1/4096，因此 |zeta(s)|>=1/10-64/4096=0.084375>0。",
        "所有中心值、导数界、余项界与父 trace hash 进入 dyadic complex interval replay 账本。",
    ]


def build_rows(previous: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Euler-Maclaurin replay 判定表。"""
    active = previous.get("next_priority") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    compression_ready = previous.get("top_edge_full_segment_compressed") is True
    audit_supports_contract = (
        audit["audit_min_center_abs"] > CENTER_VALUE_FLOOR
        and audit["audit_max_derivative_abs"] < DERIVATIVE_BOUND_CONTRACT
        and audit["certified_margin_if_replay_passes"] > 0
    )
    return [
        row(
            "TopCriticalSegmentGateActive",
            active,
            True,
            "上一层已把顶边自足剩余压缩到 Im(s)=14, 1/2<=Re(s)<=1。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理低高度解析证书，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "SymmetryAndEulerProductCompressionImported",
            compression_ready,
            True,
            "顶边左半和右外段已关闭，只需临界半段。",
            "critical half segment only.",
        ),
        row(
            "FloatReconnaissanceSupportsWideMargin",
            audit_supports_contract,
            False,
            (
                f"侦察最小 |zeta|≈{audit['audit_min_center_abs']:.12f}，"
                f"最大水平导数≈{audit['audit_max_derivative_abs']:.12f}，"
                "远优于 0.1/64 合同。"
            ),
            "不能作为自足证明，只用于确定可行证书参数。",
        ),
        row(
            "CenterDerivativePropagationLemmaClosed",
            audit["certified_margin_if_replay_passes"] > 0,
            True,
            "若中心值 >=1/10 且导数 <=64，则每段内 |zeta|>=0.084375，因而 xi 非零。",
            "finite replay remains.",
        ),
        row(
            "ExactDyadicEulerMaclaurinReplayStillMissing",
            False,
            False,
            "还需把 1024 个中心值和导数界用有理区间 Euler-Maclaurin replay 实际登记。",
            f"{NEW_ATOM} AND {ROUNDING_ATOM}",
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "旧顶边临界半段盒账本已压缩为有限 Euler-Maclaurin replay，但严格自足尚未闭合。",
            NEW_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行顶边临界半段 Euler-Maclaurin replay 路由。"""
    previous = load_json(paths["previous"])
    audit = audit_grid()
    rows = build_rows(previous, audit)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_top_critical_segment_em_replay_router",
        "status": "top_critical_segment_reduced_to_em_replay_ledger_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "top_critical_segment_compressed_to_em_replay": True,
        "top_critical_segment_self_contained_closed": False,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {OLD_ATOM: NEW_ATOM},
        "audit": audit,
        "proof_contract": proof_contract(),
        "next_priority": NEW_ATOM,
        "secondary_priority": ROUNDING_ATOM,
        "tertiary_priority": WINDING_ATOM,
        "plain_conclusion": (
            "顶边临界半段已压成一个具体有限 replay 账本：1024 个 dyadic 小段、Euler-Maclaurin "
            "N=32,p=8 中心值证书与 |zeta'|<=64 导数证书。浮点侦察显示最小 |zeta| 约 0.10547，"
            "导数约 0.77566，合同余量很宽；但严格自足仍需把这些值写成有理区间 replay。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    audit = result["audit"]
    lines = [
        "# Prime Matrix 顶边临界半段 Euler-Maclaurin replay 路由器",
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
            "top_critical_segment_compressed_to_em_replay="
            f"{fmt_bool(result['top_critical_segment_compressed_to_em_replay'])}"
        ),
        f"top_critical_segment_self_contained_closed={fmt_bool(result['top_critical_segment_self_contained_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 侦察参数",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| height | `{audit['height']}` |",
        f"| sigma range | `{audit['sigma_range']}` |",
        f"| mesh denominator | `{audit['mesh_denominator']}` |",
        f"| cell count | `{audit['cell_count']}` |",
        f"| EM N | `{audit['replay_contract_n']}` |",
        f"| EM p | `{audit['replay_contract_p']}` |",
        f"| center floor contract | `{audit['center_value_floor_contract']}` |",
        f"| derivative bound contract | `{audit['derivative_bound_contract']}` |",
        f"| propagation loss | `{audit['propagation_loss_contract']:.12f}` |",
        f"| certified margin if replay passes | `{audit['certified_margin_if_replay_passes']:.12f}` |",
        f"| audit min center abs | `{audit['audit_min_center_abs']:.12f}` |",
        f"| audit min center sigma | `{audit['audit_min_center_sigma']:.12f}` |",
        f"| audit max derivative abs | `{audit['audit_max_derivative_abs']:.12f}` |",
        f"| audit derivative slack factor | `{audit['audit_derivative_slack_factor']:.6f}` |",
        f"| audit max EM remainder bound | `{audit['audit_max_em_remainder_bound']:.6e}` |",
        f"| audit max eta/EM cross error | `{audit['audit_max_eta_em_cross_error']:.6e}` |",
        "",
        "## 2. 有限证明合同",
        "",
    ]
    for index, item in enumerate(result["proof_contract"], start=1):
        lines.append(f"{index}. {item}")
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
            "## 4. 下一步",
            "",
            f"严格自足最窄点：`{result['next_priority']}`。",
            f"并行实现门：`{result['secondary_priority']}`。",
            f"之后仍需：`{result['tertiary_priority']}`。",
            "",
            "判定：已经不是开放解析问题，而是一个具体有限有理区间 replay 账本。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
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
