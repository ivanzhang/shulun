# DSO-E：Euler 局部因子 decorrelation 接口

本文专攻 `docs/rh-pc4-complexity-escape-interface.md` 中 CE-1 留下的唯一核心输入：当频率复杂度无界但不进入 FCT 低维频率闭包时，新增 Euler 局部因子的非主偏差应满足平方可控 decorrelation。本文仍不是 RH 证明；目标是把 DSO-E 拆成可审查的局部正交、非共振倒数和 FCT 失败三分。

## 1. 局部模型

对新增素数层 `p`，设局部空间

`G_p=(Z/pZ)^*`, `μ_p` 为均匀概率测度。

PPI/OMR 的局部非主因子可写成有限组合

`b_p(x)=Σ_{ν∈Ω_p} a_{p,ν} χ_{p,ν}(x)`, `∫_{G_p} b_p dμ_p=0`,

其中 `χ_{p,ν}` 包括乘法字符、加法相位 `e_p(hx)`、倒数相位 `e_p(hx^{-1})` 及其有限乘积。归一化取

`||b_p||_2^2=Σ_ν |a_{p,ν}|^2 + Err_p`,

其中 `Err_p` 是同一局部层内非正交交叉项。

## 2. 单层 Parseval 正交

**Lemma DSO-E1（单新增坐标正交）。** 若 `χ_{p,ν}` 是 `G_p` 上彼此不同的非主加法字符或乘法字符，则

`∫_{G_p} χ_{p,ν}\overline{χ_{p,ν'}} dμ_p=0` 对 `ν≠ν'`,

并且

`||b_p||_2^2=Σ_ν |a_{p,ν}|^2`。

**证明。** 这是有限阿贝尔群字符正交。非主字符均值为零，不同字符内积为零。有限线性组合展开后只保留对角项。证毕。

## 3. 倒数相位的非共振正交

倒数映射 `x↦x^{-1}` 是 `G_p` 的置换。因此纯倒数相位的交叉项

`p^{-1} Σ_{x∈G_p} e_p((h-h')x^{-1})`

在 `h≠h'` 时等于 `-1/p`，本身比 Weil 界更强。真正需要 NRC/Weil 的是混合相位，例如

`p^{-1} Σ_{x∈G_p} e_p(ax+b x^{-1})`,

它来自倒数窗口与线性相位、旧坐标投影或相位推送后的交叉项。

**Lemma DSO-E2（倒数/混合相位非共振界）。** 对纯倒数相位，若 `h≠h'`，则

`|p^{-1}Σ_{x∈G_p} e_p((h-h')x^{-1})| <= p^{-1}`。

对混合相位，若频率对 `(a,b)` 非退化，即不落入 FCT 记录的低维共振关系，则

`|p^{-1}Σ_{x∈G_p} e_p(ax+b x^{-1})| <= 2 p^{-1/2}`。

若该非退化条件失败，则该频率对进入 FCT。

**证明。** 纯倒数情形令 `y=x^{-1}`，得到非零剩余类上的非主加法字符和，归一化后大小为 `p^{-1}`。混合非退化情形由标准完成 Kloosterman/Weil 界，已在 `docs/nrc-theoremization.md` 的 NRC 输入中采用。退化时相位函数降为常数或低维 span 中的祖先相位关系，这正是 `docs/fct-tree-wfe-theoremization.md` 的 frequency-collision terminal。证毕。

## 4. 多频局部平方控制

**Lemma DSO-E3（局部多频平方控制）。** 设 `|Ω_p|=m_p`，且任意不同频率对要么非共振满足 DSO-E2，要么进入 FCT。若 FCT 不发生，则

`||b_p||_2^2 <= (1+2m_p p^{-1/2}) Σ_{ν∈Ω_p}|a_{p,ν}|^2`。

若所有交叉项都是纯倒数差，则可把 `2p^{-1/2}` 改为 `p^{-1}`。

特别地，当 `m_p <= c p^{1/4}` 时，有

`||b_p||_2^2 <= 2 Σ_ν |a_{p,ν}|^2`。

**证明。** 展开 `L^2` 范数。对角项给 `Σ|a|^2`；非对角项由 DSO-E2 逐项界为 `2p^{-1/2}|a_ν||a_{ν'}|`。用 `2|ab|<=|a|^2+|b|^2`，每个频率至多与 `m_p-1` 个频率相交，得到系数 `1+2m_p p^{-1/2}`。证毕。

## 5. 无界频率复杂度的二次剥离

DSO-E3 只处理 `m_p` 不太大的局部层。若 `m_p` 很大，不能直接用逐项 Weil 界；此时必须二次剥离。

**Lemma DSO-E4（大局部复杂度二分，组合接口）。** 若某密集尺度包中存在无限多层满足 `m_p>c p^{1/4}`，则至少发生一项：

1. 频率集合 `Ω_p` 在短深度 span 中高度聚集，触发 FCT；
2. 系数质量分散到大量小原子，触发 LSMP；
3. 可抽取子集 `Ω'_p`，满足 `|Ω'_p|<=c p^{1/4}` 且承载固定比例的 `l^2` 质量，返回 DSO-E3。

**证明。** 按祖先 span 与系数 dyadic 大小分解 `Ω_p`。若某短深度 span 承载正比例质量，触发 FCT。若没有重 span，则质量分散在大量小块；若每个可控大小子集都承载极小质量，则 dyadic 层蛋糕与 coarea 给出 LSMP 小质量逃逸。剩余情形必有一个可控大小子集承载固定比例 `l^2` 质量，对该子集应用 DSO-E3。这里的最后一步由 `docs/rh-pc4-lsmp-frequency-corollary.md` 的 LSMP-Freq 推论逐行实现。证毕。

## 6. DSO-E 主命题

**Proposition DSO-E（Euler 局部因子 decorrelation，条件化闭合）。** 对 PC4-PI 中出现的新增 Euler 局部因子 `b_p`，若 FCT 与 LSMP 均不发生，则存在常数 `C(𝓦_*)` 使

`Σ_{p∈𝓟} ||b_p||_2^2 <= C(𝓦_*) Σ_{p∈𝓟} Σ_{ν∈Ω_p}|a_{p,ν}|^2`

并且每个非主局部因子均值为零。若该平方控制失败，则必触发 FCT 或 LSMP；其中大复杂度层的剥离步骤依赖 DSO-E4 与 LSMP 接口。

**证明。** 均值为零来自非主字符和非退化倒数相位的局部平均；退化均值不为零时记录为 FCT。对每个 `p`，若 `m_p<=c p^{1/4}`，由 DSO-E3 控制。若 `m_p>c p^{1/4}`，由 DSO-E4 三分：FCT 或 LSMP 发生，或抽取可控子集返回 DSO-E3；对剩余子集迭代剥离。若迭代无限分散，则正是 LSMP；若有限结束，则得到所有承载质量的可控子集平方控制。求和得命题。证毕。

## 7. 与 CE 和 DSO 的闭合关系

DSO-E 补上 `docs/rh-pc4-complexity-escape-interface.md` 中 CE-1 的独立新频率近正交输入：不进入 FCT 的新增局部因子不能长期同向累积非主偏差；若局部复杂度过大，则转入 LSMP 或 FCT。

因此 PC4-PI 的密集尺度正交链条现在形成如下条件化闭环：

- 固定复杂度模板：`docs/rh-pc4-dso-template-consistency.md` + DSO-C；
- 复杂度逃逸：`docs/rh-pc4-complexity-escape-interface.md`；
- 独立新频率正交：本文 DSO-E；
- 投稿级核查：`docs/rh-pc4-dso-euler-match-audit.md` 已将 DSO-E2 对齐到初等字符正交、`EXT-KL` 与 NRC/FCT 口径；`docs/rh-pc4-lsmp-frequency-corollary.md` 已将 DSO-E4 的剩余组合义务降为 LSMP 推论。


## 8. 无条件化匹配入口

DSO-E1--E4 与 NRC/EXT-KL、FCT、LSMP-Freq、PI-Seed 的逐项匹配审查见 `docs/rh-pc4-dso-e-unconditionalization-audit.md`。
