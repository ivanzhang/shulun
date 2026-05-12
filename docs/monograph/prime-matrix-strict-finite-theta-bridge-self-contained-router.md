# Prime Matrix strict 有限 theta 桥自足路由器

**状态：** `finite_theta_bridge_and_anchor_self_contained_closed_global_theta_contour_open`

有限 theta 桥可以自足闭合：因为 `vartheta(x)-(1+1/36260)x` 在相邻素数之间严格递减，只需扫描 `p<=20000` 的素数点。高精度证书显示最坏点为 `p=3`，仍有约 `1.208` 的负余量；`x=20000` 处 `vartheta(20000)-20000≈-194.69`，远小于允许值 `20000/36260≈0.5516`。这关闭的是锚点和阈值以下有限桥，不关闭 `x>=20000` 的内部 theta/PNT contour 包络。

```text
theta_target_at_20000_self_contained_closed=true
finite_theta_bridge_below_20000_self_contained_closed=true
internal_dusart_global_theta_envelope_closed=false
internal_zero_free_region_to_theta_contour_closed=false
self_contained_mertens_tail_closed=false
b3_tv_strict_self_contained_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 有限核验

| item | value |
| --- | ---: |
| anchor x | `20000` |
| prime count | `2262` |
| last prime | `19997` |
| theta(anchor) | `19805.309624307867332892257521075951802404856781984847615829414541837246924851674` |
| theta(anchor)-anchor | `-194.690375692132667107742478924048197595143218015152384170585458162753075148326` |
| target allowance | `0.55157198014340871483728626585769442912300055157198014340871483728626585769442912` |
| anchor gap | `-195.24194767227607582257976518990589202426621856672436431399417300003934100602043` |
| max gap prime | `3` |
| max finite bridge gap | `-1.2083232665689665104947482345591763814413777578997310911661369640947050246903504` |
| finite bridge margin | `1.2083232665689665104947482345591763814413777578997310911661369640947050246903504` |

证明化简：

对任意相邻素数区间 [p_k,p_{k+1})，vartheta(x) 常值而 vartheta(x)-(1+1/36260)x 严格递减；故 0<x<=20000 的最大值只需在素数点扫描。

## 2. 自足替换

| old | new |
| --- | --- |
| `ThetaEnvelopeTargetAt20000NumericalBudgetLedger` | `ThetaEnvelopeTargetAt20000SelfContainedClosedByPrimeLogCertificate` |
| `FiniteThetaEnvelopeBridgeBelowAnalyticThreshold` | `FiniteThetaBridgeBelow20000SelfContainedClosedByPrimeLogCertificate` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只给解析输入的有限核验证书，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `FinitePrimeLogThetaCertificateBuilt` | `true` | `true` | 用素数点高精度 log 累加与单调性，扫描 0<x<=20000 的 theta 上界。 | FiniteThetaBridgeBelow20000SelfContainedClosedByPrimeLogCertificate |
| `ThetaEnvelopeTargetAt20000NumericalBudgetLedger` | `true` | `true` | x=20000 处 theta(x)-x 明显为负，强于 x/36260 允许值。 | ThetaEnvelopeTargetAt20000SelfContainedClosedByPrimeLogCertificate |
| `FiniteThetaEnvelopeBridgeBelowAnalyticThreshold` | `true` | `true` | 最坏素数点 x=3 仍满足 theta(x)-x < x/36260，因此阈值以下有限桥自足闭合。 | FiniteThetaBridgeBelow20000SelfContainedClosedByPrimeLogCertificate |
| `InternalDusartGlobalThetaEnvelopeClosed` | `false` | `false` | 有限桥只覆盖 0<x<=20000，不证明 x>=20000 的内部 Dusart/PNT 包络。 | InternalZeroFreeRegionToThetaContourEnvelopeLedger |
| `SelfContainedMertensTailClosed` | `false` | `false` | 有限 theta 桥不关闭 B1 区间、reciprocal-prime Mertens 尾段或 DStructure 门。 | SelfContainedMeisselMertensB1IntervalArithmeticLedger AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosed` | `false` | `false` | 该有限桥只补解析输入，不产生最终反例矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
InternalZeroFreeRegionToThetaContourEnvelopeLedger
```
