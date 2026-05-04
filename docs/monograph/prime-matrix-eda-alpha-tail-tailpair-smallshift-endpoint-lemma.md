# AlphaTail 尾素对小位移端点清除引理

**状态：** `alpha_tail_tailpair_smallshift_endpoint_lemma_proved`

本文把端点吸收中的样本现象提升为确定性引理：在小位移窗口中，几何截断产生的所有
等乘数共振责任区间都必定贴住端点领口。因此 `InteriorSpike` 自动为空。

## 1. 贴边事实

沿用 `TailPair geometric certificate` 的记号。设

\[
I_m=[A,B],\qquad H=B-A+1.
\tag{SSE-1}
\]

固定 `g,j_1,j_2`，令

\[
u={-(j_1-j_2)r\over g}>0.
\tag{SSE-2}
\]

几何截断给出的 `q` 区间是

\[
Q_-=\left\lceil {A+j_1r\over u}\right\rceil,\qquad
Q_+=\left\lfloor {B+j_1r\over u}\right\rfloor.
\tag{SSE-3}
\]

映回 `d` 区间

\[
D=[uQ_- - j_1r,\ uQ_+ - j_1r].
\tag{SSE-4}
\]

由上取整和下取整，

\[
0\le D^- - A < u,\qquad
0\le B-D^+<u.
\tag{SSE-5}
\]

所以

\[
\operatorname{dist}_{I_m}(D)
=\min(D^- - A,B-D^+)<u.
\tag{SSE-6}
\]

## 2. 小位移端点清除

因为 `g` 整除 `-(j_1-j_2)r`，有

\[
u\le |j_1-j_2|\,|r|\le (m-1)|r|.
\tag{SSE-7}
\]

若

\[
(m-1)|r|\le \theta H,
\tag{SSE-8}
\]

则所有几何截断责任区间都满足

\[
\operatorname{dist}_{I_m}(D)<\theta H.
\tag{SSE-9}
\]

因此每一个局部尖峰都是 `EndpointSpike`，不存在 `InteriorSpike`。

**Theorem SSE（小位移端点清除）。**  
在 `(SSE-8)` 条件下，对任意 `C_local`，`TailPairLocalSpike` 的内区集合为空：

\[
\mathcal S_{\rm int}(C_{\rm local},\theta)=\varnothing.
\tag{SSE-10}
\]

**证明。**  
任意局部尖峰都有某个几何责任区间 `D`。由 `(SSE-6)` 与 `(SSE-7)`，
`dist_I(D)<=(m-1)|r|`。再由 `(SSE-8)` 得 `dist_I(D)<theta H`，故该尖峰按定义为
`EndpointSpike`。证毕。

## 3. 意义

这一步把一部分“跨窗口扫描 InteriorSpike”改成了确定性小位移条件。对 `|r|` 足够小的
AlphaTail 窗口，`(SSE-8)` 有余量成立；对较大位移窗口，该引理可能失败，但仍可使用
`TailPair endpoint absorption` 的精确责任区间审计来判断是否存在内区尖峰。因此内部尾素对共振
被拆成两个可审稿对象：

```text
smallshift pass => InteriorSpike 自动为空；
smallshift fail => 使用精确 endpoint absorption 审计，若仍 interior_clear，则只剩 EndpointSpike。
```

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_smallshift_endpoint_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_smallshift_endpoint_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --endpoint-theta 0.1 --format table
```

输出 `u_max=(m-1)|r|`、`theta*H`、`u_max/H` 与 `smallshift_pass`。

## 5. 审稿边界

已证明：

```text
(m-1)|r| <= theta H => InteriorSpike 为空；
该条件是充分条件，不是必要条件。
```

尚未证明：

```text
EndpointSpike/PDEC/SAE 全部排斥；
或在 smallshift 失败窗口中用精确审计证明 interior_clear，或证明 InteriorSpike 不持久。
```

下一步最小硬点转为端点出口：证明这些端点尖峰要么由统一 endpoint 常数吸收，
要么触发 Directed endpoint CRTDefect/PDEC 并被排斥。
