# Prime Matrix localized P-CRT transfer / Linnik=2 屏障路由

**状态：** `localized_pcrt_transfer_reduced_to_pointwise_linnik2_ap_or_structural_frontier_open`

`LocalizedPCRTColumnUniformityTransferToInitialPxPSquare` 的列侧内容已经压成精确的点态 AP 屏障：对每个非零 `c mod P`，必须证明存在素数 `ell<=P^2` 且 `ell≡c mod P`。这正是 prime-modulus 的 Linnik 指数 2 型断言。完整 P-wheel 的 CRT 非 P 列均匀性只是全周期平均恒等式，不能提供每个初始短 AP 的首素数位置；BV/平均均匀性也只给几乎所有列。因此该路线若不引入新的点态 AP 定理，就必须回流到 PDEC same-set scope 或 signed payload/ExactUV 前沿。行/列命题仍未无条件闭合。

```text
localized_pcrt_transfer_active=true
column_occupancy_equivalent_to_least_prime_ap=true
linnik2_barrier_identified=true
localized_transfer_current_corpus_proved=false
pointwise_linnik2_ap_theorem_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2
```

## 1. 等价链

| from | to |
| --- | --- |
| `LocalizedPCRTColumnUniformityTransferToInitialPxPSquare` | `initial-square non-P column occupancy` |
| `initial-square non-P column occupancy` | `PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2` |
| `PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2` | `prime-modulus pointwise least-prime-in-AP exponent 2` |
| `pure complete P-wheel CRT identity` | `global average only; no pointwise short AP localization` |
| `failure to prove L2_AP internally` | `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn` |

## 2. 有限 AP 样本（P <= 3000）

- 检查素数模数：`429`。
- 缺失剩余类总数：`0`。
- 最大首素数行号：`108`。

| P | worst residue | first prime | row index | row/P | missing classes | mean first row |
| --- | --- | --- | --- | --- | --- | --- |
| 2861 | 1524 | 307651 | 108 | 0.0377 | 0 | 7.763 |
| 2129 | 1014 | 220301 | 104 | 0.0488 | 0 | 7.359 |
| 2749 | 1337 | 265241 | 97 | 0.0353 | 0 | 7.699 |
| 2857 | 734 | 255007 | 90 | 0.0315 | 0 | 7.825 |
| 2539 | 162 | 226133 | 90 | 0.0354 | 0 | 7.564 |
| 1847 | 1140 | 165523 | 90 | 0.0487 | 0 | 7.223 |
| 2659 | 789 | 234781 | 89 | 0.0335 | 0 | 7.659 |
| 1531 | 1174 | 134371 | 88 | 0.0575 | 0 | 7.191 |
| 2237 | 1159 | 189067 | 85 | 0.0380 | 0 | 7.349 |
| 2953 | 2448 | 247547 | 84 | 0.0284 | 0 | 7.731 |
| 2789 | 2452 | 233939 | 84 | 0.0301 | 0 | 7.679 |
| 2887 | 2809 | 239543 | 83 | 0.0287 | 0 | 7.714 |

样本只用于定位风险形态；证明不依赖经验无反例。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LocalizedPCRTTransferActive` | `true` | `false` | 上一层把前素数间隙/P-wheel 均匀性路线压到初始方阵局部化转移。 | LocalizedPCRTColumnUniformityTransferToInitialPxPSquare |
| `ColumnOccupancyEquivalentToLeastPrimeAP` | `true` | `true` | 非 P 列 c 有素数等价于存在素数 ell<=P^2 且 ell=c mod P。 | PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2 |
| `Linnik2BarrierIdentified` | `true` | `true` | 对所有非零 c mod P 证明 ell<=P^2 是 prime-modulus 点态最小 AP 素数指数 2。 | new pointwise AP theorem required |
| `CompleteCRTUniformityOnlyAverage` | `true` | `true` | 完整 P-wheel 非 P 列等量是全周期平均恒等式，不含短 AP 点态首素数信息。 | LocalizedPCRTColumnUniformityTransferToInitialPxPSquare or PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2 |
| `BVOrMeanAPInsufficientForPointwiseAllColumns` | `true` | `true` | 平均 AP 均匀性最多控制几乎所有列；目标要求每一列，不能留下单个异常类。 | pointwise capacity lower bound or new AP input |
| `LocalizedTransferCurrentCorpusProved` | `false` | `false` | 当前语料没有从完整 CRT 周期均匀性推出每个初始短 AP 均命中的定理。 | PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2 |
| `SignedPayloadFrontierStillActive` | `true` | `false` | 若不引入外部 AP 定理，结构路线仍需 signed payload 正向构造。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `PDECScopeStillOpen` | `true` | `false` | PDEC same-set 作用域仍是可提交的新证书入口，但当前未证。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步把局部化转移压成点态 AP/Linnik=2 屏障，尚未给出全局无条件矛盾。 | (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明 Linnik=2 型点态 AP 定理，也没有证明 PDEC scope、signed payload、ExactUV、模型余量、RatePreservation 或 DStructure/Rankin。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-predecessor-gap-pcrt-uniformity-router.json` | `8569aefb62fc30395f527b8aaa3966bab18e6a0dfd5ed1d6dffb83a9acde57d6` |
| `docs/monograph/prime-matrix-global-crt-signed-payload-sync-router.json` | `969459391db184ef4250b42c88f9947e1884ac92523320b47f887f729e8c6c56` |
| `docs/monograph/prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json` | `3c7602bf11d29d837d1a05964368f085de2c10dc5e786bd518b55a85b4ce3cbf` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
