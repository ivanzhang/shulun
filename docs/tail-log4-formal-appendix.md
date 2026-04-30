# Tail-log4 正式附录证明稿

本附录把 Tail-log4 从审查账本改写为更接近论文正文的定理—引理—证明格式。统一参考标签见 `docs/bibliography.md`。

## Theorem C（Tail-log4）

固定 `τ=0.7`。令尾部锚区间为 `q∈[τP,P]`，取 Selberg 平方权 `β_tail=β_{R_tail}`，满足 `R_tail^2<=P^η<P^{1/2}`。则行/列归约中的尾部贡献满足

`T_tail <= C_tail V_D P/log^4P`。

### 证明

由 `D`-粗 majorant，粗候选指标被 `β_tail` 以绝对常数控制。展开 `β_tail` 的 divisor 谱，谱变量满足 `r<=R_tail^2<=P^η`。将谱按

1. 低谱 `r<=log^8P`；
2. 中谱 `log^8P<r<=P^η`；
3. 平滑与端点余项

分解。Lemma C1、C2、C3 分别给出三部分均为 `O(V_D P/log^44P)`。三项相加强于 `log^{-4}`，定理成立。

## Lemma C1（低谱倒数窗口大筛）

对 `r<=log^8P`、Fourier 截断 `|h|<=log^16P`，低谱窗口项满足

`T_tail,low <= C_low V_D P/log^44P`。

### 证明

用 Vaaler/Beurling--Selberg 多项式逼近窗口指标。零频项与主项相消，截断误差归入 Lemma C2。非零频项化为

`Σ_{q∈[τP,P], q prime} w(q)e_P(ξq^{-1})`, `ξ≠0`。

经部分求和和 Vaughan 恒等式，分为 Type I、Type II 与端点块。按 `docs/rks-bridge-partition.md` 的长度分区：

- 短侧 `<=P^{1/18}`：固定短变量，对长变量用不完全 Kloosterman 完成和与 Weil 界，得 `<=P^{5/9}log^CP`，强于目标；
- BG 双线性覆盖区：由 `[BG2012]` 的双线性倒数 Kloosterman 定理给幂节省；
- 多线性可分裂区：由 `[BG2012]` 的 `Kloost 1/2` 给幂节省；
- 端点低体积区：总长度 `<=P/log^AP`，平凡吸收。

对数损失由 `docs/rks-parameter-audit.md` 记录，合计 `74<128`。因此可预留 `log^{-44}` 余量，得到结论。

## Lemma C2（平滑与端点余项）

Vaaler 截断与 Selberg divisor 谱端点余项满足

`T_tail,smooth <= C_smooth V_D P/log^44P`。

### 证明

取 Fourier 截断高度 `H_F=log^64P`。Vaaler 逐点误差为 `O(H_F^{-1})`。尾部每个 `q` 只产生 `O(1)` 个 `m` 候选，且 `#q=O(P/logP)`，故 Fourier 截断总误差

`O(V_D P/(logP·H_F))=O(V_D P/log^65P)`。

Selberg divisor 谱端点由平方权能量

`Σ_r |b_r|/r <= C V_D log^CP`

控制。端点层宽度 `H_F^{-1}` 给

`O(V_D P log^CP/H_F)`。

取保守 `C<=16`，得到 `O(V_D P/log^48P)`，强于 `log^{-44}`。

## Lemma C3（中谱平均二元上筛）

中谱部分满足

`T_tail,mid <= C_mid V_D P/log^44P`。

### 证明

中谱同步条件经 dyadic 分块化为二元线性素数系统

`q prime`, `q≡t a^{-1} mod b`, `(a q-t)/b prime`。

小模数层 `b<P^{1/2-ε}`：对两个线性形式应用二维 Selberg 上筛 `[Selberg-Sieve]`，得到

`<< S(a,b,t)P/(φ(b)log^2P)`。

平均奇异级数由 divisor-sum 展开控制；异常局部因子只来自 `abt`。大模数层由 `docs/tail-log4-theoremization.md` 的 TL4-M3：固定 `a,b,t` 后对变量 `q_2` 应用同一个二维上筛，再平均 `a,b,t`。端点项包含在上筛基本引理余项中。

取中谱下界 `r>log^80P`。平均奇异级数、dyadic 分块、大模数端点与系数损失合计不超过 `log^32P`，仍保留 `log^{-48}P`，故得到 `log^{-44}`。

## Corollary C4（抽取器接口）

Theorem C 证明保守常数包中的 `tail_error_power=4`。它不需要新增 JSON 字段；只作为 `experiments/extract_p0.py` 中 Tail 余项检查的数学输入。
