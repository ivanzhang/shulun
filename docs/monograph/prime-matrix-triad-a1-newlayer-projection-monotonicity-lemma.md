# Triad-A1 Lift-B：新层投影单调性引理

**状态：** `projection_monotonicity_proved_for_lhb_M_support`

本文攻 `Lift-A` 后留下的最窄口径硬点：

```text
N = A_Q' \ pi^{-1}(A_Q)
```

是否可能非空？对当前 LHB allowed-set 的 `M_Q(t)` 定义，答案是否定的。只要 `Q|Q'` 且二者都是同一个
根基周期 `B_P=prod_{ell<P} ell` 的因子，新层支撑投影必然落在旧层支撑内。

## 1. 全周期完成集合

固定奇素数 `P`，令

```text
B_P = product_{ell<P} ell。
```

定义全周期完成集合：

```text
C_P = {R mod B_P :
       对每个 1<=c<P，存在 ell<P 使 ((R-1)P+c) == 0 mod ell }。
```

这是不依赖 `Q` 的真实对象。不同 `Q` 只是把同一个 `C_P` 投影到不同低模层。

对任意 `Q|B_P`，定义

```text
M_Q(t)=#{R in C_P : R == t mod Q}。
```

于是

```text
A_Q = supp(M_Q) = pi_Q(C_P)。
```

这与机器脚本里的 `low_holes_for_phase + high_completion_stats` 等价：固定 `t mod Q` 后，所有
`R=t+Qy mod B_P` 的选择正是高层 CRT 变量 `y`，`completion_count(t)` 正是满足全列覆盖的 `R` 数。

## 2. 投影单调性

设

```text
Q' = rQ,   pi: Z/Q'Z -> Z/QZ。
```

若 `u in A_Q'`，则存在 `R in C_P` 使

```text
R == u mod Q'。
```

令 `t=pi(u)`。因为 `Q|Q'`，必有

```text
R == t mod Q。
```

所以 `t in A_Q`。因此：

\[
\pi(A_{Q'})\subseteq A_Q.
\tag{LPM-1}
\]

等价地，

\[
N=A_{Q'}\setminus\pi^{-1}(A_Q)=\varnothing.
\tag{LPM-2}
\]

证明只用了同一个全周期完成集合 `C_P`，没有任何概率输入。

## 3. fiber 删除公式自动纯化

由 `N=empty`，`Lift-A` 的恒等式直接变成：

\[
|A_{Q'}|=\sum_{t\in A_Q}s(t),
\quad
\delta_{Q'}=\delta_Q\cdot {1\over |A_Q|}\sum_{t\in A_Q}{s(t)\over r}.
\tag{LPM-3}
\]

因此当前 LHB `M(t)` 分支内不需要保留 `ProjectionStitching` 作为同层出口。它只会在换了 formal unit、
换了坏窗集合或把诊断支撑当成正式容量时重新出现。

## 4. 对升层塔的意义

沿同一个 `C_P` 的轮筛塔

```text
Q0 | Q1 | Q2 | ... | B_P
```

每一步都满足：

```text
A_{Q_{n+1}} projects into A_{Q_n}。
```

所以递归剥离剩下真正的二分是：

```text
FiberDeletion:
  平均 s(t)/r 明显小于 1，支撑重新稀疏；

NoDeletion:
  s(t)/r 接近 1，必须检查 fiber 条件分布。
```

`NoDeletion` 再进入：

```text
KL 偏斜持续   => refined/new-layer PDEC；
KL 近零平坦   => CleanKLS/DLS。
```

这比原来的四分更硬：在 LHB `M_Q` 支撑上，`ProjectionStitching` 已被同一 `C_P` 口径消掉。

## 5. 与已物化审计的关系

已物化两层：

```text
2310 -> 30030；
30030 -> 510510。
```

机器审计均得到：

```text
all_monotone_lift_support=True。
```

现在这项读数不再只是经验验证，而是 `(LPM-1)` 的有限复核。真正有信息量的是删除强度：

```text
2310 -> 30030:  min density drop 3.19672；
30030 -> 510510: min density drop 6.13889。
```

## 6. 闭合边界

本文完成：

```text
LHB allowed-set 的 M_Q 支撑投影单调性；
N=empty 的一般证明；
升层塔中 ProjectionStitching 出口的条件性删除。
```

本文未完成：

```text
任意后继层都产生足够 FiberDeletion；
NoDeletion 分支的 KL/PDEC 或 CleanKLS 终端排斥；
真实 PDEC 坏窗集合 S 与 LHB allowed-set 的全局同一性之外的分支。
```

因此 `Lift-B` 闭合了升层口径硬点，但最终行命题仍要继续攻 `FiberDeletion vs NoDeletion` 的全局二分。
