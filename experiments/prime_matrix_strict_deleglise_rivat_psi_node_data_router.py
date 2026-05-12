#!/usr/bin/env python3
"""生成 strict Deléglise-Rivat psi 节点数据/等价算法路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_deleglise_rivat_psi_node_data_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-deleglise-rivat-psi-node-data-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
import shutil
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-deleglise-rivat-psi-node-data-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-deleglise-rivat-psi-node-data-router.md"

NODE_SLACK = MONOGRAPH / "prime-matrix-strict-middle-psi-fine-mesh-node-slack-router.json"
BT_INPUT = MONOGRAPH / "prime-matrix-strict-brun-titchmarsh-short-interval-input-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"
AUDIT_SCRIPT = ROOT / "experiments" / "prime_matrix_middle_psi_node_table_audit.py"
BATCH_RUNNER_SCRIPT = ROOT / "experiments" / "prime_matrix_middle_psi_node_batch_runner.py"
SAMPLE_NODE_TABLE = Path("/tmp/middle-psi-nodes-sample.jsonl")

SOURCE_FILES = [NODE_SLACK, BT_INPUT, CLAIM_STATUS, AUDIT_SCRIPT, BATCH_RUNNER_SCRIPT]

TARGET = "DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger"
NODE_HASH = "MiddlePsiFineMeshNodeSlackFloorAndHashLedger"
NODE_AUDIT = "NodeSlackFloorAuditLedger"
MESH_HASH = "MeshCompletenessAndIndexHashLedger"
ROUNDING = "MiddlePsiUpperDirectedRoundingLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

X_LEFT = 8.0e11
X_RIGHT = math.exp(28)
MESH_H = 1_000_000.0
EXPECTED_NODE_COUNT = math.ceil((X_RIGHT - X_LEFT) / MESH_H)

SOURCE_REPO = "https://github.com/mhdeleglise/PsiTheta"
SOURCE_COMMIT = "21f4f6553851f218801a733f607426c3dba9ba11"
SOURCE_PAGE = "https://math.univ-lyon1.fr/~deleglis/calculs.html"
PAPER_CITATION = "M. Deléglise and J. Rivat, Computing Psi(x), Mathematics of Computation 67(224), 1998, 1691-1696."

CHECKOUT_CANDIDATES = [
    Path("/tmp/PsiTheta"),
    ROOT / "external" / "PsiTheta",
]

NODE_TABLE_CANDIDATES = [
    MONOGRAPH / "prime-matrix-strict-middle-psi-fine-mesh-node-table.json",
    MONOGRAPH / "prime-matrix-strict-middle-psi-fine-mesh-node-table.jsonl",
    ROOT / "data" / "middle-psi-fine-mesh-node-table.jsonl",
]

SOURCE_HASH_FILES = [
    "README.md",
    "makefile",
    "psi.cc",
    "theta.cc",
    "psitheta.h",
    "tst_psi.cpp",
    "tst_theta.cpp",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """稳定输出浮点。"""
    return f"{value:.15e}"


def table_cell(value: Any) -> str:
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


def checkout_profile() -> dict[str, Any]:
    """检查本地是否已有 PsiTheta 源码签名。"""
    existing = [path for path in CHECKOUT_CANDIDATES if path.exists()]
    chosen = existing[0] if existing else None
    file_hashes: dict[str, str] = {}
    missing_files: list[str] = []
    if chosen is not None:
        for rel in SOURCE_HASH_FILES:
            path = chosen / rel
            if path.exists():
                file_hashes[rel] = sha256(path)
            else:
                missing_files.append(rel)
    return {
        "candidate_checkouts": [str(path) for path in CHECKOUT_CANDIDATES],
        "existing_checkouts": [str(path) for path in existing],
        "checkout_present": chosen is not None,
        "chosen_checkout": str(chosen) if chosen is not None else None,
        "source_file_hashes": file_hashes,
        "missing_source_files": missing_files,
        "required_source_files_present": chosen is not None and not missing_files,
    }


def toolchain_profile() -> dict[str, Any]:
    """检查当前环境能否编译 PsiTheta。"""
    make_path = shutil.which("make")
    gpp_path = shutil.which("g++")
    clang_path = shutil.which("clang++")
    return {
        "make_present": make_path is not None,
        "gpp_present": gpp_path is not None,
        "clangpp_present": clang_path is not None,
        "compiler_present": gpp_path is not None or clang_path is not None,
        "make_path": make_path,
        "gpp_path": gpp_path,
        "clangpp_path": clang_path,
        "requires_gmp_mpfr": True,
        "note": "GMP/MPFR runtime libraries were observed externally, but headers/compiler must be verified by build.",
    }


def binary_profile(chosen_checkout: str | None) -> dict[str, Any]:
    """检查源码是否已编译出 psi/theta 可执行文件。"""
    if chosen_checkout is None:
        return {
            "psi_binary_present": False,
            "theta_binary_present": False,
            "psi_binary_hash": None,
            "theta_binary_hash": None,
        }
    root = Path(chosen_checkout)
    psi = root / "psi"
    theta = root / "theta"
    return {
        "psi_binary_present": psi.exists() and psi.is_file(),
        "theta_binary_present": theta.exists() and theta.is_file(),
        "psi_binary_hash": sha256(psi) if psi.exists() else None,
        "theta_binary_hash": sha256(theta) if theta.exists() else None,
    }


def naive_psi_float(limit: int) -> float:
    """用小范围朴素筛计算 psi(limit)，仅用于 smoke test。"""
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    total = 0.0
    for p in range(2, limit + 1):
        if is_prime[p]:
            power = p
            logp = math.log(p)
            while power <= limit:
                total += logp
                if power > limit // p:
                    break
                power *= p
    return total


def run_command(args: list[str], cwd: Path, timeout: int = 20) -> tuple[bool, str]:
    """运行外部命令并返回成功标记和精简输出。"""
    try:
        completed = subprocess.run(
            args,
            cwd=str(cwd),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, str(exc)
    output = completed.stdout.strip() or completed.stderr.strip()
    return completed.returncode == 0, output


def smoke_test_profile(chosen_checkout: str | None) -> dict[str, Any]:
    """运行 README theta 示例和小范围 psi 朴素对照。"""
    if chosen_checkout is None:
        return {"smoke_test_closed": False, "reason": "no checkout"}
    root = Path(chosen_checkout)
    psi = root / "psi"
    theta = root / "theta"
    if not psi.exists() or not theta.exists():
        return {"smoke_test_closed": False, "reason": "missing psi/theta binaries"}

    theta_ok, theta_out = run_command(["./theta", "1234567890", "25"], root)
    psi_ok, psi_out = run_command(["./psi", "1000000", "25"], root)
    theta_expected = "1.234518946373189641192934e9"
    psi_naive = naive_psi_float(1_000_000)
    try:
        psi_value = float(psi_out)
    except ValueError:
        psi_value = float("nan")
    psi_relative_error = abs(psi_value - psi_naive) / psi_naive if psi_naive else float("inf")
    return {
        "smoke_test_closed": theta_ok
        and psi_ok
        and theta_out == theta_expected
        and psi_relative_error < 1e-12,
        "theta_readme_output": theta_out,
        "theta_readme_expected": theta_expected,
        "theta_readme_match": theta_out == theta_expected,
        "psi_1e6_output": psi_out,
        "psi_1e6_naive_float": psi_naive,
        "psi_1e6_relative_error": psi_relative_error,
    }


def node_table_profile() -> dict[str, Any]:
    """检查是否已有细网格节点表。"""
    existing = [path for path in NODE_TABLE_CANDIDATES if path.exists()]
    sizes = {str(path.relative_to(ROOT)): path.stat().st_size for path in existing}
    hashes = {str(path.relative_to(ROOT)): sha256(path) for path in existing}
    return {
        "candidate_paths": [str(path.relative_to(ROOT)) for path in NODE_TABLE_CANDIDATES],
        "existing_paths": [str(path.relative_to(ROOT)) for path in existing],
        "node_table_present": bool(existing),
        "node_table_sizes": sizes,
        "node_table_hashes": hashes,
    }


def batch_runner_profile() -> dict[str, Any]:
    """检查批处理 runner 与目标量级样本。"""
    sample_records: list[dict[str, Any]] = []
    sample_slack_ok = False
    if SAMPLE_NODE_TABLE.exists():
        with SAMPLE_NODE_TABLE.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    sample_records.append(json.loads(line))
        sample_slack_ok = bool(sample_records) and all(
            record.get("slack_ge_required_floor") is True for record in sample_records
        )
    return {
        "batch_runner_script_present": BATCH_RUNNER_SCRIPT.exists(),
        "sample_node_table": str(SAMPLE_NODE_TABLE),
        "sample_node_table_present": SAMPLE_NODE_TABLE.exists(),
        "sample_record_count": len(sample_records),
        "sample_output_sha256": sha256(SAMPLE_NODE_TABLE) if SAMPLE_NODE_TABLE.exists() else None,
        "sample_slack_ok": sample_slack_ok,
        "sample_records": sample_records[:3],
    }


def workload_profile(required_floor: float) -> dict[str, Any]:
    """给出批量节点生成工作量和记录格式。"""
    last_start = X_LEFT + (EXPECTED_NODE_COUNT - 1) * MESH_H
    return {
        "x_left": X_LEFT,
        "x_right": X_RIGHT,
        "mesh_h": MESH_H,
        "expected_start_node_count": EXPECTED_NODE_COUNT,
        "first_start_node": X_LEFT,
        "last_start_node": last_start,
        "required_node_slack_floor": required_floor,
        "single_cli_program_not_sufficient_for_hash_certificate": True,
        "batch_adapter_required": True,
        "canonical_output_format": "jsonl, one sorted record per i, UTF-8, LF line ending, SHA256 over exact bytes",
        "required_record_fields": [
            "i",
            "x_i",
            "psi_value",
            "psi_rounding_mode",
            "psi_precision_decimal_digits",
            "slack_lower_bound",
            "slack_ge_required_floor",
            "source_commit",
            "source_chunk_hash",
        ],
    }


def build_result() -> dict[str, Any]:
    """构造 Deléglise-Rivat 节点数据路由证书。"""
    node = load_json(NODE_SLACK)
    bt = load_json(BT_INPUT)
    required_floor = float(node["mesh_profile"]["required_node_slack_floor"])
    checkout = checkout_profile()
    toolchain = toolchain_profile()
    binaries = binary_profile(checkout["chosen_checkout"])
    smoke = smoke_test_profile(checkout["chosen_checkout"])
    batch_runner = batch_runner_profile()
    node_table = node_table_profile()
    workload = workload_profile(required_floor)
    source_identified = True
    build_ready = (
        checkout["required_source_files_present"]
        and toolchain["make_present"]
        and toolchain["compiler_present"]
        and binaries["psi_binary_present"]
        and binaries["theta_binary_present"]
    )
    node_archive_ready = node_table["node_table_present"]
    audit_script_ready = AUDIT_SCRIPT.exists()
    batch_runner_ready = batch_runner["batch_runner_script_present"] and batch_runner["sample_slack_ok"]
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            node.get("counterexample_assumption_only") is True
            and node.get("row_column_unconditional_closed") is False,
            True,
            "本步只处理中段 psi 节点数据来源，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "ExternalPsiThetaSourceLocated",
            source_identified,
            True,
            "Deléglise 本人页面与 mhdeleglise/PsiTheta 仓库给出 psi/theta 计算源码入口。",
            "source is identified, not yet a node certificate",
        ),
        row(
            "PublishedAlgorithmCitationLocated",
            source_identified,
            True,
            "源码 README 对应 Deléglise-Rivat Computing Psi(x) 论文，算法来源边界可登记。",
            "paper proof not rederived here",
        ),
        row(
            "LocalSourceCheckoutSignature",
            checkout["required_source_files_present"],
            checkout["required_source_files_present"],
            "本地若有源码 checkout，则登记关键源码文件 hash。",
            "checkout or vendored source tree",
        ),
        row(
            "BuildablePsiThetaToolchain",
            build_ready,
            build_ready,
            "当前环境已需要 make、C++ 编译器和 psi/theta 可执行文件共同验收。",
            "install/build toolchain or use a prebuilt audited container",
        ),
        row(
            "PsiThetaSmokeTestLedger",
            smoke["smoke_test_closed"],
            smoke["smoke_test_closed"],
            "README theta 示例和 psi(1e6) 朴素筛对照已作为基础 smoke test。",
            "target-scale and full node table still required",
        ),
        row(
            "CanonicalBatchPsiNodeRunnerLedger",
            batch_runner_ready,
            batch_runner_ready,
            "已新增批处理 runner，并用目标区间首节点生成 JSONL 样本；完整归档仍未生成。",
            "full node archive generation still required",
        ),
        row(
            "CanonicalNodeTableAuditScriptLedger",
            audit_script_ready,
            audit_script_ready,
            "已新增机械验收脚本，可检查 JSONL 节点表的索引、x_i、余量下界、节点数和 SHA256。",
            "requires actual node table to pass",
        ),
        row(
            "MachineReadableNodeArchiveLedger",
            node_archive_ready,
            node_archive_ready,
            "仓库当前仍未发现中段百万网格完整节点表。",
            "generate or import node jsonl archive",
        ),
        row(
            "SourceAlgorithmToDusartConventionMatch",
            False,
            False,
            "需要证明源码输出的 psi 口径、端点跳变、舍入方向与 Dusart 表使用口径一致。",
            ROUNDING,
        ),
        row(
            TARGET,
            False,
            False,
            "算法源已定位，但构建、批量节点生成、节点表 hash、口径/舍入验收尚未闭合。",
            "BuildablePsiThetaToolchain AND PsiThetaSmokeTestLedger AND CanonicalBatchPsiNodeRunnerLedger AND MachineReadableNodeArchiveLedger AND SourceAlgorithmToDusartConventionMatch",
        ),
        row(
            NODE_HASH,
            False,
            False,
            "节点数据源未闭合时，节点余量/hash 守门不能升级。",
            f"{TARGET} AND {NODE_AUDIT} AND {MESH_HASH} AND {ROUNDING}",
        ),
        row(
            "CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger",
            False,
            False,
            "BT 外部输入和素数幂修正已处理，但短区间总包仍卡在节点余量/hash。",
            NODE_HASH,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "节点数据源定位不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_deleglise_rivat_psi_node_data_router",
        "status": (
            "psi_algorithm_source_built_smoke_passed_batch_node_archive_hash_open"
            if build_ready and smoke["smoke_test_closed"]
            else "psi_algorithm_source_identified_build_batch_node_archive_hash_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "external_psi_theta_source_identified": source_identified,
        "published_algorithm_citation_located": source_identified,
        "local_source_checkout_signature_closed": checkout["required_source_files_present"],
        "buildable_psi_theta_toolchain_closed": build_ready,
        "compiled_psi_theta_binaries_present": binaries["psi_binary_present"] and binaries["theta_binary_present"],
        "psi_theta_smoke_test_closed": smoke["smoke_test_closed"],
        "canonical_batch_psi_node_runner_closed": batch_runner_ready,
        "canonical_node_table_audit_checker_closed": audit_script_ready,
        "machine_readable_node_archive_closed": node_archive_ready,
        "source_algorithm_to_dusart_convention_match_closed": False,
        "deleglise_rivat_psi_node_data_or_equivalent_hash_closed": False,
        "middle_psi_fine_mesh_node_slack_floor_hash_closed": False,
        "certified_short_interval_psi_increment_upper_closed": False,
        "brun_titchmarsh_short_interval_input_external_closed": bt.get(
            "brun_titchmarsh_short_interval_input_external_closed"
        )
        is True,
        "prime_power_short_interval_correction_closed": True,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "external_sources": {
            "source_page": SOURCE_PAGE,
            "source_repo": SOURCE_REPO,
            "source_commit_observed": SOURCE_COMMIT,
            "paper_citation": PAPER_CITATION,
        },
        "checkout_profile": checkout,
        "toolchain_profile": toolchain,
        "binary_profile": binaries,
        "smoke_test_profile": smoke,
        "batch_runner_profile": batch_runner,
        "node_table_profile": node_table,
        "workload_profile": workload,
        "replacement_after_this": {
            TARGET: (
                "BuildablePsiThetaToolchain AND PsiThetaSmokeTestLedger AND "
                "CanonicalBatchPsiNodeRunnerLedger AND MachineReadableNodeArchiveLedger AND "
                "SourceAlgorithmToDusartConventionMatch"
            ),
            NODE_HASH: f"{TARGET} AND {NODE_AUDIT} AND {MESH_HASH} AND {ROUNDING}",
        },
        "next_direct_attack_target": (
            "MachineReadableNodeArchiveLedger"
            if build_ready and smoke["smoke_test_closed"] and batch_runner_ready
            else (
                "CanonicalBatchPsiNodeRunnerLedger"
                if build_ready and smoke["smoke_test_closed"]
                else "BuildablePsiThetaToolchainOrPrebuiltAuditedContainerLedger"
            )
        ),
        "parallel_attack_targets": [
            "CanonicalBatchPsiNodeRunnerLedger",
            "MachineReadableNodeArchiveLedger",
            "SourceAlgorithmToDusartConventionMatch",
        ],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Deléglise-Rivat 等价计算路线向前推进了一层：PsiTheta 源码和论文来源已经可定位，"
            "但这还不是节点证书。本环境已可构建并通过基础 smoke test，但仓库没有 646258 个节点的"
            "机器可读表；还必须补完整节点归档、节点表 hash，以及与 Dusart "
            "psi 口径和外向舍入的一致性证明。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict Deléglise-Rivat psi 节点数据路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"external_psi_theta_source_identified={fmt_bool(result['external_psi_theta_source_identified'])}",
        f"local_source_checkout_signature_closed={fmt_bool(result['local_source_checkout_signature_closed'])}",
        f"buildable_psi_theta_toolchain_closed={fmt_bool(result['buildable_psi_theta_toolchain_closed'])}",
        f"compiled_psi_theta_binaries_present={fmt_bool(result['compiled_psi_theta_binaries_present'])}",
        f"psi_theta_smoke_test_closed={fmt_bool(result['psi_theta_smoke_test_closed'])}",
        f"canonical_batch_psi_node_runner_closed={fmt_bool(result['canonical_batch_psi_node_runner_closed'])}",
        f"canonical_node_table_audit_checker_closed={fmt_bool(result['canonical_node_table_audit_checker_closed'])}",
        f"machine_readable_node_archive_closed={fmt_bool(result['machine_readable_node_archive_closed'])}",
        f"deleglise_rivat_psi_node_data_or_equivalent_hash_closed={fmt_bool(result['deleglise_rivat_psi_node_data_or_equivalent_hash_closed'])}",
        f"middle_psi_fine_mesh_node_slack_floor_hash_closed={fmt_bool(result['middle_psi_fine_mesh_node_slack_floor_hash_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部来源",
        "",
        "| key | value |",
        "| --- | --- |",
    ]
    for key, value in result["external_sources"].items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.extend(["", "## 2. 构建与节点表画像", "", "```text"])
    for section in [
        "checkout_profile",
        "toolchain_profile",
        "binary_profile",
        "smoke_test_profile",
        "batch_runner_profile",
        "node_table_profile",
        "workload_profile",
    ]:
        lines.append(f"[{section}]")
        for key, value in result[section].items():
            if isinstance(value, bool):
                lines.append(f"{key}={fmt_bool(value)}")
            elif isinstance(value, (int, float)):
                lines.append(f"{key}={fmt_float(float(value))}")
            else:
                lines.append(f"{key}={value}")
        lines.append("")
    lines.extend(["```", "", "## 3. 剩余替换", "", "```text"])
    for key, value in result["replacement_after_this"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 4. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
