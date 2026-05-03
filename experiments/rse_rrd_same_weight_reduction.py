#!/usr/bin/env python3
"""RRD 同权归一化与两段式硬点拆解。

用法示例：
  python3 experiments/rse_rrd_same_weight_reduction.py
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import median
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_SCAN = MONOGRAPH / "kscwm-crd-dual-obstruction-scan.json"
DEFAULT_LEDGER = MONOGRAPH / "rse-rrd-ospc-margin-ledger.json"
DEFAULT_JSON = MONOGRAPH / "rse-rrd-same-weight-reduction.json"
DEFAULT_MD = MONOGRAPH / "rse-rrd-same-weight-reduction.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    if not path.exists():
        raise FileNotFoundError(f"缺少输入文件: {path}")
    return json.loads(path.read_text())


def summarize_scan(scan: dict[str, Any], rrd_budget: float) -> dict[str, Any]:
    """汇总旧 RRD 压力扫描，判断单密度替换是否足够。"""
    rows: list[dict[str, Any]] = []
    for case in scan.get("cases", []):
        ratio = float(case["rough_discrepancy_ratio"])
        rows.append(
            {
                "P": int(case["P"]),
                "M_exp": float(case["M_exp"]),
                "R_exp": float(case["R_exp"]),
                "term_count": int(case["term_count"]),
                "rough_discrepancy_ratio": ratio,
                "passes_rrd_budget_as_stress_test": ratio <= rrd_budget,
            }
        )
    ordered = sorted(rows, key=lambda row: row["rough_discrepancy_ratio"], reverse=True)
    by_m: dict[str, dict[str, Any]] = {}
    for row in rows:
        key = f"{row['M_exp']:.6g}"
        group = by_m.setdefault(key, {"M_exp": row["M_exp"], "ratios": [], "count": 0})
        group["ratios"].append(row["rough_discrepancy_ratio"])
        group["count"] += 1
    for group in by_m.values():
        ratios = group.pop("ratios")
        group["max_ratio"] = max(ratios)
        group["median_ratio"] = median(ratios)
        group["all_pass_budget_as_stress_test"] = group["max_ratio"] <= rrd_budget
    return {
        "case_count": len(rows),
        "rrd_budget": rrd_budget,
        "max_ratio": ordered[0]["rough_discrepancy_ratio"] if ordered else 0.0,
        "median_ratio": median([row["rough_discrepancy_ratio"] for row in rows]) if rows else 0.0,
        "hardest_case": ordered[0] if ordered else None,
        "groups_by_M_exp": sorted(by_m.values(), key=lambda group: group["M_exp"]),
        "top_cases": ordered[:8],
        "direct_one_density_replacement_passes": bool(ordered and ordered[0]["rough_discrepancy_ratio"] <= rrd_budget),
    }


def build_reduction(scan: dict[str, Any], ledger: dict[str, Any]) -> dict[str, Any]:
    """建立 RRD 同权归一化拆解账本。"""
    rrd_budget = next(float(item["budget"]) for item in ledger["budgets"] if item["key"] == "RRD")
    scan_summary = summarize_scan(scan, rrd_budget)
    return {
        "certificate_type": "rse_rrd_same_weight_reduction",
        "status": "same_weight_reduction_and_two_stage_rrd_obligation",
        "scan_source": str(DEFAULT_SCAN.relative_to(ROOT)),
        "ledger_source": str(DEFAULT_LEDGER.relative_to(ROOT)),
        "rrd_budget": rrd_budget,
        "scan_summary": scan_summary,
        "main_reduction": {
            "kernel_amplitude": "|K_{h,ell}(m)| <= 2*pi*h*H/(ell*M) on m~M when hH/(ell M) is small",
            "coefficient_cancellation": "(|omega_ell|/h) * (h/ell) = |omega_ell|/ell",
            "same_weight_norm": "RRD naturally lands in the same Selberg variation norm V_omega=sum |omega_ell|/ell",
            "sufficient_bound": "C_RRD <= Theta_crit*(eta_low + eta_perp) with Theta_crit<=1 under the same critical-band convention",
        },
        "two_stage_targets": [
            {
                "key": "RRD-low",
                "budget": 0.006,
                "meaning": "粗数指示函数中由小模周期/低 Buchstab 层产生的可见结构项。",
                "required_action": "证明该低模项或者被并入 OSPC/CRTDefect 出口，或者在 RRD 账本中消耗不超过 0.006。",
            },
            {
                "key": "RRD-perp",
                "budget": 0.012,
                "meaning": "去掉低模投影后的正交粗数余项。",
                "required_action": "用 Buchstab 分解、CRT 非零类均衡和短窗不可复用证明同权测试范数不超过 0.012。",
            },
            {
                "key": "RRD-conversion",
                "budget": 0.002,
                "meaning": "振幅线性化、dyadic 端点和 H/M 归一化换算误差。",
                "required_action": "把 |1-e(t)| 的二阶余项、端点层和有限截断误差全部外向舍入进 0.002。",
            },
        ],
        "review_conclusion": (
            "旧的一步常数密度替换在压力样本中最坏 roughDiff/env 约为 "
            f"{scan_summary['max_ratio']:.6f}，不能直接作为 C_RRD<=0.020 的证明。"
            "可行路线是先剥离低模/Buchstab 可见结构，再只对正交余项证明同权小范数。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """生成 Markdown 审查报告。"""
    summary = audit["scan_summary"]
    hardest = summary["hardest_case"]
    lines = [
        "# RRD 同权归一化与两段式拆解",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告专攻 `RRD`：把粗数替换误差从原始振荡和式中剥离出来，检查它能否进入上一轮建立的 `C_RRD<=0.020` 账本。",
        "",
        "## 1. 直接单密度替换的压力结论",
        "",
        f"- RRD 账本目标：`C_RRD<={audit['rrd_budget']:.3f}`。",
        f"- 旧扫描样本数：`{summary['case_count']}`。",
        f"- 旧 `roughDiff/env` 最大值：`{summary['max_ratio']:.6f}`。",
        f"- 旧 `roughDiff/env` 中位数：`{summary['median_ratio']:.6f}`。",
        f"- 最坏样本：`P={hardest['P']}, M=P^{hardest['M_exp']}, R=P^{hardest['R_exp']}`。",
        "",
        "结论：旧的一步常数密度替换不能直接当作 `C_RRD<=0.020` 的证明。它是定位工具，不是终局 RRD 估计。",
        "",
        "按 `M` 层分组：",
        "",
        "| M_exp | 样本数 | max roughDiff/env | median | 是否直接低于 0.020 |",
        "| ---: | ---: | ---: | ---: | :---: |",
    ]
    for group in summary["groups_by_M_exp"]:
        lines.append(
            f"| {group['M_exp']:.3f} | {group['count']} | {group['max_ratio']:.6f} | "
            f"{group['median_ratio']:.6f} | {'Y' if group['all_pass_budget_as_stress_test'] else 'N'} |"
        )
    lines += [
        "",
        "这给出一个有用定位：较长 `M=P^1.4` 层已经接近或低于预算，真正硬点集中在较短粗锚层，例如旧样本中的 `M=P^1.2`。",
        "",
        "## 2. 同权归一化的核心恒等式",
        "",
        "对",
        "",
        "\\[",
        "K_{h,\\ell}(m)=e\\left({hX\\over \\ell m}\\right)",
        "\\left(1-e\\left({hH\\over \\ell m}\\right)\\right)",
        "\\]",
        "",
        "在 `m~M` 且 `hH/(ell M)` 小的区间，有一阶振幅界",
        "",
        "\\[",
        "|K_{h,\\ell}(m)|\\le 2\\pi {hH\\over \\ell M}+O\\left(({hH\\over \\ell M})^2\\right).",
        "\\]",
        "",
        "代回 RRD 系数后，主因子发生精确降阶：",
        "",
        "\\[",
        "{|\\omega_\\ell|\\over h}\\cdot {hH\\over \\ell M}",
        "\\bigg/ {H\\over M}",
        "={|\\omega_\\ell|\\over \\ell}.",
        "\\]",
        "",
        "因此 RRD 天然落入与 QLOW 相同的 Selberg 变差范数",
        "",
        "\\[",
        "\\mathcal V_\\omega=\\sum_\\ell {|\\omega_\\ell|\\over \\ell}.",
        "\\]",
        "",
        "这一步是本轮真正的结构推进：`RRD` 不需要新归一化，只需证明粗数误差在上述同权测试范数中足够小。",
        "",
        "## 3. 必要两段式拆解",
        "",
        "令",
        "",
        "\\[",
        "a_m=1_{P^-(m)>Y}-\\rho_M.",
        "\\]",
        "",
        "不能直接要求 `a_m` 对所有临界核都小，因为小模周期和 Buchstab 低层会产生可见结构。应取一个低模投影 `\\Pi_{\\le Z}`，写成",
        "",
        "\\[",
        "a_m=\\Pi_{\\le Z}a_m+(1-\\Pi_{\\le Z})a_m.",
        "\\]",
        "",
        "于是",
        "",
        "\\[",
        "\\mathcal E_{\\rm RRD}=\\mathcal E_{\\rm low}+\\mathcal E_{\\rm perp}.",
        "\\]",
        "",
        "低模项不是随机误差，应进入 `OSPC/CRTDefect` 或单独预算；正交项才用 Buchstab+CRT 均衡+短窗不可复用证明小范数。",
        "",
        "## 4. 新的 RRD 子预算",
        "",
        "| 子项 | 预算 | 证明义务 |",
        "| --- | ---: | --- |",
    ]
    for target in audit["two_stage_targets"]:
        lines.append(
            f"| `{target['key']}` | {target['budget']:.3f} | {target['required_action']} |"
        )
    lines += [
        "",
        "三项合计仍为 `0.020`。因此 `RRD` 的下一步最小硬点已从“证明单密度替换很小”改为：",
        "",
        "\\[",
        "C_{\\rm RRD-low}+C_{\\rm RRD-perp}+C_{\\rm RRD-conv}\\le 0.020.",
        "\\]",
        "",
        "## 5. 审稿结论",
        "",
        audit["review_conclusion"],
        "",
        "下一步应先形式化 `\\Pi_{\\le Z}`：它必须是有限小模周期投影或 Buchstab 低层投影，并证明低模部分若超过 `0.006` 就自动触发 OSPC/CRTDefect；否则剩余正交项进入 `0.012` 的同权大筛/均衡估计。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan", type=Path, default=DEFAULT_SCAN)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    audit = build_reduction(load_json(args.scan), load_json(args.ledger))
    args.json_out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    args.md_out.write_text(render_markdown(audit) + "\n")
    print(args.json_out)
    print(args.md_out)


if __name__ == "__main__":
    main()
