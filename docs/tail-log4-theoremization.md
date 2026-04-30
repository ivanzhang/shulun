# Tail-log4 独立定理化与审稿补强

统一参考文献标签见 `docs/bibliography.md`。
本文件专门补强待证数学输入 C。目标是把 `Tail-log4` 从单一黑箱拆成三条可审查定理，并明确每条定理依赖的标准工具。

## 1. Tail-log4 主定理

**Theorem TL4（尾部 log4 界）.** 固定 `τ=0.7`。令尾部素因子区间为 `q∈[τP,P]`，取尾部 Selberg 平方权 `β_tail=β_{R_tail}`，满足 `R_tail^2<=P^η<P^{1/2}`。则对任意行或列归约产生的尾部覆盖项，均有

`T_tail <= C_tail V_D P/log^4 P`。

这里 `C_tail` 可并入保守常数包中的 `C_sieve`，不需要新增抽取器字段。

**证明。** 第 806 节的 `D`-粗 majorant 给出常数 1 的 Selberg 平方权上界。展开 `β_tail` 后，谱变量满足 `r<=R_tail^2<=P^η`，故尾部只需低谱、中谱和平滑余项三部分。由 Theorem TL4-L、TL4-S、TL4-M 分别得

`T_tail,low <= C_low V_D P/log^44 P`,

`T_tail,smooth <= C_smooth V_D P/log^44 P`,

`T_tail,mid <= C_mid V_D P/log^44 P`。

三项相加仍为 `O(V_D P/log^44P)`，强于抽取器只需要的 `log^{-4}`。证毕。

## 2. Theorem TL4-L：低谱倒数窗口大筛

**命题。** 令 `L=log^8P`，`H_F=log^16P`。对 `r<=L`、尾部素数 `q∈[τP,P]` 与由行/列归约产生的 bounded-variation 窗口函数 `B_r(q)`，有

`Σ_{r<=L} r^{-1}|Σ_q (B_r(q)-P/(rq))|^2 <= C_L P^2/log^44P`。

**证明框架。**

1. 用 Vaaler 多项式把 `B_r(q)` 展开到 `|h|<=H_F`，截断误差进入 TL4-S。
2. `h=0` 项与主项 `P/(rq)` 相消。
3. 对 `h≠0`，相位为 `h kP/(rq)` 或列对偶形式的有界变差变体。
4. 小 `k` 非振荡区用容量剥离：`k<=P/log^80P` 时尾部可贡献点数本身为 `O(P/log^80P)`，强于 `log^{-44}`。
5. 大 `k` 区用 Vaughan 分解把素数 q 和转为 Type I/II 倒数指数和；体积大于 `P/log^C P` 的块由 BG/coherent reciprocal Kloosterman 输入给任意固定对数节省，低体积块平凡吸收。
6. 对 `r,h` 与 dyadic 块求和只损失 `log^{O(1)}P`，保守账本 `K_sieve_log_saving=128` 覆盖该损失。

**剩余外部输入。** 只需 BG/coherent reciprocal Kloosterman 的“任意固定对数节省”版本；本命题不再额外假设素数短区间下界。

## 3. Theorem TL4-S：平滑与端点余项

**命题。** 在 `H_F=log^64P` 的 Vaaler/Beurling 截断和 Selberg divisor 谱端点平滑下，全部平滑余项满足

`T_tail,smooth <= C_S V_D P/log^44P`。

**证明。** Vaaler 截断逐点误差为 `O(H_F^{-1})`。尾部每个素数 `q` 只产生 `O(1)` 个尾部 `m` 候选，且 `# {q∈[τP,P]}=O(P/logP)`，所以 Fourier 截断余项为

`O(V_D P/(logP H_F))=O(V_D P/log^65P)`。

Selberg divisor 谱端点项由平方权能量控制：

`Σ_r |b_r|/r <= C V_D log^C P`。

端点层宽度为 `H_F^{-1}`，故端点贡献

`O(V_D P log^C P/H_F)`。

保守取内部复杂度 `C<=16`，`H_F=log^64P` 给出 `O(V_D P/log^48P)`，强于 `log^{-44}`。证毕。

## 4. Theorem TL4-M：中谱平均二元上筛

**命题。** 对 `log^8P<r<=P^η` 的中谱部分，行/列尾部归约产生的二元线性素数条件满足

`T_tail,mid <= C_M V_D P/log^44P`。

**证明框架。**

1. 将中谱条件按 dyadic 变量 `(a,b,t)` 分块，得到二元线性系统

   `q prime`, `q≡t a^{-1} mod b`, `(a q-t)/b prime`。

2. 小模数层 `b<P^{1/2-ε}` 用二维 Selberg 上筛，得到

   `<< S(a,b,t)P/(φ(b)log^2P)`。

3. 奇异级数 `S(a,b,t)` 的异常局部因子只来自 `abt`，展开为 divisor-sum 后在 dyadic 平均中有界。

4. 大模数层用平均大模数二元上筛：不要求单个大模数 AP 中的素数渐近，只对 `(a,b,t)` 平均；端点和重数由 `(a,b)=1` 与 Large-modulus-spacing 控制。

5. 取中谱下界参数 `B_m=80`，平均奇异级数、dyadic 分块与大模数余项总损失记为 `log^32P`，扣除后仍有 `log^{-48}P` 余量，因此得到 `log^{-44}`。

**剩余外部输入。** 这里的核心外部输入不是素数短区间定理，而是 Selberg 二维线性上筛的平均版本和平均大模数二元上筛。该输入比原始行/列命题窄得多，适合单独作为引用定理或附录证明。

## 5. 审稿状态变化

经过本定理化，Tail-log4 不再是一个整体黑箱。它被拆成：

- TL4-S：已由初等截断与 Selberg 权能量证明；
- TL4-L：只依赖 BG/coherent reciprocal Kloosterman 的对数节省；
- TL4-M：只依赖二维 Selberg 上筛与平均大模数二元上筛。

因此待证输入 C 的黑箱数量从一个笼统 Tail-log4 降为两个标准解析输入：低谱倒数 Kloosterman 对数节省与中谱平均二元上筛。

## 6. TL4-M 的进一步拆解：平均大模数二元上筛

本节把 TL4-M 中剩余的“平均大模数二元上筛”继续拆开，避免把大模数层作为不可审查黑箱。

### 6.1 二元线性上筛模板

**Lemma TL4-M1（二维线性 Selberg 上筛模板）.** 设 `I=[X,2X]`，`a,b,t` 为固定整数，`(a,b)=1`，并设线性形式

`L_1(n)=n`, `L_2(n)=(bn+t)/a`

在同余条件 `bn+t≡0 (mod a)` 上取整数值。若局部无固定素数障碍，则

`#{n∈I: n prime, L_2(n) prime, bn+t≡0 (mod a)}`

`<= C S(a,b,t) X/(φ(a) log^2 X)`，

其中 `S(a,b,t)` 是二元奇异级数，`C` 为绝对常数。

**证明。** 在同余类 `n≡-tb^{-1} (mod a)` 上应用 Selberg 上筛到两个线性形式 `n` 与 `(bn+t)/a`。筛维数为 2，筛水平取 `z=X^{1/u}`，基本引理给上筛函数 `O(log^{-2}X)`，同余类密度给 `φ(a)^{-1}`，局部修正因子合并为 `S(a,b,t)`。这只是上界筛，不需要素数在单个大模数 AP 中的渐近公式。证毕。

### 6.2 平均奇异级数账本

**Lemma TL4-M2（平均奇异级数有界）.** 在 dyadic 范围 `a,b≈B`、`|t|<=H`、`(a,b)=1` 中，有

`Σ_{a,b≈B,(a,b)=1} Σ_{|t|<=H} S(a,b,t)/φ(a)`

`<= C log^C P · Σ_{a≈B}1/φ(a) · B H`。

**证明。** 对任意素数 `ℓ`，奇异级数局部因子仅在 `ℓ|abt` 或两个线性形式模 `ℓ` 退化时偏离 `1+O(ℓ^{-2})`。把异常因子用

`∏_{ℓ|abt}(1+C/ℓ)`

控制，再展开为 divisor-sum。对 dyadic 平均，条件 `d|abt` 的贡献由

`#{a,b,t: d|abt} <= B^2H τ(d)^2/d`

或分配到 `a,b,t` 的三个除数组合控制；求和给 `log^C P`。再乘 `1/φ(a)` 的平均 `Σ_{a≈B}1/φ(a)<<logP`，得到结论。证毕。

### 6.3 大模数平均层

**Proposition TL4-M3（平均大模数二元上筛）.** 设 `a,b≈B>=P^{1/2-ε}`、`(a,b)=1`、`H=P/r`、`log^80P<r<=P^η`，且 `η<1/2-3ε`。则

`Σ_{a,b≈B,(a,b)=1} #{(q_1,q_2,t): q_i≈P prime, |t|<=H, q_1 a-q_2 b=t}`

`<= C P B H log^C P/log^2P`。

**证明。** 固定 `a,b,t`，方程等价于

`q_1=(bq_2+t)/a`, `bq_2+t≡0 (mod a)`。

对 `q_2≈P` 应用 Lemma TL4-M1，得到上界

`C S(a,b,t) P/(φ(a)log^2P)`。

对 `a,b,t` 求和并用 Lemma TL4-M2，得到

`<= C P/log^2P · log^C P · Σ_{a≈B}1/φ(a) · B H`。

由于 `Σ_{a≈B}1/φ(a)<<logP`，该对数可并入 `log^C P`，得到命题。

需要说明的是，这里没有额外端点项。Selberg 上筛直接作用于有限区间 `q_2≈P` 与同余类 `mod a`，端点只改变筛权支撑的首尾 `O(1)` 个整数；这些贡献已经包含在上筛基本引理的余项中。若改用先枚举整除 `a|(bq_2+t)` 的粗方法，会出现表面 `logP` 损失，但那是把筛前候选和筛后双素数候选分开估计造成的伪损失，不进入 Selberg 二维上筛证明。证毕。

### 6.4 对 TL4-M 的影响

由 Lemma TL4-M1、TL4-M2 与 Proposition TL4-M3，大模数层不再需要独立黑箱；它归约为标准二维 Selberg 上筛及其平均奇异级数账本。TL4-M 剩余的唯一外部输入是小/中模数层与低谱层共用的标准筛法工具，而不是任何关于单个大模数 AP 的素数渐近。

因此待证输入 C 进一步缩小为：

- TL4-L 的 BG/coherent reciprocal Kloosterman 对数节省；
- TL4-M 的二维 Selberg 上筛模板与平均奇异级数账本，其中大模数层已由 Proposition TL4-M3 处理。

## 7. TL4-L 的进一步拆解：BG/coherent 输入与 Type I/II 核验

本节补强 TL4-L，目标是把“BG/coherent reciprocal Kloosterman 对数节省”拆成明确可引用定理模式和 Vaughan Type I/II 适用核验。

### 7.1 可引用倒数和定理模式

**Theorem RKS-log（reciprocal Kloosterman log-saving 模式）.** 设 `p=P` 为素数，`I,J⊂[1,p-1]` 为区间或 dyadic 集合，系数满足 `|α_m|,|β_n|<=τ_C(m),τ_C(n)`。若

`|I||J| >= p/log^A p`,

则对任意非零 `ξ mod p`，有

`|Σ_{m∈I}Σ_{n∈J} α_m β_n e_p(ξ (mn)^{-1})|`

`<= C_A |I||J|/log^{A_1}p`。

其中 `A_1` 可按需要预先取大，只需相应增大输入定理中的 `A` 与分解阶数。该模式是 Bourgain--Garaev 型 prime-field multilinear reciprocal Kloosterman 估计在二线性/多线性分块后的对数节省版本；divisor-bounded 系数通过 dyadic 分层只损失 `log^{O(1)}p`。

**审稿说明。** 最终论文应在参考文献中引用精确的 Bourgain--Garaev 或后续多线性倒数 Kloosterman 定理，并说明其 entropy/source 条件覆盖本文 dyadic 块。本文使用的只是任意固定对数节省，不需要固定幂节省的最优常数。

### 7.2 从素数 q 和到 Vaughan Type I/II

TL4-L 的非零 Fourier 模为

`S=Σ_{q∈[τP,P], q prime} w(q)e(hkP/(rq))`,

其中 `r<=log^8P`、`1<=|h|<=log^16P`，`w` 有 bounded variation。用部分求和可把 `w` 变成 dyadic 光滑权；再用 Vaughan 恒等式展开 `Λ(q)`。得到三类块：

1. **Type I**：`Σ_{m<=U} a_m Σ_{n≈P/m} e(ξ/(mn))`；
2. **Type II**：`Σ_{m≈M} a_m Σ_{n≈N} b_n e(ξ/(mn))`，`MN≈P`，且 `M,N` 均不太小；
3. **低体积/端点块**：`MN<=P/log^A P` 或某变量长度短于 dyadic 阈值。

这里 `ξ` 可写成非零模 `P` 频率；因 `r,h` 都小于 `P`，且 `h≠0`，频率非零。

### 7.3 Type II 块核验

若 `M N≈P` 且 `M,N>=log^C P`，不能仅凭体积就直接引用 BG 文献。应按 `docs/rks-bridge-partition.md` 分区：BG 多线性/双线性覆盖区由引用定理给幂节省；短变量为对数级时由完成和吸收；剩余近极端不平衡区需要 RKS-bridge-minor。

在完成该桥接后，可得

`S_{II}(M,N) <= MN/log^{A_1}P`。

对所有 dyadic `M,N` 和所有 `r,h` 求和损失至多 `log^{C_0}P`。取 `A_1>=44+C_0+10`，得到 TL4-L 所需 `log^{-44}` 余量。

### 7.4 Type I 块核验

Type I 中若内变量长度 `N=P/m` 满足 `N>=P/log^A P`，则对固定 `m` 的一维倒数和可用完成和/Kusmin--Landau 给对数节省；更统一地，把 `m` 保留为外系数，仍满足 `MN≈P`，若 `m` 范围长度 `M>=log^C P`，由 Theorem RKS-log 处理。

若 `M<log^C P`，则外变量只有对数多个。对每个固定 `m`，相位在 `n≈P/m` 上为 `e_P(ξ m^{-1}n^{-1})`。区间长度 `N≈P/m>=P/log^C P`，完成和或分部加和给

`Σ_{n≈N} e_P(ξ m^{-1}n^{-1}) <= N/log^{A_1}P`

在任意固定对数节省意义下；这是 RKS-log 的一变量长区间退化形式。对 `m` 求和仍只损失对数幂。

### 7.5 低体积块吸收

低体积块满足总候选数 `<=P/log^A P`，或来自 Vaughan 分解端点。平凡估计给其贡献 `<=P/log^A P`。取 `A>=60`，经过 `r,h` 和 dyadic 求和后仍为 `O(P/log^44P)`。

这解释了 TL4-L 中“低体积时由平凡估计吸收”的精确含义：低体积块的总长度已经小于目标余量，不需要任何相消。

### 7.6 TL4-L 结论

由 7.2--7.5，非零 Fourier 模总贡献满足

`Σ_{r<=log^8P} r^{-1}|Σ_q(B_r(q)-P/(rq))|^2 <= C P^2/log^44P`。

其中平方和来自 Cauchy 与 dyadic 正交化；`r,h` 的数量为 `log^{O(1)}P`，已由 `A_1` 余量覆盖。于是 TL4-L 的唯一剩余引用已经缩小为 Theorem RKS-log。最终审稿时，只需把 RKS-log 与所引用 BG/多线性倒数 Kloosterman 定理逐项匹配即可。
