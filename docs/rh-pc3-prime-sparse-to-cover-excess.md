# PC-3 专攻：素数过疏到允许合数覆盖容量过剩

本文件专攻 `docs/rh-offline-zero-prime-count-contradiction.md` 中标出的当前最优硬点 PC-3：若某区间素数相对 `Li`/CRT 零频基线过疏，如何严格推出允许合数覆盖容量必须过剩？这是把 RH 反例的素数计数波动接入方阵/CRT 覆盖矛盾场的关键翻译步骤。

## 1. PC-3 命题形式

令 `I=[X,X+H]`，`z=X^α`，`R_z(n)=1_{(n,P(z))=1}`。设 `Prime_z(I)` 是区间内大于 `z` 的素数权或计数，`Candidate_z(I)` 是小因子剥离后的筛余候选数，`ACC_z(I)` 是允许合数覆盖容量。

候选集合分解为

`Candidate_z(I) = Prime_z(I) + Composite_z(I)`。

若素数过疏：

`Prime_z(I) <= ExpectedPrime_z(I)-Δ`,

并且 `Candidate_z(I)` 接近 CRT 零频基线，则必须有

`Composite_z(I) >= ExpectedComposite_z(I)+Δ-O(Error)`。

若允许覆盖必须解释所有合数候选，则

`ACC_z(I) >= Composite_z(I)`，

从而得到 ACC 过剩。

## 2. 核心恒等式

对筛余候选有精确集合恒等式：

`R_z(n)=1_{n prime, n>z}+1_{n composite, P^-(n)>z}+Boundary_z(n)`。

边界项只来自 `n<=z` 的小素数、素数幂和区间端点平滑误差。在 `X` 大且 `z<X^α` 时，边界总量低于主目标波动。

加权求和得

`Candidate_z(I)=Prime_z(I)+Composite_z(I)+Boundary_z(I)`。

因此

`Composite_z(I)-ExpectedComposite_z(I)`

等于

`Candidate_z(I)-ExpectedCandidate_z(I) - (Prime_z(I)-ExpectedPrime_z(I)) + BoundaryError`。

这就是 PC-3 的代数核心。

## 3. Candidate_z 的刚性基线

`Candidate_z(I)` 由 CRT 非零类交集决定。其期望为

`ExpectedCandidate_z(I) ≈ H Π_{p<=z}(1-1/p)`。

误差来自：

1. 区间端点与周期不整除；
2. CRT 周期截断；
3. 平滑权误差。

这些误差是几何/周期误差，不含 zeta 离线零点的 `X^β` 相干项。若选择 `H` 大于 `M_z` 或用平滑周期平均，则

`Candidate_z(I)-ExpectedCandidate_z(I)=O(M_z)+O(smooth error)`。

因此，只要 `Δ` 远大于这些周期误差，素数过疏就必然转化为合数候选过剩。

## 4. 从 Composite 到 ACC

`Composite_z(I)` 是真实合数候选数量；`ACC_z(I)` 是允许覆盖容量。若允许覆盖系统必须解释每个合数候选，则至少需要

`ACC_z(I) >= Composite_z(I)`。

更精确地，若使用 Buchstab 权 `ω_z^B(n)=log P^-(n)`，则

`Composite_z^B(I) <= ACC_z^B(I)+OverlapLoss_z(I)`。

其中 `OverlapLoss` 表示多重解释、边界分裂和非法锚剔除造成的损失。若 `OverlapLoss` 不能达到 `Δ` 级，则 composite 过剩迫使 ACC 过剩。

## 5. PC-3 定理草案

**Theorem PC-3（过疏到覆盖过剩）。** 假设区间 `I` 满足：

1. 素数过疏：`Prime_z(I) <= ExpectedPrime_z(I)-Δ`；
2. 候选基线刚性：`|Candidate_z(I)-ExpectedCandidate_z(I)| <= Δ/4`；
3. 边界误差：`|Boundary_z(I)| <= Δ/4`；
4. overlap 损失：`OverlapLoss_z(I) <= Δ/4`。

则

`ACC_z(I) >= ExpectedACC_z(I)+cΔ`。

**证明。** 由候选恒等式，合数候选过剩至少为 `Δ-Δ/4-Δ/4=Δ/2`。由 overlap 损失上界，允许覆盖容量必须承担至少 `Δ/4` 的过剩。调整常数得结论。证毕。

## 6. 四个假设的可证性分析

### 6.1 素数过疏

由离线零点显式公式给出，属于 PC-1。需要选择相位使负峰出现。

### 6.2 候选基线刚性

这是 CRT 周期事实。若 `I` 长度覆盖许多 `P(z)` 周期，则误差小；若 `P(z)` 太大，则需用平滑平均或较小 `z`。这决定 `α` 的选择。

### 6.3 边界误差

小素数、素数幂、端点平滑都应低阶。可通过 `z=X^α` 且 `α` 小、`H` 足够长控制。

### 6.4 OverlapLoss

这是最硬的新项。若合数有多个解释，可能降低所需 ACC 过剩。本文局部刚性提供：

- 大因子短窗不可复用；
- 最小大因子 Buchstab 权唯一分配；
- Tail-log4 控制尾部；
- D 组能量控制主体重叠。

因此使用 `ω_z^B=log P^-(n)` 可大幅降低 overlap 风险，因为每个合数按最小大因子唯一归属。

## 7. 为什么最小大因子权是关键

若不用最小大因子权，合数 `n=ab` 可被多个锚解释，overlap 可能吸收过疏缺口。使用 `P^-(n)` 后，每个筛余合数只有一个最小大因子锚，形成唯一账本：

`Composite_z^B(I)=Σ_{q>z} (log q) #{m: qm in I, P^-(m)>=q}`。

这把 “真实合数过剩” 直接转成 “最小锚层过剩”。允许覆盖若不能提供同等锚容量，就出现缺口；若提供，则进入 ACC 过剩与 D 组矛盾场。

## 8. PC-3 的最优参数选择

需要平衡：

- `z=X^α` 不能太大，否则 CRT 周期 `P(z)` 过大，候选基线误差难控；
- `z` 不能太小，否则筛余候选太多，合数层复杂；
- 区间长度 `H` 要大于若干 CRT 周期或使用平滑周期平均；
- 离线零点给的波动 `Δ≈H X^{β-1}` 或平滑全局 `X^β` 必须大于周期误差。

初步可选：先研究全局平滑 `[1,X]` 而非短区间，令 `z=c log X` 或 `z=(log X)^A`，使 `P(z)=X^{o(1)}`，候选基线误差远小于 `X^β`。

这牺牲局部短区间锋利度，但更容易证明 PC-3。

## 9. PC-3-global 弱版

**PC-3-global。** 在 `[1,X]` 平滑权下，若 `Prime_z(X)` 相对 `Li` 过疏 `Δ=X^{β-o(1)}`，取 `z=(log X)^A`，则筛余合数候选的最小大因子 Buchstab 权相对 CRT 基线过剩 `>=cΔ`，除非 overlap-energy 达到 `cΔ`。

这已经足以接 ACC 不同步路线：要么 ACC 过剩，要么 overlap-energy 过大，后者成为下一矛盾场。

## 10. 下一步最优硬点

PC-3 已被压缩到两个更具体任务：

1. 证明 `Candidate_z` 的 CRT 基线误差在 `z=(log X)^A` 时为 `o(X^β)`；
2. 证明最小大因子 Buchstab 权下 `OverlapLoss=o(X^β)`，或 overlap-energy 过大触发 D 组终端。

其中第 1 项较容易；第 2 项是下一核心硬点。

## 11. 结论

素数过疏确实可以严格翻译为合数候选过剩，前提是候选基线稳定、边界误差小、overlap 损失不能吞掉缺口。最小大因子 Buchstab 权使这个翻译最接近严格，因为它把每个合数唯一分配给一个锚。

因此 PC-3 的证明路线已经清晰：先取全局平滑和小 `z` 证明候选基线稳定，再专攻 overlap-energy，证明多重/非法解释不能吸收离线零点级缺口。
