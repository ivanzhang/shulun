# Prime Matrix cycle-debt fresh-modulus 到 tail-sieve 桥接路由器

**状态：** `fresh_modulus_escalation_routed_to_tail_sieve_interface_strict_self_contained_open`

固定有限 ColumnCRT 终端已经被排除后，持久 branch replay 若不在新素数层触发 PDEC/ColumnCRT，就必须把每个 fresh prime 变成一个被禁止的相位条件；这正是 B3 尾段避单余类粗筛对象。因此无界扩模分支被路由到 tail-sieve stability 接口。接受外部或标准 beta-sieve 输入时该尾段分支条件关闭；严格自足路线仍剩 Mertens/PNT/Dusart 尾段内联证明与 fresh-layer PDEC 排斥。

```text
previous_hardpoint=UnboundedFreshModulusEscalationPDECOrTailSieveStabilityContradiction
fresh_modulus_escalation_registered=true
finite_columncrt_terminal_excluded=true
non_pdec_unbounded_fresh_layers_force_tail_rough_object=true
tail_object_interface_closed=true
conditional_external_tail_sieve_closed=true
strict_self_contained_tail_sieve_closed=false
fresh_layer_pdec_excluded=false
row_column_unconditional_closed=false
next_direct_attack_target=FreshLayerPDECColumnCRTExclusionOrSelfContainedTailSieveStabilityClosure
```

## 1. 桥接引理

设持久 replay 在有限登记模数 `Q` 上已经不能终止。任一后续 fresh prime `ell` 满足 `gcd(ell,Q)=1`，因此 `ell` 层是旧 CRT 周期之外的新坐标。若该层不触发 PDEC/ColumnCRT，则反例链在 `ell` 层只能记录一个被禁止的相位；对无界多个 fresh primes 重复此过程，就得到区间 `1<=k<P` 内避开每个素数 `q<=P^0.43` 的一个指定余类的粗筛对象。

该对象与既有 B3 尾段接口一致：对 squarefree `d<P`，CRT 只留下一个模 `d` 的禁余类集合，其计数为 `(P-1)/d` 加不超过 `1` 的端点误差。

## 2. 读数

| item | value |
| --- | ---: |
| registered replay blocks | 6 |
| min first fresh log10 gain | 2.400 |
| min 8-fresh sample log10 gain | 19.435 |
| tail alpha | 0.430000 |
| model main at P=100000 | 4896.256004 |
| 10% surplus over 401 | 88.625600 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FreshModulusEscalationImported | `true` | `true` | 上一证书已证明固定有限 ColumnCRT replay 类不能成为无限反例链的终端稳定结构。 | UnboundedFreshModulusEscalationPDECOrTailSieveStabilityContradiction |
| FiniteColumnCRTTerminalExcluded | `true` | `true` | 有限原子分支已关闭，且固定登记模数在新素数层下必被互素 CRT 坐标继续扩张。 | closed for registered finite terminal classes |
| NonPDECUnboundedFreshLayersForceRoughObject | `true` | `false` | 若每个 fresh layer 都不触发 PDEC/ColumnCRT，则每个新素数层只留下一个被禁止的相位，持久族必须落入一维避单余类粗筛对象。 | one-residue-per-prime tail rough object |
| TailObjectInterfaceMatchedToB3 | `true` | `true` | 该避单余类对象与既有 B3 lower-sieve 账本同口径：squarefree d 的计数为 (P-1)/d 加端点误差。 | B3 lower-sieve rough-object interface |
| ExternalOrStandardTailSieveClosesStabilityBranch | `true` | `false` | 若允许外部显式 Mertens/Dusart 或标准 beta-sieve 输入，tail-sieve stability 分支可条件关闭。 | external/standard beta-sieve input |
| StrictSelfContainedTailSieveStillOpen | `true` | `false` | 严格自足路线不能借用外部筛定理；仍需内联 Mertens/PNT/Dusart 倒素数尾段证明。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| FreshLayerPDECExitStillRequiresExclusion | `false` | `false` | 若 fresh layer 中出现相位复用、投影碰撞、moving support 逃逸或 ColumnCRT 缺陷，还必须给出 PDEC 排斥证书。 | FreshLayerPDECColumnCRTExclusion |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只把无界扩模分支接到尾段筛稳定接口；尚未完成严格自足尾段证明和 fresh-layer PDEC 排斥。 | FreshLayerPDECColumnCRTExclusionOrSelfContainedTailSieveStabilityClosure |

## 4. 剩余基

严格自足 branch-replay 路线：

```text
FreshLayerPDECColumnCRTExclusion AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372
```

接受外部或标准筛输入的 branch-replay 路线：

```text
FreshLayerPDECColumnCRTExclusion
```

继承的全局 strict 剩余基：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本证书不宣称行/列命题已无条件闭合；它只把无界 fresh-modulus 分支压入 tail-sieve/PDEC 双出口。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-ledger.json` | `bfc13d727a480ee6bb358d5f01a826b5e14b0a2bdef7dd8961c4f58c5ba116d9` |
| `docs/monograph/prime-matrix-strict-dynamic-skeleton-tail-b3-bridge-router.json` | `dad9b5f3f5f1d66df613a270f14e4608e99b511c22efa597075061bfc528f55e` |
