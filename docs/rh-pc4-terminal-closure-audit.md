# PC4 终端输入审查：A/SC/PI/FCT closure 依赖图

本文进入 RH 总攻框架第 5 项“终端输入”。目标是审查 `PC4-A`、`PC4-SC`、`PC4-PI`、`PC4-FCT` 四个 closure 的依赖关系，避免循环证明，并把剩余义务压缩成可排序的容量账本与 Noether 终止问题。

## 1. 四个终端分支

当前 PC4 显性终端分支为：

1. `PC4-A`：ACC 同步过剩/不足；
2. `PC4-SC`：短簇集中；
3. `PC4-PI`：高投影增量；
4. `PC4-FCT`：频率闭包。

它们相互转化：ACC 同步可转 PI/FCT/SC；短簇可转 PI/A/FCT；PI 的复杂度或非共振失败可转 FCT/LSMP；FCT 漂移压力可转 PI/SC/LSMP。

## 2. 防循环原则

终端 closure 不应写成“互相假设已闭合”后直接闭合。正确口径应为：

1. 每个分支先给出 Seed：若它作为最终逃逸通道，则可抽取固定复杂度、同相位、非终端子列；
2. 然后给出 Pressure：固定逃逸通道若持续，则产生更低复杂度、可求和体积下降、平方能量增长或新终端；
3. 失败分支只允许返回到“Seed/终端事件”，不能引用对方的最终 closure 作为证明前提；
4. 最后用全局有限下降或能量容量上界统一排除无限循环。

因此最终闭合顺序应是“事件图无无限路径”，而不是四个定理两两互相引用。

## 3. 事件图

定义终端事件集合：

`𝓔={A_seed, SC_seed, PI_seed, FCT_seed, LSMP, LV, NRC, CE, CapacityFail}`。

各 closure 应改写成事件图边：

- `A_seed -> PI_seed / FCT_seed / SC_seed / LSMP / LV / CE / CapacityFail`；
- `SC_seed -> PI_seed / A_seed / FCT_seed / LV / LSMP / shorter_SC`；
- `PI_seed -> FCT_seed / LSMP / LV / NRC / CE / CapacityBound`；
- `FCT_seed -> PI_seed / SC_seed / LSMP / LV / lower_FCT / CapacityFail`。

需要证明：在排除 `LSMP/LV/NRC/CapacityFail` 后，`A/SC/PI/FCT` 子图不存在无限逃逸路径。

## 4. 可用下降量

当前文档中已出现的下降量包括：

1. **复杂度秩**：FCT-Noether 中的低维 span 秩/深度；
2. **体积预算**：SC 中短窗长度、Bohr 半径、局部乘积容量；
3. **平方能量预算**：PI 中固定模板投影能量；
4. **覆盖模板复杂度**：A 与 CE 中固定 ACC 模板或复杂度逃逸。

若某条路径不降低这些量，则它必须在同一固定模板/同相位子列上重复承载 `X^{β-o(1)}` 级异常，触发 PI 能量发散或 ACC 同步压力；若降低，则不能无限下降。

## 5. 终端输入合并命题

**Proposition Terminal-Closure-Reduction（PC4 终端闭合归约）。** 若以下四类输入成立：

1. `PI` 固定模板能量上界；
2. `FCT` Noether 闭包链终止；
3. `SC` 局部容量/体积下降；
4. `A` ACC 同步压力转事件图边；

并且 `LSMP/LV/NRC/CapacityFail` 均被外部输入排除或吸收，则 `A/SC/PI/FCT` 不能形成无限最终逃逸通道。

**证明。** 反设存在无限逃逸路径。若路径中某个下降量无限严格下降，因下降量离散且有下界，矛盾。若最终稳定在固定复杂度、固定体积、固定相位模板上，则固定模板反复承载离线零点级异常：若表现为投影能量，违背 PI 容量上界；若表现为频率闭包，违背 FCT-Noether；若表现为短簇局部密度，违背 SC 容量；若表现为覆盖同步，违背 A 同步压力。故无无限路径。证毕。

## 6. 下一步硬点排序

为了把第 5 项从事件图归约推进到可审稿闭合，建议依次审查：

1. `PC4-PI`：终端输入审查见 `docs/rh-pc4-pi-terminal-audit.md`；dense 包已由正交输入支撑，剩余硬点是 PI-Lacunary-Capacity；
2. `PC4-FCT`：Noether 闭包链是否有明确离散下降量；
3. `PC4-SC`：shorter_SC 递归的严格体积/长度下降账本见 `docs/rh-pc4-short-cluster-descent-ledger.md`；
4. `PC4-A`：ACC 同步压力是否只转事件图边而不引用最终 closure。

完成这四项后，第 5 项终端输入可从“条件化 closure”升级为“无循环终端事件图闭合”。
