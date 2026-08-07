# MFAC 取向来源 No-Go 审计设计

## 目标

新增一个最小、可复核的审计器，检查当前项目语料是否已经提交了从允许的
pre-Cauchy 输入到 actual noncanonical primitive orientation 的前向来源证据。
审计的结论只能描述当前语料状态；它不得声称此类构造在数学上不可能存在，
更不得声称 RH、行/列命题或 signed transport 已证明。

## 非目标

- 不构造新的 alpha/delta signed coefficient。
- 不从 payment、Phi pushforward、Cauchy/dispersion、零行覆盖、terminal 表或外部谱输入反推取向。
- 不把 Möbius/parity 影子自动升级为 actual emitter 的 orientation。
- 不修改既有 MFAC-1A/1B 的边界结论。

## 事实输入

审计只读取现有 JSON/路由证书，并使用以下已知边界：

1. actual atomic record constructor 审计给出最早缺字段 `origin_selector`；
2. Phi-LPF 支撑键 `(p,m)` 唯一编码无符号 composite owner，但不赋 signed value；
3. rough-cofactor 分裂是 domain 分裂，不给 `a_p(qm)` 的 orientation/local factor 更新；
4. Möbius/parity 目前仅为候选取向影子，未有 exact emitter coefficient、local-factor product 或 prepushforward identity。

## 审计模型

定义候选取向来源条目：

```text
{
  name,
  pre_cauchy,
  independent_of_downstream,
  provides_origin_selector,
  provides_orientation_bit,
  provides_local_factor_product,
  provides_prepushforward_sum_identity,
  actual_emitter_registered
}
```

一个条目只有在所有布尔字段均为真时才是 `admissible_orientation_source`。
审计器必须至少列出：

- `phi_lpf_owner_support`：无符号支撑；
- `rough_cofactor_domain_split`：无符号递推分裂；
- `mobius_parity_shadow`：候选取向影子；
- `actual_atomic_record_constructor`：actual record 构造器状态。

## 判定规则

1. 若 actual record 审计没有前向构造器，`actual_atomic_record_constructor` 不能提供 `origin_selector`。
2. Phi-LPF 支撑与 rough-cofactor 分裂不得提供 orientation bit 或 local-factor product。
3. Möbius/parity 只有在独立记录了 emitter registration、local-factor product 和 prepushforward sum identity 时才可通过；当前证据不足时必须失败。
4. 所有候选均失败时，输出：

```text
admissible_orientation_source_present=false
earliest_missing_forward_field=origin_selector
next_positive_gate=PrimitiveOrientationLocalFactorProductLawBeforePushforward
```

5. 无论结果如何，必须明确 `mathematical_nonexistence_proved=false` 与
`row_column_unconditional_closed=false`。

## 产物与验证

新增：

- `experiments/prime_matrix_mfac_orientation_provenance_no_go_audit.py`
- `experiments/prime_matrix_mfac_orientation_provenance_no_go_audit_test.py`
- `docs/monograph/prime-matrix-mfac-orientation-provenance-no-go-audit.md`
- `docs/monograph/prime-matrix-mfac-orientation-provenance-no-go-audit.json`

测试覆盖：当前语料负例、完整 synthetic 正例、Möbius/parity 不足反例、下游依赖拒绝。
审计运行生成 Markdown/JSON 证书；主稿与 claim-status 表仅在测试通过后再决定是否同步，且只写审计边界。
