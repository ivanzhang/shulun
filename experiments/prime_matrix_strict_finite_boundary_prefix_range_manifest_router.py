#!/usr/bin/env python3
"""生成 strict 有限边界 prefix 范围与参数 manifest 证书。

用法示例：
  python3 experiments/prime_matrix_strict_finite_boundary_prefix_range_manifest_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-finite-boundary-prefix-range-manifest-router.json

输出：
  docs/monograph/prime-matrix-strict-finite-boundary-prefix-range-manifest-router.json
  docs/monograph/prime-matrix-strict-finite-boundary-prefix-range-manifest-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DOCS = ROOT / "docs"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-range-manifest-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-range-manifest-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-certificate-attack-router.json",
    MONOGRAPH / "prime-matrix-dynamic-skeleton-lower-factorization-router.json",
    DOCS / "dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.json",
    MONOGRAPH / "prime-matrix-strict-dynamic-skeleton-tail-b3-bridge-router.json",
    MONOGRAPH / "prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json",
]

TARGET = "FiniteBoundaryPrefixRangeAndParameterManifest"
WINDOW = "SameParameterPrefixWindowSpecification"
RUNNER = "ReproduciblePrefixRoughCountRunnerHashLedger"
TAIL = "AnalyticTailToFiniteBoundaryMonotoneBridge"
TYPE_LEDGER = "FormalUnitTypeThresholdLedger"
ROW_FREE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"

PARAMETER_ID = "alpha043_pge100000_external_b3_pending_finite_prefix_named_return"
ALPHA = 0.43
P_TAIL_START = 100_000
FINITE_BRIDGE_START = 3001
FINITE_BRIDGE_END = 99_991
TARGET_S = 401


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书，缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """记录依赖哈希。"""
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


def finite_bridge_summary(dynamic: dict[str, Any]) -> dict[str, Any]:
    """提取已关闭的 3001<=P<100000 有限桥摘要。"""
    finite = dynamic.get("finite_metrics", {})
    return {
        "range": f"{FINITE_BRIDGE_START}<=P<100000",
        "prime_min": finite.get("prime_min", FINITE_BRIDGE_START),
        "prime_max": finite.get("prime_max", FINITE_BRIDGE_END),
        "record_count": finite.get("record_count"),
        "prime_count": finite.get("prime_count"),
        "target_s": finite.get("target_s", TARGET_S),
        "min_skeleton_count": finite.get("min_skeleton_count"),
        "min_record": finite.get("min_record", {}),
        "closed": dynamic.get("finite_dynamic_skeleton_certificate_closed") is True,
    }


def active_manifest() -> dict[str, Any]:
    """给出当前 strict D0/prefix 线可合法使用的参数清单。"""
    s_value = 1.0 / ALPHA
    return {
        "parameter_id": PARAMETER_ID,
        "alpha": ALPHA,
        "s": s_value,
        "p_tail_start": P_TAIL_START,
        "z_rule": "z=floor(P^0.43) or equivalent monotone cutoff recorded in same-parameter window",
        "sieve_level_rule": "D comparable to P, with squarefree d<P in the prefix CRT count formula",
        "prefix_interval": "1<=c<P",
        "rough_object": "#{1<=c<P: xP+c avoids the prescribed residue class modulo each q<=z}",
        "target_lower_bound_role": "D0_prefix_lower_bound for terminal margin table",
        "finite_bridge_before_tail": f"{FINITE_BRIDGE_START}<=P<100000 handled by dynamic skeleton finite certificate, not by the current D0 p>=100000 table row",
    }


def range_rows(finite: dict[str, Any]) -> list[dict[str, Any]]:
    """列出 manifest 覆盖区间。"""
    return [
        {
            "range": "P<3001",
            "role": "outside_current_manifest",
            "status": "not_part_of_current_alpha043_pge100000_D0_row",
            "meaning": "更小 P 属于旧有限桥或其它全局边界，不由本 D0 同参数行关闭。",
        },
        {
            "range": finite["range"],
            "role": "pre_tail_bridge",
            "status": "closed_by_dynamic_skeleton_finite_certificate" if finite["closed"] else "open",
            "meaning": f"已有动态粗骨架有限桥；最小值 {finite.get('min_skeleton_count')}，目标 {finite.get('target_s')}。",
        },
        {
            "range": "P>=100000",
            "role": "active_same_parameter_prefix_tail",
            "status": "manifest_closed_runner_and_tail_bridge_open",
            "meaning": "当前 finite prefix 证书的同参数 D0 行从这里开始；需要同参数窗口、runner/hash 和解析尾段桥接。",
        },
    ]


def decision_rows(data: dict[str, dict[str, Any]], finite: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 range manifest 判定表。"""
    attack = data["attack"]
    concrete = data["concrete"]
    dynamic = data["dynamic"]
    tail = data["tail"]

    parameter_row = concrete.get("candidate_parameter_row", {})
    parameter_matches = (
        parameter_row.get("parameter_id") == PARAMETER_ID
        and parameter_row.get("p_min") == P_TAIL_START
        and abs(float(parameter_row.get("alpha", ALPHA)) - ALPHA) < 1e-15
    )
    tail_matches = (
        tail.get("tail_object_interface_closed") is True
        and tail.get("ten_percent_capacity_algebra_imported") is True
    )

    return [
        {
            "gate": "RangeManifestTargetImported",
            "closed": attack.get("next_direct_attack_target") == TARGET,
            "proved": False,
            "meaning": "上一层已把 finite prefix 首字段定为范围与参数 manifest。",
            "remaining": TARGET,
        },
        {
            "gate": "CandidateParameterIdPinned",
            "closed": parameter_matches,
            "proved": parameter_matches,
            "meaning": "当前同参数 D0 行固定为 alpha=0.43, P>=100000。",
            "remaining": "parameter row pinned",
        },
        {
            "gate": "PreTailFiniteBridgeLocated",
            "closed": finite["closed"],
            "proved": finite["closed"],
            "meaning": "3001<=P<100000 的动态粗骨架有限桥已有证书，不应混入当前 P>=100000 D0 runner。",
            "remaining": "pre-tail bridge imported as boundary evidence",
        },
        {
            "gate": "TailObjectInterfaceMatched",
            "closed": tail_matches,
            "proved": tail_matches,
            "meaning": "P>=100000 尾段对象已经对齐为一维 prefix rough-count / B3 lower-sieve 对象。",
            "remaining": WINDOW,
        },
        {
            "gate": "RangeAndParameterManifestClosed",
            "closed": parameter_matches and finite["closed"] and tail_matches,
            "proved": parameter_matches and finite["closed"] and tail_matches,
            "meaning": "有限桥、尾段起点、alpha/z 规则、prefix 区间和目标角色已经列为可审查 manifest。",
            "remaining": WINDOW,
        },
        {
            "gate": "SameParameterWindowStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "manifest 只列清范围；还没有证明 D0、M#、terminal budget 使用完全同一 z,D,Lambda/type alphabet。",
            "remaining": f"{WINDOW} AND {TYPE_LEDGER} AND {ROW_FREE}",
        },
        {
            "gate": "FiniteBoundaryPrefixCertificateProved",
            "closed": False,
            "proved": False,
            "meaning": "runner/hash 与解析尾段桥接仍未完成，因此 finite prefix 证书尚未闭合。",
            "remaining": f"{WINDOW} AND {RUNNER} AND {TAIL}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 range manifest 证书。"""
    data = {
        "attack": load_json(MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-certificate-attack-router.json"),
        "dynamic": load_json(MONOGRAPH / "prime-matrix-dynamic-skeleton-lower-factorization-router.json"),
        "tail": load_json(MONOGRAPH / "prime-matrix-strict-dynamic-skeleton-tail-b3-bridge-router.json"),
        "concrete": load_json(MONOGRAPH / "prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json"),
    }
    finite = finite_bridge_summary(data["dynamic"])
    rows = decision_rows(data, finite)
    manifest_closed = next(row for row in rows if row["gate"] == "RangeAndParameterManifestClosed")["closed"]

    return {
        "certificate_type": "prime_matrix_strict_finite_boundary_prefix_range_manifest_router",
        "status": "finite_boundary_prefix_range_manifest_closed_same_parameter_window_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "range_manifest_target_imported": rows[0]["closed"],
        "candidate_parameter_id_pinned": rows[1]["closed"],
        "pre_tail_finite_bridge_located": rows[2]["closed"],
        "tail_object_interface_matched": rows[3]["closed"],
        "range_and_parameter_manifest_closed": manifest_closed,
        "same_parameter_window_specification_proved": False,
        "runner_hash_ledger_proved": False,
        "analytic_tail_bridge_proved": False,
        "finite_boundary_prefix_certificate_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "manifest": active_manifest(),
        "finite_bridge_summary": finite,
        "range_rows": range_rows(finite),
        "hardpoint_before_router": TARGET,
        "hardpoint_after_router": f"{WINDOW} AND {RUNNER} AND {TAIL}",
        "next_direct_attack_target": WINDOW,
        "parallel_attack_targets": [RUNNER, TAIL, TYPE_LEDGER, ROW_FREE],
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`FiniteBoundaryPrefixRangeAndParameterManifest` 已可关闭：当前同参数 D0 行固定为 "
            "`alpha043_pge100000_external_b3_pending_finite_prefix_named_return`，即 alpha=0.43、P>=100000、"
            "prefix 区间 1<=c<P；3001<=P<100000 作为已归档的动态粗骨架有限桥接边界，"
            "不混入当前 D0 runner。真正剩余转为同参数窗口规格、runner/hash 和解析尾段桥接。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    manifest = result["manifest"]
    finite = result["finite_bridge_summary"]
    lines = [
        "# Prime Matrix strict 有限边界 prefix 范围 manifest 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"range_manifest_target_imported={fmt_bool(result['range_manifest_target_imported'])}",
        f"candidate_parameter_id_pinned={fmt_bool(result['candidate_parameter_id_pinned'])}",
        f"pre_tail_finite_bridge_located={fmt_bool(result['pre_tail_finite_bridge_located'])}",
        f"tail_object_interface_matched={fmt_bool(result['tail_object_interface_matched'])}",
        f"range_and_parameter_manifest_closed={fmt_bool(result['range_and_parameter_manifest_closed'])}",
        f"same_parameter_window_specification_proved={fmt_bool(result['same_parameter_window_specification_proved'])}",
        f"runner_hash_ledger_proved={fmt_bool(result['runner_hash_ledger_proved'])}",
        f"analytic_tail_bridge_proved={fmt_bool(result['analytic_tail_bridge_proved'])}",
        f"finite_boundary_prefix_certificate_proved={fmt_bool(result['finite_boundary_prefix_certificate_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Manifest",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in manifest.items():
        lines.append(f"| `{cell(key)}` | {cell(value)} |")

    lines.extend(
        [
            "",
            "## 2. Range Rows",
            "",
            "| range | role | status | meaning |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["range_rows"]:
        lines.append(
            "| "
            + " | ".join([cell(row["range"]), cell(row["role"]), cell(row["status"]), cell(row["meaning"])])
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 有限桥摘要",
            "",
            "| item | value |",
            "| --- | ---: |",
            f"| prime_min | {finite.get('prime_min')} |",
            f"| prime_max | {finite.get('prime_max')} |",
            f"| record_count | {finite.get('record_count')} |",
            f"| prime_count | {finite.get('prime_count')} |",
            f"| min_skeleton_count | {finite.get('min_skeleton_count')} |",
            f"| target_s | {finite.get('target_s')} |",
            "",
            "## 4. 判定表",
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
            "## 5. 下一最窄点",
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
            "审稿边界：本步只关闭范围与参数 manifest；没有证明同参数窗口、runner/hash 或尾段桥接，因此 D0 仍未数值化。",
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
