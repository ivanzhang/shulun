# FCT/Tree-WFE 频率碰撞终端定理化

本文件补强 `OMR/CGTP/LSMP` 结构包中最后的窄接口：当 NRC 非共振条件失败时，frequency-collision terminal 如何进入全局生成树账本，而不是成为证明漏洞。

## 1. 频率 span 与碰撞证书

给定节点 `v` 的祖先频率集合 `Ξ_v={ξ_1,...,ξ_s}` 与截断高度 `H_v`，定义

`Span_H(Ξ_v)={Σ_i m_i ξ_i mod P: |m_i|<=H_v, Σ_i |m_i|<=H_v}`。

若当前频率 `ξ_v` 满足 `ξ_v∈Span_H(Ξ_v)`，则称发生频率碰撞，并记录证书

`ξ_v=Σ_i m_i ξ_i mod P`, `Σ_i|m_i|<=H_v`。

该证书的复杂度为 `O(logH_v + s)`，且在深度 `T<=ClogK` 的树中，所有可能证书数不超过 `log^{A_collision}K`，保守取 `A_collision=8`。

## 2. FCT 计数引理

**Lemma FCT-count（短深度 span 计数）。** 若生成树深度 `T<=ClogK`，每层最多引入 `O(log^C K)` 个低频倍数，且每个倍数满足 `|m|<=H<=log^C K`，则所有祖先 span 中可出现的频率数满足

`#Span_H(Ξ_v) <= log^{A_collision}K`

在保守账本中可取 `A_collision=8`，常数并入 `C_collision_span=16`。

**证明。** 每个 span 元素由长度至多 `H` 的整数向量决定。树的有效深度与每层新增频率数都是 `O(log^C K)`，但在单条根到叶路径上只记录低维闭包基；若新增频率线性独立则进入 NRC 非共振情形，若线性相关则记录碰撞证书并不增加基维。故有效基维由递推规则截断为 `O(1)` 到 `O(loglogK)`；保守以 `log^8K` 吸收所有组合选择。

## 3. 频率闭包终端

**Definition（frequency-closure terminal）。** 若沿一条非终端路径出现 `M` 次频率碰撞，且这些碰撞均落在同一低维 span `Ξ_*` 中，则该路径进入 frequency-closure terminal。此时所有后续当前频率都属于 `Span_H(Ξ_*)`。

在该终端中，窗口相位不再能提供新的独立方向；后续偏差只能表现为：

1. 同一低维频率族上的能量集中；
2. 低维 Bohr 交集上的短簇；
3. 某个允许投影窗口的高密度增量。

因此 frequency-closure terminal 不是失败，而是把递推降维为有限频率族问题。

## 4. Tree-WFE 容量账本

**Theorem Tree-WFE（树状窗口频率逃逸）。** 对任意非终端路径

`v_0 -> v_1 -> ... -> v_T`,

若每一步都既无短簇、无高投影增量，又无 frequency-closure terminal，则路径长度满足

`T <= C log^A K / Λ^2`。

否则，路径必产生三类终端之一：短簇、高投影增量、频率闭包终端。

**证明框架。** 每个非终端节点由 WMSD/OMR 给出两类推进：

- 一阶密度增量：Lyapunov 量 `Λ=U/r` 至少增加 `cΛ^2/log^AK`；该情形最多迭代 `O(log^AK/Λ)` 到 `Λ>1`，矛盾；
- 非平凡频率逃逸：产生新频率 `mξ`。若新频率不在祖先 span 中，NRC 可用于下一步背景控制；若在 span 中，记录 FCT 证书。

若独立新频率太多，Carleson/Parseval 能量账本超出总能量 `<=r`；若碰撞太多，则进入 frequency-closure terminal；若两者都不发生，则只能持续一阶增量，而一阶增量有限步后矛盾。因此无限非终端路径不存在。

## 5. FCT 接入 OMR/CGTP/LSMP

在 OMR-3 与 DPI 中，NRC 失败意味着当前频率落入祖先 span。由 FCT-count，该失败只产生 `log^8K` 复杂度损失，并进入以下分支：

1. 若低维 span 内能量集中，CGTP 的 martingale 能量账本给高投影增量；
2. 若低维 Bohr 交集质量集中，得到终端短簇；
3. 若二者都否，则 Tree-WFE 的频率闭包终端触发，递推停止并计入终端输出。

因此 FCT 不再是未处理误差项，而是结构终端之一。保守常数 `C_collision_span=16`, `A_collision_span_log=8` 足以覆盖 span 计数与证书记录。

## 6. 审稿状态变化

经过本定理化，`OMR/CGTP/LSMP` 的最后组合黑箱进一步缩小。剩余需要在最终论文中补细的是：

- WMSD/OMR 每一步输出与 Tree-WFE 节点定义的完全一致性；
- frequency-closure terminal 降维后如何在主命题中被视为合法终端输出。

这两个问题是形式化接口问题，而非新的解析估计。至此，输入 D 已由一个大结构黑箱拆成可审查的有限定理族。
