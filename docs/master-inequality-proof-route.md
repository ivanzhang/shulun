# Master Inequality 证明路线：从多投影总场到反例排斥

**状态：** 总路线；关键子不等式待证。

## 1. 总目标

要排斥方阵内行反例与列反例，目标不是单独证明某个局部现象，而是证明总场不等式：

`LocalBarrier + BalanceDefect + MirrorDefect >= 1`。

行反例主要需要 `LocalBarrier>=1`；列反例需要再接入 `BalanceDefect` 与 `MirrorDefect`。

## 2. LocalBarrier 的来源

`LocalBarrier=ΔE-ΔC+ΔS+KILL`。

四项含义：

- `ΔS`：小素数非零同余壳迁移；
- `-ΔC`：剩余层容量损失；
- `ΔE`：同余锁相重叠增长；
- `KILL`：补旧洞需要支付的任务量。

平方自由 CRT 保证补多个短差点必须动用独立根基坐标，从而贡献 `SyncLoss`，表现为 `ΔC` 无法自由增长或 `ΔE` 被迫增加。

## 3. BalanceDefect 的来源

完整 CRT 周期中列计数均衡：

`T_1=...=T_{P-1}`。

若列反例存在，即某列前窗口边际为零，则该列在前窗口产生缺陷流低谷。均衡要求周期其它位置回补。

但回补列支撑由 Barrier 新生列决定，不是任意可选。因此定义：

`BalanceDefect = 1` 若所需列回补不在可达 Barrier 支撑中。

最终需证明列反例必导致 `BalanceDefect=1` 或局部 Barrier 非零。

## 4. MirrorDefect 的来源

镜像刚性：

`Z(r,c)=Z(M+1-r,P-c)`。

任何前窗口缺陷低谷都会在周期末端镜像列出现对应结构。若列回补试图避开某列，也必须同时避开镜像列。这进一步削弱可补偿自由度。

定义：

`MirrorDefect = 1` 若 Barrier 支撑不能与镜像配对同时满足。

## 5. 平方自由同步损耗子命题 SFL

**SFL。** 若短差核 `K` 由大根基素数层补洞，且差 `d` 小于这些大素数，则每个短差点需要不同 CRT 坐标；补 `m` 个点需模数乘积至少 `prod_{i=1}^m q_i`。

若该乘积 `>P`，前窗口代表至多一个；若代表存在，则其余覆盖结构被刚性决定，通常触发 Barrier 新生洞。

这是平方自由 CRT 的直接投影。

## 6. 列均衡支撑子命题 CBS

**CBS。** 在极小核迁移图中，Barrier 新生列支撑不能长期避开任意固定列 `c<P`，否则完整 CRT 周期列均衡被破坏。

该命题负责列反例。

## 7. 镜像配对子命题 MPS

**MPS。** 若某列支撑模式可避开 `c`，则镜像要求同时避开 `P-c`；但小壳 CRT 迁移释放列在镜像下成对出现，除非局部 Barrier 为零。由行局部闭合排除 Barrier 为零后，镜像避让不可能。

## 8. 最终证明骨架

1. 假设行反例：某行 `H=empty`。
2. 取前窗口偏序下降链的最后非空极小核到空集的一步。
3. 对该步应用 LocalBarrier。由 SFL、重叠能量、壳迁移释放证明 `LocalBarrier>=1`，矛盾。
4. 假设列反例：某列前窗口无缺陷。
5. 行局部闭合保证每行有缺陷，于是缺陷流必须避开该列。
6. CBS+MPS 与 CRT 列均衡/镜像矛盾。

## 9. 当前最小硬点排序

1. 证明 SFL 的严格版本：短差大层补洞的互异坐标与前窗口代表稀缺。
2. 证明 LocalBarrier 下界：互异坐标同步若有前窗口代表，必产生新洞。
3. 证明 CBS：极小核迁移图的可达支撑覆盖所有列。
4. 接入 MPS：镜像配对排除列避让。

## 10. 相关文件

- `docs/root-generation-squarefree-crt-master-field.md`
- `experiments/squarefree_sync_loss_scan.py`
- `docs/squarefree-sync-loss-scan.md`
- `docs/two-dimensional-defect-field-framework.md`
