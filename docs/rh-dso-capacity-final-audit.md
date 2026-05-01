# DSO/容量定理最终审稿矩阵

本文对 PC4 正交输入 `DSO-C/TC/CE/DSO-E` 及相关 `CapacityFail` 做最终审稿级矩阵核查。目标是确认：DSO 成功时只是 Hilbert/CRT 容量上界，失败时只输出已命名事件 `PI/FCT/LSMP/LV/NRC/CE/CapacityFail`，不产生新的 RH 反例逃逸通道。

## 1. DSO 模块矩阵

| 模块 | 核心内容 | 成功输出 | 失败输出 |
| --- | --- | --- | --- |
| `DSO-C` | 逆极限 CRT martingale square-function | 平方能量容量上界 | 无；这是 Hilbert 正交定理 |
| `TC` | 固定模板自然细化接入 DSO-C | 固定模板满足 square-function | `CE/LSMP/FCT/LV` |
| `CE` | 模板复杂度、尾项、旧坐标、边界逃逸四分 | 无独立成功态 | `FCT/LSMP/LV/PI_seed` |
| `DSO-E` | 新增 Euler 局部因子去相关 | 局部平方可控，回到 DSO-C | `NRC/FCT/LSMP/PI_seed` |
| `Orthogonality-Final` | 合并 DSO-C/TC/CE/DSO-E | 分散能量不是独立逃逸 | 输出到 PC4 事件图或外部吸收 |

## 2. DSO-C：纯 Hilbert 容量上界

`docs/rh-pc4-dso-crt-martingale.md` 的核心是：在 CRT 逆极限概率空间上，martingale differences 两两正交，故

`Σ_k ||D_kF||_2^2 <= ||F||_2^2`。

该结论是无条件 Hilbert 空间事实，不依赖 RH、NRC 或 PC4 closure。它只要求待估对象确实来自同一固定模板的自然细化；这个要求由 TC 或 CE 分流处理。

## 3. TC：固定模板一致性

`docs/rh-pc4-dso-template-consistency.md` 说明：有限个倒数环带、短弧、Bohr 切片及其有限并差，在固定复杂度和平方可和截断误差下，可以接入 DSO-C。

若 TC 失败，失败原因只可能是：

1. 复杂度无界，进入 `CE/FCT/LSMP`；
2. 截断尾项不可和，进入 `CE/LSMP/PI_seed`；
3. 旧坐标布尔结构重写，进入 `CE/LV/FCT`；
4. 边界体积不可吸收，进入 `LV/SC/LSMP`。

因此 TC 失败不是新的正交逃逸。

## 4. CE：复杂度逃逸分类器

`docs/rh-pc4-complexity-escape-interface.md` 已把 CE 四分为：频率复杂度、尾项能量、旧坐标重写、边界体积。对应出口为：

`CE -> FCT / LSMP / LV / PI_seed`。

CE 不引用 PC4 最终 closure，只输出 seed 或外部事件，由 `docs/rh-pc4-terminal-final-no-cycle-audit.md` 和 `docs/rh-pc4-external-event-absorption-audit.md` 接收。

## 5. DSO-E：Euler 局部去相关

`docs/rh-pc4-dso-e-unconditionalization-audit.md` 与 `docs/rh-pc4-dso-euler-match-audit.md` 已将 DSO-E 拆为：

- E1：有限群字符正交，无条件；
- E2：倒数/混合相位，调用 `EXT-KL/NRC`；
- E3：可控多频 Gram 矩阵界；
- E4：大复杂度剥离，输出 `FCT/LSMP` 或返回 E3。

因此 DSO-E 成功回到 DSO-C 的平方容量账本；失败只输出 `NRC/FCT/LSMP/PI_seed`。

## 6. CapacityFail 绑定规则

`CapacityFail` 必须绑定到具体容量定理，不能作为自由黑箱。当前可绑定项为：

1. `DSO` 正交容量：`docs/rh-pc4-orthogonality-final-closure-audit.md`；
2. `PI` lacunary/Carleson 容量：`docs/rh-pc4-pi-lacunary-capacity.md`、`docs/rh-pc4-pi-cap-carleson.md`；
3. `SC` 局部乘积容量：`docs/rh-pc4-short-cluster-local-density.md`；
4. `DGap` 盒有限重叠/投影容量：`docs/rh-pc4-dual-box-overlap.md`、`docs/rh-pc4-dual-projection-orthogonalization.md`；
5. `OV2/MLC` 主层容量：`docs/rh-ov2-mlc-unconditional-core.md`、`docs/rh-ov2-mlc-uniform-absorption.md`。

若容量定理已证明，`CapacityFail` 是矛盾；若容量定理仍条件化，则它必须留在对应文档的审稿义务中，而不能回流为 DSO 或 PC4 内部事件。

## 7. DSO/容量最终定理

**Theorem DSO-Capacity-Final-Audit。** 当前总攻链条中，所有 DSO/正交容量分支均满足：成功时给 Hilbert/CRT/Carleson/局部乘积容量上界；失败时只输出 `PI_seed, FCT_seed, SC, LV, LSMP, NRC, CE` 或命名 `CapacityFail`。因此 DSO/容量分支不提供新的未命名最终逃逸通道。

**证明。** DSO-C 是 Hilbert 正交；TC 将固定模板接入 DSO-C，失败转 CE；CE 四分转 FCT/LSMP/LV/PI；DSO-E 成功回 DSO-C，失败转 NRC/FCT/LSMP/PI。其它容量失败按第 6 节绑定到具体容量定理。所有出口均已由 PC4 终端无循环审查或外部事件吸收矩阵接收。证毕。

## 8. 下一步最优硬点

DSO/容量审稿完成后，剩余最优硬点转向 `LSMP/FCT/CapacityFail` 的最终闭合强度：特别是 LSMP coarea/DPI、FCT Tree-WFE 与各容量定理的证明细节是否足够审稿级。
