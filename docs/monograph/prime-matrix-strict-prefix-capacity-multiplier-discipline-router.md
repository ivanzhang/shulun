# Prime Matrix strict prefix 容量乘子纪律路由器

**状态：** `prefix_capacity_multiplier_discipline_closed_normalized_potential_anticollapse_open`

`RegisteredPrefixCapacityMultiplierDiscipline` 可以闭合为精确乘子记账：每个标签 q 在同一行只命中 mu_q(x;P) 个列，且 mu_q<=ceil(P/q)。因此 prefix atom 按 1/mu_q 赋权后，同一 q 的总权重至多 1，归一化质量 M# 下界不同标签数。剩余不是乘子纪律本身，而是证明 M# 足够大，并证明不同标签不会在 row-free type/quotient 投影下塌缩。

```text
exact_row_hit_multiplicity_formula_closed=true
uniform_capacity_ceiling_closed=true
capacity_normalized_charge_closed=true
distinct_label_lower_bound_closed=true
registered_prefix_capacity_multiplier_discipline_proved=true
normalized_prefix_residual_potential_lower_bound_proved=false
prefix_label_support_to_row_free_type_anticollapse_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 乘子公式

固定 `q<P`，令 `a_q` 是 `-xP mod q` 在 `[1,q]` 中的正代表，其中余数 `0` 写成 `q`。则

```text
mu_q(x;P)=1+floor((P-1-a_q)/q),
mu_q(x;P)<=ceil(P/q).
```

对 prefix canonical label `tau_z(c)` 定义

```text
M#_{x,z}=sum_{c in R_{x,z}} 1/mu_{tau_z(c)}.
```

同一标签 `q` 至多贡献 `mu_q` 个 atom，因此其归一化总贡献至多 `1`，从而 `#distinct labels >= M#_{x,z}`。

## 2. 乘子律

| law | formula | status |
| --- | --- | --- |
| `row_hit_multiplicity_formula` | mu_q(x;P)=#{1<=c<P: c == -xP mod q}=1+floor((P-1-a_q)/q), a_q in [1,q]. | `closed` |
| `uniform_capacity_ceiling` | mu_q(x;P)<=ceil(P/q); in particular q>z gives mu_q<=ceil(P/z). | `closed` |
| `capacity_normalized_charge` | M#_{x,z}=sum_{c in R_{x,z}} 1/mu_{tau_z(c)}. | `defined_closed` |
| `distinct_label_lower_bound` | #distinct tau_z labels >= M#_{x,z}. | `closed` |
| `label_to_type_gap` | distinct labels do not yet imply enough row-free formal-unit types without anti-collapse. | `open` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CapacityMultiplierInputActive` | `true` | `false` | 上一层把 prefix 加权转移后的直接硬点定为容量乘子纪律。 | RegisteredPrefixCapacityMultiplierDiscipline |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只在早期零行假设下登记每个 q 的行内命中容量。 | 保持 row_column_unconditional_closed=false。 |
| `ExactRowHitMultiplicityFormulaClosed` | `true` | `true` | 固定 q<P 时，覆盖列是单个模 q 余类在 [1,P-1] 的截断，故 mu_q 有显式整式公式。 | 无。 |
| `UniformCapacityCeilingClosed` | `true` | `true` | 由公式立得 mu_q<=ceil(P/q)，所以降低 cutoff 后的复用风险被显式乘子控制。 | 乘子可控不等于归一化质量足够大。 |
| `CapacityNormalizedChargeClosed` | `true` | `true` | 给每个 prefix atom 赋权 1/mu_tau；同一标签的总权重不超过 1。 | 需要证明总归一化权重超过类型阈值。 |
| `DistinctLabelLowerBoundClosed` | `true` | `true` | 按标签分组求和，#distinct labels >= sum_c 1/mu_tau(c)。 | 不同标签到不同 row-free type 仍需防止哈希/quotient 塌缩。 |
| `RegisteredCapacityMultiplierDisciplineClosed` | `true` | `true` | 容量乘子字段和归一化记账纪律已经闭合；不能再把 completed-internal 标签的多命中当作免费独立实例。 | RegisteredPrefixCapacityMultiplierDiscipline |
| `NormalizedPrefixPotentialLowerBoundCurrentCorpusProved` | `false` | `false` | 尚未证明 M#_{x,z} 对某个统一 prefix z 超过类型压缩阈值。 | NormalizedPrefixResidualPotentialLowerBound |
| `PrefixLabelToTypeAntiCollapseCurrentCorpusProved` | `false` | `false` | 尚未证明不同 tau_z 标签或标签骨架不会在 row-free type 投影下大量合并。 | PrefixLabelSupportToRowFreeTypeAntiCollapse |
| `EffectiveTypeInstanceLowerBoundCurrentCorpusProved` | `false` | `false` | 有了容量纪律后，最终仍需归一化质量下界与标签到类型抗塌缩合取。 | NormalizedPrefixResidualPotentialLowerBound AND PrefixLabelSupportToRowFreeTypeAntiCollapse |

## 4. 下一最窄点

```text
NormalizedPrefixResidualPotentialLowerBound
```

并行保留：

```text
PrefixLabelSupportToRowFreeTypeAntiCollapse
```

审稿边界：本步闭合的是 prefix 标签复用的精确乘子记账；它没有证明归一化残洞势下界，也没有关闭行/列无条件命题。
