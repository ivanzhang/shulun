# BPN low-hole bucket 容量命题

**状态：** `exact_high_layer_completion_identity_proved_symbolic_capacity_open`

本文把上一轮 `low-hole bucket` 的有限读数提升一层：不再把完整 CRT 周期当黑箱枚举，
而是将它拆成低骨架洞集与高层 CRT 补洞变量。

## 1. 低骨架与高层变量

固定低模

\[
Q=\prod_{\ell\in L}\ell,
\]

其中 `L` 是低根基素数集合。对行相位 `t mod Q`，仅用 `L` 覆盖列
`1<=c<P` 后得到低骨架洞集

\[
H_Q(t)=\{c: (t-1)P+c\not\equiv0\pmod \ell,\ \ell\in L\}.
\]

令高根基素数集合

\[
R=\{\ell<P:\ell\notin L\},\qquad M_R=\prod_{\ell\in R}\ell.
\]

所有同一低相位的行可写为

\[
r=t+Qy,\qquad y\bmod M_R.
\]

## 2. 精确补洞同余

对高素数 `ell in R` 与低洞 `c in H_Q(t)`，格点被 `ell` 覆盖当且仅当

\[
(t+Qy-1)P+c\equiv0\pmod \ell.
\]

因为 `gcd(QP,ell)=1`，这等价于

\[
y\equiv (1-cP^{-1}-t)Q^{-1}\pmod \ell.
\tag{1}
\]

于是每个洞 `c` 对每个高素数 `ell` 给出一个 `y mod ell` 的禁/补洞相位。

## 3. 完成容量恒等式

定义

\[
C_P(t;Q)=
\#\left\{
y\bmod M_R:
\forall c\in H_Q(t),\ \exists \ell\in R
\text{ 使 } y\equiv a_{\ell,c,t}\pmod\ell
\right\},
\]

其中 `a_{ell,c,t}` 由 `(1)` 给出。

**Theorem LHB-1（高层补洞恒等式）。**
对每个低相位 `t mod Q`，`C_P(t;Q)` 精确等于完整 CRT 周期中行相位为 `t mod Q`
的零行数。

**证明。**
行 `r=t+Qy` 中，低素数集合 `L` 已覆盖非洞列；剩余列正是 `H_Q(t)`。某个洞 `c`
被完整根基筛覆盖，当且仅当存在高素数 `ell in R` 使 `(r-1)P+c≡0 mod ell`。
由上节代数，这等价于 `(1)`。所有洞同时被覆盖，正是定义 `C_P(t;Q)` 的条件。
`y mod M_R` 与同一低相位下完整 CRT 周期中的行一一对应。证毕。

## 4. 有限读数给出的符号化目标

脚本 `experiments/prime_matrix_bpn_low_hole_bucket_capacity.py` 对 `Q=210` 扫描
`P=13,17,19,23`。核心现象是：

```text
高洞数低相位的 completion_count 迅速归零；
P=23 时 |H_Q(t)|>=5 的相位全部 completion_count=0。
```

低范围 `P<=23,Q=210` 中有一个更强的诊断读数：

```text
P=13: high prime count=1, max holes with completion=1；
P=17: high prime count=2, max holes with completion=2；
P=19: high prime count=3, max holes with completion=3；
P=23: high prime count=4, max holes with completion=4。
```

同时，在所有成功补洞样本中，单个高素数最多补一个低骨架洞：

```text
max single-prime cover on completion = 1。
```

但该“单洞匹配”不是一般定理。扩大到 `P>=29` 后，同一高素数的一个残基类可能覆盖两个
低骨架洞。因此最终路线必须使用更一般的残基类 set-cover/Hall 亏损，而不是坚持单洞匹配。

因此下一步符号化目标可写为：

**Conjectural Lemma LHB-2（高洞数补洞容量排斥）。**
存在显式阈值 `m_0(P,Q)`，使得

\[
|H_Q(t)|\ge m_0(P,Q)\quad\Longrightarrow\quad C_P(t;Q)=0.
\]

在 `P=23,Q=210` 的有限账本中，`m_0=5`。

一个低范围可用的充分条件是：

**Lemma Target LHB-3（高素数单洞匹配）。**
若对给定低相位 `t`，任一成功补洞的 `y` 下，每个高根基素数 `ell in R`
至多覆盖一个低骨架洞，则

\[
C_P(t;Q)>0\quad\Longrightarrow\quad |H_Q(t)|\le |R|.
\]

因此若

\[
|H_Q(t)|>|R|,
\]

则 `C_P(t;Q)=0`。

该命题只在 `P=13,17,19,23,Q=210` 的有限样本中吻合。一般情形应替换为下面的精确
set-cover 定理。

## 4A. 精确 set-cover 形式

对每个高素数 `ell in R` 和残基 `a mod ell`，定义其在低洞集上的覆盖块

\[
B_{\ell,a}(t)=\{c\in H_Q(t): a_{\ell,c,t}=a\}.
\]

由 CRT 独立性，每个 `y mod M_R` 等价于对每个 `ell in R` 选择一个残基 `a_\ell mod ell`。
因此

\[
C_P(t;Q)>0
\]

当且仅当存在一组选取 `a_\ell`，使

\[
H_Q(t)\subseteq \bigcup_{\ell\in R}B_{\ell,a_\ell}(t).
\tag{2}
\]

这就是精确的多素数残基类 set-cover 问题。

**Lemma LHB-4a（列残基刚性）。**
对任意高素数 `ell in R` 与任意两洞 `c,c' in H_Q(t)`，

\[
a_{\ell,c,t}=a_{\ell,c',t}
\quad\Longleftrightarrow\quad
c\equiv c'\pmod\ell.
\]

因此

\[
m_\ell(W):=\max_{a\bmod\ell}|W\cap B_{\ell,a}(t)|
=\max_{b\bmod\ell}|W\cap\{c:c\equiv b\pmod\ell\}|.
\tag{2a}
\]

**证明。**
由 `(1)`，

\[
a_{\ell,c,t}-a_{\ell,c',t}=-(c-c')P^{-1}Q^{-1}\pmod\ell.
\]

因为 `ell` 不整除 `P Q`，`P^{-1}Q^{-1}` 在 `mod ell` 下可逆，所以差为零当且仅当
`c-c'≡0 mod ell`。证毕。

**Lemma LHB-4（Hall 型容量亏损证书）。**
若存在子集 `W⊆H_Q(t)` 使

\[
|W|>
\sum_{\ell\in R}\max_{a\bmod\ell}|W\cap B_{\ell,a}(t)|,
\tag{3}
\]

则 `C_P(t;Q)=0`。

**证明。**
任意一个 `y` 对每个高素数 `ell` 只选择一个残基类 `B_{\ell,a_\ell}`。因此它在 `W`
中最多覆盖
`\sum_{\ell}\max_a |W∩B_{\ell,a}|` 个洞。若 `(3)` 成立，则任何选择都不能覆盖整个
`W`，更不能覆盖 `H_Q(t)`。证毕。

脚本 `experiments/prime_matrix_bpn_low_hole_bucket_capacity.py` 已加入该 Hall 亏损搜索。
读数显示：

```text
Q=210:
  P<=31 的全部 zero phases 由 Hall 亏损覆盖；
  P=37 仅剩 4 个 zero phases 未由当前子集搜索覆盖；
  P>=43 在 Q=210 下无 zero phases。

Q=2310:
  P=13,17,19,23,29,31,37,43,47 的全部 zero phases
  均由 Hall 亏损证书覆盖。
```

更细的 `Q=2310` 证书形态不是“任意子集搜索”那么松。这里必须按“最小删洞数”
分类，而不是按“最大亏损优先”的任意见证分类。设

\[
d(t)=|H_Q(t)|-|W_t|,
\]

其中 `W_t` 取删洞数最小的 Hall 亏损见证。修正后的实际读数为：

```text
P=13: {d=0: 2306}
P=17: {d=0: 2282}
P=19: {d=0: 2170}
P=23: {d=0: 2078}
P=29: {d=0: 2160}
P=31: {d=0: 1714}
P=37: {d=0: 1500}
P=43: {d=0: 220, d=1: 40}
P=47: {d=0: 32,  d=1: 12}
```

因此当前最窄可攻目标应写成二层容量亏损，而不是泛泛的子集存在：

```text
对实际 PDEC 所需的 low-hole zero bucket，
证明 H_Q(t)、或 H_Q(t) 删除 1 个洞
已经满足 Hall 容量亏损不等式。
```

这一步把搜索空间从任意 `W⊆H_Q(t)` 压缩为“整洞集/一洞删除”二分。
先前出现的二洞删除是证书选择口径造成的假例外：同一相位的整洞集已经 Hall 亏损，
只是最大亏损搜索先遇到了较小子集。

一洞删除本身也有明确机制。令

\[
m_\ell(W)=\max_{a\bmod\ell}|W\cap B_{\ell,a}(t)|.
\]

若 `Delta(H)=0`，但存在洞 `c_*` 使

\[
\sum_{\ell\in R}\bigl(m_\ell(H)-m_\ell(H\setminus\{c_*\})\bigr)\ge2,
\tag{4}
\]

则

\[
\Delta(H\setminus\{c_*\})
=\Delta(H)-1+\sum_{\ell\in R}\bigl(m_\ell(H)-m_\ell(H\setminus\{c_*\})\bigr)>0.
\]

这说明 `c_*` 是一个“桥洞”：它同时支撑至少两个高素数的最大残基覆盖块；
删去一个洞却让总容量下降至少两个单位。新增审计
`prime-matrix-bpn-lhb-bridge-deletion-audit.md` 显示，`Q=2310` 的全部一洞删除相位
都由该桥洞条件认证，且样本中支撑素数均为 `[13,19]`。

新增列残基刚性审计
`prime-matrix-bpn-lhb-column-residue-rigidity-audit.md` 进一步确认：

```text
Q=2310, P=13..47:
zero bucket 全部满足下列二分之一：
1. Delta(H_Q(t))>0；
2. Delta(H_Q(t))=0，且存在桥洞 c_*。

临界态只出现在 P=43,47；
全部临界态的桥洞均为 13 与 19 的唯一最大列残基块交点。
```

扩展审计 `prime-matrix-bpn-lhb-column-residue-rigidity-extended.md` 检查 `P=53,59,61`：

```text
P=53: zero bucket = 0；
P=59: zero bucket = 8，全部 Delta(H)>0；
P=61: zero bucket = 0。
```

因此桥洞交叉不是大范围常态，而是 `Q=2310` 下 `P=43,47` 的临界机制；
越过该临界带后，low-hole zero bucket 要么消失，要么由整洞集直接 Hall 亏损覆盖。

进一步的贪心补洞审计
`prime-matrix-bpn-lhb-greedy-cover-transition-audit.md` 给出构造性非零证书：

```text
Q=2310:
P=53: greedy fail = 26；
P=59: greedy fail = 22；
P>=61, P<=109: greedy fail = 0。
```

贪心证书每一步选择一个高素数 `ell` 与一个列残基类 `b mod ell`，覆盖尚未覆盖的所有
`c≡b mod ell` 的低洞。若贪心成功，则直接给出一组高层残基选择，因此
`completion_count(t)>0`，该相位不可能是 zero bucket。

因此下一步最窄硬点已从“单洞匹配”校正为：

```text
证明实际 PDEC 所需的 low-hole zero buckets
均满足整洞集 Hall 亏损；
若整洞集刚好临界，则存在桥洞 c_* 满足 (4)。
```

## 5. 证明路线

`LHB-2` 的证明不能再靠平均密度。最直接路线是 Hall/CRT 不相容：

1. 对每个洞 `c` 形成高素数补洞残基族
   \[
   \mathcal A_c=\{(\ell,a_{\ell,c,t}):\ell\in R\}.
   \]
2. 若所有洞可同时补完，则存在 `y` 命中每个 `\mathcal A_c` 至少一次。
3. 同一高素数 `ell` 能同时补多个洞只在这些洞的目标残基相容时发生；
4. 多个高素数组合给出 CRT 交，若组合族不能覆盖全部洞，则 `C_P(t;Q)=0`。

这正是低洞 bucket 的下一层最窄硬点：

```text
把 completion_count=0 证明为下列两类之一：
Delta(H_Q(t))>0；
或存在桥洞 c0 使 Delta(H_Q(t)\{c0})>0。
```

其中

\[
\Delta(W)=|W|-\sum_{\ell\in R}\max_{a\bmod \ell}|W\cap B_{\ell,a}(t)|.
\]

该形式是当前最窄的审稿义务：只需解释整洞集容量亏损，以及临界整洞集中的桥洞容量下降，
而不再需要无限制搜索任意 Hall 子集。

更具体地，最终应证明下列低骨架列残基命题：

**Target LHB-5（整洞集亏损或桥洞交叉）。**
对实际 `PDEC` 所需的低骨架洞集 `H=H_Q(t)`，若高层补洞 set-cover 不可完成，则

\[
\Delta(H)>0
\]

或存在两个高素数 `ell_1,ell_2 in R` 与洞 `c_* in H`，使 `c_*` 同时属于
`ell_1` 与 `ell_2` 的唯一最大列残基块，并且

\[
\Delta(H\setminus\{c_*\})>0.
\]

该目标只涉及列集合 `H` 在高素数模数下的最大残基块交叉，不再涉及完整 CRT 周期变量 `y`。

**Target LHB-6（转折后贪心补洞）。**
对固定低模 `Q=2310`，证明存在显式转折阈值 `P_g`，使得对所有 `P>=P_g`
和所有低相位 `t mod Q`，低洞集 `H_Q(t)` 可由高素数列残基块贪心覆盖。
等价地，存在互异高素数 `\ell_1,\ldots,\ell_s` 与残基 `b_i mod \ell_i`，使

\[
H_Q(t)\subseteq \bigcup_i\{c:c\equiv b_i\pmod{\ell_i}\}.
\]

实验账本支持 `P_g=61`。最新低范围最终证书又确认 `13<=P<61` 的 zero bucket
已经由整洞集亏损、桥洞临界和精确 DP 临界三类全部闭合；`P=59` 的 8 个相位仍属
整洞集直接亏损，不再是独立结构缺口。

进一步的增益账本显示，`Target LHB-6` 的可证明核心不是完整贪心算法本身，而是
小高素数列残基块提供的重复增益。

**Lemma LHB-6a（重复增益充分条件）。**
设贪心或任意构造过程选出互异高素数残基块

\[
C_i=H_Q(t)\cap(b_i\bmod \ell_i),\qquad \ell_i\in R,
\]

并覆盖全部 `H_Q(t)`。令 `s` 为所用块数，

\[
D(t)=|H_Q(t)|-s
=\sum_i(|C_i\setminus(C_1\cup\cdots\cup C_{i-1})|-1)
\]

为重复增益。若

\[
D(t)\ge |H_Q(t)|-|R|,
\tag{5}
\]

则 `s<=|R|`，所以可把这些块赋给互异高素数，得到 `completion_count(t)>0`。

**证明。**
由定义 `s=|H_Q(t)|-D(t)`。条件 `(5)` 给出 `s<=|R|`。每个被选块来自一个互异高素数的
一个列残基类；按列残基刚性 `LHB-4a`，这等价于对该高素数选择一个高层 `y mod ell`
残基。所有块覆盖 `H_Q(t)`，所以 set-cover 条件 `(2)` 成立。证毕。

新增贪心转折审计显示：

```text
P>=61, P<=109:
全部 2310 个低相位满足 (5)；
重复增益主要来自 13,17,19,23，随后由 29,31,37,... 补强。
```

因此 `Target LHB-6` 可进一步压缩为：

```text
证明 P>=61 时，小高素数碰撞梯给出的重复增益
D(t) 至少为 |H_Q(t)|-|R|。
```

再进一步，动态贪心的选择自由不是必要的。固定碰撞梯审计
`prime-matrix-bpn-lhb-fixed-ladder-audit.md` 使用完全确定的高素数升序

\[
13,17,19,23,29,31,37,\ldots
\]

并在每个高素数上选择当前未覆盖洞中最大的一个列残基块。读数显示：

```text
Q=2310:
P=53 fixed-ladder fail = 44；
P=59 fixed-ladder fail = 36；
P>=61, P<=149 fixed-ladder fail = 0。
```

这把转折后范围的目标继续压缩为固定顺序命题。

**Target LHB-7（固定小高素数碰撞梯）。**
对 `Q=2310` 与 `P>=61`，令高素数按升序排列。对任意低相位 `t`，
从 `H_0=H_Q(t)` 开始递推：

1. 在第 `j` 个高素数 `\ell_j` 下，取使
   `|H_{j-1}\cap(b mod \ell_j)|` 最大的列残基 `b_j`；
2. 删除该块：
   \[
   H_j=H_{j-1}\setminus \{c\in H_{j-1}:c\equiv b_j\pmod{\ell_j}\}.
   \]

则存在 `s<=|R|` 使 `H_s=∅`。等价地，固定小高素数碰撞梯提供足够重复增益：

\[
\sum_{j=1}^s\left(|H_{j-1}\cap(b_j\bmod\ell_j)|-1\right)
\ge |H_Q(t)|-|R|.
\tag{6}
\]

证明 `Target LHB-7` 将比证明任意贪心成功更可审查，因为它只涉及固定升序高素数与
每一步最大列残基块。

一旦该定理成立，`low-hole bucket` 约束即可作为真实 `A,b` 行接入 `PDEC-Dual-Cert`。

## 7. LHB-7 的可证明分解

`Target LHB-7` 的优点是它可以脱离完整 CRT 枚举，改写成有限个列残基碰撞不等式。
对任意剩余洞集 `S` 和高素数 `ell`，记

\[
N_{\ell,a}(S)=|\{c\in S:c\equiv a\pmod \ell\}|,\qquad
E_\ell(S)=\sum_{a\bmod\ell}\binom{N_{\ell,a}(S)}2 .
\]

固定梯第 `j` 步的真实增益为

\[
g_j-1=\max_a N_{\ell_j,a}(H_{j-1})-1.
\]

由

\[
N_{\ell,a}(S)(N_{\ell,a}(S)-1)
\le
(\max_b N_{\ell,b}(S)-1)N_{\ell,a}(S)
\]

求和可得完全初等的能量下界

\[
g_j-1\ge {2E_{\ell_j}(H_{j-1})\over |H_{j-1}|}.
\tag{7}
\]

因此 `LHB-7` 可由以下更窄的碰撞能量目标推出：

\[
\sum_j {2E_{\ell_j}(H_{j-1})\over |H_{j-1}|}
\ge |H_Q(t)|-|R|.
\tag{8}
\]

这里的每个对象只依赖 `Q=2310` 的低洞列集合在固定模数
`13,17,19,23,...` 下的残基计数；不再需要枚举高层 CRT 变量。

审计还显示 `P=53,59` 的固定梯失败均为“一洞未补完”，而 `P>=61` 的样本全部成功。
这说明转折点的真实障碍不是大规模容量不足，而是早期 `13,17,19,23` 残基碰撞
刚好少一个重复增益。下一步最小证明任务应集中在两项：

1. 对任意低相位 `t`，给出 `|H_Q(t)|` 的显式上界；
2. 对固定递推残集 `H_j`，证明前若干小高素数的碰撞能量下界足以补足
   `|H_Q(t)|-|R|`。

若这两项闭合，则 `P>=61` 的 low-hole bucket 不再需要动态贪心或完整 CRT 枚举。

## 8. 鸽巢尾段判据

上一节仍使用低洞集的实际残基碰撞。还可以再剥离一层：对任意有限集合 `S`，
在模 `ell` 的 `ell` 个残基类中必有一类至少包含 `ceil(|S|/ell)` 个元素。因此固定梯残量
总被以下纯数值递推控制：

\[
U_0=H_{\max}(P),\qquad
U_j=U_{j-1}-\left\lceil {U_{j-1}\over \ell_j}\right\rceil ,
\tag{9}
\]

其中 `H_max(P)` 是长度 `P-1` 的任意 `Q=2310` 连续残基段内最多的 `Q`-互素残基数，
`\ell_j` 是 `13,17,19,23,...` 中小于 `P` 的高素数。

**Lemma LHB-8（鸽巢尾段充分条件）。**
若递推 (9) 在用完所有 `\ell_j<P` 前达到 `0`，则 `Target LHB-7` 对该 `P` 成立。

**证明。**
设第 `j-1` 步剩余洞集为 `S`，`|S|<=U_{j-1}`。模 `\ell_j` 的最大残基块至少有
`ceil(|S|/\ell_j)` 个洞；固定梯删除最大块，故

\[
|S'|\le |S|-\left\lceil {|S|\over \ell_j}\right\rceil
\le U_{j-1}-\left\lceil {U_{j-1}\over \ell_j}\right\rceil
=U_j .
\]

归纳得实际剩余洞数不超过 `U_j`。若某步 `U_j=0`，实际洞集为空。

审计 `prime-matrix-bpn-lhb-pigeonhole-tail-audit.md` 使用 `Q=2310` 周期前缀和精确计算
`H_max(P)`，并检查递推 (9)。在 `P<=100000` 的扫描中，鸽巢判据唯一失败窄带为

```text
P = 61,67,71,73,79,83,89,97,101,103。
```

从 `P=107` 到 `100000` 全部由 Lemma LHB-8 的纯鸽巢递推闭合。严格全局化还需
一个显式素数计数/Mertens 乘积界，证明递推 (9) 在 `P>=107` 不再反弹；而
`61<=P<=103` 的有限窄带则应回到第 7 节的真实碰撞能量下界。

窄带对照表如下：

| P | `Hmax(P)` | high # | 鸽巢残量 | 固定梯失败数 | 固定梯最小余量 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 61 | 15 | 12 | 2 | 0 | 0 |
| 67 | 16 | 13 | 2 | 0 | 0 |
| 71 | 17 | 14 | 2 | 0 | 0 |
| 73 | 18 | 15 | 2 | 0 | 1 |
| 79 | 19 | 16 | 2 | 0 | 1 |
| 83 | 20 | 17 | 1 | 0 | 2 |
| 89 | 21 | 18 | 1 | 0 | 2 |
| 97 | 23 | 19 | 2 | 0 | 2 |
| 101 | 24 | 20 | 1 | 0 | 2 |
| 103 | 25 | 21 | 1 | 0 | 3 |

这张表说明：尾段硬点已经被压成两类完全明确的审稿义务。其一是把鸽巢递推的
`P>=107` 数值稳定性升级为显式解析不等式；其二是在十个窄带素数上给出有限残基
碰撞证书，补足鸽巢法最多 `2` 个洞的缺口。

## 9. `P/5` 分割的解析接口

为了避免直接证明完整递推的单调性，可使用更适合显式估计的二段式判据。令

\[
y=\left\lfloor {P\over 5}\right\rfloor .
\]

先只用 `13<=ell<=y` 的高素数执行鸽巢递推，得到残量 `V(P)`；再记

\[
R(P)=|\{\ell:\ y<\ell<P,\ \ell\ {\rm prime},\ \ell\nmid 2310\}|.
\]

**Lemma LHB-9（`P/5` 分割充分条件）。**
若

\[
V(P)\le R(P),
\tag{10}
\]

则 `Target LHB-7` 对该 `P` 成立。

**证明。**
前半段递推后还剩至多 `V(P)` 个洞。后半段每个高素数 `ell>y` 至少有一个残基类
命中当前非空洞集，因此每使用一个后半段高素数，剩余洞数至少下降 `1`。若后半段
高素数个数 `R(P)` 不小于 `V(P)`，则全部洞被删除。

审计中 `P/5` 分割判据在 `P<=100000` 的 `P>=107` 尾段无失败，最小余量为 `0`；
失败仍只发生在

```text
P = 61,67,71,73,79,83,89,97,101,103。
```

若把前半段递推进一步放宽为连续乘积上界，则低尾段会损失取整收益。审计显示该连续
乘积上界最后失败于 `P=229`，从 `P=233` 起在 `P<=100000` 扫描中无失败。因此
`P>=233` 的全局化可集中证明单个显式不等式：

\[
H_{\max}(P)
\prod_{13\le \ell\le P/5}\left(1-{1\over \ell}\right)
\le
\pi(P-1)-\pi(P/5),
\tag{11}
\]

其中左侧是 `V(P)` 的连续上界，右侧是 `R(P)`。用 `Q=2310` 的精确周期前缀表给
`H_{\max}(P)`，再配合标准显式 Mertens 乘积上界和素数计数区间下界，即可把
`P>=233` 尾段证明转化为常数核查。

于是 LHB-7 的剩余范围被分成三段：

```text
61<=P<=103：真实碰撞能量窄带；
107<=P<=229：精确 P/5 分割递推有限证书；
P>=233：连续乘积 + 显式 prime-count/Mertens 常数。
```

这比直接声称 (11) 覆盖 `P>=107` 更精确；小尾段必须保留取整增益。

## 10. 显式常数包与三段尾段闭合

`prime-matrix-bpn-lhb-explicit-tail-constant-audit.md` 对 (11) 做了保守常数核查。先由
`Q=2310` 的周期前缀表得到精确上偏差：

\[
H_{\max}(P)\le {16\over 77}(P-1)+5.
\tag{12}
\]

其中最大上偏差出现在长度 `227`，实际为 `52-(16/77)227=4.831168...`。

若接受以下标准显式输入：

```text
Mertens upper:
prod_{p<=x}(1-1/p) <= e^{-gamma}(1+0.03)/log x；

prime counting:
pi(x) >= x/log x，
pi(x) <= 1.25506 x/log x。
```

这些输入可由 Rosser--Schoenfeld 1962 给出：Corollary 1 的 `(3.5),(3.6)` 给出
上述 `pi` 上下界，Theorem 7 的 `(3.26)` 给出
`prod_{p<=x}(1-1/p)<e^{-gamma}(1+1/(2log^2 x))/log x`。对本文 `P>=13208`
的尾段，`floor(P/5)>=2641`，故 `1+1/(2log^2 floor(P/5))<1.009<1.03`，
Mertens 乘积界可安全放宽为上表的 `1.03`。引用接口与适用范围已登记在
`external-theorem-index.md`。

则高素数乘积有

\[
\prod_{13\le\ell\le y}\left(1-{1\over \ell}\right)
\le {77\over16}{e^{-\gamma}(1.03)\over \log y}.
\tag{13}
\]

把 (12)、(13) 与素数计数上下界代入 (11)，审计得到保守解析余量从

```text
P >= 13208
```

起为正；样本中 `P=13208` 的余量约 `0.00043556`。因此尾段可分成：

```text
107<=P<=229：精确 P/5 分割递推有限证书；
233<=P<=13207：精确连续乘积有限证书；
P>=13208：显式 Mertens/prime-count 常数包。
```

该三段路线避免两个错误：一是不把连续乘积误用于 `107<=P<=229`，二是不把
大范围数值扫描当成无限证明。真正需要外部引用的只剩标准显式 Mertens 与素数计数
常数；若采用更尖锐的 Dusart/Rosser--Schoenfeld 常数，`13208` 还可继续下降。

## 11. 尾段有限证书

`prime-matrix-bpn-lhb-tail-finite-certificate.md` 已生成两段有限证书。

第一段是 `107<=P<=229` 的精确 `P/5` 分割递推表：共有 `23` 个素数行，
全部满足

\[
V(P)\le R(P),
\]

最小余量为 `0`。这说明该段虽然不能用连续乘积粗上界替代，但精确取整递推已经足够。

第二段是 `233<=P<=13207` 的连续乘积有限证书：共有 `1520` 个素数行。验收不使用
浮点数，而是对

\[
H_{\max}(P){A_y\over B_y}\le R(P),
\qquad
{A_y\over B_y}=\prod_{13\le\ell\le y}\left(1-{1\over\ell}\right)
\]

执行整数交叉乘法：

\[
R(P)B_y-H_{\max}(P)A_y>0.
\tag{14}
\]

全部 `1520` 行通过，浮点余量最小出现在 `P=233`，约为 `0.5347204`。
因此在接入窄带与低范围证书前，待合并项压缩为：

```text
P>=13208：引用显式 Mertens/prime-count 常数；
61<=P<=103：碰撞能量窄带；
P<61：低范围三类有限证书。
```

## 12. 窄带碰撞能量证书

`prime-matrix-bpn-lhb-narrow-band-collision-certificate.md` 已闭合十个窄带素数

```text
P=61,67,71,73,79,83,89,97,101,103。
```

对每个低相位 `t mod 2310`，证书按固定升序高素数梯执行最大残基块删除，并记录

\[
\operatorname{surplus}(t)
=\bigl(|H_Q(t)|-s(t)\bigr)
-\max(0,|H_Q(t)|-|R|).
\tag{15}
\]

这里 `|H_Q(t)|-s(t)` 是实际重复碰撞增益，后一项是覆盖所需的最小重复增益。
证书结果为：

| P | phases | max required gain | min surplus | min margin |
| ---: | ---: | ---: | ---: | ---: |
| 61 | 2310 | 3 | 0 | 0 |
| 67 | 2310 | 3 | 0 | 0 |
| 71 | 2310 | 3 | 0 | 0 |
| 73 | 2310 | 3 | 1 | 1 |
| 79 | 2310 | 3 | 1 | 1 |
| 83 | 2310 | 3 | 2 | 2 |
| 89 | 2310 | 3 | 2 | 2 |
| 97 | 2310 | 4 | 2 | 2 |
| 101 | 2310 | 4 | 2 | 2 |
| 103 | 2310 | 4 | 3 | 3 |

全部 `23100` 个低相位通过，且每个 `P` 的全相位摘要哈希记录在 JSON 中。
因此 `61<=P<=103` 窄带已经不再是未证缺口；它是有限碰撞能量证书义务。

## 13. 低范围最终证书

`prime-matrix-bpn-lhb-low-range-final-certificate.md` 已完成 `13<=P<61` 的最终聚合证书。
证书覆盖

```text
P=13,17,19,23,29,31,37,41,43,47,53,59。
```

总计 `15414` 个 zero bucket 全部闭合，其中：

```text
整洞集亏损：15282；
桥洞临界：108；
精确 DP 临界：24。
```

唯一需要修正旧表述的是 `P=41`：它有 `24` 个 `Delta(H)=0` 且无桥洞的临界相位。
这些相位已由完整残基类 set-cover DP 有限证书闭合，因此不能再写成“低范围全部为
整洞集亏损或桥洞交叉”，应写成“三类证书闭合”。

结合低范围、窄带、两段尾段有限证书后，当前 `low-hole bucket` 主线剩余压缩为：

```text
P>=13208：显式 Mertens/prime-count 常数引用核验。
```
