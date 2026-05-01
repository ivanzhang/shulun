# PC3-OV2 上游输入无条件化审查：AAI/PPI/MLC 三接口

本文补强 `docs/rh-pc3-ov2-unconditionalization-audit.md`，把 PC3-OV2 从“条件化覆盖桥接”整理为上游输入矩阵：哪些部分已经是代数/初等无条件，哪些部分只是输出到 PC4 内部事件或外部吸收矩阵。目标是消除 `AAI/PPI/MLC` 作为未拆黑箱的风险。

## 1. PC3-OV2 输入与输出

输入来自 PC1/PC2：

`P_z<=P_z^0-Δ`, `Δ=X^{β-o(1)}`, `β>1/2`，

以及 PC2 已无条件化的

`B_z-B_z^0>=Δ-o(Δ)`。

PC3-OV2 需要输出：

1. `ACC_z>=ACC_z^0+cΔ`，进入 `A`；或
2. overlap/D 组终端，进入 `SC/PI/FCT/LV/LSMP/NRC/DSO/CE/CapacityFail`。

## 2. 三接口状态矩阵

| 接口 | 核心任务 | 当前状态 | 输出/依赖 |
| --- | --- | --- | --- |
| `AAI` | overlap 语义与双锚正规形 | 无条件代数定理 | 输出 `n=q_1q_2r` |
| `PPI` | 双锚到倒数相位窗口 | 代数+Fourier/Vaaler 无条件核心 | 非共振到 NRC， 共振到 FCT，复杂度到 CE/LSMP |
| `MLC-Core` | 主层容量与 dyadic 定位 | 初等容量无条件核心 | 低体积到 LV/SC，主层到 PPI |
| `MLC-Uniform` | 不可检测质量吸收 | 条件化到已列全局接口 | 输出 FCT/SC/LV/LSMP/DSO/PI/Uniform |

因此 PC3 内部只剩“事件输出”，不再有未命名 OV2 黑箱。

## 3. AAI 无条件块

`docs/rh-ov2-aai-unconditional-theorem.md` 已证明：

- 真实最小锚唯一；
- 允许锚必须整除 `n`；
- overlap 是允许锚相对真实最小锚的逐层正部扣重；
- overlap 受整除上包络逐点控制；
- 正 overlap 给同层或跨层双锚正规形 `n=q_1q_2r`。

该部分不依赖解析数论，也不依赖 PC4 closure。它是纯代数/定义级上游输入。

## 4. PPI 无条件核心与出口

`docs/rh-ov2-ppi-unconditional-theorem.md` 已证明可无条件化的核心：

- 双锚正规形在局部投影下给倒数相位；
- 有限窗口检测由 σ-代数层蛋糕得到；
- 窗口指标由 Vaaler/Fourier 截断展开；
- 频率项按非共振、FCT 共振、复杂度/截断逃逸三分。

PPI 不直接证明 NRC 或 FCT；它只输出清晰事件边：

`PPI -> PI/NRC/FCT/CE/LSMP`。

这些事件已由 `docs/rh-pc4-external-event-absorption-audit.md` 与 `docs/rh-pc4-terminal-final-no-cycle-audit.md` 接收。

## 5. MLC 容量核心与均匀吸收

`docs/rh-ov2-mlc-unconditional-core.md` 给出主层容量的初等核心：

- `Q^2R~X`；
- 体积 `V_{Q,R}<<RQlog^C X`；
- 低尾层 `R<log^{A_1}X` 由 LV 吸收；
- 近平方边界层归入低尾层或短簇；
- 大 overlap 经 dyadic pigeonhole 定位到主层；
- 主层门槛可压过 NRC 平方根量级。

`docs/rh-ov2-mlc-uniform-absorption.md` 处理不可检测主层质量：若不被 PPI 检测，则只能进入 FCT、SC/LV/LSMP、DSO/PI/CE，或作为 Uniform 零频背景由容量吸收。

因此 MLC 的不可检测情形不是新上游假设，而是外部事件矩阵的一组输出边。

## 6. PC3-OV2 上游闭合定理

**Theorem PC3-OV2-Upstream-Unconditional-Audit。** 在 PC2 已给出 `B_z-B_z^0>=Δ-o(Δ)` 的前提下，PC3-OV2 的 AAI/PPI/MLC 三接口可被以下无条件或已命名事件输出替代：

1. AAI：纯代数无条件；
2. PPI：倒数相位推送、窗口检测与 Fourier 截断无条件，失败/余项输出到 NRC/FCT/CE/LSMP/PI；
3. MLC-Core：主层容量、低尾层、近平方边界与 dyadic 定位无条件；
4. MLC-Uniform：不可检测质量输出到 FCT/SC/LV/LSMP/DSO/PI/CE 或零频容量吸收。

故若素数过疏不能产生 ACC 正向过剩，则 PC3-OV2 的所有剩余质量都进入 PC4 内部终端图或外部吸收矩阵。

**证明。** 粗合数过剩若小 overlap，则由覆盖账本直接给 ACC 正向过剩。若 overlap 大，AAI 把 overlap 点转为双锚正规形。MLC-Core 排除低尾层/边界层并定位主层。主层若可检测，由 PPI 推送到倒数相位窗口，再输出 PI/NRC/FCT/CE/LSMP。若不可检测，由 MLC-Uniform 输出 FCT/SC/LV/LSMP/DSO/PI/CE 或零频吸收。所有输出均已命名并被终端/外部审查接收。证毕。

## 7. 对上游无条件化的影响

至此，上游三块状态为：

- PC1：引用级无条件解析输入；
- PC2：初等无条件 CRT 基线；
- PC3-OV2：AAI/PPI/MLC 内部接口拆解完成，剩余均为已命名 PC4 终端或外部事件。

因此总攻的剩余压力不再是“上游输入未拆”，而是：这些已命名事件中的外部定理引用与容量定理是否足够强，尤其是 NRC/EXT、DSO、LSMP/FCT 与 CapacityFail 对应文档的最终审稿级证明。
