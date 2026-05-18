#!/usr/bin/env python3
"""生成单个 moving LPF coordinate drift 的尺度逃逸证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_single_moving_lpf_coordinate_scale_escape_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.json",
]

PREVIOUS_TARGET = "SingleMovingLPFCoordinateDriftOrPrefixColumnCRTPDEC"
IMPORT = "SingleMovingLPFCoordinateDriftImportedLedger"
STABLE_PREFIX = "SingleMovingCoordinateStablePrefixLedger"
DYADIC_SCALE = "SingleMovingCoordinateDyadicScaleLedger"
BOUNDED_SCALE = "BoundedScaleDriftDegeneratesToFixedCoordinateLedger"
SCALE_ESCAPE = "UnboundedCoordinateScaleEscapeLedger"
POST_WIDTH = "PostMovingCoordinateSupportDescentLedger"
SAME_SCALE = "SameScaleCoordinateCycleExcludedLedger"
SPARSE = "SparseCoordinateDriftSAERegistrationLedger"
NO_ANON = "NoAnonymousSingleCoordinateDriftLedger"
NEW_TARGET = "ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC"

REDUCED_TARGET = (
    f"{IMPORT} AND {STABLE_PREFIX} AND {DYADIC_SCALE} AND {BOUNDED_SCALE} "
    f"AND {SCALE_ESCAPE} AND {POST_WIDTH} AND {SAME_SCALE} AND {SPARSE} "
    f"AND {NO_ANON} AND {NEW_TARGET}"
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
    """把旧活动基中的单坐标漂移替换为尺度逃逸分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造单坐标尺度逃逸判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "SingleMovingCoordinateDriftImported",
            imported,
            False,
            "上一层把首移动坐标池压成单个 mu 随 P 漂移，或 prefix ColumnCRT/PDEC。",
            PREVIOUS_TARGET,
        ),
        row(
            "StablePrefixForSingleCoordinateClosed",
            True,
            True,
            "单坐标漂移仍保留稳定前缀 A_prefix 和有效宽度 W_prefix；漂移只发生在 mu 坐标。",
            STABLE_PREFIX,
        ),
        row(
            "DyadicScaleCoordinateClosed",
            True,
            True,
            "对 mu 定义 dyadic scale B(mu)=2^floor(log_2 mu)，且 B<=mu<=2B。",
            DYADIC_SCALE,
        ),
        row(
            "BoundedScaleDegeneratesClosed",
            True,
            True,
            "若 B(mu) 在无限子族中有界，则 mu 只取有限个素值；无限复现必有固定 mu 子族，回到固定坐标 ColumnCRT/PDEC 或有限原子。",
            BOUNDED_SCALE,
        ),
        row(
            "UnboundedScaleEscapeClosed",
            True,
            True,
            "真正单坐标漂移必须沿 cofinal 子族满足 B(mu)->infty；否则已由有界尺度退化吸收。",
            SCALE_ESCAPE,
        ),
        row(
            "PostMovingCoordinateSupportDescentClosed",
            True,
            True,
            "加入 mu 后后继 residual 支撑宽度至多 ceil(W_prefix/mu)<=ceil(W_prefix/B)，因此在 B>=2 时严格小于 W_prefix。",
            POST_WIDTH,
        ),
        row(
            "SameScaleCoordinateCycleExcluded",
            True,
            True,
            "每个真实尺度逃逸都严格降低后继支撑，且有界尺度已回到固定坐标；同尺度漂移循环被排除。",
            SAME_SCALE,
        ),
        row(
            "SparseCoordinateDriftRegistered",
            True,
            False,
            "若漂移事件不形成持久同尺度压力，只能登记为稀疏 drift/SAE 质量；本步登记出口但不证明全局求和界。",
            SPARSE,
        ),
        row(
            "NoAnonymousSingleCoordinateDrift",
            True,
            True,
            "单坐标漂移被拆成固定坐标退化、尺度逃逸支撑递降、稀疏 SAE 或 ColumnCRT/PDEC；不再保留匿名 drift。",
            NO_ANON,
        ),
        row(
            "ScaleEscapingCoordinateStillOpen",
            False,
            False,
            "仍未排除尺度逃逸单坐标递降族，也未证明稀疏 drift SAE 全局可求和。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥尺度逃逸单坐标递降族，或证明其必回流为 ColumnCRT/PDEC/SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造单坐标尺度逃逸证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "单个 moving LPF coordinate drift 被拆成有界 dyadic 尺度退化和无界尺度逃逸。"
        "若尺度有界，则 mu 只取有限素值，持久复现回到固定坐标 ColumnCRT/PDEC 或有限原子。"
        "若真漂移，则 B(mu) 必无界；加入 mu 后后继支撑至多 ceil(W_prefix/B)，"
        "从而同尺度循环不可能。剩余是尺度逃逸递降族或稀疏 drift/SAE。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_single_moving_lpf_coordinate_scale_escape_router",
        "status": "single_moving_lpf_coordinate_drift_reduced_to_scale_escape_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "single_coordinate_drift_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "stable_prefix_closed": True,
        "dyadic_scale_closed": True,
        "bounded_scale_degenerates_closed": True,
        "unbounded_scale_escape_closed": True,
        "post_coordinate_support_descent_closed": True,
        "same_scale_cycle_excluded": True,
        "sparse_drift_registered": True,
        "anonymous_single_coordinate_drift_removed": True,
        "scale_escaping_coordinate_excluded": False,
        "sparse_drift_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "scale_escape_formulas": {
            "effective_width": "W_prefix=floor(W/A_prefix)",
            "dyadic_scale": "B(mu)=2^floor(log_2 mu), B<=mu<=2B",
            "bounded_scale_exit": "B bounded on infinite subfamily => finitely many mu => fixed coordinate ColumnCRT/PDEC or finite atom",
            "scale_escape": "true drift requires B(mu)->infty on a cofinal subfamily",
            "post_support": "W_after<=ceil(W_prefix/mu)<=ceil(W_prefix/B)",
            "strict_descent": "B>=2 => W_after<W_prefix unless already finite",
            "sparse_exit": "nonpersistent drift events route to sparse drift SAE/Rankin ledger",
            "new_failure": "scale-escaping single-coordinate descent or sparse drift SAE/ColumnCRT/PDEC",
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
        "# Prime Matrix single-moving LPF coordinate scale-escape 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"single_coordinate_drift_imported={fmt_bool(cert['single_coordinate_drift_imported'])}",
        f"stable_prefix_closed={fmt_bool(cert['stable_prefix_closed'])}",
        f"dyadic_scale_closed={fmt_bool(cert['dyadic_scale_closed'])}",
        f"bounded_scale_degenerates_closed={fmt_bool(cert['bounded_scale_degenerates_closed'])}",
        f"unbounded_scale_escape_closed={fmt_bool(cert['unbounded_scale_escape_closed'])}",
        f"post_coordinate_support_descent_closed={fmt_bool(cert['post_coordinate_support_descent_closed'])}",
        f"same_scale_cycle_excluded={fmt_bool(cert['same_scale_cycle_excluded'])}",
        f"sparse_drift_registered={fmt_bool(cert['sparse_drift_registered'])}",
        f"anonymous_single_coordinate_drift_removed={fmt_bool(cert['anonymous_single_coordinate_drift_removed'])}",
        f"scale_escaping_coordinate_excluded={fmt_bool(cert['scale_escaping_coordinate_excluded'])}",
        f"sparse_drift_sae_summability_proved={fmt_bool(cert['sparse_drift_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单坐标与 dyadic 尺度",
        "",
        "上一层剩余为单个 `mu` 随 `P` 漂移。稳定前缀仍给出：",
        "",
        "```text",
        "W_prefix=floor(W/A_prefix).",
        "```",
        "",
        "对 `mu` 定义 dyadic 尺度：",
        "",
        "```text",
        "B(mu)=2^floor(log_2 mu),",
        "B(mu)<=mu<=2B(mu).",
        "```",
        "",
        "## 2. 有界尺度退化",
        "",
        "若 `B(mu)` 在无限子族中有界，则 `mu` 只可能取有限多个素值。由无限鸽巢，存在固定 `mu` 的无限子族。该分支不是 moving drift，而是已登记的固定坐标 ColumnCRT/PDEC 或有限原子。",
        "",
        "因此真正的单坐标漂移必须满足：",
        "",
        "```text",
        "B(mu)->infty",
        "```",
        "",
        "沿一个 cofinal 子族成立。",
        "",
        "## 3. 后继支撑递降",
        "",
        "加入 `mu` 后，后继 residual 支撑宽度满足：",
        "",
        "```text",
        "W_after<=ceil(W_prefix/mu)<=ceil(W_prefix/B(mu)).",
        "```",
        "",
        "由于非有限活动层有 `B(mu)>=2`，若尚未进入有限原子，则 `W_after<W_prefix`。所以单坐标尺度逃逸不能在同一支撑尺度上循环。",
        "",
        "## 4. 稀疏 drift 出口",
        "",
        "若漂移事件不能形成持久同尺度压力，只能登记为 sparse drift/SAE 质量；本证书只登记该出口，不证明全局求和界。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        PREVIOUS_TARGET,
        "  -> " + IMPORT,
        "  AND " + STABLE_PREFIX,
        "  AND " + DYADIC_SCALE,
        "  AND " + BOUNDED_SCALE,
        "  AND " + SCALE_ESCAPE,
        "  AND " + POST_WIDTH,
        "  AND " + SAME_SCALE,
        "  AND " + SPARSE,
        "  AND " + NO_ANON,
        "  AND " + NEW_TARGET,
        "```",
        "",
        "剩余从单坐标漂移变成尺度逃逸单坐标递降族，或 sparse drift/SAE/ColumnCRT/PDEC。",
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
            "- 本证书没有证明尺度逃逸单坐标递降族不可能。",
            "- 本证书没有证明 sparse drift/SAE 全局可求和。",
            "- 本证书只排除有界尺度匿名漂移和同尺度循环。",
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
