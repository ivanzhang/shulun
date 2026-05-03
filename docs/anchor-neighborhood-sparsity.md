# Anchor-neighborhood sparsity：从常数线性到对数线性

**状态：** Cross-linear 修正；邻域吸引度实验显示平均度缓慢增长。

## 1. 扫描结果

新增脚本：`experiments/anchor_neighborhood_sparsity_scan.py`。

结果显示每个锚的平均邻域吸引度不是绝对常数，而随 `P` 缓慢增长：

- `P=251`：最高平均度约 `6.8`；
- `P=503`：最高平均度约 `9.0`；
- `P=1009`：最高平均度约 `11`；
- `P=2003`：最高平均度约 `15`。

因此原始 `Cross <= C Q_eff` 可能过强。更现实的目标是

`Cross <= C Q_eff log P`

或 `C Q_eff log log P`。

## 2. 为什么出现对数因子

固定锚 `q`，其命中点数约 `P/q`。每个命中点的 `D=sqrt(P)` 邻域会吸引其它锚图像。对其它锚 `q'` 的命中概率约 `D/q'`。

求和得到

`Σ_{q'>D} D/q' ≈ D * (log log P - log log D)`。

因为 `D=sqrt(P)`，该差约常数倍，但有效锚与粗候选过滤、多个命中点 `P/q` 叠加，会给小锚较高邻域度。实验中最大度集中在较小锚如 `47,53,61`。

因此平均度有对数级增长是合理的。

## 3. 修正后的 Cross 上界

候选引理：

**Cross-log.** 有效锚图像族的小 gap 近碰撞数满足

`Cross <= C Q_eff log P`。

这比 Cross-linear 弱，但仍提供内部结构约束。

## 4. 与矛盾链的关系

近乎完美匹配要求 `Cross >= N-1`，而若 `Q_eff <= (1-η)N`，则 Cross-log 只给

`N <= C(1-η)N log P`，不矛盾。

所以 Cross-log 不能单独闭合。它需要与二阶复用能量结合，作为复用上界的一部分。

## 5. 新组合目标

最终矛盾应不再依赖 `Cross` 单独小于 `N`，而应结合三项：

1. `Q_eff` 有固定比例损耗；
2. 复用能量 `E` 只有线性/对数线性上界；
3. 近乎完美匹配要求同时高覆盖 `A>=N` 和高小 gap 交错 `Cross>=N`。

三者合并可能形成：

`required_energy(A,Cross,N) > available_energy(Q_eff,E,Cross)`。

## 6. 下一步

专攻联合能量，而不是单独 Cross：定义

`Φ = E + λ Cross`

或

`Φ = Σ_q n_q^2 + λ * neighbor_degree(q)`。

列反例给 `Φ` 下界；冷却与邻域稀疏给 `Φ` 上界。寻找可闭合常数。
