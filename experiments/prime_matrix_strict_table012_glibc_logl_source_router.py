#!/usr/bin/env python3
"""生成 strict table_012 glibc logl 源码绑定证书。

用法示例：
  python3 experiments/prime_matrix_strict_table012_glibc_logl_source_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table012-glibc-logl-source-router.json

本证书只关闭“当前 logl 证明对象到底是什么”：
glibc 2.39 x86_64 的 long-double log 路径不是软件多项式 log，
而是 `sysdeps/x86_64/fpu/e_logl.S` 中的 x87 `fyl2x/fyl2xp1` 路线。
因此下一硬点应改成 x87 指令精度账本，或绕开 libm 做 MPFR 全量重扫。
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"

OUT_JSON = DOCS / "prime-matrix-strict-table012-glibc-logl-source-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table012-glibc-logl-source-router.md"

SOURCE_URL = "https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=sysdeps/x86_64/fpu/e_logl.S;hb=glibc-2.39"
CODE_BROWSER_URL = "https://codebrowser.dev/glibc/glibc/sysdeps/x86_64/fpu/e_logl.S.html"
INTEL_SDM_URL = "https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html"

SOURCE_CACHE = DATA / "glibc-2.39-x86_64-e_logl.S"
DISASM_CACHE = DATA / "glibc-2.39-libm-logl-disassembly.txt"
LOG_POINT_AUDIT = DOCS / "prime-matrix-strict-table012-logl-mpfr-point-audit-router.json"
LIBM = Path("/lib/x86_64-linux-gnu/libm.so.6")

OLD_SOURCE = "Glibc239Ldbl96LoglSourceAndPolynomialErrorLedger"
SOURCE_BINDING = "Glibc239X86_64ELoglSSourceAndBinaryPathBindingLedger"
X87_ACCURACY = "X87FYL2X_FYL2XP1InstructionAccuracyLedger"
MPFR_RESCAN = "CertifiedMPFRIntervalThetaExtremalRescanArchive"
LOGL_ABS = "StdLogLAbsErrorLe1eMinus12ForIntegerInputsUpTo8e11"


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def fetch_source() -> str:
    """下载或读取 glibc 2.39 e_logl.S 源码。"""
    DATA.mkdir(parents=True, exist_ok=True)
    if not SOURCE_CACHE.exists():
        content = urlopen(SOURCE_URL, timeout=20).read().decode("utf-8")
        SOURCE_CACHE.write_text(content, encoding="utf-8")
    return SOURCE_CACHE.read_text(encoding="utf-8")


def objdump_text(start: str, stop: str) -> str:
    """读取本机 libm 的反汇编片段。"""
    return subprocess.check_output(
        ["objdump", "-d", f"--start-address={start}", f"--stop-address={stop}", str(LIBM)],
        text=True,
    )


def symbol_table() -> str:
    """读取 logl 相关符号表。"""
    return subprocess.check_output(["objdump", "-T", str(LIBM)], text=True)


def build_result() -> dict[str, Any]:
    """构造源码绑定证书。"""
    source = fetch_source()
    wrapper_disasm = objdump_text("0x11c60", "0x11d05")
    core_disasm = objdump_text("0x1a510", "0x1a56c")
    finite_disasm = objdump_text("0x1a570", "0x1a5a6")
    symbols = "\n".join(line for line in symbol_table().splitlines() if " logl" in line or "__logl_finite" in line)
    DISASM_CACHE.write_text(
        "\n".join(
            [
                "== symbols ==",
                symbols,
                "",
                "== logl wrapper ==",
                wrapper_disasm,
                "",
                "== shared x87 core ==",
                core_disasm,
                "",
                "== __logl_finite ==",
                finite_disasm,
                "",
            ]
        ),
        encoding="utf-8",
    )

    source_uses_x87 = "fyl2x" in source and "fyl2xp1" in source and "fldln2" in source
    binary_uses_x87 = "fyl2x" in core_disasm and "fyl2xp1" in core_disasm and "fldln2" in core_disasm
    wrapper_jumps_to_core = "jmp" in wrapper_disasm and "1a510" in wrapper_disasm
    finite_symbol_present = "__logl_finite" in symbols and "1a570" in symbols
    polynomial_route_rejected = source_uses_x87 and binary_uses_x87
    source_binding_closed = source_uses_x87 and binary_uses_x87 and wrapper_jumps_to_core and finite_symbol_present
    point_audit = load_json(LOG_POINT_AUDIT)

    return {
        "certificate_type": "prime_matrix_strict_table012_glibc_logl_source_router",
        "status": "glibc_logl_source_bound_x87_instruction_accuracy_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "upstream_point_audit_closed": point_audit.get("logl_mpfr_point_audit_closed") is True,
        "glibc_logl_source_binding_closed": source_binding_closed,
        "software_polynomial_error_route_rejected": polynomial_route_rejected,
        "x87_instruction_accuracy_closed": False,
        "std_logl_abs_error_1e_minus_12_closed": False,
        "certified_log_summation_interval_arithmetic_closed": False,
        "theta_less_than_identity_to_8e11_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "source": {
            "url": SOURCE_URL,
            "code_browser_url": CODE_BROWSER_URL,
            "cache_path": str(SOURCE_CACHE.relative_to(ROOT)),
            "sha256": sha256(SOURCE_CACHE),
            "uses_fyl2x": "fyl2x" in source,
            "uses_fyl2xp1": "fyl2xp1" in source,
            "uses_fldln2": "fldln2" in source,
        },
        "binary": {
            "path": str(LIBM),
            "sha256": sha256(LIBM),
            "disassembly_path": str(DISASM_CACHE.relative_to(ROOT)),
            "disassembly_sha256": sha256(DISASM_CACHE),
            "symbols": symbols.splitlines(),
            "wrapper_jumps_to_core_0x1a510": wrapper_jumps_to_core,
            "core_uses_fyl2x": "fyl2x" in core_disasm,
            "core_uses_fyl2xp1": "fyl2xp1" in core_disasm,
            "finite_symbol_present": finite_symbol_present,
        },
        "proof_reduction": [
            {
                "gate": OLD_SOURCE,
                "closed": False,
                "meaning": "旧名字里的 polynomial route 与源码不匹配；glibc 2.39 x86_64 logl 走 x87 指令。",
                "remaining": SOURCE_BINDING,
            },
            {
                "gate": SOURCE_BINDING,
                "closed": source_binding_closed,
                "meaning": "官方 e_logl.S、本机符号表和反汇编已绑定到同一个 x87 fyl2x/fyl2xp1 实现路径。",
                "remaining": "closed" if source_binding_closed else "source/binary path mismatch",
            },
            {
                "gate": X87_ACCURACY,
                "closed": False,
                "meaning": "需从 Intel/AMD x87 指令语义或实测形式化证书推出 FYL2X/FYL2XP1 在本输入域误差 <= 1e-12。",
                "remaining": "architectural instruction error bound or exhaustive interval replacement",
            },
            {
                "gate": MPFR_RESCAN,
                "closed": False,
                "meaning": "替代路线：完全绕开 x87/libm，用 MPFR 外向 log 全量重扫 theta 极值归档。",
                "remaining": "heavy full archive rescan",
            },
            {
                "gate": LOGL_ABS,
                "closed": False,
                "meaning": "只有 x87 指令精度账本或 MPFR 重扫闭合后，logl 全域误差命题才闭合。",
                "remaining": f"{X87_ACCURACY} OR {MPFR_RESCAN}",
            },
        ],
        "external_references": {
            "glibc_e_logl_source": CODE_BROWSER_URL,
            "intel_sdm": INTEL_SDM_URL,
        },
        "source_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in [SOURCE_CACHE, DISASM_CACHE, LOG_POINT_AUDIT]
            if path.exists()
        },
        "next_direct_attack_target": X87_ACCURACY,
        "parallel_attack_targets": [MPFR_RESCAN],
        "plain_conclusion": (
            "glibc logl 的源码对象已绑定清楚：Ubuntu glibc 2.39 的 x86_64 long-double log "
            "实际依赖 x87 `fyl2x/fyl2xp1`，不是可直接做系数审计的软件多项式。"
            "因此旧的多项式误差证明路线应删除；唯一内部硬点改成 x87 指令精度账本。"
            "若不接受硬件指令精度证明，唯一自足替代就是 MPFR 外向 log 全量重扫。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict table_012 glibc logl 源码绑定证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"glibc_logl_source_binding_closed={fmt_bool(result['glibc_logl_source_binding_closed'])}",
        f"software_polynomial_error_route_rejected={fmt_bool(result['software_polynomial_error_route_rejected'])}",
        f"x87_instruction_accuracy_closed={fmt_bool(result['x87_instruction_accuracy_closed'])}",
        f"std_logl_abs_error_1e_minus_12_closed={fmt_bool(result['std_logl_abs_error_1e_minus_12_closed'])}",
        f"certified_log_summation_interval_arithmetic_closed={fmt_bool(result['certified_log_summation_interval_arithmetic_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 源码与二进制",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| `source_url` | `{table_cell(result['source']['url'])}` |",
        f"| `source_sha256` | `{result['source']['sha256']}` |",
        f"| `libm_sha256` | `{result['binary']['sha256']}` |",
        f"| `disassembly_sha256` | `{result['binary']['disassembly_sha256']}` |",
        f"| `wrapper_jumps_to_core_0x1a510` | `{fmt_bool(result['binary']['wrapper_jumps_to_core_0x1a510'])}` |",
        f"| `core_uses_fyl2x` | `{fmt_bool(result['binary']['core_uses_fyl2x'])}` |",
        f"| `core_uses_fyl2xp1` | `{fmt_bool(result['binary']['core_uses_fyl2xp1'])}` |",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | meaning | remaining |",
        "| --- | --- | --- | --- |",
    ]
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
            "## 3. 下一最窄点",
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
    print(f"glibc_logl_source_binding_closed={fmt_bool(result['glibc_logl_source_binding_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
