#!/usr/bin/env python3
"""RSE 主链 RRD/OSPC 余量账本。

用法示例：
  python3 experiments/rse_rrd_ospc_margin_ledger.py
"""
from __future__ import annotations

import argparse
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 50

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_SUPNORM = MONOGRAPH / "qlow-mid-comp-supnorm-audit.json"
DEFAULT_JSON = MONOGRAPH / "rse-rrd-ospc-margin-ledger.json"
DEFAULT_MD = MONOGRAPH / "rse-rrd-ospc-margin-ledger.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取已有审计 JSON。"""
    if not path.exists():
        raise FileNotFoundError(f"缺少输入文件: {path}")
    return json.loads(path.read_text())


def decimal_from_json(value: Any) -> Decimal:
    """用字符串构造 Decimal，避免二进制浮点再引入新误差。"""
    return Decimal(str(value))


def to_jsonable(value: Any) -> Any:
    """把 Decimal 递归转成字符串，保证 JSON 稳定可审查。"""
    if isinstance(value, Decimal):
        return format(value, "f")
    if isinstance(value, dict):
        return {key: to_jsonable(val) for key, val in value.items()}
    if isinstance(value, list):
        return [to_jsonable(item) for item in value]
    return value


def build_ledger(supnorm: dict[str, Any]) -> dict[str, Any]:
    """从 QLOW sup-rho 证书抽取可分配余量，并建立主链证明义务账本。"""
    hardest = supnorm["hardest_case"]
    target = decimal_from_json(hardest["target"])
    comp_bound = decimal_from_json(hardest["sup_bound"])
    computed_margin = target - comp_bound
    reported_margin = decimal_from_json(supnorm["min_slack"])
    margin = min(computed_margin, reported_margin)

    # 这些数不是证明结论，而是后续 RRD/OSPC 必须落入的同口径目标。
    budgets = [
        {
            "key": "RRD",
            "name": "粗数替换误差",
            "budget": Decimal("0.020"),
            "required_bound": "C_RRD <= 0.020",
            "proof_obligation": "把 E_rough-discrep 的绝对值归一化到 QLOW 的 K V_omega 尺度，并证明同权 convention 下的损失不超过 0.020。",
        },
        {
            "key": "OSPC",
            "name": "有向小素集中出口",
            "budget": Decimal("0.020"),
            "required_bound": "C_OSPC <= 0.020",
            "proof_obligation": "证明 OSPC 必触发 CRTDefect/Tail-anchor 出口，且 Fourier 到缺陷的常数损失不超过 0.020。",
        },
        {
            "key": "SelbergUniform",
            "name": "P>=P0 统一 Selberg 矩常数",
            "budget": Decimal("0.008"),
            "required_bound": "C_SelbergUniform <= 0.008",
            "proof_obligation": "把样本网格的 Selberg 有理审计升级为 P>=P0 的矩阵扰动/谱隙统一界。",
        },
        {
            "key": "LedgerRounding",
            "name": "账本换算与外向舍入",
            "budget": Decimal("0.003"),
            "required_bound": "C_round <= 0.003",
            "proof_obligation": "统一 H/Q、Selberg 变差、RSE 核和 RRD/OSPC 之间的归一化换算误差。",
        },
    ]
    allocated = sum(item["budget"] for item in budgets)
    reserve = margin - allocated

    return {
        "certificate_type": "rse_rrd_ospc_margin_ledger",
        "status": "positive_margin_proof_obligation_ledger" if reserve > 0 else "overallocated_ledger",
        "source": str(DEFAULT_SUPNORM.relative_to(ROOT)),
        "normalization": "所有 C_* 必须先换算到 QLOW-MID-COMP 的 target=0.35 归一化损失尺度；否则本账本不能使用。",
        "hardest_case": {
            "P": hardest["P"],
            "R_exp": hardest["R_exp"],
            "R": hardest["R"],
            "target": target,
            "comp_bound": comp_bound,
            "computed_margin": computed_margin,
            "available_margin": margin,
            "reported_min_slack": reported_margin,
            "margin_consistency_error": computed_margin - reported_margin,
        },
        "budgets": budgets,
        "allocated_budget": allocated,
        "reserve": reserve,
        "closure_criterion": "C_RRD + C_OSPC + C_SelbergUniform + C_round < available_margin",
        "current_review_conclusion": (
            "QLOW-MID-COMP 的样本网格已有正余量；RRD/OSPC 尚未由本账本证明。"
            "下一步必须逐项证明 budget 表中的 required_bound。"
        ),
        "next_hard_points": [
            "RRD：粗数替换误差的同权归一化上界。",
            "OSPC：有向小素集中到 CRTDefect/Tail-anchor 的定量推出。",
            "SelbergUniform：样本 Selberg 矩常数到 P>=P0 的统一化。",
        ],
    }


def render_markdown(ledger: dict[str, Any]) -> str:
    """渲染可读审稿账本。"""
    hardest = ledger["hardest_case"]
    lines = [
        "# RSE 主链 RRD/OSPC 余量账本",
        "",
        f"**状态：** `{ledger['status']}`",
        "",
        "本账本只做一件事：把 `QLOW-MID-COMP` 的 `sup-rho` 正余量转换成 `RRD/OSPC` 后续证明必须满足的同口径常数目标。它不是 `RRD/OSPC` 的证明。",
        "",
        "## 归一化约定",
        "",
        ledger["normalization"],
        "",
        "若某个误差项只在未归一化的 `H sum 1/m`、Fourier 能量或 Selberg 变差尺度下给出，必须先证明到 `K V_omega` / `target=0.35` 的换算因子，才能放入本表。",
        "",
        "## 可用余量",
        "",
        "| 来源 | P | R | target | comp_bound | available_margin |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
        f"| `{ledger['source']}` | {hardest['P']} | {hardest['R']} | {Decimal(hardest['target']):.6f} | {Decimal(hardest['comp_bound']):.6f} | {Decimal(hardest['available_margin']):.6f} |",
        "",
        "其中 `available_margin = 0.35 - supBound`。当前最紧样本给出约 `0.0533695` 的后续可分配余量。",
        "",
        "## 证明义务预算",
        "",
        "| 接口 | 预算 | 必须证明的同口径界 | 具体义务 |",
        "| --- | ---: | --- | --- |",
    ]
    for item in ledger["budgets"]:
        lines.append(
            f"| `{item['key']}` {item['name']} | {Decimal(item['budget']):.3f} | `{item['required_bound']}` | {item['proof_obligation']} |"
        )
    lines += [
        "",
        f"- 已分配预算：`{Decimal(ledger['allocated_budget']):.6f}`。",
        f"- 保留余量：`{Decimal(ledger['reserve']):.6f}`。",
        "",
        "因此当前可审查判据为",
        "",
        "\\[",
        f"C_{{\\rm RRD}}+C_{{\\rm OSPC}}+C_{{\\rm SelbergUniform}}+C_{{\\rm round}}<{hardest['available_margin']}.",
        "\\]",
        "",
        "按上表目标值，只要四项分别落入 `0.020+0.020+0.008+0.003=0.051`，仍有约 `0.0023695` 余量。",
        "",
        "## RRD 需要证明的形式",
        "",
        "原始接口为",
        "",
        "\\[",
        "|\\mathcal E_{\\mathrm{rough-discrep}}|",
        "\\le",
        "\\eta_{\\mathrm{rough}} H\\sum_{m\\sim M,\\ P^-(m)>Y}\\frac1m.",
        "\\]",
        "",
        "下一步不能只估计 `eta_rough`，还必须给出从右侧到 `C_RRD` 的同权换算，目标是 `C_RRD<=0.020`。",
        "",
        "## OSPC 需要证明的形式",
        "",
        "原始接口为",
        "",
        "\\[",
        "(r-1)\\sum_a |C_a(q,r)|^2",
        "\\ge",
        "(1+\\delta_{\\mathrm{dir}})",
        "\\frac{(\\sum_a |C_a(q,r)|)^2}{r-1}.",
        "\\]",
        "",
        "下一步必须把该有向能量异常定量推出为 `CRTDefect/Tail-anchor` 可吸收出口，并证明出口损失在 `C_OSPC<=0.020` 内。",
        "",
        "## 审稿结论",
        "",
        ledger["current_review_conclusion"],
        "",
        "当前主链最小剩余项已经从笼统的 `RRD/OSPC` 改写为四个可逐项检查的常数不等式。下一步最优硬攻是先做 `RRD` 的同权归一化，因为它是标量误差；随后处理 `OSPC` 的有向 Fourier 到 CRTDefect 的定量出口。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supnorm", type=Path, default=DEFAULT_SUPNORM)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    ledger = build_ledger(load_json(args.supnorm))
    args.json_out.write_text(json.dumps(to_jsonable(ledger), ensure_ascii=False, indent=2) + "\n")
    args.md_out.write_text(render_markdown(to_jsonable(ledger)) + "\n")
    print(args.json_out)
    print(args.md_out)


if __name__ == "__main__":
    main()
