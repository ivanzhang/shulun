# AlphaTail `C13` 中间层结构空性合同

**状态：** `midlayer_structural_void_sample_closed_global_open`

本文替换较弱的 `MidHalfOnly` 样本接口。新的接口不要求先证明所有整数
`h`-gate 都落在半层；它只针对真实低素候选，直接从大小压缩与同余奇偶推出
`lift=1` 中间层空性。

## 1. 记号

固定窗口 `(p,B,r,m)`。令低大素块最小素数为 `L`，并设

\[
N=(m-1)|r|.
\tag{MSV-1}
\]

对 `lift=1` 中间层真实候选，存在整数

\[
1\le h<u,\qquad \ell\ge L,\qquad |n|\le N
\tag{MSV-2}
\]

使

\[
q={ (u+h)\ell+n\over u}
\tag{MSV-3}
\]

且由目标窗口几何有

\[
q\le {2B\over u}.
\tag{MSV-4}
\]

## 2. 压缩引理

若

\[
2B+N<5L,
\tag{MSV-5}
\]

则任何真实中间层候选都满足 `u+h<=4`。

证明：由 `(MSV-3)` 与 `(MSV-4)` 得

\[
(u+h)\ell+n\le 2B.
\]

再用 `ell>=L` 与 `n>=-N` 得

\[
(u+h)L-N\le 2B.
\]

若 `u+h>=5`，则 `5L-N<=2B`，与 `(MSV-5)` 矛盾。所以 `u+h<=4`。
由于 `1<=h<u`，只剩两种真实中间候选：

```text
(u,h)=(2,1)；
(u,h)=(3,1)。
```

## 3. 同余杀除

真实候选还必须满足

\[
n+h\ell\equiv0\pmod u.
\tag{MSV-6}
\]

若 `2|r`，则 `n` 为偶数；低素 `ell>2` 为奇数，所以 `(u,h)=(2,1)` 时
`n+ell` 为奇数，不可能被 `2` 整除。

若 `3|r`，则 `n` 被 `3` 整除；低素 `ell>3` 不被 `3` 整除，所以
`(u,h)=(3,1)` 时 `n+ell` 不可能被 `3` 整除。

因此在

```text
2B+(m-1)|r|<5L；
6 divides r；
L>3
```

下，`lift=1` 中间层真实低素候选为空。

## 4. 目标族比例接口

在默认 `alpha=0.9,m<=5` 下，若目标族满足

```text
B/p < 1.8；
|r|/p < 0.225；
6 divides |r|；
L > alpha p；
```

则

\[
2B+(m-1)|r|
<3.6p+0.9p
=4.5p
<5L.
\]

所以该比例接口同时推出：

```text
lift>=2 structural void；
lift=1 midlayer structural void。
```

## 5. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_midhalf_structural_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_midhalf_structural_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --format table
```

输出摘要：

```text
cases_forced=True；
shift_even=True；
shift_mod3=True；
low_gt3=True；
structural_mid_void=True；
min_compression_margin=6007。
```

## 6. 审稿边界

该合同闭合的是显式高 `P` 样本与满足比例接口的窗口。完整行命题仍依赖
`TargetFamilyGenerator`：

```text
证明所有 C13 高 P 目标窗口都满足上述比例接口；
证明目标窗口族无遗漏；
对失败窗口给有限证书或 PDEC/SAE 出口。
```
