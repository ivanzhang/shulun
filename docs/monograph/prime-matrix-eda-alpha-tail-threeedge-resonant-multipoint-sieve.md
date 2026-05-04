# ThreeEdge 共振四点/五点链筛包络

**状态：** `alpha_tail_threeedge_resonant_multipoint_sieve_reduction_open`

本文处理五射线热门差值账本留下的共振差值。三边尾锚的基集合是三点链 `T_r`，所以
`s=±r` 与 `s=±2r` 会把两个三点链拼成四点链与五点链。这比旧二点阶段的三点共振更稀疏。

## 1. 多点链定义

对 `m>=2` 定义

\[
T_{m,r}=\{d:d,d+r,\ldots,d+(m-1)r\ {\rm all\ pass\ current\ smooth/squarefree\ support}\}.
\tag{MPS-1}
\]

三边尾锚中：

\[
s=\pm r\quad\Longrightarrow\quad T_{4,r},
\tag{MPS-2}
\]

\[
s=\pm2r\quad\Longrightarrow\quad T_{5,r}.
\tag{MPS-3}
\]

精确地，若 `d_1,d_2 in T_{3,r}` 且 `d_1-d_2=r`，则以 `d_2` 为起点的
`d_2,d_2+r,d_2+2r,d_2+3r` 全部通过；`-r` 只改变方向。`±2r` 同理给出五点链。

## 2. 局部禁零类数

对素数 `q`，多点链需要避开

\[
d\equiv -jr\pmod q,\qquad j=0,1,\ldots,m-1.
\tag{MPS-4}
\]

令

\[
b_{m,q}(r)=\#\{-jr\pmod q:0\le j<m\}.
\tag{MPS-5}
\]

则精确有

\[
b_{m,q}(r)=
\begin{cases}
1,&q\mid r,\\
\min(m,q),&q\nmid r.
\end{cases}
\tag{MPS-6}
\]

**证明。**  
若 `q|r`，所有 `-jr` 同余于 `0`。若 `q∤r`，乘以 `r^{-1}` 后集合等价于
`{0,-1,\ldots,-(m-1)} mod q`，其 distinct 个数为 `min(m,q)`。证毕。

因此未锁高素数在四点链中给四禁，在五点链中给五禁；小素数只按 `min(m,q)` 退化。这是新的强筛重度。

## 3. Selberg 上筛接口

令

\[
P(z)=\prod_{y<q\le z}q.
\tag{MPS-7}
\]

对任意 Selberg 上筛权 `lambda_a`，

\[
|T_{m,r}|
\le
\sum_{d\in I_m}
\left(
\sum_{\substack{a|P(z)\\d\bmod a\in\Omega_{m,r}(a)}}\lambda_a
\right)^2,
\tag{MPS-8}
\]

其中 `I_m` 是 `m` 个点同时处在目标块内的 `d` 区间，`\Omega_{m,r}(a)` 由 `(MPS-4)` 经 CRT 生成。
主筛因子为

\[
\mathcal V_{m,r}(z)
\asymp
\prod_{y<q\le z}
\left(1-{b_{m,q}(r)\over q}\right).
\tag{MPS-9}
\]

当 `q∤r` 且 `q>m`，四点链给 `1-4/q`，五点链给 `1-5/q`。这比三点链的 `1-3/q`
多出一层或两层筛压。

## 4. 共振压力二分

若五射线跨点相关的共振部分超过预算，则至少发生一项：

1. **多点链包络失败。**  
   `|T_{4,r}|` 或 `|T_{5,r}|` 超过 `(MPS-8)` 的 Selberg 上筛预算。
2. **奇异因子过大。**  
   `r` 含有过多中高素因子，使大量 `q` 从四禁/五禁退化为一禁，进入 `ColumnCRT/Rankin`。
3. **端点相位缺陷。**  
   多点链集中在固定低模相位，进入 `PDEC`。
4. **孤窗异常。**  
   异常只在单个短窗出现，进入 `SAE`。

## 5. 与五射线账本的衔接

五射线 Rankin 账本已处理

\[
s\notin\{0,\pm r,\pm2r\}.
\tag{MPS-10}
\]

本文处理剩余：

```text
s=0      -> point-load Rankin/Tail;
s=±r     -> four-point chain T_{4,r};
s=±2r    -> five-point chain T_{5,r}.
```

因此三边尾锚跨点分支已经被完全拆成：

```text
nonresonant five-factor Rankin
or point-load Rankin/Tail
or four/five-point Selberg envelope
or PDEC/SAE/ColumnCRT.
```

## 6. 审计样本

审计脚本：

```text
experiments/prime_matrix_alpha_tail_multipoint_chain_audit.py
```

样本：

| p | block | shift | T3 | T4 | T5 | b4 avg | b5 avg |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 362 | 189 | 101 | 3.760000 | 4.680000 |
| 5003 | 8192 | -36 | 1686 | 1209 | 916 | 3.760000 | 4.680000 |
| 10007 | 16384 | -900 | 3720 | 2860 | 2302 | 3.640000 | 4.520000 |

## 7. 审稿边界

已证明：

```text
five-ray resonances s=±r,±2r
=> four-point or five-point smooth/squarefree chain
=> Selberg envelope with b_{m,q}(r)=#{-jr mod q}.
```

尚未证明：

```text
四点/五点 Selberg 包络常数足以压住正式反例所需共振压力；
以及包络失败出口 PDEC/SAE/ColumnCRT 不可能。
```

下一步最小硬点是把 `(MPS-9)` 的显式常数与五射线共振计数预算相乘，形成可核验的不等式；失败时输出
多点链 `PDEC/SAE` 证书。
