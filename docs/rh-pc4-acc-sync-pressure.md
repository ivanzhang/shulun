# PC4-A：ACC 同步压力命题

本文接续 `docs/rh-pc4-acc-seed.md`。ACC-Seed 已把无穷多 ACC 过剩归约为固定组件、固定覆盖模板与同相位子列。本文证明下一层压力命题：固定 ACC 模板若在无穷多尺度上同向产生 `X^β` 级过剩，则该过剩必须表现为可检测投影能量、频率闭包，或短簇/低体积集中。因此在 PC4-PI 与 PC4-FCT 已条件化闭合后，ACC 同步不能作为独立最终通道。

## 1. 固定 ACC 模板的偏差函数

由 ACC-Seed，固定覆盖模板 `𝓐_*` 后，每个尺度有局部偏差函数

`a_X(n)=1_{𝓐_*(X)}(n)-E_0 1_{𝓐_*(X)}(n)`，

其平滑总偏差为

`A(X)=Σ_n a_X(n)W(n/X)`。

同向 ACC 过剩表示在无穷子列上

`A(X_j) >= c X_j^{β-o(1)}`, `β>1/2`,

且相位与同一离线零点短弧一致。

## 2. 频率分解

固定模板 `𝓐_*` 由有限锚层、倒数相位、Bohr 切片和 dyadic 窗口组成。对每个尺度，作局部 Fourier/Vaaler 分解：

`a_X = a_X^{low} + a_X^{osc} + a_X^{tail}`。

其中：

- `low` 是零频和低体积边界项；
- `osc` 是有限个非主 CRT/Euler 局部频率；
- `tail` 是截断尾项与小质量原子。

Tail 与低体积项若承载主偏差，则转入 LSMP/LV 或短簇。因此非终端状态下，主偏差必须来自 `osc`。

## 3. 同步压力到投影或 FCT

**Lemma A-SP1（固定模板同步压力）。** 若固定 ACC 模板 `𝓐_*` 的振荡部分在无穷多尺度上同向承载 `X^β` 级偏差，则至少发生一项：

1. 存在允许投影窗口 `B_X`，满足高投影增量条件，转入 PC4-PI；
2. 主振荡频率落入低维祖先 span，转入 PC4-FCT；
3. 非主频率平方和超过 DSO/CE 容量界，矛盾。

**证明。** 对 `osc` 的有限频率展开做 dyadic pigeonhole。若某个可检测窗口或频率包承载固定比例偏差，则其条件期望相对零频基线产生高投影增量，进入 PC4-PI。若该频率包的非共振估计失败，则按 NRC/FCT 口径进入 PC4-FCT。若所有频率包都分散且非共振，则 DSO-E/DSO-C 与 PC4-PI-Dense 的平方容量界控制总振荡能量，不能支撑 `X^β` 级同向偏差。证毕。

## 4. Tail/低体积分支

**Lemma A-SP2（不可检测部分转 LSMP/LV/短簇）。** 若 `low` 或 `tail` 承载固定 ACC 模板的主过剩，则触发 LSMP、LV 或短簇。

**证明。** `low` 的非零贡献只能来自边界、低体积集合或零频基线偏差；零频基线已在 `ACC^0` 中扣除，剩余边界/低体积由 LV 吸收。`tail` 若不可平方求和，则由 `docs/rh-pc4-complexity-escape-interface.md` 与 `docs/rh-pc4-lsmp-frequency-corollary.md` 转入 LSMP；若集中于短窗或低维 Bohr 交集，则为短簇。证毕。

## 5. ACC-Sync-Pressure 主命题

**Proposition ACC-Sync-Pressure（ACC 同步压力，条件化）。** 若固定 ACC 模板 `𝓐_*` 在无穷多尺度上产生同相位 `X^β` 级过剩，`β>1/2`，则至少发生一项：

1. `PC4-PI` 高投影增量分支；
2. `PC4-FCT` 频率闭包分支；
3. 短簇；
4. `LSMP/LV` 低质量或低体积逃逸；
5. DSO/CE 容量矛盾。

**证明。** 对固定模板偏差作第 2 节分解。若主贡献来自 `low/tail`，由 A-SP2 转终端。否则来自 `osc`，由 A-SP1 转入 PC4-PI、PC4-FCT 或容量矛盾。证毕。

## 6. 对 PC4-A 的影响

结合 `docs/rh-pc4-acc-seed.md`：若 ACC 过剩可作为最终通道，则存在固定模板同步种子。本文表明固定模板同步种子不能保持为独立通道，必须进入 PC4-PI、PC4-FCT、短簇、LSMP/LV 或容量矛盾。

由于 PC4-PI 与 PC4-FCT 已有条件化闭合，PC4-A 的剩余任务缩小为：

1. 把短簇分支交给 PC4-SC；
2. 把 LSMP/LV 与容量矛盾引用到最终总框架；
3. 合并 ACC-Seed 与 ACC-Sync-Pressure，写出 `PC4-A-Closure`。

下一步最优专攻是 `PC4-A-Closure`，然后转向 PC4-SC。
