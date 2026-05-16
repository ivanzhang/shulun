# Prime Matrix pressure-packet carrying ceiling via Brun-Selberg

**状态：** `pressure_packet_carrying_ceiling_reduced_to_brun_selberg_plus_supersqrt_pdec`

本步继续下钻上一文件留下的硬点：

```text
Global pressure-packet carrying ceiling.
```

结论是：这个硬点不是一个新的黑箱。它可被精确拆成：

```text
sqrt-product packet gate
+ Brun/Selberg twin reciprocal ceiling
+ SuperSqrt/PressureProduct PDEC exclusion.
```

其中 Brun/Selberg 部分是标准解析筛输入；作者侧若要完全自足，需要把该输入内联为
二维 Selberg 上筛常数包。否则它应作为明确外部定理输入登记，而不能伪装成已内证。

## 1. 压力包质量

令 `q` 为 AffineTwin 模数，故 `q` 与 `q-2` 同为素数。写

```text
g = q - 2,
f = q,
M_q = A_g A_f.
```

一个移动压力包的自然成对 SAE 质量为

```text
mu_q = M_q / (g f).
```

平方根门为

```text
M_q^2 <= g f.
```

若平方根门成立，则

```text
mu_q <= 1/sqrt(g f) <= 1/(q-2).
```

所以压力包可求和性被精确送到孪生素数倒数和。

## 2. Brun/Selberg 倒数天花板

设

```text
Pi_2(X) = #{q <= X : q and q-2 are prime}.
```

二维 Selberg/Brun 上筛给出标准无条件上界

```text
Pi_2(X) <= C_BS X / (log X)^2       (X >= X0).
```

由分部求和，对 `Q>=X0` 有

```text
sum_{q >= Q, q and q-2 prime} 1/q
 <= Pi_2(Q)/Q + integral_Q^infty Pi_2(t)/t^2 dt
 <= C_BS/(log Q)^2 + C_BS/log Q.
```

因此

```text
sum_{q >= Q, twin} 1/(q-2)
```

也收敛；例如 `q>=5` 时 `1/(q-2)<=3/q`。

这给出 moving pressure packets 的解析承载天花板：

```text
sum_{q twin, M_q^2<=q(q-2)} M_q/(q(q-2))
 <= sum_{q twin} 1/(q-2)
 < infinity.
```

## 3. 失败即 SuperSqrt/PressureProduct PDEC

若平方根门失败，则

```text
M_q^2 > g f.
```

等价于两侧压力乘积穿越：

```text
(A_g^2/g) * (A_f^2/f) > 1.
```

这正是已命名的

```text
SuperSqrtEpochPair-PDEC / PressureProduct-PDEC / ColumnCRT
```

出口。也就是说，pressure-packet carrying ceiling 的失败不是无名现象：

```text
carrying ceiling failure
=> either Brun/Selberg input absent,
   or sqrt-product gate fails,
   hence SuperSqrt/PressureProduct PDEC.
```

## 4. 新闭合链

当前 AffineTwin fill-arrival 支线可写成：

```text
threshold crossing
=> pressure packet
=> repeated residue/reset ColumnCRT-PDEC
   or fixed packet ColumnCRT-PDEC
   or moving packet.

moving packet
=> sqrt-product gate holds
      => Brun/Selberg twin reciprocal ceiling absorbs SAE mass
   or sqrt-product gate fails
      => SuperSqrt/PressureProduct PDEC.
```

因此最新剩余不再是笼统的 `GlobalFillResidueArrivalBound`，而是两个明确输入：

| 输入 | 类型 | 状态 |
| --- | --- | --- |
| `BrunSelbergTwinReciprocalCeiling` | 标准二维上筛/可外部引用或内联证明 | 外部可用，作者侧自足需内联 |
| `SuperSqrtPressureProductPDECExclusion` | 结构性 PDEC/ColumnCRT 排斥 | 仍开放 |

## 5. 对临界密度反馈桥的意义

临界密度反馈原理要求：反例不能免费制造超过 `1/log` 固定点承载能力的局部补洞。
本步说明在 AffineTwin 压力包层，承载能力的解析上界正是 Brun/Selberg 型
`1/log^2` 孪生筛密度。

如果 moving packets 遵守平方根门，它们落入 Brun/Selberg 可求和尾和；
如果它们不遵守平方根门，局部压力已经超过平方根临界面，必须显化为 PDEC/ColumnCRT。

这就是局部反馈矛盾场在当前最窄点的精确形式。

## 6. 当前状态

本步关闭：

- pressure packet carrying ceiling 的解析路线；
- 分部求和把 `Pi_2(X)<<X/log^2 X` 转成 twin reciprocal 收敛；
- carrying failure 到 SuperSqrt/PressureProduct PDEC 的等价回流。

本步未关闭：

- 作者侧完全自足的二维 Selberg/Brun 常数包；
- `SuperSqrtPressureProductPDECExclusion`。

因此行/列命题仍未无条件闭合。最新最窄硬点变成：

```text
SuperSqrtPressureProductPDECExclusion
```

并行保留：

```text
SelfContainedBrunSelbergTwinReciprocalCeiling
```

作为去外部化工程。
