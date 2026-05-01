# PC4 终端最终无循环审查：A/PI/FCT/SC 统一事件图

本文在 `docs/rh-pc4-terminal-closure-audit.md` 基础上，合并四个已补强账本：

- `docs/rh-pc4-acc-sync-ledger.md`：ACC/A 同步无循环账本；
- `docs/rh-pc4-pi-terminal-final-reduction.md`：PI seed--dense--lacunary 终端归约；
- `docs/rh-pc4-fct-noether-descent-ledger.md`：FCT Noether 离散下降账本；
- `docs/rh-pc4-short-cluster-descent-ledger.md`：SC 短簇递归下降账本。

目标不是宣称 RH 已证明，而是把 PC4 终端子图从“互相引用的条件化 closure”改写为一个可审查的无循环事件图：每条边要么输出外部终端，要么降低某个离散账本；若不降低，则固定模板重复并由对应账本转入终端。

## 1. 事件集合

定义内部事件

`𝓘={A,PI,FCT,SC}`，

外部吸收事件

`𝓞={LV,LSMP,NRC,CE,DSO,CapacityFail}`。

其中 `DSO` 包括 DSO-C/DSO-E/正交容量上界失败，`CapacityFail` 包括 AAI/局部乘积容量、PI Carleson 容量、DGap 盒容量等接口违反。

## 2. 四个账本的输出边

四个内部事件的输出如下。

### A/ACC

由 `ACC-Sync-No-Cycle`：

`A -> PI / FCT / SC / LV / LSMP / CE / DSO / CapacityFail`。

若 A 试图留在自身内部，则 ACC 势函数下降；若不下降，则固定模板重复，触发上述边。

### PI

由 `PC4-PI-Terminal-Final-Reduction`：

`PI -> FCT / SC / LV / LSMP / NRC / CE / DSO / CapacityFail`。

lacunary 包只按 disjoint 容量记账；dense 包由正交闭合转 DSO/FCT/NRC/LSMP/LV；边界坏包转 SC/CE/LV。

### FCT

由 `FCT-Noether-Descent`：

`FCT -> PI / SC / LV / LSMP / NRC / DSO / CE / CapacityFail`。

真闭包步降低 Noether 势函数；重复关系转 PI/SC 或容量出口。

### SC

由 `SC-Descent-Termination`：

`SC -> PI / A / FCT / LV / LSMP / CE / CapacityFail`。

真 `shorter_SC` 步降低短簇势函数；重复短簇模板转 PI/A/FCT 或容量出口。

## 3. 统一势函数

给每个内部状态附加对应离散势函数：

- `𝓟_A`：ACC 模板复杂度/Bohr 体积/dyadic/过剩容量账本；
- `𝓟_PI`：PI 容量账本，lacunary 为 disjoint 容量，dense 由正交容量控制；
- `𝓟_FCT`：FCT 规范关系秩、Smith/Hermite 指数、Bohr 体积、深度账本；
- `𝓟_SC`：短簇长度、体积、相位自由度、dyadic 层账本。

定义全局词典序势函数

`𝓟_global=(N_switch, 𝓟_A, 𝓟_PI, 𝓟_FCT, 𝓟_SC)`，

其中 `N_switch` 记录在不触发外部终端的前提下尚未规范化固定的事件类型切换次数。每当事件切换后进入新 seed，若无法抽取固定模板，则进入 CE/LSMP/FCT；若能抽取固定模板，则对应分支账本生效。为避免人为循环，采用“段分解”而非逐步比较：把无限路径分成 maximal 同类段。

## 4. 段分解无循环定理

**Theorem PC4-Terminal-No-Cycle。** 假设四个账本定理成立，并且外部事件 `LV/LSMP/NRC/CE/DSO/CapacityFail` 均被上游或附录接口吸收。则内部事件图 `A/PI/FCT/SC` 不存在无限最终逃逸路径。

**证明。** 反设存在无限路径，只访问 `A/PI/FCT/SC` 且不触发外部吸收事件。按事件类型分成 maximal 同类段。

若某一类型出现无限长同类段，则对应账本直接排除：A 用 `ACC-Sync-No-Cycle`，PI 用 `PC4-PI-Terminal-Final-Reduction`，FCT 用 `FCT-Noether-Descent`，SC 用 `SC-Descent-Termination`。

于是每个同类段有限，路径必须无限次切换事件类型。每次切换都来自当前分支账本的“固定模板重复出口”或“真变化出口”。若是固定模板重复出口，则目标事件承载同一个离线零点级异常的可检测投影、频率闭包、短簇或 ACC 同步。进入目标事件后，若它不能固定 seed，则触发 CE/LSMP/NRC；若能固定 seed，则目标账本开始运行。

考虑无限次切换中某个事件类型出现无穷多次。抽取该事件的无穷返回子列。若其规范模板只有有限多种，则某一固定模板重复无穷多次，由该事件的重复出口引理触发外部吸收或另一固定事件的能量发散；沿有限事件类型继续抽取，最终得到某个固定模板的无限同类重复，已被第一段排除。若规范模板无限多种，则复杂度、Bohr 体积层、dyadic 层或相位自由度中至少一项无限真变化；由相应账本，要么离散势函数无限下降，要么进入 CE/LV/LSMP/FCT/NRC，均不可能。

因此无限内部路径不存在。证毕。

## 5. 对 RH 总攻骨架的作用

本审查把 PC4 的显性终端分支统一为一个无循环黑箱接口：

`PC4-Terminal-No-Cycle`。

在 RH 总攻文档中，凡 PC3/PC4-Dual/DGap 把异常送入 A/PI/FCT/SC，均可引用本接口说明：只要外部解析输入、低体积/复杂度吸收、正交容量与局部乘积容量均已无条件化，PC4 内部不会再产生循环逃逸。

## 6. 剩余审稿义务

本文仍保留清晰的数学诚实口径：它闭合的是 PC4 终端事件图的循环结构，不自动证明 RH。剩余义务集中在：

1. 外部事件 `LV/LSMP/NRC/CE/DSO/CapacityFail` 的逐项吸收审查见 `docs/rh-pc4-external-event-absorption-audit.md`；
2. PC4-Dual 与 DGap 接口到 `A/PI/FCT/SC` 的精确匹配；
3. PC1--PC3 到 PC4 输入的常数和尺度一致性审查。
