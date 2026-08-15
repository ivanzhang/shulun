# MFAC W2→W3 实际 Mellin 传递合同审计 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建 W2→W3 实际 dyadic 能量到 Mellin 半平面范数的防循环合同审计器，登记外部引理而不证明 W3 或 RH。

**Architecture:** 单一标准库模块负责严格合同校验、状态载荷、JSON/Markdown 证书和 CLI；单元测试对所有量词、测度、来源和结论边界回归验证。默认合同只记录外部证明包，所有 W3/RH 状态固定未证明。

**Tech Stack:** Python 3 标准库（`argparse`、`json`、`math`、`pathlib`、`typing`、`unittest`）。

---

### Task 1: 写入最小红灯测试

**Files:**
- Create: `experiments/prime_matrix_mfac_w2_w3_mellin_transfer_audit_test.py`

- [x] **Step 1: 写入合法合同不会提升 W3 或 RH 的测试**

```python
def test_valid_contract_only_registers_mellin_transfer_chain(self) -> None:
    payload = audit_w2_w3_mellin_transfer(default_contract())
    self.assertEqual(payload["w2_to_w3_status"], "assumption_chain_registered")
    self.assertEqual(payload["actual_mellin_half_plane_contraction_status"], "unproved")
    self.assertEqual(payload["w3_spectral_contraction_status"], "unproved")
    self.assertFalse(payload["rh_proved"])
```

- [x] **Step 2: 运行测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w2_w3_mellin_transfer_audit_test.MFACW2W3MellinTransferAuditTest.test_valid_contract_only_registers_mellin_transfer_chain -v`

Expected: FAIL with `ModuleNotFoundError`，因为新审计模块尚不存在。

### Task 2: 实现最小合同审计器

**Files:**
- Create: `experiments/prime_matrix_mfac_w2_w3_mellin_transfer_audit.py`

- [x] **Step 1: 实现合法合同和固定状态**

```python
REQUIRED_LEMMAS = (
    "actual_dyadic_chebyshev_energy_bound",
    "dyadic_scale_partition",
    "weighted_scale_summability",
    "mellin_plancherel_transfer",
)

def audit_w2_w3_mellin_transfer(contract: Mapping[str, object]) -> dict[str, object]:
    """登记 W2→W3 外部传递证明包，绝不提升为 W3 或 RH 结论。"""
    checked = _validate_contract(contract)
    return {
        **checked,
        "w2_to_w3_status": "assumption_chain_registered",
        "actual_mellin_half_plane_contraction_status": "unproved",
        "w3_spectral_contraction_status": "unproved",
        "rh_proved": False,
    }
```

实现初始验证：`contract` 为 `Mapping`，四项引理均为内建 `True`，并严格检查实际误差对象、dyadic 变量、测度、半平面参数和常数依赖。

- [x] **Step 2: 运行 Task 1 测试确认转绿**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w2_w3_mellin_transfer_audit_test.MFACW2W3MellinTransferAuditTest.test_valid_contract_only_registers_mellin_transfer_chain -v`

Expected: PASS。

### Task 3: 添加循环与输入验证红灯测试

**Files:**
- Modify: `experiments/prime_matrix_mfac_w2_w3_mellin_transfer_audit_test.py`

- [x] **Step 1: 写入禁项、参数、来源和目标结论测试**

```python
def test_contract_rejects_cycles_bad_measure_parameter_and_promoted_fields(self) -> None:
    base = default_contract()
    for field in REQUIRED_LEMMAS:
        broken = dict(base)
        broken[field] = False
        with self.assertRaisesRegex(ValueError, field):
            audit_w2_w3_mellin_transfer(broken)
    for source in ("RH", "Mellin_contraction", "finite_profile"):
        broken = dict(base)
        broken["claimed_transfer_uses"] += (source,)
        with self.assertRaisesRegex(ValueError, "禁止"):
            audit_w2_w3_mellin_transfer(broken)
    for parameter in (0.5, 1.0, float("nan"), True):
        broken = dict(base)
        broken["half_plane_parameter"] = parameter
        with self.assertRaisesRegex(ValueError, "half_plane_parameter"):
            audit_w2_w3_mellin_transfer(broken)
```

- [x] **Step 2: 运行测试确认红灯**

Run: `python3 -m unittest experiments.prime_matrix_mfac_w2_w3_mellin_transfer_audit_test.MFACW2W3MellinTransferAuditTest.test_contract_rejects_cycles_bad_measure_parameter_and_promoted_fields -v`

Expected: FAIL，原因是最小实现尚未验证 `claimed_transfer_uses` 中的禁止来源或所有目标结论字段。

### Task 4: 完成证书与 CLI

**Files:**
- Modify: `experiments/prime_matrix_mfac_w2_w3_mellin_transfer_audit.py`
- Modify: `experiments/prime_matrix_mfac_w2_w3_mellin_transfer_audit_test.py`
- Create: `docs/monograph/prime-matrix-mfac-w2-w3-mellin-transfer-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-w2-w3-mellin-transfer-audit.md`

- [x] **Step 1: 完成防循环验证、证书写出和 CLI**

```python
def write_certificate(payload: Mapping[str, object], json_out: Path, markdown_out: Path) -> None:
    """写出机器证书和显式保留未证明边界的人读证书。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_out.write_text(_render_markdown(payload), encoding="utf-8")
```

拒绝 `uses`、`claimed_transfer_uses` 中的禁项，以及 `rh_proved`、`w3_closed` 和
`actual_mellin_half_plane_contraction` 等目标字段。CLI 接受 `--half-plane-parameter`、
`--json-out`、`--markdown-out`，并写出四项引理、固定测度和未证明边界。

- [x] **Step 2: 添加脚本路径 CLI 证书测试**

```python
def test_script_path_cli_writes_non_proof_certificate(self) -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        result = subprocess.run([...], check=False, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads((root / "transfer.json").read_text(encoding="utf-8"))
        self.assertFalse(payload["rh_proved"])
        self.assertIn("w3_spectral_contraction_status=unproved", (root / "transfer.md").read_text(encoding="utf-8"))
```

- [x] **Step 3: 完整验证并生成默认证书**

Run:

```bash
python3 -m unittest experiments.prime_matrix_mfac_w2_w3_mellin_transfer_audit_test -v
python3 experiments/prime_matrix_mfac_w2_w3_mellin_transfer_audit.py --half-plane-parameter 0.75
```

Expected: 全部 PASS；JSON、Markdown 与命令行输出均保持 W3/RH 未证明边界。
