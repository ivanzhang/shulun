#!/usr/bin/env python3
"""生成 strict 有限边界 prefix 证书攻坚路由器。

用法示例：
  python3 experiments/prime_matrix_strict_finite_boundary_prefix_certificate_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-finite-boundary-prefix-certificate-attack-router.json

输出：
  docs/monograph/prime-matrix-strict-finite-boundary-prefix-certificate-attack-router.json
  docs/monograph/prime-matrix-strict-finite-boundary-prefix-certificate-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-certificate-attack-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-certificate-attack-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-forced-load-latest-frontier-sync-router.json",
    MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json",
    MONOGRAPH / "prime-matrix-strict-normalized-prefix-potential-router.json",
    MONOGRAPH / "prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json",
    MONOGRAPH / "prime-matrix-strict-finite-prefix-named-return-coupled-margin-ledger-router.json",
]

TARGET = "FiniteBoundaryPrefixRoughCountCertificate"
RANGE = "FiniteBoundaryPrefixRangeAndParameterManifest"
WINDOW = "SameParameterPrefixWindowSpecification"
RUNNER = "ReproduciblePrefixRoughCountRunnerHashLedger"
TAIL = "AnalyticTailToFiniteBoundaryMonotoneBridge"
TYPE_LEDGER = "FormalUnitTypeThresholdLedger"
ROW_FREE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书，缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """记录依赖哈希，便于审稿复核。"""
    result = {"script": sha256(Path(__file__).resolve())}
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def components() -> list[dict[str, Any]]:
    """列出 finite prefix 证书必须包含的字段。"""
    return [
        {
            "component": RANGE,
            "closed": False,
            "proved": False,
            "meaning": "明确有限边界覆盖的 P 区间、素数枚举边界、alpha/z/D/Lambda 与同参数 id。",
            "remaining": RANGE,
        },
        {
            "component": WINDOW,
            "closed": False,
            "proved": False,
            "meaning": "把 D0 prefix lower bound、M# 势和 terminal budget 使用的 z,D,Lambda 锁成同一窗口。",
            "remaining": WINDOW,
        },
        {
            "component": RUNNER,
            "closed": False,
            "proved": False,
            "meaning": "提供可复现 runner、输入清单、输出摘要和 hash，证明有限区间内每个 P 的 prefix 粗筛余下界。",
            "remaining": RUNNER,
        },
        {
            "component": TAIL,
            "closed": False,
            "proved": False,
            "meaning": "证明有限 runner 终点之后由解析 B3/rough-count 下界接管，且没有参数换轨。",
            "remaining": TAIL,
        },
    ]


def decision_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 finite boundary prefix 攻坚判定表。"""
    frontier = data["frontier"]
    uniform = data["uniform"]
    concrete = data["concrete"]
    coupled = data["coupled"]

    return [
        {
            "gate": "FiniteBoundaryPrefixTargetImported",
            "closed": frontier.get("next_direct_attack_target") == TARGET,
            "proved": False,
            "meaning": "最新强制负载前沿已把下一主攻点同步为有限边界 prefix 证书。",
            "remaining": TARGET,
        },
        {
            "gate": "RoughCountFormulaAvailable",
            "closed": uniform.get("main_error_split_closed") is True,
            "proved": True,
            "meaning": "prefix 粗筛余公式已化为 lower weights 主项减边界项；有限证书只负责剩余边界区间。",
            "remaining": TARGET,
        },
        {
            "gate": "CandidateParameterRowAvailable",
            "closed": concrete.get("candidate_parameter_row_generated") is True,
            "proved": False,
            "meaning": "候选同参数行已可命名，但 D0/E0/U0 与 finite hash 未填入。",
            "remaining": "fill D0/E0/U0/hash",
        },
        {
            "gate": "FiniteBoundaryHashPresent",
            "closed": concrete.get("finite_boundary_hash_available") is True or coupled.get("finite_boundary_hash_present") is True,
            "proved": False,
            "meaning": "当前没有可复核 finite boundary hash；因此不能把渐近余量升级为全局 D0。",
            "remaining": RUNNER,
        },
        {
            "gate": "BoundaryRangeManifestPresent",
            "closed": False,
            "proved": False,
            "meaning": "当前语料没有明确 finite runner 应覆盖的闭区间、阈值来源和参数锁定清单。",
            "remaining": RANGE,
        },
        {
            "gate": "SameParameterWindowLocked",
            "closed": False,
            "proved": False,
            "meaning": "finite prefix 不能单独跑；必须与终端预算中的 z,D,Lambda、row-free type alphabet 同步。",
            "remaining": f"{WINDOW} AND {TYPE_LEDGER} AND {ROW_FREE}",
        },
        {
            "gate": "AnalyticTailBridgePresent",
            "closed": False,
            "proved": False,
            "meaning": "即使有限 runner 给出 hash，还需证明 runner 终点以后由解析尾段无缝接管。",
            "remaining": TAIL,
        },
        {
            "gate": "FiniteBoundaryPrefixCertificateProved",
            "closed": False,
            "proved": False,
            "meaning": "有限边界 prefix 证书已被拆成四个字段，但当前四项均未同时完成。",
            "remaining": f"{RANGE} AND {WINDOW} AND {RUNNER} AND {TAIL}",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只是把 finite prefix 原子拆细；命名回流、moving atom 和 DStructure 仍未闭合。",
            "remaining": f"{TARGET} AND {NAMED_RETURN} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 finite boundary prefix 证书攻坚结果。"""
    data = {
        "frontier": load_json(MONOGRAPH / "prime-matrix-strict-forced-load-latest-frontier-sync-router.json"),
        "uniform": load_json(MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json"),
        "concrete": load_json(MONOGRAPH / "prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json"),
        "coupled": load_json(MONOGRAPH / "prime-matrix-strict-finite-prefix-named-return-coupled-margin-ledger-router.json"),
    }
    rows = decision_rows(data)
    return {
        "certificate_type": "prime_matrix_strict_finite_boundary_prefix_certificate_attack_router",
        "status": "finite_boundary_prefix_split_to_range_window_runner_tail_bridge_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "finite_boundary_prefix_target_imported": rows[0]["closed"],
        "rough_count_formula_available": rows[1]["closed"],
        "candidate_parameter_row_available": rows[2]["closed"],
        "finite_boundary_hash_present": False,
        "boundary_range_manifest_present": False,
        "same_parameter_window_locked": False,
        "analytic_tail_bridge_present": False,
        "finite_boundary_prefix_certificate_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": TARGET,
        "hardpoint_after_router": f"{RANGE} AND {WINDOW} AND {RUNNER} AND {TAIL}",
        "next_direct_attack_target": RANGE,
        "parallel_attack_targets": [WINDOW, RUNNER, TAIL, TYPE_LEDGER, ROW_FREE, NAMED_RETURN, DSTRUCTURE],
        "components": components(),
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`FiniteBoundaryPrefixRoughCountCertificate` 不能再被当作一个无结构的缺 hash 标签。"
            "它必须拆成四个可审查字段：有限区间与参数 manifest、同参数 prefix 窗口、"
            "可复现 runner/hash 清单、以及解析尾段到有限边界的单调桥接。"
            "当前材料尚未给出这些字段，因此本步没有闭合 D0；下一最窄点是 "
            "`FiniteBoundaryPrefixRangeAndParameterManifest`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 有限边界 prefix 证书攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"finite_boundary_prefix_target_imported={fmt_bool(result['finite_boundary_prefix_target_imported'])}",
        f"rough_count_formula_available={fmt_bool(result['rough_count_formula_available'])}",
        f"candidate_parameter_row_available={fmt_bool(result['candidate_parameter_row_available'])}",
        f"finite_boundary_hash_present={fmt_bool(result['finite_boundary_hash_present'])}",
        f"boundary_range_manifest_present={fmt_bool(result['boundary_range_manifest_present'])}",
        f"same_parameter_window_locked={fmt_bool(result['same_parameter_window_locked'])}",
        f"analytic_tail_bridge_present={fmt_bool(result['analytic_tail_bridge_present'])}",
        f"finite_boundary_prefix_certificate_proved={fmt_bool(result['finite_boundary_prefix_certificate_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 原子拆分",
        "",
        "```text",
        result["hardpoint_before_router"],
        "  =>",
        result["hardpoint_after_router"],
        "```",
        "",
        "| component | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["components"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{cell(row['component'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    cell(row["meaning"]),
                    cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    cell(row["meaning"]),
                    cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本步没有运行有限验证，也没有把 runner 缺口写成证明；"
            "它只把 finite prefix 证书拆成下一轮可生成和可审查的最小字段。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    MONOGRAPH.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
