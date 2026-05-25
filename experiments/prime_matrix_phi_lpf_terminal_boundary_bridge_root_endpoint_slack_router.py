#!/usr/bin/env python3
"""审计 bridge-root Beatty margin 的 endpoint slack 分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_endpoint_slack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack-router.md

本层承接 q-spine Beatty margin 证书。它把 D-singleton 正 margin 从
P*(q-a*g)-q*q' 继续拆成

    q*(P-q-g*(1+r)) + g*D,

其中 m=P+r 且 D=qr-aP。这样第二个薄 margin 的来源变成显式：
endpoint slack 为 0，但 residual D>0，所以 margin=gD=3954。
该证书仍不证明统一 endpoint-slack law；它只把最新源律压成更小的
EndpointSlackNonnegativeLawOrPDEC。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

BEATTY_JSON = DOCS / (
    "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-beatty-margin-router.json"
)

ENDPOINT_SLACK_LAW = "BridgeRootEndpointSlackNonnegativeLawOrPDEC"
TAIL_OVERHANG_LAW = "RightSelectedTerminalTailOverhangPDEC"
MASS_RATIO_LAW = "BoundaryAdjacentRunMassRatioLawOrPDEC"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
GROUP_ORBIT_INPUT = "AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), BEATTY_JSON]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def transition_label(row: dict[str, Any]) -> str:
    """微转移标签。"""
    return f"m{row['m']} q{row['q']}->{row['q_next']}"


def derive_rows(beatty_payload: dict[str, Any]) -> list[dict[str, Any]]:
    """从 Beatty margin 证书派生 endpoint slack 行。"""
    rows: list[dict[str, Any]] = []
    for row in beatty_payload["micro_transition_rows"]:
        P = int(row["P"])
        q = int(row["q"])
        g = int(row["g"])
        r = int(row["r"])
        a = int(row["beatty_a_floor_qr_over_P"])
        D = int(row["D_from_r"])
        numerator = int(row["phase_delta_num"])
        endpoint_slack = P - q - g * (1 + r)
        endpoint_term = q * endpoint_slack
        residual_term = g * D
        if row["micro_role"] == "D_singleton_bridge_old":
            slack_formula = endpoint_term + residual_term
            slack_identity_closed = slack_formula == numerator
            positive_by_slack_closed = endpoint_slack >= 0 and D > 0 and numerator > 0
            pure_formula = None
            pure_identity_closed = False
        else:
            pure_formula = -P * a * g
            slack_formula = None
            slack_identity_closed = False
            positive_by_slack_closed = False
            pure_identity_closed = pure_formula == numerator and a > 0 and g > 0 and numerator < 0
        rows.append(
            {
                "packet_id": row["packet_id"],
                "atom_key": row["atom_key"],
                "micro_role": row["micro_role"],
                "P": P,
                "m": int(row["m"]),
                "r": r,
                "q": q,
                "q_next": int(row["q_next"]),
                "g": g,
                "a": a,
                "D": D,
                "phase_delta_num": numerator,
                "endpoint_slack": endpoint_slack,
                "endpoint_term_q_times_slack": endpoint_term,
                "residual_term_gD": residual_term,
                "D_singleton_endpoint_slack_formula": slack_formula,
                "D_singleton_endpoint_slack_identity_closed": slack_identity_closed,
                "D_singleton_positive_by_nonnegative_slack_closed": positive_by_slack_closed,
                "A_singleton_pure_negative_formula": pure_formula,
                "A_singleton_pure_negative_identity_closed": pure_identity_closed,
            }
        )
    return rows


def d_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """筛出 D-singleton 行。"""
    return [row for row in rows if row["micro_role"] == "D_singleton_bridge_old"]


def a_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """筛出 A-singleton 行。"""
    return [row for row in rows if row["micro_role"] == "A_singleton_pre_bridge"]


def build_certificate() -> dict[str, Any]:
    """组装 endpoint slack 证书。"""
    beatty_payload = load_json(BEATTY_JSON)
    rows = derive_rows(beatty_payload)
    d_only = d_rows(rows)
    a_only = a_rows(rows)
    a_pure_closed = all(row["A_singleton_pure_negative_identity_closed"] for row in a_only)
    d_identity_closed = all(row["D_singleton_endpoint_slack_identity_closed"] for row in d_only)
    d_slack_nonnegative_closed = all(row["endpoint_slack"] >= 0 for row in d_only)
    d_residual_positive_closed = all(row["D"] > 0 for row in d_only)
    d_positive_by_slack_closed = all(
        row["D_singleton_positive_by_nonnegative_slack_closed"] for row in d_only
    )
    endpoint_slack_reduction_closed = (
        beatty_payload.get("bridge_root_qspine_beatty_margin_closed") is True
        and len(rows) == 4
        and a_pure_closed
        and d_identity_closed
        and d_slack_nonnegative_closed
        and d_residual_positive_closed
        and d_positive_by_slack_closed
    )
    min_slack = min((row["endpoint_slack"] for row in d_only), default=None)
    min_d_margin = min((row["phase_delta_num"] for row in d_only), default=None)
    zero_slack_rows = [transition_label(row) for row in d_only if row["endpoint_slack"] == 0]
    latest_gate = (
        f"{ENDPOINT_SLACK_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} "
        f"AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} "
        f"AND {GROUP_ORBIT_INPUT}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_boundary_bridge_root_endpoint_slack_router",
        "status": "bridge_root_endpoint_slack_reduction_closed_uniform_slack_law_open",
        "verified_date": "2026-05-25",
        "previous_beatty_margin_closed": beatty_payload.get(
            "bridge_root_qspine_beatty_margin_closed"
        )
        is True,
        "micro_transition_count": len(rows),
        "A_singleton_pure_negative_identity_closed": a_pure_closed,
        "D_singleton_endpoint_slack_identity_closed": d_identity_closed,
        "D_singleton_endpoint_slack_nonnegative_finite_closed": d_slack_nonnegative_closed,
        "D_singleton_residual_D_positive_finite_closed": d_residual_positive_closed,
        "D_singleton_positive_by_endpoint_slack_closed": d_positive_by_slack_closed,
        "bridge_root_endpoint_slack_reduction_closed": endpoint_slack_reduction_closed,
        "bridge_root_uniform_endpoint_slack_law_proved": False,
        "right_tail_overhang_pdec_constructed": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "D_singleton_min_endpoint_slack": min_slack,
        "D_singleton_min_positive_margin": min_d_margin,
        "D_singleton_zero_slack_rows": zero_slack_rows,
        "identity": "D-singleton phase_delta_num = q*(P-q-g*(1+r)) + g*D; A-singleton phase_delta_num = -P*a*g",
        "endpoint_slack_rows": rows,
        "next_primary_attack_target": ENDPOINT_SLACK_LAW,
        "latest_open_gate": latest_gate,
        "plain_conclusion": (
            "The thin D-singleton margin is explained by endpoint slack.  The "
            "m761 q601->607 row has endpoint slack 0, so its positive margin is "
            "exactly gD=3954.  The remaining uniform problem is to prove the "
            "endpoint slack nonnegative law, or to name the failure as PDEC."
        ),
        "gate_rows": [
            {
                "gate": "BeattyMarginImported",
                "closed": beatty_payload.get("bridge_root_qspine_beatty_margin_closed") is True,
                "proved": beatty_payload.get("bridge_root_qspine_beatty_margin_closed") is True,
                "meaning": "the q-spine Beatty numerator factorization is imported.",
                "remaining": "none for import",
            },
            {
                "gate": "ASingletonPureNegativeFormula",
                "closed": a_pure_closed,
                "proved": a_pure_closed,
                "meaning": "A-singleton rows satisfy phase_delta_num=-P*a*g<0.",
                "remaining": "finite A-side endpoint formula",
            },
            {
                "gate": "DSingletonEndpointSlackFormula",
                "closed": d_identity_closed,
                "proved": d_identity_closed,
                "meaning": "D-singleton rows satisfy phase_delta_num=q*(P-q-g*(1+r))+gD.",
                "remaining": "finite D-side endpoint formula",
            },
            {
                "gate": "DSingletonPositiveByEndpointSlack",
                "closed": d_positive_by_slack_closed,
                "proved": d_positive_by_slack_closed,
                "meaning": "finite D rows have endpoint slack >=0 and residual D>0, hence positive margin.",
                "remaining": "finite endpoint slack ledger",
            },
            {
                "gate": "BridgeRootUniformEndpointSlackLaw",
                "closed": False,
                "proved": False,
                "meaning": "a uniform law must force endpoint slack nonnegative outside the finite q=607 spine.",
                "remaining": ENDPOINT_SLACK_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "this is a finite endpoint-slack reduction, not a global parity-breaking theorem.",
                "remaining": (
                    f"{ENDPOINT_SLACK_LAW} AND {TAIL_OVERHANG_LAW} AND {MASS_RATIO_LAW} "
                    f"AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}"
                ),
            },
        ],
        "source_hashes": source_hashes(),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF terminal boundary bridge-root endpoint slack 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把 q-spine Beatty margin 继续压成 endpoint slack 非负门。",
        "",
        "```text",
        f"previous_beatty_margin_closed={fmt_bool(payload['previous_beatty_margin_closed'])}",
        f"micro_transition_count={payload['micro_transition_count']}",
        f"A_singleton_pure_negative_identity_closed={fmt_bool(payload['A_singleton_pure_negative_identity_closed'])}",
        f"D_singleton_endpoint_slack_identity_closed={fmt_bool(payload['D_singleton_endpoint_slack_identity_closed'])}",
        f"D_singleton_endpoint_slack_nonnegative_finite_closed={fmt_bool(payload['D_singleton_endpoint_slack_nonnegative_finite_closed'])}",
        f"D_singleton_residual_D_positive_finite_closed={fmt_bool(payload['D_singleton_residual_D_positive_finite_closed'])}",
        f"D_singleton_positive_by_endpoint_slack_closed={fmt_bool(payload['D_singleton_positive_by_endpoint_slack_closed'])}",
        f"bridge_root_endpoint_slack_reduction_closed={fmt_bool(payload['bridge_root_endpoint_slack_reduction_closed'])}",
        f"bridge_root_uniform_endpoint_slack_law_proved={fmt_bool(payload['bridge_root_uniform_endpoint_slack_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "核心恒等式：",
        "",
        "```text",
        payload["identity"],
        "```",
        "",
        "## 1. endpoint slack rows",
        "",
        "| role | transition | r | D | endpoint slack | q*slack | gD | numerator | closed |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in payload["endpoint_slack_rows"]:
        if row["micro_role"] == "D_singleton_bridge_old":
            closed = row["D_singleton_positive_by_nonnegative_slack_closed"]
        else:
            closed = row["A_singleton_pure_negative_identity_closed"]
        lines.append(
            "| `{role}` | {label} | {r} | {D} | {slack} | {qslack} | {gD} | {num} | `{closed}` |".format(
                role=row["micro_role"],
                label=transition_label(row),
                r=row["r"],
                D=row["D"],
                slack=row["endpoint_slack"],
                qslack=row["endpoint_term_q_times_slack"],
                gD=row["residual_term_gD"],
                num=row["phase_delta_num"],
                closed=fmt_bool(closed),
            )
        )
    lines.extend(
        [
            "",
            "## 2. thin margin diagnosis",
            "",
            "```text",
            f"D_singleton_min_endpoint_slack={payload['D_singleton_min_endpoint_slack']}",
            f"D_singleton_min_positive_margin={payload['D_singleton_min_positive_margin']}",
            f"D_singleton_zero_slack_rows={payload['D_singleton_zero_slack_rows']}",
            "```",
            "",
            "## 3. 门控表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in payload["gate_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=cell(row["meaning"]),
                remaining=cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.extend(["", "行/列命题仍未无条件闭合。", ""])
    return "\n".join(lines)


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")


def main() -> None:
    """命令入口。"""
    payload = build_certificate()
    write_outputs(payload)
    print(
        "bridge_root_endpoint_slack_reduction_closed="
        f"{fmt_bool(payload['bridge_root_endpoint_slack_reduction_closed'])}"
    )
    print(
        "D_singleton_min_endpoint_slack="
        f"{payload['D_singleton_min_endpoint_slack']}"
    )
    print(
        "D_singleton_min_positive_margin="
        f"{payload['D_singleton_min_positive_margin']}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
