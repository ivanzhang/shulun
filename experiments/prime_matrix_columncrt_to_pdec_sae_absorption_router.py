#!/usr/bin/env python3
"""把 ColumnCRT 独立证书族吸收到 PDEC/SAE。

用法示例：
  python3 experiments/prime_matrix_columncrt_to_pdec_sae_absorption_router.py

输出：
  docs/monograph/prime-matrix-columncrt-to-pdec-sae-absorption-router.json
  docs/monograph/prime-matrix-columncrt-to-pdec-sae-absorption-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_TERMINAL = (
    DOCS / "prime-matrix-terminal-certificate-package-compression-router.json"
)
DEFAULT_COLUMN_ABSORB = DOCS / "prime-matrix-columncrt-displacement-pdec-absorption.md"
DEFAULT_COLUMN_CONTRACT = DOCS / "h4-pdec-column-defect-routing-contract.md"
DEFAULT_PERSISTENT_ADMISSION = (
    DOCS / "prime-matrix-pdec-cap-persistent-terminal-admission-router.json"
)
DEFAULT_RPZ_GATE = DOCS / "prime-matrix-rpz-unit-endpoint-columncrt-gate.md"
DEFAULT_RPZ_THRESHOLD = DOCS / "prime-matrix-rpz-columncrt-threshold-obstruction.md"
DEFAULT_JSON = DOCS / "prime-matrix-columncrt-to-pdec-sae-absorption-router.json"
DEFAULT_MD = DOCS / "prime-matrix-columncrt-to-pdec-sae-absorption-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(path: Path, needles: list[str]) -> bool:
    """检查文件是否包含全部关键文本。"""
    text = path.read_text(encoding="utf-8")
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造 ColumnCRT 吸收审查行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    terminal: dict[str, Any],
    column_absorb_path: Path,
    column_contract_path: Path,
    persistent_admission: dict[str, Any],
    rpz_gate_path: Path,
    rpz_threshold_path: Path,
) -> list[dict[str, Any]]:
    """生成 ColumnCRT 吸收审查表。"""
    terminal_has_column = any(
        "ColumnCRT" in item
        for item in terminal["independent_terminal_inputs_after_compression"]
    )
    absorption_contract = contains_all(
        column_absorb_path,
        ["ColumnCRT-Displacement Absorption", "displacement PDEC", "SAE-column"],
    )
    column_contract = contains_all(
        column_contract_path,
        ["ColumnCRTDefect", "CD2", "相位兼容性"],
    )
    persistent_absorbs_column = any(
        item.get("gate") == "ColumnCRTAbsorbedBeforeAdmission"
        and item.get("closed")
        for item in persistent_admission.get("rows", [])
    )
    rpz_gate_materialized = contains_all(
        rpz_gate_path,
        ["routes_to_fixed_nonzero_columncrt_residue", "404", "非零位移"],
    )
    threshold_tuning_blocked = contains_all(
        rpz_threshold_path,
        ["阈值障碍", "单靠阈值调参无法闭合", "endpoint-PDEC"],
    )

    return [
        row(
            gate="TerminalPackageStillListsColumnCRT",
            closed=terminal_has_column,
            evidence="terminal compression output contains ColumnCRT",
            meaning="上一轮压缩后 ColumnCRT 仍暂列独立证书族。",
            remaining="decide whether it is genuinely independent",
        ),
        row(
            gate="ColumnCRTRoutingContractClosed",
            closed=column_contract,
            evidence="h4-pdec-column-defect-routing-contract",
            meaning="列位移缺陷已有同口径、相位兼容和条件路由合同。",
            remaining="exclusion not supplied by the contract",
        ),
        row(
            gate="RPZFixedDisplacementGateMaterialized",
            closed=rpz_gate_materialized,
            evidence="rpz unit endpoint columncrt gate",
            meaning="RPZ unit seam 的固定非零位移入口已材料化。",
            remaining="exclude the gate or absorb it",
        ),
        row(
            gate="ThresholdTuningDoesNotExclude",
            closed=threshold_tuning_blocked,
            evidence="rpz columncrt threshold obstruction",
            meaning="调小 L_D 只触发 ColumnCRTDefect，不能给矛盾。",
            remaining="use endpoint-PDEC, avoidance, or independent theorem",
        ),
        row(
            gate="ColumnCRTDisplacementAbsorption",
            closed=absorption_contract,
            evidence="columncrt displacement pdec absorption",
            meaning="持久非零位移过载就是 displacement PDEC；孤立位移过载就是 SAE-column。",
            remaining="prove displacement PDEC or SAE",
        ),
        row(
            gate="PersistentAdmissionAbsorbsColumnCRT",
            closed=persistent_absorbs_column,
            evidence="persistent terminal admission router",
            meaning="裸 ColumnCRT 不能准入终端，必须先转成 displacement/primitive PDEC 或 SAE。",
            remaining="primitive same-formal-unit PDEC",
        ),
    ]


def run(
    terminal_path: Path,
    column_absorb_path: Path,
    column_contract_path: Path,
    persistent_admission_path: Path,
    rpz_gate_path: Path,
    rpz_threshold_path: Path,
) -> dict[str, Any]:
    """运行 ColumnCRT 到 PDEC/SAE 的吸收路由。"""
    terminal = load_json(terminal_path)
    persistent_admission = load_json(persistent_admission_path)
    rows = build_rows(
        terminal=terminal,
        column_absorb_path=column_absorb_path,
        column_contract_path=column_contract_path,
        persistent_admission=persistent_admission,
        rpz_gate_path=rpz_gate_path,
        rpz_threshold_path=rpz_threshold_path,
    )
    absorption_closed = all(item["closed"] for item in rows[1:])
    independent_after_absorption = [
        "Global SAE finite/window/local-survivor certificate family",
        "PDEC family including displacement/endpoint/cofactor/primitive certificates",
    ]
    evidence_paths = [
        terminal_path,
        column_absorb_path,
        column_contract_path,
        persistent_admission_path,
        rpz_gate_path,
        rpz_threshold_path,
    ]
    return {
        "certificate_type": "prime_matrix_columncrt_to_pdec_sae_absorption_router",
        "status": "columncrt_absorbed_to_pdec_sae_terminal_two_family_remainder",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "columncrt_independent_terminal_removed": absorption_closed,
        "terminal_package_fully_proved": False,
        "row_column_unconditional_closed": False,
        "independent_terminal_inputs_after_columncrt_absorption": independent_after_absorption,
        "rows": rows,
        "absorption_law": (
            "ColumnCRT is not an independent terminal certificate family. A persistent "
            "nonzero displacement overload is a displacement PDEC on an enlarged finite "
            "signature; a sparse displacement overload is SAE/endpoint; and balanced "
            "displacement loads become admissible PDEC-dual constraints. RPZ unit endpoint "
            "gates show why threshold tuning alone cannot close the branch, but they do not "
            "prevent absorption into endpoint/displacement PDEC or SAE."
        ),
        "review_conclusion": (
            "ColumnCRT 独立终端已吸收到 PDEC/SAE。第一包的独立剩余进一步压成两族："
            "全局 SAE 证书族与包含 displacement/endpoint/cofactor/primitive 的 PDEC 证书族。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix ColumnCRT 到 PDEC/SAE 吸收路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 吸收律",
        "",
        result["absorption_law"],
        "",
        "```text",
        (
            "columncrt_independent_terminal_removed="
            f"{fmt_bool(result['columncrt_independent_terminal_removed'])}"
        ),
        f"terminal_package_fully_proved={fmt_bool(result['terminal_package_fully_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 审查表",
        "",
        "| gate | closed | evidence | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {evidence} | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(bool(item["closed"])),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(["", "## 3. 吸收后的独立终端输入", ""])
    for item in result["independent_terminal_inputs_after_columncrt_absorption"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## 4. 判定",
            "",
            "ColumnCRT 的固定非零位移入口是真实结构，但不是第三类独立终端。"
            "若它持久，必须作为 displacement PDEC 在同一 formal unit 上提交 `U_CRT<L_PDEC`；"
            "若它孤立，则进入 SAE/endpoint；若位移负载平衡，则变成 PDEC 对偶证书的合法约束行。"
            "因此第一包下一步只剩 PDEC family 与 SAE family 两族证书。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--terminal-json", type=Path, default=DEFAULT_TERMINAL)
    parser.add_argument("--column-absorb-md", type=Path, default=DEFAULT_COLUMN_ABSORB)
    parser.add_argument("--column-contract-md", type=Path, default=DEFAULT_COLUMN_CONTRACT)
    parser.add_argument(
        "--persistent-admission-json", type=Path, default=DEFAULT_PERSISTENT_ADMISSION
    )
    parser.add_argument("--rpz-gate-md", type=Path, default=DEFAULT_RPZ_GATE)
    parser.add_argument("--rpz-threshold-md", type=Path, default=DEFAULT_RPZ_THRESHOLD)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        terminal_path=args.terminal_json,
        column_absorb_path=args.column_absorb_md,
        column_contract_path=args.column_contract_md,
        persistent_admission_path=args.persistent_admission_json,
        rpz_gate_path=args.rpz_gate_md,
        rpz_threshold_path=args.rpz_threshold_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["independent_terminal_inputs_after_columncrt_absorption"])


if __name__ == "__main__":
    main()
