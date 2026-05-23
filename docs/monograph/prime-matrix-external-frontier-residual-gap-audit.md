# Prime Matrix 外部前沿 residual-gap 审计

**状态**：`residual_gaps_quantified_target_open`
**核验日期**：`2026-05-23`

## 1. 原子结论

- 已发表点态短区间最强可用副产品：Baker--Harman--Pintz 给连续空行串残余指数 `0.05`。
- 前沿预印本近似副产品：Runbo Li v8 若接受可把残余指数压到 `0.04`，仍未到 `theta<=1/2`。
- 列方向最接近方阵的条件输入：Bruna 在 GLH 下给 `q^(2+epsilon)`，仍是条件且超出 strict `P^2`。
- AP 平均分布已经多次越过 `x^1/2`，但共同缺口是固定素模数 `q=P` 的零例外全剩余类转移。
- P2 almost-prime 已进入 `P^2` 方阵，但对象不是素数；这把奇偶屏障定位为真实剩余硬点。

## 2. 最小剩余基

```text
PointwiseShortIntervalPrimeTheoremThetaLeHalf
GridTransferredShortIntervalSecondMomentAtThetaHalf
LinnikExponentLeTwoWithSquareWindowConstants
MeanValueAPToFixedPrimeModulusZeroExceptionTransfer
ConditionalLinnikTwoPlusEpsilonToUnconditionalLinnikLeTwoWithConstants
NonlinearParityBreakingActualSourceConstructor
```

## 3. 残余缺口表

| kind | name | status | residual gate | transformed residual | closes? | note |
|---|---|---|---|---|---|---|
| pointwise_short_interval | Baker-Harman-Pintz 2001 | `published` | `PointwiseShortIntervalPrimeTheoremThetaLeHalf` | theta_gap=0.025; run_exp=0.05 | `false` | 给出已发表点态短区间 side theorem；行串残余指数为 0.05。 |
| pointwise_short_interval | Runbo Li short intervals | `arXiv:2308.04458v8` | `PointwiseShortIntervalPrimeTheoremThetaLeHalf` | theta_gap=0.02; run_exp=0.04 | `false` | 若接受，可把行串残余指数压到 0.04；仍大于 theta=1/2 门槛。 |
| pointwise_short_interval | Guth-Maynard zero-density consequence | `arXiv:2405.20552v2` | `PointwiseShortIntervalPrimeTheoremThetaLeHalf` | theta_gap=0.0666666666667; run_exp=0.133333333333 | `false` | 17/30 技术很强，但换算成行厚度仍是 P^(2/15+o(1))。 |
| pointwise_short_interval | Le Duc Hieu prime APs in short intervals | `arXiv:2509.04883v2` | `PointwiseShortIntervalPrimeTheoremThetaLeHalf` | theta_gap=0.0666666666667; run_exp=0.133333333333 | `false` | 短区间内素数等差数列结构更强，但长度门槛仍未到单行 P。 |
| exceptional_set_to_grid_transfer | Gafni-Tao exceptional short intervals | `arxiv_exceptional_set_interface` | `GridTransferredShortIntervalSecondMomentAtThetaHalf` | grid_transfer=open | `false` | almost-all/exceptional-set 信息不能自动控制所有 P-间隔行端点。 |
| least_prime_ap_linnik | Xylouris general Linnik published scale | `published` | `LinnikExponentLeTwoWithSquareWindowConstants` | L_gap=3; overshoot=P^3 | `false` | 按当前账本记录为 <5 量级；距 P^2 方阵仍差约 P^3。 |
| least_prime_ap_linnik | Meng bounded-cubic-part AP prime | `published_special_prime_modulus_compatible` | `LinnikExponentLeTwoWithSquareWindowConstants` | L_gap=2.5; overshoot=P^2.5 | `false` | 素模数兼容，但首素数高度仍为 P^4.5，距 P^2 差 P^2.5。 |
| conditional_linnik_near_square | Bruna conditional GLH least AP prime | `conditional_arxiv` | `ConditionalLinnikTwoPlusEpsilonToUnconditionalLinnikLeTwoWithConstants` | epsilon plus conditional GLH hypothesis | `false` | GLH 下到 q^(2+epsilon)，是条件近门槛，不是无条件 strict P^2 方阵内闭合。 |
| almost_prime_ap_wrong_object | Li-Zhang-Cai least P2 almost-prime in AP | `arxiv_wrong_parity_object` | `NonlinearParityBreakingActualSourceConstructor` | square_margin=0.1655; wrong_object=P2 | `false` | 指数进入 P^2，但对象是 P2 almost-prime；这正定位奇偶屏障。 |
| average_ap_distribution | Stadlmann smooth-moduli prime AP distribution | `accepted_average_smooth_moduli` | `MeanValueAPToFixedPrimeModulusZeroExceptionTransfer` | modulus_range=P^1.05; fixed_modulus_transfer=open | `false` | 模数范围覆盖 P，但平均/光滑模数结构不能推出固定素模数 P 的零例外全 residue。 |
| average_ap_distribution | Runbo Li smooth-moduli minorant | `arXiv:2505.09629v3` | `MeanValueAPToFixedPrimeModulusZeroExceptionTransfer` | modulus_range=P^1.05263157895; fixed_modulus_transfer=open | `false` | minorant 越过 1/2 后仍是平均光滑模数输入，不是逐列点态正性。 |
| average_ap_distribution | Pascadi weighted prime/smooth distribution | `arXiv:2505.00653v2` | `MeanValueAPToFixedPrimeModulusZeroExceptionTransfer` | modulus_range=P^1.25; fixed_modulus_transfer=open | `false` | 模数范围到 P^(5/4-o(1))，但 weighted mean value 不给固定 P 零例外。 |
| average_ap_distribution | Runbo Li large-moduli AP bilinear | `arXiv:2602.20917v5` | `MeanValueAPToFixedPrimeModulusZeroExceptionTransfer` | modulus_range=P^1.05882352941; fixed_modulus_transfer=open | `false` | q=P 在范围内，但结果仍是结构化平均而非固定素模数全 residue。 |
| average_ap_distribution | Runbo Li large-moduli AP trilinear | `arXiv:2602.20917v5` | `MeanValueAPToFixedPrimeModulusZeroExceptionTransfer` | modulus_range=P^1.0625; fixed_modulus_transfer=open | `false` | q=P 在范围内，但 almost-all/结构化平均不能专化成每列有素数。 |

## 4. 审稿边界

本审计是非循环推进：它把每个外部输入换算成目标窗口中的剩余指数缺口或对象缺口。它不声称外部引理版或内部自足版已经无条件闭合。

```text
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```
