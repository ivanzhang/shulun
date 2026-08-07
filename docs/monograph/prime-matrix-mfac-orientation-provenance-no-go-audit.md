# MFAC 取向来源 provenance no-go 审计

**状态：** `current_corpus_has_no_admissible_forward_orientation_source`
**核验日期：** `2026-08-07`

```text
admissible_orientation_source_present=false
earliest_missing_forward_field=origin_selector
next_positive_gate=PrimitiveOrientationLocalFactorProductLawBeforePushforward
mathematical_nonexistence_proved=false
rh_proved=false
row_column_unconditional_closed=false
```

当前语料未提交满足全部前向字段的 actual primitive orientation 来源。
这不表示数学上不可能存在此类来源，也不证明 signed transport、行/列命题或 RH。

## 候选来源

| name | admissible | missing fields |
| --- | --- | --- |
| `actual_atomic_record_constructor` | `false` | `pre_cauchy, provides_origin_selector, provides_orientation_bit, provides_local_factor_product, provides_prepushforward_sum_identity, actual_emitter_registered` |
| `phi_lpf_owner_support` | `false` | `provides_origin_selector, provides_orientation_bit, provides_local_factor_product, provides_prepushforward_sum_identity, actual_emitter_registered` |
| `rough_cofactor_domain_split` | `false` | `provides_origin_selector, provides_orientation_bit, provides_local_factor_product, provides_prepushforward_sum_identity, actual_emitter_registered` |
| `mobius_parity_shadow` | `false` | `provides_origin_selector, provides_local_factor_product, provides_prepushforward_sum_identity, actual_emitter_registered` |

## 正向门

要继续内部 signed-source 路线，必须独立提交 `PrimitiveOrientationLocalFactorProductLawBeforePushforward`：在 pre-Cauchy 层同时给出 origin selector、orientation bit、local-factor product、actual-emitter registration 与 prepushforward signed-sum identity。
