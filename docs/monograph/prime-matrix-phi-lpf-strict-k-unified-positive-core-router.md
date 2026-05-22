# Prime Matrix Phi-LPF strict k unified positive core 证书

**状态：** `strict_k_positive_core_unified_across_dual_owner_rejection_gap_coordinates`

本层把当前三个硬点同步成同一个整数。对 `1<k<P`，令

```text
N_P(k)=pi((k+1)P-1)-pi(kP).
```

则已有四个坐标完全一致：

```text
N_P(k)=(P-1)-B_P(k)-S_P(k)
      =(P-1)-OwnerMass
      =RejectionMass-(RawTotal-(P-1)).
N_P(k)>=1 iff next_prime(kP)<(k+1)P.
```

## 1. 有限审计

```text
max_prime=257
strict_row_count=6228
all_four_coordinate_identities_hold=true
minimum_positive_core_value=1
finite_evidence_not_used_as_global_proof=true
```

最小正性核心样本：

```text
P=3, k=2, N=1, offset=-; P=5, k=4, N=1, offset=-; P=7, k=3, N=1, offset=-; P=11, k=10, N=1, offset=-; P=13, k=9, N=1, offset=-; P=17, k=12, N=1, offset=-; P=19, k=15, N=1, offset=-
```

最大 next-prime offset 样本：

```text
P=233, k=186, N=15, offset=53
```

## 2. 样本行

| P | k | N | dual | owner defect | rejection excess | next offset | B | S |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 11 | 10 | 1 | 1 | 1 | 1 | 3 | 7 | 2 |
| 59 | 42 | 3 | 3 | 3 | 3 | 25 | 40 | 15 |
| 101 | 100 | 12 | 12 | 12 | 12 | 3 | 60 | 28 |
| 571 | 438 | 27 | 27 | 27 | 27 | 11 | 382 | 161 |
| 1009 | 1008 | 70 | 70 | 70 | 70 | 5 | 670 | 268 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FourCoordinateCoreIdentityClosed | `true` | `true` | dual-window value、owner defect、raw/rejection excess 与 next-prime row opening 是同一个整数 N_P(k)。 | unified positive core |
| FalseIndependentHardpointsRemoved | `true` | `true` | DualWindowAntiTiling、PositiveRejectionExcess 与 SqrtGapInput 不是三个独立缺口，而是同一正性核心的不同坐标。 | single core |
| FiniteAuditAllCoordinatesAgree | `true` | `true` | 有限审计确认四坐标读数一致，但不作为全局证明。 | finite audit only |
| UnifiedPositiveCoreProved | `false` | `false` | 本层没有证明 N_P(k)>=1；它只消除接口分裂。 | prove the unified core |
| RowColumnUnconditionalClosureReached | `false` | `false` | strict 行正性仍需 sqrt-scale gap 输入或内部双窗口反铺满。 | SqrtGapInputAfterX OR DualWindowAntiTilingInequality |

## 4. 结论

当前 strict-k 前沿的多个名字已经统一为同一个正性核心。证明 DualWindowAntiTiling、PositiveRejectionExcess 或 SqrtGapInput 中任一项，本质上都是证明同一个整数 N_P(k) 为正。非循环路线不应继续把这些名字当作互相独立的逃逸口；下一步必须直接证明统一核心，或输入平方根尺度短区间定理。

本层不是无条件证明；它的作用是把当前真剩余精确压成单核：

```text
UnifiedPositiveCore: N_P(k)>=1 for every prime P and every 1<k<P.
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-smooth-owner-quotient-window-router.json` | `d5ab5fc9084b7382ee7ed2c1319a1c012394742d413e24d32d826f8e3a9f04e7` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.json` | `762c7de91c70ae99628279eb52aa2b5a94185e4d5ed2c32921f08ce6f0133881` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json` | `f825d0e5df9740a53392e3dc0821ca50208291280e33fe9e9ab04e878a70ab3b` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json` | `59bf235653fb8aef057ba81b7e3e42132d7b8bf1b15283671e52330a9cb6ad0d` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.json` | `d0b1755f1ba90db1c954b73254aad74aef846825e80dc38b7a128638e7550b6c` |
