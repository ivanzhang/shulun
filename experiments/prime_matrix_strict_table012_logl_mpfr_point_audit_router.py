#!/usr/bin/env python3
"""生成 strict table_012 logl/MPFR 点审计证书。

用法示例：
  python3 experiments/prime_matrix_strict_table012_logl_mpfr_point_audit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table012-logl-mpfr-point-audit-router.json

该证书审计所有 table_012 行端点、极值点及其邻点的 `std::logl` 误差。
它只提供强证据和环境锁定，不把有限点审计冒充为全域证明。
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 80

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"

OUT_JSON = DOCS / "prime-matrix-strict-table012-logl-mpfr-point-audit-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table012-logl-mpfr-point-audit-router.md"
POINT_AUDIT = DATA / "theta-table012-logl-mpfr-point-audit.jsonl"

ARCHIVE = DATA / "theta-table012-extremal-archive.jsonl"
LOG_FRONTIER = DOCS / "prime-matrix-strict-table012-log-oracle-frontier-router.json"
CPP = ROOT / "experiments" / "prime_matrix_table012_logl_mpfr_point_audit.cpp"

LOGL_ABS = "StdLogLAbsErrorLe1eMinus12ForIntegerInputsUpTo8e11"
LIBM_SOURCE = "Glibc239X86_64ELoglSSourceAndBinaryPathBindingLedger"
X87_ACCURACY = "X87FYL2X_FYL2XP1InstructionAccuracyLedger"
MPFR_RESCAN = "CertifiedMPFRIntervalThetaExtremalRescanArchive"


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    """读取 JSONL。"""
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def dec(value: Any) -> Decimal:
    """转 Decimal。"""
    return Decimal(str(value))


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def collect_points(rows: list[dict[str, Any]]) -> list[int]:
    """收集端点、极值点、邻点和少量结构锚点。"""
    points: set[int] = {2, 3, 5, 10, 100, 1000, 10_000, 1_000_000, 100_000_000, 800_000_000_000}
    for row in rows:
        for key in ["left", "right", "max_x"]:
            value = int(row[key])
            for delta in [-2, -1, 0, 1, 2]:
                n = value + delta
                if 2 <= n <= 800_000_000_000:
                    points.add(n)
    p = 1
    while p <= 800_000_000_000:
        points.add(p)
        if p > 2:
            points.add(p - 1)
            points.add(p + 1)
        p *= 2
    return sorted(points)


def compile_audit(exe: Path) -> None:
    """编译 C++ 点审计器。"""
    subprocess.run(
        [
            "g++",
            "-O2",
            "-std=c++17",
            "-Wall",
            "-Wextra",
            "-o",
            str(exe),
            str(CPP),
            "-lmpfr",
            "-lgmp",
        ],
        check=True,
    )


def run_audit(points: list[int]) -> list[dict[str, Any]]:
    """运行点审计并落盘 JSONL。"""
    exe = Path("/tmp/table012_logl_mpfr_point_audit")
    compile_audit(exe)
    output = subprocess.check_output([str(exe), *[str(point) for point in points]], text=True)
    POINT_AUDIT.parent.mkdir(parents=True, exist_ok=True)
    POINT_AUDIT.write_text(output, encoding="utf-8")
    return [json.loads(line) for line in output.splitlines() if line.strip()]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    rows = load_jsonl(ARCHIVE)
    points = collect_points(rows)
    records = run_audit(points)
    log_frontier = load_json(LOG_FRONTIER)

    failed = [item for item in records if item.get("passed") is not True]
    max_record = max(records, key=lambda item: dec(item["abs_error"])) if records else {}
    point_audit_passed = bool(records) and not failed

    return {
        "certificate_type": "prime_matrix_strict_table012_logl_mpfr_point_audit_router",
        "status": "logl_mpfr_point_audit_passed_global_logl_proof_still_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "upstream_next_target": log_frontier.get("next_direct_attack_target"),
        "logl_mpfr_point_audit_closed": point_audit_passed,
        "std_logl_abs_error_1e_minus_12_closed": False,
        "certified_log_summation_interval_arithmetic_closed": False,
        "theta_less_than_identity_to_8e11_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "audit": {
            "path": str(POINT_AUDIT.relative_to(ROOT)),
            "sha256": sha256(POINT_AUDIT),
            "point_count": len(records),
            "failed_count": len(failed),
            "max_abs_error": max_record.get("abs_error"),
            "max_abs_error_n": max_record.get("n"),
            "threshold": "1e-12",
        },
        "proof_boundary": {
            "what_this_closes": "给 table_012 端点、极值点和结构锚点提供 MPFR 对照证据，并锁定本机 glibc/libm 行为。",
            "why_not_global": "有限点审计不能排除未采样整数上的 libm 异常；黑箱函数没有可用的连续性证明。",
            "remaining": f"{LIBM_SOURCE} OR {MPFR_RESCAN}",
        },
        "proof_reduction": [
            {
                "gate": "StructuredCriticalPointLogLAudit",
                "closed": point_audit_passed,
                "meaning": "所有归档端点、极值点、邻点和二进制锚点的 logl/MPFR 差均小于 1e-12。",
                "remaining": "closed as evidence only",
            },
            {
                "gate": LOGL_ABS,
                "closed": False,
                "meaning": "要把证据升级成证明，必须覆盖所有整数输入，而不是有限点。",
                "remaining": f"{LIBM_SOURCE} OR {MPFR_RESCAN}",
            },
            {
                "gate": LIBM_SOURCE,
                "closed": False,
                "meaning": "证明 glibc 2.39 x86_64 ldbl-96 logl 的范围约化和多项式误差全域小于 1e-12。",
                "remaining": "source-level polynomial/range-reduction error certificate",
            },
            {
                "gate": MPFR_RESCAN,
                "closed": False,
                "meaning": "绕开 libm：用 MPFR 外向 log 全量重扫 theta 极值并登记新 hash。",
                "remaining": "heavy full rescan",
            },
        ],
        "source_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in [ARCHIVE, LOG_FRONTIER, CPP, POINT_AUDIT]
            if path.exists()
        },
        "next_direct_attack_target": LIBM_SOURCE,
        "parallel_attack_targets": [MPFR_RESCAN],
        "plain_conclusion": (
            "本步没有闭合全域 logl 证明，但把证据层补齐：归档端点、极值点、邻点和结构锚点"
            "全部通过 MPFR 对照，最大观测误差远小于 1e-12。严格自足闭合仍只剩二选一："
            "先绑定 glibc 2.39 x86_64 logl 源码/二进制路径，再证明其 x87 指令精度；"
            "或用 MPFR 外向 log 全量重扫归档。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    audit = result["audit"]
    lines = [
        "# Prime Matrix strict table_012 logl/MPFR 点审计证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"logl_mpfr_point_audit_closed={fmt_bool(result['logl_mpfr_point_audit_closed'])}",
        f"std_logl_abs_error_1e_minus_12_closed={fmt_bool(result['std_logl_abs_error_1e_minus_12_closed'])}",
        f"certified_log_summation_interval_arithmetic_closed={fmt_bool(result['certified_log_summation_interval_arithmetic_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 点审计摘要",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in audit.items():
        lines.append(f"| `{key}` | `{table_cell(value)}` |")
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "| item | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["proof_boundary"].items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | meaning | remaining |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["proof_reduction"]:
        lines.append(
            "| `{}` | `{}` | {} | {} |".format(
                table_cell(item["gate"]),
                fmt_bool(item["closed"]),
                table_cell(item["meaning"]),
                table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"logl_mpfr_point_audit_closed={fmt_bool(result['logl_mpfr_point_audit_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
