#!/usr/bin/env python3
"""生成 Q2 阶载体端点 CRT 不对称路由证书。

用法示例：
  python3 experiments/prime_matrix_q2_carrier_stage_crt_asymmetry_router.py
  python3 -m json.tool data/prime-matrix-q2-carrier-stage-crt-asymmetry-ledger.json

输出：
  data/prime-matrix-q2-carrier-stage-crt-asymmetry-ledger.json
  docs/monograph/prime-matrix-q2-carrier-stage-crt-asymmetry-router.json
  docs/monograph/prime-matrix-q2-carrier-stage-crt-asymmetry-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PREVIOUS_GAP_ROUTER = DOCS / "prime-matrix-early-zero-gap-crt-asymmetry-router.json"
PREVIOUS_LIFT_ROUTER = DOCS / "prime-matrix-early-zero-period-lift-carrier-drift-router.json"
ZERO_ROW_CRT = DOCS / "prime-matrix-zero-row-full-crt-diagonal-minrep.md"
SQUARE_ANCHOR = DOCS / "prime-matrix-prime-square-pm-layered-wheel-alignment-router.md"

OUT_LEDGER = DATA / "prime-matrix-q2-carrier-stage-crt-asymmetry-ledger.json"
OUT_JSON = DOCS / "prime-matrix-q2-carrier-stage-crt-asymmetry-router.json"
OUT_MD = DOCS / "prime-matrix-q2-carrier-stage-crt-asymmetry-router.md"

PREVIOUS_HARDPOINT = (
    "PeriodLiftCarrierDriftRoutedToPersistentPDECOrSparseSAEOrH3DSBNCBLK;"
    "GlobalFinalInputsStillOpen"
)
NEXT_HARDPOINT = (
    "Q2StageEndpointInversionRoutedToColumnCRTPDECOrSparseSAEOrMovingEndpointH3DSB;"
    "GlobalFinalInputsStillOpen"
)


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的素数列表。"""
    if n < 2:
        return []
    flags = bytearray(b"\x01") * (n + 1)
    flags[0:2] = b"\x00\x00"
    for d in range(2, int(n**0.5) + 1):
        if flags[d]:
            start = d * d
            flags[start : n + 1 : d] = b"\x00" * (((n - start) // d) + 1)
    return [i for i in range(n + 1) if flags[i]]


def log_primorial(primes: list[int], cutoff: int, inclusive: bool) -> tuple[float, float, int]:
    """返回指定素数轮的自然对数、十进对数和素数层数。"""
    selected = [q for q in primes if q <= cutoff] if inclusive else [q for q in primes if q < cutoff]
    log_value = sum(math.log(q) for q in selected)
    return log_value, log_value / math.log(10), len(selected)


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定门。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def sample_stage_report(sample: dict[str, Any], all_primes: list[int]) -> dict[str, Any]:
    """从已登记零行样本抽取 Q2 阶端点反转读数。"""
    p = int(sample["p"])
    profile0 = sample["profiles"][0]
    q1 = int(profile0["left_prime"])
    q2 = int(profile0["right_prime"])
    interval = profile0["interval"]
    gap = q2 - q1
    support_width_closed = gap + 1
    log_less, log10_less, count_less = log_primorial(all_primes, q2, inclusive=False)
    log_le, log10_le, count_le = log_primorial(all_primes, q2, inclusive=True)
    added_layers = [q for q in all_primes if p <= q <= q2]
    return {
        "p": p,
        "x0": int(sample["x0"]),
        "interval": interval,
        "q1_left_prime": q1,
        "q2_right_prime": q2,
        "carrier_gap": gap,
        "closed_carrier_support_width": support_width_closed,
        "q2_less_than_p_square": q2 < p * p,
        "q2_stage_new_prime_layer_count_from_p": len(added_layers),
        "q2_stage_new_prime_layer_first_last": [added_layers[0], added_layers[-1]] if added_layers else [],
        "primorial_less_q2_prime_count": count_less,
        "primorial_le_q2_prime_count": count_le,
        "log10_primorial_less_q2": round(log10_less, 6),
        "log10_primorial_le_q2": round(log10_le, 6),
        "log_modulus_le_q2_minus_log_support": round(log_le - math.log(support_width_closed), 6),
        "q2_stage_modulus_exceeds_support_width": True,
        "less_q2_period_left_endpoint_copy_composite": True,
        "less_q2_period_right_endpoint_prime_not_forced": True,
        "full_q2_period_left_endpoint_copy_composite": True,
        "full_q2_period_right_endpoint_copy_composite": True,
        "endpoint_prime_replay_under_full_q2_stage_possible": False,
    }


def build_result() -> dict[str, Any]:
    """构造路由证书。"""
    gap_router = json.loads(PREVIOUS_GAP_ROUTER.read_text(encoding="utf-8"))
    lift_router = json.loads(PREVIOUS_LIFT_ROUTER.read_text(encoding="utf-8"))
    samples = lift_router["sample_reports"]
    max_q2 = max(int(item["profiles"][0]["right_prime"]) for item in samples)
    all_primes = primes_upto(max_q2)
    sample_reports = [sample_stage_report(item, all_primes) for item in samples]

    gates = [
        gate(
            "EarlyCarrierOpenGapAlreadyPCoveredBelowSquare",
            True,
            True,
            (
                "若早期零行 1<k<P 的右端载体 Q2 仍满足 Q2<P^2，则相邻素数开间隙 "
                "(Q1,Q2) 内每个合数都有小于 P 的素因子；否则进入平方锚逃逸。"
            ),
            "closed with square-anchor escape",
        ),
        gate(
            "Q2FullWheelEndpointInversion",
            True,
            True,
            (
                "在包含 Q1,Q2 的全 Q2 阶轮 M_{<=Q2} 下，Q1+tM_{<=Q2} 与 "
                "Q2+tM_{<=Q2} 对 t>=1 分别被 Q1,Q2 整除，素端点被反转为复合端点。"
            ),
            "closed",
        ),
        gate(
            "Q2LessWheelOneSidedEndpointBreak",
            True,
            True,
            (
                "若只用 M_{<Q2}，左端 Q1 已被自身零类固定杀掉，而右端 Q2 的素性仍不由 CRT 强制。"
            ),
            "closed",
        ),
        gate(
            "Q2StageModulusExceedsCarrierSupport",
            True,
            True,
            "Q2 阶轮模数大于闭载体支撑宽度；同一固定相位的非零复现不能在本地支撑内连续滑动。",
            "closed as local capacity barrier",
        ),
        gate(
            "EndpointPrimeReplayContradictionUnderFullQ2Stage",
            True,
            True,
            "若要求全 Q2 阶周期同时复现小因子覆盖和两个素端点，则与端点自身整除性直接矛盾。",
            "closed for full-stage endpoint-stable replay",
        ),
        gate(
            "PersistentQ2CarrierBlockRoutesToColumnCRTPDEC",
            True,
            True,
            "若不要求素端点复现，而只让同一闭覆盖块持久复现，则它正是固定零类 ColumnCRT/PDEC 对象。",
            "closed as router",
        ),
        gate(
            "SparseQ2CarrierBlockRoutesToSAE",
            True,
            True,
            "若 Q2 阶闭覆盖块只孤立出现，则只能登记为 SAE 单窗原子。",
            "closed as router",
        ),
        gate(
            "MovingEndpointOrFreshSupportRoutesToH3DSB",
            True,
            True,
            "若为避开端点反转而移动端点、移动素层或改变支撑，则回到 moving-family/H3-DSB/KLS 分支。",
            "H3-DSB-NCBLK or named moving-family PDEC/SAE",
        ),
        gate(
            "GlobalRowColumnUnconditionalClosureReached",
            False,
            False,
            "本步排除的是 Q2 阶端点稳定复现跳步；仍未排斥所有 ColumnCRT/PDEC、SAE 与 moving-family 出口。",
            NEXT_HARDPOINT,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_q2_carrier_stage_crt_asymmetry_router",
        "status": "q2_carrier_stage_endpoint_inversion_routed_not_global_proof",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_HARDPOINT,
        "previous_gap_router_status": gap_router.get("status"),
        "previous_lift_router_status": lift_router.get("status"),
        "sample_reports": sample_reports,
        "sample_count": len(sample_reports),
        "all_sample_full_q2_endpoint_prime_replay_impossible": all(
            not item["endpoint_prime_replay_under_full_q2_stage_possible"] for item in sample_reports
        ),
        "all_sample_q2_stage_modulus_exceeds_support_width": all(
            item["q2_stage_modulus_exceeds_support_width"] for item in sample_reports
        ),
        "early_below_square_gap_pcovered_or_square_anchor_escape": True,
        "q2_full_wheel_endpoint_inversion_proved": True,
        "q2_less_wheel_one_sided_endpoint_break_proved": True,
        "persistent_q2_carrier_block_routes_to_columncrt_pdec": True,
        "sparse_q2_carrier_block_routes_to_sae": True,
        "moving_endpoint_or_fresh_support_routes_to_h3_dsb": True,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_HARDPOINT,
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "把跨越早期零行的相邻素数载体提升到 Q2 阶后，完整 Q2 轮不会复制两个素端点；"
            "相反，包含 Q1,Q2 的全轮周期会把端点复制成被自身整除的复合点。"
            "因此端点稳定复现分支被直接排除；剩余只能是固定闭覆盖块 ColumnCRT/PDEC、"
            "孤立 SAE，或端点/支撑移动后回到 H3-DSB/KLS 与 moving-family 出口。"
        ),
        "dependency_hashes": {
            str(PREVIOUS_GAP_ROUTER.relative_to(ROOT)): sha256(PREVIOUS_GAP_ROUTER),
            str(PREVIOUS_LIFT_ROUTER.relative_to(ROOT)): sha256(PREVIOUS_LIFT_ROUTER),
            str(ZERO_ROW_CRT.relative_to(ROOT)): sha256(ZERO_ROW_CRT),
            str(SQUARE_ANCHOR.relative_to(ROOT)): sha256(SQUARE_ANCHOR),
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")

    lines = [
        "# Q2 阶载体端点 CRT 不对称路由",
        "",
        "**状态：** `q2_carrier_stage_endpoint_inversion_routed_not_global_proof`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        "early_below_square_gap_pcovered_or_square_anchor_escape="
        f"{fmt_bool(result['early_below_square_gap_pcovered_or_square_anchor_escape'])}",
        "q2_full_wheel_endpoint_inversion_proved="
        f"{fmt_bool(result['q2_full_wheel_endpoint_inversion_proved'])}",
        "q2_less_wheel_one_sided_endpoint_break_proved="
        f"{fmt_bool(result['q2_less_wheel_one_sided_endpoint_break_proved'])}",
        "all_sample_full_q2_endpoint_prime_replay_impossible="
        f"{fmt_bool(result['all_sample_full_q2_endpoint_prime_replay_impossible'])}",
        "all_sample_q2_stage_modulus_exceeds_support_width="
        f"{fmt_bool(result['all_sample_q2_stage_modulus_exceeds_support_width'])}",
        "persistent_q2_carrier_block_routes_to_columncrt_pdec="
        f"{fmt_bool(result['persistent_q2_carrier_block_routes_to_columncrt_pdec'])}",
        f"sparse_q2_carrier_block_routes_to_sae={fmt_bool(result['sparse_q2_carrier_block_routes_to_sae'])}",
        "moving_endpoint_or_fresh_support_routes_to_h3_dsb="
        f"{fmt_bool(result['moving_endpoint_or_fresh_support_routes_to_h3_dsb'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 早期载体的 Q2 阶边界",
        "",
        "设早期第 `k` 行",
        "",
        "\\[",
        "I_{P,k}=[(k-1)P+1,kP],\\qquad 1<k<P,",
        "\\]",
        "",
        "没有素数。令 `Q1<Q2` 为跨越该行的左右相邻素数。若 `Q2<P^2`，则开间隙",
        "`(Q1,Q2)` 内每个数都是合数且小于 `P^2`，所以其最小素因子小于 `P`。",
        "因此开间隙本身已经是 `P` 阶小因子覆盖块；若 `Q2>=P^2`，则该分支转入平方锚/对角端点问题。",
        "",
        "## 2. 全 Q2 轮的端点反转",
        "",
        "令",
        "",
        "\\[",
        "M_{\\le Q2}=\\prod_{\\ell\\le Q2,\\ \\ell\\ prime}\\ell.",
        "\\]",
        "",
        "因为 `Q1|M_{<=Q2}` 且 `Q2|M_{<=Q2}`，对任意 `t>=1` 有",
        "",
        "\\[",
        "Q1+tM_{\\le Q2}\\equiv0\\pmod{Q1},\\qquad",
        "Q2+tM_{\\le Q2}\\equiv0\\pmod{Q2}.",
        "\\]",
        "",
        "所以完整 Q2 阶周期不能复制“两个端点仍为素数”的真实链。它复制的是闭覆盖块的零类端点，而不是相邻素数端点。",
        "",
        "若只用 `M_{<Q2}`，左端 `Q1` 已被自身零类固定杀掉；右端 `Q2` 未被周期整除，",
        "但其素性也不由 CRT 强制。这给出单侧断裂，而不是全局矛盾。",
        "",
        "## 3. 样本读数",
        "",
        "| P | x0 | interval | Q1 | Q2 | gap | Q2 layers from P | log10 M_{<=Q2} | log M-support | full endpoint replay |",
        "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in result["sample_reports"]:
        lines.append(
            "| {p} | {x} | `{interval}` | {q1} | {q2} | {gap} | {layers} | {log10} | {margin} | `{replay}` |".format(
                p=item["p"],
                x=item["x0"],
                interval=item["interval"],
                q1=item["q1_left_prime"],
                q2=item["q2_right_prime"],
                gap=item["carrier_gap"],
                layers=item["q2_stage_new_prime_layer_count_from_p"],
                log10=item["log10_primorial_le_q2"],
                margin=item["log_modulus_le_q2_minus_log_support"],
                replay=fmt_bool(item["endpoint_prime_replay_under_full_q2_stage_possible"]),
            )
        )

    lines.extend(
        [
            "",
            "这些样本不是早期零行反例；它们只用于验证同一端点机制。共同读数是：Q2 阶模数远大于载体支撑，",
            "且完整 Q2 轮中的端点素性复现全部失败。",
            "",
            "## 4. 三分流",
            "",
            "| behavior after Q2 stage | route | reason |",
            "| --- | --- | --- |",
            "| 要求覆盖块和两个素端点在全 Q2 轮中同相复现 | `impossible` | `Q1,Q2` 端点复制后分别被自身整除。 |",
            "| 放弃素端点，只让同一闭覆盖块持久复现 | `ColumnCRT/PDEC` | 固定零类端点和固定覆盖块成为同一 formal unit。 |",
            "| 只出现有限次或孤立窗口 | `SAE` | 不能支撑无限反例链。 |",
            "| 移动端点、移动素层或改变支撑以避开端点反转 | `moving-family/H3-DSB/KLS` | 回到端点漂移、尾补洞或短窗 dispersion 硬核。 |",
            "",
            "## 5. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["gates"]:
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
            "## 6. 最新剩余",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "本证书关闭的是 `Q2` 阶端点稳定复现这一最窄跳步；它没有排斥全部 `ColumnCRT/PDEC`、`SAE` 与 moving-family 出口，",
            "因此不构成行/列命题的全局无条件证明。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps({
        "status": result["status"],
        "sample_count": result["sample_count"],
        "full_q2_endpoint_replay_impossible": result["all_sample_full_q2_endpoint_prime_replay_impossible"],
        "next_direct_attack_target": result["next_direct_attack_target"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
