# RH 总攻全文接口一致性审查：PC1--PC2--PC3--PC4--Dual

本文核查当前 RH 反例矛盾场骨架中最容易产生审稿问题的接口一致性：尺度 `X,z,M`，异常幅度 `Δ`，符号约定，零频基线，误差 `o(Δ)`，以及事件入口。本文仍不宣称 RH 已证明；它的作用是把条件化总攻链条中所有传递变量统一成一张可审查表。

## 1. 全局变量约定

| 符号 | 统一含义 | 使用范围 |
| --- | --- | --- |
| `X` | 平滑窗口中心尺度，支撑在 `[X/2,2X]` 或同等固定倍区间 | PC1--PC4 |
| `z` | 根基素数截断，取 `z=(log X)^A`, `0<A<1` | PC2--PC4 |
| `M` | CRT 周期 `M=∏_{p<=z}p=exp((1+o(1))z)=X^{o(1)}` | PC2/CRT |
| `Δ` | 离线零点异常幅度 `X^{β-o(1)}`, `β>1/2` | 全链条 |
| `E_z` | 素数异常 `P_z-P_z^0` | PC1--PC4 |
| `C_z` | CRT 候选总量 | PC2 |
| `B_z` | 粗合数候选账本 `C_z-P_z` | PC2--PC4 |
| `ACC_z` | 允许覆盖容量 | PC3/PC4 |
| `O_z` | overlap 扣重 | PC3/PC4/Dual |
| `Gap_z` | 真实粗合数未被允许覆盖解释的缺口 | PC4-Dual |
| `DGap_z` | `Gap_z^0-Gap_z`，对偶缺口压缩 | Dual/DGap |

所有 `o(Δ)` 误差都允许吸收固定对数损失、CRT 边界误差、平滑端点误差与有限重叠 `log^C X` 损失，因为 `M=X^{o(1)}` 且 `Δ=X^{β-o(1)}`。

## 2. 符号传递

定义

`E_z=P_z-P_z^0`。

PC2 给

`C_z-C_z^0=o(Δ)`，因此

`B_z-B_z^0=(C_z-P_z)-(C_z^0-P_z^0)=-E_z+o(Δ)`。

于是：

- **过疏**：`E_z<=-Δ` 推出 `B_z-B_z^0>=Δ-o(Δ)`；
- **过密**：`E_z>=Δ` 推出 `B_z-B_z^0<=-Δ+o(Δ)`。

这正是 PC3 与 Dual 分支的符号入口。后续任何文档若使用“过剩/不足”，都应相对该约定解释。

## 3. 统一覆盖恒等式

采用 `docs/rh-pc4-dual-gap-ledger.md` 的账本约定：

`B_z=ACC_z-O_z+Gap_z+Err_bd`。

相减得

`-E_z=(ACC_z-ACC_z^0)-(O_z-O_z^0)+(Gap_z-Gap_z^0)+o(Δ)`。

这条方程同时支撑两边：

- 过疏时左侧为正，主压力是 `ACC` 正向过剩、`O` 负向或 `Gap` 正向；PC3-OV2 将其整理为 ACC 过剩或 D 组终端。
- 过密时左侧为负，等价于

  `(ACC_z^0-ACC_z)+(O_z-O_z^0)+DGap_z >= Δ-o(Δ)`，

  即 Dual 三分。

## 4. 接口传递表

| 阶段 | 输入 | 输出 | 误差要求 | 下游 |
| --- | --- | --- | --- | --- |
| PC1 | 离线零点 `β>1/2` | `|E_z|>=Δ` 的平滑素数异常 | 权函数非湮灭与对数损失吸收 | PC2 |
| PC2 | `|E_z|>=Δ`，`z=(log X)^A` | `B_z-B_z^0=-E_z+o(Δ)` | `C_z-C_z^0=o(Δ)` | PC3/Dual |
| PC3-OV2 | `E_z<0` | `A` 或 D 组终端 | AAI/PPI/MLC/LV 损失为 `X^{o(1)}` | PC4 内部/外部 |
| PC4-Dual | `E_z>0` | `A/OV2/DGap/接口失败` | Dual-Gap-Ledger 误差为 `o(Δ)` | DGap 匹配 |
| DGap | `DGap>=cΔ` | `SC/PI/FCT/A/LV/LSMP/CapacityFail` | 盒重叠、正交化、低维抽取损失为 `X^{o(1)}` | PC4 终端/外部 |
| PC4 终端 | `A/PI/FCT/SC` seed | 无内部无限逃逸 | 离散账本下降或固定模板重复出口 | 外部吸收 |
| 外部吸收 | `LV/LSMP/NRC/CE/DSO/CapacityFail` | 吸收或回到 seed/命名容量 | 不允许无标记回流 | 总闭合 |

## 5. 事件入口一致性

当前所有事件入口统一如下：

- `A`：`|ACC_z-ACC_z^0|>=cΔ` 的固定模板同步，正负号均允许；
- `PI`：允许投影窗口上出现 `δ^2 μ^0` 发散或 `X^{2β-1-o(1)}` 级平方能量；
- `FCT`：频率落入固定低维短深度 span 并同相位承载异常；
- `SC`：短物理窗、短 Bohr 原子或少数盒承载 `cΔ` 级质量；
- `LV`：有效体积低于主误差预算；
- `LSMP`：小质量原子/薄层族或频率原子分散；
- `NRC`：非共振完成和输入，失败转 FCT；
- `CE`：固定模板失败的复杂度/尾项/旧坐标/边界四分；
- `CapacityFail`：必须绑定具体容量定理，不作为自由事件。

这些入口已分别由 `docs/rh-pc4-terminal-final-no-cycle-audit.md`、`docs/rh-pc4-external-event-absorption-audit.md` 与 `docs/rh-pc4-dual-dgap-event-match-audit.md` 接收；DGap 的投影、低维抽取和 DSO/PI 桥接细节由 `docs/rh-dgap-projection-line-by-line-audit.md`、`docs/rh-dgap-lowdim-extraction-line-by-line-audit.md`、`docs/rh-dso-pi-squarefunction-bridge-audit.md` 补强。

## 6. 发现并修正的格式问题

当前总攻骨架中曾出现两项编号均为 `5` 的输入列表项。应统一为：

1. PC1 解析输入；
2. PC2 CRT 基线；
3. PC3-OV2；
4. PC4 终端无循环事件图；
5. PC4 外部事件吸收矩阵；
6. PC4-Dual/DGap 事件匹配；
7. NRC/EXT、LV/LSMP、AAI/PPI/MLC、DSO/CE 等外部结构接口。

本文同时要求总攻骨架的“剩余无条件化清单”更新为最新状态：PC4 终端、外部吸收与 Dual/DGap 匹配均已有专门总审查，下一步应攻 PC1/PC2/PC3 接口的显式无条件化或逐项引用。

## 7. 一致性定理

**Theorem Global-Interface-Consistency。** 在采用第 1--5 节约定后，当前文档链条中 PC1--PC2--PC3--PC4--Dual 的尺度、符号、异常幅度与事件入口是一致的。任何离线零点异常 `|E_z|>=Δ` 均被传递为：过疏进入 PC3-OV2，过密进入 PC4-Dual；两路最终均落入 PC4 内部无循环事件图或外部吸收矩阵。

**证明。** PC1 给 `E_z` 的带符号异常。PC2 由 `C_z=C_z^0+o(Δ)` 推出粗合数账本反号异常。覆盖恒等式给统一场方程。若 `E_z<0`，符号与 PC3-OV2 入口一致；若 `E_z>0`，符号与 Dual 三分一致。PC3 与 Dual 的全部输出已分别由终端无循环审查、外部吸收审查和 Dual/DGap 匹配审查接收。故接口一致。证毕。

## 8. 下一步最优硬点

接口一致性完成后，真正剩余硬点不再是分支遗漏，而是三个上游输入的无条件化强度：

1. PC1 解析振荡输入的引用级审查见 `docs/rh-pc1-analytic-input-citation-audit.md`；
2. PC2 CRT 基线已由 `docs/rh-pc2-baseline-unconditional-audit.md` 标记为无条件初等输入；
3. PC3-OV2 中 AAI/PPI/MLC 三接口已由 `docs/rh-pc3-ov2-upstream-unconditional-audit.md` 拆为无条件核心与已命名事件输出。
