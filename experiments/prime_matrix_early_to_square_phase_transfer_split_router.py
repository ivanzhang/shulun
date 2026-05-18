#!/usr/bin/env python3
"""生成早期零行到平方锚相位转移的首破裂分裂证书。

用法示例：
  python3 experiments/prime_matrix_early_to_square_phase_transfer_split_router.py
  python3 -m json.tool docs/monograph/prime-matrix-early-to-square-phase-transfer-split-router.json

输出：
  data/prime-matrix-early-to-square-phase-transfer-split-ledger.json
  docs/monograph/prime-matrix-early-to-square-phase-transfer-split-router.json
  docs/monograph/prime-matrix-early-to-square-phase-transfer-split-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-early-to-square-phase-transfer-split-ledger.json"
OUT_JSON = DOCS / "prime-matrix-early-to-square-phase-transfer-split-router.json"
OUT_MD = DOCS / "prime-matrix-early-to-square-phase-transfer-split-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.json",
    DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json",
    DOCS / "prime-matrix-inverse-alignment-latest-frontier-sync-router.json",
    DOCS / "prime-matrix-terminal-row-square-phase-bridge-router.json",
    DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json",
    DOCS / "prime-matrix-zero-row-minrep-route-review.md",
    ROOT / "docs" / "front-window-branch-potential.md",
    ROOT / "docs" / "phase-delay-minimal-solution-route.md",
]

TRANSFER = "AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn"
SQUARE_ZERO = "ZeroAtXEqualsP"
PPLUS1_NONZERO = "NoZeroRowAtXEqualsP_PlusOneRowAfterSquare"
FIRST_BREAK = "FirstBreakPhaseSlipNamedReturnExclusion"
PHASE_SLIP = "RegisteredFirstBreakUnitPhaseSlipPDECSAELocalSurvivorReturn"
EARLY_TERMINAL = "EarlyZeroTerminalExclusionPackage"
SIGNED_ROW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
SOURCE_TABLE = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXTERNAL_KZ = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证据哈希。"""
    paths = [Path(__file__).resolve()] + SOURCE_FILES
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
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


def build_rows(phase_schema_imported: bool) -> list[dict[str, Any]]:
    """构造首破裂分裂判定表。"""
    return [
        row(
            "TransferTargetImported",
            True,
            False,
            "上一证书确认第 P+1 行非零不能直接推出全早期非零；缺失项就是早期零行到平方锚的非循环转移。",
            TRANSFER,
        ),
        row(
            "ContiguousZeroBlockDichotomyClosed",
            True,
            True,
            "若某个 x0<P 是零行，则从 x0 向 P 前进：要么每一行都保持零行直到 x=P，要么存在首个破裂行 y<=P。",
            f"{SQUARE_ZERO} OR {PHASE_SLIP}",
        ),
        row(
            "PersistToSquareImpliesSquareZero",
            True,
            True,
            "若零行块一直延续到 x=P，则平方锚第 P+1 行就是零行；这正是已分离的 square-anchor 分支。",
            SQUARE_ZERO,
        ),
        row(
            "FirstBreakReleaseSetNonempty",
            True,
            True,
            "若 x=P 非零且前面存在零行，则首个破裂行 y 有非空释放列集；上一行 y-1 仍为零行。",
            PHASE_SLIP,
        ),
        row(
            "ReleasedColumnsArePrimeSurvivorsBeforeOrAtSquare",
            True,
            True,
            "释放列 c 在行 y 不再被任何 q<P 覆盖；若 y<P，则 yP+c<P^2 且为素数，若 y=P，则为平方锚幸存素数。",
            "prime survivor / square-anchor survivor",
        ),
        row(
            "UnitPhaseSlipFormulaClosed",
            True,
            True,
            "从 y-1 到 y，每个小模 q 的覆盖相位按 rho_q(y)=rho_q(y-1)-P mod q 单位滑移；释放列正是该滑移造成的边界非覆盖。",
            "none for formula",
        ),
        row(
            "PhaseSlipSchemaAdmissionImported",
            phase_schema_imported,
            phase_schema_imported,
            "早期零行的同 formal-unit 相位缺陷准入旧证书已把稳定短复现/无自同构边界缺陷登记到 PDEC/SAE/ColumnCRT。",
            EARLY_TERMINAL,
        ),
        row(
            "AbstractTransferReduced",
            True,
            False,
            "抽象 transfer 不再保留：它被分裂为 square-zero 分支或首破裂 phase-slip 命名回流。",
            f"{PPLUS1_NONZERO} AND {FIRST_BREAK}",
        ),
        row(
            "TransferProvedAsContradiction",
            False,
            False,
            "本步只完成分裂和命名回流；尚未排斥首破裂 phase-slip 的 PDEC/SAE/LocalSurvivor 终端。",
            FIRST_BREAK,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥 first-break 命名终端，或继续完成 signed-row/source-rank 主前沿。",
            f"({FIRST_BREAK} OR {SIGNED_ROW} OR {SOURCE_TABLE} OR {FIXED_KEY} OR {NEW_JOINT} OR {EXTERNAL_KZ}) AND {MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造首破裂分裂证书。"""
    pplus1 = load_json(DOCS / "prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.json")
    phase_schema = load_json(DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json")
    exactuv = load_json(DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json")
    phase_schema_imported = phase_schema.get("early_zero_phase_defect_schema_admission_closed") is True
    rows = build_rows(phase_schema_imported)
    reduced_basis = (
        f"({PPLUS1_NONZERO} AND {FIRST_BREAK}) "
        f"OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) "
        f"OR {NEW_JOINT} OR {EXTERNAL_KZ}"
    )
    latest_basis = f"({reduced_basis}) AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    plain = (
        "早期零行到平方锚的抽象转移已被压成首破裂分裂："
        "若零行块从某个 x0<P 一直延续到 x=P，则得到 square-zero；"
        "否则存在首个破裂行 y，释放列形成单位相位滑移缺陷，并按旧 early-zero phase-defect schema "
        "进入 PDEC/SAE/ColumnCRT/LocalSurvivor 命名回流。"
        "因此当前剩余不再是抽象 transfer，而是排斥 first-break phase-slip 命名终端。"
    )
    return {
        "certificate_type": "prime_matrix_early_to_square_phase_transfer_split_router",
        "status": "early_to_square_transfer_split_to_first_break_phase_slip_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "transfer_target_imported": pplus1.get("needed_transfer_theorem") == TRANSFER,
        "contiguous_zero_block_dichotomy_closed": True,
        "persist_to_square_implies_square_zero": True,
        "first_break_release_set_nonempty": True,
        "released_columns_are_prime_survivors_before_or_at_square": True,
        "unit_phase_slip_formula_closed": True,
        "phase_slip_schema_admission_imported": phase_schema_imported,
        "abstract_transfer_reduced_to_square_zero_or_first_break_return": True,
        "transfer_proved_as_contradiction": False,
        "row_column_unconditional_closed": False,
        "previous_global_direct_attack_preserved": exactuv.get("next_direct_attack_target", SIGNED_ROW),
        "next_direct_attack_target": FIRST_BREAK,
        "parallel_direct_attack_targets": [SIGNED_ROW, SOURCE_TABLE, FIXED_KEY, NEW_JOINT, EXTERNAL_KZ],
        "reduced_transfer_basis": reduced_basis,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix early-to-square 相位转移首破裂分裂证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"contiguous_zero_block_dichotomy_closed={fmt_bool(cert['contiguous_zero_block_dichotomy_closed'])}",
        f"persist_to_square_implies_square_zero={fmt_bool(cert['persist_to_square_implies_square_zero'])}",
        f"first_break_release_set_nonempty={fmt_bool(cert['first_break_release_set_nonempty'])}",
        f"unit_phase_slip_formula_closed={fmt_bool(cert['unit_phase_slip_formula_closed'])}",
        f"phase_slip_schema_admission_imported={fmt_bool(cert['phase_slip_schema_admission_imported'])}",
        f"transfer_proved_as_contradiction={fmt_bool(cert['transfer_proved_as_contradiction'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 分裂定理",
        "",
        "假设存在早期零行 `x0<P`。从 `x0` 逐行推进到 `P`：",
        "",
        "```text",
        "若所有 x0<=t<=P 都是零行 => x=P 是平方锚零行。",
        "否则令 y 为首个非零行；则 y-1 是零行，y 有非空释放列集。",
        "```",
        "",
        "对释放列 `c`，上一行由某个 `q<P` 覆盖，而当前行不再被任何 `q<P` 覆盖。",
        "相位公式为：",
        "",
        "```text",
        "rho_q(t) = -tP mod q,   rho_q(t+1)=rho_q(t)-P mod q.",
        "```",
        "",
        "因此首破裂不是新的自由出口，而是单位相位滑移造成的边界非覆盖缺陷。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 新活动基",
            "",
            "抽象 transfer 分支压成：",
            "",
            "```text",
            cert["reduced_transfer_basis"],
            "```",
            "",
            "合并 exact-UV/source-rank 前沿后的活动基：",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 4. 下一直接主攻",
            "",
            "本分支下一主攻：",
            "",
            "```text",
            cert["next_direct_attack_target"],
            "```",
            "",
            "全局上一主攻仍保留：",
            "",
            "```text",
            cert["previous_global_direct_attack_preserved"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " OR ".join(cert["parallel_direct_attack_targets"]),
            "```",
            "",
            "## 5. 诚实边界",
            "",
            "- 本证书不证明早期零行不存在。",
            "- 本证书只把早期到平方锚的抽象转移压成 square-zero 或 first-break phase-slip 命名回流。",
            "- 仍需排斥 `FirstBreakPhaseSlipNamedReturnExclusion`，或完成 signed-row/source-rank 主前沿。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
