# ShiftSmooth 的大素数排除筛包络

**状态：** `alpha_tail_shiftsmooth_largeprime_sieve_envelope_reduction_open`

本文把 `ShiftSmooth(r)` 的全局上界写成一个可验收的 Selberg 上筛包络。关键点：`d` 与 `d+r`
都为 `y`-smooth，等价于它们都没有大于 `y` 的素因子。对每个大素数 `ell>y`，这给出两个禁零类；
若 `ell|r`，两个禁零类合并成一个。这正是二禁降一禁在真正上界筛中的位置。

## 1. 大素数排除

设

\[
B<d\le2B,\qquad |r|\le B,\qquad y=\lfloor0.9p\rfloor.
\tag{LPS-1}
\]

若 `d` 与 `d+r` 都为 `y`-smooth，则对任意素数

\[
y<\ell\le 3B
\tag{LPS-2}
\]

必须有

\[
d\not\equiv0\pmod\ell,\qquad d\not\equiv-r\pmod\ell.
\tag{LPS-3}
\]

因为 `d` 与 `d+r` 的绝对值都不超过 `3B`，任何大于 `y` 的素因子都会出现在 `(LPS-2)` 中。

## 2. 二禁降一禁

定义

\[
\omega_r(\ell)=
\begin{cases}
1,& \ell\mid r,\\
2,& \ell\nmid r.
\end{cases}
\tag{LPS-4}
\]

则 `(LPS-3)` 在模 `ell` 上排除 `omega_r(ell)` 个剩余类。

因此无符号 `ShiftSmooth` 数量满足

\[
C_{\rm all}(r)
\le
S(B,r;y),
\tag{LPS-5}
\]

其中 `S(B,r;y)` 是区间 `(B,2B]` 中避开所有 `(LPS-3)` 大素数零类的点数。
同符号计数 `C_sigma(r)` 更小：

\[
C_\sigma(r)\le C_{\rm all}(r).
\tag{LPS-6}
\]

## 3. Selberg 上筛包络

令

\[
P(z)=\prod_{y<\ell\le z}\ell,\qquad z=3B.
\tag{LPS-7}
\]

对任意 Selberg 上筛权 `lambda_a`，`a|P(z)`，`lambda_1=1`，有

\[
S(B,r;y)
\le
\sum_{B<d\le2B}
\left(
\sum_{\substack{a|P(z)\\ d\bmod a\in\Omega_r(a)}}\lambda_a
\right)^2,
\tag{LPS-8}
\]

其中 `Omega_r(a)` 是由 `(LPS-3)` 通过 CRT 生成的禁零类集合。
展开后得到

\[
S(B,r;y)
\le
B\,\mathcal V_r(z)
+
\mathcal E_r(\lambda),
\tag{LPS-9}
\]

主筛因子为

\[
\mathcal V_r(z)
\asymp
\prod_{y<\ell\le z}\left(1-{\omega_r(\ell)\over\ell}\right),
\tag{LPS-10}
\]

误差 `E_r(lambda)` 是有限端点 CRT 锯齿项。

本文不声称 `(LPS-9)` 的常数已经闭合；它给出正式上界接口。

## 4. 奇异因子增益

与普通二禁模型相比，若 `ell|r`，局部因子从 `1-2/ell` 变为 `1-1/ell`。因此

\[
\prod_{\substack{y<\ell\le z\\ \ell|r}}
{1-1/\ell\over 1-2/\ell}
\tag{LPS-11}
\]

是位移 `r` 的奇异因子增益。它解释热门位移常常带有小或中等素因子：这些因子降低了双光滑排除筛的重度。

## 5. 出口

若 `ShiftSmooth(r)` 超过 `(LPS-9)` 的可接受包络，则只能发生：

1. **端点 CRT 误差过大**：`E_r(lambda)` 同号累积，进入 `PDEC/SAE`；
2. **位移奇异因子集中**：许多热门 `r` 共享大素因子结构，进入 `ColumnCRT`；
3. **Selberg 常数账本失败**：需要调整筛水平或提交有限 Rankin/Selberg 证书。

## 6. 审稿边界

已证明：

```text
ShiftSmooth(r) <= 大素数二禁/一禁 Selberg 上筛包络。
```

尚未证明：

```text
该包络在 AlphaTail 所需常数下足够小。
```

下一步最小硬点是选择筛水平与权重，核验 `(LPS-9)` 的主项和端点误差是否足以压住
`ShiftSmooth` 热门位移；失败则输出 `PDEC/ColumnCRT/SAE` 证书。
