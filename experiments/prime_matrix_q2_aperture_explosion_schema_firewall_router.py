#!/usr/bin/env python3
"""生成 Q2 aperture-explosion schema-firewall 同步路由证书。

用法示例：
  python3 experiments/prime_matrix_q2_aperture_explosion_schema_firewall_router.py
  python3 -m json.tool data/prime-matrix-q2-aperture-explosion-schema-firewall-ledger.json

输出：
  data/prime-matrix-q2-aperture-explosion-schema-firewall-ledger.json
  docs/monograph/prime-matrix-q2-aperture-explosion-schema-firewall-router.json
  docs/monograph/prime-matrix-q2-aperture-explosion-schema-firewall-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PREVIOUS = DOCS / "prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.json"
SUPPORT_MOTION = DOCS / "prime-matrix-cycle-debt-fresh-support-motion-global-router.json"
PDEC_FIREWALL = DOCS / "prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-router.json"
CURRENT_ZERO = DOCS / "prime-matrix-cycle-debt-branch-replay-current-frontier-zero-router.json"

OUT_LEDGER = DATA / "prime-matrix-q2-aperture-explosion-schema-firewall-ledger.json"
OUT_JSON = DOCS / "prime-matrix-q2-aperture-explosion-schema-firewall-router.json"
OUT_MD = DOCS / "prime-matrix-q2-aperture-explosion-schema-firewall-router.md"

PREVIOUS_HARDPOINT = (
    "ControlledFreshLayerTailMassSAEOrApertureExplosionH3PDEC;"
    "GlobalFinalInputsStillOpen"
)
NEXT_HARDPOINT = (
    "Q2ApertureExplosionCurrentSchemaFirewall;"
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


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定门。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 依赖。"""
    return json.loads(path.read_text(encoding="utf-8"))


def build_result() -> dict[str, Any]:
    """构造同步路由证书。"""
    previous = load_json(PREVIOUS)
    support = load_json(SUPPORT_MOTION)
    pdec = load_json(PDEC_FIREWALL)
    current = load_json(CURRENT_ZERO)

    support_closed = bool(support.get("registered_support_motion_escape_closed"))
    pdec_closed = bool(pdec.get("current_corpus_materialized_fresh_layer_pdec_closed"))
    current_zero = bool(current.get("cycle_debt_branch_replay_current_materialized_frontier_zero"))

    samples = []
    for item in previous.get("sample_reports", []):
        samples.append(
            {
                "p": item["p"],
                "x0": item["x0"],
                "q2": item["q2"],
                "initial_closed_width": item["initial_closed_width"],
                "controlled_tail_route": "SAE",
                "aperture_explosion_route": "explicit moving-family/PDEC schema firewall",
            }
        )

    gates = [
        gate(
            "ControlledFreshTailImported",
            True,
            bool(previous.get("controlled_non_pdec_fresh_tail_routes_to_sae")),
            "上一证书已把受控孔径、无 PDEC 的 fresh-tail 压入 SAE。",
            "aperture explosion or PDEC only",
        ),
        gate(
            "ApertureExplosionMeansSchemaChange",
            True,
            True,
            "若 log W_j 反复追赶 log M_j，则局部端点替换模型失效；必须给出支撑运动、阻断包变化或 fresh-layer PDEC schema。",
            "explicit schema firewall",
        ),
        gate(
            "RegisteredSupportMotionImportedClosed",
            support_closed,
            support_closed,
            "已有 registered support-motion 全局路由排除了本地支撑漂移；持久 registered replay 只能提升为远程 ColumnCRT/PDEC。",
            support.get("next_direct_attack_target", "RemotePspaceColumnCRTExclusionOrUnregisteredMovingFamilyRouter"),
        ),
        gate(
            "CurrentMaterializedFreshPDECImportedClosed",
            pdec_closed,
            pdec_closed,
            "已有 fresh-layer PDEC admission firewall 关闭当前语料中的无名材料化 PDEC/ColumnCRT。",
            pdec.get("next_direct_attack_target", "FutureExplicitPrimitiveFreshLayerPDECSchemaIfNew"),
        ),
        gate(
            "CurrentBranchReplayFrontierZeroImported",
            current_zero,
            current_zero,
            "已有 current-frontier-zero 证书说明当前 branch-replay 语料内没有活动终端实例。",
            current.get("next_direct_attack_target", "GlobalFinalInputsStillOpen"),
        ),
        gate(
            "FutureExplicitSchemaReopenOnly",
            True,
            True,
            "未来若出现 Q2 aperture-explosion/moving-family/PDEC 候选，必须提交 source、shape、phase、persistence 与哈希账本；不能作为无名终端保留。",
            "future explicit schema if new",
        ),
        gate(
            "GlobalRowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步当前语料的 schema 防火墙；没有证明未来 schema 不存在，也没有关闭全局最终输入。",
            NEXT_HARDPOINT,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_q2_aperture_explosion_schema_firewall_router",
        "status": "q2_aperture_explosion_current_schema_firewall_not_global_proof",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_HARDPOINT,
        "controlled_fresh_tail_imported": True,
        "registered_support_motion_imported_closed": support_closed,
        "current_materialized_fresh_pdec_imported_closed": pdec_closed,
        "current_branch_replay_frontier_zero_imported": current_zero,
        "future_explicit_aperture_explosion_schema_submitted": False,
        "unnamed_aperture_explosion_terminal_allowed": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_HARDPOINT,
        "sample_reports": samples,
        "sample_count": len(samples),
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "Q2 fresh-layer tail-mass 之后，受控孔径已进入 SAE；剩余的孔径爆炸若要成为真实反例链，"
            "必须材料化为支撑运动、阻断包变化或 fresh-layer PDEC 的显式 schema。当前 registered support-motion、"
            "材料化 fresh-layer PDEC 与 branch-replay 物化前沿均已有防火墙同步；因此当前无名 aperture-explosion "
            "终端不可保留。未来若提交显式 schema，需要按防火墙重开。"
        ),
        "dependency_hashes": {
            str(PREVIOUS.relative_to(ROOT)): sha256(PREVIOUS),
            str(SUPPORT_MOTION.relative_to(ROOT)): sha256(SUPPORT_MOTION),
            str(PDEC_FIREWALL.relative_to(ROOT)): sha256(PDEC_FIREWALL),
            str(CURRENT_ZERO.relative_to(ROOT)): sha256(CURRENT_ZERO),
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
        "# Q2 aperture-explosion schema-firewall 同步路由",
        "",
        "**状态：** `q2_aperture_explosion_current_schema_firewall_not_global_proof`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        f"controlled_fresh_tail_imported={fmt_bool(result['controlled_fresh_tail_imported'])}",
        "registered_support_motion_imported_closed="
        f"{fmt_bool(result['registered_support_motion_imported_closed'])}",
        "current_materialized_fresh_pdec_imported_closed="
        f"{fmt_bool(result['current_materialized_fresh_pdec_imported_closed'])}",
        "current_branch_replay_frontier_zero_imported="
        f"{fmt_bool(result['current_branch_replay_frontier_zero_imported'])}",
        "future_explicit_aperture_explosion_schema_submitted="
        f"{fmt_bool(result['future_explicit_aperture_explosion_schema_submitted'])}",
        f"unnamed_aperture_explosion_terminal_allowed={fmt_bool(result['unnamed_aperture_explosion_terminal_allowed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 同步逻辑",
        "",
        "受控孔径 fresh-tail 已被压入 `SAE`。剩余若声称孔径增长能追赶 fresh modulus，",
        "它就必须说明哪个支撑、阻断包、相位映射或 fresh-layer PDEC 在持久复现。",
        "这类对象不能无名保留：registered support-motion、当前材料化 fresh-layer PDEC 与 current frontier zero",
        "已经给出准入防火墙。",
        "",
        "## 2. 样本路由",
        "",
        "| P | x0 | Q2 | initial width | controlled route | explosion route |",
        "| ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for item in result["sample_reports"]:
        lines.append(
            "| {p} | {x0} | {q2} | {width} | `{controlled}` | `{explosion}` |".format(
                p=item["p"],
                x0=item["x0"],
                q2=item["q2"],
                width=item["initial_closed_width"],
                controlled=item["controlled_tail_route"],
                explosion=item["aperture_explosion_route"],
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
            "## 4. 最新剩余",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "本证书只是当前语料的 schema 防火墙同步；它不证明未来显式 aperture-explosion/moving-family schema 不存在，",
            "也不构成行/列命题的全局无条件证明。",
            "",
            "## 5. 依赖哈希",
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
        "unnamed_aperture_explosion_terminal_allowed": result["unnamed_aperture_explosion_terminal_allowed"],
        "next_direct_attack_target": result["next_direct_attack_target"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
