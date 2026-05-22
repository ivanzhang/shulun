# Prime Matrix Phi-LPF strict-k external bulk square-band partition 证书

**状态：** `strict_k_external_bulk_covered_remaining_forced_to_high_k_square_band`

本层把 `[kP,kP+P]`、`1<k<P` 的 Phi-LPF 端点差分与三个外部输入统一成一个分区账本。
端点差分本身是精确计数；正性来源只能来自外部短区间输入，或来自内部 LPF/平方相位 excess。

```text
N_P(k)=pi((k+1)P-1)-pi(kP).
```

## 1. 外部输入适配

- 有限 sqrt-gap 输入：`kP<=10^18` 的 strict 行已经由已接入的 Lemma 2.7 与小 `x` 审计覆盖。
- Dusart 2010：`x>396738` 时长度 `x/(25 log^2 x)` 可用，在 strict 行中只覆盖 `k<=25 log^2(kP)`。
- Baker--Harman--Pintz 2001：充分大 `x` 时长度 `x^(21/40)` 可用；代入 `x=kP` 得

```text
P >= (kP)^(21/40)  iff  k <= P^(19/21).
```

因此 BHP 能给渐近 bulk 子带，但仍留下 `P^(19/21)<k<P` 的顶端平方边界带。

## 2. 尺度样本

| P scale | finite sqrt k cap | Dusart k cap | BHP k cap | BHP bulk fraction | remaining top fraction |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1000000000 | 999999999 | 23711 | 138949549 | 1.389495e-01 | 8.610505e-01 |
| 1000000000000 | 1000000 | 36351 | 71968567300 | 7.196857e-02 | 9.280314e-01 |
| 1000000000000000000 | 1 | 69143 | 19306977288832504 | 1.930698e-02 | 9.806930e-01 |
| 1000000000000000000000000 | 0 | 111846 | 5179474679231212945408 | 5.179475e-03 | 9.948205e-01 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PhiLPFEndpointDifferenceImportedForAllStrictRows | `true` | `true` | 对 1<k<P，Phi-LPF 端点差分已经给出 N_P(k)=pi((k+1)P-1)-pi(kP) 的精确计数对象。 | positivity source still needed |
| FiniteSqrtInitialSegmentClosed | `true` | `true` | 已接入有限 sqrt-gap 输入：kP<=10^18 的 strict 行由外部有限引理和小 x 直接核查覆盖。 | x>10^18 |
| DusartExplicitLogBandPartitionClosed | `true` | `true` | Dusart 2010 的显式区间可覆盖 k<=25 log^2(kP) 的低 k 带；这是可验证 log-band，不触及顶端平方边界。 | k beyond explicit logarithmic band |
| BHPAsymptoticBulkBandPartitionClosed | `true` | `true` | Baker--Harman--Pintz 的 x^(21/40) 短区间若用于 x=kP，则覆盖 k<=P^(19/21) 的 bulk 子带。 | asymptotic threshold and high-k band |
| RemainingRowsForcedIntoHighKSquareBand | `true` | `true` | 排除有限 sqrt 初段、Dusart log-band 和 BHP bulk 后，任何剩余反例必须满足 x>10^18 且 P^(19/21)<k<P。 | P^(19/21)<k<P, especially top row k=P-1 |
| TopBandConvertedToHalfRoughSemiprimeShadow | `true` | `true` | 顶行 k=P-1 已进一步化为 R_{1/2}(P)>T_{1/2}(P) 的 half-rough semiprime-shadow excess。 | general high-k band still needs analogous excess |
| HighKSquareBandPositivityProved | `false` | `false` | 尚未证明高 k 平方边界带的 Phi-LPF 端点差分恒为正，也未证明 top-row half-rough excess 的全局下界。 | HighKSquareBandPhiLPFExcess OR HalfRoughSurvivorExcessOverReciprocalSemiprimeShadow |
| UnifiedPositiveCoreProved | `false` | `false` | 本层是分区和剩余定位，不是三目标命题的无条件闭合。 | sqrt-scale theorem, high-k structural excess, or semiprime-shadow PDEC exclusion |

## 4. 结论

Phi-LPF 端点差分已经能精确计算 [kP,kP+P] 的素数个数；外部引理路线现在被分成三块：有限 sqrt 初段、Dusart 显式 log-band、BHP 渐近 bulk。它们之后的真剩余不是全域未知，而是 x>10^18 且 P^(19/21)<k<P 的平方边界高 k 带；顶行已经进一步压成 half-rough semiprime-shadow excess。

换言之，继续走外部引理路线必须拿到真正 `sqrt(x)` 尺度且常数不超过 1 的无条件短区间定理；
否则就必须在高 `k` 平方边界带内部证明 Phi-LPF excess，顶行最窄形式就是
`R_{1/2}(P)>T_{1/2}(P)`。

本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它只把真剩余定位到更窄的
高 `k` 平方边界带与 half-rough semiprime-shadow excess。

## 5. 外部来源

| input | source | repository use |
| --- | --- | --- |
| finite sqrt-gap input | https://link.springer.com/article/10.1007/s00208-023-02574-1 Lemma 2.7; uses Oliveira e Silva--Herzog--Pardi prime-gap computation, https://doi.org/10.1090/S0025-5718-2013-02787-1 | closes every strict row with kP<=10^18 |
| Dusart 2010 | https://arxiv.org/abs/1002.0442 | covers k<=25 log^2(kP) |
| Baker--Harman--Pintz 2001 | https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/difference-between-consecutive-primes-ii/2EF13261B3B25458A25F41ED74AA2FC2 | with constant-one exponent arithmetic, covers k<=P^(19/21); threshold is asymptotic, not an explicit finite ledger |

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail-router.json` | `8ab6da3a1ad8bb73f3b4511f503c5914984cfeb1d8b62e05dcb63ce41ea6b381` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.json` | `762c7de91c70ae99628279eb52aa2b5a94185e4d5ed2c32921f08ce6f0133881` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json` | `9c8b4ae328fe2254bf81e16e4f058921efc6c3ea616a97f196a42482151dd028` |
| `docs/monograph/prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow-router.json` | `c5ca8b97bf9f6dc2c5abaec3dd7f4ba612a3996df98696b3b01167e2b076f936` |
