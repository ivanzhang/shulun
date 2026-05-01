# GEE Load 口径统一审查

本文补第三项剩余义务：全文统一使用“相对零频基线的超额偏差”作为 `Load`，避免把零频容量、内部转移步或 seed 重复计入异常负担。

## 1. 统一定义

对任何出口 `E`，最终稿中采用：

`Load(E;X)=Σ_{a routed finally to E} θ_{a,E} Excess(a)`，

其中

`Excess(a)=max(0, σΣ_{n∈a}(w_X(n)-w_X^0(n)))`。

若使用平方能量包，则采用等价超额形式：

`ExcessEnergy=max(0, Energy-C_0·ZeroFrequencyCapacity)`。

## 2. 不计入 Load 的对象

以下对象不得计入最终 `Load`：

1. CRT/MLC/PI/DSO 零频容量本身；
2. `A/FCT/SC` 的内部势函数下降步；
3. `CE/LSMP` 输出但已转入其它出口的 seed；
4. `LV` 阈值失败并已转出的对象；
5. NRC 非共振失败后转入 FCT 的对象。

## 3. 旧文替换规则

最终论文中遇到旧表述：

- “`Load(E)=Σ|bias|`”应解释为“最终路由到 `E` 的超额偏差和”；
- “容量界给 `Load` 上界”应改为“扣除零频容量后，超额部分给 `Load` 上界”；
- “FCT/SC/A 给 `o(Δ)`”应改为“FCT/SC/A 无最终未处理负担，内部转移或转出后最终 `Load=o(Δ)`”。

## 4. Theorem Load-Convention-Compatibility

**Theorem.** 在统一 Load 口径下，GEE-0 下界与九出口上界使用同一异常账本；零频容量不重复计数，内部转移不重复计数，seed 转出不重复计数。

**证明。** GEE-0 的原始异常即 `w_X-w_X^0` 的同向正偏差。统一定义只在该偏差项上拆分权重，不重新加入 `w_X^0`。内部转移只改变同一偏差的结构标签，不增加负担。seed 转出由 Seed-Transfer 将权重从源出口移到目标出口。故上下界口径一致。证毕。
