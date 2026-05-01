# PC4-Dual/DGap 到终端事件图的匹配审查

本文接续 `docs/rh-pc4-external-event-absorption-audit.md`。目标是核查过密对偶分支，特别是 `DGap` 压缩异常，是否逐项落入已经建立的内部事件图

`A/PI/FCT/SC`

或外部吸收矩阵

`LV/LSMP/NRC/CE/DSO/CapacityFail`。

本文不证明 RH；它消除的是“过密分支是否还留有未命名逃逸口”的审稿风险。

## 1. 过密三分入口

由 `docs/rh-pc4-dual-overdense-closure.md` 与 `docs/rh-pc4-dual-gap-ledger.md`，过密输入给出：

`(ACC_z^0-ACC_z)+(O_z-O_z^0)+DGap_z >= Δ-o(Δ)`。

因此至少发生一项：

1. `ACC_z^0-ACC_z >= cΔ`：ACC 负向同步；
2. `O_z-O_z^0 >= cΔ`：overlap 过剩；
3. `DGap_z >= cΔ`：对偶缺口压缩；
4. 边界/基线接口失败。

匹配如下：ACC 负向同步进入 `A`；overlap 过剩进入 OV2/D 组终端，再由 `PI/FCT/SC/LV/LSMP/NRC/CapacityFail` 接收；边界/基线失败进入 `LV/CE/CapacityFail`。唯一需要细查的是 `DGap`。

## 2. DGap 出口矩阵

`docs/rh-pc4-dual-dgap-decomposition.md` 将 `DGap_z>=cΔ` 分为六类。

| DGap 输出 | 对应事件 | 入口文档 | 说明 |
| --- | --- | --- | --- |
| 短窗/短 Bohr 原子集中 | `SC` | `docs/rh-pc4-short-cluster-descent-ledger.md` | 对偶短簇由同一短簇势函数处理 |
| 低体积盒/可求和尾层 | `LV/LSMP` | `docs/rh-lv-low-volume-principle.md`, `docs/rh-pc4-lsmp-frequency-corollary.md` | 外部吸收矩阵处理 |
| 分散盒质量可投影检测 | `PI` | `docs/rh-pc4-pi-terminal-final-reduction.md` | 负/正偏差平方能量同样触发 PI |
| PI 不可检测但低维谱承载 | `FCT` | `docs/rh-pc4-dual-lowdim-frequency-extraction.md` | 低维频率抽取给 FCT seed |
| 覆盖同步或 overlap 解释 | `A/OV2` | `docs/rh-pc4-acc-sync-ledger.md`, `docs/rh-ov2-overlap-terminal-proof.md` | ACC 正负同步同用 A 账本 |
| 盒/投影/基线接口失败 | `CapacityFail/CE/LV` | 盒有限重叠、投影正交化、PC2 基线文档 | 必须绑定命名容量或接口 |

该矩阵说明：`DGap` 没有第七种内部逃逸类型。

## 3. 盒有限重叠匹配

`docs/rh-pc4-dual-box-overlap.md` 的作用是把 DGap 场局部化到有限重叠盒族。若盒族固定复杂度，则重叠损失为 `log^C X`，可吸收入 `X^{o(1)}`。若有限重叠失败，失败原因只能是：

1. 物理窗低体积/端点异常，进入 `LV/SC`；
2. dyadic 锚层无限细化，进入 `CE/LSMP`；
3. 相位模板复杂度逃逸，进入 `CE/FCT/LSMP`。

因此盒有限重叠失败不是新 DGap 分支，而是外部吸收矩阵中的 `CE/LV/LSMP/CapacityFail`。

## 4. 投影正交化匹配

`docs/rh-pc4-dual-projection-orthogonalization.md` 将分散正质量盒场分解为：

- 允许投影空间 `V_PI`；
- 低维频率/短簇/低体积空间 `V_low`；
- 误差逃逸空间 `V_err`。

若能量落在 `V_PI`，进入 `PI`。若落在 `V_low`，分别进入 `FCT/SC/LV/LSMP`。若落在 `V_err`，进入 `CE/CapacityFail`。这与 PC4 终端图完全匹配。

## 5. 低维频率抽取匹配

`docs/rh-pc4-dual-lowdim-frequency-extraction.md` 处理 PI 不可检测的剩余盒能量。其结论是：若能量不能由 PI 检测，且不在 SC/LV/LSMP/CE，则主要谱支撑落入固定低维 CRT/Bohr 频率族 `Λ_*`，这正是 FCT-Seed 输入。

因此 `DGap -> FCT` 不是跳步，而是：

`DGap 分散盒能量 -> PI 不可检测 -> 低维谱抽取 -> FCT_seed`。

随后由 `FCT-Noether-Descent` 和 `PC4-Terminal-No-Cycle` 接收。

## 6. 符号对称性审查

过密分支中的 `ACC_z^0-ACC_z` 是 ACC 负向同步，而此前 PC4-A 常以正向过剩书写。二者使用同一账本，因为 `docs/rh-pc4-acc-sync-ledger.md` 只依赖固定模板偏差的绝对同相位量级：

`|ACC_z-ACC_z^0| >= cΔ`。

正负号只改变偏差函数方向，不改变 `low/osc/tail` 分解、平方能量压力、FCT 共振或短簇集中。因此 ACC 负向同步合法进入 `A`。

## 7. 匹配定理

**Theorem Dual-DGap-Event-Match。** 假设 Dual-Gap-Ledger、DGap-Decomposition、DGap-Box-Overlap、DGap-Projection-Orthogonalization 与 DGap-LowDim-Frequency-Extraction 的接口成立。则 PC4-Dual 过密分支的每个出口均落入以下集合之一：

`A, PI, FCT, SC, LV, LSMP, CE, DSO, CapacityFail, OV2/D`。

其中内部事件 `A/PI/FCT/SC` 由 `docs/rh-pc4-terminal-final-no-cycle-audit.md` 处理，外部事件由 `docs/rh-pc4-external-event-absorption-audit.md` 处理，`OV2/D` 由既有 OV2/D 组终端接口转入同一集合。因此 PC4-Dual/DGap 不提供新的最终逃逸通道。

**证明。** 过密先由第 1 节三分。ACC 负向同步由第 6 节进入 A；overlap 过剩进入 OV2/D；边界/基线失败进入 LV/CE/CapacityFail。DGap 分支由第 2 节矩阵逐项匹配：集中为 SC，低体积为 LV/LSMP，分散可检测为 PI，分散不可检测为 FCT，覆盖解释为 A/OV2，接口失败为 CapacityFail/CE。所有出口均在声明集合内。证毕。

## 8. 对总攻的影响

结合本审查，RH 总攻中 `E_z>0` 的过密路径可写成：

`过密 -> Dual-Gap-Ledger -> A/OV2/DGap/接口失败 -> PC4 内部无循环图或外部吸收矩阵`。

因此下一步最优硬点转为全文接口一致性：PC1--PC2--PC3--PC4--Dual 的尺度 `X,z,Δ`、符号约定和误差 `o(Δ)` 是否逐项一致。
