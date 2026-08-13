# MFAC 全项目 RH 主链依赖图实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development（推荐）或 superpowers:executing-plans 逐任务执行。本计划用 checkbox（`- [ ]`）跟踪步骤。

**Goal:** 将阶段 1 的 19 个 MFAC 库存模块按预注册人工多角色映射到 W0--W5、C1--C7 和旁路标签，生成严格覆盖、不可认证 RH 的主链依赖图。

**Architecture:** 审计器只解析阶段 1 库存 JSON 的 `modules`，并用模块名集合与内部 `MODULE_ROLE_REGISTRY` 做双向严格校验。图谱使用固定主链 `W0→W1→W2→W3→W4→W5→RH` 和固定循环表；库存分类只能阻断或条件化节点，不能把任何节点升级为 `proved`。

**Tech Stack:** Python 3 标准库（`argparse`、`json`、`pathlib`、`typing`、`unittest`、`tempfile`、`subprocess`）；阶段 1 库存 JSON 和现有 `docs/monograph/` 证书模式。

**Design Source:** `docs/superpowers/specs/2026-08-13-mfac-rh-main-chain-graph-design.md`

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_rh_main_chain_graph_audit.py`
  - 库存读取、全量预注册角色、集合覆盖校验、节点/边状态、渲染与 CLI。
- Create: `experiments/prime_matrix_mfac_rh_main_chain_graph_audit_test.py`
  - 合成库存的严格覆盖、角色多重性、RH 边界和 CLI 测试。
- Create: `docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.json`
  - 当前 19 模块的机器可读 RH 主链图谱。
- Create: `docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.md`
  - 节点、主链边、循环边、逐模块角色与最短阻断路径表。

不修改阶段 1 扫描器、既有 MFAC 审计器或其证书；不读取模块源码/Markdown 来分配角色；完成后只提交本规格、本计划、新图谱模块、测试和两种图谱证书，不混入用户已有未提交文件。

### Task 1: 写出库存覆盖与多角色红灯测试

**Files:**
- Create: `experiments/prime_matrix_mfac_rh_main_chain_graph_audit_test.py`

- [ ] **Step 1: 写出严格映射与多角色保留测试**

```python
import unittest

from experiments.prime_matrix_mfac_rh_main_chain_graph_audit import build_main_chain_graph


class MFACRHMainChainGraphAuditTest(unittest.TestCase):
    """验证 MFAC RH 主链图谱的严格覆盖和保守边界。"""

    def test_registry_covers_inventory_and_preserves_multiple_roles(self) -> None:
        """每个库存模块必须预注册，且一个模块可以保留多个角色。"""
        inventory = {
            "modules": [
                {
                    "module_name": "actual_lcm_gram_energy",
                    "classification": "open_or_unresolved",
                    "rh_blockers": ["rh_not_proved_or_open_marker"],
                },
                {
                    "module_name": "mertens_conditional_l2_upper",
                    "classification": "conditional_or_external_dependency",
                    "rh_blockers": ["conditional_or_external_marker"],
                },
            ]
        }

        graph = build_main_chain_graph(inventory)

        by_name = {item["module_name"]: item for item in graph["module_roles"]}
        self.assertEqual(graph["unmapped_modules"], [])
        self.assertEqual(graph["stale_registry_modules"], [])
        self.assertEqual(len(by_name["actual_lcm_gram_energy"]["roles"]), 2)
        self.assertEqual(
            {role["node"] for role in by_name["mertens_conditional_l2_upper"]["roles"]},
            {"W1", "C7"},
        )
        self.assertFalse(graph["rh_proved"])
```

- [ ] **Step 2: 运行测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_rh_main_chain_graph_audit_test.MFACRHMainChainGraphAuditTest.test_registry_covers_inventory_and_preserves_multiple_roles -v`

Expected: FAIL，原因是图谱模块尚不存在。

### Task 2: 实现预注册角色与严格集合校验

**Files:**
- Create: `experiments/prime_matrix_mfac_rh_main_chain_graph_audit.py`
- Modify: `experiments/prime_matrix_mfac_rh_main_chain_graph_audit_test.py`

- [ ] **Step 1: 定义角色构造器和完整预注册表**

```python
from typing import Mapping


def _role(node: str, relation: str, rationale: str) -> dict[str, str]:
    """构造一个人工预注册角色，避免从证书文本推断数学作用。"""
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
```

- [ ] **Step 2: 实现双向严格覆盖和初始图谱**

```python

def _require_inventory_modules(inventory: Mapping[str, object]) -> list[Mapping[str, object]]:
    """验证库存模块列表，拒绝把错误输入伪装成完整图谱。"""
    modules = inventory.get("modules")
    if type(modules) is not list:
        raise ValueError("inventory.modules 必须是 list")
    if any(not isinstance(item, Mapping) or type(item.get("module_name")) is not str for item in modules):
        raise ValueError("inventory.modules 必须只含带 module_name 的 Mapping")
    return modules


def build_main_chain_graph(inventory: Mapping[str, object]) -> dict[str, object]:
    """组合库存状态与人工角色，且永远不认证 RH。"""
    modules = _require_inventory_modules(inventory)
    inventory_names = {item["module_name"] for item in modules}
    registry_names = set(MODULE_ROLE_REGISTRY)
    unmapped = sorted(inventory_names - registry_names)
    stale = sorted(registry_names - inventory_names)
    if unmapped or stale:
        raise ValueError(
            f"角色登记与库存不一致：unmapped={unmapped}; stale={stale}"
        )
    module_roles = [
        {
            "module_name": item["module_name"],
            "inventory_classification": item.get("classification"),
            "inventory_rh_blockers": tuple(item.get("rh_blockers", ())),
            "roles": MODULE_ROLE_REGISTRY[item["module_name"]],
        }
        for item in sorted(modules, key=lambda item: item["module_name"])
    ]
    return {
        "certificate_type": "prime_matrix_mfac_rh_main_chain_graph_audit",
        "module_count": len(module_roles),
        "module_roles": module_roles,
        "unmapped_modules": [],
        "stale_registry_modules": [],
        "rh_chain_closed": False,
        "rh_proved": False,
    }
```

- [ ] **Step 3: 运行 Task 1 测试确认通过**

Run: `python3 -m unittest experiments.prime_matrix_mfac_rh_main_chain_graph_audit_test -v`

Expected: PASS。

### Task 3: 写出严格覆盖和主链阻断红灯测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_rh_main_chain_graph_audit_test.py`

- [ ] **Step 1: 添加未知模块阻断、条件不升级和 W2 阻断路径测试**

```python
    def test_unknown_module_blocks_and_conditional_w1_never_closes_chain(self) -> None:
        """未映射模块必须阻断；条件 W1 不能跳过 W2 或关闭 RH 链。"""
        with self.assertRaisesRegex(ValueError, "unmapped"):
            build_main_chain_graph(
                {"modules": [{"module_name": "unknown", "classification": "open_or_unresolved"}]}
            )

        inventory = {
            "modules": [
                {"module_name": name, "classification": "open_or_unresolved", "rh_blockers": []}
                for name in MODULE_ROLE_REGISTRY
            ]
        }
        inventory["modules"] = [
            {
                **item,
                "classification": "conditional_or_external_dependency",
            }
            if item["module_name"] == "mertens_conditional_l2_upper"
            else item
            for item in inventory["modules"]
        ]

        graph = build_main_chain_graph(inventory)

        self.assertEqual(graph["nodes"]["W1"]["status"], "conditional")
        self.assertEqual(graph["nodes"]["W2"]["status"], "not_started")
        self.assertEqual(graph["shortest_blocking_path"], ["W1", "W2"])
        self.assertFalse(graph["rh_chain_closed"])
        self.assertFalse(graph["rh_proved"])
```

- [ ] **Step 2: 运行新增测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_rh_main_chain_graph_audit_test.MFACRHMainChainGraphAuditTest.test_unknown_module_blocks_and_conditional_w1_never_closes_chain -v`

Expected: FAIL，原因是节点、主链边和最短阻断路径尚未实现。

### Task 4: 实现节点状态、固定边、证书和 CLI

**Files:**
- Modify: `experiments/prime_matrix_mfac_rh_main_chain_graph_audit.py`
- Modify: `experiments/prime_matrix_mfac_rh_main_chain_graph_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.md`

- [ ] **Step 1: 实现 W0--W5 状态与固定主链/C1--C7 表**

```python
OBLIGATION_NODES = ("W0", "W1", "W2", "W3", "W4", "W5")
MAIN_CHAIN = (("W0", "W1"), ("W1", "W2"), ("W2", "W3"), ("W3", "W4"), ("W4", "W5"), ("W5", "RH"))
CYCLE_EDGES = {
    "C1": "Chebyshev_error → W0/W2",
    "C2": "Mellin_norm → W2",
    "C3": "zero_free_region/zeta_zero → W3/W4",
    "C4": "RH → W1--W5",
    "C5": "finite_profile → W1/W3/W4",
    "C6": "free_multiplicative_model → W3",
    "C7": "Mertens/PNT cancellation → W1 tail L2",
}


def _node_status(module_roles: list[dict[str, object]], node: str) -> tuple[str, tuple[str, ...]]:
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
    """返回主链的首条非 proved 边；当前实现没有任何 proved 节点。"""
    for source, target in MAIN_CHAIN:
        if target == "RH" or nodes[source]["status"] != "proved" or nodes[target]["status"] != "proved":
            return [source, target]
    return []
```

在 `build_main_chain_graph` 中填充 `nodes`、`main_chain_edges` 与 `cycle_edges`。每条
主链边写入 `status="unproved"`、支持模块名和禁止输入说明；不要从条件模块将任何节点
升级为 `proved`。

- [ ] **Step 2: 实现 Markdown、JSON 写出与 CLI**

```python
DEFAULT_INVENTORY = Path("docs/monograph/prime-matrix-mfac-project-inventory-audit.json")
DEFAULT_JSON = Path("docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.json")
DEFAULT_MARKDOWN = Path("docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.md")


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
```

`render_markdown` 必须包含逐模块角色表、W0--W5 节点表、主链边表、C1--C7 表、
`shortest_blocking_path`、`rh_chain_closed=false`、`rh_proved=false`，并明确说明图谱不运行模块且不构成 RH 证明。

- [ ] **Step 3: 添加 CLI 与输入 RH 声明边界测试并运行模块测试**

```python
    def test_cli_never_promotes_inventory_rh_claim_to_graph_proof(self) -> None:
        """即使库存模块声称 RH，图谱也只按预注册义务输出未闭合状态。"""
        from pathlib import Path
        from tempfile import TemporaryDirectory
        import json
        import subprocess
        import sys

        with TemporaryDirectory() as directory:
            root = Path(directory)
            inventory_path = root / "inventory.json"
            json_path = root / "graph.json"
            markdown_path = root / "graph.md"
            inventory_path.write_text(
                json.dumps(
                    {
                        "modules": [
                            {
                                "module_name": name,
                                "classification": "open_or_unresolved",
                                "rh_blockers": [],
                                "rh_proved_field": name == "actual_lcm_gram_energy",
                            }
                            for name in MODULE_ROLE_REGISTRY
                        ]
                    }
                ),
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_rh_main_chain_graph_audit.py",
                    "--inventory", str(inventory_path),
                    "--json-out", str(json_path),
                    "--markdown-out", str(markdown_path),
                ],
                cwd=Path.cwd(), capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertFalse(payload["rh_proved"])
            self.assertFalse(payload["rh_chain_closed"])
            self.assertIn("不构成 RH 证明", markdown_path.read_text(encoding="utf-8"))
```

Run: `python3 -m unittest experiments.prime_matrix_mfac_rh_main_chain_graph_audit_test -v`

Expected: PASS，且任何测试产物均不含 `rh_proved=true` 或 `rh_chain_closed=true`。

### Task 5: 生成图谱、回归并提交阶段 2

**Files:**
- Create: `docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.md`

- [ ] **Step 1: 生成默认图谱并检查严格覆盖与顶层边界**

Run:

```bash
python3 experiments/prime_matrix_mfac_rh_main_chain_graph_audit.py
python3 - <<'PY'
import json
from pathlib import Path
payload = json.loads(Path("docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.json").read_text())
assert payload["unmapped_modules"] == []
assert payload["stale_registry_modules"] == []
assert payload["rh_chain_closed"] is False
assert payload["rh_proved"] is False
assert payload["shortest_blocking_path"] == ["W0", "W1"]
PY
```

Expected: 19 模块均已映射；默认图谱首条未闭合边是 `W0→W1`，且顶层不认证 RH。

- [ ] **Step 2: 运行图谱测试和全量 MFAC 回归**

Run:

```bash
python3 -m unittest experiments.prime_matrix_mfac_rh_main_chain_graph_audit_test -v
python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v
git diff --check
```

Expected: 新图谱测试和全量 MFAC 测试通过；`git diff --check` 无输出。

- [ ] **Step 3: 仅提交阶段 2 文件**

Run:

```bash
git add \
  docs/superpowers/specs/2026-08-13-mfac-rh-main-chain-graph-design.md \
  docs/superpowers/plans/2026-08-13-mfac-rh-main-chain-graph.md \
  experiments/prime_matrix_mfac_rh_main_chain_graph_audit.py \
  experiments/prime_matrix_mfac_rh_main_chain_graph_audit_test.py \
  docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.json \
  docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.md
git commit -m "审计 MFAC RH 主链依赖图"
```

Expected: 提交只包含阶段 2 的规格、计划、图谱模块、测试和证书；`AGENTS.md` 与用户原有未提交文件绝不进入暂存区。

## 计划自检

- **规格覆盖：** Task 1--2 实现 19 模块预注册映射、多个角色和双向集合覆盖；Task 3--4 实现 W0--W5、C1--C7、主链阻断、证书和 CLI；Task 5 覆盖默认图谱、回归和独立提交。
- **RH 边界：** 不存在将 `forward_obligation` 或库存声明转成 `proved` 的路径；顶层固定 `rh_chain_closed=false`、`rh_proved=false`。
- **范围控制：** 只读取阶段 1 JSON，不读取/执行模块，不生成额外可视化，不改变阶段 1 分类。
- **占位符检查：** 本计划不含 `TBD`、`TODO`、未定义接口或泛化的“适当处理”步骤。
