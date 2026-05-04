# AlphaTail `C13` 高 P 的低筛保存审计

**状态：** `c13_lowsieve_preservation_ap_input_open`

本文接续 `HighP-PLT`。上一层把高 `P` 的 `D2` 支配压成

\[
G^L\ge R,\qquad
R:=\sum_m(B_{2,m}+\mathrm{Cap}_{{\rm even},m}),
\tag{LSP-1}
\]

其中 `G^L` 是低大素筛后仍保存的等乘数固定 gap 尾素对数。本文审计低筛删除是否可由纯
整数同余上界吸收。

## 1. 删除同余类

对一个等乘数通道

\[
d+j_1r=qu,\qquad d+j_2r=(q+g)u,
\tag{LSP-2}
\]

低大素 `ell` 删除该候选，当且仅当某个点位 `j` 满足

\[
d+jr\equiv0\pmod \ell.
\tag{LSP-3}
\]

代入 `d=qu-j_1r`，得到 `q` 的单一同余类：

\[
qu+(j-j_1)r\equiv0\pmod\ell,
\tag{LSP-4}
\]

即

\[
q\equiv -(j-j_1)r\,u^{-1}\pmod\ell.
\tag{LSP-5}
\]

因此低筛删除具有强刚性：每个 `(channel,ell,j)` 只删除 `q` 区间中的一个剩余类。

## 2. 纯整数删除上界

记 `G^geom` 为不加低筛、但要求几何候选 `d in I_m` 的固定 gap 尾素对数。若 `D_low` 是低筛
实际删除量，则

\[
G^L=G^{\rm geom}-D_{\rm low}.
\tag{LSP-6}
\]

由 `(LSP-5)` 得到整数同余删除天花板：

\[
D_{\rm low}
\le
U_{\rm int}
:=
\sum_{\rm channel}
\sum_{\ell\in L_{\rm low}}
\sum_{j=0}^{m-1}
\#\{q\in J_{\rm channel}:q\equiv a_{\ell,j}\pmod\ell\}.
\tag{LSP-7}
\]

于是纯整数路线的充分条件为

\[
G^{\rm geom}-U_{\rm int}\ge R.
\tag{LSP-8}
\]

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_preservation_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_preservation_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
highP-total:
  geom=17860；
  required=15322.036283；
  slack=2537.963717；
  actual_deleted=50；
  integer_deletion_ceiling=2309；
  integer_ceiling_pass=True。
```

逐窗口：

```text
p=5003:
  geom=6325；
  required=5642.272633；
  slack=682.727367；
  actual_deleted=5；
  integer_deletion_ceiling=1245；
  integer_ceiling_pass=False。

p=10007:
  geom=11535；
  required=9679.763650；
  slack=1855.236350；
  actual_deleted=45；
  integer_deletion_ceiling=1064；
  integer_ceiling_pass=True。
```

## 4. 结论

纯整数同余天花板在高 `P` 总池中通过，但在当前逐窗口最紧点 `p=5003` 不通过。因此若主链坚持
逐窗口付款，`LowSievePreservation` 不能只靠 `(LSP-7)`；必须使用更强的 AP 素对删除上界：

\[
D_{\rm low}
\le
U_{\rm AP},
\tag{LSP-9}
\]

其中 `U_AP` 只计同余类中同时满足 `q,q+g` 为尾素数的候选。实际样本中

```text
p=5003:
  actual_deleted=5 << slack=682.727367。
```

这说明剩余不是同余结构本身，而是需要证明“固定 gap 素对不会集中落入这些低筛删除同余类”。

## 5. 下一硬点

当前最窄目标更新为：

```text
LowSievePreservation-AP:
  对每个删除同余类，证明固定 gap 尾素对计数满足 AP 上界；
  或证明若 AP 删除过密，则产生固定模 CRTDefect/PDEC/SAE 出口。
```

本文完成的是低筛删除结构和整数天花板审计，不是行命题闭合。

下一层 AP 素对删除证书见
`prime-matrix-eda-alpha-tail-tailpair-c13-lowsieve-ap-deletion-audit.md`。该证书在当前压力样本中
给出 `U_AP=50`，逐窗口最紧点 `p=5003` 只有 `U_AP=5`，从而修复纯整数天花板的逐窗口失败。
