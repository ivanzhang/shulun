# Prime Matrix Phi-LPF strict-k finite sqrt square-phase tail 证书

**状态：** `finite_sqrt_gap_initial_segment_closed_tail_routed_to_square_phase_full_cover`

本层把 Phi-LPF strict 行的端点差分接入一个已发表的有限 sqrt-gap 输入：
若 `x=kP` 且 `1<k<P`，则 `sqrt(x)<P`。所以只要 `[x,x+sqrt(x)]`
内有素数，便自动得到

```text
N_P(k)=pi((k+1)P-1)-pi(kP)>=1.
```

Erdos--Harcos--Kharel--Maga--Mezei--Toroczkai 的 Lemma 2.7 给出
`117<=x<=10^18` 时 `[x,x+sqrt(x)]` 有素数；阈值以下的 strict 行由
直接有限核查覆盖。因此可能的 strict 反例必须进入 `x>10^18` 的无限尾段。

## 1. 有限 sqrt-gap 桥

```text
external_range=[117, 1000000000000000000]
small_direct_x_limit=116
small_checked_row_count=49
all_small_rows_positive=true
minimum_small_row_prime_count=1
```

顶行 `x=P^2-P` 的有限覆盖达到：

```text
top_row_integer_base_bound=1000000000
largest_prime_base_with_top_row_start_le_x_max=999999937
top_row_start_at_largest_prime_base=999999873000004032
```

这只清掉巨大有限初段；`P>999999937`
的顶行尾段仍未由外部有限计算处理。

## 2. 平方相位尾段等价

顶行失败等价于：

```text
N_top(P)=0
iff for every 1<=r<P, gcd(P^2-r, product_{q<P} q)>1
iff [1,P-1] is covered by residue classes r == P^2 mod q, q<P.
```

也就是说，prime-indexed Oppermann-left 的尾段失败不是新的计数误差，而是
`P^2` 特殊相位启动的长度 `P-1` 低筛全覆盖块。它应进入：

```text
SquarePhaseTailLongBlockPDECExclusion
OR SquarePhaseRoughSurvivorUniformLowerBound
OR genuine sqrt-scale theorem beyond 10^18.
```

## 3. 顶行低筛覆盖样本

| P | interval | slots | prime count | first prime | full cover | owner counts |
| ---: | --- | ---: | ---: | ---: | --- | --- |
| 5 | 21..24 | 4 | 1 | 23 | `false` | 2:2, 3:1 |
| 11 | 111..120 | 10 | 1 | 113 | `false` | 2:5, 3:2, 5:1, 7:1 |
| 17 | 273..288 | 16 | 3 | 283 | `false` | 2:8, 3:3, 5:1, 7:1 |
| 101 | 10101..10200 | 100 | 12 | 10193 | `false` | 2:50, 3:17, 5:7, 7:4, 11:2, 13:1, 17:1, 23:1, 29:1, 53:1, 61:1, 67:1, 73:1 |
| 257 | 65793..66048 | 256 | 23 | 66047 | `false` | 2:128, 3:43, 5:17, 7:10, 11:5, 13:3, 17:2, 19:4, 23:2, 29:2, 31:1, 37:1, 41:2, 43:1, 59:1, 67:1, 71:1, 101:1, 103:1, 107:1, 131:1, 149:1, 199:1, 211:1, 233:1, 251:1 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FiniteSqrtGapBridgeCriterionClosed | `true` | `true` | 对 x=kP 且 1<k<P，有 sqrt(x)<P；因此 [x,x+sqrt(x)] 内有素数会推出 strict 行正性。 | criterion only |
| PublishedFiniteSqrtGapClosesInitialSegment | `true` | `true` | 外部 Lemma 2.7 给出 117<=x<=10^18 时 [x,x+sqrt(x)] 有素数，阈值以下 strict 行由直接有限核查覆盖。 | x>10^18 tail |
| PrimeIndexedTopRowFiniteReachIdentified | `true` | `true` | 顶行 x=P^2-P 的外部有限覆盖达到 P<=999999937；这清掉巨大有限初段但不触及无限尾段。 | prime bases P>999999937 |
| TopRowFailureEquivalentToMinusSquarePhaseFullCover | `true` | `true` | N_top(P)=0 等价于每个 r=1..P-1 都满足 P^2-r 被某个 q<P 整除，即 r==P^2 mod q 的低筛禁类全覆盖。 | exclude special-phase full cover |
| FiniteBridgePlusGenericGapTheoremsCloseInfiniteTail | `false` | `false` | Dusart/BHP 等通用输入在 x>10^18 的 sqrt-edge 仍长于 P 或只覆盖低 k 子带。 | sqrt-scale theorem or structural square-phase proof |
| UnifiedPositiveCoreProved | `false` | `false` | 本层只清理有限初段并把尾段反例锁到平方相位长覆盖块；没有证明所有 P,k 的正性。 | SquarePhaseTailLongBlockPDECExclusion OR SquarePhaseRoughSurvivorUniformLowerBound |

## 5. 结论

Phi-LPF 端点差分现在与一个审稿级有限 sqrt-gap 输入接牢：所有 `kP<=10^18`
的 strict 行正性可由外部有限定理加极小初段核查覆盖。剩余不是有限验证缺口，
而是无限尾段的结构问题。最坏顶行尾段精确化为：

```text
P>999999937 and [1,P-1] fully covered by r == P^2 mod q for primes q<P.
```

这一步仍不证明 `UnifiedPositiveCore`。它把当前真剩余收缩为平方相位特殊长块的
PDEC/rough-survivor 排斥，或一个真正的 `sqrt(x)` 尺度无条件短区间定理。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-unified-positive-core-router.json` | `f203a0d971a15e543b30bf22eb2bfea0b62524939af19781cf0ae23d4b92446d` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-oppermann-alignment-router.json` | `3ebb0f9350f9f3fd7b67ef5b4bf6d3cc407462439520a5e06e4a810b6f208489` |
| `docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.json` | `328ee462d76cb6213f976eee33133885f20109157d16cf80d236ae27d78d8993` |
| `docs/monograph/prime-matrix-primorial-jacobsthal-central-block-router.json` | `35ae489251780714fd8168bb39108b636a4882d967acd642f4c24a6a046fbcfb` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.json` | `762c7de91c70ae99628279eb52aa2b5a94185e4d5ed2c32921f08ce6f0133881` |
