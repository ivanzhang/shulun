# PC4-PI：高投影增量分支闭合命题

本文整合 `PI-Seed`、`PI-Cap` 与 `PC4-PI-Dense`，形成 RH 总攻框架中高投影增量分支的可引用闭合命题。本文不宣称证明 RH；它证明的是：在既有终端分支均被排除、且外部 NRC/EXT 输入可用时，高投影增量不能作为 RH 反例链条的最终逃逸通道。

## 1. 输入与目标

假设 PC1+PC2+PC3-OV2 链条在无穷多尺度 `X_j` 上把离线零点异常推入 D 组高投影增量终端。每个尺度给出允许窗口 `A_j` 与归一化增量 `δ_j`，满足

`μ_j(A_j) >= (1+δ_j) μ_j^0(A_j)`,

并有平方能量贡献

`E_PI=Σ_j δ_j^2 μ_j^0(A_j)`。

目标是证明：若高投影增量试图在无穷多尺度吸收离线零点异常，则要么触发既有终端，要么与跨尺度容量上界矛盾。

## 2. PI-Seed：能量下界或逃逸

由 `docs/rh-pc4-pi-seed.md`：若无穷多高投影增量存在，并且有统一复杂度预算子列，则可抽取固定复杂度模板 `𝓦_*` 与同相位无穷子列，使

`Σ_j δ_j^2 μ_j^0(A_j)=∞`

除非低质量逃逸发生。若不存在统一复杂度预算子列，则进入 Complexity-Escape；若低质量逃逸发生，则进入 LSMP/LV/短簇/FCT。

因此，在排除 Complexity-Escape、LSMP、LV、短簇、FCT 后，高投影增量分支必须给出某个固定模板的发散能量种子。

## 3. PI-Cap：lacunary/dense 分包

由 `docs/rh-pc4-pi-cap-carleson.md`，固定模板的跨尺度容量账本按尺度位置分成两类：

1. **lacunary 包**：尺度中心充分分离，包容量由几何重叠与 Carleson 账本控制；
2. **dense 包**：尺度中心密集，不能靠几何分离，需要密集尺度正交。

lacunary 分包给出有限容量贡献；dense 分包由 `docs/rh-pc4-pi-dense-closure-theorem.md` 的 PC4-PI-Dense 处理。

## 4. Dense 分包闭合

PC4-PI-Dense 证明：在无 FCT、无 LSMP、无 LV、无高投影增量返回分支且 NRC/EXT-KL 可用时，任意 dense 包满足

`E_dense(𝓘) <= C(𝓦_*) Cap(𝓘)`。

若该界失败，则触发 FCT、LSMP、LV、PI-Seed/OV2 或 NRC 退化转 FCT。因此在非终端假设下，所有 dense 包总贡献由容量账本控制。

## 5. PC4-PI 主闭合命题

**Theorem PC4-PI-Closure（高投影增量分支闭合，条件化）。** 假设：

1. PC1+PC2+PC3-OV2 在无穷多尺度上产生高投影增量分支；
2. 短簇、FCT、LSMP、LV、ACC 过剩返回、OV2 异常均不作为最终终端；
3. NRC/EXT-KL 解析输入按既有文档可用；
4. PI-Cap 的 lacunary 包容量账本成立；
5. dense 包引用 PC4-PI-Dense。

则高投影增量分支不能作为 RH 反例链条的最终逃逸通道。

**证明。** 反设高投影增量分支在无穷多尺度上吸收离线零点异常且不触发任何终端。由 PI-Seed，在排除复杂度逃逸与低质量逃逸后，抽取固定模板 `𝓦_*`、同相位子列，并得到发散能量种子 `Σδ_j^2 μ_j^0(A_j)=∞`。按 PI-Cap 把该子列分入 lacunary 与 dense 包。lacunary 包由几何/Carleson 容量账本给有限上界；dense 包由 PC4-PI-Dense 给容量上界。两类包合计得到固定模板总能量有限，与 PI-Seed 的发散下界矛盾。因此反设不成立。证毕。

## 6. 失败分支账本

PC4-PI-Closure 的任何失败都不是新通道，而是转入既有分支：

- 复杂度无界：`docs/rh-pc4-complexity-escape-interface.md`；
- dense 正交失败：`docs/rh-pc4-pi-dense-closure-theorem.md`；
- Euler 局部退化：`docs/rh-pc4-dso-euler-decorrelation.md` 与 FCT；
- 小质量分散：`docs/rh-pc4-lsmp-frequency-corollary.md` 与 LSMP；
- 非共振失败：`docs/nrc-theoremization.md` 转 FCT。

因此 PC4-PI 分支现在可在 RH 总攻框架中作为“条件化闭合分支”引用。

## 7. 对 RH 总攻的意义

`docs/rh-pc4-final-exclusion-framework.md` 中 PC4 需要四个跨尺度排斥：ACC、短簇、投影增量、频率闭包。本文把其中的投影增量分支推进为条件化闭合：只要 lacunary 容量账本与 dense closure 被接受，高投影增量无法长期吸收离线零点异常。

下一步 RH 总攻的最优方向是回到 PC4 总框架，选择剩余分支中最可攻的一项：

1. `PC4-FCT`：频率闭包跨尺度排斥；
2. `PC4-A`：ACC 不同步排斥；
3. `PC4-SC`：短簇跨尺度排斥；
4. 必要时补 `PC4-Dual` 处理过密对偶。


## 8. 终端输入审查入口

PC4-PI 在事件图中的归约、dense 包状态与 lacunary 包剩余硬点见 `docs/rh-pc4-pi-terminal-audit.md`。
