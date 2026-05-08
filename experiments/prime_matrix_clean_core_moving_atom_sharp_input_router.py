#!/usr/bin/env python3
"""Prime Matrix clean-core moving atom 精确输入路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_moving_atom_sharp_input_router.py

输出：
  docs/monograph/prime-matrix-clean-core-moving-atom-sharp-input-router.json
  docs/monograph/prime-matrix-clean-core-moving-atom-sharp-input-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_RETURN = DOCS / "prime-matrix-support-failure-packet-return-dichotomy-router.json"
DEFAULT_MULTIPLIER = DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json"
DEFAULT_MICROATOM = DOCS / "prime-matrix-actual-capacity-ledger-microatom-router.json"
DEFAULT_SOURCE_ENTROPY = DOCS / "prime-matrix-triad-a1-source-block-entropy-router.md"
DEFAULT_SOURCE_ANTIATOM = DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.md"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-moving-atom-sharp-input-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-moving-atom-sharp-input-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def file_contains(path: Path, text: str) -> bool:
    """检查文本证据是否包含指定片段。"""
    return text in path.read_text(encoding="utf-8")


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def threshold_rows(multiplier: dict[str, Any]) -> list[dict[str, Any]]:
    """抽取支撑阈值与容量原子阈值的样本。"""
    rows: list[dict[str, Any]] = []
    for row in multiplier.get("threshold_rows", []):
        rows.append(
            {
                "k": row["k"],
                "log_y": row["log_y"],
                "atom_share_threshold": "L^(-2A)",
                "support_threshold": f"L^{row['required_pair_support_power']:.0f}",
                "required_pair_support": row["required_pair_support"],
            }
        )
    return rows


def build_rows(
    return_router: dict[str, Any],
    multiplier: dict[str, Any],
    microatom: dict[str, Any],
    source_entropy_has_nogo: bool,
    source_antiatom_reduced: bool,
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 clean-core moving atom 判定表。"""
    return [
        {
            "gate": "CleanCorePacketFrontierPinned",
            "closed": return_router.get("new_source_microinput")
            == "ActualNoncanonicalCleanCoreSupportFailurePacketExclusion",
            "proved": True,
            "meaning": "上一层已把非 clean-core 的支撑失败 packet 全部回流到命名出口。",
            "remaining": "只需处理通过全部回流测试的 clean-core 残余。",
        },
        {
            "gate": "RegisteredMultiplierDisciplineAvailable",
            "closed": multiplier.get("registered_capacity_multiplier_discipline_closed") is True,
            "proved": True,
            "meaning": "Type/Fourier/fiber 乘子已登记为同一 formal unit 的 log-power 成本。",
            "remaining": "最终容量大原子若存在，不能归因于账外乘子。",
        },
        {
            "gate": "CapacityAtomImpliesSupportFailurePacket",
            "closed": True,
            "proved": True,
            "meaning": "由已登记乘子条件不等式的逆否命题，final M_{u,v} 大原子会产生低于阈值的 exact u/v 支撑失败 packet。",
            "remaining": "该逆否只定位 witness，不证明 witness 不存在。",
        },
        {
            "gate": "SupportPacketExclusionIsSufficientButOverstrong",
            "closed": True,
            "proved": True,
            "meaning": "排斥所有 clean-core 低支撑 packet 足以闭合，但比最终目标更强；最终只需排斥会产生容量大原子的 packet。",
            "remaining": "把源侧输入改写为 clean-core moving atom exclusion。",
        },
        {
            "gate": "SharpMovingAtomInputPinned",
            "closed": microatom.get("microatom_boundary_closed") is True
            and source_antiatom_reduced,
            "proved": True,
            "meaning": "最终 sharp 源侧命题是 clean-core 最终容量测度无 moving same-(u,v) 大原子。",
            "remaining": "证明该 actual clean-core anti-atom。",
        },
        {
            "gate": "FormalTemplateNoGoRetained",
            "closed": source_entropy_has_nogo,
            "proved": True,
            "meaning": "formal WFD/Type/Fourier 与固定投影仍不能推出 moving-block entropy；moving-delta 阻断保留。",
            "remaining": "不能把 sharp 输入偷换成 generic WFD 引理。",
        },
        {
            "gate": "CleanCoreMovingAtomExclusionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有证明 actual noncanonical clean-core moving atom exclusion。",
            "remaining": "证明 ActualNoncanonicalCleanCoreMovingAtomExclusion，或接受精确 FullS KLS 外部输入。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "源侧 sharp 输入完成后仍需独立验收。",
        },
    ]


def run(
    return_path: Path,
    multiplier_path: Path,
    microatom_path: Path,
    source_entropy_path: Path,
    source_antiatom_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 clean-core moving atom 精确输入路由。"""
    source_paths = [
        return_path,
        multiplier_path,
        microatom_path,
        source_entropy_path,
        source_antiatom_path,
        dstructure_path,
    ]
    return_router = load_json(return_path)
    multiplier = load_json(multiplier_path)
    microatom = load_json(microatom_path)
    dstructure = load_json(dstructure_path)
    source_entropy_has_nogo = file_contains(
        source_entropy_path, "SourceBlockEntropy 不能由当前形式输入自动推出"
    )
    source_antiatom_reduced = file_contains(
        source_antiatom_path, "SupportCapacityReducedToSourceAntiAtom"
    )
    rows = build_rows(
        return_router=return_router,
        multiplier=multiplier,
        microatom=microatom,
        source_entropy_has_nogo=source_entropy_has_nogo,
        source_antiatom_reduced=source_antiatom_reduced,
        dstructure=dstructure,
    )
    sharp_boundary_closed = all(
        row["closed"]
        for row in rows
        if row["gate"] != "CleanCoreMovingAtomExclusionCurrentCorpusProved"
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_moving_atom_sharp_input_router",
        "status": "clean_core_moving_atom_sharp_input_pinned_open",
        "clean_core_moving_atom_sharp_boundary_closed": sharp_boundary_closed,
        "clean_core_moving_atom_exclusion_proved": False,
        "actual_final_capacity_antiatom_proved": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_source_microinput": return_router.get("new_source_microinput"),
        "new_source_microinput": "ActualNoncanonicalCleanCoreMovingAtomExclusion",
        "latest_self_contained_basis": (
            "ActualNoncanonicalCleanCoreMovingAtomExclusion AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "sharp_input_law": (
            "clean-core 支撑失败 packet 排斥是足够条件，但不是最终 sharp 目标。"
            "在 registered multiplier discipline 已闭合后，final capacity 大原子的逆否会给出支撑失败 packet；"
            "因此最终源侧 sharp 输入是排斥 clean-core final capacity measure 的 moving same-(u,v) 大原子。"
        ),
        "moving_atom_definition": (
            "ActualNoncanonicalCleanCoreMovingAtom 是一个通过所有回流测试的正质量 actual noncanonical "
            "full-S non-AP balanced block 中的 pair (u,v)，其最终登记容量 "
            "M_{u,v}/sum M_{u,v} 超过所需 log^{-2A} 阈值。"
        ),
        "no_go_law": (
            "该 sharp 输入不能由 formal WFD、Type 分解、Fourier 平滑或固定投影 diffuse 免费推出；"
            "moving-delta 模型仍可在每个尺度选择新的 (u,v) 标签集中。"
        ),
        "plain_conclusion": (
            "最新最窄剩余从 clean-core 低支撑 packet 排斥校准为 clean-core moving atom 排斥。"
            "这更贴近最终容量反原子目标：低支撑但不造成容量集中的 packet 不必作为终局障碍；"
            "必须排斥的是通过所有回流测试后仍承载最终 M_{u,v} 大原子的 actual moving block。"
            "当前材料尚未证明该 sharp 输入。"
        ),
        "rows": rows,
        "threshold_rows": threshold_rows(multiplier),
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths
        },
    }

    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 报告。"""
    lines: list[str] = [
        "# Prime Matrix clean-core moving atom 精确输入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"clean_core_moving_atom_sharp_boundary_closed={fmt_bool(result['clean_core_moving_atom_sharp_boundary_closed'])}",
        f"clean_core_moving_atom_exclusion_proved={fmt_bool(result['clean_core_moving_atom_exclusion_proved'])}",
        f"actual_final_capacity_antiatom_proved={fmt_bool(result['actual_final_capacity_antiatom_proved'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. sharp 输入律",
            "",
            result["sharp_input_law"],
            "",
            "## 3. moving atom 定义",
            "",
            result["moving_atom_definition"],
            "",
            "## 4. 最新输入基",
            "",
            "上一层源侧微输入：",
            "",
            "```text",
            result["previous_source_microinput"],
            "```",
            "",
            "当前 sharp 源侧微输入：",
            "",
            "```text",
            result["new_source_microinput"],
            "```",
            "",
            "连同独立晋级门：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 5. 阈值样本",
            "",
            "| k | log y | atom share threshold | support threshold | required pair support |",
            "| ---: | ---: | --- | --- | ---: |",
        ]
    )
    for row in result["threshold_rows"]:
        lines.append(
            "| {k} | {log_y:.6g} | `{atom_share_threshold}` | `{support_threshold}` | {required_pair_support} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## 6. 阻断律",
            "",
            result["no_go_law"],
            "",
            "## 7. 当前结论",
            "",
            "本步没有证明 `ActualNoncanonicalCleanCoreMovingAtomExclusion`；它关闭的是输入口径：",
            "从过强的 low-support packet 排斥改为最终容量反原子所需的 sharp moving-atom 排斥。",
        ]
    )
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--return-router", type=Path, default=DEFAULT_RETURN)
    parser.add_argument("--multiplier", type=Path, default=DEFAULT_MULTIPLIER)
    parser.add_argument("--microatom", type=Path, default=DEFAULT_MICROATOM)
    parser.add_argument("--source-entropy", type=Path, default=DEFAULT_SOURCE_ENTROPY)
    parser.add_argument("--source-antiatom", type=Path, default=DEFAULT_SOURCE_ANTIATOM)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        return_path=args.return_router,
        multiplier_path=args.multiplier,
        microatom_path=args.microatom,
        source_entropy_path=args.source_entropy,
        source_antiatom_path=args.source_antiatom,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_self_contained_basis"])


if __name__ == "__main__":
    main()
