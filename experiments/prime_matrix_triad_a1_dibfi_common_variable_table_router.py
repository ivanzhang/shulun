#!/usr/bin/env python3
"""建立 DI/BFI 窗口匹配的共同变量表。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_common_variable_table_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-common-variable-table-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-common-variable-table-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DIBFI_WINDOW_MATCH = (
    DOCS / "prime-matrix-triad-a1-dibfi-window-match-router.json"
)
DEFAULT_THEOREM_LOCATION = (
    DOCS / "prime-matrix-triad-a1-dibfi-theorem-location-router.json"
)
DEFAULT_KLS_TEMPLATE = DOCS / "kls-window-di-bfi-adaptation-template.md"
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_SOURCE_CEN = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def contains_all(path: Path, needles: list[str]) -> bool:
    """核查文档是否含有全部关键词。"""
    text = path.read_text(encoding="utf-8")
    return all(needle in text for needle in needles)


def build_variable_rows() -> list[dict[str, Any]]:
    """构造 AP、KE-13/WFD 与 DI/BFI 共用变量表。"""
    return [
        {
            "symbol": "X",
            "prime_matrix_role": "clean A1/HLC 分支交给解析 dispersion 的总长度尺度",
            "ap_role": "BFI prime-AP discrepancy 的 ambient length",
            "wfd_role": "Type-I/II 分块满足 N*M≈X",
            "dibfi_role": "BFI Theorem 10 的 x 参数",
            "transfer_use": "保持原始误差对象的总质量尺度",
            "scale_use": "所有 Q,N,M,C,S,H 的上界都归一到 X",
            "fixed_by_table": True,
        },
        {
            "symbol": "Q",
            "prime_matrix_role": "clean branch 的 well-factorable 模数总 level",
            "ap_role": "q<=Q 的 AP 模数范围",
            "wfd_role": "lambda_q 或 lambda_c 的总支撑 level",
            "dibfi_role": "BFI well-factorable level",
            "transfer_use": "AP 模权不换成 canonical support 权",
            "scale_use": "需证明 Q<=X^(4/7-eps) 或当前引用版允许的等价范围",
            "fixed_by_table": True,
        },
        {
            "symbol": "N,M",
            "prime_matrix_role": "Vaughan/Heath-Brown 后的素数/互补因子 dyadic 块",
            "ap_role": "nm≡a mod q 的双变量",
            "wfd_role": "Type-I/II 输入，N*M≈X",
            "dibfi_role": "BFI dispersion 的 Dirichlet polynomial blocks",
            "transfer_use": "把 AP 误差拆块但不改变求和对象",
            "scale_use": "需证明每个 dyadic 块落入 BFI/DI 处理范围",
            "fixed_by_table": True,
        },
        {
            "symbol": "c,C",
            "prime_matrix_role": "CRT/gcd 剥离后的有效 Kloosterman 模数 dyadic 块",
            "ap_role": "由 q 或 q 的因子组合产生的模数块",
            "wfd_role": "KE-13 中 c~C 的 well-factorable 模数变量",
            "dibfi_role": "DI Theorem 12 的 Kloosterman modulus family",
            "transfer_use": "dispersion 后保留同一模数责任，不切到 canonical 分支",
            "scale_use": "需证明 C 与 Q、X 的关系满足 DI J-scale 估计",
            "fixed_by_table": True,
        },
        {
            "symbol": "s,S",
            "prime_matrix_role": "completion 后的可逆类或尾素/互补单位变量",
            "ap_role": "Type block 中进入逆元相位的变量",
            "wfd_role": "KE-13 中 s~S, (s,c)=1 的逆元变量",
            "dibfi_role": "DI Kloosterman 分子中的可逆类变量",
            "transfer_use": "CRT 合并 s1,s2 后得到同一 s 变量",
            "scale_use": "需证明 S 的 dyadic 范围与 DI estimate 的 N/R/S 参数匹配",
            "fixed_by_table": True,
        },
        {
            "symbol": "h,H",
            "prime_matrix_role": "sawtooth/Fourier 非零频率",
            "ap_role": "AP discrepancy 完成后的非主频",
            "wfd_role": "KE-13 中 0<|h|<=H 的频率变量",
            "dibfi_role": "DI/BFI Kloosterman/Bessel frequency parameter",
            "transfer_use": "h=0 主项扣除，h!=0 保留原始误差频率",
            "scale_use": "需证明 H 截断尾项和 DI 频率范围同时满足",
            "fixed_by_table": True,
        },
        {
            "symbol": "lambda",
            "prime_matrix_role": "generic WFD 分支的 well-factorable 模权",
            "ap_role": "BFI Theorem 10 的 lambda_q",
            "wfd_role": "KE-13 的 lambda_c",
            "dibfi_role": "well-factorable weight",
            "transfer_use": "不替换为 canonical RIW/Buchstab support 证明",
            "scale_use": "level 与分解层数只产生 log^O 损失",
            "fixed_by_table": True,
        },
        {
            "symbol": "alpha,beta,omega",
            "prime_matrix_role": "Type 系数与平滑频率权",
            "ap_role": "Dirichlet polynomial coefficients and smooth cutoffs",
            "wfd_role": "divisor-bounded beta_s 与 smooth omega_h",
            "dibfi_role": "DI/BFI 二范数与平滑权输入",
            "transfer_use": "系数由分解/平滑产生，不能加入块中心化均值扣除",
            "scale_use": "二范数、导数和平滑损失进入 log^C 账本",
            "fixed_by_table": True,
        },
        {
            "symbol": "g",
            "prime_matrix_role": "非互素模数层",
            "ap_role": "q 因子或 r1,r2 的 gcd stratum",
            "wfd_role": "(r1,r2)=g 强迫 s1≡s2 mod g",
            "dibfi_role": "非互素层的 divisor/gcd 损失",
            "transfer_use": "不相容层为零，相容层不改变目标对象",
            "scale_use": "sum_g tau(g)^C/g 进入 log^C",
            "fixed_by_table": True,
        },
        {
            "symbol": "A,B(A),C0",
            "prime_matrix_role": "最终任意对数节省目标与损失预算",
            "ap_role": "x/log^A x 目标强度",
            "wfd_role": "KE-13 的 log^{-A} 节省",
            "dibfi_role": "外部定理给任意 log-saving 后吸收损失",
            "transfer_use": "所有转移损失只允许进入 log^C0",
            "scale_use": "选择 B(A)=A+C0+10",
            "fixed_by_table": True,
        },
    ]


def build_transfer_rows() -> list[dict[str, Any]]:
    """构造对象不变转移的同变量方程。"""
    return [
        {
            "step": "APError",
            "formula": "E_AP(X,Q)=sum_{q<=Q} lambda_q sum_{nm≈X} a_n b_m Delta_q(nm)",
            "same_variables": "X,Q,N,M,lambda,alpha,beta",
            "target_preserved": True,
            "remaining_proof": "把 clean A1 generic WFD 残差精确写成该 AP error 或其 dyadic 总和",
        },
        {
            "step": "TypeDecomposition",
            "formula": "E_AP=sum_{N*M≈X} E_{N,M}+log^O endpoint errors",
            "same_variables": "X,N,M,alpha,beta",
            "target_preserved": True,
            "remaining_proof": "证明 Vaughan/Heath-Brown 分解后的端点误差均进入 log budget",
        },
        {
            "step": "DispersionCauchy",
            "formula": "E_{N,M} -> E_disp(r1,r2,s1,s2,h) without block-centering insertion",
            "same_variables": "Q,N,M,c,s,h,lambda,beta,omega",
            "target_preserved": False,
            "remaining_proof": "写出从 BFI 原始 dispersion 到 KE-5 的逐项恒等式，确认未删同块对角",
        },
        {
            "step": "CRTPhase",
            "formula": "phase(r1,r2,s1,s2,h)=e_c(a_h*s+b_h*bar(s))",
            "same_variables": "c,s,h,g",
            "target_preserved": True,
            "remaining_proof": "已有模板；最终稿中需把符号与 KE-13 完全统一",
        },
        {
            "step": "KE13Identification",
            "formula": "E_disp main nonzero-frequency blocks = WFD_core(C,S,H,lambda,beta,omega)",
            "same_variables": "C,S,H,lambda,beta,omega,A",
            "target_preserved": False,
            "remaining_proof": "证明所有 dyadic 主块完全覆盖且无额外中心化/投影项",
        },
    ]


def build_scale_rows() -> list[dict[str, Any]]:
    """构造尺度不等式共同表。"""
    return [
        {
            "inequality": "TypeProduct",
            "statement": "N*M≈X",
            "variables": "X,N,M",
            "needed_for": "BFI AP discrepancy and Type-I/II dispersion",
            "status": "named_not_quantified",
            "closed": False,
        },
        {
            "inequality": "BFILevel",
            "statement": "Q<=X^(4/7-eps) or an explicitly stronger admitted range",
            "variables": "X,Q,eps",
            "needed_for": "BFI1986-Theorem10",
            "status": "named_not_quantified",
            "closed": False,
        },
        {
            "inequality": "KLSModulusWindow",
            "statement": "C is a dyadic sublevel of Q and matches the DI modulus family",
            "variables": "C,Q,X",
            "needed_for": "DI1982-Theorem12",
            "status": "named_not_quantified",
            "closed": False,
        },
        {
            "inequality": "InverseVariableWindow",
            "statement": "S matches the DI inverse-variable length after completion",
            "variables": "S,N,M,C",
            "needed_for": "DI1982-Theorem12",
            "status": "named_not_quantified",
            "closed": False,
        },
        {
            "inequality": "FrequencyWindow",
            "statement": "0<|h|<=H and Fourier tail is absorbed by B(A)",
            "variables": "H,X,C,S,A",
            "needed_for": "DI/BFI plus sawtooth completion",
            "status": "named_not_quantified",
            "closed": False,
        },
        {
            "inequality": "DIJScaleDominance",
            "statement": "DI Theorem 12 J-scale bound is <= natural WFD scale/log^A after substitution",
            "variables": "C,S,H,N,M,Q,A",
            "needed_for": "KE-13 log-saving",
            "status": "main_remaining_scale_certificate",
            "closed": False,
        },
        {
            "inequality": "LogLossAbsorption",
            "statement": "B(A)=A+C0+10 absorbs dyadic, gcd, endpoint, coefficient and smoothing costs",
            "variables": "A,B(A),C0,g,lambda,beta,omega",
            "needed_for": "final arbitrary log-saving",
            "status": "ledger_ready_needs_C0_extraction",
            "closed": False,
        },
    ]


def build_gate_rows(
    window_match: dict[str, Any],
    theorem_location: dict[str, Any],
    kls_template_path: Path,
    kze_spine_path: Path,
    source_cen_path: Path,
) -> list[dict[str, Any]]:
    """构造共同变量表门控。"""
    kls_ready = contains_all(kls_template_path, ["变量适配表", "相位归一化", "B(A)"])
    kze_ready = contains_all(kze_spine_path, ["KE-13", "WFD-core", "KE-5", "KE-8"])
    source_cen_ready = contains_all(source_cen_path, ["SOURCE-CEN is false", "未块中心化"])
    return [
        {
            "gate": "PreviousFrontierIsWindowMatch",
            "available": window_match["terminal_gap_after_router"],
            "needed": "start exactly from DIBFIWindowScaleAndTargetTransferMatch",
            "gap": "none",
            "route": "common variable table",
            "closed": window_match["terminal_gap_after_router"]
            == "DIBFIWindowScaleAndTargetTransferMatch",
        },
        {
            "gate": "TheoremLocationsStillPinned",
            "available": theorem_location["terminal_gap_after_router"],
            "needed": "BFI Theorem 10 and DI Theorem 12 remain fixed",
            "gap": "none",
            "route": "reuse theorem-location certificate",
            "closed": bool(theorem_location["theorem_locations_pinned"]),
        },
        {
            "gate": "NoVariableFork",
            "available": "one table contains AP, WFD and DI/BFI roles for every active symbol",
            "needed": "target transfer and scale inequalities must use the same symbols",
            "gap": "none after this router",
            "route": "common variable table",
            "closed": True,
        },
        {
            "gate": "TargetNotChangedByCentering",
            "available": "SOURCE-CEN no-go keeps the uncentered WFD target",
            "needed": "the table cannot add a hidden block-centering variable",
            "gap": "none at table level",
            "route": "uncentered target row",
            "closed": source_cen_ready,
        },
        {
            "gate": "LocalFormulasAvailable",
            "available": "KZ-E spine and KLS template contain KE-5, KE-8, KE-13 and variable adaptation",
            "needed": "common rows must reference existing local formulas",
            "gap": "none at table level",
            "route": "transfer rows plus scale rows",
            "closed": kls_ready and kze_ready,
        },
        {
            "gate": "TransferAndScaleCertificate",
            "available": "common variables are fixed",
            "needed": "prove transfer equations and scale inequalities using this table",
            "gap": "the actual certificate is not yet proved",
            "route": "DIBFICommonVariableTransferScaleCertificate",
            "closed": False,
        },
    ]


def run(
    window_match_path: Path,
    theorem_location_path: Path,
    kls_template_path: Path,
    kze_spine_path: Path,
    source_cen_path: Path,
) -> dict[str, Any]:
    """运行共同变量表路由。"""
    window_match = load_json(window_match_path)
    theorem_location = load_json(theorem_location_path)
    variable_rows = build_variable_rows()
    transfer_rows = build_transfer_rows()
    scale_rows = build_scale_rows()
    gate_rows = build_gate_rows(
        window_match,
        theorem_location,
        kls_template_path,
        kze_spine_path,
        source_cen_path,
    )
    open_gates = [row["gate"] for row in gate_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_common_variable_table_router",
        "status": "dibfi_common_variable_table_materialized_certificate_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "dibfi_window_match_json": file_sha256(window_match_path),
            "dibfi_theorem_location_json": file_sha256(theorem_location_path),
            "kls_template_md": file_sha256(kls_template_path),
            "kze_spine_md": file_sha256(kze_spine_path),
            "source_cen_no_go_md": file_sha256(source_cen_path),
        },
        "variable_rows": variable_rows,
        "transfer_rows": transfer_rows,
        "scale_rows": scale_rows,
        "gate_rows": gate_rows,
        "open_gates": open_gates,
        "common_variable_table_materialized": True,
        "no_variable_fork": True,
        "target_transfer_and_scale_share_variables": True,
        "all_transfer_steps_target_preserving": all(
            row["target_preserved"] for row in transfer_rows
        ),
        "all_scale_inequalities_closed": all(row["closed"] for row in scale_rows),
        "next_external_target": "DIBFICommonVariableTransferScaleCertificate",
        "terminal_gap_after_router": "DIBFICommonVariableTransferScaleCertificate",
        "structural_law": (
            "The two remaining DI/BFI obligations now live on one variable table. "
            "Target transfer and scale inequalities cannot be solved independently with different "
            "symbols: X,Q,N,M,C,S,H,lambda,beta,omega,g,A,B(A) are shared across AP discrepancy, "
            "KE-13/WFD-core and DI/BFI theorem inputs. Therefore the next proof target is a single "
            "certificate: prove the listed transfer equations and scale inequalities on this common table."
        ),
        "review_conclusion": (
            "共同变量表已建立，两个硬点被锁到同一套变量上。当前不再是两个发散任务，而是一个"
            "合取证书：同一变量表上同时证明对象不变转移与尺度不等式。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI 共同变量表路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "one variable table:",
        "  X,Q,N,M,C,S,H,lambda,beta,omega,g,A,B(A);",
        "",
        "same variables feed:",
        "  AP discrepancy;",
        "  KE-13/WFD-core;",
        "  BFI Theorem 10;",
        "  DI Theorem 12;",
        "",
        "next certificate:",
        f"  {result['terminal_gap_after_router']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `common_variable_table_materialized={fmt_bool(result['common_variable_table_materialized'])}`。",
        f"- `no_variable_fork={fmt_bool(result['no_variable_fork'])}`。",
        f"- `target_transfer_and_scale_share_variables={fmt_bool(result['target_transfer_and_scale_share_variables'])}`。",
        f"- `all_transfer_steps_target_preserving={fmt_bool(result['all_transfer_steps_target_preserving'])}`。",
        f"- `all_scale_inequalities_closed={fmt_bool(result['all_scale_inequalities_closed'])}`。",
        f"- `open_gates={result['open_gates']}`。",
        f"- `next_external_target={result['next_external_target']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 共同变量表",
        "",
        "| symbol | prime-matrix role | AP role | WFD role | DI/BFI role | transfer use | scale use | fixed |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["variable_rows"]:
        lines.append(
            "| `{symbol}` | {pm} | {ap} | {wfd} | {dibfi} | {transfer} | {scale} | `{fixed}` |".format(
                symbol=table_cell(row["symbol"]),
                pm=table_cell(row["prime_matrix_role"]),
                ap=table_cell(row["ap_role"]),
                wfd=table_cell(row["wfd_role"]),
                dibfi=table_cell(row["dibfi_role"]),
                transfer=table_cell(row["transfer_use"]),
                scale=table_cell(row["scale_use"]),
                fixed=fmt_bool(bool(row["fixed_by_table"])),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 对象转移方程",
            "",
            "| step | formula | same variables | target preserved | remaining proof |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["transfer_rows"]:
        lines.append(
            "| `{step}` | `{formula}` | {variables} | `{preserved}` | {remaining} |".format(
                step=table_cell(row["step"]),
                formula=table_cell(row["formula"]),
                variables=table_cell(row["same_variables"]),
                preserved=fmt_bool(bool(row["target_preserved"])),
                remaining=table_cell(row["remaining_proof"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 尺度不等式表",
            "",
            "| inequality | statement | variables | needed for | status | closed |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["scale_rows"]:
        lines.append(
            "| `{ineq}` | `{statement}` | {variables} | {needed_for} | `{status}` | `{closed}` |".format(
                ineq=table_cell(row["inequality"]),
                statement=table_cell(row["statement"]),
                variables=table_cell(row["variables"]),
                needed_for=table_cell(row["needed_for"]),
                status=table_cell(row["status"]),
                closed=fmt_bool(bool(row["closed"])),
            )
        )
    lines.extend(
        [
            "",
            "## 6. 门控表",
            "",
            "| gate | available | needed | gap | route | closed |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["gate_rows"]:
        lines.append(
            "| `{gate}` | {available} | {needed} | {gap} | {route} | `{closed}` |".format(
                gate=table_cell(row["gate"]),
                available=table_cell(row["available"]),
                needed=table_cell(row["needed"]),
                gap=table_cell(row["gap"]),
                route=table_cell(row["route"]),
                closed=fmt_bool(bool(row["closed"])),
            )
        )
    lines.extend(
        [
            "",
            "## 7. 当前结论",
            "",
            "共同变量表已经完成，剩余目标不是两个可分散处理的口号，而是一个单一证书：",
            "",
            "```text",
            "DIBFICommonVariableTransferScaleCertificate",
            "```",
            "",
            "该证书必须同时证明对象转移方程和尺度不等式；若任何一行失败，generic WFD 外部 DI/BFI "
            "引用版仍不能标记闭合。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dibfi-window-match-json", type=Path, default=DEFAULT_DIBFI_WINDOW_MATCH
    )
    parser.add_argument(
        "--dibfi-theorem-location-json", type=Path, default=DEFAULT_THEOREM_LOCATION
    )
    parser.add_argument("--kls-template-md", type=Path, default=DEFAULT_KLS_TEMPLATE)
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--source-cen-md", type=Path, default=DEFAULT_SOURCE_CEN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        window_match_path=args.dibfi_window_match_json,
        theorem_location_path=args.dibfi_theorem_location_json,
        kls_template_path=args.kls_template_md,
        kze_spine_path=args.kze_spine_md,
        source_cen_path=args.source_cen_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "no_variable_fork": result["no_variable_fork"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
