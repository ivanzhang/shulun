# Prime Matrix 逆元零行精确收费剖面路由器

**状态：** `exact_inverse_alignment_zero_row_charge_profile_closed_sibling_numeric_envelope_open`

逆元方程组现在已转成可复核的零行收费剖面：给定假设零行 x，每个小素数 q 给出唯一相位 rho_q(x)，容量 mu_q 与实际列命中数满足精确恒等式。若 x 是零行，则总容量必分解为 P-1 个被覆盖列加 overlap_debt；prefix 残洞再由 tau_z(c) 分桶，每个桶的原始容量正是同一 mu_tau。这说明许多冷兄弟窗口不能当作无来源的抽象分叉，它们必须来自同一行相位源和同一容量/重叠账本。但这一步仍只关闭了解集与收费恒等式；要形成全局矛盾，还需证明这些精确 tau/cold 兄弟收费在同参数下有统一父级 envelope，或者直接证明 x<P 的最小对齐解不可能存在。

```text
exact_zero_row_solution_profile_closed=true
capacity_overlap_identity_closed=true
prefix_tau_sibling_charge_identity_closed=true
sibling_cold_core_threshold_numeric_envelope_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 恒等式

| name | statement | status |
| --- | --- | --- |
| `exact_phase_solution_set` | for fixed P,x, every q<P contributes one phase rho_q(x)=-xP mod q. | `closed` |
| `capacity_hit_identity` | sum_{q<P} mu_q(x;P)=sum_{1<=c<P} #{q<P: c=rho_q(x) mod q}. | `closed` |
| `zero_row_overlap_identity` | if x is a zero row, sum_q mu_q=(P-1)+overlap_debt(x). | `closed` |
| `prefix_tau_sibling_identity` | for z<P, R_{x,z} is partitioned by tau_z(c); each tau bucket has size <= mu_tau. | `closed` |
| `sibling_numeric_envelope` | a uniform parent-level bound for all exact tau/cold sibling families. | `open` |

## 2. 最小零行收费样本

| P | min x | x/P | sum mu | overlap debt | max multiplicity | first-factor histogram |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 13 | 168 | 12.923 | 15 | 3 | 3 | `{2: 6, 3: 2, 5: 2, 7: 1, 11: 1}` |
| 17 | 1210 | 71.176 | 21 | 5 | 4 | `{2: 8, 3: 3, 5: 2, 7: 1, 11: 1, 13: 1}` |
| 19 | 3658 | 192.526 | 26 | 8 | 4 | `{2: 9, 3: 3, 5: 2, 7: 2, 11: 1, 13: 1}` |
| 23 | 58 | 2.522 | 33 | 11 | 3 | `{2: 11, 3: 4, 5: 2, 7: 2, 13: 1, 17: 1, 19: 1}` |
| 29 | 5209 | 179.621 | 44 | 16 | 4 | `{2: 14, 3: 5, 5: 2, 7: 2, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1}` |
| 31 | 60794 | 1961.097 | 46 | 16 | 4 | `{2: 15, 3: 5, 5: 2, 7: 2, 11: 2, 13: 1, 17: 1, 19: 1, 23: 1}` |
| 37 | 73916 | 1997.730 | 56 | 20 | 4 | `{2: 18, 3: 6, 5: 3, 7: 2, 11: 2, 13: 2, 17: 1, 29: 1, 31: 1}` |
| 41 | 170880 | 4167.805 | 63 | 23 | 5 | `{2: 20, 3: 7, 5: 3, 7: 2, 11: 2, 13: 1, 17: 1, 19: 1, 23: 1, 29: 1, 31: 1}` |
| 43 | 162932 | 3789.116 | 67 | 25 | 5 | `{2: 21, 3: 7, 5: 3, 7: 2, 11: 2, 13: 1, 17: 1, 19: 2, 23: 1, 29: 1, 31: 1}` |

## 3. Prefix Tau 兄弟剖面

| P | x | z | R_xz size | M# | tau counts | appeared capacity | charged slack |
| ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| 13 | 168 | 3 | 4 | 2.666667 | `{5: 2, 7: 1, 11: 1}` | 5 | 1 |
| 13 | 168 | 5 | 2 | 2.000000 | `{7: 1, 11: 1}` | 2 | 0 |
| 17 | 1210 | 3 | 5 | 3.166667 | `{5: 2, 7: 1, 11: 1, 13: 1}` | 7 | 2 |
| 17 | 1210 | 4 | 5 | 3.166667 | `{5: 2, 7: 1, 11: 1, 13: 1}` | 7 | 2 |
| 17 | 1210 | 5 | 3 | 2.500000 | `{7: 1, 11: 1, 13: 1}` | 4 | 1 |
| 19 | 3658 | 3 | 6 | 2.666667 | `{5: 2, 7: 2, 11: 1, 13: 1}` | 10 | 4 |
| 19 | 3658 | 4 | 6 | 2.666667 | `{5: 2, 7: 2, 11: 1, 13: 1}` | 10 | 4 |
| 19 | 3658 | 5 | 4 | 2.166667 | `{7: 2, 11: 1, 13: 1}` | 6 | 2 |
| 23 | 58 | 3 | 7 | 3.566667 | `{5: 2, 7: 2, 13: 1, 17: 1, 19: 1}` | 12 | 5 |
| 23 | 58 | 4 | 7 | 3.566667 | `{5: 2, 7: 2, 13: 1, 17: 1, 19: 1}` | 12 | 5 |
| 23 | 58 | 5 | 5 | 3.166667 | `{7: 2, 13: 1, 17: 1, 19: 1}` | 7 | 2 |
| 29 | 5209 | 3 | 9 | 3.233333 | `{5: 2, 7: 2, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1}` | 20 | 11 |
| 29 | 5209 | 4 | 9 | 3.233333 | `{5: 2, 7: 2, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1}` | 20 | 11 |
| 29 | 5209 | 5 | 7 | 2.833333 | `{7: 2, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1}` | 15 | 8 |
| 31 | 60794 | 3 | 10 | 4.000000 | `{5: 2, 7: 2, 11: 2, 13: 1, 17: 1, 19: 1, 23: 1}` | 20 | 10 |
| 31 | 60794 | 4 | 10 | 4.000000 | `{5: 2, 7: 2, 11: 2, 13: 1, 17: 1, 19: 1, 23: 1}` | 20 | 10 |
| 31 | 60794 | 5 | 8 | 3.666667 | `{7: 2, 11: 2, 13: 1, 17: 1, 19: 1, 23: 1}` | 14 | 6 |
| 37 | 73916 | 3 | 12 | 4.595238 | `{5: 3, 7: 2, 11: 2, 13: 2, 17: 1, 29: 1, 31: 1}` | 23 | 11 |
| 37 | 73916 | 4 | 12 | 4.595238 | `{5: 3, 7: 2, 11: 2, 13: 2, 17: 1, 29: 1, 31: 1}` | 23 | 11 |
| 37 | 73916 | 5 | 9 | 4.166667 | `{7: 2, 11: 2, 13: 2, 17: 1, 29: 1, 31: 1}` | 16 | 7 |
| 37 | 73916 | 6 | 9 | 4.166667 | `{7: 2, 11: 2, 13: 2, 17: 1, 29: 1, 31: 1}` | 16 | 7 |
| 41 | 170880 | 3 | 13 | 5.041667 | `{5: 3, 7: 2, 11: 2, 13: 1, 17: 1, 19: 1, 23: 1, 29: 1, 31: 1}` | 29 | 16 |
| 41 | 170880 | 4 | 13 | 5.041667 | `{5: 3, 7: 2, 11: 2, 13: 1, 17: 1, 19: 1, 23: 1, 29: 1, 31: 1}` | 29 | 16 |
| 41 | 170880 | 5 | 10 | 4.666667 | `{7: 2, 11: 2, 13: 1, 17: 1, 19: 1, 23: 1, 29: 1, 31: 1}` | 21 | 11 |
| 41 | 170880 | 6 | 10 | 4.666667 | `{7: 2, 11: 2, 13: 1, 17: 1, 19: 1, 23: 1, 29: 1, 31: 1}` | 21 | 11 |
| 43 | 162932 | 3 | 14 | 5.291667 | `{5: 3, 7: 2, 11: 2, 13: 1, 17: 1, 19: 2, 23: 1, 29: 1, 31: 1}` | 30 | 16 |
| 43 | 162932 | 5 | 11 | 4.916667 | `{7: 2, 11: 2, 13: 1, 17: 1, 19: 2, 23: 1, 29: 1, 31: 1}` | 22 | 11 |
| 43 | 162932 | 6 | 11 | 4.916667 | `{7: 2, 11: 2, 13: 1, 17: 1, 19: 2, 23: 1, 29: 1, 31: 1}` | 22 | 11 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ExactZeroRowSolutionProfileClosed` | `true` | `true` | 具体 P 的零行行号 x 可由逆元 CRT 覆盖系统给出，并生成完整相位剖面。 | uniform proof, not sample computation |
| `CapacityOverlapIdentityClosed` | `true` | `true` | 任何零行都必须把总覆盖容量分解为 P-1 个实际列加重叠债。 | convert overlap debt into hot/fixed/PDEC returns globally |
| `PrefixTauSiblingChargeIdentityClosed` | `true` | `true` | prefix residual 的 tau 兄弟桶与 mu_tau 容量完全同字段匹配。 | SiblingColdCoreThresholdNumericEnvelopeTable |
| `DirectEarlyZeroRowContradictionFound` | `false` | `false` | 精确解集给出强诊断，但尚未从有限样本或恒等式推出全局反例不存在。 | SiblingColdCoreThresholdNumericEnvelopeTable OR PrimeGapBelowP2ForAllPBlocks |
| `SiblingColdCoreNumericEnvelopeProved` | `false` | `false` | 仍需同参数证明父级兄弟预算支配所有精确 tau/cold 兄弟收费。 | SiblingColdCoreThresholdNumericEnvelopeTable |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未同时完成冷兄弟数值 envelope、持久 moving atom 和 DStructure/Rankin 验收。 | SiblingColdCoreThresholdNumericEnvelopeTable AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一步

- 主攻：`ExactInverseAlignmentSiblingChargeUniformEnvelope`。
- 并行保留：
  - `SiblingColdCoreThresholdNumericEnvelopeTable`
  - `PrimeGapBelowP2ForAllPBlocks`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

审稿边界：本步不使用真实零行缺席，不声明全局 `min x>P`，也不声明行/列命题无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/inverse-alignment-covering-system-sample-ledger.json` | `e1a0d939b424b57cf8c1f97c8d0a0e973c3f91896789011e786fa833ade10f9a` |
| `data/inverse-alignment-exact-zero-row-charge-profile-ledger.json` | `c7cabc90437430aee6614b0428662fe0ce67a1eac9a3ee263b5560ef06481db3` |
| `docs/monograph/prime-matrix-inverse-alignment-covering-system-router.json` | `09be6a101dd2775a057577a1ef960270dbd88b03dd5e5cec4d1bddec67eb1acf` |
| `docs/monograph/prime-matrix-inverse-alignment-latest-frontier-sync-router.json` | `ff08e13fd2dbbd7dbbdaf7a1648fc8f339cd2e52eec84a5ba3a0df7873c05d9c` |
| `docs/monograph/prime-matrix-inverse-alignment-prefix-demand-bridge-router.json` | `369bf801b153a8cb792ef4a0971d5156020eb6604c2cdd31808d81cd4770c70a` |
| `docs/monograph/prime-matrix-strict-cold-window-sibling-charging-router.json` | `be05fb4b2dee03515ca4eea8e086eff6341c0e04d69da9501072cccf74414591` |
| `docs/monograph/prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json` | `c2ef211342a04f992f35f62a595d3c1647663d1a9fde5d1e78ff57c735bf63d6` |
| `experiments/prime_matrix_inverse_alignment_exact_zero_row_charge_profile_router.py` | `73f5b8d588c01e02b1c4ea14b6d2c182b27a27eb66b3f2a8b727aa1732e59721` |
