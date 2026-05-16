# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin SparseSAE global envelope router

**状态：** `single_atom_sae_tail_envelope_closed_per_q_multiplicity_open`

本步把 SparseSAE 的真正可求和部分剥离出来：单个固定 AffineTwin 双槽原子的质量为 `1/(q(q-2))`，而奇数尾和满足望远镜恒等式，故所有 `q>=Q` 的单原子包络 `<=1/(2(Q-2))`。当前前沿 `Q=31` 时尾和为 0.017241379310，当前实现质量为 0.001112347052。但 `eta` 稀疏门本身不够推出全局可求和：若每个 q 都允许正比例多原子，总贡献可发散。因此最新硬点被精确压成每 q multiplicity 的 O(1)/衰减界，或 HighDensityEpochPair-PDEC 排斥。

```text
candidate_q_values=[31, 43, 103]
realized_q_values=[31]
universal_single_atom_tail_from_q_ge_5=1/6 ~= 0.166666666667
frontier_single_atom_tail_from_q_ge_31=1/58 ~= 0.017241379310
current_realized_sae_mass=1/899 ~= 0.001112347052
single_atom_sae_tail_envelope_proved=true
eta_sparse_alone_summability_proved=false
row_column_unconditional_closed=false
```

## 1. 望远镜包络

```text
1/(q(q-2)) = (1/2) * (1/(q-2) - 1/q)
sum over odd q >= Q is <= 1/(2(Q-2)).
AffineTwin q values are a subset of these odd q.
```

## 2. 单原子质量

| q | realized | single SAE mass | recorded match | sparse gate |
| ---: | ---: | ---: | ---: | ---: |
| 31 | `true` | `1/899` ~= 0.001112347 | `true` | `true` |
| 43 | `false` | `1/1763` ~= 0.000567215 | `true` | `true` |
| 103 | `false` | `1/10403` ~= 0.000096126 | `true` | `true` |

## 3. 关键边界

- 单原子 SAE 可求和已经闭合；这是全局恒等式，不依赖有限扫描或孪生素数猜想。
- `eta` 稀疏门不能单独闭合全局求和，因为每个 q 的正比例多原子会给出约 `eta` 的贡献。
- 因此真正剩余不是再换命题，而是证明每 q 的 AffineTwin 原子数为 O(1)/有额外衰减，或把超额送入 HighDensityEpochPair-PDEC/ColumnCRT。

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `affine_twin_single_atom_sae_tail_envelope` | `closed` | For odd q>=Q, sum 1/(q(q-2)) is bounded by the telescoping tail 1/(2(Q-2)); affine-twin q values form a subset of these odd q. |
| `eta_sparse_alone_not_global_summability` | `closed_diagnostic` | The eta sparse gate alone permits O(eta q(q-2)) atoms at each q; without a per-q multiplicity/decay bound this does not yield a summable global SAE family. |
| `per_q_multiplicity_or_high_density_pdec` | `open` | A global proof must show O(1) or decaying affine-twin atoms per q, or route excess multiplicity to HighDensityEpochPair-PDEC/ColumnCRT. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SingleAtomSAETailEnvelopeClosed` | `true` | `true` | 单固定双槽原子的 SAE 质量全局可求和，且不依赖孪生素数输入。 | closed |
| `CurrentRealizedSAEWithinFrontierTail` | `true` | `false` | 当前实现质量低于 q>=当前前沿的望远镜尾和。 | finite evidence only |
| `EtaSparseAloneSufficientForGlobalSummability` | `false` | `false` | eta 稀疏本身不足以推出全局可求和；还需要每 q multiplicity 控制。 | AffineTwinPerQMultiplicityBoundOrHighDensityEpochPairPDECExclusion |
| `HighDensityEpochPairPDECRouted` | `true` | `true` | multiplicity 过大时仍回流 HighDensityEpochPair-PDEC/ColumnCRT。 | exclusion still separate |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭单原子求和包络，不关闭全局行/列命题。 | AffineTwinPerQMultiplicityBoundOrHighDensityEpochPairPDECExclusion |

## 6. 下一步

- 主攻：`AffineTwinPerQMultiplicityBoundOrHighDensityEpochPairPDECExclusion`。
- 具体目标：证明每个 q 的 AffineTwin 原子 multiplicity 为 O(1)/衰减；若失败，输出 HighDensityEpochPair-PDEC/ColumnCRT。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_sparse_sae_global_envelope_router.py` | `b381c0aaafae790fae8e97a40895c1a7b9fa462459ce813e6d5cef788238a4a4` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-ledger.json` | `8323447f703d339a1ff63e35f0dcaff4d697b295ea79241f67c23d2ecd5c00d3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-ledger.json` | `18a67505beef2a1ba7ec53a6088bb26da6a3955e2f63c02f5e215cfe171a8063` |
