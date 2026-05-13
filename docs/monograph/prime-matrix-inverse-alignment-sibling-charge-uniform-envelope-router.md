# Prime Matrix 逆元 tau 兄弟收费统一 Envelope 路由器

**状态：** `raw_inverse_alignment_tau_envelope_closed_but_scale_insufficient_cold_restricted_envelope_open`

精确逆元 tau 兄弟剖面给出了一个无条件 raw envelope：出现的 tau 桶容量不超过 `sum_{z<q<P} ceil((P-1)/q)`。但这个 envelope 在 `z=P^0.43` 时是 `Θ(P)` 级，尺度远大于当前需求侧的 `P^0.43/log P` 级目标，因此不能直接闭合冷供给预算。这说明逆元方程组必须继续与终端冷窗口条件结合：只有仍通过冷兼容测试且没有热核心、固定历史或 PDEC/ColumnCRT 回流的 tau 兄弟桶，才可以计入冷供给。

```text
exact_tau_charge_profile_imported=true
raw_inverse_alignment_tau_charge_envelope_closed=true
raw_envelope_scale_mismatch_certified=true
exact_inverse_alignment_sibling_charge_uniform_envelope_proved=false
cold_restricted_inverse_alignment_sibling_charge_envelope_proved=false
row_column_unconditional_closed=false
```

## 1. Envelope 结论

| name | statement | status |
| --- | --- | --- |
| `raw_tau_capacity_envelope` | sum_{q>z, tau bucket appears} mu_q <= sum_{z<q<P} ceil((P-1)/q). | `closed` |
| `mertens_scale` | for z=P^alpha, the raw envelope has scale about P log(1/alpha). | `closed_as_scale_diagnostic` |
| `raw_envelope_insufficient` | P log(1/alpha) is too large to close the current cold-supply budget against P^alpha/log P demand. | `closed_negative_result` |
| `cold_restricted_envelope_needed` | only tau buckets that remain cold-compatible after terminal window tests may be counted as cold supply. | `next_input` |

## 2. 样本 Envelope

| P | x | z | R_xz | appeared capacity | suffix capacity | suffix/atom |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 168 | 3 | 4 | 5 | 5 | 1.250 |
| 17 | 1210 | 3 | 5 | 7 | 7 | 1.400 |
| 19 | 3658 | 3 | 6 | 10 | 11 | 1.833 |
| 23 | 58 | 3 | 7 | 12 | 14 | 2.000 |
| 29 | 5209 | 4 | 9 | 20 | 20 | 2.222 |
| 31 | 60794 | 4 | 10 | 20 | 21 | 2.100 |
| 37 | 73916 | 4 | 12 | 23 | 26 | 2.167 |
| 41 | 170880 | 4 | 13 | 29 | 30 | 2.308 |
| 43 | 162932 | 5 | 11 | 22 | 24 | 2.182 |

## 3. 尺度诊断

| P | z=P^0.43 | raw model | demand model | raw/demand |
| ---: | ---: | ---: | ---: | ---: |
| 100000 | 141.254 | 84397.007 | 28.533 | 2957.884 |
| 1000000 | 380.189 | 843970.070 | 63.998 | 13187.499 |
| 1000000000 | 7413.102 | 843970070.295 | 831.904 | 1014503.849 |
| 1000000000000 | 144543.977 | 843970070294.529 | 12165.630 | 69373313.101 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ExactTauChargeImported` | `true` | `true` | 逆元剖面已给出 tau 桶、mu_tau 和实际 assigned atom。 | none for raw identity |
| `RawInverseAlignmentTauChargeEnvelopeClosed` | `true` | `true` | tau 兄弟收费有一个无条件 raw 上界：所有 q>z 的 mu_q 总和。 | scale is too large |
| `RawEnvelopeScaleMismatchCertified` | `true` | `true` | z=P^0.43 时 raw 上界为 Θ(P)，不能闭合当前冷供给预算。 | ColdRestrictedInverseAlignmentSiblingChargeEnvelope |
| `ExactInverseAlignmentSiblingChargeUniformEnvelopeProved` | `false` | `false` | 不带冷兼容过滤的逆元 tau envelope 过宽，不能作为最终父级预算。 | ColdRestrictedInverseAlignmentSiblingChargeEnvelope |
| `ColdRestrictedEnvelopeProved` | `false` | `false` | 还需把终端冷窗口、热回流、固定历史回流条件压入 tau 桶筛选。 | SiblingColdCoreThresholdNumericEnvelopeTable AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链与真实链的终端矛盾。 | ColdRestrictedInverseAlignmentSiblingChargeEnvelope AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一步

- 主攻：`ColdRestrictedInverseAlignmentSiblingChargeEnvelope`。
- 并行保留：
  - `SiblingColdCoreThresholdNumericEnvelopeTable`
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `FixedTypeHistoryPDECExclusion`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

审稿边界：本步证明 raw envelope 的存在和不足，不声明反例矛盾已闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/inverse-alignment-exact-zero-row-charge-profile-ledger.json` | `c7cabc90437430aee6614b0428662fe0ce67a1eac9a3ee263b5560ef06481db3` |
| `docs/monograph/prime-matrix-inverse-alignment-exact-zero-row-charge-profile-router.json` | `f6f2c2c1d5bbd95e83d085f48ac5c6bb6a6250c72fc450112b6815b8313429ba` |
| `docs/monograph/prime-matrix-strict-cold-window-sibling-charging-router.json` | `be05fb4b2dee03515ca4eea8e086eff6341c0e04d69da9501072cccf74414591` |
| `docs/monograph/prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json` | `c2ef211342a04f992f35f62a595d3c1647663d1a9fde5d1e78ff57c735bf63d6` |
| `experiments/prime_matrix_inverse_alignment_sibling_charge_uniform_envelope_router.py` | `93e7a5c4eb9ce4e65acb581a1e09a0aee9827c9a52d3dc2ce11f9f58eccceb87` |
