# Prime Matrix strict row-level 非循环取向律路由器

**状态：** `row_level_noncircular_origin_reduced_to_orientation_local_factor_law_open`

本步继续沿同一个目标下钻：早期零行反例链若要在 strict 内部线中闭合，必须给出逐行 clean-core 原始 signed coefficient 生成表。前一轮已确认 signed value/slot/value-map/source identity 会回到 row-level 表本身，因此不能自证。本轮把这个表的首个真正不可替代字段压得更窄：必须有一个 Cauchy/Phi/payment 推前之前的 primitive 取向与 local factor 乘积律，正向输出 signed coefficient。只靠 unsigned 几何骨架、P 列锚、层叠轮、ExactUV 支撑或 payment 影像，最多确定行的位置和容量，不能决定反变号的 signed value。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
row_level_generation_target_active=true
unsigned_geometry_even_under_orientation_flip=true
signed_coefficient_is_orientation_sensitive=true
orientation_local_factor_law_proved=false
row_level_clean_core_origin_generation_table_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 本轮压缩

当前目标仍是：

```text
RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
WITH
NoncircularPreCauchySignedCoefficientOriginInputIndependentOfRowLevelGenerationCycle
```

新的最小字段为：

```text
PrimitiveOrientationLocalFactorProductLawBeforePushforward
```

它必须在同一 formal unit 中，对每条 actual noncanonical primitive row 给出

```text
signed_weight(row)=orientation(row) * local_factor_product(row) * truncation_weight(row)
```

并证明该表达式在 Cauchy、dispersion、Phi/payment 推前、terminal return 之前已经成立。

## 2. 取向障碍

已闭合的几何链条给出的是偶数据：

| closed data | what it determines | what it cannot determine |
| --- | --- | --- |
| carry-shell/P 列/phase skeleton | 候选 row 的位置、相位、窗口 | signed coefficient 的正负号 |
| layered wheel / CRT covering | unsigned 覆盖与同余兼容 | primitive row 的取向反变因子 |
| ExactUV support / rank | `(u,v)` 支撑、纤维秩、重数口径 | pushforward 前的原始符号来源 |
| Phi/payment atom | 下游收费位置 | Cauchy 前的 signed source law |
| formal-unit hash | 记录守恒与同单位绑定 | signed value 的数值生成 |

因此若一个候选证明只读取这些偶数据，它在 alpha/delta 交换、basis word 重标号或 row/source identity 回环下保持不变；但 signed coefficient 必须随 primitive orientation 或 local factor parity 改变。这个奇偶不匹配说明：已闭合几何不能生成 signed coefficient，只能验证一个已经给出的 signed law 是否兼容。

## 3. 非循环取向律合同

| field | required content |
| --- | --- |
| `prepushforward_domain` | actual noncanonical primitive row，时间戳早于 Cauchy/Phi/payment |
| `orientation_bit` | alpha/delta 或 primitive word 取向下的反变号；不能由下游 payment 反推 |
| `local_factor_product` | 筛因子、截断因子、branch local factor、零因子排除条件 |
| `truncation_weight` | 与同一 source tuple、anchor、phase 使用同一 formal unit 的权重口径 |
| `nonzero_certificate` | local factor 非零、符号不冲突、branch key 不超预算 |
| `prepushforward_sum_identity` | signed rows 推前前求和等于目标 alpha/delta primitive contribution |
| `no_cycle_use` | 不读取 row-level 表、origin identity、payment skeleton、早期零行 cover 或 terminal certificate |
| `return_tags` | 缺取向、零 local factor、符号冲突、canonical 泄漏、超预算均命名回流 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RowLevelGenerationTargetActive` | `true` | `false` | 当前仍在攻击逐行 clean-core 原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `ExistingSignedValueCycleDetected` | `true` | `true` | signed slot/value-map/source identity 回到 row-level 表。 | 不能自证 |
| `UnsignedGeometryAlreadyClosed` | `true` | `true` | row skeleton、P列锚、phase、层叠轮等只给偶几何数据。 | signed value 不由几何产生 |
| `GeometryEvenOrientationBarrier` | `true` | `true` | 只读偶几何数据的公式无法产生 orientation-sensitive signed coefficient。 | PrimitiveOrientationLocalFactorProductLawBeforePushforward |
| `MobiusParityCandidateInsufficientAsIs` | `true` | `false` | Möbius/parity 可作为候选取向影子，但当前未证明它就是 actual noncanonical primitive emitter 的精确系数。 | exact constructor declaration + local factor product identity |
| `PreCauchyConstructorLineStillNeeded` | `true` | `false` | 取向律必须由 Cauchy 前 constructor/emitter declaration 支撑。 | ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter |
| `NoReverseRecoveryDisciplinePreserved` | `true` | `true` | 不从早期零行、payment/Phi 或 terminal 证书反推 signed value。 | 正向证明取向律 |
| `OrientationLocalFactorLawCurrentCorpusProved` | `false` | `false` | 当前材料没有提交反变取向和 local factor 乘积律。 | PrimitiveOrientationLocalFactorProductLawBeforePushforward |
| `RowLevelOriginGenerationTableCurrentCorpusProved` | `false` | `false` | 没有该取向律，row-level 表仍未闭合。 | PrimitiveOrientationLocalFactorProductLawBeforePushforward |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `false` | `false` | 本步只进一步压缩缺口，不声明行/列命题无条件闭合。 | 取向律 + DStructure/Rankin 独立验收 |

## 5. 下一真正单点

首攻：

```text
PrimitiveOrientationLocalFactorProductLawBeforePushforward
```

等价展开：

```text
ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter
AND
ExactPrimitiveOrientationBitLaw
AND
ExactPrimitiveLocalFactorProductIdentity
AND
PrepushforwardSignedSumIdentity
AND
NoDownstreamOrCycleRecovery
```

若该取向律无法正向提交，则当前内部 strict 线不能继续靠 signed-source 表自闭合，只能回到：

```text
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
OR
AcceptFullSKLSExtExternalContract
```

并且无论内部或外部数学线如何推进，最终仍保留：

```text
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 结论

当前最新最窄硬点不是“再构造一张 row 表”，而是证明 row 表里 signed coefficient 的取向来源：一个 Cauchy 前、反推无关、与同一 formal unit 绑定的 primitive orientation/local-factor 乘积律。没有这个奇数据，所有已闭合的偶几何刚性只能定位候选行，不能产生 signed value，也就不能推出早期零行反例链与真实结构链的终端矛盾。
