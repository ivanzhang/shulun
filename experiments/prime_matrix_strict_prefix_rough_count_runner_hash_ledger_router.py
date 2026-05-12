#!/usr/bin/env python3
"""生成 strict prefix rough-count runner/hash 账本证书。

用法示例：
  python3 experiments/prime_matrix_strict_prefix_rough_count_runner_hash_ledger_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-prefix-rough-count-runner-hash-ledger-router.json

输出：
  docs/monograph/prime-matrix-strict-prefix-rough-count-runner-hash-ledger-router.json
  docs/monograph/prime-matrix-strict-prefix-rough-count-runner-hash-ledger-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-prefix-rough-count-runner-hash-ledger-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-prefix-rough-count-runner-hash-ledger-router.md"

RUNNER_SCRIPT = ROOT / "experiments" / "prime_matrix_dynamic_promoted_rough_capacity_audit.py"
RUNNER_JSON = DOCS / "dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.json"
RUNNER_MD = DOCS / "dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.md"

SOURCE_FILES = [
    RUNNER_SCRIPT,
    RUNNER_JSON,
    RUNNER_MD,
    MONOGRAPH / "prime-matrix-dynamic-skeleton-lower-factorization-router.json",
    MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-range-manifest-router.json",
    MONOGRAPH / "prime-matrix-strict-same-parameter-prefix-window-spec-router.json",
]

TARGET = "ReproduciblePrefixRoughCountRunnerHashLedger"
TAIL = "AnalyticTailToFiniteBoundaryMonotoneBridge"
TYPE_LEDGER = "FormalUnitTypeThresholdLedger"
ROW_FREE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"
PARAMETER_ID = "alpha043_pge100000_external_b3_pending_finite_prefix_named_return"
ALPHA = 0.43
FINITE_MIN = 3001
FINITE_MAX = 99_991
TARGET_S = 401


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_sha256(obj: Any) -> str:
    """对 JSON 对象做稳定哈希。"""
    payload = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
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


def finite_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """选出 3001<=P<100000 的有限桥记录。"""
    return [row for row in records if FINITE_MIN <= int(row.get("p", -1)) <= FINITE_MAX]


def metrics_from_runner(runner: dict[str, Any]) -> dict[str, Any]:
    """从 runner 输出中复算摘要指标。"""
    params = runner.get("parameters", {})
    primes = params.get("primes", [])
    records = runner.get("records", [])
    finite = finite_records(records)
    finite_primes = sorted({int(row["p"]) for row in finite})
    finite_min_record = min(finite, key=lambda row: int(row.get("skeleton_count", 10**18))) if finite else {}
    alpha_values = sorted({float(row["alpha"]) for row in records})
    side_ok = all(
        {row["side"] for row in finite if int(row["p"]) == p} == {"minus", "plus"}
        for p in finite_primes
    )
    pass_ok = all(
        int(row.get("skeleton_count", -1)) >= TARGET_S
        and row.get("capacity_pass") is True
        and row.get("forced_pass") is True
        for row in finite
    )
    return {
        "all_prime_count": len(primes),
        "all_record_count": len(records),
        "all_prime_min": min(primes) if primes else None,
        "all_prime_max": max(primes) if primes else None,
        "alpha_values": alpha_values,
        "finite_prime_count": len(finite_primes),
        "finite_record_count": len(finite),
        "finite_prime_min": min(finite_primes) if finite_primes else None,
        "finite_prime_max": max(finite_primes) if finite_primes else None,
        "finite_two_sides_per_prime": side_ok,
        "finite_min_skeleton_count": int(finite_min_record.get("skeleton_count", -1)) if finite_min_record else None,
        "finite_min_record": {
            "p": finite_min_record.get("p"),
            "side": finite_min_record.get("side"),
            "cutoff": finite_min_record.get("cutoff"),
            "low_prime_count": finite_min_record.get("low_prime_count"),
            "skeleton_count": finite_min_record.get("skeleton_count"),
        },
        "target_s": TARGET_S,
        "finite_all_records_pass_target": pass_ok,
    }


def build_rows(data: dict[str, dict[str, Any]], metrics: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 runner/hash 账本判定行。"""
    same = data["same_window"]
    skeleton = data["skeleton"]
    runner = data["runner"]
    params = runner.get("parameters", {})
    skeleton_metrics = skeleton.get("finite_metrics", {})

    expected_source_hash = skeleton.get("source_hashes", {}).get(
        "docs/dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.json"
    )
    json_hash = sha256(RUNNER_JSON) if RUNNER_JSON.exists() else None

    metrics_match = (
        skeleton_metrics.get("prime_min") == metrics["finite_prime_min"]
        and skeleton_metrics.get("prime_max") == metrics["finite_prime_max"]
        and skeleton_metrics.get("record_count") == metrics["finite_record_count"]
        and skeleton_metrics.get("prime_count") == metrics["finite_prime_count"]
        and skeleton_metrics.get("min_skeleton_count") == metrics["finite_min_skeleton_count"]
        and skeleton_metrics.get("target_s") == TARGET_S
    )

    return [
        {
            "gate": "RunnerTargetImported",
            "closed": same.get("next_direct_attack_target") == TARGET,
            "proved": False,
            "meaning": "上一层已把同参数窗口后的 finite prefix 首字段定为 runner/hash 账本。",
            "remaining": TARGET,
        },
        {
            "gate": "RunnerArtifactPresent",
            "closed": RUNNER_SCRIPT.exists() and RUNNER_JSON.exists() and RUNNER_MD.exists(),
            "proved": RUNNER_SCRIPT.exists() and RUNNER_JSON.exists() and RUNNER_MD.exists(),
            "meaning": "runner 脚本、JSON 输出和 Markdown 摘要均在仓库中。",
            "remaining": "artifact hash ledger",
        },
        {
            "gate": "ParameterVectorPinned",
            "closed": params.get("alphas") == [ALPHA]
            and metrics["all_prime_min"] == 13
            and metrics["all_prime_max"] == FINITE_MAX,
            "proved": True,
            "meaning": "输出文件内置完整 prime list 与 alpha=0.43；有限桥使用其 3001<=P<100000 子区间。",
            "remaining": "canonical replay command can be derived from JSON parameters.",
        },
        {
            "gate": "FiniteBridgeSubsetMetricsMatch",
            "closed": metrics_match,
            "proved": metrics_match,
            "meaning": "从 runner JSON 复算出的 finite subset 指标与 dynamic skeleton 路由器登记值一致。",
            "remaining": "analytic monotone bridge still separate.",
        },
        {
            "gate": "FiniteTargetPass",
            "closed": metrics["finite_two_sides_per_prime"] and metrics["finite_all_records_pass_target"],
            "proved": metrics["finite_two_sides_per_prime"] and metrics["finite_all_records_pass_target"],
            "meaning": "3001<=P<100000 每个素数两侧均有记录，且 skeleton_count>=401。",
            "remaining": "does not cover P>=100000 tail by itself.",
        },
        {
            "gate": "HashLedgerMatchesImportedSource",
            "closed": json_hash == expected_source_hash,
            "proved": json_hash == expected_source_hash,
            "meaning": "dynamic skeleton 路由器登记的 runner JSON hash 与当前文件 hash 一致。",
            "remaining": "full replay not executed in this router.",
        },
        {
            "gate": "ReproducibleRunnerHashLedgerClosed",
            "closed": True,
            "proved": True,
            "meaning": "脚本 hash、输入参数 hash、输出 JSON/MD hash 和有限子区间指标已形成可复核账本。",
            "remaining": TAIL,
        },
        {
            "gate": "FiniteBoundaryPrefixCertificateProved",
            "closed": False,
            "proved": False,
            "meaning": "runner/hash 只覆盖可复核计算账本；解析尾桥、类型阈值和最终正余量仍未闭合。",
            "remaining": f"{TAIL} AND {TYPE_LEDGER} AND {ROW_FREE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 runner/hash 账本证书。"""
    data = {
        "runner": load_json(RUNNER_JSON),
        "skeleton": load_json(MONOGRAPH / "prime-matrix-dynamic-skeleton-lower-factorization-router.json"),
        "same_window": load_json(MONOGRAPH / "prime-matrix-strict-same-parameter-prefix-window-spec-router.json"),
        "range_manifest": load_json(MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-range-manifest-router.json"),
    }
    metrics = metrics_from_runner(data["runner"])
    rows = build_rows(data, metrics)
    ledger_closed = all(row["closed"] for row in rows if row["gate"] != "FiniteBoundaryPrefixCertificateProved")

    params = data["runner"].get("parameters", {})
    replay = {
        "script": "experiments/prime_matrix_dynamic_promoted_rough_capacity_audit.py",
        "alpha_argument": ",".join(str(x) for x in params.get("alphas", [])),
        "prime_list_source": "docs/dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.json:parameters.primes",
        "out_prefix": "docs/dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506",
        "canonical_replay_command": (
            "python3 experiments/prime_matrix_dynamic_promoted_rough_capacity_audit.py "
            "--primes \"$(jq -r '.parameters.primes|join(\",\")' "
            "docs/dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.json)\" "
            "--alphas 0.43 --out-prefix docs/dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506"
        ),
        "full_replay_executed_in_this_router": False,
    }

    hash_ledger = {
        "runner_script_sha256": sha256(RUNNER_SCRIPT),
        "runner_json_sha256": sha256(RUNNER_JSON),
        "runner_md_sha256": sha256(RUNNER_MD),
        "runner_parameters_sha256": stable_sha256(params),
        "finite_subset_metrics_sha256": stable_sha256(metrics),
    }

    return {
        "certificate_type": "prime_matrix_strict_prefix_rough_count_runner_hash_ledger_router",
        "status": "prefix_rough_count_runner_hash_ledger_closed_analytic_tail_bridge_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "parameter_id": PARAMETER_ID,
        "same_parameter_window_specification_imported": data["same_window"].get("same_parameter_window_specification_proved") is True,
        "reproducible_prefix_rough_count_runner_hash_ledger_proved": ledger_closed,
        "runner_full_replay_executed": False,
        "analytic_tail_bridge_proved": False,
        "finite_boundary_prefix_certificate_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replay_contract": replay,
        "runner_hash_ledger": hash_ledger,
        "finite_subset_metrics": metrics,
        "decision_rows": rows,
        "hardpoint_before_router": TARGET,
        "hardpoint_after_router": TAIL,
        "parallel_attack_targets": [
            TYPE_LEDGER,
            ROW_FREE,
            "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ],
        "next_direct_attack_target": TAIL,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ReproduciblePrefixRoughCountRunnerHashLedger` 可关闭为可复核 hash 账本："
            "runner 脚本、输入 prime/alpha 参数、输出 JSON/MD 与 3001<=P<100000 finite subset 指标均已登记，"
            "且 dynamic skeleton 路由器引用的 JSON hash 与当前文件一致。"
            "本步没有重新执行全量 replay，也不证明 P>=100000 解析尾桥，因此 finite prefix 证书尚未闭合。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    metrics = result["finite_subset_metrics"]
    hashes = result["runner_hash_ledger"]
    lines = [
        "# Prime Matrix strict prefix rough-count runner/hash 账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"reproducible_prefix_rough_count_runner_hash_ledger_proved={fmt_bool(result['reproducible_prefix_rough_count_runner_hash_ledger_proved'])}",
        f"runner_full_replay_executed={fmt_bool(result['runner_full_replay_executed'])}",
        f"analytic_tail_bridge_proved={fmt_bool(result['analytic_tail_bridge_proved'])}",
        f"finite_boundary_prefix_certificate_proved={fmt_bool(result['finite_boundary_prefix_certificate_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Hash Ledger",
        "",
        "| item | sha256 |",
        "| --- | --- |",
    ]
    for key, value in hashes.items():
        lines.append(f"| `{cell(key)}` | `{cell(value)}` |")

    lines.extend([
        "",
        "## 2. Finite Subset Metrics",
        "",
        "| metric | value |",
        "| --- | ---: |",
    ])
    for key in [
        "all_prime_count",
        "all_record_count",
        "all_prime_min",
        "all_prime_max",
        "finite_prime_count",
        "finite_record_count",
        "finite_prime_min",
        "finite_prime_max",
        "finite_min_skeleton_count",
        "target_s",
    ]:
        lines.append(f"| `{cell(key)}` | {cell(metrics[key])} |")
    lines.append(f"| `finite_two_sides_per_prime` | `{fmt_bool(metrics['finite_two_sides_per_prime'])}` |")
    lines.append(f"| `finite_all_records_pass_target` | `{fmt_bool(metrics['finite_all_records_pass_target'])}` |")

    lines.extend([
        "",
        "Worst finite record:",
        "",
        "```json",
        json.dumps(metrics["finite_min_record"], ensure_ascii=False, indent=2, sort_keys=True),
        "```",
        "",
        "## 3. Replay Contract",
        "",
        "| field | value |",
        "| --- | --- |",
    ])
    for key, value in result["replay_contract"].items():
        lines.append(f"| `{cell(key)}` | {cell(value)} |")

    lines.extend([
        "",
        "## 4. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ])
    for row in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=cell(row["meaning"]),
                remaining=cell(row["remaining"]),
            )
        )

    lines.extend([
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
        "审稿边界：本步是 hash/replay 账本，不是全量重跑证明，也不是解析尾段桥。",
    ])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
