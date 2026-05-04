# 多点 `C=1` 缺陷的粗筛/平方自由分解

**状态：** `alpha_tail_multipoint_rough_smooth_decomposition_reduction_open`

本文继续攻击多点主筛 `C=1` 候选。关键是把

\[
E_m=|T_{m,r}|-|I_m|V_m
\tag{RSD-1}
\]

拆成两个确定项：大素粗筛端点盈余与小素平方自由删除量。这样，若 `E_m>0`，它不能只是“多点链偏多”，
而必须表现为一个粗筛 CRT 端点盈余大到压过小素平方因子的删除。

## 1. 三个集合

令 `I_m` 为 `m` 点都落在目标块内的起点区间。设 `y` 为光滑阈值，`z_m` 为所有点的最大可能值。

定义大素粗筛幸存集

\[
R_{m,r}=\{d\in I_m:\forall j<m,\ d+jr\ {\rm 无素因子}\ q\in(y,z_m]\}.
\tag{RSD-2}
\]

定义平方自由光滑多点链

\[
T_{m,r}=\{d\in R_{m,r}:\forall j<m,\ d+jr\ {\rm squarefree}\}.
\tag{RSD-3}
\]

因为任一 `d+jr<=z_m`，若它没有 `(y,z_m]` 内素因子，则所有素因子都不超过 `y`。所以
`T_{m,r}` 正是 `R_{m,r}` 中再删除小素平方因子的部分。

## 2. 精确分解恒等式

令

\[
H_m=|I_m|,\qquad
V_m=\prod_{y<q\le z_m}\left(1-{b_{m,q}(r)\over q}\right).
\tag{RSD-4}
\]

定义

\[
\Delta^{\rm rough}_m=|R_{m,r}|-H_mV_m,
\tag{RSD-5}
\]

\[
D^{\rm sq}_m=|R_{m,r}|-|T_{m,r}|\ge0.
\tag{RSD-6}
\]

则有精确恒等式

\[
E_m=\Delta^{\rm rough}_m-D^{\rm sq}_m.
\tag{RSD-7}
\]

**证明。**  
由定义直接相减：

\[
|T|-HV=(|R|-HV)-(|R|-|T|).
\]

证毕。

## 3. `C=1` 反例的必要条件

若 `C=1` 失败，即 `E_m>0`，则必有

\[
\Delta^{\rm rough}_m>D^{\rm sq}_m\ge0.
\tag{RSD-8}
\]

因此正缺陷必须同时满足：

1. 大素粗筛 CRT 端点盈余为正；
2. 该盈余大于全部小素平方自由删除量。

这比单纯 `E_m>0` 更强。它把反例压成一个明确矛盾场：

```text
large-prime residue classes overfill the interval
and small-prime square obstructions fail to delete enough points.
```

第一项进入低模/高模 `PDEC`；第二项若异常偏小，则进入小素平方因子稀缺证书。

## 4. 二分出口

对任意 `0<eta<1`，若 `E_m>0`，则至少发生一项：

\[
\Delta^{\rm rough}_m\ge \eta H_mV_m,
\tag{RSD-9}
\]

或

\[
D^{\rm sq}_m<\Delta^{\rm rough}_m<\eta H_mV_m.
\tag{RSD-10}
\]

`(RSD-9)` 是粗筛端点大盈余，直接进入 `PDEC/SAE`。`(RSD-10)` 是平方自由删除不足；它要求
大量粗筛幸存点同时避开所有小素平方因子，进入小素平方类的 CRT 容量账本。

## 5. 审计样本

审计脚本：

```text
experiments/prime_matrix_alpha_tail_rough_smooth_decomp_audit.py
```

样本：

| p | block | shift | m | rough | smooth sqfree | HV | rough surplus | sq deletion | E |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 4 | 1186 | 189 | 1312.796894 | -126.796894 | 997 | -1123.796894 |
| 997 | 4096 | -36 | 5 | 995 | 101 | 985.094774 | 9.905226 | 894 | -884.094774 |
| 5003 | 8192 | -36 | 4 | 4577 | 1209 | 4576.405896 | 0.594104 | 3368 | -3367.405896 |
| 5003 | 8192 | -36 | 5 | 4261 | 916 | 3951.765916 | 309.234084 | 3345 | -3035.765916 |
| 10007 | 16384 | -900 | 4 | 8518 | 2860 | 8068.084595 | 449.915405 | 5658 | -5208.084595 |
| 10007 | 16384 | -900 | 5 | 7629 | 2302 | 6604.719933 | 1024.280067 | 5327 | -4302.719933 |

## 6. 审稿边界

已证明：

```text
E_m = rough_endpoint_surplus - squarefree_deletion.
C=1 failure => rough_endpoint_surplus > squarefree_deletion.
```

尚未证明：

```text
rough_endpoint_surplus 始终不能超过 squarefree_deletion；
或该超过事件必触发 PDEC/SAE/ColumnCRT 证书并可排斥。
```

下一步最小硬点是分别证明粗筛端点盈余上界与平方自由删除下界，或把二者失衡输出为正式证书。
