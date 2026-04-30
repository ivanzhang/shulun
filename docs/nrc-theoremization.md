# NRC 非共振倒数完成和定理化

统一参考文献标签见 `docs/bibliography.md`。
本文件补强 `docs/omr-cgtp-lsmp-theoremization.md` 中剩余深层输入 NRC。目标是把“非共振倒数完成和相对均匀性”写成独立可审查定理，并把失败情形明确转入 FCT/Tree-WFE。

## 1. 允许窗口与复杂度

允许窗口 `g` 是由以下原子经过有限交、并、差、阈值截取和平滑替换得到：

1. 区间指标或平滑区间权；
2. 固定小模数同余类指标；
3. 有限个祖先倒数相位环带 `Φ(e_P(ξ_i d^{-1}))`；
4. 上述对象的有限乘积。

记 `K(g)` 为生成复杂度。经过 Fourier 展开和同余/区间切分后，`g` 可写成

`g(d)=Σ_ν c_ν 1_{d∈I_ν}1_{d≡a_ν mod q_ν} e_P(β_ν d^{-1}) + Err_smooth`,

并满足

`Σ_ν |c_ν| <= K(g)log^C K(g)`, `#ν<=K(g)log^C K(g)`。

这里每个 `β_ν` 是祖先频率的低频整数线性组合。

## 2. 非共振条件

给定当前频率 `ξ` 与祖先频率集合 `Ξ(g)`，定义低频 span

`Span_H(Ξ)= {-Σ_i m_i ξ_i mod P: |m_i|<=H, Σ_i |m_i|<=H}`。

窗口 `g` 对当前频率 `ξ` 非共振，是指

`ξ notin Span_H(Ξ(g))`。

若该条件失败，则不使用 NRC，而记录为 frequency-collision terminal。

## 3. NRC 主定理

**Theorem NRC（非共振相对均匀性）。** 若 `g∈𝓦(K)` 对当前频率 `ξ` 非共振，则

`|Σ_d g(d)e_P(ξd^{-1})| <= C_weil K P^{1/2} log^{A_weil}P`。

保守可取正文常数包中的

`C_weil_completion=11664`, `A_weil_completion_log=4`，

并把额外 `log^C K` 并入 `K_eff`。

**证明。** 展开 `g`。每个主项化为

`Σ_{d∈I, d≡a mod q} e_P(α d^{-1})`,

其中 `α=ξ+β_ν`。非共振保证 `α≠0 mod P`。写 `d=a+qn`，因 `q<P` 且 `q not≡0 mod P`，这是模 `P` 的仿射变量替换。不完全和由完成法表示为

`P^{-1}Σ_{h mod P} \widehat{1_I}(h) Σ_{t mod P}^{*} e_P(αt^{-1}+ht)`。

完整和是经典 Kloosterman 型有理函数和。因 `α≠0`，相位 `α/t+ht` 非 Artin--Schreier 退化，Weil 界给每个完整和 `<=2P^{1/2}`；Fourier 系数绝对和给 `O(logP)`。故单个原子项 `<=C P^{1/2}logP`。乘以展开总 `l^1` 复杂度得到结论。平滑误差由截断高度并入 `log^{A_weil}P`。

## 4. NRC 对 OMR-3 与 DPI 的输出

在 OMR-3 中，若分散环带总偏差不是高投影增量，则偏差只能来自

`Σ_d g(d)e_P(ξd^{-1})`。

非共振时由 NRC 得到上界 `C K_effP^{1/2}log^AP`。当 EHPD 门槛满足

`Λ^2 r >= C K_eff P^{1/2}log^AP`，

该背景不足以解释 `cΛ^2r/log^AK` 级偏差，于是必须产生高投影增量。

在 DPI 中，同向偏移项同样化为允许窗口上的非零倒数相位平均。非共振时 NRC 控制该平均；若控制失败，则频率落入祖先 span，即 FCT 分支。

## 5. 审稿状态变化

NRC 已不再是深层黑箱：其解析核心只是标准完成法加 Weil/Kloosterman 界。剩余不是解析估计，而是组合接入问题：当非共振条件失败时，frequency-collision terminal 必须在 Tree-WFE 中被计账并产生容量矛盾或频率闭包终端。

因此 OMR/CGTP/LSMP 结构包的剩余黑箱进一步缩小为：

- **FCT/Tree-WFE 接口**：共振失败分支的全局树状能量/容量闭合。
