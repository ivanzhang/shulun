# 多点共振主筛因子常数账本

**状态：** `alpha_tail_multipoint_mainfactor_ledger_reduction_open`

本文继续压缩 `multipoint resonance budget` 的常数硬点。目标不是宣称四点/五点共振已经闭合，而是把
所需 Selberg 常数精确物化：给定参数后，需要证明的只剩

\[
|T_{m,r}|\le C_m |I_m|V_{m,r}
\tag{MFL-1}
\]

中的显式常数 `C_m` 足够小，或证明常数失败必进入 `PDEC/SAE/ColumnCRT`。

## 1. 主筛因子

对 `m=4,5`，令

\[
I_m=\{d:d,d+r,\ldots,d+(m-1)r\ {\rm all\ lie\ in\ the\ block}\}.
\tag{MFL-2}
\]

设 `y` 为光滑阈值，`z_m` 为覆盖 `I_m` 中所有点的最大值。定义大素删除主因子

\[
V_{m,r}(y,z_m)=
\prod_{y<q\le z_m}\left(1-{b_{m,q}(r)\over q}\right),
\tag{MFL-3}
\]

其中

\[
b_{m,q}(r)=\#\{-jr\bmod q:0\le j<m\}.
\tag{MFL-4}
\]

若 `q>m` 且 `q\nmid r`，则 `b_{m,q}=m`；若 `q|r`，则 `b_{m,q}=1`。

## 2. 常数需求

定义经验/证书需求常数

\[
C_m^{\rm req}(r)=
{|T_{m,r}|\over |I_m|V_{m,r}(y,z_m)}.
\tag{MFL-5}
\]

正式证明需要提交一个无条件上筛常数 `C_m^{\rm Sel}`，满足

\[
C_m^{\rm Sel}\ge C_m^{\rm req}(r)
\tag{MFL-6}
\]

并同时让共振预算

\[
2C_u\{C_4^{\rm Sel}|I_4|V_{4,r}
+C_5^{\rm Sel}|I_5|V_{5,r}\}
<\mathcal L_{\rm needed}
\tag{MFL-7}
\]

留有正余量。

这把当前硬点从“共振链可能多”压成一个明确常数核验问题。

## 3. 失败出口

若 `(MFL-6)` 或 `(MFL-7)` 失败，则必须发生下列一项：

1. **Selberg 常数不足。**  
   所选权重 `lambda` 太弱；需要优化权重或提高 level。
2. **奇异因子异常。**  
   `V_{m,r}` 因许多 `q|r` 过大，进入 `ColumnCRT/Rankin`。
3. **端点主因子错配。**  
   实际 `T_m` 高于完整 residue 主项，进入多点 `PDEC`。
4. **孤窗异常。**  
   只在少数块超出，进入 `SAE`。

因此失败不会回到未结构化状态；它必须输出具体 `m,r,I_m,V_m,C_m^{req}` 证书。

## 4. 审计样本

审计脚本：

```text
experiments/prime_matrix_alpha_tail_multipoint_mainfactor_audit.py
```

样本使用 `z_m=max(d+(m-1)r)`：

| p | block | shift | m | domain | count | V | C_req |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 4 | 3988 | 189 | 0.32918678 | 0.143967 |
| 997 | 4096 | -36 | 5 | 3952 | 101 | 0.24926487 | 0.102528 |
| 5003 | 8192 | -36 | 4 | 8084 | 1209 | 0.56610662 | 0.264181 |
| 5003 | 8192 | -36 | 5 | 8048 | 916 | 0.49102459 | 0.231795 |
| 10007 | 16384 | -900 | 4 | 13684 | 2860 | 0.58959987 | 0.354483 |
| 10007 | 16384 | -900 | 5 | 12784 | 2302 | 0.51663954 | 0.348539 |

## 5. 审稿边界

已证明：

```text
多点共振预算所需的 Selberg 主项常数
=> 显式 C_req = |T_m|/(|I_m|V_m).
```

尚未证明：

```text
存在正式 Selberg 权重给出足够小的 C_m^{Sel}；
以及该常数足以满足最终反例压力不等式。
```

下一步最小硬点是选择具体 Selberg/Brun 权重，给出 `C_m^{Sel}` 的逐行证明，或把超常数样本路由到
`PDEC/SAE/ColumnCRT`。
