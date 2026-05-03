# 相邻素数平方壳层筛升级引理

**状态：** `annulus_reduced_to_old_sieve_survivor_nonempty`

本文严写从 `p=p_k` 升级到 `q=p_{k+1}` 时，平方壳层

\[
\mathcal A(p,q)=(p^2,q^2]\cap\mathbb Z
\]

中旧筛与新筛的精确关系。该关系是递推路线中 `Annulus(p,q)` 的结构性简化。

## 1. 壳层旧筛幸存者引理

**Lemma ASL-1（平方壳层旧筛幸存者）。**
设 `p<q` 为相邻奇素数。若

\[
n\in(p^2,q^2],\qquad (n,\prod_{\ell\le p}\ell)=1,
\]

则 `n` 是素数，或

\[
n=q^2.
\]

**证明。**
若 `n` 不是素数，则取其最小素因子 `r=P^-(n)`。由假设，`r>p`。又因 `n\le q^2`，

\[
r\le \sqrt n\le q.
\]

由于 `q` 是 `p` 后的下一素数，不存在素数严格位于 `(p,q)`，故 `r=q`。于是 `n=qm`，且 `m\ge q`。再由 `n\le q^2` 得 `m\le q`，所以 `m=q`，从而 `n=q^2`。证毕。

## 2. 新素数 `q` 的非冗余筛除点

**Corollary ASL-2（新增筛线非冗余性）。**
在壳层 `(p^2,q^2]` 中，加入新素数 `q` 后，对旧筛幸存集合真正新增删除的点只有 `q^2`。

**证明。**
`q` 的倍数写成 `n=qm`。若 `n` 是旧筛幸存者，则由 ASL-1，`n` 不是素数且只能为 `q^2`。反之 `q^2` 显然旧筛幸存并被 `q` 删除。证毕。

## 3. 关于 `pq` 的修正

`pq` 的确属于壳层，因为

\[
p^2<pq<q^2.
\]

但它不是旧筛幸存者：

\[
p\mid pq.
\]

因此 `pq` 已经在第 `k` 阶筛中被旧素数 `p` 删除。若只看“`q` 的倍数”，`pq` 会被 `q` 再次命中；但这是冗余命中，不是升级到 `q` 后新增筛掉的待定素数点。

所以精确表述应为：

```text
壳层中 q-倍数的非冗余新增删除点：q^2。
壳层中 q-倍数但旧筛已删除的典型点：pq，以及其他 qm 中 m 有 <=p 的素因子的点。
```

## 4. Annulus 命题的正确改写

令新 `q×q` 方阵第 `s` 行为

\[
J_s^{(q)}=[(s-1)q+1,sq].
\]

其壳层部分为

\[
A_s=J_s^{(q)}\cap(p^2,q^2].
\]

由 ASL-1，若存在

\[
n\in A_s,\qquad n\ne q^2,\qquad (n,\prod_{\ell\le p}\ell)=1,
\tag{1}
\]

则 `n` 必为素数。因此 `Annulus(p,q)` 不必重新证明壳层内素数的完整分布；它可改写为更窄的旧筛剩余非空命题：

\[
\forall s\text{ requiring annulus support},\quad
\left(A_s\setminus\{q^2\}\right)
\cap
\{n:(n,\prod_{\ell\le p}\ell)=1\}
\ne\varnothing.
\tag{Annulus-Rough}
\]

一旦 `(Annulus-Rough)` 成立，`Annulus(p,q)` 自动成立。

## 5. 该引理如何用于递推链

原递推链为

```text
Row(p) + ASB(p,q) + Annulus(p,q) => Row(q).
```

ASL-1 将最后一项替换为

```text
Annulus-Rough(p,q): 每个需由壳层负责的 q 行段含旧 p-筛幸存者，且不只含 q^2。
```

于是递推链可写成

```text
Row(p) + ASB(p,q) + Annulus-Rough(p,q) => Row(q).
```

这比原 `Annulus` 更强可操作，因为壳层候选只需用旧素数 `<=p` 的 CRT 非零同余类检查；不再需要处理 `q` 以下未知合数结构。ASL-1 已经证明：旧筛幸存者除 `q^2` 外自动是素数。

## 6. 仍未自动闭合的部分

ASL-1 不能单独证明 `(Annulus-Rough)`。它只证明：

```text
非空旧筛幸存者 => 素数。
```

还需要证明：

```text
每个相关壳层行段确实存在旧筛幸存者，且不是 q^2。
```

这仍是 CRT/端点/粗剩余非空问题。但难度已经明显降低：新增素数 `q` 不再带来复杂覆盖能力，壳层中的非冗余新筛除只剩单点 `q^2`。

## 7. 审计核查

审计脚本 `experiments/prime_matrix_square_annulus_sieve_lift_audit.py` 与报告
`docs/monograph/prime-matrix-square-annulus-sieve-lift-audit.md` 在 `max_p=2000` 的相邻素数对上核查：

- 相邻素数对数：`302`。
- 壳层幸存合数例外失败数：`0`。
- 非冗余 `q` 倍数均为 `q^2`。
- 完整壳层 `q` 行旧筛幸存者空段数：`0`。
- 边界部分壳层空段只出现在少数小素数对，且这些行通常由旧核心 seam 负责。

这支持把 `Annulus` 接口从“壳层素数存在”改写为“壳层旧筛剩余非空”。
