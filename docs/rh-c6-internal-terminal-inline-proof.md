# C6 内部终端 A/PI/FCT/SC 内联证明链

本文补 `docs/rh-merge-unconditional-checklist.md` 的 C6。目标是把内部终端 `A/PI/FCT/SC` 从多个互引 closure 文档合并成一条可放入主稿的编号证明链。本文保持严格口径：C6 闭合的是内部事件图的无循环性；外部出口 `LV/LSMP/NRC/CE/DSO`、过疏入口 C4 与外部定理 C10 仍需分别放电。

## 1. 内部与外部事件

定义内部事件集合

`𝓘={A,PI,FCT,SC}`。

外部或已命名吸收事件集合为

`𝓞={LV,LSMP,NRC,CE,DSO}`，

并且 `CapacityFail` 不再作为自由事件：按 C8，它必须替换为具体容量引理成功上界，或替换为进入 `𝓘∪𝓞` 的命名失败出口。

C6 的命题是：若异常进入 `𝓘`，则它不可能只在 `𝓘` 内无限循环并吸收离线零点级异常；每条无限路径必触发 `𝓞` 或与某个容量账本矛盾。

## 2. Lemma C6.1：A/ACC 同步分支

**Lemma C6.1（ACC no-cycle）。** 在排除 `PI/FCT/SC/LV/LSMP/CE/DSO` 的非终端假设下，`A` 分支不能无限承载固定比例异常。

**证明。** A 状态规范化为 `A=(𝓒,𝓐,Q,R,𝓑,ω)`，记录覆盖组件、有限复杂度模板、dyadic 层、CRT/Bohr 切片和离线相位方向。若模板复杂度、Bohr/CRT 切片、dyadic 层或未解释容量账本发生真变化，则由 ACC 势函数

`𝓐pot=C_1cplx+C_2b+C_3h+C_4v`

严格下降，或触发 `CE/FCT/LSMP/LV/SC`。势函数为非负整数加权和，不能无限下降。若真变化有限，则固定 ACC 模板在无穷尺度上重复同向过剩；固定模板的 `low/osc/tail` 分解迫使异常进入 `PI/FCT/SC/LV/LSMP/DSO/CE`。与非终端假设矛盾。证毕。

## 3. Lemma C6.2：PI 投影增量分支

**Lemma C6.2（PI terminal reduction）。** 在排除 `FCT/SC/LV/LSMP/NRC/CE/DSO` 的非终端假设下，`PI` 不能作为最终逃逸通道。

**证明。** PI 输入给固定模板窗口 `A_j` 与能量 `e_j=δ_j^2 μ_j^0(A_j)`。按尺度 Mellin 距离分成 lacunary 包、dense 包和边界坏包。边界坏包若无限承载能量，则进入 `CE/LSMP/LV/SC`。lacunary 包由 disjoint Mellin/Carleson 容量上界控制；若违反容量即触发容量矛盾或 `SC/LV/CE`，若满足容量则不能解释 RH 反例所需的跨尺度同相位压缩。剩余 dense 包由 CRT/Mellin martingale 或 square-function 去相关处理；若正交容量失败，则进入 `DSO/NRC/LSMP/LV/FCT`。因此 PI 不可能在排除这些终端后无限吸收异常。证毕。

## 4. Lemma C6.3：FCT 频率闭包分支

**Lemma C6.3（FCT Noether descent）。** 在排除 `PI/SC/LV/LSMP/DSO/CE/NRC` 的非终端假设下，不存在无限 FCT 闭包链。

**证明。** FCT 状态写为 `S=(Λ,R,𝓑,τ)`，其中 `Λ` 为低维频率格，`R` 为整数关系矩阵，`𝓑` 为 Bohr/倒数切片，`τ` 为深度标签。取 Smith/Hermite 规范形，定义整数势函数

`𝓝(S)=A_1r_free(S)+A_2q(S)+A_3L(S)-A_4τ(S)`。

新证书若在旧 span 外，则不是 FCT，进入 `NRC/DSO/PI`。若固定自由相位、压缩关系指数或细化非冗余 Bohr 层，则 `𝓝` 严格下降或进入 `LV/SC/LSMP`。若无真变化，则是同一规范状态重复；固定状态重复承载同向异常会给 `PI` 投影增量、`SC/LV/LSMP` 集中或 `DSO/CE` 容量出口。故无限 FCT 链不可能。证毕。

## 5. Lemma C6.4：SC 短簇分支

**Lemma C6.4（SC descent）。** 在排除 `PI/A/FCT/LV/LSMP/CE/DSO` 的非终端假设下，短簇 `SC` 不能无限递归。

**证明。** SC 状态由短窗 `I`、dyadic 层 `Q,R`、局部乘积壳、相位自由度和簇长度等数据规范化。局部乘积容量 `Vol_eff(I;Q,R)` 控制固定短窗内 `q_1q_2r` 型锚复用；若容量失败，按 C8 转入具体容量矛盾或 `PI/A/FCT/LV/LSMP/CE`。非失败分支中，SC 的真递归步只能缩短簇长度、降低体积层、固定相位自由度或剥离 dyadic 层；相应短簇势函数严格下降。若真变化有限，则固定短簇模板重复承载异常，触发 `PI/A/FCT` 可检测结构或 `LV/LSMP/CE` 边界低体积事件。证毕。

## 6. Theorem C6：内部事件图无循环

**Theorem C6-Internal-Terminal-No-Cycle.** 假设 C8 的 `CapacityFail` 绑定规则生效，且所有外部出口 `LV/LSMP/NRC/CE/DSO` 均按 C7/C10 或相应主文链接收。则内部事件图 `A/PI/FCT/SC` 不存在无限最终逃逸路径。

**证明。** 反设存在只在 `𝓘` 中运行且不触发外部出口的无限路径。按事件类型分成 maximal 同类段。若某类出现无限长同类段，则分别由 C6.1、C6.2、C6.3、C6.4 排除。于是每段有限，必须无限次切换事件类型。

抽取无限次出现的某个事件类型。若其规范模板只有有限多种，则某一固定模板无穷次返回；沿有限事件图继续抽取，最终得到某个同类固定模板无限重复，已由对应 C6.i 的重复出口排除。若规范模板无限多种，则复杂度、Bohr 体积、dyadic 层、频率关系或短簇自由度中至少一项无限真变化；对应 C6.i 的势函数严格下降或触发 `CE/LV/LSMP/FCT/NRC/DSO`，违背非外部出口假设。因此无限内部逃逸路径不存在。证毕。

## 7. 对割集的影响

C6 可从“待容量绑定”更新为“内部无循环已内联，待外部出口 C7/C10 与过疏入口 C4 放电”。当前剩余真正割集为

`{C1,C4,C10,C11}`。

其中 C4 负责把过疏 PC3/OV2 入口定理化；C10 负责 `EXT-PC1-LI/EXT-KL/EXT-Vaaler` 等正式引用；C11 是 LaTeX 审稿工程。
