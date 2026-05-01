# PC4-FCT：频率闭包分支闭合命题

本文合并 `FCT-Seed`、`FCT-Drift` 与 `FCT-Noether`，形成 RH 总攻框架中频率闭包分支的条件化闭合命题。本文不宣称证明 RH；它说明在既有终端分支与容量输入被接受时，FCT 不能作为 RH 反例链条的最终逃逸通道。

## 1. 输入与目标

假设 PC1+PC2+PC3-OV2 链条在无穷多尺度上将离线零点异常推入 FCT 终端。FCT 表示当前频率落入祖先短深度 span，单尺度上由 `docs/fct-tree-wfe-theoremization.md` 记录为频率碰撞证书。

目标是证明：若 FCT 在跨尺度上反复吸收离线零点异常，则它最终必须转入 PC4-PI、短簇、LSMP/LV 或 DSO/CE 容量矛盾，而不能无限停留在频率闭包内部。

## 2. Seed：固定低维编码

由 `docs/rh-pc4-fct-seed.md`，若无穷多尺度由 FCT 吸收，并排除 Complexity-Escape、LSMP、LV、PC4-PI 终端，则可抽取：

1. 固定 FCT 类型 `𝓕_*`；
2. 固定离线相位短弧 `I_*`；
3. 无穷子列 `X_{j_k}`；
4. 固定低维整数关系模板；

使 FCT 低维模型在同一相位方向上吸收 `γlogX_{j_k}` 的偏差。

## 3. Drift：新增 CRT 坐标漂移压力

由 `docs/rh-pc4-fct-phase-drift.md`，固定低维编码若长期成功，则三分：

1. 新增坐标短弧命中只按零频期望发生，无法解释离线零点级同向偏差；
2. 命中超额产生非主局部偏差平方压力，触发 PC4-PI、短簇、LSMP/LV 或 DSO-E 容量矛盾；
3. 产生新的低维同步证书，进入下一层 FCT 闭包。

因此，排除第一、二项后，FCT 唯一可能继续存在的方式是产生无限闭包证书链。

## 4. Noether：闭包链终止

由 `docs/rh-pc4-fct-noether.md` 与 `docs/rh-pc4-fct-noether-descent-ledger.md`，在排除 PC4-PI、短簇、LSMP、LV 与 DSO/CE 容量失败后，FCT 闭包证书链不可能无限延续。其机制是：将 FCT 状态规范化为 Hermite/Smith 代表后，每个真闭包步都降低离散势函数；若势函数不降，则不是新闭包，而是同一 Bohr 交集反复承载偏差，触发 PC4-PI 或短簇。

## 5. PC4-FCT 主闭合命题

**Theorem PC4-FCT-Closure（频率闭包分支闭合，条件化）。** 假设：

1. 无穷多尺度的 RH 反例链条最终由 FCT 吸收；
2. PC4-PI、短簇、LSMP、LV、DSO/CE 容量失败均不作为最终终端；
3. NRC/EXT 解析输入按既有文档可用；
4. FCT 单尺度证书满足 `docs/fct-tree-wfe-theoremization.md` 的 Tree-WFE 接口。

则 FCT 不能作为 RH 反例链条的最终逃逸通道。

**证明。** 反设 FCT 可作为最终逃逸通道。由 FCT-Seed，抽取固定低维编码和同相位子列。由 FCT-Drift，该编码要么只有零频贡献，不能解释离线零点级偏差；要么产生平方能量压力，转入 PC4-PI/短簇/LSMP/LV/容量矛盾；要么生成新的 FCT 闭包证书。前两种与反设矛盾，只剩无限闭包证书链。但 FCT-Noether 排除无限闭包链。因此 FCT 不能作为最终逃逸通道。证毕。

## 6. 对 RH 总攻的影响

PC4-FCT 与 PC4-PI 一样，现已推进为条件化闭合分支：

- PC4-PI 处理高投影增量跨尺度能量；
- PC4-FCT 处理频率闭包跨尺度吸收；
- 两者互相接力：FCT 的能量集中转入 PI，PI 的复杂度/非共振失败转入 FCT。

因此 RH 总攻剩余主分支进一步集中到：

1. `PC4-A`：ACC 不同步排斥；
2. `PC4-SC`：短簇跨尺度排斥；
3. `PC4-Dual`：必要时处理过密对偶。

下一步最优专攻应转向 `PC4-A` 或 `PC4-SC`。从现有 PC3-OV2 链条看，`PC4-A` 更直接承接 ACC 过剩主分支，建议优先攻 `PC4-A`。
