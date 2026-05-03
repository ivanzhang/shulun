# H3 尾标签精确补洞的刚性硬核

**状态：** `tail_filler_local_rigidity_proved_global_exclusion_open`

本文继续直接攻击当前唯一闭合目标中的真正硬障碍：

```text
Tail labels with y<P^-(n)<=p cannot form an exact full-row filler
without producing ColumnCRT/endpoint/cofactor contradiction.
```

不转换命题；本文只把“尾标签精确补洞”内部的相邻差值、互质、复用间距和二步刚性全部写成可审查
方程，明确哪些部分已证，哪一条仍是全局排斥核心。

## 1. 六轮候选链

令 `A_s={a_1<...<a_N}` 为固定 `q` 行窗口中的 H3 六轮候选。相邻差值交替为

\[
a_{j+1}-a_j\in\{2,4\},
\tag{TFR-1}
\]

并且二步差值恒为

\[
a_{j+2}-a_j=6.
\tag{TFR-2}
\]

尾标签精确补洞假设是：每个被尾部解释的候选都可唯一写成

\[
a_j=\ell_j m_j,
\qquad
y<\ell_j=P^-(a_j)\le p,
\qquad
P^-(m_j)\ge \ell_j.
\tag{TFR-3}
\]

若整行 H3 被尾部补满，则 `(TFR-3)` 对所有 `j` 成立；若小骨架已剥离，则它对剩余连续或准连续
洞链成立。

## 2. 相邻互质刚性

若 `a_j` 与 `a_{j+1}` 均满足 `(TFR-3)`，则

\[
\gcd(a_j,a_{j+1})=1.
\tag{TFR-4}
\]

原因是二者为奇数，且公因子必须整除 `2` 或 `4`。

因此四个因子块

\[
\{\ell_j\}\cup \mathrm{PrimeFactors}(m_j),
\qquad
\{\ell_{j+1}\}\cup \mathrm{PrimeFactors}(m_{j+1})
\]

完全不相交。特别地：

\[
\ell_j\ne \ell_{j+1},
\quad
\gcd(m_j,m_{j+1})=1,
\quad
\gcd(\ell_j,m_{j+1})=\gcd(\ell_{j+1},m_j)=1.
\tag{TFR-5}
\]

这证明了用户指出的精细刚性：相邻合数不仅通常由不同因子解释，而是必须由完全不同的大因子族解释。

## 3. 二步互质刚性

若 `a_j` 与 `a_{j+2}` 均满足 `(TFR-3)`，则

\[
\gcd(a_j,a_{j+2})\mid 6.
\]

但二者均避开 `2,3`，故

\[
\gcd(a_j,a_{j+2})=1.
\tag{TFR-6}
\]

因此相距两步的尾补洞点也不能共享任何大素因子。换言之，一个尾标签 `ell>y>=5` 不可能在
`a_j,a_{j+1},a_{j+2}` 三连局部中复用。

## 4. 复用间距刚性

若同一尾标签 `ell>y` 同时命中 `a_i` 与 `a_j`，`i<j`，则

\[
\ell\mid a_j-a_i.
\]

六轮候选每步增量至多 `4`，故

\[
a_j-a_i\le 4(j-i).
\]

于是

\[
j-i\ge {\ell\over4}>{y\over4}.
\tag{TFR-7}
\]

所以任何长度 `floor(y/4)+1` 的连续 H3 候选块中，所有尾标签互不相同。

这比单纯容量上界更强：它是沿候选链方向的局部排斥，不依赖统计平均。

## 5. 相邻差值方程

相邻尾补洞点必须满足

\[
\ell_{j+1}m_{j+1}-\ell_jm_j=\delta_j,
\qquad
\delta_j\in\{2,4\}.
\tag{TFR-8}
\]

由 `(TFR-5)`，`ell_j,ell_{j+1},m_j,m_{j+1}` 两侧因子族互素。因此 `(TFR-8)` 是一个真正的
大因子短差值方程：两个 `y`-rough 合数相差 `2` 或 `4`。

模 `ell_j` 与 `ell_{j+1}` 分别给出

\[
\ell_{j+1}m_{j+1}\equiv \delta_j\pmod{\ell_j},
\qquad
\ell_jm_j\equiv -\delta_j\pmod{\ell_{j+1}}.
\tag{TFR-9}
\]

每一条相邻边都强制两个互补商落入由另一尾标签决定的非零同余类。这是尾补洞链的基本相位锁。

## 6. 局部块的因子消耗下界

取任意连续候选块 `B={a_r,...,a_{r+K-1}}`，若其直径

\[
a_{r+K-1}-a_r<y,
\tag{TFR-10}
\]

则任意两个不同候选不能共享任何尾素因子。因为共享因子 `rho>y` 将整除二者差值，而差值绝对值
小于 `y`。

因此若整块由尾标签补洞，则该块消耗至少 `2K` 个带重不同的大素因子：

\[
\omega\left(\prod_{a\in B}a\right)\ge 2K
\quad\text{with all counted primes }>y.
\tag{TFR-11}
\]

这是局部“因子预算”刚性。它本身尚不矛盾，因为 `q^2` 壳层可容纳许多大素因子；但它排除了
尾标签在短局部内通过复用来廉价补洞。

## 7. 三连局部的强制形态

任意三个连续候选若全由尾部补洞，则存在两条短差值方程

\[
\ell_{j+1}m_{j+1}-\ell_jm_j=\delta_j,
\]

\[
\ell_{j+2}m_{j+2}-\ell_{j+1}m_{j+1}=\delta_{j+1},
\]

并且三组因子族两两不交。消去中项得

\[
\ell_{j+2}m_{j+2}-\ell_jm_j=6.
\tag{TFR-12}
\]

所以三连补洞等价于两个互素 `y`-rough 合数相差 `6`，中间再插入一个与二者均互素的
`y`-rough 合数，且两个间隔分别为 `2,4` 或 `4,2`。

这就是尾补洞的最小非平凡刚性单元。任何整行精确补洞都由这些三连单元重叠拼成。

## 8. 为什么这仍未直接矛盾

上述局部刚性非常强，但还不足以单独推出全局矛盾。原因是：

```text
存在 y-rough 合数短差值族；
线性筛在 u=2 不能区分素数与双粗半素数；
局部互质不禁止远距离复用。
```

因此最后需要的不是再证明相邻互质，而是全局化：

```text
这些局部短差值方程能否在长度约 q/3 的六轮链上连续拼接，
同时保持所有同余相位、CRT 周期均衡、端点镜像和列位移兼容？
```

## 9. 当前真正硬命题

当前唯一剩余硬障碍可压成以下不再含糊的命题：

```text
Tail-Filler Global Incompatibility.
Let A_s be an H3 candidate row.  Suppose every a_j in a long subchain
is represented as a_j=ell_j m_j with y<ell_j<=p and P^-(m_j)>=ell_j.
Then the edge congruences (TFR-9), spacing rule (TFR-7), and two-step
equation (TFR-12) force one of:
  ColumnCRT non-zero displacement concentration;
  endpoint phase persistence;
  cofactor short-difference overcapacity.
```

这仍是原 `Square-root Defect Exclusion` 的内部硬核：它直接排斥尾标签/双粗点作为整行精确补洞器。

## 10. 本次实际推进

本次硬攻严格完成了以下内容：

1. 相邻候选必须由完全不同的大因子族解释；
2. 二步候选也不能共享大因子；
3. 同一尾标签复用间距至少为 `y/4`；
4. 连续短块尾补洞至少消耗 `2K` 个不同大因子；
5. 三连补洞的最小方程是两个互素 `y`-rough 合数相差 `6`，中间插入第三个互素 `y`-rough 合数。

未完成且不能省略的是第 9 节的全局不相容性证明。
