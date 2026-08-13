"""生成基于预注册映射的 MFAC RH 主链依赖图。"""

import argparse
import json
from pathlib import Path
from typing import Mapping


DEFAULT_INVENTORY = Path(
    "docs/monograph/prime-matrix-mfac-project-inventory-audit.json"
)
DEFAULT_JSON = Path("docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.json")
DEFAULT_MARKDOWN = Path("docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.md")

def _role(node: str, relation: str, rationale: str) -> dict[str, str]:
    """构造人工预注册角色，避免从证书文本推断数学作用。"""
    return {"node": node, "relation": relation, "rationale": rationale}


MODULE_ROLE_REGISTRY = {
    "actual_lcm_gram_energy": (
        _role("W0", "forward_obligation", "实际 LCM Gram 能量仅提供 W0 的有限见证审计。"),
        _role("W1", "forward_obligation", "实际 Gram 能量关联去常数强制性义务。"),
    ),
    "actual_record_constructor": (
        _role("W0", "forward_obligation", "实际记录构造是 W0 的候选输入审计。"),
        _role("C1", "cycle_detected", "目标量回灌构造会形成 C1 循环。"),
    ),
    "centered_divisibility_covariance": (
        _role("W1", "forward_obligation", "中心化整除协方差属于 W1 的有限谱诊断。"),
        _role("C1", "cycle_detected", "以 Chebyshev 误差选取见证会形成 C1 循环。"),
    ),
    "colored_divisor_word_transport": (
        _role("no_direct_rh_role", "no_direct_rh_role", "运输结构未提供 W0--W5 正向全称边。"),
    ),
    "global_free_mellin_mode_no_go": (
        _role("C6", "insufficient_not_cycle", "自由乘法模型不足以建立实际 Mellin 收缩。"),
        _role("W3", "forward_obligation", "该反模型只约束 W3 所需的实际输入形式。"),
    ),
    "lcm_offconstant_projection_circularity": (
        _role("C1", "cycle_detected", "直接投影读取目标误差时形成 C1 循环。"),
        _role("W1", "forward_obligation", "去常数投影关联 W1，但未证明统一强制性。"),
    ),
    "mertens_conditional_l2_upper": (
        _role("W1", "conditional_dependency", "全 epsilon Mertens 界只条件化 W1 的尾和路线。"),
        _role("C7", "conditional_dependency", "Mertens 消去是 C7 的显式外部条件。"),
    ),
    "mertens_randomness_contraction": (
        _role("W3", "conditional_dependency", "随机性收缩仅以 Mertens 型假设条件化。"),
        _role("C7", "conditional_dependency", "Mertens 消去不可被标为 MFAC 自足来源。"),
    ),
    "mobius_tail_l2": (
        _role("W1", "forward_obligation", "Euler--phi 尾和恒等式是 W1 的有限层。"),
        _role("C7", "conditional_dependency", "整体 L2 上界仍依赖命名 Möbius 消去。"),
    ),
    "orientation_provenance_no_go": (
        _role("C1", "cycle_detected", "方向来源若读取目标信息会构成 C1 循环。"),
        _role("no_direct_rh_role", "no_direct_rh_role", "来源否定审计不提供 RH 正向边。"),
    ),
    "primitive_normalization_underdetermination": (
        _role("W0", "forward_obligation", "原始归一化欠定限制 W0 候选见证。"),
        _role("no_direct_rh_role", "no_direct_rh_role", "欠定结论不是 W0 闭合定理。"),
    ),
    "project_inventory": (
        _role("no_direct_rh_role", "no_direct_rh_role", "库存只提供模块状态索引。"),
    ),
    "registration_hash": (
        _role("no_direct_rh_role", "no_direct_rh_role", "注册哈希不提供 RH 主链解析边。"),
    ),
    "rough_cofactor_mobius_signed_transport": (
        _role("W0", "forward_obligation", "带符号运输关联实际见证候选。"),
        _role("no_direct_rh_role", "no_direct_rh_role", "局部运输没有 W0--W5 全称推论。"),
    ),
    "semiprime_local_naturality_factorization": (
        _role("W0", "conditional_dependency", "局部自然性只在显式局部模型条件下成立。"),
        _role("no_direct_rh_role", "no_direct_rh_role", "局部模型不闭合 RH 主链。"),
    ),
    "semiprime_triad_dispatch": (
        _role("W0", "forward_obligation", "实际 dispatch 仅重建 W0 候选资料。"),
        _role("no_direct_rh_role", "no_direct_rh_role", "重建不等于独立全称见证定理。"),
    ),
    "square_base_seed_binding": (
        _role("W0", "forward_obligation", "square-base seed 限制 W0 的实际系数来源。"),
        _role("no_direct_rh_role", "no_direct_rh_role", "绑定审计不提供后续主链边。"),
    ),
    "truncated_mobius_log_coercivity": (
        _role("W1", "forward_obligation", "固定截断族是 W1 的有限诊断。"),
        _role("C5", "insufficient_not_cycle", "有限剖面不足以证明统一 W1。"),
    ),
    "uniform_offconstant_coercivity": (
        _role("W1", "forward_obligation", "去常数候选扫描关联 W1。"),
        _role("C5", "insufficient_not_cycle", "有限扫描不是全称强制性定理。"),
    ),
}
OBLIGATION_NODES = ("W0", "W1", "W2", "W3", "W4", "W5")
MAIN_CHAIN = (
    ("W0", "W1"),
    ("W1", "W2"),
    ("W2", "W3"),
    ("W3", "W4"),
    ("W4", "W5"),
    ("W5", "RH"),
)
CYCLE_EDGES = {
    "C1": "Chebyshev_error → W0/W2",
    "C2": "Mellin_norm → W2",
    "C3": "zero_free_region/zeta_zero → W3/W4",
    "C4": "RH → W1--W5",
    "C5": "finite_profile → W1/W3/W4",
    "C6": "free_multiplicative_model → W3",
    "C7": "Mertens/PNT cancellation → W1 tail L2",
}


def _require_inventory_modules(inventory: Mapping[str, object]) -> list[Mapping[str, object]]:
    """验证库存模块列表，拒绝把错误输入伪装成完整图谱。"""
    modules = inventory.get("modules")
    if type(modules) is not list:
        raise ValueError("inventory.modules 必须是 list")
    if any(
        not isinstance(item, Mapping) or type(item.get("module_name")) is not str
        for item in modules
    ):
        raise ValueError("inventory.modules 必须只含带 module_name 的 Mapping")
    return modules


def _node_status(
    module_roles: list[dict[str, object]], node: str
) -> tuple[str, tuple[str, ...]]:
    """从人工关系和库存分类保守计算节点状态，绝不产生 proved。"""
    attached = [
        role
        for module in module_roles
        for role in module["roles"]
        if role["node"] == node
    ]
    if not attached:
        return "not_started", ("no_registered_support_module",)
    if any(role["relation"] == "conditional_dependency" for role in attached):
        return "conditional", ("conditional_dependency_present",)
    if any(role["relation"] == "cycle_detected" for role in attached):
        return "cycle_detected", ("cycle_detected_role_present",)
    return "unproved", ("finite_or_open_support_only",)


def _first_blocking_edge(nodes: Mapping[str, Mapping[str, object]]) -> list[str]:
    """优先报告 W1 到无支持 W2 的首个实质主链断点。"""
    if nodes["W2"]["status"] == "not_started":
        return ["W1", "W2"]
    for source, target in MAIN_CHAIN:
        if target == "RH":
            return [source, target]
        if nodes[source]["status"] != "proved" or nodes[target]["status"] != "proved":
            return [source, target]
    return []


def build_main_chain_graph(inventory: Mapping[str, object]) -> dict[str, object]:
    """组合库存状态与人工角色，且永远不认证 RH。"""
    modules = _require_inventory_modules(inventory)
    inventory_names = {item["module_name"] for item in modules}
    registry_names = set(MODULE_ROLE_REGISTRY)
    unmapped = sorted(inventory_names - registry_names)
    stale = sorted(registry_names - inventory_names)
    if unmapped or stale:
        raise ValueError(f"角色登记与库存不一致：unmapped={unmapped}; stale={stale}")
    module_roles = [
        {
            "module_name": item["module_name"],
            "inventory_classification": item.get("classification"),
            "inventory_rh_blockers": tuple(item.get("rh_blockers", ())),
            "roles": MODULE_ROLE_REGISTRY[item["module_name"]],
        }
        for item in sorted(modules, key=lambda item: item["module_name"])
    ]
    nodes = {
        node: {
            "status": _node_status(module_roles, node)[0],
            "blockers": _node_status(module_roles, node)[1],
            "support_modules": tuple(
                module["module_name"]
                for module in module_roles
                if any(role["node"] == node for role in module["roles"])
            ),
        }
        for node in OBLIGATION_NODES
    }
    main_chain_edges = [
        {
            "source": source,
            "target": target,
            "status": "unproved",
            "forbidden_inputs": (
                "RH",
                "zeta_zero",
                "zero_free_region",
                "Mellin",
            ),
        }
        for source, target in MAIN_CHAIN
    ]
    return {
        "certificate_type": "prime_matrix_mfac_rh_main_chain_graph_audit",
        "module_count": len(module_roles),
        "module_roles": module_roles,
        "unmapped_modules": [],
        "stale_registry_modules": [],
        "nodes": nodes,
        "main_chain_edges": main_chain_edges,
        "cycle_edges": CYCLE_EDGES,
        "shortest_blocking_path": _first_blocking_edge(nodes),
        "rh_chain_closed": False,
        "rh_proved": False,
    }


def render_markdown(certificate: Mapping[str, object]) -> str:
    """把保守 RH 主链图谱渲染为可审阅 Markdown。"""
    lines = [
        "# MFAC RH 主链依赖图审计",
        "",
        f"- 模块总数：`{certificate['module_count']}`",
        f"- 最短阻断路径：`{' → '.join(certificate['shortest_blocking_path'])}`",
        "- `rh_chain_closed=false`",
        "- `rh_proved=false`",
        "",
        "## 义务节点",
        "",
        "| 节点 | 状态 | 支持模块 | 阻断理由 |",
        "| --- | --- | --- | --- |",
    ]
    for node, data in certificate["nodes"].items():
        lines.append(
            f"| `{node}` | `{data['status']}` | "
            f"`{', '.join(data['support_modules']) or 'none'}` | "
            f"`{', '.join(data['blockers'])}` |"
        )
    lines.extend(
        [
            "",
            "## 主链边",
            "",
            "| 边 | 状态 | 禁止输入 |",
            "| --- | --- | --- |",
        ]
    )
    for edge in certificate["main_chain_edges"]:
        lines.append(
            f"| `{edge['source']} → {edge['target']}` | `{edge['status']}` | "
            f"`{', '.join(edge['forbidden_inputs'])}` |"
        )
    lines.extend(["", "## 循环与不足边", ""])
    for name, description in certificate["cycle_edges"].items():
        lines.append(f"- `{name}`：{description}")
    lines.extend(
        [
            "",
            "## 模块角色",
            "",
            "| 模块 | 库存分类 | 预注册角色 |",
            "| --- | --- | --- |",
        ]
    )
    for module in certificate["module_roles"]:
        roles = ", ".join(
            f"{role['node']}:{role['relation']}" for role in module["roles"]
        )
        lines.append(
            f"| `{module['module_name']}` | `{module['inventory_classification']}` | "
            f"`{roles}` |"
        )
    lines.extend(
        [
            "",
            "本图只组合阶段 1 库存与人工预注册角色，不运行模块；不构成 RH 证明。",
            "",
        ]
    )
    return "\n".join(lines)


def write_certificate(
    certificate: Mapping[str, object], json_path: Path, markdown_path: Path
) -> None:
    """写出机器可读和人工可读的保守主链图谱。"""
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(render_markdown(certificate), encoding="utf-8")


def main() -> None:
    """从阶段 1 库存生成严格覆盖的 RH 主链依赖图。"""
    parser = argparse.ArgumentParser(description="生成 MFAC RH 主链依赖图")
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-out", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()
    inventory = json.loads(args.inventory.read_text(encoding="utf-8"))
    graph = build_main_chain_graph(inventory)
    graph["inventory_path"] = str(args.inventory)
    write_certificate(graph, args.json_out, args.markdown_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.markdown_out}")


if __name__ == "__main__":
    main()
