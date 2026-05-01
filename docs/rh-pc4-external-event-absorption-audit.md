# PC4 外部事件吸收总审查：LV/LSMP/NRC/CE/DSO/CapacityFail

本文接续 `docs/rh-pc4-terminal-final-no-cycle-audit.md`。PC4 内部事件图 `A/PI/FCT/SC` 已被统一无循环账本处理；剩余义务是核查外部事件

`𝓞={LV,LSMP,NRC,CE,DSO,CapacityFail}`

是否都有明确入口、吸收机制和不可回流口径。本文不宣称 RH 已证明；它给出 PC4 外部出口的审稿矩阵，使后续总攻可以逐项检查外部输入，而不让它们重新变成 PC4 内部循环。

## 1. 吸收矩阵

| 外部事件 | 主入口 | 吸收机制 | 不可回流口径 |
| --- | --- | --- | --- |
| `LV` | `docs/rh-lv-low-volume-principle.md` | 有效体积 `Vol_eff<=X/log^{B+C}X` 时平凡估计吸收 | 若平凡估计失效，只能记录为 SC 或 LSMP，不返回裸 LV |
| `LSMP` | `docs/omr-cgtp-lsmp-theoremization.md`, `docs/rh-pc4-lsmp-frequency-corollary.md` | 小质量原子/薄层 coarea + DPI 吸收 | 若不可吸收，输出 PI/FCT，不引用 PI closure |
| `NRC` | `docs/nrc-theoremization.md`, `docs/external-theorem-package.md` | 非共振完成和/Weil--Kloosterman 界 | 非共振失败定义为 FCT 频率碰撞 |
| `CE` | `docs/rh-pc4-complexity-escape-interface.md` | 复杂度、尾项、旧坐标、边界四分 | 输出 FCT/LSMP/LV/PI-Seed，不作为独立终端循环 |
| `DSO` | `docs/rh-pc4-orthogonality-final-closure-audit.md` | DSO-C Hilbert 鞅平方函数 + DSO-E 匹配 | 失败输出 PI-Seed/FCT/LSMP/LV/NRC |
| `CapacityFail` | AAI/SC-LD/PI-lacunary/DGap 盒容量文档 | 容量界本身的反设矛盾或转入上表事件 | 不作为新事件；必须指明对应容量定理 |

## 2. LV 吸收

`LV` 的编号入口是 `docs/rh-lv-low-volume-principle.md`。其核心引理是平凡体积吸收：若有效支撑大小低于主误差预算一个对数余量，则所有 dyadic、Fourier、平滑和 divisor-bounded 损失可被对数余量吸收。

PC4 中出现 LV 的情形包括：短簇体积降到底层、ACC 边界低体积、PI 边界坏包、CE 边界体积逃逸。统一处理如下：若满足 LV 体积条件，则吸收；若不满足，则该对象已不是低体积事件，必须按其结构转为 SC、LSMP、PI 或 A，而不能继续称为 LV。

## 3. LSMP 吸收

LSMP 的主体入口是 `docs/omr-cgtp-lsmp-theoremization.md`，频率原子版本入口是 `docs/rh-pc4-lsmp-frequency-corollary.md`。其作用是处理小质量原子、薄层族、频率原子分散与不可控尾项。

不可回流原则：LSMP 失败时只允许输出两类边：

1. 方向筛选/DPI 产生允许窗口偏差，输出 `PI_seed`；
2. 频率原子落入短深度 span，输出 `FCT_seed`。

因此 LSMP 不引用 PC4-PI 或 PC4-FCT 的最终 closure，只输出 seed，由 `PC4-Terminal-No-Cycle` 接收。

## 4. NRC 吸收

NRC 的主体入口是 `docs/nrc-theoremization.md`，外部引用包是 `docs/external-theorem-package.md`。在 PC4 中，NRC 主要承担两件事：

1. 完整加法/倒数/Kloosterman 型相位的非共振完成和界；
2. 把非共振失败精确定义为频率落入祖先短深度 span，即 FCT。

因此 NRC 的不可回流口径是：成功则给正交容量上界，失败则输出 `FCT_seed`，而不是形成独立未知事件。

## 5. CE 吸收

CE 的入口是 `docs/rh-pc4-complexity-escape-interface.md`。它把固定模板条件失败分为四类：频率复杂度逃逸、尾项能量逃逸、旧坐标重写逃逸、边界体积逃逸。

对应吸收：

- 频率复杂度逃逸：由 DSO-E/NRC/FCT/LSMP 接收；
- 尾项能量逃逸：由 LSMP 或 PI-Seed 接收；
- 旧坐标重写逃逸：由 LV 或 FCT 接收；
- 边界体积逃逸：由 LV/SC/LSMP 接收。

所以 CE 不是第五个 PC4 内部分支，而是“不能固定模板”时的出口分类器。

## 6. DSO 吸收

DSO 的最终入口是 `docs/rh-pc4-orthogonality-final-closure-audit.md`。该文把分散正交能量归为：

1. 固定模板平方可和：DSO-C/TC 控制；
2. 频率复杂度逃逸：DSO-E + NRC/FCT/LSMP 控制；
3. 尾项/边界/旧坐标逃逸：CE 控制；
4. 非共振解析失败：NRC/FCT 控制。

正确事件边是

`DSO failure -> PI_seed / FCT_seed / LSMP / LV / NRC / CE`。

这保证 DSO 不依赖 PC4 终端最终闭合，避免循环。

## 7. CapacityFail 吸收

`CapacityFail` 不是单独数学现象，而是某个已命名容量定理的反设失败。使用时必须指明来源：

- AAI/OV2 主层容量：`docs/rh-ov2-main-layer-capacity-interface.md`；
- SC 局部乘积容量：`docs/rh-pc4-short-cluster-local-density.md`；
- PI lacunary/Carleson 容量：`docs/rh-pc4-pi-lacunary-capacity.md` 与 `docs/rh-pc4-pi-cap-carleson.md`；
- DSO 正交容量：`docs/rh-pc4-orthogonality-final-closure-audit.md`；
- DGap 盒容量：`docs/rh-pc4-dual-box-overlap.md` 与相关 DGap 文档。

若容量界本身已证明，则 `CapacityFail` 是矛盾；若容量界仍是接口，则它应列入对应容量文档的剩余审稿义务，而不能作为 PC4 内部新循环事件。

## 8. 外部事件吸收定理

**Theorem PC4-External-Absorption-Audit。** 在上述入口文档可用的前提下，PC4 外部事件 `LV/LSMP/NRC/CE/DSO/CapacityFail` 不产生新的内部无限逃逸路径。每个外部事件要么被相应估计吸收，要么输出到 `A/PI/FCT/SC` 的 seed 或命名容量矛盾，并由 `PC4-Terminal-No-Cycle` 或对应容量文档处理。

**证明。** 按第 2--7 节逐项核查。LV 成功为平凡体积吸收，失败转结构事件；LSMP 成功为小质量吸收，失败只输出 PI/FCT seed；NRC 成功为完成和界，失败是 FCT；CE 是四分出口分类器；DSO 成功为平方函数容量，失败输出 PI/FCT/LSMP/LV/NRC/CE；CapacityFail 必须绑定到具体容量定理，已证明则矛盾，未证明则保留为命名审稿义务。无一项允许无标记地回到自身或回到 PC4 closure 作为前提。证毕。

## 9. 对总攻的影响

结合 `docs/rh-pc4-terminal-final-no-cycle-audit.md`，PC4 现在有两层闭合口径：

1. 内部层：`A/PI/FCT/SC` 无无限循环；
2. 外部层：`LV/LSMP/NRC/CE/DSO/CapacityFail` 不产生无标记回流。

`PC4-Dual/DGap -> A/PI/FCT/SC/LV/CapacityFail` 的匹配审查见 `docs/rh-pc4-dual-dgap-event-match-audit.md`；该文确认 DGap 压缩异常逐项落入已命名容量、内部 seed 或外部吸收矩阵。
