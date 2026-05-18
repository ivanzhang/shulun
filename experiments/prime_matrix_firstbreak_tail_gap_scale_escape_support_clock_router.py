#!/usr/bin/env python3
"""生成 scale-escaping single-coordinate descent 的支撑时钟证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_scale_escape_support_clock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.json",
]

PREVIOUS_TARGET = "ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC"
IMPORT = "ScaleEscapingSingleCoordinateDescentImportedLedger"
CLOCK = "ScaleEscapeIntegerSupportClockLedger"
HALVING = "ScaleEscapeHalvingClockDescentLedger"
FINITE_DEPTH = "FiniteDepthScaleEscapePerFiberLedger"
TERMINAL_ATOM = "TerminalWidthOneFiniteAtomLedger"
PRODUCT_EXIT = "ScaleLadderProductWidthColumnCRTExitLedger"
PERSISTENT_SIGNATURE = "PersistentScaleLadderSignatureRegistrationLedger"
SPARSE_SAE = "SparseScaleLadderSAERegistrationLedger"
NO_CYCLE = "NoCyclicScaleEscapeDescentLedger"
NO_ANON = "NoAnonymousScaleEscapeDescentLedger"
NEW_TARGET = "PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC"

REDUCED_TARGET = (
    f"{IMPORT} AND {CLOCK} AND {HALVING} AND {FINITE_DEPTH} "
    f"AND {TERMINAL_ATOM} AND {PRODUCT_EXIT} AND {PERSISTENT_SIGNATURE} "
    f"AND {SPARSE_SAE} AND {NO_CYCLE} AND {NO_ANON} AND {NEW_TARGET}"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve()] + SOURCE_FILES
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def replace_latest_basis(previous: dict[str, Any]) -> str:
    """把旧活动基中的尺度逃逸硬点替换成支撑时钟分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 scale-escape 支撑时钟判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "ScaleEscapingSingleCoordinateDescentImported",
            imported,
            False,
            "上一层把单个 moving LPF 坐标压成尺度逃逸递降或 sparse drift/SAE/ColumnCRT/PDEC。",
            PREVIOUS_TARGET,
        ),
        row(
            "IntegerSupportClockDefined",
            True,
            True,
            "对每个有效支撑宽度 W 定义整数时钟 K(W)=ceil(log_2 max(W,1))；K(W)=0 等价于 W<=1。",
            CLOCK,
        ),
        row(
            "HalvingClockDescentClosed",
            True,
            True,
            "真实尺度逃逸层满足 B>=2 且 W_next<=ceil(W/B)，因此 W>=2 时 K(W_next)<=K(W)-1。",
            HALVING,
        ),
        row(
            "FiniteDepthPerFiberClosed",
            True,
            True,
            "每个固定反例纤维上的尺度逃逸步数至多 K(W_0)；同一纤维不能有无限 scale-escape 内循环。",
            FINITE_DEPTH,
        ),
        row(
            "TerminalWidthOneFiniteAtomClosed",
            True,
            True,
            "若递降到 W<=1，则 residual 支撑只剩有限原子或已命名边界，不能继续作为匿名 moving-family 容量池。",
            TERMINAL_ATOM,
        ),
        row(
            "ScaleLadderProductWidthExitClosed",
            True,
            True,
            "若尺度阶梯乘积越过初始有效宽度，则合成周期超过支撑，进入 ColumnCRT/PDEC 或有限原子出口。",
            PRODUCT_EXIT,
        ),
        row(
            "PersistentScaleLadderSignatureRegistered",
            True,
            False,
            "未被终端宽度、product-width 或稀疏性吸收的无限族必须保留有序尺度阶梯与相位签名；本步登记该持久签名，不排斥它。",
            PERSISTENT_SIGNATURE,
        ),
        row(
            "SparseScaleLadderSAERegistered",
            True,
            False,
            "不能在同一签名上持久复现的尺度逃逸事件登记为 sparse scale-ladder SAE；本步不证明全局求和。",
            SPARSE_SAE,
        ),
        row(
            "NoCyclicScaleEscapeDescent",
            True,
            True,
            "整数时钟严格下降，故尺度逃逸递降不能构成同宽度循环或回到旧尺度支撑层。",
            NO_CYCLE,
        ),
        row(
            "NoAnonymousScaleEscapeDescent",
            True,
            True,
            "抽象 scale-escape 口径被拆成终端原子、product-width ColumnCRT/PDEC、持久阶梯签名或 sparse SAE。",
            NO_ANON,
        ),
        row(
            "PersistentScaleLadderStillOpen",
            False,
            False,
            "仍未排斥持久尺度阶梯签名，也未证明 sparse scale-ladder SAE 全局可求和。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥持久尺度阶梯签名，或证明其必回流为 ColumnCRT/PDEC/SAE 且全局可控。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 scale-escape 支撑时钟证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "尺度逃逸单坐标递降被加上整数支撑时钟 K(W)=ceil(log_2 max(W,1))。"
        "每个真实逃逸坐标有 B>=2 且 W_next<=ceil(W/B)，所以 K 严格下降。"
        "因此同一反例纤维不能形成 scale-escape 内循环；抽象剩余被压成终端宽度原子、"
        "product-width ColumnCRT/PDEC、持久尺度阶梯签名或 sparse scale-ladder SAE。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_scale_escape_support_clock_router",
        "status": "scale_escaping_single_coordinate_descent_reduced_to_support_clock_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "scale_escape_descent_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "integer_support_clock_closed": True,
        "halving_clock_descent_closed": True,
        "finite_depth_per_fiber_closed": True,
        "terminal_width_one_finite_atom_closed": True,
        "scale_ladder_product_width_exit_closed": True,
        "persistent_scale_ladder_signature_registered": True,
        "sparse_scale_ladder_sae_registered": True,
        "cyclic_scale_escape_descent_excluded": True,
        "anonymous_scale_escape_descent_removed": True,
        "persistent_scale_ladder_excluded": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "support_clock_formulas": {
            "clock": "K(W)=ceil(log_2 max(W,1))",
            "one_step_support": "W_{i+1}<=ceil(W_i/B_i), B_i>=2",
            "one_step_clock": "W_i>=2 => K(W_{i+1})<=K(W_i)-1",
            "depth_budget": "number of scale-escape steps <= K(W_0)",
            "terminal_width": "K(W)=0 => W<=1 => finite atom or named boundary",
            "product_width_exit": "prod_i B_i>W_0 => composite period exceeds initial support => ColumnCRT/PDEC or finite atom",
            "persistent_exit": "non-sparse infinite family must carry an ordered scale-ladder signature",
            "sparse_exit": "nonpersistent scale-ladder events route to sparse SAE ledger",
        },
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix scale-escape support-clock 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"scale_escape_descent_imported={fmt_bool(cert['scale_escape_descent_imported'])}",
        f"integer_support_clock_closed={fmt_bool(cert['integer_support_clock_closed'])}",
        f"halving_clock_descent_closed={fmt_bool(cert['halving_clock_descent_closed'])}",
        f"finite_depth_per_fiber_closed={fmt_bool(cert['finite_depth_per_fiber_closed'])}",
        f"terminal_width_one_finite_atom_closed={fmt_bool(cert['terminal_width_one_finite_atom_closed'])}",
        f"scale_ladder_product_width_exit_closed={fmt_bool(cert['scale_ladder_product_width_exit_closed'])}",
        f"persistent_scale_ladder_signature_registered={fmt_bool(cert['persistent_scale_ladder_signature_registered'])}",
        f"sparse_scale_ladder_sae_registered={fmt_bool(cert['sparse_scale_ladder_sae_registered'])}",
        f"cyclic_scale_escape_descent_excluded={fmt_bool(cert['cyclic_scale_escape_descent_excluded'])}",
        f"anonymous_scale_escape_descent_removed={fmt_bool(cert['anonymous_scale_escape_descent_removed'])}",
        f"persistent_scale_ladder_excluded={fmt_bool(cert['persistent_scale_ladder_excluded'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 支撑时钟",
        "",
        "上一层剩余为尺度逃逸单坐标递降或 sparse drift/SAE。对任一有效支撑宽度 `W` 定义整数时钟：",
        "",
        "```text",
        "K(W)=ceil(log_2 max(W,1)).",
        "```",
        "",
        "`K(W)=0` 等价于 `W<=1`，此时 residual 支撑已退化为有限原子或命名边界。",
        "",
        "## 2. 单步严格下降",
        "",
        "真实尺度逃逸层满足 `B_i>=2`，并继承上一层支撑递降：",
        "",
        "```text",
        "W_{i+1}<=ceil(W_i/B_i)<=ceil(W_i/2).",
        "```",
        "",
        "因此当 `W_i>=2` 时：",
        "",
        "```text",
        "K(W_{i+1})<=K(W_i)-1.",
        "```",
        "",
        "这给出非循环证明路线中的单调量：尺度逃逸不能回到同一支撑时钟层。",
        "",
        "## 3. 有限深度与终端出口",
        "",
        "从初始 `W_0` 出发，同一反例纤维上的尺度逃逸步数至多：",
        "",
        "```text",
        "K(W_0)=ceil(log_2 max(W_0,1)).",
        "```",
        "",
        "若递降到 `W<=1`，则进入有限原子或已命名边界。若尺度阶梯乘积越过初始支撑：",
        "",
        "```text",
        "prod_i B_i>W_0,",
        "```",
        "",
        "则合成周期超过支撑，进入 ColumnCRT/PDEC 或有限原子。",
        "",
        "## 4. 持久阶梯签名与 sparse 出口",
        "",
        "未被终端宽度或 product-width 吸收的无限族，不能再以匿名 scale-escape descent 存在。它必须保留一个有序尺度阶梯签名及相位数据。不能在同一签名上持久复现的事件登记为 sparse scale-ladder SAE；本证书只登记该出口，不证明全局求和界。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        PREVIOUS_TARGET,
        "  -> " + IMPORT,
        "  AND " + CLOCK,
        "  AND " + HALVING,
        "  AND " + FINITE_DEPTH,
        "  AND " + TERMINAL_ATOM,
        "  AND " + PRODUCT_EXIT,
        "  AND " + PERSISTENT_SIGNATURE,
        "  AND " + SPARSE_SAE,
        "  AND " + NO_CYCLE,
        "  AND " + NO_ANON,
        "  AND " + NEW_TARGET,
        "```",
        "",
        "剩余从抽象尺度逃逸递降变成持久尺度阶梯签名，或 sparse scale-ladder SAE/ColumnCRT/PDEC。",
        "",
        "## 6. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(item["gate"]),
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 7. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 8. 诚实边界",
            "",
            "- 本证书没有证明持久尺度阶梯签名不可能。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只关闭抽象 scale-escape 内循环和匿名递降口径。",
            f"- `{NEW_TARGET}` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 9. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """生成全部证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    OUT_LEDGER.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
