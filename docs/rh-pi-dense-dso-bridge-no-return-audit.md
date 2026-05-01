# PI dense/Carleson 与 DSO bridge 适用条件无回流审查

本文补强容量矩阵中的剩余接口：`PI dense/Carleson` 与 `DSO/PI bridge` 的适用条件失败时，是否会无标记回流到 PI 或 DSO 自身。结论是：所有失败边都进入已命名事件 `CE/LSMP/FCT/LV/SC/DSO/PI_seed/Capacity`，不形成自由循环。本文不宣称 RH 已证明。

## 1. 接口对象

涉及三类容量入口：

1. `PI-lacunary`：强 lacunary 尺度包的 Mellin 有限重叠；
2. `PI-dense/Carleson`：dense 尺度包的固定模板 Carleson/平方函数容量；
3. `DSO/PI bridge`：新增独立频率包由 DSO square-function 反馈到允许投影族。

三者共同处理同一问题：高投影或新增频率能量不能在跨尺度中无成本累积。

## 2. 适用条件清单

| 接口 | 必要条件 | 若失败则转入 |
| --- | --- | --- |
| PI-lacunary | Mellin 支撑强分离 | dense pack / DSO |
| PI-lacunary | 固定投影模板 | CE/LSMP/FCT |
| PI-lacunary | 边界尾项平方可和 | CE/LSMP/LV |
| PI-dense | 模板可拉回 CRT martingale | TC；否则 CE/FCT |
| PI-dense | dense pack 有统一归一化容量 | DSO/Carleson；否则分包重做 lacunary/dense |
| PI-dense | 投影窗口属于允许族 | 非允许即 CE 或 FCT |
| DSO/PI bridge | 新增包是允许投影有限交 | 非允许即 CE/LSMP/FCT |
| DSO/PI bridge | 新增坐标自然细化 | 否则旧坐标重写，转 CE/LV/FCT |
| DSO/PI bridge | 误差不吞噬能量 | 否则 LSMP/LV/CE |
| DSO/PI bridge | 重叠不超过 `log^C X` | 否则 SC/LV/CE |

## 3. lacunary/dense 二分无回流

任意无穷尺度列按间距二分：

- 若存在强 lacunary 承载子列，则进入 `PI-lacunary`；
- 否则存在 dense pack，进入 `PI-dense/DSO`。

若 lacunary 条件失败，它不是失败事件，而是定义上进入 dense pack。若 dense pack 不能统一，则重新细分为有限或可数个 lacunary/dense 子包；若细分复杂度无界，进入 `CE/LSMP`。因此二分本身无回流。

## 4. DSO bridge 到 PI 的无回流

`DSO/PI bridge` 的关键边为：

`新增独立频率包 -> martingale square-function -> 允许投影检测 -> PI_seed 或容量终端`。

若 square-function 成功但允许投影检测失败，则只有三种可能：

1. 频率包不是允许投影有限交，转 `CE/FCT`；
2. 投影质量被低体积或误差吞噬，转 `LV/LSMP/CE`；
3. 包重叠过高，转 `SC`。

因此不会回到“未检测 DSO 能量”。

## 5. Carleson 容量失败的规范含义

`CapacityFail` 在 PI dense/Carleson 中只能表示两件事：

1. 已证明容量界被反设违反，直接矛盾；
2. 容量界适用条件不满足，按第 2 节转入命名事件。

不能把 `CapacityFail` 作为新终端，也不能从 `CapacityFail` 返回 PI closure 作为前提。

## 6. 主定理

**Theorem PI-Dense-DSO-NoReturn（条件化）。** 在固定复杂度模板、平方可和尾项和已登记外部事件吸收口径下，`PI-lacunary`、`PI-dense/Carleson` 与 `DSO/PI bridge` 的适用条件失败不会产生未命名回流。每条失败边都进入 `CE/LSMP/FCT/LV/SC/DSO/PI_seed/Capacity` 中的已登记节点；若容量界本身被违反，则为对应容量定理的反设矛盾。

**证明。** 第 2 节逐项列出适用条件和失败出口。第 3 节说明 lacunary/dense 二分失败只是进入另一包类型或复杂度事件。第 4 节说明 DSO square-function 若不能反馈 PI，只能因非允许、误差吞噬或高重叠而进入已命名事件。第 5 节规范 `CapacityFail` 含义。故无自由回流。证毕。

## 7. 对容量矩阵的影响

本文把 `PI dense/Carleson 与 DSO bridge 适用条件无回流审查` 从剩余硬点降为条件化可审查接口。当前容量链剩余主要是全局 `log^C X` 常数层级排序，以及最终论文中逐项引用位置的编辑化。
