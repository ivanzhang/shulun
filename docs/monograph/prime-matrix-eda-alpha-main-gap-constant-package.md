# EDA Alpha-MainGap 常数包：用粗高标签容量闭合主间隙

**状态：** `alpha_maingap_constant_package_reduction_open`

本文继续优化对角分支。关键新观察：

```text
若 alpha 足够接近 1，例如 alpha=0.9，
高标签容量无需第二命中精细上界；
粗界 C_alpha<=2(pi(p)-pi(alpha p)) 已可能被 Mertens 主量压住。
```

这把 `HCap-2Hit` 从必须项降级为优化项。

## 1. 粗高标签容量

对 `alpha>1/2`，每个高标签 `q in (alpha p,p)` 在 `[1,p-1]` 中最多命中两列。因此

\[
C_\alpha(p)\le
2\bigl(\pi(p-1)-\pi(\lfloor\alpha p\rfloor)\bigr).
\tag{AMG-1}
\]

这是完全初等的容量上界。

## 2. 显式常数包

假设存在显式常数 `c_M>0,C_\pi>0` 与阈值 `p_0`，使对所有 `p>=p_0`：

\[
V_\alpha(p)=\prod_{q\le \alpha p}\left(1-{1\over q}\right)
\ge {c_M\over\log p},
\tag{AMG-2}
\]

以及

\[
\pi(p-1)-\pi(\lfloor\alpha p\rfloor)
\le C_\pi(1-\alpha){p\over\log p}.
\tag{AMG-3}
\]

则

\[
(p-1)V_\alpha(p)-C_\alpha(p)
\ge
\left(c_M-2C_\pi(1-\alpha)+o(1)\right){p\over\log p}.
\tag{AMG-4}
\]

因此只要

\[
c_M>2C_\pi(1-\alpha),
\tag{AMG-5}
\]

就得到固定正主量间隙。

## 3. Alpha 阈值

条件 `(AMG-5)` 等价于

\[
\alpha>1-{c_M\over 2C_\pi}.
\tag{AMG-6}
\]

保守示例：若显式 Mertens 下界给 `c_M=0.45`，显式素数计数短区间上界给 `C_pi=1.30`，
则

\[
1-{0.45\over2\cdot1.30}\approx0.826923.
\tag{AMG-7}
\]

所以 `alpha=0.9` 有明显余量。

脚本：

```text
experiments/prime_matrix_alpha_main_gap_constant_scan.py
```

用于扫描常数阈值。

## 4. 对低模出口的影响

由 `DLS13-LowMod exclusion`，若主量间隙

\[
G_\alpha(p)=(p-1)V_\alpha(p)-C_\alpha(p)
\ge c_\alpha {p\over\log p}
\tag{AMG-8}
\]

成立，则任意固定 `D` 的低模坏相位在充分大 `p` 自动排除。

因此 `alpha=0.9` 下，低模出口可由标准显式 Mertens/PNT 常数包处理；不再需要先证明
`HCap-2Hit` 的精细分布。

## 5. 仍未闭合的部分

`AMG` 只处理主量间隙和固定低模出口。完整对角分支还需处理：

1. `Tail-Bad`: 高模尾项是否可能吞掉全部主量间隙；
2. 有限小素数段；
3. 显式常数引用的逐项核验。

换言之，本文证明：

```text
MainGap(alpha=0.9) follows from standard explicit Mertens/PNT constants.
```

但还没有证明：

```text
H_alpha(p)>C_alpha(p)
```

因为还需排斥尾项过强负缺陷。

## 6. 下一步最优

当前最优硬点从 `HCap-2Hit` 转为：

```text
AlphaTail(alpha=0.9):
prove E_{>D}(p) cannot be <= -(1-theta)G_alpha(p),
unless semiprime-shell/core SAE occurs.
```

这比原 `2/3` 路线有更大主量余量，是更好的总攻路径。
