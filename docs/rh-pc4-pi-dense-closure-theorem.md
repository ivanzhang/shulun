# PC4-PI：密集尺度正交闭合命题

本文整合 `DSO-C`、`DSO-C-TC`、`Complexity-Escape`、`DSO-E` 与 `LSMP-Freq`，形成 PC4-PI 可引用的密集尺度正交闭合命题。本文仍不是 RH 证明；它闭合的是 RH 总攻路线中“高投影增量在密集尺度包内不能无成本累积”的结构接口。

## 1. 输入对象

设 `𝓘=[Y,Y^B]` 是密集尺度包，`A_j` 是 PPI/OMR 给出的允许投影窗口，考虑能量和

`E_dense(𝓘)=Σ_{X_j∈𝓘} δ_j^2 μ_j^0(A_j)`。

这里 `δ_j` 是归一化投影偏差，`μ_j^0` 是 CRT 零频候选测度。目标是在非终端假设下证明

`E_dense(𝓘) <= C(𝓦_*) Cap(𝓘)`。

非终端假设包括：无 FCT、无 LSMP、无 LV、无短簇、无高投影增量返回分支，且 NRC/EXT-KL 解析输入可用。

## 2. 固定复杂度分支

若模板满足固定复杂度、自然细化与平方可和误差，则由：

- `docs/rh-pc4-dso-crt-martingale.md` 的 DSO-C martingale square-function；
- `docs/rh-pc4-dso-template-consistency.md` 的 DSO-C-TC；

得到新增 CRT 坐标上的平方函数上界。因此固定复杂度分支满足密集尺度正交容量界。

## 3. 复杂度逃逸分支

若 DSO-C-TC 条件失败，则由 `docs/rh-pc4-complexity-escape-interface.md` 的 Proposition CE，失败只可能来自：

1. 频率复杂度逃逸；
2. 尾项能量逃逸；
3. 旧 CRT 坐标重写；
4. 边界体积逃逸。

尾项、旧坐标与边界逃逸分别进入 LSMP/LV/FCT 或返回 PI-Seed/OV2。频率复杂度逃逸由 DSO-E 处理。

## 4. Euler 局部因子分支

对频率复杂度逃逸，由 `docs/rh-pc4-dso-euler-decorrelation.md`：

- 单新增坐标字符正交给零均值与 Parseval；
- 纯倒数相位由置换正交控制；
- 混合倒数相位由 `EXT-KL`/NRC 的 Kloosterman-Weil 界控制；
- 非共振失败进入 FCT。

多频局部平方控制由 DSO-E3 给出。若局部频率数过大，则 DSO-E4 三分：重 span 进入 FCT；重可控子集返回 DSO-E3；二者皆无进入 LSMP-Freq。

`docs/rh-pc4-dso-euler-match-audit.md` 已核查 DSO-E2 与 NRC/EXT 的匹配；`docs/rh-pc4-lsmp-frequency-corollary.md` 已把 DSO-E4 的小质量分散情形降为 LSMP 推论。

## 5. Dense-Closure 主命题

**Theorem PC4-PI-Dense（密集尺度正交闭合，条件化）。** 在上述输入对象与非终端假设下，固定投影模板 `𝓦_*` 在任意密集尺度包 `𝓘` 上满足

`E_dense(𝓘) <= C(𝓦_*) Cap(𝓘)`。

若该容量界失败，则至少触发以下一项：

1. `FCT` 频率碰撞/低维闭包；
2. `LSMP` 小质量原子逃逸；
3. `LV` 低体积边界终端；
4. 高投影增量返回 `PI-Seed/OV2`；
5. NRC/EXT-KL 解析输入不适用，而这按 NRC 口径同样转入 FCT。

**证明。** 分两类。若模板固定复杂度且误差平方可和，由第 2 节的 DSO-C + DSO-C-TC 得 square-function 容量界。若不满足固定复杂度条件，由第 3 节 CE 四分。尾项、旧坐标与边界逃逸直接进入 LSMP/LV/FCT/PI-Seed。剩余频率复杂度逃逸由第 4 节 DSO-E 控制：非共振局部因子平方可控；退化进入 FCT；过大频率集合由 DSO-E4 与 LSMP-Freq 分解。排除所有终端后，只剩平方可控情形，故得到容量界。证毕。

## 6. 与 PC4-PI 的闭合关系

`docs/rh-pc4-pi-cap-carleson.md` 将 PC4-PI 分成 lacunary super-capacity 与 dense-scale orthogonality。本文闭合 dense-scale orthogonality 的 CRT/Euler 分支：

- lacunary 包：仍由 PI-Cap 的 lacunary 容量账本处理；
- dense 包：由本文 PC4-PI-Dense 处理；
- 任何失败：进入 FCT/LSMP/LV/PI-Seed/OV2 等既有终端。

因此 PC4-PI 的剩余主线义务已从“证明密集尺度正交”缩小为：把本文容量界与 PI-Cap 的 lacunary 包、PI-Seed 的能量下界、PC3-OV2 桥接定理统一成 PC4-PI 总命题。

## 7. 下一步最优攻坚

下一步应严写 `PC4-PI-Closure`：

1. 引用 PI-Seed 给离线零点导致的投影能量下界；
2. 引用 PI-Cap 的 lacunary/dense 分包；
3. 对 dense 分包引用本文；
4. 对所有失败分支引用 FCT/LSMP/LV/OV2；
5. 得到“高投影增量分支不能作为 RH 反例的最终逃逸通道”。

这将把 RH 总攻的 PC4-PI 分支推进到可审查的闭合形态。
