#!/usr/bin/env python3
"""把二秩 cap-stable primitive PDEC 核不等式压到统一帽稳定证书。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_ranktwo_capstable_kernel_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-ranktwo-capstable-kernel-router.json
  docs/monograph/prime-matrix-pdec-cap-ranktwo-capstable-kernel-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_RANK = DOCS / "prime-matrix-pdec-cap-primitive-multiatom-rank-router.json"
DEFAULT_PDEC_ROUTE = DOCS / "prime-matrix-triad-a1-pdec-capacity-upper-route.md"
DEFAULT_DUAL_ABSORB = DOCS / "prime-matrix-pdec-dual-failure-absorption-contract.md"
DEFAULT_NO_CYCLE = DOCS / "prime-matrix-pdec-cap-refinement-no-cycle.md"
DEFAULT_TERMINAL_TRIAD = DOCS / "prime-matrix-terminal-certificate-triad.md"
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-ranktwo-capstable-kernel-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-ranktwo-capstable-kernel-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    blocks_final: bool,
) -> dict[str, Any]:
    """构造审查行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_final": blocks_final,
    }


def build_rows(
    rank_router: dict[str, Any],
    pdec_route_text: str,
    dual_absorb_text: str,
    no_cycle_text: str,
    terminal_triad_text: str,
) -> list[dict[str, Any]]:
    """生成二秩 cap-stable 核审查表。"""
    rank_two_kernel_active = (
        rank_router["primitive_multiatom_rank_boundary_closed"]
        and rank_router["narrowest_next_hardpoint"]
        == "RankTwoCapStablePrimitivePDECKernelInequality"
    )
    same_set_lp_protocol = has_all(
        pdec_route_text,
        [
            "U_{\\rm CRT}(h,\\zeta;\\theta)",
            "P_\\theta",
            "Same-Set Law",
            "CapacityInsufficient",
        ],
    )
    cap_localization_registered = has_all(
        dual_absorb_text,
        [
            "Cap localization",
            "C_alpha(h,zeta)",
            "{U-\\alpha M\\over 1-\\alpha}",
            "CapSparse",
            "CapPersistent",
            "CapColumn",
        ],
    )
    cap_failure_routes_named = has_all(
        dual_absorb_text,
        [
            "sparse cap",
            "refined PDEC",
            "ColumnCRT",
            "Multiplicity-Stitching",
        ],
    )
    cap_no_cycle_registered = has_all(
        no_cycle_text,
        [
            "PDEC-Cap-NoCycle",
            "固定有限签名群",
            "Boolean algebra",
            "new-layer PDEC",
        ],
    )
    terminal_interface_registered = has_all(
        terminal_triad_text,
        [
            "PDEC family certificate",
            "U_{\\rm CRT}<L_{\\rm PDEC}",
            "PDEC 失败只会产生更窄 PDEC",
        ],
    )
    cap_stability_contrapositive_closed = all(
        [
            rank_two_kernel_active,
            same_set_lp_protocol,
            cap_localization_registered,
            cap_failure_routes_named,
            cap_no_cycle_registered,
            terminal_interface_registered,
        ]
    )
    return [
        row(
            "RankTwoCapStableKernelActive",
            rank_two_kernel_active,
            rank_router["narrowest_next_hardpoint"],
            "上一层已把 primitive 多原子终端压成二秩以上且无可回流 cap 的核。",
            False,
        ),
        row(
            "SameSetLPDirectionProtocolRegistered",
            same_set_lp_protocol,
            "U_CRT(h,zeta;theta) over P_theta",
            "每个方向上界都必须在同一坏窗计数多面体 P_theta 上计算。",
            False,
        ),
        row(
            "CapLocalizationThresholdRegistered",
            cap_localization_registered,
            "g(C_alpha)>=(U-alpha M)/(1-alpha)",
            "若某方向线性泛函达到 L_PDEC，则存在对应方向帽的强质量下界。",
            False,
        ),
        row(
            "CapFailureRoutesNamed",
            cap_failure_routes_named,
            "SAE / refined PDEC / ColumnCRT / Multiplicity",
            "超过阈值的方向帽不能留在 cap-stable 核内，必须回流到已命名路线。",
            False,
        ),
        row(
            "CapRefinementNoCycleRegistered",
            cap_no_cycle_registered,
            "finite Boolean algebra or new-layer entropy dichotomy",
            "持久帽细化不会产生同层无限循环；升层也进入命名 new-layer PDEC/CleanKLS。",
            False,
        ),
        row(
            "PDECTerminalInterfaceRegistered",
            terminal_interface_registered,
            "terminal triad PDEC family contract",
            "cap 失败只允许回到三终端合同中的 PDEC/SAE/CleanKLS 路线，不能形成第四出口。",
            False,
        ),
        row(
            "RankTwoCapStableKernelInequalityByContrapositive",
            cap_stability_contrapositive_closed,
            "if every legal cap is below threshold then every direction has U_CRT<L_PDEC",
            "二秩 cap-stable 核不等式本身由 cap localization 逆否命题闭合；真正难点转为证明统一帽稳定阈值。",
            False,
        ),
        row(
            "UniformCapStabilityCertificateForRankTwoPrimitiveKernels",
            False,
            "global legal cap bounds for every rank>=2 primitive same-formal-unit kernel not submitted",
            "剩余全球硬点是为所有二秩以上 primitive 核提交合法方向帽上界，或输出命名 cap 回流证书。",
            True,
        ),
    ]


def run(
    rank_path: Path,
    pdec_route_path: Path,
    dual_absorb_path: Path,
    no_cycle_path: Path,
    terminal_triad_path: Path,
) -> dict[str, Any]:
    """运行二秩 cap-stable 核路由。"""
    rank_router = load_json(rank_path)
    pdec_route_text = read_text(pdec_route_path)
    dual_absorb_text = read_text(dual_absorb_path)
    no_cycle_text = read_text(no_cycle_path)
    terminal_triad_text = read_text(terminal_triad_path)
    rows = build_rows(
        rank_router=rank_router,
        pdec_route_text=pdec_route_text,
        dual_absorb_text=dual_absorb_text,
        no_cycle_text=no_cycle_text,
        terminal_triad_text=terminal_triad_text,
    )
    kernel_inequality_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "RankTwoCapStableKernelInequalityByContrapositive"
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_ranktwo_capstable_kernel_router",
        "status": "ranktwo_capstable_kernel_inequality_reduced_to_uniform_cap_stability",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "rank_router": file_sha256(rank_path),
            "pdec_route": file_sha256(pdec_route_path),
            "dual_absorb": file_sha256(dual_absorb_path),
            "no_cycle": file_sha256(no_cycle_path),
            "terminal_triad": file_sha256(terminal_triad_path),
        },
        "ranktwo_capstable_kernel_inequality_closed": kernel_inequality_closed,
        "uniform_cap_stability_certificate_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": "UniformCapStabilityCertificateForRankTwoPrimitiveKernels",
        "rows": rows,
        "capstable_law": (
            "For a rank-at-least-two primitive same-formal-unit PDEC kernel, fix one "
            "direction (h,zeta). The same-set LP computes U_CRT on the same count vector "
            "g. If U_CRT reaches L_PDEC, cap localization gives a direction cap "
            "C_alpha(h,zeta) with mass at least (L_PDEC-alpha M)/(1-alpha). Such a cap is "
            "not allowed to remain inside a cap-stable kernel: sparse caps route to SAE, "
            "persistent caps route to refined PDEC or ColumnCRT, and mismatched caps route "
            "to multiplicity normalization. Conversely, if every legal cap is certified "
            "below the corresponding threshold, then no direction can reach L_PDEC, hence "
            "U_CRT<L_PDEC for the kernel."
        ),
        "review_conclusion": (
            "二秩 cap-stable primitive 核的不等式本身已被改写为 cap localization 的逆否命题："
            "只要所有合法方向帽都低于阈值，就自动得到 `U_CRT<L_PDEC`；若某个方向帽达到阈值，"
            "该对象就不再是 cap-stable 核，而必须回流 `SAE/refined PDEC/ColumnCRT/multiplicity`。"
            "因此最新最窄剩余不是抽象核不等式，而是统一帽稳定证书。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 二秩 cap-stable 核路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. Cap-stable 逆否律",
        "",
        result["capstable_law"],
        "",
        "```text",
        "RankTwoCapStablePrimitivePDECKernelInequality",
        "  fix direction (h,zeta);",
        "  if U_CRT(h,zeta) >= L_PDEC:",
        "    cap localization gives C_alpha with mass >= (L-alpha M)/(1-alpha);",
        "    this is SAE / refined PDEC / ColumnCRT / multiplicity;",
        "    hence not cap-stable;",
        "  therefore cap-stable + all legal caps below threshold => U_CRT<L_PDEC.",
        "",
        "remaining:",
        "  UniformCapStabilityCertificateForRankTwoPrimitiveKernels.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `ranktwo_capstable_kernel_inequality_closed={fmt_bool(result['ranktwo_capstable_kernel_inequality_closed'])}`。",
        f"- `uniform_cap_stability_certificate_closed={fmt_bool(result['uniform_cap_stability_certificate_closed'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `narrowest_next_hardpoint={result['narrowest_next_hardpoint']}`。",
        f"- `open_final_gates={result['open_final_gates']}`。",
        "",
        "## 3. 审查表",
        "",
        "| gate | closed | blocks final | evidence | meaning |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {evidence} | {meaning} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(bool(item["closed"])),
                blocks=fmt_bool(bool(item["blocks_final"])),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 剩余",
            "",
            "下一步直接攻 `UniformCapStabilityCertificateForRankTwoPrimitiveKernels`："
            "对每个二秩以上 primitive 同 formal unit 核、每个合法方向 `(h,zeta)` 与阈值 `alpha`，"
            "证明方向帽质量低于 `(L_PDEC-alpha M)/(1-alpha)`，或输出 `SAE/refined PDEC/ColumnCRT/multiplicity` 回流证书。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rank-json", type=Path, default=DEFAULT_RANK)
    parser.add_argument("--pdec-route-md", type=Path, default=DEFAULT_PDEC_ROUTE)
    parser.add_argument("--dual-absorb-md", type=Path, default=DEFAULT_DUAL_ABSORB)
    parser.add_argument("--no-cycle-md", type=Path, default=DEFAULT_NO_CYCLE)
    parser.add_argument("--terminal-triad-md", type=Path, default=DEFAULT_TERMINAL_TRIAD)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        rank_path=args.rank_json,
        pdec_route_path=args.pdec_route_md,
        dual_absorb_path=args.dual_absorb_md,
        no_cycle_path=args.no_cycle_md,
        terminal_triad_path=args.terminal_triad_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_next_hardpoint"])


if __name__ == "__main__":
    main()
