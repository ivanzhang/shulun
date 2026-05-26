#!/usr/bin/env python3
"""归档 Phi-LPF 奇偶性障碍与真正所需素数分布公式的合同。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_parity_barrier_prime_distribution_contract_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json

输出：
  data/prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-ledger.json
  docs/monograph/prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json
  docs/monograph/prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.md

本证书的目标不是再证明一个有限相位恒等式，而是把本项目已经确认的
奇偶性障碍精确写成可审计合同：LPF/Phi 的精确分桶和截断误差都已经修正，
但它们仍是无符号粗数计数。真正突破必须产生点态素数分布下界、可求和
的 signed divisor/trace/Type-II family，或者把失败精确命名为 PDEC/SAE 回流。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LPF_BUCKET_JSON = DOCS / "prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json"
EXACT_ENDPOINT_JSON = DOCS / "prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json"
LEGENDRE_ERROR_JSON = DOCS / "prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json"
AFFINE_PARITY_JSON = DOCS / "prime-matrix-affine-2n-plus-1-euler-lpf-parity-audit.json"
VON_MANGOLDT_JSON = DOCS / "prime-matrix-phi-lpf-von-mangoldt-pure-power-compression-audit.json"
PRIME_POWER_TAIL_JSON = DOCS / "prime-matrix-phi-lpf-prime-power-tail-absorption-audit.json"
TRACE_CONTRACT_JSON = DOCS / "prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-router.json"
TRACE_KERNEL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift-router.json"
SHARED_HINGE_JSON = DOCS / "prime-matrix-phi-lpf-bridge-root-shared-pivot-hinge-contract-router.json"
EXTERNAL_SYNC_JSON = DOCS / "prime-matrix-external-live-frontier-applicability-sync-20260525.json"

SOURCE_FILES = [
    Path(__file__).resolve(),
    LPF_BUCKET_JSON,
    EXACT_ENDPOINT_JSON,
    LEGENDRE_ERROR_JSON,
    AFFINE_PARITY_JSON,
    VON_MANGOLDT_JSON,
    PRIME_POWER_TAIL_JSON,
    TRACE_CONTRACT_JSON,
    TRACE_KERNEL_JSON,
    SHARED_HINGE_JSON,
    EXTERNAL_SYNC_JSON,
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    DOCS / "external-theorem-index.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

LATEST_OPEN_GATE = (
    "ParityBarrierContractPinned "
    "AND NeedPointwiseThetaOrPsiRowLowerBoundBeyondPrimePowerTail "
    "AND NeedAdmissibleSignedDivisorTraceOrTypeIIFamily "
    "AND BridgeRootSharedPivotHingeLawOrPDEC "
    "AND TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC "
    "AND PrimitiveOrientationLocalFactorProductLawBeforePushforward "
    "AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def external_frontier_rows(external_sync: dict[str, Any]) -> list[dict[str, Any]]:
    """把外部前沿输入统一成奇偶性接口表。"""
    rows = [
        {
            "label": "Fouvry-Kowalski-Michel-Sawin trace functions",
            "url": "https://arxiv.org/abs/2511.09459",
            "what_it_could_supply": "bilinear trace-function cancellation after a genuine source-keyed trace family exists",
            "current_blocker": "terminal/hinge ledger is finite and not yet a uniform trace-function family",
            "directly_closes_now": False,
        }
    ]
    for row in external_sync.get("external_inputs", []):
        rows.append(
            {
                "label": row["label"],
                "url": row["url"],
                "what_it_could_supply": row["frontier_content"],
                "current_blocker": row["missing_currently"],
                "directly_closes_now": bool(row["can_close_current_pm_gate_directly"]),
            }
        )
    rows.append(
        {
            "label": "Pascadi weighted Type-II / smooth-number distribution",
            "url": "https://arxiv.org/abs/2505.00653",
            "what_it_could_supply": "well-factorable weighted averages after the row load is converted to AP-average form",
            "current_blocker": "current target is pointwise row/column positivity and source-keyed signed load",
            "directly_closes_now": False,
        }
    )
    return rows


def prime_distribution_contract_rows() -> list[dict[str, Any]]:
    """列出真正能越过奇偶障碍的分布公式类型。"""
    return [
        {
            "contract": "PointwiseThetaShortIntervalAtSqrtScale",
            "formula": "theta((kP,(k+1)P))>0 for every odd prime P and 1<k<P",
            "why_it_breaks_parity": "直接数素数，而不是数粗数 survivor",
            "current_status": "未证明；在硬区间内等价于逐行素数存在目标",
        },
        {
            "contract": "PsiBeyondPrimePowerTail",
            "formula": "psi((kP,(k+1)P)) > prime_power_tail((kP,(k+1)P))",
            "why_it_breaks_parity": "von Mangoldt 质量超过纯素幂尾巴时强制出现素数",
            "current_status": "尾巴等价已审计；点态 psi 下界仍未证明",
        },
        {
            "contract": "SignedMobiusVonMangoldtTypeITypeII",
            "formula": "uniform Type-I/II or Vaughan/Heath-Brown decomposition with source-key consistency",
            "why_it_breaks_parity": "有符号除子相消能区分素数与 P2/P3 粗合数",
            "current_status": "当前 PM payload 尚未构造 admissible family",
        },
        {
            "contract": "TraceKloostermanFamilyFromQSpineHinge",
            "formula": "completed source-keyed Kloosterman/trace sums with conductor and coefficient control",
            "why_it_breaks_parity": "谱/trace 相消能分离 LPF 支撑不可见的有符号相位",
            "current_status": "formal Jordan kernel 与 shared hinge 仍是有限账本；admissible family 未构造",
        },
        {
            "contract": "NamedPDECOrSAEReturn",
            "formula": "failure of a uniform law returns to a controlled PDEC/SAE/local-survivor contradiction",
            "why_it_breaks_parity": "把 parity-blind 失败变成结构不可能性，而不是继续计数",
            "current_status": "多个有限 PDEC 接口已命名；尚无全局回流闭合目标命题",
        },
    ]


def bypass_route_rows() -> list[dict[str, Any]]:
    """列出绕开传统筛法奇偶障碍的可行路线与硬口。"""
    return [
        {
            "route": "Spectral/Kuznetsov or trace-function route",
            "move": "把 terminal/q-spine 相位提升为 completed signed trace 或 Kloosterman family",
            "hard_atom": "source-key lift、Type-II 系数可分解性、conductor control",
        },
        {
            "route": "Harman/Vaughan signed-sieve route",
            "move": "在同一 row load 上用 Lambda/Mobius 加权分解替代 LPF 支撑计数",
            "hard_atom": "逐行点态下界，或零例外 AP/短区间定理",
        },
        {
            "route": "Shared-pivot PDEC route",
            "move": "证明 shared-pivot hinge 或 endpoint slack law 的失败会产生命名不可能 packet",
            "hard_atom": "uniform hinge law 或 controlled PDEC/SAE return",
        },
        {
            "route": "Finite-group/expander route",
            "move": "把 q-spine motion 编码成具有 expansion 与 anti-concentration 的真实 group orbit",
            "hard_atom": "构造 group action；当前 q-spine 只是有限 hinge ledger",
        },
        {
            "route": "Dynamical adjacent-run cancellation route",
            "move": "证明 terminal signed payload 的 uniform adjacent-run cancellation",
            "hard_atom": "same-trace-key consistency 与关于 P 的 uniform family",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装奇偶性障碍合同。"""
    lpf_bucket = load_json(LPF_BUCKET_JSON)
    exact_endpoint = load_json(EXACT_ENDPOINT_JSON)
    legendre = load_json(LEGENDRE_ERROR_JSON)
    affine = load_json(AFFINE_PARITY_JSON)
    von_mangoldt = load_json(VON_MANGOLDT_JSON)
    prime_power_tail = load_json(PRIME_POWER_TAIL_JSON)
    trace_contract = load_json(TRACE_CONTRACT_JSON)
    trace_kernel = load_json(TRACE_KERNEL_JSON)
    hinge = load_json(SHARED_HINGE_JSON)
    external_sync = load_json(EXTERNAL_SYNC_JSON)

    lpf_correction_closed = all(
        [
            lpf_bucket.get("exact_lpf_bucket_identity_closed") is True,
            exact_endpoint.get("exact_lpf_bucket_identity_closed") is True,
            exact_endpoint.get("continuous_euler_main_is_exact_count") is False,
            legendre.get("legendre_phi_periodic_truncation_error_closed") is True,
            legendre.get("half_main_truncation_error_claim_supported") is False,
        ]
    )
    parity_barrier_diagnosis_closed = all(
        [
            lpf_correction_closed,
            lpf_bucket.get("unsigned_lpf_bucket_count_sufficient_for_prime_extraction") is False,
            von_mangoldt.get("pure_power_selector_supplies_additive_signed_distribution_family") is False,
            prime_power_tail.get("pointwise_psi_row_lower_bound_beyond_tail_proved") is False,
            trace_contract.get("trace_or_typeii_family_admissible_now") is False,
            trace_kernel.get("trace_or_typeii_family_admissible_now") is False,
            hinge.get("bridge_root_shared_pivot_hinge_law_proved") is False,
        ]
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_parity_barrier_prime_distribution_contract_router",
        "status": "parity_barrier_contract_pinned_prime_distribution_formula_open",
        "verified_date": "2026-05-26",
        "parity_barrier_essence": (
            "无符号粗数信息即使在 LPF/Phi 层面完全精确，也不能把素数从两个或更多大素因子的乘积中分离出来。"
            "缺失的数据不是另一个 Euler-product 支撑计数，而是有符号除子/trace 相消，"
            "或逐点素数分布下界。"
        ),
        "lpf_bucket_exact_formula": lpf_bucket.get("exact_formula"),
        "lpf_correction_closed": lpf_correction_closed,
        "exact_endpoint_singleton_fixed": exact_endpoint.get("exact_endpoint_singleton_fixed") is True,
        "legendre_periodic_boundary_not_half_main": legendre.get(
            "legendre_phi_periodic_truncation_error_closed"
        )
        is True
        and legendre.get("half_main_truncation_error_claim_supported") is False,
        "affine_odd_axis_half_main_normalization_imported": affine.get(
            "apparent_half_main_gap_explained_by_missing_p2_all_samples"
        )
        is True
        and affine.get("euler_product_half_main_error_proved") is False,
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction": bool(
            lpf_bucket.get("unsigned_lpf_bucket_count_sufficient_for_prime_extraction")
        ),
        "von_mangoldt_pure_power_compression_closed": von_mangoldt.get(
            "lpf_pure_power_compression_closed"
        )
        is True,
        "pure_power_selector_supplies_additive_signed_distribution_family": bool(
            von_mangoldt.get("pure_power_selector_supplies_additive_signed_distribution_family")
        ),
        "psi_tail_absorption_equivalent_to_prime_presence_all_samples": prime_power_tail.get(
            "psi_tail_absorption_equivalent_to_prime_presence_all_samples"
        )
        is True,
        "pointwise_psi_row_lower_bound_beyond_tail_proved": bool(
            prime_power_tail.get("pointwise_psi_row_lower_bound_beyond_tail_proved")
        ),
        "trace_or_typeii_family_admissible_now": bool(
            trace_contract.get("trace_or_typeii_family_admissible_now")
        )
        or bool(trace_kernel.get("trace_or_typeii_family_admissible_now")),
        "shared_pivot_hinge_contract_closed": hinge.get(
            "bridge_root_qspine_pivot_to_shared_hinge_contract_closed"
        )
        is True,
        "bridge_root_shared_pivot_hinge_law_proved": bool(
            hinge.get("bridge_root_shared_pivot_hinge_law_proved")
        ),
        "parity_barrier_diagnosis_closed": parity_barrier_diagnosis_closed,
        "prime_distribution_contract_rows": prime_distribution_contract_rows(),
        "bypass_route_rows": bypass_route_rows(),
        "external_frontier_rows": external_frontier_rows(external_sync),
        "frontier_external_inputs_directly_close_now": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "next_primary_attack_target": "PsiBeyondPrimePowerTailOrAdmissibleSignedTraceTypeIIFamily",
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "奇偶性障碍已被固定为合同边界：LPF/Phi 精确性、周期截断控制、"
            "affine 奇轴归一化和 von Mangoldt 的点态 LPF 压缩都澄清了算术，"
            "但没有提供选择素数的有符号分布。真正突破必须证明超过素幂尾巴的"
            "点态 theta/psi 下界，构造 admissible signed trace/Type-II family，"
            "或给出命名 PDEC/SAE 回流。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix Phi-LPF parity barrier prime-distribution contract 路由",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 本质裁定",
        "",
        payload["parity_barrier_essence"],
        "",
        "```text",
        f"lpf_bucket_exact_formula={payload['lpf_bucket_exact_formula']}",
        f"lpf_correction_closed={fmt_bool(payload['lpf_correction_closed'])}",
        "legendre_periodic_boundary_not_half_main="
        f"{fmt_bool(payload['legendre_periodic_boundary_not_half_main'])}",
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction="
        f"{fmt_bool(payload['unsigned_lpf_bucket_count_sufficient_for_prime_extraction'])}",
        "pure_power_selector_supplies_additive_signed_distribution_family="
        f"{fmt_bool(payload['pure_power_selector_supplies_additive_signed_distribution_family'])}",
        "pointwise_psi_row_lower_bound_beyond_tail_proved="
        f"{fmt_bool(payload['pointwise_psi_row_lower_bound_beyond_tail_proved'])}",
        f"trace_or_typeii_family_admissible_now={fmt_bool(payload['trace_or_typeii_family_admissible_now'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 真正需要的素数分布合同",
        "",
        "| contract | formula | why it breaks parity | current status |",
        "| --- | --- | --- | --- |",
    ]
    for row in payload["prime_distribution_contract_rows"]:
        lines.append(
            f"| `{cell(row['contract'])}` | {cell(row['formula'])} | "
            f"{cell(row['why_it_breaks_parity'])} | {cell(row['current_status'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 可绕行路线",
            "",
            "| route | move | hard atom |",
            "| --- | --- | --- |",
        ]
    )
    for row in payload["bypass_route_rows"]:
        lines.append(f"| {cell(row['route'])} | {cell(row['move'])} | {cell(row['hard_atom'])} |")
    lines.extend(
        [
            "",
            "## 4. 外部前沿输入边界",
            "",
            "| input | url | directly closes now | blocker |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in payload["external_frontier_rows"]:
        lines.append(
            f"| {cell(row['label'])} | {cell(row['url'])} | "
            f"`{fmt_bool(row['directly_closes_now'])}` | {cell(row['current_blocker'])} |"
        )
    lines.extend(
        [
            "",
            "## 5. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.extend(["", "三命题仍未无条件闭合。", ""])
    return "\n".join(lines)


def write_outputs(payload: dict[str, Any]) -> None:
    """写出证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")


def main() -> None:
    """命令入口。"""
    payload = build_certificate()
    write_outputs(payload)
    print(f"parity_barrier_diagnosis_closed={fmt_bool(payload['parity_barrier_diagnosis_closed'])}")
    print(f"lpf_correction_closed={fmt_bool(payload['lpf_correction_closed'])}")
    print(f"next_primary_attack_target={payload['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
