# MFAC W1→W2 解析桥合同审计 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建 W1→W2 解析桥的防循环合同审计器，登记必要解析引理而不声称 Chebyshev 能量桥或 RH 已证明。

**Architecture:** 单个标准库 Python 模块负责严格合同验证、状态载荷、JSON/Markdown 证书和 CLI；单元测试覆盖合同边界及文件输出。默认合同仅登记外部证明包，结果固定为条件链已登记、桥未证明、RH 未证明。

**Tech Stack:** Python 3 标准库（`argparse`、`json`、`pathlib`、`typing`、`unittest`）。

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit.py` — 合同验证、审计、写证书和 CLI。
- Create: `experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit_test.py` — 防循环、类型、状态和 CLI 回归测试。
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-analytic-bridge-audit.json` — 默认机器证书。
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-analytic-bridge-audit.md` — 默认人读证书与使用示例。

### Task 1: 建立红灯合同测试

**Files:**
- Create: `experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit_test.py`

- [x] **Step 1: 写入合法审计与固定未证明状态测试**

```python
def test_valid_contract_registers_chain_without_proving_bridge_or_rh(self) -> None:
    payload = audit_w1_w2_analytic_bridge(default_contract())
    self.assertEqual(payload["w1_to_w2_status"], "assumption_chain_registered")
    self.assertEqual(payload["chebyshev_energy_bridge_status"], "unproved")
    self.assertFalse(payload["rh_proved"])
```

- [x] **Step 2: 运行测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_analytic_bridge_audit_test.MFACW1W2AnalyticBridgeAuditTest.test_valid_contract_registers_chain_without_proving_bridge_or_rh -v`

Expected: FAIL with `ModuleNotFoundError`，因为审计模块尚不存在。

### Task 2: 实现最小合同审计器

**Files:**
- Create: `experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit.py`

- [x] **Step 1: 写入验证器和审计函数**

```python
REQUIRED_LEMMAS = (
    "tail_l2_upper",
    "coprime_restricted_tail_bound",
    "euler_phi_aggregation",
    "chebyshev_transfer",
)


def audit_w1_w2_analytic_bridge(contract: Mapping[str, object]) -> dict[str, object]:
    """登记 W1→W2 外部解析证明包，绝不提升为定理结论。"""
    checked = _validate_contract(contract)
    return {
        **checked,
        "w1_to_w2_status": "assumption_chain_registered",
        "chebyshev_energy_bridge_status": "unproved",
        "rh_proved": False,
    }
```

实现 `_validate_contract`：要求内建 `bool` 的四项引理为真、`uniformity_variable == "truncation"`、常数依赖等于 `"fixed_test_function"`、`claimed_bridge_uses` 是 `uses` 子集，并拒绝文档设计列出的所有循环输入。

- [x] **Step 2: 运行 Task 1 测试确认转绿**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_analytic_bridge_audit_test.MFACW1W2AnalyticBridgeAuditTest.test_valid_contract_registers_chain_without_proving_bridge_or_rh -v`

Expected: PASS。

### Task 3: 扩展防御性红灯测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit_test.py`

- [x] **Step 1: 添加缺失引理、错误统一性、循环依赖和伪造状态测试**

```python
def test_contract_rejects_missing_lemmas_nonuniformity_cycles_and_rh_promotion(self) -> None:
    base = default_contract()
    for field in REQUIRED_LEMMAS:
        broken = dict(base)
        broken[field] = False
        with self.assertRaisesRegex(ValueError, field):
            audit_w1_w2_analytic_bridge(broken)
    for source in ("RH", "Mellin", "Chebyshev_error", "finite_profile"):
        broken = dict(base)
        broken["uses"] = base["uses"] + (source,)
        with self.assertRaisesRegex(ValueError, "禁止"):
            audit_w1_w2_analytic_bridge(broken)
    broken = dict(base)
    broken["rh_proved"] = True
    with self.assertRaisesRegex(ValueError, "rh_proved"):
        audit_w1_w2_analytic_bridge(broken)
```

- [x] **Step 2: 运行新增测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w1_w2_analytic_bridge_audit_test.MFACW1W2AnalyticBridgeAuditTest.test_contract_rejects_missing_lemmas_nonuniformity_cycles_and_rh_promotion -v`

Expected: FAIL，因为最小实现尚未完成所有字段验证。

### Task 4: 完成验证、证书和 CLI

**Files:**
- Modify: `experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit.py`
- Modify: `experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-analytic-bridge-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-w1-w2-analytic-bridge-audit.md`

- [x] **Step 1: 实现完整验证和证书函数**

```python
def write_certificate(payload: Mapping[str, object], json_out: Path, markdown_out: Path) -> None:
    """写出机器证书和包含未证明边界的人读证书。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_out.write_text(_render_markdown(payload), encoding="utf-8")
```

默认 CLI 调用 `default_contract()`、`audit_w1_w2_analytic_bridge()` 和 `write_certificate()`；Markdown 显式列出四项外部引理、禁止依赖、`chebyshev_energy_bridge_status=unproved`、`rh_proved=false` 以及 `python3 experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit.py` 使用示例。

- [x] **Step 2: 添加证书和脚本路径 CLI 测试**

```python
def test_script_path_cli_writes_non_proof_certificate(self) -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        result = subprocess.run([...], check=False, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads((root / "bridge.json").read_text(encoding="utf-8"))
        self.assertFalse(payload["rh_proved"])
        self.assertIn("chebyshev_energy_bridge_status=unproved", (root / "bridge.md").read_text(encoding="utf-8"))
```

- [x] **Step 3: 运行完整模块测试并生成默认证书**

Run:

```bash
python3 -m unittest experiments.prime_matrix_mfac_w1_w2_analytic_bridge_audit_test -v
python3 experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit.py
```

Expected: 全部 PASS；默认 JSON 和 Markdown 存在且保持未证明边界。
