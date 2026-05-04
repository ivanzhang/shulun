# AlphaTail `C13` 的 `lift>=2` 模 6 空性

**状态：** `c13_liftge2_mod6_sample_closed_global_open`

本文接续 `lift>=2` 空性审计。上一层显示当前样本所有高提升候选 `q` 都被 `2/3` 小素因子杀掉。
本文把该现象改写成模 `6` 判据。

## 1. 模 6 判据

对低筛 AP 删除类

\[
q=a+t\ell,\qquad t\ge2,
\tag{M6-1}
\]

其中 `ell` 是大于 `3` 的素数，故

\[
\ell\equiv1\ \text{or}\ 5\pmod6.
\tag{M6-2}
\]

若 `q` 要成为尾素，则必须满足

\[
q\equiv1\ \text{or}\ 5\pmod6.
\tag{M6-3}
\]

因此只要所有高提升候选满足

\[
a+t\ell\not\equiv1,5\pmod6,
\tag{M6-4}
\]

即可在不使用任何素数分布定理的情况下排除 `lift>=2` 删除。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_mod6_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_mod6_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --format table
```

输出摘要：

```text
highP-total:
  candidates=1368；
  bad_mod6=1368；
  good_mod6=0；
  good_tail=0；
  all_bad=True；
  q_mod6={2:250, 3:928, 4:190}；
  t_mod6={2:888, 3:480}；
  residue_mod6={0:920, 1:252, 5:196}；
  ell_mod6={1:772, 5:596}。
```

逐窗口：

```text
p=5003:
  candidates=704；
  good_mod6=0；
  all_bad=True。

p=10007:
  candidates=664；
  good_mod6=0；
  all_bad=True。
```

## 3. 结构解释

当前样本中的高提升候选只需要模 `6` 即可排除：

```text
q mod 6 = 2 或 4  => 偶数；
q mod 6 = 3       => 3 的倍数。
```

这比最小素因子枚举更强，因为它不需要实际分解 `q`，只检查

\[
(t\bmod6,\ \ell\bmod6,\ a\bmod6)
\tag{M6-5}
\]

三元组。

## 4. 全局化接口

`lift>=2` 分支现在可写成纯模算术义务：

```text
LiftGE2-Mod6Void:
  对所有 P>1000 目标窗口和所有高提升候选，
  证明 a+t ell mod 6 不落在 {1,5}。
```

若出现 `q mod 6 in {1,5}` 的未杀候选，则不应强行闭合，而应进入：

```text
LiftGE2-Residual:
  固定模 CRTDefect / PDEC / SAE 出口。
```

## 5. 审稿边界

已完成：

```text
当前压力样本 lift>=2 候选全部由模 6 判据排除；
小素因子空性从分解事实升级为纯同余事实；
为全局证明提供 LiftGE2-Mod6Void 接口。
```

仍未完成：

```text
全局证明 LiftGE2-Mod6Void；
或将 q mod 6 in {1,5} 的残余高提升候选送入 PDEC/SAE；
把该模 6 接口接回所有 P>1000 目标窗口。
```

所以本文闭合的是当前样本的模 `6` 空性，不是行命题最终闭合。
