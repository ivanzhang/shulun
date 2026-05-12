# Prime Matrix strict Meissel-Mertens B1 区间自足证书

**状态：** `meissel_mertens_b1_interval_self_contained_closed`

Meissel-Mertens B1 常数区间可用绝对收敛 Euler product 自足闭合：`gamma` 由 Euler-Maclaurin 调和数区间给出，素数有限和求到 `10^6`，尾项用 `1/N` 夹住。所得 B1 区间半径小于 `2e-6`，并覆盖外部参考值 `0.2614972128476428`。这关闭的是 B1 常数区间输入；行/列命题仍需终端侧 PDEC/CleanKLS、RatePreservation 与 DStructure 门。

```text
direct_internal_dusart_theta_pnt_envelope_closed=true
meissel_mertens_b1_interval_self_contained_closed=true
self_contained_meissel_mertens_constant_interval_closed=true
self_contained_mertens_tail_closed=false
row_column_unconditional_closed=false
```

## 1. B1 区间

| item | value |
| --- | ---: |
| prime sum limit | `1000000` |
| gamma lower | `0.577215664901532860606512` |
| gamma upper | `0.577215664901532860606512` |
| finite prime sum | `-0.315718418166032727929251` |
| tail bound abs | `0.000001000000000000000000` |
| B1 lower | `0.261496246735500132677261` |
| B1 upper | `0.261497246735500132677261` |
| B1 midpoint | `0.261496746735500132677261` |
| B1 radius | `0.000000500000000000000000` |
| external reference inside | `true` |

## 2. x=20000 基点

| item | value |
| --- | ---: |
| prime count <=20000 | `2262` |
| sum p<=20000 1/p | `2.554934231171774585658560` |
| error lower | `0.000550011297115788014601` |
| error upper | `0.000551011297115788014601` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只补 B3/Mertens 解析输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `MeisselMertensIntervalGateActive` | `true` | `true` | theta/PNT 包移出后，速率尾段解析剩余收窄到 Meissel-Mertens B1 常数区间。 | SelfContainedMeisselMertensConstantIntervalLedgerAt20000 |
| `ThetaPNTEnvelopeAlreadySelfContained` | `true` | `true` | P5.1 自足同步已经给出 theta(x)-x<x/36260，B1 证书不再承担 theta/PNT。 | DirectInternalDusartThetaPNTEnvelopeLedger |
| `EulerGammaIntervalClosed` | `true` | `true` | Euler-Maclaurin 调和数公式给出 gamma 的窄区间。 | closed |
| `PrimeEulerProductFiniteSumClosed` | `true` | `true` | 有限素数和 sum_{p<=1e6}(log(1-1/p)+1/p) 已用 Decimal 高精度计算并加保护项。 | closed |
| `PrimeEulerProductTailBoundClosed` | `true` | `true` | 尾项由绝对收敛级数控制，宽度不超过 1/N。 | closed |
| `SelfContainedMeisselMertensB1IntervalArithmeticLedger` | `true` | `true` | B1 被夹在半径小于 2e-6 的自足区间内，并覆盖外部参考值。 | closed |
| `SelfContainedMeisselMertensConstantIntervalLedgerAt20000` | `true` | `true` | B1 区间与 x=20000 基点有限核验闭合后，Meissel-Mertens 常数区间输入关闭。 | SelfContainedPrimeReciprocalMertensTailXGe20000 |
| `ExternalB1ReferenceOnlyAsAudit` | `true` | `false` | 外部 B1/Dusart 口径只作为审计对照；闭合判定使用本步 Euler-product 区间。 | not used as proof input |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步关闭常数区间输入，不产生早期零行反例链终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
```
