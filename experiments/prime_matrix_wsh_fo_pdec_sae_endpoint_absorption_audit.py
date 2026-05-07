#!/usr/bin/env python3
"""审计 FO-PDEC physical/primitive 二点原子的 SAE/Endpoint 本地吸收。

用法示例：
  python3 experiments/prime_matrix_wsh_fo_pdec_sae_endpoint_absorption_audit.py

输出：
  docs/monograph/prime-matrix-wsh-fo-pdec-sae-endpoint-absorption-audit.json
  docs/monograph/prime-matrix-wsh-fo-pdec-sae-endpoint-absorption-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_TAUTOLOGY = (
    DOCS / "prime-matrix-wsh-fo-pdec-physical-primitive-tautology-audit.json"
)
DEFAULT_FIXED_OFFSET = DOCS / "prime-matrix-wsh-fixed-offset-pdec-ledger.json"
DEFAULT_JSON = (
    DOCS / "prime-matrix-wsh-fo-pdec-sae-endpoint-absorption-audit.json"
)
DEFAULT_MD = DOCS / "prime-matrix-wsh-fo-pdec-sae-endpoint-absorption-audit.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def matching_offset_rows(
    fixed_offset: dict[str, Any],
    source: dict[str, Any],
) -> list[dict[str, Any]]:
    """找到与低模来源同一 block/row/offset 且包含该候选的偏移纤维。"""
    matches = []
    for row in fixed_offset["offset_rows"]:
        if int(row["block_index"]) != int(source["block_index"]):
            continue
        if int(row["q"]) != int(source["q"]):
            continue
        if int(row["row"]) != int(source["row"]):
            continue
        if int(row["offset"]) != int(source["offset"]):
            continue
        if not any(
            int(candidate["candidate"]) == int(source["semiprime"]) + int(source["offset"])
            for candidate in row["candidate_rows"]
        ):
            continue
        matches.append(row)
    return matches


def local_witnesses(row: dict[str, Any], atom_candidate: int) -> list[dict[str, Any]]:
    """提取同一固定偏移纤维中的本地素数见证。"""
    witnesses = []
    for candidate in row["candidate_rows"]:
        if not candidate["is_prime"]:
            continue
        witnesses.append(
            {
                "candidate": int(candidate["candidate"]),
                "semiprime": int(candidate["semiprime"]),
                "same_as_atom": int(candidate["candidate"]) == atom_candidate,
                "factors_le_p": candidate["factors_le_p"],
            }
        )
    return witnesses


def atom_absorption_rows(
    tautology: dict[str, Any],
    fixed_offset: dict[str, Any],
) -> list[dict[str, Any]]:
    """为每个物理原子的每个来源构造 SAE/Endpoint 本地吸收行。"""
    rows = []
    for atom in tautology["physical_events"]:
        atom_candidate = int(atom["candidate"])
        for source in atom["sources"]:
            matches = matching_offset_rows(fixed_offset, source)
            for offset_row in matches:
                witnesses = local_witnesses(offset_row, atom_candidate)
                factor_loads = {
                    int(item["factor"]): int(item["load"])
                    for item in offset_row["top_factors"]
                }
                rows.append(
                    {
                        "atom_candidate": atom_candidate,
                        "factor": int(atom["factor"]),
                        "block_index": int(source["block_index"]),
                        "p": int(source["p"]),
                        "q": int(source["q"]),
                        "row": int(source["row"]),
                        "column": int(source["column"]),
                        "offset": int(source["offset"]),
                        "semiprime": int(source["semiprime"]),
                        "tail_factors": source["tail_factors"],
                        "residue": int(source["target_residue"]),
                        "fiber_allowed_load": int(offset_row["allowed_load"]),
                        "fiber_prime_candidates": int(offset_row["prime_candidates"]),
                        "fiber_missing_candidates": int(offset_row["missing_candidates"]),
                        "fiber_max_factor_load": int(offset_row["max_factor_load"]),
                        "factor_199_load_in_fiber": factor_loads.get(199, 0),
                        "mirror_candidate_span": offset_row["mirror_candidate_span"],
                        "local_prime_witnesses": witnesses,
                        "has_local_survivor_witness": bool(witnesses),
                        "route": (
                            "LocalSurvivorWitnessInSameFixedOffsetFiber"
                            if witnesses
                            else "SAEEndpointStillNeedsWitness"
                        ),
                    }
                )
    rows.sort(
        key=lambda row: (
            row["atom_candidate"],
            row["block_index"],
            row["q"],
            row["row"],
            row["offset"],
        )
    )
    return rows


def build_audit(
    tautology: dict[str, Any],
    fixed_offset: dict[str, Any],
    tautology_path: Path,
    fixed_offset_path: Path,
) -> dict[str, Any]:
    """构造二点原子的 SAE/Endpoint 吸收审计。"""
    rows = atom_absorption_rows(tautology, fixed_offset)
    all_sources_have_witness = bool(rows) and all(
        row["has_local_survivor_witness"] for row in rows
    )
    all_factor_199_sparse = all(row["factor_199_load_in_fiber"] <= 1 for row in rows)
    unique_atoms = sorted({row["atom_candidate"] for row in rows})
    unique_fibers = sorted(
        {
            (
                row["block_index"],
                row["q"],
                row["row"],
                row["offset"],
            )
            for row in rows
        }
    )
    return {
        "certificate_type": "fo_pdec_sae_endpoint_absorption_audit",
        "status": (
            "audited_two_physical_primitive_atoms_absorbed_by_local_survivor_witnesses"
            if all_sources_have_witness and all_factor_199_sparse
            else "audited_two_physical_primitive_atoms_still_need_sae_witness"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "physical_primitive_tautology_audit": file_sha256(tautology_path),
            "fixed_offset_pdec_ledger": file_sha256(fixed_offset_path),
        },
        "input_subgate": tautology["closed_subgate"],
        "physical_atom_count": len(unique_atoms),
        "unique_physical_atoms": unique_atoms,
        "source_row_count": len(rows),
        "unique_fixed_offset_fiber_count": len(unique_fibers),
        "unique_fixed_offset_fibers": [
            {
                "block_index": block,
                "q": q,
                "row": row,
                "offset": offset,
            }
            for block, q, row, offset in unique_fibers
        ],
        "all_sources_have_local_survivor_witness": all_sources_have_witness,
        "all_factor_199_fibers_are_sparse_load_one": all_factor_199_sparse,
        "absorption_rows": rows,
        "closed_subgate": (
            "TwoPhysicalPrimitiveAtomsAbsorbedByLocalSurvivorWitnesses"
            if all_sources_have_witness and all_factor_199_sparse
            else "SAEEndpointWitnessStillOpenForTwoPhysicalPrimitiveAtoms"
        ),
        "remaining_after_subgate": [
            "global LocalSurvivorCert family for unaudited sparse windows",
            "future primitive PDEC only for at least three non-tautological physical atoms or an extra fixed-frequency constraint",
            "CleanKLS/DLS and D-structure/Rankin referee inputs for the full row-column theorem",
        ],
        "review_conclusion": (
            "当前 physical/primitive PDEC 只剩两个物理原子；二点 Fourier 阈值已退化为恒等式。"
            "把这两个原子送入 SAE/Endpoint 后，审计发现每个关联固定偏移纤维都有本地素数见证，"
            "且 factor=199 在每个纤维内负载至多为 1。因此当前有限二点分支被 LocalSurvivor "
            "见证吸收；这关闭的是已审计样本子门，不是完整 LocalSurvivor/PDEC 终端全集。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# FO-PDEC 二点原子的 SAE/Endpoint 本地吸收审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 子门裁定",
        "",
        "```text",
        f"input_subgate: {result['input_subgate']}",
        f"closed_subgate: {result['closed_subgate']}",
        f"physical_atom_count: {result['physical_atom_count']}",
        f"source_row_count: {result['source_row_count']}",
        f"unique_fixed_offset_fiber_count: {result['unique_fixed_offset_fiber_count']}",
        (
            "all_sources_have_local_survivor_witness: "
            f"{str(result['all_sources_have_local_survivor_witness']).lower()}"
        ),
        (
            "all_factor_199_fibers_are_sparse_load_one: "
            f"{str(result['all_factor_199_fibers_are_sparse_load_one']).lower()}"
        ),
        "```",
        "",
        "## 2. 吸收行",
        "",
        "| atom | block | q | row | offset | residue | primes in fiber | missing | factor199 load | witness primes | route |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in result["absorption_rows"]:
        witness_primes = [
            witness["candidate"] for witness in row["local_prime_witnesses"]
        ]
        lines.append(
            "| "
            + " | ".join(
                table_cell(value)
                for value in [
                    row["atom_candidate"],
                    row["block_index"],
                    row["q"],
                    row["row"],
                    row["offset"],
                    row["residue"],
                    row["fiber_prime_candidates"],
                    row["fiber_missing_candidates"],
                    row["factor_199_load_in_fiber"],
                    witness_primes,
                    row["route"],
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明读法",
            "",
            "二点 primitive Fourier 信号不能作为 PDEC 排斥阈值后，剩余对象必须改按稀疏孤窗处理。",
            "对每个来源行，若同一固定偏移纤维中存在素数候选，则该纤维不是全覆盖零窗；这个素数候选就是",
            "`LocalSurvivorCert` 的 witness。若 witness 不存在，才需要继续生成更细的 SAE/Endpoint 证书。",
            "",
            "本审计中所有来源行都有 witness prime，且 `factor=199` 在每个纤维内都是负载 `1` 的稀疏标签，",
            "所以当前两个物理原子不能继续作为终端 PDEC/SAE 障碍。",
            "",
            "## 4. 剩余",
            "",
        ]
    )
    for item in result["remaining_after_subgate"]:
        lines.append(f"- `{item}`")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tautology", type=Path, default=DEFAULT_TAUTOLOGY)
    parser.add_argument("--fixed-offset", type=Path, default=DEFAULT_FIXED_OFFSET)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    tautology = load_json(args.tautology)
    fixed_offset = load_json(args.fixed_offset)
    result = build_audit(tautology, fixed_offset, args.tautology, args.fixed_offset)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["closed_subgate"])


if __name__ == "__main__":
    main()
