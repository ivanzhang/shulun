# PC3-OV2 无条件化合并审查

本文审查 PC3-OV2 桥接定理中 AAI/PPI/MLC 三接口的无条件化进度，并明确剩余依赖已经从“OV2 黑箱”转移到 FCT、LV/LSMP、DSO/PI、NRC/EXT 与终端 closure。本文不宣称 RH 已证明；它说明 PC3-OV2 的内部结构接口已经拆开并定理化到当前可审查粒度。

## 1. PC3-OV2 目标

PC3-OV2 要证明：若平滑窗口内素数过疏

`P_z<=P_z^0-Δ`, `Δ=X^{β-o(1)}`, `β>1/2`，

则或者允许覆盖容量出现过剩，或者 overlap 大到触发 D 组终端。

代数核心是

`B_z-B_z^0>=Δ-o(Δ)`，

以及

`ACC_z=B_z-O_z`。

小 overlap 给 ACC 过剩；大 overlap 进入 OV2。

## 2. AAI 状态

AAI 负责解释 overlap 的语义。当前状态：已无条件化。

入口：`docs/rh-ov2-aai-unconditional-theorem.md`。

已证明内容：

1. 真实最小锚账本唯一；
2. overlap 是允许锚相对真实最小锚的正部扣重；
3. 允许 overlap 受整除上包络逐点控制；
4. 任一正 overlap 点产生同层或跨层双锚正规形 `n=q_1q_2r`；
5. 方阵/圆柱斜线覆盖模型是整除上包络子模型。

剩余依赖：无内部黑箱；后续只使用其输出正规形。

## 3. PPI 状态

PPI 负责把双锚正规形推送到倒数相位窗口。当前状态：核心已无条件化。

入口：`docs/rh-ov2-ppi-unconditional-theorem.md`。

已证明内容：

1. `n=q_1q_2r` 在固定模和投影方向下产生单/双倒数相位；
2. D 组可检测偏差给出有限复杂度窗口偏差；
3. 窗口偏差可 Fourier/Vaaler 展开为倒数指数和；
4. 倒数和按非共振、FCT 共振、复杂度/截断逃逸三分。

剩余依赖：非共振上界交给 NRC/EXT；共振交给 FCT；复杂度逃逸交给 CE/LSMP。

## 4. MLC 状态

MLC 负责说明大 overlap 不能藏在尾层或不可检测均匀背景。当前状态：容量核心与不可检测吸收均已拆分定理化。

入口：

- `docs/rh-ov2-mlc-unconditional-core.md`；
- `docs/rh-ov2-mlc-uniform-absorption.md`。

已证明/拆分内容：

1. 低尾层 `R<log^{A_1}X` 有强对数节省；
2. 近平方边界层归入低尾层或短簇；
3. 大能量经 dyadic pigeonhole 定位到主层；
4. 主层门槛可压过 NRC 平方根量级；
5. 不可检测质量四分为 FCT、SC/LV、DSO/PI、Uniform；
6. Uniform 背景由零频容量界吸收。

剩余依赖：FCT、LV/LSMP、DSO/PI、NRC/EXT 是全局终端/正交输入，不再属于 MLC 内部黑箱。

## 5. 合并后的 PC3-OV2 定理状态

**Proposition PC3-OV2-Internal-Closure（PC3-OV2 内部接口闭合）。** 在 PC1/PC2 已给出过疏输入和基线匹配的前提下，PC3-OV2 的 AAI/PPI/MLC 内部接口已被以下文档替代：

- AAI：无条件代数定理；
- PPI：无条件相位推送核心；
- MLC：无条件容量核心 + 不可检测均匀质量吸收。

因此 PC3-OV2 剩余假设只包括：

1. NRC/EXT 非共振完成和；
2. FCT 频率闭包终端；
3. LV/LSMP 低体积/小质量吸收；
4. DSO/PI 正交能量控制；
5. PC4 对 ACC/SC/PI/FCT 的最终排斥。

**证明。** 大 overlap 先由 AAI 转为双锚正规形；MLC 把能量定位到主层或转入低体积/短簇；主层可检测部分由 PPI 推送到倒数窗口，再由 NRC/FCT/PI 处理；不可检测部分由 MLC-Uniform-Absorption 转入 FCT、SC/LV、DSO/PI 或零频背景。故 OV2 内部三接口已不再作为单独黑箱。证毕。

## 6. 对总攻顺序的影响

第三项“覆盖输入”现在可以视为内部拆解完成。下一步总攻应转向第 4 项“正交输入”：

1. DSO-C 已有 Hilbert/martingale 核心；
2. 需要继续审查 DSO-E Euler 局部因子去相关；
3. 模板一致性与 Complexity-Escape 需检查是否仍有循环依赖；
4. LV/LSMP 与 FCT/PI closure 作为终端输入继续排队无条件化。

这意味着 RH 总攻骨架的压力点已经从 PC3-OV2 内部转移到 PC4 的正交和终端闭合输入。
