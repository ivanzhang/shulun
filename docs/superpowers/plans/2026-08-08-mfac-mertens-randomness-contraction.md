# MFAC Mertens 随机性缺陷审计 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建可复现的 `M(x)` 分块随机性缺陷审计器，严格把经验高斯比较与实际 Mellin 收缩的理论合同分开。

**Architecture:** 单个标准库 Python 模块负责精确 Möbius 筛、分层区块聚合、可种子化代理基线、经验统计和证书写出；对应 `unittest` 模块锁定代数重构、退化情形、随机可复现性与反循环状态。审计器默认生成有限范围的经验读数，只有检查到独立的理论合同字段时才可能报告实际收缩，当前语料预期保持未闭合。

**Tech Stack:** Python 3 标准库（`argparse`、`dataclasses`、`json`、`math`、`random`、`statistics`、`unittest`）。

---

## 文件结构

- Create: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit.py`
  - 精确 Möbius 筛、块统计、按 `omega(n)` 分层、三类确定性/随机代理、合同分类与证书写出。
- Create: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py`
  - 所有数据合同和证书边界的单元测试。
- Create: `docs/monograph/prime-matrix-mfac-mertens-randomness-contraction-audit.json`
  - 默认参数运行后写出的机器证书。
- Create: `docs/monograph/prime-matrix-mfac-mertens-randomness-contraction-audit.md`
  - 默认参数运行后写出的人读边界说明。
- Modify: `docs/monograph/external-theorem-index.md`
  - 仅追加证书索引、状态与“不构成 RH 证明”的边界；不改写既有 MFAC 结论。

### Task 1: 锁定精确 Möbius 与分层重构合同

**Files:**
- Create: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py`
- Create: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit.py`

- [ ] **Step 1: 写出失败的精确筛与分层重构测试**

```python
def test_mobius_sieve_and_omega_match_small_known_values(self) -> None:
    mobius, omega = mobius_and_omega_sieve(10)
    self.assertEqual(mobius[1:11], [1, -1, -1, 0, -1, 1, -1, 0, 0, 1])
    self.assertEqual(omega[1:11], [0, 1, 1, 1, 1, 2, 1, 1, 2, 2])

def test_layered_block_deltas_reconstruct_actual_mertens_delta(self) -> None:
    mobius, omega = mobius_and_omega_sieve(48)
    block = summarize_block(mobius, omega, start=12, length=24)
    self.assertEqual(block.delta_mertens, sum(block.layer_deltas.values()))
    self.assertEqual(block.delta_mertens, sum(mobius[13:37]))
```

- [ ] **Step 2: 运行测试，确认因 API 不存在而失败**

Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py -v`

Expected: FAIL，提示 `ModuleNotFoundError` 或 `ImportError`，且不得修改既有审计器。

- [ ] **Step 3: 最小实现精确 Möbius 筛与块数据结构**

```python
def mobius_and_omega_sieve(limit: int) -> tuple[list[int], list[int]]:
    if limit < 1:
        raise ValueError("limit 必须至少为 1")
    mobius = [1] * (limit + 1)
    omega = [0] * (limit + 1)
    is_prime = [True] * (limit + 1)
    for prime in range(2, limit + 1):
        if not is_prime[prime]:
            continue
        for multiple in range(prime, limit + 1, prime):
            is_prime[multiple] = False
            omega[multiple] += 1
            mobius[multiple] *= -1
        for multiple in range(prime * prime, limit + 1, prime * prime):
            mobius[multiple] = 0
    return mobius, omega
```

实现 `BlockSummary` 与 `summarize_block`，采用区间 `(start, start + length]`，并把 `mu(n)=0` 单独计入 `zero_count`；`layer_deltas` 仅累计非零 Möbius 项。

- [ ] **Step 4: 运行测试，确认精确合同通过**

Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py -v`

Expected: 两个新测试 PASS；未实现的后续测试可仍为失败。

- [ ] **Step 5: 不提交**

用户尚未要求创建提交；保留工作区变更，继续下一任务。

### Task 2: 锁定尺度桶、退化方差与经验统计合同

**Files:**
- Modify: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py`
- Modify: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit.py`

- [ ] **Step 1: 写出失败的桶统计测试**

```python
def test_degenerate_samples_do_not_construct_standardized_moments(self) -> None:
    summary = summarize_samples([0, 0, 0])
    self.assertTrue(summary["degenerate_variance"])
    self.assertIsNone(summary["standardized_skewness"])
    self.assertIsNone(summary["excess_kurtosis"])

def test_sample_summary_reports_signs_moments_and_tail_counts(self) -> None:
    summary = summarize_samples([-2, -1, 1, 2])
    self.assertEqual(summary["sample_count"], 4)
    self.assertEqual(summary["zero_count"], 0)
    self.assertEqual(summary["sign_bias"], 0.0)
    self.assertAlmostEqual(summary["mean"], 0.0)
    self.assertFalse(summary["degenerate_variance"])
```

- [ ] **Step 2: 运行新增测试，确认失败**

Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.MFACMertensRandomnessContractionAuditTest.test_degenerate_samples_do_not_construct_standardized_moments -v`

Expected: FAIL，提示 `summarize_samples` 未定义。

- [ ] **Step 3: 最小实现无偏差声明的经验汇总**

```python
def summarize_samples(values: Sequence[float]) -> dict[str, Any]:
    if not values:
        raise ValueError("样本不能为空")
    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    if variance == 0.0:
        return {"mean": mean, "variance": 0.0, "degenerate_variance": True,
                "standardized_skewness": None, "excess_kurtosis": None}
    scale = math.sqrt(variance)
    standardized = [(value - mean) / scale for value in values]
    return {"mean": mean, "variance": variance, "degenerate_variance": False,
            "standardized_skewness": average(value ** 3 for value in standardized),
            "excess_kurtosis": average(value ** 4 for value in standardized) - 3.0}
```

在同一函数中加入 `sample_count`、`zero_count`、`sign_bias` 与预先固定的 `tail_counts`；统计量必须命名为经验读数，不得输出“正态已证明”。

- [ ] **Step 4: 运行任务测试，确认通过**

Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py -v`

Expected: Task 1–2 的测试 PASS。

- [ ] **Step 5: 不提交**

用户尚未要求创建提交；保留工作区变更，继续下一任务。

### Task 3: 锁定三类代理基线的可复现性与边界

**Files:**
- Modify: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py`
- Modify: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit.py`

- [ ] **Step 1: 写出失败的代理测试**

```python
def test_seeded_independent_sign_baseline_is_reproducible(self) -> None:
    values = [1, -1, 1, -1, 0, 1]
    self.assertEqual(
        independent_sign_baseline(values, seed=17),
        independent_sign_baseline(values, seed=17),
    )

def test_layer_shuffle_preserves_each_layer_multiset(self) -> None:
    layers = {1: [1, -1, 1], 2: [-1, 1]}
    shuffled = layer_shuffle_baseline(layers, seed=9)
    self.assertEqual({key: sorted(value) for key, value in shuffled.items()},
                     {key: sorted(value) for key, value in layers.items()})

def test_proxy_baselines_are_labeled_empirical_only(self) -> None:
    result = build_proxy_baselines([1, -1, 0, 1], {1: [1, -1], 2: [1]}, seed=3)
    self.assertEqual(result["status"], "empirical_proxy_baselines_only")
    self.assertFalse(result["actual_mellin_contraction_present"])
```

- [ ] **Step 2: 运行代理测试，确认失败**

Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.MFACMertensRandomnessContractionAuditTest.test_seeded_independent_sign_baseline_is_reproducible -v`

Expected: FAIL，提示代理函数不存在。

- [ ] **Step 3: 最小实现代理与局部约束声明**

```python
def independent_sign_baseline(values: Sequence[int], seed: int) -> list[int]:
    generator = random.Random(seed)
    return [0 if value == 0 else generator.choice((-1, 1)) for value in values]

def layer_shuffle_baseline(layers: Mapping[int, Sequence[int]], seed: int) -> dict[int, list[int]]:
    generator = random.Random(seed)
    shuffled: dict[int, list[int]] = {}
    for layer, values in sorted(layers.items()):
        shuffled[layer] = list(values)
        generator.shuffle(shuffled[layer])
    return shuffled
```

实现第三类“局部约束代理”时只接受显式 `preserved_constraints` 描述，并在没有实现真实局部约束时返回 `not_implemented_with_actual_local_constraints`；不得伪造此基线。

- [ ] **Step 4: 运行代理测试，确认通过**

Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py -v`

Expected: Task 1–3 的测试 PASS。

- [ ] **Step 5: 不提交**

用户尚未要求创建提交；保留工作区变更，继续下一任务。

### Task 4: 锁定理论合同分类与不可升级状态

**Files:**
- Modify: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py`
- Modify: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit.py`

- [ ] **Step 1: 写出失败的合同分类测试**

```python
def test_missing_contract_fields_keep_empirical_audit_outside_mellin_closure(self) -> None:
    result = classify_contraction_contract({"fixed_actual_integer_embedding": True})
    self.assertEqual(result["status"], "empirical_randomness_model_not_a_rh_proof")
    self.assertIn("uniform_signed_block_covariance_bound", result["missing_contract_fields"])
    self.assertFalse(result["actual_mellin_contraction_present"])
    self.assertFalse(result["rh_proved"])

def test_complete_synthetic_contract_still_is_not_an_actual_rh_proof(self) -> None:
    result = classify_contraction_contract(complete_synthetic_contraction_contract())
    self.assertEqual(result["status"], "synthetic_contract_not_actual_proof")
    self.assertFalse(result["rh_proved"])
```

- [ ] **Step 2: 运行合同测试，确认失败**

Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.MFACMertensRandomnessContractionAuditTest.test_missing_contract_fields_keep_empirical_audit_outside_mellin_closure -v`

Expected: FAIL，提示 `classify_contraction_contract` 未定义。

- [ ] **Step 3: 最小实现不可升级分类器**

```python
REQUIRED_CONTRACTION_FIELDS = (
    "fixed_actual_integer_embedding",
    "exact_mobius_block_decomposition",
    "deterministic_dyadic_block_family",
    "uniform_signed_block_covariance_bound",
    "uniform_higher_cumulant_defect_bound",
    "uniform_large_deviation_or_high_moment_bound",
    "explicit_layer_interaction_identity",
    "noncircular_offconstant_coercive_energy_identity",
    "scale_summability_to_mellin_norm",
    "no_use_of_RH_or_zero_free_input",
)
```

分类器只接受每个字段为严格 `True` 时才称合同完整；即使 synthetic 合同完整，也必须保留 `actual_mellin_contraction_present=false` 与 `rh_proved=false`，直至由语料中独立的实际定理来源验证。

- [ ] **Step 4: 运行合同测试，确认通过**

Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py -v`

Expected: Task 1–4 的测试 PASS。

- [ ] **Step 5: 不提交**

用户尚未要求创建提交；保留工作区变更，继续下一任务。

### Task 5: 生成默认审计、证书和索引边界

**Files:**
- Modify: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py`
- Modify: `experiments/prime_matrix_mfac_mertens_randomness_contraction_audit.py`
- Create: `docs/monograph/prime-matrix-mfac-mertens-randomness-contraction-audit.json`
- Create: `docs/monograph/prime-matrix-mfac-mertens-randomness-contraction-audit.md`
- Modify: `docs/monograph/external-theorem-index.md`

- [ ] **Step 1: 写出失败的端到端证书测试**

```python
def test_writer_keeps_empirical_evidence_distinct_from_rh_proof(self) -> None:
    certificate = audit_mertens_randomness(limit=2_048, block_length=32, seed=7)
    with tempfile.TemporaryDirectory() as directory:
        json_path = Path(directory) / "certificate.json"
        markdown_path = Path(directory) / "certificate.md"
        write_certificate(certificate, json_path, markdown_path)
        payload = json.loads(json_path.read_text(encoding="utf-8"))
        markdown = markdown_path.read_text(encoding="utf-8")
    self.assertTrue(payload["layer_reconstruction_holds"])
    self.assertEqual(payload["status"], "empirical_randomness_model_not_a_rh_proof")
    self.assertFalse(payload["actual_mellin_contraction_present"])
    self.assertIn("不构成 RH 证明", markdown)
```

- [ ] **Step 2: 运行端到端测试，确认失败**

Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.MFACMertensRandomnessContractionAuditTest.test_writer_keeps_empirical_evidence_distinct_from_rh_proof -v`

Expected: FAIL，提示 `audit_mertens_randomness` 或 `write_certificate` 未定义。

- [ ] **Step 3: 最小实现审计入口与证书写出**

```python
def audit_mertens_randomness(limit: int, block_length: int, seed: int) -> dict[str, Any]:
    mobius, omega = mobius_and_omega_sieve(limit)
    blocks = collect_dyadic_blocks(mobius, omega, block_length)
    return {
        "certificate_type": "prime_matrix_mfac_mertens_randomness_contraction_audit",
        "status": "empirical_randomness_model_not_a_rh_proof",
        "parameters": {"limit": limit, "block_length": block_length, "seed": seed},
        "layer_reconstruction_holds": all(block.reconstructs for block in blocks),
        "actual_mellin_contraction_present": False,
        "rh_proved": False,
        "next_positive_gate": "ActualMertensBlockDefectToOffConstantCoerciveEnergyLawBeforeMellin",
    }
```

实现 CLI 的 `--limit`、`--block-length`、`--seed`、`--json-out`、`--markdown-out`。默认输出到 `docs/monograph/`，证书包含默认参数、样本数量、退化桶数量、三类基线的状态、缺失合同字段和明确限制说明。

- [ ] **Step 4: 运行端到端测试与默认证书生成**

Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py -v && python3 experiments/prime_matrix_mfac_mertens_randomness_contraction_audit.py`

Expected: 全部测试 PASS，并写入两个 `docs/monograph/prime-matrix-mfac-mertens-randomness-contraction-audit.*` 文件。

- [ ] **Step 5: 追加最小索引记录并做范围检查**

在 `docs/monograph/external-theorem-index.md` 追加独立小节，列出脚本、测试、证书状态和下一正向门；明确这是内部经验/合同审计，不是外部定理、Mellin 收缩或 RH 证明。

Run: `git diff --check && git diff -- docs/monograph/external-theorem-index.md`

Expected: 无空白错误；diff 只包含新增 MFAC Mertens 审计索引块。

- [ ] **Step 6: 不提交**

用户尚未要求创建提交；报告变更和验证结果，等待进一步指示。

## 最终验证

- [ ] Run: `python3 -m unittest experiments/prime_matrix_mfac_mertens_randomness_contraction_audit_test.py -v`
  - Expected: 全部测试 PASS。
- [ ] Run: `python3 experiments/prime_matrix_mfac_mertens_randomness_contraction_audit.py --limit 4096 --block-length 64 --seed 17 --json-out /tmp/mertens-audit.json --markdown-out /tmp/mertens-audit.md`
  - Expected: 两个临时证书成功写出，且 JSON 明确含有 `actual_mellin_contraction_present=false` 与 `rh_proved=false`。
- [ ] Run: `git diff --check && git status --short`
  - Expected: 无格式错误；只显示本计划对应的新增/修改文件与原有未提交文档。

## 自检

- 覆盖规格中的精确分层重构、三类基线、退化桶、可复现种子、经验/定理边界和非循环合同字段。
- 计划不依赖第三方库，不需要网络或外部数据源。
- 计划不将任何统计拟合表述为 RH 证据，也不修改既有去常数循环审计结论。
