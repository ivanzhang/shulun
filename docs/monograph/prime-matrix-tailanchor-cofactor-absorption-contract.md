# TailAnchor/CofactorAnchor 吸收合同：尾锚不是独立终端

**状态：** `tailanchor_cofactor_absorbed_to_pdec_sae_columncrt_not_closed`

本文承接 `prime-matrix-multiplicity-stitching-absorption-contract.md`。当前终端列表中还保留
`TailAnchor/CofactorAnchor`。本文把它们并回统一出口：

```text
persistent anchor => PDEC / ColumnCRT；
sparse anchor     => SAE；
anchor sum small  => capacity contradiction / CleanKLS。
```

因此尾锚和互补因子锚不是独立终端。

## 1. 互补因子反演对象

远尾命中已经由 `prime-matrix-pcolumn-nearcutoff-fartail-cofactor.md` 精确反演为：

\[
Py-d=qm,
\qquad
\left\lceil {Py-P+1\over m}\right\rceil
\le q\le
\left\lfloor {Py-1\over m}\right\rfloor,
\tag{TCA-1}
\]

其中：

```text
q 为高素数；
m 为 Y-rough 互补因子；
qm 落入同一行短窗；
d=Py-qm 为列位移。
```

所以远尾异常有三个签名：

```text
m-signature       : m/y dyadic band, m mod Q；
q-signature       : q short window, q mod Q；
column signature  : d mod Q 或 d mod P。
```

这已经是有限签名群上的对象。

## 2. Anchor 三分

设某一行的自归一化余量需要尾部支付 `R(P,y)`。把远尾正超额按互补因子锚分解：

```text
E_tail^+ = sum_m E_m^+。
```

对阈值 `eta` 作三分：

### 2.1 AnchorSmall

若

```text
sum_m E_m^+ < R(P,y),
```

则由 SN-2 带级正部判据，零行不可能。

### 2.2 AnchorSparse

若正超额只由有限少数 `m` 或短 q 窗承担，且不沿最小反例族持久，则进入：

```text
SAE-cofactor / SAE-anchor。
```

这与 `BPN` 的 `SAE-anchor` 完全同型：孤立锚必须有 survivor/lift/higher-defect，否则不能抹掉整行。

### 2.3 AnchorPersistent

若某个锚签名在无限最小反例族或同一坏窗族中持续承担固定比例正超额，则有限签名鸽巢给出：

```text
m mod Q 持久        => cofactor PDEC；
q mod Q 持久        => low-mod PDEC；
d mod Q/P 持久      => ColumnCRT；
m/q 短窗持久        => refined PDEC 或 SAE。
```

因此持久锚就是 generalized PDEC/ColumnCRT。

## 3. 尾锚持续化与 PDEC

`prime-matrix-bpn-tailanchor-persistence-dichotomy.md` 已证明：

```text
Tail-anchor concentration
=> SAE-anchor
   or Persistent Tail-anchor defect
=> SAE
   or Directed CRTDefect。
```

本文把 `Directed CRTDefect` 接入统一缺陷向量引理：令

```text
F(a)=1_{a=rho mod Q}-1/Q。
```

若饱和尾锚集合在 `rho` 上持久过密，则

\[
\sum_{a\in A_\theta}F(a)>0
\]

并由非零 Fourier 展开进入 generalized `PDEC-Cert`。若该相位同时固定列位移，则进入
`ColumnCRT`。

## 4. 反演短区间的无名失败吸收

若 `TCA-1` 中某些 `m` 的短素数区间持续超额，但低模签名不持久，则只有两种可能：

```text
1. 超额局限于有限短窗
   => SAE；

2. 超额在许多 m 上分散且无低模/列同步
   => high-dimensional DLS / CleanKLS。
```

第二项不是尾锚出口；它回到 `CleanKLS/DLS`，因为没有任何固定锚签名能承担正超额。

## 5. 形式化结论

**TailAnchor-Cofactor Absorption.**
任意远尾互补因子或尾锚出口，有限步内必进入：

```text
capacity contradiction；
SAE-anchor / SAE-cofactor；
cofactor PDEC；
low-mod PDEC；
ColumnCRT；
CleanKLS/DLS。
```

因此 `TailAnchor/CofactorAnchor` 从终端出口列表中删除。

## 6. 当前闭合边界

本文完成：

```text
尾锚/互补因子锚不是独立终端；
持久锚进入 PDEC/ColumnCRT；
稀疏锚进入 SAE；
无锚分散进入 CleanKLS/DLS。
```

本文未完成：

```text
cofactor PDEC 的 U_CRT<L_PDEC；
ColumnCRT 排斥；
SAE-anchor 排斥；
CleanKLS/DLS 全局证明。
```

最终终端列表进一步更新为：

```text
explicit/profinite/weighted/primitive/cofactor PDEC；
ColumnCRT；
SAE；
CleanKLS/DLS。
```

这仍是结构归约，不是最终无条件行命题证明。

## 7. ColumnCRT 位移 PDEC 吸收

新增 `prime-matrix-columncrt-displacement-pdec-absorption.md` 后，`ColumnCRT` 也并回 PDEC/SAE。
列位移签名为

```text
sigma_col(x)=(ell,d_c mod ell),  d_c=r_c-H。
```

CD0 已证明零位移余类除小例外外不可能。若某个非零位移余类持久过载，则进入
`displacement PDEC`；若只孤立出现，则进入 `SAE-column`；若所有位移余类都不过载，则对应
`R_{ell,a}(g)<=L_D` 可作为 PDEC 对偶约束行。
