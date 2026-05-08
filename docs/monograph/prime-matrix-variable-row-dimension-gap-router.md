# Prime Matrix 变量行维数差路由器

**状态：** `variable_row_dimension_gap_reduced_to_aligned_prime_main_or_named_defect`

本步把变量行维数差写成精确公式，并排除一个危险捷径：端点 x=P 的 P/log^2P 双素上界不能统一搬到 x≈sqrt(P)。在变量行上，R_x 的一素分支与双素分支共同处于 Buchstab u∈[2,3] 的两分支区间；真正剩余是证明一素分支在每个 P 对齐行中为正，或把为零的分支送入低模 PDEC、素对纤维集中、SAE 或 ColumnCRT。

```text
variable_row_dimension_gap_identity_closed=true
endpoint_dimension_gap_uniform_lift_rejected=true
uniform_dimension_gap_constants_proved=false
row_column_unconditional_closed=false
terminal_gap_after_router=AlignedPrimeMainBuchstabBranchLowerBoundOrDefectReturn
```

## 1. 精确变量行公式

对 `sqrt(P)<=x<P`：

```text
G_x(P)=#R_x
B_x(P)=#SemiprimeFibers_x
PrimeSurvivors_x=G_x(P)-B_x(P).
```

双素纤维有精确求和式：

```text
B_x(P)=sum_{q prime, x<q<=sqrt((x+1)P)} # {m prime: max(q,ceil((xP+1)/q))<=m<=floor((xP+P-1)/q)}.
```

因此变量行维数差不是启发式口号，而是完全等价的幸存者恒等式。

## 2. 端点合同不能直接统一外推

对角端点 `x=P` 中，双素覆盖被三条倒数地板曲线压到 `P/log^2 P` 型对象；
但在变量行，尤其 `x≈sqrt(P)` 时，collar 中的 `m` 窗口长度可达 `sqrt(P)`，双素纤维仍有 `P/log P` 量级。
所以端点维数差合同是 `alpha=1` 的退化口，不是 `alpha in [1/2,1]` 的统一证明。

## 3. 判定表

| gate | closed | proved | meaning | output |
| --- | --- | --- | --- | --- |
| `PrimeSurvivorIdentityImported` | `true` | `true` | 上一轮已证明 G_x(P)-B_x(P) 精确等于素数幸存数。 | `变量行维数差是等价目标，不是启发式近似。` |
| `ExactVariableFiberFormula` | `true` | `true` | B_x(P) 可精确写成 collar 中 q 的短素数窗口求和。 | `B_x(P)=sum_{x<q<sqrt((x+1)P)} #{prime m in I_{x,q}}。` |
| `EndpointDimensionGapDoesNotUniformlyLift` | `true` | `true` | 端点 x=P 的 B(P)=O(P/log^2 P) 依赖 m 窗口长度 O(1)；x≈sqrt(P) 时 B_x(P) 与 G_x(P) 同为 P/log P 量级。 | `不能把端点常数合同直接用于全部变量行。` |
| `TwoBranchSupportShape` | `true` | `true` | 因 x>=sqrt(P) 且 xP+c<P^2，R_x 的合数只能有两个 >x 素因子；支撑上只有一素分支与双素分支。 | `自足证明应瞄准一素分支正性或缺陷回流。` |
| `UniformBuchstabConstants` | `false` | `false` | u=log(xP)/log(x)=1+1/alpha 属于 [2,3]，但尚未证明全 alpha 的 Buchstab 常数账本和误差项。 | `UniformBuchstabOnePrimeBranchLowerBound。` |
| `EndpointContractCompatibility` | `true` | `true` | 端点维数差是变量行路线的 alpha=1 退化口。 | `EndpointDG remains a special case, not the uniform proof.` |
| `EDADualCompatibility` | `true` | `true` | 变量行维数差若失败，就是 EDA-Dual 中的低模/尾项缺陷。 | `PrimeFreeIntervalLowModPDECDefectReturn。` |
| `UniformDimensionGapConstants` | `false` | `false` | 尚未给出所有 alpha in [1/2,1] 的 G_x(P)>B_x(P) 常数账本。 | `AlignedPrimeMainBuchstabBranchLowerBoundOrDefectReturn。` |

## 4. 样本审计

样本用于定位危险 alpha 区间，不作为证明。

```text
sample_status=variable_row_dimension_gap_sample_verified_router_open
all_identity_holds=true
global_min_prime=7
global_max_semiprime_share=0.500000
```

| P | rows | min prime | max semiprime share | max fiber load | min prime logx/P | max semiprime logx/P |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 101 | 91 | 7 | 0.500000 | 2 | 0.228560 | 0.228560 |
| 499 | 477 | 29 | 0.420290 | 4 | 0.289452 | 0.220366 |
| 997 | 966 | 54 | 0.413333 | 5 | 0.313119 | 0.221999 |
| 1999 | 1955 | 110 | 0.401408 | 7 | 0.320604 | 0.215807 |

按 `alpha=log x/log P` 分桶的压力读数：

| P | alpha bucket | rows | min prime | max semiprime share | min prime share | max fiber load |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 101 | 0.50-0.60 | 5 | 9 | 0.500000 | 0.500000 | 2 |
| 101 | 0.60-0.70 | 10 | 9 | 0.368421 | 0.631579 | 2 |
| 101 | 0.70-0.80 | 15 | 11 | 0.277778 | 0.722222 | 2 |
| 101 | 0.80-0.90 | 23 | 9 | 0.266667 | 0.733333 | 1 |
| 101 | 0.90-1.01 | 37 | 7 | 0.230769 | 0.769231 | 1 |
| 499 | 0.50-0.60 | 19 | 40 | 0.420290 | 0.579710 | 4 |
| 499 | 0.60-0.70 | 36 | 42 | 0.382353 | 0.617647 | 4 |
| 499 | 0.70-0.80 | 67 | 36 | 0.305085 | 0.694915 | 2 |
| 499 | 0.80-0.90 | 124 | 34 | 0.235294 | 0.764706 | 2 |
| 499 | 0.90-1.01 | 230 | 29 | 0.152174 | 0.847826 | 1 |
| 997 | 0.50-0.60 | 31 | 83 | 0.413333 | 0.586667 | 5 |
| 997 | 0.60-0.70 | 63 | 73 | 0.370968 | 0.629032 | 4 |
| 997 | 0.70-0.80 | 125 | 68 | 0.297297 | 0.702703 | 3 |
| 997 | 0.80-0.90 | 249 | 60 | 0.247191 | 0.752809 | 2 |
| 997 | 0.90-1.01 | 497 | 54 | 0.139241 | 0.860759 | 1 |
| 1999 | 0.50-0.60 | 51 | 152 | 0.400735 | 0.599265 | 7 |
| 1999 | 0.60-0.70 | 109 | 136 | 0.353712 | 0.646288 | 5 |
| 1999 | 0.70-0.80 | 233 | 130 | 0.299492 | 0.700508 | 3 |
| 1999 | 0.80-0.90 | 497 | 118 | 0.209945 | 0.790055 | 2 |
| 1999 | 0.90-1.01 | 1064 | 110 | 0.156463 | 0.843537 | 1 |

## 5. 新最窄剩余

```text
AlignedPrimeMainBuchstabBranchLowerBoundOrDefectReturn
  = UniformBuchstabOnePrimeBranchLowerBound
    AND VariableRowRoughSkeletonLowerBound
    AND VariableRowPrimePairFiberUpperBound
    AND LowModSkeletonDeficitPDEC
    AND PrimePairFiberConcentrationTailPDEC
    AND SparsePrimeSurvivorSAE
    AND ColumnDisplacementReusePDEC.
```

含义是：若不能直接证明每行一素分支为正，就必须把失败转成同 formal unit 的低模亏损、
素对纤维集中、孤立幸存者逃逸或固定列位移复用。该路由仍未给出无条件闭合。
