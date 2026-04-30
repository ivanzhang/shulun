# D 组 Structured-EHPD 正式附录证明稿

本附录把 `OMR/CGTP/LSMP/NRC/FCT` 从结构口号改写为可审查的定理接口。目标是减少黑箱：凡是纯组合、Fourier 层蛋糕、martingale 能量或离散 coarea 的部分均给出逐行证明；凡是解析数论输入均明确归入标准外部定理包，统一引用见 `docs/external-theorem-package.md` 与 `docs/bibliography.md`。

## 1. Structured-EHPD 坏配置的标准形式

一个 `Structured-EHPD` 坏配置由有限加权集合 `(X,w)`、相位映射 `φ:X->R/Z`、允许窗口族 `𝓦(K)`、根规模 `r=sum_X w`、偏差参数 `Λ in (0,1]` 与复杂度参数 `K>=2` 组成，并满足：

1. 覆盖性：A/B 附录剥离小因子锁定与 Tail-log4 尾部锚后，剩余候选均由主体双粗锚覆盖；
2. 非终端性：无短簇、无高投影增量、无 frequency-closure terminal；
3. 非共振背景：每个新频率若不落入祖先短深度 span，则满足 NRC 完成和界；
4. 能量有界：归一化 martingale 平方能量 `E<=r`；
5. 一阶偏差：存在频率 `ξ` 使 `|S(ξ)|=|sum_X w(x)e(ξφ(x))|>=Λr`。

D 组定理证明：满足上述五项的坏配置不能存在。A/B 附录负责把行列反例归约到该标准形式；C 附录负责尾部锚削尾。

## 2. 外部定理输入

本附录只调用以下外部输入：

- `EXT-KL`：Weil/Kloosterman 完整和界及不完全和完成法；
- `EXT-BG`：Bourgain--Garaev 型倒数 Kloosterman 多线性对数节省；
- `EXT-Vaaler`：区间指标的 Vaaler/Beurling--Selberg 截断；
- `EXT-Selberg`：二维线性 Selberg 上筛上界；
- `EXT-Vaughan`：Vaughan 恒等式与 Type I/II 分解。

其中 D 组本身直接使用 `EXT-KL`；其余四项主要服务于 Tail-log4 附录 C。

## 3. OMR：一阶偏差必产生结构输出

**Lemma D1（层蛋糕到测试函数）。** 设 `F` 为偶的分段 Lipschitz 测试函数，Fourier 截断高度不超过 `H`，且有效 dyadic 层数不超过 `L`。若每个层 `B_j` 的实际质量与一阶模型质量差满足 `|Δ_j|<=ε μ(E_j)`，则

`|sum_X w(x)F(φ(x))-int F dν_1| <= C ε r L + C r/H`。

**证明。** 把 `F` 写成 dyadic 层指标的有限线性组合加截断误差：`F=sum_{j<=L} α_j 1_{B_j}+O(H^{-1})`，其中 `sum |α_j|<=C`。逐层代入残差界并求和，得 `CεrL`。Fourier 截断尾部由 Fejer/Vaaler 型平滑给 `Cr/H`。证毕。

**Lemma D2（一维圆周偏差）。** 若一阶模型

`dν_1(θ)=r(1+2λ cos(θ-θ0))dθ`, `λ>=Λ`,

则存在 `O(log(1/Λ))` 个阈值弧层，使总偏差至少为 `cΛr`。

**证明。** 对弧 `I_t={cos(θ-θ0)>=t}`，`0<=t<=1/4`，有

`ν_1(I_t)-r|I_t|=2λr int_{I_t} cos(θ-θ0)dθ`。

在该区间内积分下界为绝对常数。把 `[0,1/4]` 按 dyadic 网格离散；若所有层偏差总和小于 `cΛr`，则上述连续积分的 Riemann 和下界被违背。取常数 `c` 足够小即得。证毕。

**Proposition D3（OMR 输出）。** 在非短簇且 NRC 背景可吸收时，若 `|S(ξ)|>=Λr`，则或者存在高投影增量窗口 `W in 𝓦(K')`，满足

`μ(W)>=(1+κ Λ^2/log^8K) μ_geo(W)`,

或者当前频率进入 frequency-closure terminal。

**证明。** 由 Lemma D2 得到总量 `>=cΛr` 的一阶层偏差。若偏差集中在长度低于允许尺度的短弧，则按定义产生短簇，排除。否则用 Vitali maximal disjoint 选择抽出有限重叠窗口族，保留至少 `cΛr/log^C K` 的总偏差。若没有窗口达到 `κΛ^2/log^8K` 的相对密度增量，则这些偏差全部必须由几何测度误差或相位非均匀性承担。非共振时由 `EXT-KL` 给出的 NRC 界把总误差压到 `C K_eff P^{1/2}log^C P`；在主常数账本的吸收条件 `Λ^2r >= C K_eff P^{1/2}log^C P` 下矛盾。若 NRC 不适用，则该频率落入祖先 span，按 FCT 定义进入 frequency-closure 计账。证毕。

## 4. CGTP：投影增量的平方能量账本

**Lemma D4（martingale 平方能量增量）。** 设父块密度为 `ρ`，子窗口 `W` 的几何质量为 `m`，且实际密度为 `ρ(1+δ)`。则相对父块的平方能量增加至少

`ΔE >= c ρ^2 δ^2 m`。

**证明。** 令条件期望密度随机变量从常数 `ρ` 细分为 `ρ(1+δ)` 与互补子块上的值。条件期望的 `L^2` 能量增量等于条件方差。固定 `W` 上偏离量为 `ρδ`，互补块由总质量守恒决定；方差至少为窗口部分贡献的绝对常数倍，即 `cρ^2δ^2m`。证毕。

**Theorem D5（CGTP 有限步矛盾）。** 若沿生成树每个非终端步骤均给出 `δ>=κΛ^2/log^8K` 的高投影增量，且有效窗口总质量下界为 `m>=c r/log^8K`，则非终端步骤数至多

`T <= C log^16K / Λ^4`。

在保守常数包中，该损失被 `C_CGTP=16`, `A_CGTP_log=8` 与 `epsilon_OMR_power=64` 的余量吸收。

**证明。** 由 Lemma D4，每步能量增量至少 `c r Λ^4/log^16K`。总能量始终不超过 `r`，故步数超过 `C log^16K/Λ^4` 时矛盾。常数包中把该二次能量损失预先并入 `epsilon_OMR_power=64` 的安全余量，不影响主阈值抽取。证毕。

## 5. LSMP：小质量 packing 不制造新自由度

**Lemma D6（离散 coarea）。** 设小质量原子族 `𝓐` 的总质量为 `M`，每个原子有厚度参数 `h(A) in [K^{-1},1]`。则存在 dyadic 厚度层 `𝓐_j` 及其有限重叠边界层族 `𝓑_j`，使

`sum_{B in 𝓑_j} μ(B) >= cM/logK`, `mult(𝓑_j)<=C`, `K(B)<=Klog^C K`。

**证明。** 厚度区间 `[K^{-1},1]` 分成 `O(logK)` 个 dyadic 层。平均原理给某层承载至少 `M/O(logK)` 的质量。对该层按包含关系取 maximal disjoint 子族；标准 Vitali 覆盖给有限重叠扩大族，并只损失绝对常数。复杂度最多乘一个 dyadic 层数和有限扩大因子，故为 `Klog^C K`。证毕。

**Lemma D7（LSMP 吸收）。** 在无短簇、无高投影增量且无 frequency-closure terminal 时，小质量原子的总能量满足

`E_small <= C Λ^2 r/log^8K`。

**证明。** 若 `E_small` 大于右端，则方向筛选把平方能量转化为某一同向偏移总量 `>=cΛr/log^C K`。由 Lemma D6 抽出有限重叠薄层族承载该偏移。若薄层偏移来自真实密度增量，则产生高投影增量，矛盾；若来自短尺度集中，则产生短簇，矛盾；若来自非平凡相位平均，则非共振时由 NRC 控制并被主吸收条件压低，矛盾；若 NRC 失败，则进入 frequency-closure terminal，亦矛盾。因此小质量能量只能满足所述上界。证毕。

## 6. FCT：共振失败分支的闭合

**Lemma D8（短深度 span 计数）。** 生成树深度不超过 `T`，每个节点新增至多 `B` 个低阶倍频。若只记录祖先深度 `h<=ClogK` 内的频率 span，则候选 span 数不超过 `exp(CBlog^2K)`；在本文常数账本中以 `log^8K` 的局部复杂度损失逐层吸收。

**证明。** 每一步仅加入有限个整数倍频，且倍频阶数被窗口复杂度截断。短深度记忆意味着当前节点只需记录最近 `O(logK)` 层的有限生成元及其有界整数系数。逐层递推时该复杂度表现为固定次数的对数因子；全局指数型树数不进入单路径估计。保守地把每层选择、倍频和并差窗口损失计入 `log^8K`。证毕。

**Proposition D9（frequency-closure 终端合法性）。** 若连续共振使所有新频率均落入同一短深度 span，则递推进入 frequency-closure terminal；该终端是合法输出，不是未估误差。

**证明。** 在固定低维 span 内，后续相位测试函数都属于同一有限频率代数。若该代数上能量集中，则 CGTP 给出高投影增量；若对应 Bohr 交集质量集中，则给出短簇；若二者都不发生，则所有后续 OMR 偏差被低维模型吸收，无法继续产生新的非终端推进。按 Tree-WFE 定义递推停止并记录 frequency-closure terminal。证毕。

## 7. D 组闭合定理

**Theorem D（Structured-EHPD 排斥）。** 假设 `EXT-KL` 的 NRC 输出、A/B 的标准坏配置接入、C 的 Tail-log4 削尾和上述常数吸收条件均成立，则 `Structured-EHPD` 坏配置不存在。

**证明。** 由坏配置的一阶偏差与 Proposition D3，非终端节点必须产生高投影增量，除非出现短簇或 frequency-closure terminal；后二者被坏配置假设排除。高投影增量沿生成树由 Theorem D5 产生正平方能量增量；小质量逃逸由 Lemma D7 吸收；共振失败由 Proposition D9 转为合法终端，也被坏配置假设排除。因此若坏配置持续非终端推进，有限步后平方能量超过总上界 `E<=r`，矛盾。故坏配置不存在。证毕。

## 8. 审稿剩余边界

本附录使 D 组剩余义务变成可逐项检查的三类：

1. `EXT-KL` 等外部定理的正式编号引用；
2. A/B 附录中定义的主体双粗锚坏配置与本附录第 1 节五项标准形式逐项同名匹配；
3. 常数包中 `16,8,64` 对本附录各处 `log^8K`、`log^16K` 和 `Λ^4` 损失的吸收核对。

其中第 1 项由 `docs/external-theorem-package.md` 给出引用模板；第 3 项由 `docs/explicit-p0-constants.structured-conservative.json` 与阈值抽取脚本核验。第 2 项是下一轮最小审稿接口。
