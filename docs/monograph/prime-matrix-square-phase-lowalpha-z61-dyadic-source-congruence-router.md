# Prime Matrix square-phase low-alpha z=61 dyadic source congruence

**状态：** `z61_dyadic_absorber_reduced_to_source_congruence_skeleton_global_proof_open`

dyadic lift 吸收器已经回落到同一个源同余骨架：phase modulus `28842` 同时是负原子的 `b` 与 hit lcm，三条源纤维恰为 quotient `1,2,4`，且每条都满足 singleton interval `a=floor(p^2/(bq))+1` 与短残基 `0<qab-p^2<p`。因此下一步不再需要在抽象权重层打转，而是集中证明这种源同余骨架的全局强制性，或登记 DyadicSource-PDEC。

```text
phase_modulus=28842
phase_modulus_matches_negative_anchor=true
source_negative_quotients=[1]
source_positive_quotients=[2, 4]
quotient_ladder_matches_absorber=true
all_b_on_phase_ladder=true
all_singleton_sources_closed=true
all_short_residues_closed=true
dyadic_source_congruence_skeleton_closed_for_sample=true
row_column_unconditional_closed=false
```

## 1. 源同余骨架

| quotient | sign | p | q | a | b | delta | width(a) | singleton |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `negative` | 36739 | 53 | 883 | 28842 | 22637 | 0.024034 | true |
| 2 | `positive` | 200003 | 71 | 9767 | 57684 | 173579 | 0.048834 | true |
| 4 | `positive` | 200003 | 37 | 9371 | 115368 | 527 | 0.046854 | true |

## 2. 自足小引理

若同一 phase modulus `B` 下存在 quotient `1,2,4` 三条源纤维，其中 quotient `1` 为负、`2,4` 为正，并且三条都由 singleton interval gate `a=floor(p^2/(bq))+1` 产生，则该骨架给出 dyadic lift 吸收器。原因是 `b=B,2B,4B` 位于同一 hit-moduli 组的倍数相位，组权重相同，两个正原子逐权重吸收一个负原子。

## 3. 证明边界

- 已闭合：样本内 dyadic lift 吸收器完全来自 quotient `1,2,4` 源同余骨架。
- 未闭合：全局源同余骨架强制性，或 DyadicSource-PDEC 排斥。
- 下一目标：`GlobalDyadicSourceCongruenceProofOrDyadicSourcePDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-dyadic-absorber-router.json` | `65ce21708202ca8dcc7098eb114492541672abe0cb55743e74e261e81998e034` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-source-fiber-singleton-interval-router.json` | `aecc57280136fb8f2bee303ab38ca4ca52c942bc840f17bb2f2c1f6e725a4a76` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_dyadic_source_congruence_router.py` | `8f1fbc0f42e03efdd3ea7b04c619fb4da82a58872e0d0c35bacd2a39db03121e` |
