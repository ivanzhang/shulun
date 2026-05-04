# AlphaTail 单高素锚点证书

**状态：** `alpha_tail_single_anchor_certificate_reduction_open`

本文把 `Tail-anchor energy route` 的单锚点集中分支物化为具体证书对象：一个高素数 `q`、一个
剩余类 `0` 或 `-r mod q`、以及一个低模符号权重的非零均值。

## 1. 单锚点回顾

高尾锚点为

\[
A_q(r)=
-2
\sum_{\substack{d\in A_r\\ d\equiv0\ {\rm or}\ -r\pmod q}}
W_q(d),
\tag{SAC-1}
\]

其中

\[
W_q(d)=
\Psi_{R,r}(d)\prod_{R<\ell<q}\psi_{\ell,r}(d).
\tag{SAC-2}
\]

`W_q` 只依赖

\[
d\bmod Q_{q,r},\qquad
Q_{q,r}=\prod_{\substack{\ell<q\\ \ell\nmid r}}\ell.
\tag{SAC-3}
\]

## 2. 类贡献二分

写

\[
S_{q,0}=\sum_{\substack{d\in A_r\\ d\equiv0\pmod q}}W_q(d),
\qquad
S_{q,-r}=\sum_{\substack{d\in A_r\\ d\equiv-r\pmod q}}W_q(d).
\tag{SAC-4}
\]

若

\[
|A_q(r)|\ge \Lambda,
\tag{SAC-5}
\]

则由 `(SAC-1)`，

\[
|S_{q,0}+S_{q,-r}|\ge{\Lambda\over2}.
\tag{SAC-6}
\]

因此至少一个类 `c in {0,-r}` 满足

\[
|S_{q,c}|\ge{\Lambda\over4}.
\tag{SAC-7}
\]

这是单锚点集中最小证书。

## 3. 中心化与 PDEC/SAE

令

\[
A_{q,c}(a)=
\#\{d\in A_r:d\equiv c\pmod q,\ d\equiv a\pmod {Q_{q,r}}\}.
\tag{SAC-8}
\]

则

\[
S_{q,c}=\sum_{a\bmod Q_{q,r}} A_{q,c}(a)\,W_q(a).
\tag{SAC-9}
\]

把 `W_q` 减去其完整 residue 系均值，得到零均值测试函数 `W_q^0`。若 `(SAC-7)` 的主量不能由
均值项解释，则存在非零 Fourier/CRT 系数，进入 `PDEC`；若它只在单个窗口出现，则进入 `SAE`。

## 4. 证书字段

一个 `SingleAnchor-Cert` 必须给出：

```text
p, B, r, R;
q;
c in {0,-r mod q};
Q_{q,r};
phase counts A_{q,c}(a);
zero-mean weight W_q^0(a);
lower bound |sum A W_q^0|;
PDEC or SAE route key.
```

这与 `h4-pdec-certificate-template.md` 的字段兼容：`Q=Q_{q,r}`，`S` 为该锚点类中的坏点，
`F=W_q^0`。

## 5. 审稿边界

审计脚本：

```text
experiments/prime_matrix_alpha_tail_single_anchor_audit.py
```

样本：

| p | block | shift | R | q | anchor | left sum | right sum | left count | right count |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 31 | 37 | 42 | -5 | -16 | 33 | 34 |
| 5003 | 8192 | -36 | 31 | 61 | 70 | -14 | -21 | 52 | 53 |
| 10007 | 16384 | -900 | 31 | 73 | 130 | -35 | -30 | 93 | 84 |

样本说明：单个锚点最大贡献不大于总高尾贡献的主要部分，且左右类都参与。因此全局硬点更可能是
分散锚点能量，而不是单个锚点完全集中；但若正式反例链抽出单锚点集中，本文给出可提交证书格式。

## 6. 审稿边界

已证明：

```text
single high-prime anchor concentration
=> one residue class carries a centered low-mod signed mass certificate,
unless the class mean term explains it.
```

尚未证明：

```text
该证书不可能。
```

下一步最小硬点是对正式反例抽出的 `SingleAnchor-Cert` 提交 PDEC 上界，或证明其为孤立 SAE 并
由小窗口账本排斥。
