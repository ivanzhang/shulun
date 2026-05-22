# Prime Matrix Phi-LPF strict k external gap bridge 证书

**状态：** `external_gap_lemmas_screened_against_strict_k_interval`

设 `x=kP`。目标区间为 `[kP,kP+P]`，内部槽长度为 `P-1`。
任一外部短区间引理若保证 `[x,x+H(x)]` 内有素数，则在 strict 行中可用的充要桥接条件是：

```text
H(kP) <= P = x/k.
```

## 1. 外部引理筛查

- Dusart 2010: `x>396738` 时 `[x,x+x/(25 log^2 x)]` 有素数，桥接条件为 `k<=25 log^2(kP)`。
- Baker-Harman-Pintz 2001: 充分大 `x` 时 `[x,x+x^0.525]` 有素数，桥接条件为 `k<=x^0.475`。

strict 条件只给 `k<P`，即 `k<sqrt(x)`。所以 BHP 的 `0.475` 指数仍低于最坏边界 `0.5`，
Dusart 的显式相对界只覆盖对数宽的低 `k` 子带。

## 2. 边界样本

| P | k | P/sqrt(x) | Dusart H/P | Dusart covers | BHP H/P | BHP covers |
| ---: | ---: | ---: | ---: | --- | ---: | --- |
| 101 | 100 | 1.004987562 | 0.047051 | `false` | 1.252989 | `false` |
| 1009 | 1008 | 1.000495909 | 0.210728 | `true` | 1.412435 | `false` |
| 10007 | 10006 | 1.000049969 | 1.179364 | `false` | 1.584865 | `false` |
| 1000003 | 1000002 | 1.000000500 | 52.392224 | `false` | 1.995262 | `false` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PhiLPFDualWindowValueImported | `true` | `true` | 上一层已把 strict 行素数个数写成 N_P(k)=(P-1)-B_P(k)-S_P(k)。 | dual value imported |
| ExternalIntervalLemmaBridgeCriterionClosed | `true` | `true` | 任一外部引理 prime in [x,x+H(x)] 可用于 x=kP 当且仅当 H(kP)<=P。 | bridge criterion |
| Dusart2010CoversLogBandOnly | `true` | `true` | Dusart 的显式区间给 H=x/(25 log^2 x)，只覆盖 k<=25 log^2(kP) 的子带。 | k beyond logarithmic band |
| BakerHarmanPintzCoversExponent0475BandOnly | `true` | `true` | BHP 的 x^0.525 区间只覆盖 k<=x^0.475；strict 边界允许 k 接近 x^0.5。 | sqrt-edge band |
| KnownExternalGapBoundsCloseAllStrictRows | `false` | `false` | 当前接入的无条件外部短区间引理不能覆盖 k≈P≈sqrt(x) 的最坏边界。 | sqrt-scale or dual-window anti-tiling input |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层明确外部引理的可用范围，没有证明 strict 行正性。 | DualWindowAntiTilingInequality OR SqrtGapInputAfterX |

## 4. 结论

外部短区间引理可精确桥接到 Phi-LPF strict 行：只要 H(kP)<=P，端点差 N_P(k) 就为正。Dusart 2010 给显式 log-band，BHP 2001 给指数 0.475 的 k-band；二者都不能覆盖 k 接近 P 的 sqrt-edge。因此当前真剩余是 sqrt-scale 输入或内部双窗口反铺满不等式。

这不是负结论，而是精确定位：若继续走外部引理路线，需要 Legendre 强度的
`H(x)<=sqrt(x)` 右侧短区间输入并配合有限验证；否则必须从 Phi-LPF 双窗口
`B_P(k)+S_P(k)<=P-2` 的内部反铺满结构突破。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-smooth-owner-quotient-window-router.json` | `d5ab5fc9084b7382ee7ed2c1319a1c012394742d413e24d32d826f8e3a9f04e7` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-beatty-euclidean-source-window-router.json` | `c6fbac529d47b04093d14185381cf071de813a9182a00fa03a8dcc92689bf2c6` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value-router.json` | `eed9e255475862b421b6591d3b431a111368cf67d9e75c52bf67ba600c7d9409` |
