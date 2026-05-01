# I2 自适应分层与 Single-Prime CRTDefect 二分审查（2026-05-01）

## 目标

I2 原要求：自适应真实命中分层可执行，并且单素数贡献过大时进入 Single-Prime CRTDefect 出口。

本轮证明显示：分层算法本身是无条件的贪心分解；唯一非平凡情况是单素数大贡献，而这正是 I3 需要排除的 CRTDefect。

## 文稿位置

- `docs/monograph/two-point-secondary-sieve-research.md` 第 350--353 节；
- `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 的 `Adaptive true-hit layering dichotomy` 引理。

## 分层引理

对当前真实剩余集 `U_Y`，定义

\[
a_p=\frac1{|U_Y|}\#\{x\in U_Y:x\equiv0\text{ or }w\pmod p\}.
\]

取 `eta=0.05`。若所有 `a_p<=eta`，则按素数顺序贪心累加，得到连续薄层 `P_j`，满足

\[
\nu_j^{real}=\sum_{p\in P_j}a_p\le0.4,
\]

且除末层外

\[
\nu_j^{real}>0.4-\eta\ge0.35.
\]

证明只用 `a_p<=eta` 和贪心停止规则。

## 缺陷出口

若存在 `a_p>eta`，则 `U_Y` 在模 `p` 的两个坏相位类 `0,w` 上有固定正比例集中。这推出差值集合在 `mod p` 的 `0,±w` 类上产生二阶投影能量异常。该异常即 Single-Prime CRTDefect，归入 I3 的 CRTDefect/Directional Balance 排除。

## 当前状态

I2 不再作为独立条件输入。当前唯一剩余核心输入是 I3：

- SC2 二阶相关；
- 45-Main 主同步削峰；
- 小 `q<=100` 有限包；
- Single-Prime CRTDefect 排除；
- I4 所需矩常数与端点 Directional Balance。
