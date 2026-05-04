# AlphaTail 尾素对共振的 Brun/Selberg 常数包接口

**状态：** `alpha_tail_tailpair_brun_selberg_envelope_open`

本文把几何截断后的 `TailPairResonance` 分支转成一个明确的固定差值素对上界账本。
这一步仍不闭合行命题；它把剩余硬点压缩为可审稿的常数包：

```text
短区间固定差值素对上界 + 几何截断
=> TailPairResonance 容量上界。
```

## 1. 几何区间化

由 `TailPair geometric certificate`，固定 `g,j_1,j_2` 后有

\[
u={-(j_1-j_2)r\over g}>0,\qquad d=qu-j_1r.
\tag{BSG-1}
\]

窗口条件 `d in I_m=[A,B]` 等价于

\[
q\in J(g,j_1,j_2)
=
\left[
\left\lceil {A+j_1r\over u}\right\rceil,\,
\left\lfloor {B+j_1r\over u}\right\rfloor
\right].
\tag{BSG-2}
\]

因此共振容量由若干固定 gap 的短区间素对计数控制：

\[
N_g(J)=\#\{q\in J:q,q+g\in\mathcal P_T\}.
\tag{BSG-3}
\]

## 2. 固定差值上界输入

需要的外部或内部上界输入是：

\[
N_g(J)\le
C_{\rm BS}\,\mathfrak S_g\,{|J|\over \log^2 J_-}
 + E_{\rm end}(g,J),
\tag{BSG-4}
\]

其中 `J_- = max(3, inf J)`，`\mathfrak S_g` 是固定差值局部因子。本文使用的标准形为

\[
\mathfrak S_g
=
\prod_{\ell\mid g,\ \ell>2}{\ell-1\over \ell-2},
\tag{BSG-5}
\]

偶性常数与筛归一化全部吸收到 `C_BS` 中。`(BSG-4)` 是上界筛方向，不要求素数对存在，
因此不触碰 parity barrier。若要完全无黑箱，必须在后续把 `(BSG-4)` 逐行内联为
Selberg 二次型或有限证书。

## 3. TailPairResonance 验收不等式

把 `(BSG-4)` 代入几何截断，得到

\[
M_2^{=}
\le
\sum_{g,j_1,j_2}
\left(
C_{\rm BS}\mathfrak S_g {|J(g,j_1,j_2)|\over\log^2 J_-}
 + E_{\rm end}(g,J)
\right).
\tag{BSG-6}
\]

若右端小于 tail-overlap 必须支付的预算，则等乘数共振分支关闭；若右端过大，
失败输出必须指出具体 `g,j_1,j_2,J`。该失败不再是模糊异常，而是：

```text
固定短区间中同 gap 素对过密
=> TailPairResonance-SAE 或 Endpoint concentration。
```

## 4. 常数审计

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_brun_constant_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_brun_constant_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --format table
```

脚本输出：

```text
geom_count          几何截断上界；
bs_scale            sum S_g |J|/log^2 J_-；
required_C_BS       使 C_BS * bs_scale 覆盖 geom_count 所需常数；
top_requirements    最大局部常数需求。
```

该常数不是证明；它是下一步 Selberg 常数包必须达到的验收目标。

## 5. 审稿边界

已证明：

```text
TailPairResonance 被几何区间化；
若固定差值上界 (BSG-4) 成立，则得到总容量上界 (BSG-6)；
失败可定位到具体短区间素对过密。
```

尚未证明：

```text
(BSG-4) 的统一常数包；
或所有超预算短区间过密都进入 SAE/Endpoint 并被排斥。
```

下一步最小硬点是把 `required_C_BS` 降到一个可由 Selberg 上筛证明的显式常数，
或者证明超出该常数的窗口必是孤立 `SAE`。
