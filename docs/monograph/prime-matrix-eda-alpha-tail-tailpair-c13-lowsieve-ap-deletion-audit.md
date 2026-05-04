# AlphaTail `C13` 低筛删除的 AP 素对证书

**状态：** `c13_lowsieve_ap_deletion_sample_closed_global_open`

本文接续低筛保存审计。上一层显示纯整数同余删除天花板 `U_int` 在逐窗口 `p=5003`
不够强。本文改用真正相关的对象：落入低筛删除同余类的固定 gap 尾素对。

## 1. AP 删除证书

对等乘数通道

\[
d+j_1r=qu,\qquad d+j_2r=(q+g)u,
\tag{APD-1}
\]

低大素 `ell` 与点位 `j` 的删除条件等价于

\[
q\equiv -(j-j_1)r\,u^{-1}\pmod\ell.
\tag{APD-2}
\]

因此定义 AP 删除素对数

\[
U_{\rm AP}:=
\sum_{\rm channel}\sum_{\ell,j}
\#\{q\in J_{\rm channel}:
q,q+g\in P_T,\ q\equiv a_{\ell,j}\pmod\ell\}.
\tag{APD-3}
\]

每个被低筛删除的几何候选至少被 `(APD-3)` 中某一项计到，所以

\[
D_{\rm low}\le U_{\rm AP}.
\tag{APD-4}
\]

**引理 APD-1（低筛保存的 AP 充分条件）。**  
若

\[
U_{\rm AP}\le G^{\rm geom}-R,
\tag{APD-5}
\]

其中 `R=sum(B2_m+Cap_even_m)`，则 `LowSievePreservation` 成立，继而该窗口满足
`HighP-D2-Lower`。

**证明。**  
由 `G^L=G^{geom}-D_low` 与 `(APD-4)`，

\[
G^L\ge G^{\rm geom}-U_{\rm AP}.
\]

若 `(APD-5)` 成立，则 `G^L>=R`。由 `HighP-PLT` 的充分条件，得到 `HighP-D2-Lower`。□

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_ap_deletion_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_ap_deletion_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
highP-total:
  geom=17860；
  required=15322.036283；
  slack=2537.963717；
  actual_del=50；
  int_ceiling=2309；
  raw_ap=50；
  unique_ap=50；
  classes=3552；
  active_classes=50；
  max_class=1；
  ap_pass=True。
```

逐窗口：

```text
p=5003:
  slack=682.727367；
  int_ceiling=1245；
  raw_ap=5；
  ap_pass=True。

p=10007:
  slack=1855.236350；
  int_ceiling=1064；
  raw_ap=45；
  ap_pass=True。
```

## 3. 结构解释

整数天花板失败的原因是它把 AP 同余类中的所有整数都当成可删除候选；但真实删除还要求
`q` 与 `q+g` 同时为尾素数。样本中：

```text
整数同余命中总量 U_int = 2309；
真实 AP 素对命中 U_AP = 50；
每个活跃 AP 类最多贡献 1 个素对。
```

这说明低筛保存的实质硬点不是同余类数量，而是固定 gap 素对在这些 AP 类中的分布上界。

## 4. 审稿边界

已完成：

```text
低筛删除 AP 充分条件；
当前压力样本中 AP 删除证书逐窗口通过；
p=5003 的整数天花板缺口被 AP 素对计数修复。
```

仍未完成：

```text
全局证明 U_AP <= G_geom-R；
或证明 U_AP 过大时触发固定模 CRTDefect/PDEC/SAE；
把该 AP 上界接入所有 P>1000 目标窗口族。
```

AP-Brun 常数余量见
`prime-matrix-eda-alpha-tail-tailpair-c13-lowsieve-ap-brun-margin.md`。该文件显示当前样本若有
`C_AP<=20` 的目标 AP 素对上界，则逐层通过；最紧允许常数为 `27.077992`。

所以本文闭合的是当前压力样本的 `LowSievePreservation-AP` 证书，不是行命题最终闭合。
