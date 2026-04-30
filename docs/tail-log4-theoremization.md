# Tail-log4 独立定理化与审稿补强

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
