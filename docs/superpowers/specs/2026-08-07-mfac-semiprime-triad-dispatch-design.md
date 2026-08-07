# MFAC 半素数三项 Dispatch 审计设计

## 目标

新增最小审计器，固定 offdiagonal 素数对 `p < q` 的三项全局 Möbius payload：

```text
(p, q, +log p)
(q, p, +log q)
(p*q, 1, -log(p*q))
```

检查当前语料是否已经给出从这三项到 actual primitive row 的前向、pre-Cauchy dispatch。
审计必须将“同一 canonical LPF row 的三项零和 collapse”与“已登记 actual dispatch”
严格区分。

## 备选路径与选择

- **A：半素数三项 dispatch 审计（采用）**：最小对象只有三项，可直接检查 row、orientation、local factor 与 registration。
- B：完整 rough-cofactor tree 的 gauge/no-go 审计：覆盖更广，但在首个 seed 缺失时引入无关分支。
- C：直接回流 PDEC/CleanKLS：是合法终端出口，但不检验当前 global D/E transport 能否产生 actual source。

## 非目标

- 不证明 actual dispatch 在数学上不可能存在。
- 不把全局 Möbius payload、D/E history 或三项零和自动升级为 actual primitive source。
- 不构造 alpha/delta、`ψ` 平滑误差、零点排除、行/列无条件命题或 RH 结论。
- 不读取 payment、Phi pushforward、Cauchy/dispersion、零行覆盖、terminal/origin table 或外部谱输入来补写 dispatch。

## 审计模型

每条三项输入包含：

```text
divisor, cofactor, global_payload
```

其 admissible dispatch 必须额外含：

```text
pre_cauchy
independent_of_downstream
origin_selector
actual_emitter_registered
row_key
orientation
local_factor
prepushforward_identity
```

判定：

1. 三项全部映到同一 `row_key`，且 payload 和为零，输出 `canonical_zero_sum_collapse=true`；这不是 actual signed seed。
2. 某项字段缺失时，输出 `actual_dispatch_present=false`，并报告最早缺失字段。
3. 仅当三项均有完整前向字段、至少一项为 actual noncanonical row、且 prepushforward identity 已登记时，才允许 `actual_dispatch_present=true`。
4. synthetic 完整 dispatch 必须通过；依赖 `payment` 的 dispatch 必须被拒绝。

## 当前语料预期

以最小见证 `(p,q)=(2,3)` 为例，当前项目仅有 global colored-word transport，未有 actual primitive binding。因此预期：

```text
global_triad_reconstructed=true
actual_dispatch_present=false
earliest_missing_field=origin_selector
canonical_zero_sum_collapse=false
mathematical_nonexistence_proved=false
rh_proved=false
```

`canonical_zero_sum_collapse` 的合成正例将独立覆盖，避免把“当前无 dispatch”误报为“已证明 collapse”。

## 产物与验证

新增：

- `experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit.py`
- `experiments/prime_matrix_mfac_semiprime_triad_dispatch_audit_test.py`
- `docs/monograph/prime-matrix-mfac-semiprime-triad-dispatch-audit.json`
- `docs/monograph/prime-matrix-mfac-semiprime-triad-dispatch-audit.md`

测试至少覆盖：当前语料负例、完整 synthetic actual dispatch、合成同-row 零和 collapse、
payment 依赖拒绝和证书的 non-RH 边界。状态总表与外部定理索引只登记审计结论及下一正向门：

```text
OffDiagonalSemiprimeTriadActualDispatchBeforePushforward
```
