# AlphaTail `C13` 低筛 AP 删除的 Brun 常数余量

**状态：** `c13_lowsieve_ap_brun_margin_conditional_ready`

本文接续 AP 删除证书。上一层给出精确证书 `U_AP<=G_geom-R`。本文把精确 `U_AP`
升级为可全局化的 AP-Brun 常数判据。

## 1. AP-Brun 充分条件

对每个删除类

\[
q\in J,\qquad q\equiv a\pmod \ell,\qquad q,q+g\in P_T,
\tag{ABM-1}
\]

设

\[
N_{\ell,a,g}(J)
=
\#\{q\in J:q\equiv a\pmod\ell,\ q,q+g\in P_T\}.
\tag{ABM-2}
\]

若存在常数 `C_AP` 使目标族中所有删除类满足

\[
N_{\ell,a,g}(J)
\le
C_{\rm AP}\,
\mathfrak S(g)\,
{|J\cap(a\bmod\ell)|\over \log^2 J_-},
\tag{ABM-3}
\]

则

\[
U_{\rm AP}
\le
C_{\rm AP}\,\mathcal B_{\rm AP},
\tag{ABM-4}
\]

其中

\[
\mathcal B_{\rm AP}:=
\sum_{\rm deletion\ classes}
\mathfrak S(g)\,
{|J\cap(a\bmod\ell)|\over \log^2 J_-}.
\tag{ABM-5}
\]

因此低筛保存的充分条件为

\[
C_{\rm AP}\mathcal B_{\rm AP}
\le
G^{\rm geom}-R.
\tag{ABM-6}
\]

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_ap_brun_margin.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_ap_brun_margin.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --ap-c 20 --format table
```

输出摘要：

```text
highP-total:
  slack=2537.963717；
  raw_ap=50；
  ap_scale=51.228906；
  brun_cap(C_AP=20)=1024.578126；
  allowable_C=49.541634；
  observed_C=0.976011；
  pass=True。
```

逐窗口：

```text
p=5003:
  slack=682.727367；
  ap_scale=24.555737；
  allowable_C=27.803171；
  pass=True at C_AP=20。

p=10007:
  slack=1855.236350；
  ap_scale=26.673169；
  allowable_C=69.554403；
  pass=True at C_AP=20。
```

逐层最紧者为：

```text
p=5003,m=5:
  allowable_C=27.077992。
```

## 3. 审稿意义

这一层把全局剩余从“精确计数 `U_AP`”压成单个常数输入：

```text
AP-Brun-C20:
  在目标删除类中证明固定 gap AP 素对上界常数 C_AP<=20；
  或把超过 C_AP=20 的删除类送入 CRTDefect/PDEC/SAE。
```

注意：本文没有证明 `C_AP<=20`。它只证明若该 AP-Brun 常数包成立，则当前高 `P`
压力样本的低筛保存余量足够。

## 4. 剩余义务

已完成：

```text
AP-Brun 常数判据；
当前样本的允许常数、观测常数和 C_AP=20 余量；
最紧层定位为 p=5003,m=5。
```

仍未完成：

```text
无条件证明目标 AP 删除类满足 C_AP<=20；
或证明 C_AP 超标会触发固定模 CRTDefect/PDEC/SAE；
把该常数包推广到所有 P>1000 目标窗口。
```

所以本文是 `LowSievePreservation-AP` 的条件常数接口，不是行命题最终闭合。
