# Prime Matrix critical fill-arrival anti-overfilling router

**状态：** `critical_fill_arrival_pressure_packet_routing_closed_global_ceiling_open`

本文把上一步的临界密度反馈桥落到当前 Prime Matrix 最窄点：

```text
AffineTwinFillResidueArrivalBoundOrFillCatchUpMassPDECExclusion
```

核心修正是：不能只盯住新增 fill residue 的裸质量 `E_f/f`。裸质量说明
fill 侧确实付费，但它本身不直接给全局求和矛盾。真正与阈值穿越等价的量是
两侧 residue 压力乘积。

## 1. 变量

令

```text
g = q - 2,
f = q,
A_g = generator 侧已用 residue 数,
A_f = fill 侧已用 residue 数,
T_q = floor(sqrt(g f)).
```

安全门为

```text
A_g A_f <= T_q.
```

若某条补齐路线把两侧 residue 数变为 `A'_g,A'_f`，则阈值穿越等价于

```text
A'_g A'_f >= T_q + 1.
```

## 2. 精确压力形式

定义两侧压力

```text
P_g = (A'_g)^2 / g,
P_f = (A'_f)^2 / f.
```

则

```text
A'_g A'_f > sqrt(g f)
iff
P_g P_f > 1.
```

因此任何阈值穿越都不是单侧计数事件，而是互反压力事件：

```text
P_f > 1/P_g,
P_g > 1/P_f.
```

特别地，若 generator 侧已经有一侧高压，fill 侧仍必须补到相应的互反平方根压力；
若 generator 侧没有高压，fill 侧必须更强。

## 3. fill 最小追赶公式

固定补齐后的 generator 数 `A'_g`，fill 侧要穿越阈值的最小目标为

```text
A'_{f,min}(A'_g) = floor(T_q / A'_g) + 1.
```

因此所需新增 fill residue 为

```text
E_f(A'_g) = max(0, floor(T_q / A'_g) + 1 - A_f).
```

这解释了当前三个候选：

| q | current `(A_g,A_f)` | route | minimal fill target | minimal fill increment |
| ---: | ---: | --- | ---: | ---: |
| 31 | `(3,4)` | mixed `A'_g=6` | `5` | `1` |
| 43 | `(8,2)` | fill-only `A'_g=8` | `6` | `4` |
| 43 | `(8,2)` | mixed `A'_g=9` | `5` | `3` |
| 103 | `(12,1)` | fill-only `A'_g=12` | `9` | `8` |
| 103 | `(12,1)` | mixed `A'_g=13` | `8` | `7` |

这与现有 threshold-route 与 fill-catchup 账本一致。

## 4. 新的最窄二分

由上式，阈值穿越带来的是 fill 侧平方根压力包：

```text
A'_f > sqrt(f / P_g).
```

于是无条件路线必须证明以下二分：

```text
threshold crossing
=> reset/ColumnCRT PDEC
   or fixed pressure packet recurrence PDEC
   or moving pressure packet SAE/Rankin
   or non-sparse pressure packet demand.
```

其中：

- 若新增 fill residue 复用旧 residue，已经由上一账本路由为 `reset/ColumnCRT PDEC`；
- 若固定 `q`、固定双槽、固定压力包复现，则合成模数 `q(q-2)` 大于相位支撑，进入 `ColumnCRT/PDEC`；
- 若 `q` 或槽图样移动，单个双槽原子的自然 SAE 质量是 `1/(q(q-2))`，而阈值压力包的成对质量至少达到 `1/sqrt(q(q-2))`；
- 若这些移动压力包仍不足以承载反例链，则 SAE 吸收；
- 若反例链要求非稀疏压力包需求，则它必须输出明确的 `NonSparseAffineTwinPressureDemand`，再与 Brun 型 twin-reciprocal 账本或内部替代包比较。

## 5. 为什么裸 fill 质量不是最终上界

上一账本给出的裸 fill 质量为

```text
E_f / f.
```

而成对 SAE 增量为

```text
A'_g E_f / (g f).
```

二者关系为

```text
E_f / f = (g / A'_g) * A'_g E_f / (g f).
```

当 generator 侧不够密时，裸 fill 质量会远大于成对 SAE 质量；这时不能强行用
SAE 求和吸收裸质量。正确做法是：

```text
generator 稀薄但 fill 大量追赶
=> fill 平方根压力包
=> fixed packet PDEC 或 moving packet demand。
```

这就是临界密度反馈桥在此处给出的真正新增约束：反例不能免费把裸 fill 质量
当作普通噪声吸收；它必须以压力包、PDEC 或 SAE 的形式显化。

## 6. 可写成定理的输入

下一步应直接攻击如下输入。

```text
CF-PM-FillPressurePacket:
在 square-phase/off-band AffineTwin formal unit 中，若无限多阈值穿越发生，
且没有 reset/ColumnCRT PDEC，则穿越产生的 fill 平方根压力包要么形成
可求和的 moving-packet SAE/Rankin 质量，要么形成非稀疏压力包需求。
后一种需求必须触发 HighDensityEpochPair/PressureProduct PDEC，
或与 twin-reciprocal/Brun 型临界账本矛盾。
```

这比原来的 `GlobalFillResidueArrivalBound` 更精确：

```text
旧目标：控制 fill-side residue arrival。
新目标：控制 threshold-relevant fill pressure packets。
```

## 7. 当前闭合与剩余

已闭合：

- `A'_g A'_f > sqrt(gf)` 与 `P_g P_f>1` 等价；
- 最小 fill 追赶公式 `floor(T_q/A'_g)+1-A_f`；
- 新 fill 或 reset/ColumnCRT PDEC 二分；
- 固定双槽相位锁 `q(q-2)>(q+9)/2`；
- moving family 的 SAE/ColumnCRT 分流。

仍未闭合：

```text
Global pressure-packet carrying ceiling.
```

也就是必须证明 moving pressure packets 总能被 SAE/Rankin 吸收，或者证明非稀疏
pressure demand 必然回流到 `HighDensityEpochPair/PressureProduct/ColumnCRT/PDEC`。

本步不宣称行/列命题无条件闭合；它把当前硬点从“fill 到达率”压缩成
“threshold-relevant pressure packet carrying ceiling”。
