# Prime Matrix 早期零行双高因子带进位壳路由器

**状态：** `exact_carry_shell_identity_closed_primitive_capacity_open`

本步闭合了早期零行高补洞支撑的精确几何：所有双高因子补洞都落在 `h=a+b-floor(ab/P), c=ab mod P` 的带进位壳上。于是 `EarlyZeroPrimitivePDECBudgetInequality` 不再是泛称 PDEC 容量问题，而被压成 `CarryShellPrimitiveCapacityBoundOrPDECReturn`。

```text
exact_carry_shell_identity_closed=true
bottom_band_k0_recovered=true
early_zero_primitive_pdec_budget_closed=false
row_column_unconditional_closed=false
```

## 1. 带进位壳恒等式

假设 `1<=x<P`，`c in R_x`，且该残洞被未完成高素斜线补掉：

```text
xP+c = q m,  x<q<P.
```

因为 `c in R_x`，`xP+c` 没有不超过 `x` 的素因子，所以 `m>x`。又 `q>=x+1`，于是

```text
m = (xP+c)/q < (x+1)P/(x+1) = P.
```

令

```text
h=P-x,  q=P-a,  m=P-b,  k=floor(ab/P).
```

则 `1<=a,b<h`，并且

```text
(P-a)(P-b) = P(P-a-b+k) + (ab mod P).
```

与 `xP+c=(P-h)P+c` 比较得到精确恒等式：

```text
h = a+b-k,
c = ab mod P,
k = floor(ab/P).
```

这说明高补洞不是任意列覆盖，而是被限制在有限的 `carry shell` 上。

## 2. 底部带作为 k=0 特例

若 `h<sqrt(P)`，则 `ab<h^2<P`，所以 `k=0`。恒等式退化为：

```text
a+b=h,
c=ab=a(h-a).
```

这正好恢复已有底部缺口对容量定理；底部二次曲线是全局带进位壳的最低层。

## 3. 判定表

| gate | closed | proved | meaning | output |
| --- | --- | --- | --- | --- |
| `EarlyZeroTerminalPackageImported` | `true` | `true` | 上一轮已把早期零行分支压成 PDEC/SAE/ColumnCRT 终端排斥包。 | `当前只攻击 PDEC primitive budget 的支撑几何。` |
| `DoubleHighFactorWindow` | `true` | `true` | 若 c in R_x 且由高素 q 补洞，则 xP+c=qm，且 x<q,m<P。 | `所有补洞原子都是双高因子窗口内的物理原子。` |
| `ExactCarryShellIdentity` | `true` | `true` | 写 q=P-a,m=P-b,k=floor(ab/P)，则 h=P-x=a+b-k 且 c=ab mod P。 | `高补洞支撑被限制在带进位双高因子壳。` |
| `BottomBandK0Recovered` | `true` | `true` | 当 h<sqrt(P) 时 ab<P，故 k=0，恢复底部二次缺口曲线 c=a(h-a)。 | `底部带 BDP 是 carry-shell 的 k=0 特例。` |
| `SampleCarryAudit` | `true` | `false` | 样本全行高补洞均满足双高因子窗口和带进位恒等式；这只是审计，不替代代数证明。 | `carry_shell_identity_sample_verified_theorem_algebraic_budget_open` |
| `PrimitivePDECSupportReframed` | `true` | `true` | 早期零行的 primitive PDEC 下界不能再用任意坏窗支撑；它只能在 carry-shell 支撑上提交。 | `EarlyZeroPrimitivePDECBudgetInequality -> CarryShellPrimitiveCapacityBoundOrPDECReturn。` |
| `NamedReturnCompatibility` | `true` | `true` | carry-shell 上若出现孤立窗、端点、同列位移或复用，已有 SAE/ColumnCRT/PDEC 命名回流。 | `无名出口删除。` |
| `CarryShellPrimitiveCapacityBound` | `false` | `false` | 尚未证明每个 h 壳的双高因子可用列容量严格小于 R_x，或失败必给可排斥 PDEC。 | `CarryShellPrimitiveCapacityBoundOrPDECReturn。` |

## 4. 样本审计

样本审计只用于防止口径错误；恒等式本身由上面的代数证明给出。

```text
sample_status=carry_shell_identity_sample_verified_theorem_algebraic_budget_open
all_factor_windows_ok=true
all_carry_identities_ok=true
all_bottom_bands_have_zero_carry=true
```

| P | high filler hits | max row hits | max carry | positive carry rows | bottom positive carry rows |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 101 | 362 | 80 | 80 | 66 | 0 |
| 499 | 4778 | 425 | 454 | 430 | 0 |
| 997 | 14788 | 863 | 932 | 891 | 0 |

## 5. 新最窄剩余

本步把早期零行终端包中的 primitive PDEC 容量项进一步压缩为：

```text
CarryShellPrimitiveCapacityBoundOrPDECReturn
  = CarryShellPrimitiveCapacityBound
    OR CarryShellPersistentConcentrationPDECReturn
    OR CarryShellSparseLocalSurvivorOrSAEReturn
    OR CarryShellDisplacementColumnCRTReturn.
```

其中真正未闭合的是 `CarryShellPrimitiveCapacityBound`：要证明每个 `h` 壳的双高因子可用列容量不能吃掉整个 `R_x`，或者一旦吃掉就强制产生可排斥的 PDEC/SAE/ColumnCRT 证书。

因此本步是支撑几何闭合，不是行命题无条件闭合；`row_column_unconditional_closed=false` 仍保持。
