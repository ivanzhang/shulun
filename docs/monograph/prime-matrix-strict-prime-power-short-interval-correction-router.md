# Prime Matrix strict 短区间 psi 素数幂修正路由器

**状态：** `prime_power_short_interval_correction_closed_bt_and_node_hash_still_open`

素数幂修正包可以关闭：在 8e11 到 e^28 的百万短区间中，k>=2 的底数投影宽度都小于 1；即使用每个指数预留 2 个命中的保守算法，总权重也只有约 1.84e2，远低于短区间账本中的 20000 预留。因此短区间总包现在实质只剩 Brun-Titchmarsh 素数计数输入和细网格节点余量/hash。

```text
prime_power_short_interval_correction_closed=true
prime_power_total_bound=1.835984147142672e+02
prime_power_reserve=2.000000000000000e+04
prime_power_reserve_margin=1.981640158528573e+04
certified_short_interval_psi_increment_upper_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 指数预算

| k | base_width_at_left | contribution_bound | below_one |
| ---: | ---: | ---: | --- |
| `2` | `5.590168196940795e-01` | `2.800000069143977e+01` | `true` |
| `3` | `3.867989084028522e-03` | `1.866666712762651e+01` | `true` |
| `4` | `2.955441143512871e-04` | `1.400000034571989e+01` | `true` |
| `5` | `6.005619167126497e-05` | `1.120000027657591e+01` | `true` |
| `6` | `2.007274962068095e-05` | `9.333333563813257e+00` | `true` |
| `7` | `8.958868605191128e-06` | `8.000000197554220e+00` | `true` |
| `8` | `4.805139905528222e-06` | `7.000000172859943e+00` | `true` |
| `9` | `2.918991405920224e-06` | `6.222222375875505e+00` | `true` |
| `10` | `1.937397644979910e-06` | `5.600000138287955e+00` | `true` |
| `11` | `1.372828133838766e-06` | `5.090909216625414e+00` | `true` |
| `12` | `1.022474966916320e-06` | `4.666666781906629e+00` | `true` |
| `13` | `7.917511748445349e-07` | `4.307692414067658e+00` | `true` |
| `14` | `6.324154027126383e-07` | `4.000000098777110e+00` | `true` |
| `15` | `5.180334854415491e-07` | `3.733333425525303e+00` | `true` |
| `16` | `4.332443417354170e-07` | `3.500000086429972e+00` | `true` |
| `17` | `3.686740752684159e-07` | `3.294117728404679e+00` | `true` |
| `18` | `3.183611232415728e-07` | `3.111111187937753e+00` | `true` |
| `19` | `2.783777848236468e-07` | `2.947368493835766e+00` | `true` |
| `20` | `2.460561696615571e-07` | `2.800000069143977e+00` | `true` |
| `21` | `2.195352530875994e-07` | `2.666666732518074e+00` | `true` |
| `22` | `1.974861385534155e-07` | `2.545454608312707e+00` | `true` |
| `23` | `1.789400561058585e-07` | `2.434782668820850e+00` | `true` |
| `24` | `1.631776198607326e-07` | `2.333333390953314e+00` | `true` |
| `25` | `1.496557273661381e-07` | `2.240000055315182e+00` | `true` |
| `26` | `1.379582119653833e-07` | `2.153846207033829e+00` | `true` |
| `27` | `1.277618442152573e-07` | `2.074074125291835e+00` | `true` |
| `28` | `1.188124842954608e-07` | `2.000000049388555e+00` | `true` |
| `29` | `1.109080658423522e-07` | `1.931034530444122e+00` | `true` |
| `30` | `1.038862720292855e-07` | `1.866666712762652e+00` | `true` |
| `31` | `9.761548147579902e-08` | `1.806451657512243e+00` | `true` |
| `32` | `9.198803363474894e-08` | `1.750000043214986e+00` | `true` |
| `33` | `8.691515418490781e-08` | `1.696969738875138e+00` | `true` |
| `34` | `8.232309989253395e-08` | `1.647058864202340e+00` | `true` |
| `35` | `7.815018143730867e-08` | `1.600000039510844e+00` | `true` |
| `36` | `7.434446436249686e-08` | `1.555555593968876e+00` | `true` |
| `37` | `7.086195985550603e-08` | `1.513513550888636e+00` | `true` |
| `38` | `6.766519877743349e-08` | `1.473684246917883e+00` | `true` |
| `39` | `6.472209657104600e-08` | `1.435897471355886e+00` | `true` |
| `40` | `6.200504198972112e-08` | `1.400000034571989e+00` | `true` |

## 2. 剩余替换

```text
CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger
  =>
BrunTitchmarshShortIntervalPrimeCountUpperLedger AND MiddlePsiFineMeshNodeSlackFloorAndHashLedger

PrimePowerShortIntervalCorrectionLedger
  =>
closed by elementary prime-power interval budget in this certificate

```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只补 psi 短区间增量中的素数幂误差，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `PrimePowerCorrectionGateActive` | `true` | `true` | 短区间增量账本把 psi 增量拆成素数项和素数幂修正，本步处理 k>=2 的修正。 | PrimePowerShortIntervalCorrectionLedger |
| `ExponentRangeLedger` | `true` | `true` | 在本区间内只需检查 2<=k<=floor(log_2(x_right+h)) 的素数幂。 | none |
| `SubunitBaseWidthLedger` | `true` | `true` | 对每个 k>=2，长度 1e6 的区间投影到 p 变量后的宽度小于 1；保守地每个 k 只预留 2 个命中。 | none |
| `UniformPrimePowerWeightBudgetLedger` | `true` | `true` | 素数幂总权重保守上界约 1.84e2，远小于 20000 预留。 | none |
| `PrimePowerShortIntervalCorrectionLedger` | `true` | `true` | 百万网格每段的素数幂修正被 20000 预留无条件吸收。 | none |
| `CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger` | `false` | `false` | 素数幂包已闭合后，短区间总包还剩 BT 素数计数输入和细网格节点余量/hash。 | BrunTitchmarshShortIntervalPrimeCountUpperLedger AND MiddlePsiFineMeshNodeSlackFloorAndHashLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 素数幂短区间修正不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
BrunTitchmarshShortIntervalPrimeCountUpperLedger
```
