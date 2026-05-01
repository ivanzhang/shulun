# PC4-PI：Dense-scale orthogonality 密集尺度包正交接口

本文专攻 `docs/rh-pc4-pi-cap-carleson.md` 留下的最后实质硬点：密集尺度包内固定投影模板的正交上界。目标不是一次性证明 RH，而是把 `PI-Cap` 的深层输入拆成两个可审查接口：Mellin 波包正交与 CRT martingale 正交。

## 1. 密集尺度包

固定投影模板 `𝓦_*`。设尺度包

`𝓘=[Y,Y^B]`

内有许多尺度 `X_j`，它们不够 lacunary，窗口支撑在 Mellin 变量 `u=log X` 上大量重叠。PI-Seed 给可能的能量和

`Σ_{X_j in 𝓘} δ_j^2 μ_j^0(A_j)`。

平凡包容量上界不足以排斥离线零点；需要正交增益。

## 2. Mellin 波包正交接口

每个平滑窗口 `W(n/X_j)` 在 Mellin 侧是波包

`X_j^s \widehat W(s)`。

固定离线频率 `γ` 对应 `s=β+iγ`。固定投影模板的贡献可以抽象为

`F_j(u)=a_j Φ(u-logX_j) e^{iγu}`，

其中 `Φ` 由平滑权与模板决定。

**Lemma DSO-M（Mellin Bessel 上界，待证接口）。** 对任意密集尺度包 `𝓘` 与固定模板 `𝓦_*`，若系数 `a_j` 来自零频归一化投影增量，则

`∫_{u in log𝓘} |Σ_j a_j Φ(u-logX_j)|^2 du <= C(𝓦_*) Σ_j |a_j|^2`。

若该 Bessel 上界成立，则密集包内的同模板贡献被 `l^2` 系数能量控制；它本身不排除单点大峰，但排除在同一包内无成本地累积平方能量。要与离线零点矛盾，还需 PI-Seed 给出的同包平方能量下界超过该 `l^2` 容量。

**证明状态。** 这是标准 Hilbert 空间波包 Bessel 型命题的适配版。对固定紧支撑 `Φ`，若中心分离则由 almost orthogonality；若中心密集，则需要 Carleson embedding 或采样 Bessel 条件。当前尚需证明投影模板生成的 `a_j` 满足相应 Carleson 测度条件。

## 3. CRT martingale 正交接口

随着 `z` 增长，`M(z)=∏_{p<=z}p` 的 CRT σ-代数逐步细化。新增素数层提供新的独立局部坐标。固定投影模板若想在所有尺度保持同向偏置，必须在不断新增的 CRT 坐标中维持相干。

设 `𝔽_z` 为模 `M(z)` 的非零类 σ-代数。定义投影偏差 martingale 差

`D_z = E[f | 𝔽_z]-E[f | 𝔽_{z^-}]`。

**Lemma DSO-C（CRT martingale square function，待证接口）。** 对固定投影模板 `𝓦_*`，有

`Σ_{z in dense pack} ||D_z||_2^2 <= C ||f||_2^2`。

因此若高投影增量在密集尺度包中每次都需要新增 CRT 层提供同向偏差，则平方和受全局 `L^2` 容量控制。

**证明状态。** 该命题形式上是 Doob martingale/Parseval 正交。但困难在于：投影窗口 `A_j` 随尺度、dyadic 层和倒数相位变化，并非简单固定函数 `f`。需要把固定模板拉回到统一 inverse limit CRT 空间 `lim (Z/M(z)Z)^*`，证明这些拉回函数复杂度一致且 martingale 差正交。

## 4. Euler product 局部因子正交

Euler product 视角给同一事实的乘法版本：新增素数层 `p` 的局部因子只影响新坐标。固定有限复杂度模板依赖有限层或低复杂度组合；若它长期同向偏置所有新增层，则等价于一个非主局部因子平均不为零，违反局部因子正交。

**Lemma DSO-E（Euler factor decorrelation，候选接口）。** 固定模板 `𝓦_*` 对新增素数层的非主局部偏差应满足零均值与平方可控：

`E_p[local_bias_p(𝓦_*)]=0`, `Σ_{p in pack} |local_bias_p|^2 <= C(𝓦_*)`

在适当归一化下成立，除非模板进入 FCT 低维频率闭包。

这把密集尺度正交与 FCT 分支连接起来：若不能 decorrelate，则说明频率被有限低维结构锁定。

## 5. DSO 主命题

**Proposition DSO（密集尺度包正交，条件化）。** 若 DSO-M 与 DSO-C 至少一条成立，并且 DSO-E 处理新增素数层的非独立残差，则固定投影模板在任意密集尺度包中满足

`Σ_{X_j in 𝓘} δ_j^2 μ_j^0(A_j) <= C(𝓦_*) Cap(𝓘)`，

除非触发 FCT 或 LSMP 小质量逃逸。

**证明。** Mellin 侧由 DSO-M 给波包 Bessel 上界；CRT 侧由 DSO-C 给新增 σ-代数的 square function 上界；Euler product 残差由 DSO-E 排除或转入 FCT。若两种正交模型至少一种能覆盖当前模板，便得到固定模板的 Carleson 包容量上界。证毕。

## 6. 与 PI-Cap 的关系

`docs/rh-pc4-pi-cap-carleson.md` 将 PI-Cap 分成 lacunary super-capacity 与 dense-scale orthogonality。本文给出 dense-scale orthogonality 的精确接口。因此 PC4-PI 的剩余真正硬点进一步压缩为：

1. 证明 DSO-M 的 Mellin Bessel/Carleson 条件；
2. 或证明 DSO-C 的 inverse-limit CRT martingale square function；
3. 并用 DSO-E 处理不正交残差，将其转入 FCT。

## 7. 下一步最优攻坚

三条路线中，最可操作的是 DSO-C：构造 inverse-limit CRT 概率空间，并把固定模板窗口拉回为一致复杂度函数族。它最贴近本文已有 CRT 非零类均衡与 D 组 martingale 能量账本。
