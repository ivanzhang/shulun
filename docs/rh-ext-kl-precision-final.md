# EXT-KL 精确适配最终记录

本文专门消除清单中残留的 `EXT-KL` 精确适配义务。它只处理主稿实际调用的单变量、素数模、非退化 Kloosterman 型完成和，不扩展到一般模数或高维族。

## 1. 使用命题

**Proposition EXT-KL-Restricted.** 设 `p` 为素数，`a,b\in F_p` 且 `ab\ne0`。则

`|Σ_{x\in F_p^*} e_p(ax+b/x)| <= 2p^{1/2}`。

若 `I\subset F_p` 为区间，则通过 additive completion，

`|Σ_{x\in I, x\ne0} e_p(ax+b/x)| <= C p^{1/2}\log p`。

这里 `C` 为绝对常数；主稿只把它作为固定对数损失使用。

## 2. 标准来源

- Iwaniec--Kowalski, *Analytic Number Theory*, Chapter 12：Kloosterman sums、Weil bound 与 completion 方法。
- Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups*：几何形式的 Kloosterman sheaf 与 Riemann Hypothesis over finite fields 支撑的平方根相消。

## 3. 变量匹配

主稿中的 NRC 单变量入口在局部化后具有相位

`e_p(a x + b/x)`，

其中模数是某个素数层 `p`，变量 `x` 遍历非零同余类或其区间截断，且非退化条件为 `ab\ne0 mod p`。

- 若 `a=0` 或 `b=0`，该入口不调用 `EXT-KL`，而进入 FCT/退化相位出口。
- 若变量不在完整 `F_p^*` 上，先用 additive completion，额外损失 `O(log p)`。
- 若存在多个 dyadic/模板入口，总数已由 AEX-3 表限制为 `log^C X`。

## 4. 对 AEX-3 的贡献

单变量 NRC 入口总负担满足

`Load_1(NRC;X) <= X^{1/2}\log^C X`。

由于反设离线零点给出的异常尺度为 `Δ=X^{β-o(1)}` 且 `β>1/2`，故

`X^{1/2}\log^C X=o(Δ)`。

因此单变量 NRC 入口在 `EXT-KL-Restricted` 下闭合。Tail/RKS、双变量 PPI 与 DSO-E 入口不由本命题直接闭合，它们按 AEX-3 的 Transfer/DSO-SF 路由处理。

## 5. 审稿结论

清单中“`EXT-KL` 精确适配”应标记为完成：主稿只使用素数模非退化 `ax+b/x` 完成和，来源、变量匹配、退化出口和对数损失均已明确。该记录不声称所有 NRC 分支由 `EXT-KL` 单独闭合；它只闭合 AEX-3 中的单变量外部输入。
