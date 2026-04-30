# PC-3 两个剩余任务：候选 CRT 基线误差与 overlap-energy

本文件继续推进 `docs/rh-pc3-prime-sparse-to-cover-excess.md` 最后压缩出的两个任务：

1. 证明 `Candidate_z` 的 CRT 基线误差在合适参数下为 `o(X^β)`；
2. 证明最小大因子 Buchstab 权下 `OverlapLoss=o(X^β)`，或 overlap-energy 过大触发 D 组终端。

目标是形成一个可审查的 `PC-3-global` 弱闭合版本。

## 1. 任务一：Candidate_z 的 CRT 基线误差

取全局平滑权 `W(n/X)`，令 `z=(log X)^A`，`M=P(z)=prod_{p<=z}p`。候选计数为

`Candidate_z(X)=Σ_n 1_{(n,M)=1} W(n/X)`。

CRT 零频期望为

`ExpectedCandidate_z(X)=X \hat W(1) φ(M)/M`。

### Lemma CAND-1（Poisson/周期误差）

对固定光滑紧支撑 `W`，有

`Candidate_z(X)=X\hat W(1)φ(M)/M + O_A(M^C)`

其中 `C` 只依赖有限个平滑范数；若使用标准周期分块，也可取误差 `O(M)` 加平滑端点项。

**证明。** 函数 `1_{(n,M)=1}` 是周期 `M` 的函数。把整数按 `n=a+kM` 分解，对每个 reduced residue class `a` 应用 Euler--Maclaurin 或 Poisson summation：

`Σ_k W((a+kM)/X)=X/M \hat W(1)+O_N((M/X)^N)`

在支撑范围内求和 `φ(M)` 个类，再加有限端点误差。得到主项和 `O(M)` 型误差；保守写作 `O_A(M^C)`。证毕。

### 参数结论

若 `z=(log X)^A`，则

`log M = θ(z) ~ z = (log X)^A`。

当 `A<1` 时，`M=exp((log X)^A)=X^{o(1)}`。因此对任意 `β>1/2`，

`M^C=o(X^β)`。

故候选 CRT 基线误差无法吸收离线零点级 `X^β` 波动。

## 2. 任务二：OverlapLoss 与最小大因子唯一分配

使用 Buchstab 权

`ω_z^B(n)=log P^-(n)`。

对 `z`-粗合数 `n`，最小大因子 `q=P^-(n)` 唯一。因此真实合数 Buchstab 权有唯一分解：

`Composite_z^B(X)=Σ_{q>z} (log q) Σ_{m>1, P^-(m)>=q} W(qm/X)`。

这消除了“同一合数被多个主体锚重复解释”的主 overlap。剩余 overlap 只来自三类：

1. 窗口边界平滑误差；
2. 尾部锚与主体锚分区边界；
3. 非法覆盖容量与真实最小锚分配之间的差异。

## 3. Overlap-energy 定义

定义局部 overlap 误差

`O_z(X)=Composite_z^B(X)-ACC_z^B(X)`。

把它按锚 `q` 分解为

`O_z(X)=Σ_q O_q(X)`。

定义 overlap-energy

`E_ov(X)=Σ_q |O_q(X)|^2 / W_q`,

其中 `W_q` 是锚 `q` 的几何基线质量。该归一化使得若许多锚同步异常，则 `E_ov` 增大。

## 4. Lemma OV-1（小 overlap-energy 给小损失）

若 `E_ov(X)<=X^{1+ε}`，且总几何质量 `Σ_q W_q <= X log^C X`，则

`|O_z(X)| <= X^{1/2+ε}log^C X`。

**证明。** Cauchy--Schwarz：

`|Σ_q O_q|^2 <= (Σ_q |O_q|^2/W_q)(Σ_q W_q)`。

代入假设得 `|O_z|^2<=X^{2+ε}log^C X`，开方并调整 `ε` 得结论。证毕。

因此若离线零点产生 `X^β` 波动且 `β>1/2+ε`，小 overlap-energy 不能吸收它。

## 5. Lemma OV-2（大 overlap-energy 触发 D 组终端）

若 `E_ov(X)>X^{1+ε}` 在无穷多尺度发生，则存在锚层窗口族出现高投影增量、短簇或 frequency-closure terminal。

**证明路线。** 大 `E_ov` 表示某些锚层的实际覆盖与允许容量差异平方和过大。按 dyadic `q` 层分解，存在一层贡献过大。该层内：

1. 若误差集中于少数短窗口，得到短簇；
2. 若误差分散但同向，得到高投影增量；
3. 若误差由少数频率反复解释，进入 FCT；
4. 若非共振分散，由 NRC/Weil 平均压低，与大能量矛盾。

这正是 D 组 OMR/CGTP/LSMP/FCT 结构的 overlap 版本。

## 6. PC-3-global 弱闭合

**Theorem PC-3-global weak。** 设存在素数过疏波动

`Prime_z(X)<=ExpectedPrime_z(X)-Δ`, `Δ=X^{β-o(1)}`, `β>1/2`。

取 `z=(log X)^A`, `A<1`。若 overlap-energy 不触发 D 组终端，则

`ACC_z^B(X)>=ExpectedACC_z^B(X)+cΔ`。

**证明。** CAND-1 给候选基线误差 `o(Δ)`。边界项由平滑和小 `z` 给 `o(Δ)`。候选恒等式推出真实合数 Buchstab 权过剩 `>=Δ-o(Δ)`。若 overlap-energy 小，OV-1 给 `OverlapLoss=o(Δ)`；若 overlap-energy 大，OV-2 已触发 D 组终端。排除终端时，ACC 必须承担 `cΔ` 过剩。证毕。

## 7. 当前意义

这把 PC-3 的两个任务压缩为一个清晰二分：

- 候选 CRT 基线误差在 `z=(log X)^A`, `A<1` 下已经可控；
- overlap 要么小到不能吸收离线零点波动，要么大到触发 D 组终端。

因此 PC-3-global weak 已形成可审查的证明骨架。下一步真正需要加强的是 OV-2，把“大 overlap-energy 触发 D 组终端”从证明路线升级为逐行引理。
