# 共振差值 `s=±r` 的三点光滑链

**状态：** `alpha_tail_resonant_difference_chain_reduction_open`

热门差值审计显示，跨点锚点相关的最大压力来自 `s=±r`。这不是 Rankin 失败，而是一个特殊共振：
若 `d_1-d_2=r`，则两个 `ShiftSmooth(r)` 点拼成三点链。

## 1. 共振差值的几何含义

令

\[
A_r=\{d:d,d+r\ {\rm both\ pass\ the\ current\ smooth/squarefree\ support}\}.
\tag{RDC-1}
\]

若 `d_1,d_2 in A_r` 且

\[
d_1-d_2=r,
\tag{RDC-2}
\]

则 `d_1=d_2+r`。由 `d_2 in A_r` 得 `d_2,d_2+r` 通过；由 `d_1 in A_r` 得
`d_1,d_1+r` 通过。因此

\[
d_2,\quad d_2+r,\quad d_2+2r
\tag{RDC-3}
\]

全部通过。`s=-r` 同理给出反向三点链。

## 2. 共振分支定义

定义三点链集合

\[
T_r=
\{d:d,\ d+r,\ d+2r\ {\rm all\ pass\ the\ current\ support}\}.
\tag{RDC-4}
\]

则

\[
\#\{(d_1,d_2)\in A_r^2:d_1-d_2=r\}=|T_r|,
\tag{RDC-5}
\]

\[
\#\{(d_1,d_2)\in A_r^2:d_1-d_2=-r\}=|T_{-r}|.
\tag{RDC-6}
\]

所以共振跨点相关不是普通差值复用；它等价于三点光滑链过多。

## 3. 三点链的筛重度

对素数 `q`，三点

\[
d,\quad d+r,\quad d+2r
\tag{RDC-7}
\]

的零类数为：

```text
1 个零类，若 q|r；
3 个零类，若 q∤r 且 q≠2；
至多 2 个零类，若 q=2 且 r 为奇数。
```

在本文主情形 `r` 来自偶性/小因子锁后，`q|r` 的素数继续给奇异因子增益；未锁素数则从二点筛的
二禁升级为三禁。因此三点链应比 `ShiftSmooth(r)` 更稀疏。

## 4. 出口

若共振分支过大，则只能发生：

1. **三点链奇异因子过大。**  
   `r` 含有太多小/中素因子，使大量局部三禁降为一禁，进入 `ColumnCRT`；
2. **三点链端点/PDEC。**  
   三点链集中在固定低模相位，进入 `PDEC`；
3. **孤立 SAE。**  
   共振只在单窗出现，进入 `SAE`。

## 5. 当前最小硬点

非共振差值已由 Rankin 账本强力压制；真正剩余是：

```text
Resonant three-point smooth chain T_r.
```

下一步应对 `T_r` 写出三禁/一禁 Selberg 包络，并比较它与正式反例所需共振压力。
