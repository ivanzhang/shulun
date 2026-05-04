# EDA 对角最终硬核边界：精确相位而非字符全反相

**状态：** `diagonal_final_hardcore_boundary_open`

本文继续专攻当前最小剩余：`x=p` 对角端点。上一轮得到二次相位锁：

\[
q\mid p^2+k\Longrightarrow \chi_q(k)=\chi_q(-1).
\tag{DFH-1}
\]

本轮审计和结构复核表明：`Legendre` 全反相条件只是强充分条件，不是可行主路线；真实硬核仍是
精确单残基避让：

\[
\exists\,1\le k<p:\quad
k\not\equiv -p^2\pmod q\quad\text{for all }q<p.
\tag{DFH-2}
\]

这等价于 `(p^2,p^2+p)` 中存在素数。

## 1. 强字符路线的失效边界

强条件要求存在偶数 `k<p`，使对每个奇素数 `q<p`：

\[
\chi_q(k)=-\chi_q(-1).
\tag{DFH-3}
\]

它确实推出 `p^2+k` 为素数，但样本显示实际幸存列通常只对约一半奇素数满足反相。
例如审计脚本

```text
experiments/prime_matrix_diagonal_qpl_audit.py
```

给出：

| p | diagonal_U | survivor k examples | odd primes | opposite Legendre count range |
|---:|---:|---|---:|---:|
| 23 | 2 | 12,18 | 7 | 3 |
| 101 | 11 | 10,22,42,... | 24 | 8--15 |
| 499 | 40 | 16,36,58,... | 93 | 39--52 |
| 997 | 78 | 4,18,30,... | 166 | 74--90 |

因此 `(DFH-3)` 过强；若继续把它作为闭合目标，会排除真实素数幸存列本身。

## 2. 精确相位才是必要充分条件

对角筛余为

\[
U_p(p)=
\#\{1\le k<p:(p^2+k,M_p)=1\},
\qquad M_p=\prod_{q<p}q.
\tag{DFH-4}
\]

所以 `U_p(p)>0` 等价于 `(DFH-2)`。这里每个 `q` 只禁止一个残基；二次字符只说明该残基
落在哪个二次字符半边，不能替代精确残基避让。

换言之，对角硬核不是：

```text
找一个列 k 同时满足所有二次字符反相。
```

而是：

```text
证明固定单残基族 {-p^2 mod q}_{q<p} 不能覆盖 [1,p-1]。
```

## 3. 与短区间素数问题的精确关系

**定理 DFH-1（对角硬核等价素数平方后一半区间）。**  
对任意奇素数 `p`，

\[
U_p(p)>0
\quad\Longleftrightarrow\quad
\pi(p^2+p-1)-\pi(p^2)>0.
\tag{DFH-5}
\]

**证明。**  
这正是 DBB-1 的重新编号：若 `p^2+k` 未被 `<p` 素数整除，由
`p^2<p^2+k<(p+1)^2` 可知它只能是素数；反向显然。证毕。

因此任何完整证明 `X_0(p)>p` 的论文必须提供 `(DFH-5)` 的新证明，或者提供更强的
ExactEndpoint-MinRep 缺陷排斥。不能只用以下材料替代：

1. CRT 全周期均衡；
2. 变量阶 Bonferroni 点态消尾；
3. 内部因子降阶；
4. 二次字符必要条件；
5. 普通总容量启发。

## 4. 为什么当前已有工具还差一步

普通筛给出的期望主量约为

\[
(p-1)\prod_{q<p}\left(1-\frac1q\right)\asymp {p\over\log p}.
\tag{DFH-6}
\]

这解释了样本中 `diagonal_U` 为 `p/log p` 量级。但要把期望变成逐点正性，需要端点下界筛；
在筛长 `H=p`、筛界 `z=p` 的临界位置，普通下界筛遇到奇偶障碍，不能自动推出正性。

已归档的变量阶布尔消尾只证明

\[
S_{K_p}(p,p)=U_p(p),
\tag{DFH-7}
\]

没有给出 `U_p(p)>0` 的正下界。因此它排除了“尾项技术假障碍”，但没有突破
`DFH-5` 的短区间硬核。

## 5. 当前可继续攻击的最窄接口

对角分支现在只能沿三条诚实路线继续：

### 路线 A：对角精确相位 PDEC

证明若单残基族全覆盖 `[1,p-1]`，则低模 Fourier 能量或端点 sawtooth 缺陷超过 PDEC
允许阈值。目标形式：

\[
\sum_{0<|h|<Q}
\left|
\sum_{q<Q} e\!\left(h(-p^2)\over q\right) w_q
\right|^2
\le \text{admissible bound},
\tag{DFH-8}
\]

并把失败局部化为有限坏相位证书。

### 路线 B：固定相位 Jacobsthal 边界

把 `(DFH-2)` 看成 primorial 模 `M_p` 上从 `p^2+1` 开始的局部 Jacobsthal 问题。
需要证明这个特殊起点不可能处于长度 `p-1` 的全非互素块。

注意：全局 Jacobsthal 上界若大于 `p` 不够；必须使用起点 `p^2` 的特殊相位。

### 路线 C：外部短区间素数输入

若引用一个能保证

\[
\pi(n+\sqrt n)-\pi(n)>0
\tag{DFH-9}
\]

在 `n=p^2` 上成立的外部定理，则对角分支立即闭合。但这已是平方根长度素数间隔输入，
必须作为外部深定理明确列出，不能说成由 CRT 初等推出。

## 6. 审稿结论

当前最小剩余已压到：

```text
Diagonal Exact Phase Non-Coverage:
prove {-p^2 mod q : q<p} does not cover [1,p-1].
```

内部因子分支的 PDL/FactorDescent 进展仍然有效，但它不能覆盖 `x=p`。因此全局闭合必须满足：

```text
Internal branch closed
AND
Diagonal exact phase branch closed.
```

本文完成的是对角硬核的最终边界澄清和路线筛选；尚未证明 `(DFH-2)`。下一步最优应直接专攻
路线 A：对角精确相位 PDEC，而不是继续加强已失效的 Legendre 全反相充分条件。
