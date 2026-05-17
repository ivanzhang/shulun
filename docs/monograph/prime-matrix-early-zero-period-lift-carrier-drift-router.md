# 早期零行 CRT 周期提升与载体端点漂移路由

**状态：** `period_lift_carrier_drift_routed_not_global_proof`

零行覆盖相位确实按行周期 L_P=prod_{q<P}q 精确提升；但相邻素数载体端点不随 P*L_P 作 CRT 平移。这个不对称不会单独给出矛盾，只能三分流：持久漂移模式是 PDEC/ColumnCRT，孤立漂移是 SAE，非周期端点漂移回到 H3-DSB/KLS 的 NC-BLK 或外部 DI/BFI 分支。

```text
previous_hardpoint=EarlyZeroGapCarrierAsymmetryRoutedToH3DSBNCBLKOrExternalDIBFI;GlobalFinalInputsStillOpen
zero_row_period_lift_exact=true
carrier_endpoint_periodic_translation_forced=false
all_sample_lifts_zero=true
sample_endpoint_translate_match_total_after_t0=1
persistent_drift_routes_to_pdec_columncrt=true
sparse_drift_routes_to_sae=true
nonperiodic_drift_routes_to_h3_dsb=true
row_column_unconditional_closed=false
next_direct_attack_target=PeriodLiftCarrierDriftRoutedToPersistentPDECOrSparseSAEOrH3DSBNCBLK;GlobalFinalInputsStillOpen
```

## 1. 周期提升引理

令

\[
L_P=\prod_{q<P,\ q\ prime}q.
\]

若 `x` 是 `P` 的零行乘数，即对每个 `1<=c<P` 存在 `q<P` 使 `q|Px+c`，则对任意整数 `t>=0`，

\[
P(x+tL_P)+c\equiv Px+c\pmod q.
\]

因此 `x+tL_P` 仍为零行乘数。这是反例覆盖链在 CRT 行周期中的精确复现。

## 2. 端点漂移不随周期提升

设提升后的零行区间为

\[
I_t=[P(x+tL_P)+1,\ P(x+tL_P)+P].
\]

令 `a_t,b_t` 为跨越 `I_t` 的左右最近素数。零行周期性只保证 `I_t` 内没有素数；它不保证

\[
a_t=a_0+tPL_P,\qquad b_t=b_0+tPL_P.
\]

所以周期复制的是小素因子覆盖，不是相邻素数端点。这正是 `P,k` 行周期中的全局非对称。

## 3. 样本审计

- `lift_steps`: `12`。
- `all_sample_lifts_zero`: `true`。
- `sample_endpoint_translate_match_total_after_t0`: `1`。

| P | x0 | L_P | P*L_P | all lifts zero | endpoint translate matches after t0 | distinct slack pairs | gap range |
| ---: | ---: | ---: | ---: | --- | ---: | ---: | --- |
| 13 | 168 | 2310 | 30030 | `true` | 0 | 11 | `[20, 52]` |
| 17 | 1210 | 30030 | 510510 | `true` | 1 | 10 | `[22, 40]` |
| 19 | 3658 | 510510 | 9699690 | `true` | 0 | 12 | `[24, 126]` |
| 23 | 58 | 9699690 | 223092870 | `true` | 0 | 12 | `[34, 76]` |

首个样本的提升端点摘录：

| t | interval | left_prime | right_prime | gap | left_slack | right_slack |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 0 | `[2185, 2197]` | 2179 | 2203 | 24 | 6 | 6 |
| 1 | `[32215, 32227]` | 32213 | 32233 | 20 | 2 | 6 |
| 2 | `[62245, 62257]` | 62233 | 62273 | 40 | 12 | 16 |
| 3 | `[92275, 92287]` | 92269 | 92297 | 28 | 6 | 10 |
| 4 | `[122305, 122317]` | 122299 | 122321 | 22 | 6 | 4 |
| 5 | `[152335, 152347]` | 152311 | 152363 | 52 | 24 | 16 |
| 6 | `[182365, 182377]` | 182353 | 182387 | 34 | 12 | 10 |
| 7 | `[212395, 212407]` | 212383 | 212411 | 28 | 12 | 4 |

## 4. 三分流

| carrier drift behavior | route | reason |
| --- | --- | --- |
| 固定有限相位持久复现 | `PDEC/ColumnCRT` | 端点 slack、列位移或低模频率成为同一 formal unit 的重复缺陷。 |
| 只在孤立周期步出现 | `SAE` | 单窗逃逸不能支撑无限反例链。 |
| 端点非周期漂移但覆盖压力持续 | `H3-DSB/KLS -> NC-BLK or external DI/BFI` | 剩余必须由尾补洞/短窗口 Kloosterman dispersion 控制。 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ZeroRowPeriodLiftExact | `true` | `true` | 若 x 是 P 零行，则 x+t*prod_{q<P}q 仍由同一批小素数覆盖，行覆盖相位精确周期提升。 | closed |
| CarrierEndpointTranslateNotForced | `true` | `true` | 相邻素数载体端点不受该 CRT 周期控制；端点平移匹配不是零行周期性的推论。 | closed |
| SampleCarrierDriftVerified | `true` | `true` | 已登记零行样本的周期提升全部保持零行覆盖；端点 slack/gap 大量漂移，少数偶然平移不由 CRT 覆盖周期强制。 | finite audit only |
| PersistentDriftPatternRoutesToPDECColumnCRT | `true` | `true` | 若端点漂移模式在固定有限相位中持久重复，则它正是 ColumnCRT/PDEC formal unit。 | closed as router |
| SparseDriftPatternRoutesToSAE | `true` | `true` | 若漂移只在孤立周期步出现，则是 SAE 单窗逃逸。 | closed as router |
| NonperiodicDriftRoutesToH3DSB | `true` | `true` | 若覆盖周期持续而素数端点非周期漂移，则必须由 H3 尾补洞/DSB/KLS/NC-BLK 控制。 | H3-DSB-NCBLK |
| GlobalContradictionFromPeriodLiftAlone | `false` | `false` | 周期提升只制造无限复现的复合短块；这本身与素数分布不矛盾，必须再排斥端点漂移分支。 | needs PDEC/SAE/H3-DSB closure |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步关闭的是 P,k CRT 周期不对称的精确路由，不关闭完整行/列无条件命题。 | PeriodLiftCarrierDriftRoutedToPersistentPDECOrSparseSAEOrH3DSBNCBLK;GlobalFinalInputsStillOpen |

## 6. 最新剩余

```text
PeriodLiftCarrierDriftRoutedToPersistentPDECOrSparseSAEOrH3DSBNCBLK;GlobalFinalInputsStillOpen
```

本证书不关闭全局行/列命题；它只把 `P,k` 行 CRT 周期重复后的端点非对称压成命名三分流。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-early-zero-gap-crt-asymmetry-router.json` | `9f10be0a0445eef5185d4e9d03dab884b330a0ae06b9ff9c7a0ffb910086a804` |
| `docs/monograph/prime-matrix-zero-row-full-crt-diagonal-minrep.md` | `8fed996d49bd3da39370eb919cac7601759d12152d44d2a39854f3fd236515ab` |
| `docs/monograph/prime-matrix-h3-tail-filler-rigidity-hardcore.md` | `06249e3e3a114246526246970f6f8e2588c144021103f5568ef53102325aea10` |
| `docs/monograph/prime-matrix-h3-dsb-hlc-blk-energy-core-obstruction.md` | `c424b1aed6378b1e476c86e238dfe7e02cf59f983efffcb6a8b9b7bf18715ca7` |
