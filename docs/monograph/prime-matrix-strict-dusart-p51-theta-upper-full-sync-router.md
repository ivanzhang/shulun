# Prime Matrix strict Dusart P5.1 theta 上界全段同步证书

**状态：** `dusart_p51_theta_upper_full_external_and_self_contained_table_lane_closed`

Dusart P5.1 的全段 theta 上界已同步到 table_012-x87 自足低段：低段由独立 `theta(x)<x` 到 `8e11` 归档给出，中段由 `psi<1.00002841x` 与 `psi-theta>0.9999sqrt(x)` 拼接给出，高尾由 FK b0=28 的 `0.00001262<1/36260` 给出。因此可在解析输入链中登记 `theta(x)-x<x/36260` 对所有 `x>0` 成立。该步仍不产生行/列反例链终端矛盾。

```text
dusart_p51_full_theta_statement_external_closed=true
dusart_p51_full_theta_statement_self_contained_closed=true
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 三段算术

| segment | relative result | margin to 1/36260 |
| --- | ---: | ---: |
| low `0<x<=8e11` | `0` | `0.00002757859900717043574186431329288472145615002757859900717043574186431329` |
| middle `8e11<=x<=e^28` | `0.00002757855443376834247272442125594899423162180240085192566211998826311803` | `4.457340209326913989203693572722452822517774708150831575360119526E-11` |
| high `x>=e^28` | `0.00001262` | `0.00001495859900717043574186431329288472145615002757859900717043574186431329` |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只合取 P5.1 的解析输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `DusartP51FullSyncGateActive` | `true` | `true` | 上一证书已把下一最窄点设为 Dusart P5.1 全段 theta 上界同步。 | DusartP51ThetaUpperFullSyncLedger |
| `LowSegmentThetaLtIdentityTo8e11` | `true` | `true` | 对 0<x<=8e11，theta(x)<x，故 theta(x)-x<0<x/36260；低段现有外部表路线和 table_012-x87 自足路线。 | table_012 x87 independent archive |
| `LowSegmentThetaLtIdentityTo8e11SelfContained` | `true` | `true` | table_012 独立极值归档、区间预算和 x87 log-oracle 证书给出低段 theta<x 的作者侧自足输入。 | table_012 x87 independent archive |
| `MiddleStripPsiThetaSplice` | `true` | `true` | 对 8e11<=x<=e^28，psi<1.00002841x 且 psi-theta>0.9999sqrt(x)，得到目标余量。 | middle strip closed |
| `HighTailFaberKadiriB28Splice` | `true` | `true` | 对 x>=e^28，FK b0=28 给出 psi 高尾误差 0.00001262，小于 1/36260；theta<=psi。 | high tail closed |
| `ThreeSegmentArithmeticClosed` | `true` | `true` | 低段、中段、高尾三段阈值顺序与余量均为正。 | arithmetic synchronized |
| `DusartP51ThetaUpperFullSyncLedger` | `true` | `true` | 高尾、中段和低段三段输入齐备后，Dusart P5.1 全段 theta(x)-x<x/36260 闭合。 | theorem closed on external lane and self-contained table_012 lane |
| `DusartP51ThetaUpperFullSelfContainedLedger` | `true` | `true` | table_012 原始有限计算/hash 已由独立极值归档与 x87 log-oracle 证书内化，P5.1 全段 theta 上界在作者侧解析输入链中闭合。 | closed |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步关闭的是解析输入定理，不直接产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一最窄点

```text
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

