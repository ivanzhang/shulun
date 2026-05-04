# 共振三点链的奇偶闸门

**状态：** `alpha_tail_resonant_chain_parity_gate_reduction_open`

三点链数量本身仍是无符号对象。跨点锚点相关要真正形成反例压力，还必须在三点链上产生同向符号。
本文把共振链的符号部分压成三组二点 Möbius 相关与低模 Parity-PDEC。

## 1. 三点支撑

对

\[
d,\quad d+r,\quad d+2r
\tag{RCG-1}
\]

都 squarefree 的链，记素因子支撑为

\[
S_0(d),\quad S_1(d),\quad S_2(d).
\tag{RCG-2}
\]

三组 Möbius 相关为

\[
K_{01}=\sum_{d\in T_r}\mu(d)\mu(d+r),
\quad
K_{12}=\sum_{d\in T_r}\mu(d+r)\mu(d+2r),
\quad
K_{02}=\sum_{d\in T_r}\mu(d)\mu(d+2r).
\tag{RCG-3}
\]

审计中的 `corr01,corr12,corr02` 正是这三项。

## 2. 对称差公式

在三点链上，

\[
\mu(d+ir)\mu(d+jr)=
(-1)^{|S_i(d)\triangle S_j(d)|}.
\tag{RCG-4}
\]

因此任意一组相关偏大，都等价于对应两点支撑的对称差奇偶偏置。

## 3. 共振符号压力二分

若共振分支需要有符号贡献达到 `Xi`，则至少发生一项：

\[
|K_{01}|\ge c\Xi,\qquad
|K_{12}|\ge c\Xi,\qquad
|K_{02}|\ge c\Xi,
\tag{RCG-5}
\]

或无符号三点链包络已经超预算。这里常数 `c` 由具体锚点权分解给出；若权分解未指定，可把
`(RCG-5)` 作为正式反例链抽取后的验收项。

## 4. 局部状态

对素数 `q`：

1. 若 `q|r`，则 `q` 对三点共同锁定，不进入任意对称差；
2. 若 `q\nmid r` 且 `q>2`，则 `q` 只能整除三点中的一个，必进入两组对称差；
3. 若 `q=2`，按 `r` 奇偶退化为两类或一类。

这说明三点链的奇偶偏置比二点情形更受约束：未锁素数的单点出现会同时影响两条边的 parity。

## 5. 出口

每个 `K_{ij}` 都可按前文 `Parity-PDEC bridge` 处理：

```text
K_ij large
=> finite low-mod Parity-PDEC
   or high-tail parity anchor
   or SAE.
```

三点结构额外提供一致性约束：同一个未锁素数不能独立调节三条边的奇偶；这应进入后续
`ThreeEdge-Parity` 账本。

## 6. 审稿边界

已证明：

```text
resonant signed pressure
=> one of K01,K12,K02 is large,
or unweighted three-point chain envelope fails.
```

尚未证明：

```text
三组 K_ij 都不能达到正式反例所需尺度。
```

下一步最小硬点是把三组 `K_ij` 的低模 parity 测试函数合并，利用同一个未锁素数同时影响两条边的
约束，形成更强的 `ThreeEdge-Parity-PDEC`。
