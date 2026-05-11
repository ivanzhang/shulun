# Prime Matrix strict alpha row unsigned skeleton 路由器

**状态：** `alpha_row_unsigned_skeleton_closed_signed_lift_and_overload_return_open`

本步继续攻当前最窄硬点，并把 alpha row 发射公式拆成已闭合的 unsigned skeleton 与仍开放的 signed 层。source tuple 可复算 A、D0/K/Omega、phase_rule；carry-shell 给出 h,a,b,c 同余骨架；P列锚和层叠轮给出相位兼容字母表；anchor-collar 给出短纤维限制。因此当前真正剩余不是 row 的 unsigned 形状，而是把这个 skeleton 提升为 pre-Cauchy signed alpha primitive coefficient，并排斥或登记短纤维过载回流。

```text
alpha_row_unsigned_skeleton_router_closed=true
unsigned_source_tuple_carry_shell_binding_closed=true
unsigned_carry_shell_congruence_row_skeleton_closed=true
unsigned_phase_wheel_compatibility_closed=true
alpha_formula_signed_coefficient_lift_proved=false
alpha_formula_anchor_collar_overload_named_return_proved=false
alpha_row_anchor_phase_emission_formula_proved=false
pointwise_primitive_kernel_table_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

AlphaRowAnchorPhaseEmissionFormulaLedger 的 unsigned 骨架部分已经由 source tuple、carry-shell、anchor-collar、P列锚和 layered-wheel 共同关闭；剩余不是几何 row 形状，而是 `AlphaFormulaSignedCoefficientLiftLedger` 与 `AlphaFormulaAnchorCollarOverloadNamedReturnLedger`。

## 2. unsigned 骨架公式

| name | formula | role |
| --- | --- | --- |
| `P-column distance coordinate` | `n_{x,c}=xP+c=P(x+1)-(P-c)=Py-d, 1<=d<P` | 把行坐标统一放到第 P 列锚点 Py 左侧距离 d。 |
| `carry-shell identity` | `h=a+b-floor(ab/P), c=ab mod P` | 把双高因子补洞压到带进位壳变量 h,a,b,c。 |
| `wheel skeleton shift` | `S_W(P,y) == S_W(P,2)+P(y-2) mod W` | 把 P 列锚相位与第一行轮骨架圆柱平移连接。 |
| `anchor collar` | `x<q<sqrt((x+1)P), m in interval length < P/q <= sqrt(P)` | 把高素 anchor 和 cofactor 限制到短素数纤维。 |
| `phase discipline` | `phase_rule(d)=true or named phase return` | source tuple 的相位过滤不能静默删点。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AlphaRowAnchorPhaseTargetActive` | `true` | `false` | 逐点 primitive 核表当前优先卡在 alpha row anchor/phase 发射公式。 | AlphaRowAnchorPhaseEmissionFormulaLedger |
| `SourceTupleAnchorPayloadClosed` | `true` | `true` | source tuple 已给出同 formal-unit 的 A、D0/K/Omega、phase_rule 与 hash。 | 这只锁定输入参数，不给 signed coefficient。 |
| `CarryShellUnsignedFormulaClosed` | `true` | `true` | 双高因子补洞满足 h=a+b-floor(ab/P), c=ab mod P。 | 这是 unsigned row 形状公式。 |
| `AnchorCollarUnsignedFiberClosed` | `true` | `true` | 最小高素 anchor 被限制到 canonical collar，cofactor 位于短素数纤维。 | 过载仍需命名回流或容量排斥。 |
| `PColumnLayeredPhaseSkeletonClosed` | `true` | `true` | P列锚、圆柱平移和层叠轮筛给出候选 row 的相位字母表。 | 相位字母表仍是 unsigned/geometric。 |
| `UnsignedVariableBindingClosed` | `true` | `true` | A、D0/K/Omega、phase_rule 可作为 carry-shell 变量筛选和锚区间过滤的输入。 | 不产生 signed alpha source measure。 |
| `UnsignedCongruenceRowSkeletonClosed` | `true` | `true` | carry-shell 同余和 P列距离坐标给出候选 row skeleton 的确定性索引规则。 | 不证明该 row skeleton 是 pre-Cauchy alpha primitive row。 |
| `UnsignedPhaseCompatibilityClosed` | `true` | `true` | phase_rule、P列圆柱平移和 layered-wheel 单位类可在同一 source tuple 中登记。 | 不控制 signed 变差和 branch key。 |
| `SignedCoefficientLiftStillOpen` | `true` | `false` | 已有 signed-lift 审查证明：unsigned carry-shell 命中不能自动定义 actual signed alpha source。 | AlphaFormulaSignedCoefficientLiftLedger |
| `AnchorCollarOverloadReturnStillOpen` | `true` | `false` | 短纤维过载已被识别为 PDEC/SAE/ColumnCRT/CleanKLS 回流形状，但排斥未证。 | AlphaFormulaAnchorCollarOverloadNamedReturnLedger |
| `AlphaRowAnchorPhaseEmissionFormulaCurrentCorpusProved` | `false` | `false` | unsigned skeleton 已可登记，但完整 alpha row 发射公式还缺 signed lift 与过载回流排斥。 | AlphaFormulaSignedCoefficientLiftLedger AND AlphaFormulaAnchorCollarOverloadNamedReturnLedger |

## 4. 下一真正硬点

```text
AlphaFormulaSignedCoefficientLiftLedger
```

并行必要输入：

```text
AlphaFormulaAnchorCollarOverloadNamedReturnLedger
```
