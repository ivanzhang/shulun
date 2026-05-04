# AlphaTail `C13` 的 `lift>=2` 结构空性充分条件

**状态：** `c13_liftge2_structural_criterion_sample_closed_global_open`

本文把 `lift>=2` 的样本签名空性进一步压成三个直接可检查的窗口几何条件。

## 1. 结构判据

设低大素块最小素数为

\[
L=\min L_{\rm low},
\]

窗口参数为 `(B,r,m)`，并记 `R=|r|`。若满足

\[
B<2L,
\tag{LGC-1}
\]

\[
(m-1)R<L,
\tag{LGC-2}
\]

\[
6\mid R,
\tag{LGC-3}
\]

则所有 `lift>=2` 候选均被模 `6` 排除。

## 2. 证明

任意 `lift>=2` 候选满足

\[
q=a+t\ell,\qquad t\ge2,\qquad 0\le a<\ell,\qquad \ell\ge L.
\tag{LGC-4}
\]

### 2.1 排除 `u>=2`

若乘数 `u>=2`，则由几何区间上界有

\[
q\le {2B\over u}\le B.
\tag{LGC-5}
\]

但 `t>=2` 给出

\[
q=a+t\ell\ge2\ell\ge2L.
\tag{LGC-6}
\]

由 `(LGC-1)` 得 `B<2L`，与 `(LGC-5)`、`(LGC-6)` 矛盾。所以必有

\[
u=1.
\tag{LGC-7}
\]

### 2.2 限制 `t`

当 `u=1` 时，仍有 `q<=2B`。由 `(LGC-1)` 得

\[
q<4L\le4\ell.
\tag{LGC-8}
\]

因此 `t=floor(q/ell)` 只能满足

\[
t\in\{2,3\}.
\tag{LGC-9}
\]

### 2.3 限制 `h`

由

\[
a=n+h\ell,\qquad n=-(j-j_1)r,
\tag{LGC-10}
\]

以及 `(LGC-2)` 得

\[
|n|\le(m-1)R<L\le\ell.
\tag{LGC-11}
\]

由于 `0<=a<ell`，若 `n>=0` 则只能 `h=0`；若 `n<0` 则只能 `h=1`。故

\[
h\in\{0,1\}.
\tag{LGC-12}
\]

### 2.4 模 6 排除

由 `(LGC-3)` 得 `n==0 mod 6`。再由 `u=1`，

\[
q=(t+h)\ell+n\equiv(t+h)\ell\pmod6.
\tag{LGC-13}
\]

其中 `t+h in {2,3,4}`，而尾素 `ell>3` 满足 `ell mod 6 in {1,5}`。于是

\[
q\bmod6\in\{2,3,4\}.
\tag{LGC-14}
\]

所以 `q` 不可能是尾素，`lift>=2` 真实删除数为 `0`。□

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_structural_criterion.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_structural_criterion.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --format table
```

输出摘要：

```text
highP-total:
  candidates=1368；
  good=0；
  criterion=True；
  all_bad=True；
  min_block_margin=822；
  min_n_margin=4363。
```

逐层：

```text
p=5003,m=4:
  L=4507；
  B/L=1.817617；
  n_span/L=0.023963；
  criterion=True。

p=5003,m=5:
  L=4507；
  B/L=1.817617；
  n_span/L=0.031950；
  criterion=True。

p=10007,m=4:
  L=9007；
  B/L=1.819030；
  n_span/L=0.299767；
  criterion=True。

p=10007,m=5:
  L=9007；
  B/L=1.819030；
  n_span/L=0.399689；
  criterion=True。
```

## 4. 全局接口

全局化 `lift>=2 Mod6Void` 不再需要逐候选枚举；只需对完整目标窗口族证明：

```text
LGC-A: B < 2L_min；
LGC-B: (m-1)|r| < L_min；
LGC-C: 6 divides |r|。
```

若三者成立，则 `D_ge2=0` 无条件成立。

## 5. 审稿边界

已完成：

```text
给出 lift>=2 空性的三条结构充分条件；
逐行证明三条条件推出 u=1、t in {2,3}、h in {0,1}；
当前压力样本全部满足，且最小余量明确。
```

仍未完成：

```text
证明完整目标窗口族均满足 LGC-A/B/C；
若某窗口不满足，则给出有限证书或 PDEC/SAE 出口；
把该结构判据接回全局 LowSievePreservation。
```
