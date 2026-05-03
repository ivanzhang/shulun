# Annulus-Rough 非空命题硬攻

**状态：** `annulus_rough_reduced_to_signed_low_mod_defect_bridge`

本文接续 `prime-matrix-square-annulus-lift-lemma.md`。新的壳层事实已经把 `Annulus(p,q)` 从“壳层素数存在”压缩为“旧筛幸存者非空”。本报告严写该递推关系，并诚实标出最后剩余桥接。

## 1. 记号

设 `p<q` 为相邻奇素数，`q=p+g`。令

\[
J_s^{(q)}=[(s-1)q+1,sq]\qquad(1\le s\le q)
\]

为 `q×q` 方阵第 `s` 行。旧核心与平方壳层分别为

\[
C_p=[1,p^2],\qquad A(p,q)=(p^2,q^2].
\]

定义行段

\[
C_s=J_s^{(q)}\cap C_p,\qquad A_s=J_s^{(q)}\cap A(p,q).
\]

旧 `p`-筛幸存集合为

\[
\mathcal R_p(I)=\{n\in I:(n,\prod_{\ell\le p}\ell)=1\}.
\]

## 2. 递推闭合定理

**Theorem RLC（递推闭合条件）。**
若以下两项成立：

1. **Core-Seam/ASB：** 对每个 `s`，若 `C_s` 非空且该行需要旧核心提供素数，则
   \[
   C_s\cap\mathbb P\ne\varnothing.
   \]
2. **Annulus-Rough：** 对每个 `s`，若 `A_s` 非空且该行没有由旧核心完成，则
   \[
   \mathcal R_p(A_s\setminus\{q^2\})\ne\varnothing.
   \tag{AR}
   \]

则 `Row(q)` 成立。

**证明。**
固定任意 `q` 行 `J_s^{(q)}`。若 `C_s` 中已有素数，则完成。否则该行必须由壳层段 `A_s` 负责。由 `(AR)`，存在

\[
n\in A_s,\qquad n\ne q^2,\qquad (n,\prod_{\ell\le p}\ell)=1.
\]

根据平方壳层引理 ASL-1，壳层旧筛幸存者除 `q^2` 外自动为素数，故 `n` 是素数并位于 `J_s^{(q)}`。任意行均成立，所以 `Row(q)` 成立。证毕。

因此严格递推链为

```text
Row(p) + ASB/Core-Seam(p,q) + Annulus-Rough(p,q) => Row(q).
```

这里 `Row(p)` 的作用不是直接覆盖所有 `q` 行，而是配合 ASB/Core-Seam 处理旧核心重分块；Annulus-Rough 只处理 `(p^2,q^2]`。

## 3. 新发现带来的真实简化

旧写法中，`Annulus(p,q)` 看似需要重新处理壳层内的合数结构。但 ASL-1 给出：

\[
n\in(p^2,q^2],\ (n,P(p))=1
\quad\Longrightarrow\quad
n\in\mathbb P\ \text{or}\ n=q^2.
\]

因此加入 `q` 后真正非冗余删除的旧筛幸存者只有 `q^2`。特别：

- `pq` 在壳层中，但 `p|pq`，已被旧筛删除；
- 其他 `qm` 若 `m<q`，则 `m` 有素因子 `<=p`，也已被旧筛删除；
- 所以 `q` 的新增筛线不会在壳层中制造复杂覆盖场，只留下单点例外 `q^2`。

这把壳层问题从“证明有素数”降为“证明旧筛剩余非空”。

## 4. Annulus-Rough 失败的精确形态

若 `(AR)` 对某个行段 `A_s` 失败，则

\[
\mathcal R_p(A_s)\subseteq\{q^2\}.
\tag{1}
\]

若 `q^2\notin A_s`，则 `\mathcal R_p(A_s)=\varnothing`；若 `q^2\in A_s`，则唯一旧筛幸存者至多是 `q^2`。这等价于：

```text
该壳层 q 行段被 <=p 的旧素数斜线完全覆盖，
除了可能的单点 q^2。
```

由 ASL-1，这同时意味着该行段内没有素数。因此 `(AR)` 的失败是一个强短区间覆盖事件，不是高素新筛事件。

## 5. 签名低模亏损方程

对 `T<=p` 定义截断旧筛剩余

\[
R_T(I)=\#\{n\in I:(n,\prod_{\ell<T}\ell)=1\},
\]

以及 Mertens 主项

\[
M_T(I)=|I|\prod_{\ell<T}\left(1-{1\over\ell}\right).
\]

设

\[
D_T^{\rm ann}(I)=R_T(I)-M_T(I).
\]

若 `I=A_s\setminus\{q^2\}` 且 Annulus-Rough 失败，则

\[
R_{p^+}(I)=0,
\]

其中 `p^+` 表示筛去所有 `<=p` 的素数。于是

\[
D_{p^+}^{\rm ann}(I)
=-\,|I|\prod_{\ell\le p}\left(1-{1\over\ell}\right).
\tag{2}
\]

按 Mertens 量级，

\[
|D_{p^+}^{\rm ann}(I)|
\asymp {|I|\over\log p}.
\tag{3}
\]

对完整壳层 `q` 行，`|I|` 约为 `q`，所以亏损量级约为

\[
{q\over\log p},
\]

这远大于常数级端点误差。故 Annulus-Rough 失败必然产生一个**有符号低模大亏损**。

## 6. 与 ASB/RPD 的统一接口

ASB/RPD 当前剩余接口是：

```text
large positive FAC low-mod endpoint defect D_T
=> directed CRTDefect/Tail-anchor/OSPC.
```

Annulus-Rough 失败给出的是同一类对象的负号版本：

```text
large negative annulus low-mod defect D_T^ann
=> directed CRTDefect/Tail-anchor/OSPC.
```

因此两个剩余硬点可以统一为一个有符号桥接命题：

**Signed-LowMod-Bridge.**
若某个递推采样行段的截断筛余误差满足

\[
|D_T(I)|\ge \Delta_T(I)
\]

并且该误差大到足以破坏预期非空/预算余量，则该行段在小 CRT 模数上产生有向端点集中，从而触发 `CRTDefect/Tail-anchor/OSPC`。

这正是此前矛盾场思想的统一形式：不是分别处理旧核心尖峰与新壳层空段，而是把二者都变成低模端点场的有符号异常。

## 7. 为什么这仍不是无条件闭合

ASL-1 已经闭合了“壳层幸存者是素数”这一步。但 `(AR)` 的非空性仍不能从 ASL-1 自动推出。

若某个完整壳层 `q` 行段没有旧筛幸存者，则它给出一个长度约 `q`、位置约 `q^2` 的无素数窗口。统一证明这种窗口不存在，本质上接近 `\sqrt x` 长度短区间素数问题。现有普通短区间素数定理不能直接给出该长度。

因此不能把 Annulus-Rough 直接写成已证定理。正确的下一步是证明第 6 节的 `Signed-LowMod-Bridge`，即：

```text
壳层空段造成的大负低模亏损
不能与 CRT 周期均衡、端点漂移、相邻互质刚性同时存在。
```

## 8. 强度审查：为什么不能用粗平均闭合

对完整壳层行段，长度约为 `q`，主项约为

\[
M_{p^+}(I)
=|I|\prod_{\ell\le p}(1-1/\ell)
\asymp {q\over \log p}.
\]

这随 `p` 增长，但只呈对数余量。若使用普通上/下筛常数或裸并集容量，常数损失会直接吃掉该余量。更关键的是，`I` 的长度只有 `\sqrt{q^2}` 量级；要无条件证明每个这样的短段含素数，已经是 Legendre 尺度的短区间问题。

因此最后桥接不能写成：

```text
完整 CRT 周期均衡 => 短行段均衡。
```

原因是完整 CRT 周期为

\[
P(p)=\prod_{\ell\le p}\ell,
\]

远大于 `q`，而 `A_s` 只截取极短的一段。完整周期均衡不能自动控制短段端点误差。

同样，不能写成：

```text
总平均有余量 => 每个壳层行段非空。
```

因为审计显示完整壳层行的最小旧筛幸存者数可低至 `1`。这是极薄余量；任何常数级粗化都会丢失非空性。

## 9. 审计支持

审计 `docs/monograph/prime-matrix-square-annulus-sieve-lift-audit.md` 在 `max_p=2000` 的 `302` 个相邻素数对上显示：

- 壳层幸存合数例外失败数：`0`；
- 非冗余 `q` 倍数均为 `q^2`；
- 完整壳层 `q` 行旧筛幸存者空段数：`0`；
- 完整壳层 `q` 行最小旧筛幸存者数：`1`；
- 边界部分壳层空段只出现在少数小素数对，且通常可由旧核心 seam 负责。

该审计验证结构归约与样本非空，但不替代全局证明。

## 10. 当前最小闭合路径

递推路线现在可清晰写成：

```text
Row(p)
+ ASB/RPD-or-positive-lowmod-defect-exit
+ Annulus-Rough-or-negative-lowmod-defect-exit
+ Signed-LowMod-Bridge
=> Row(q).
```

其中已经严格闭合的是：

```text
annulus old p-sieve survivor != q^2 => prime.
```

剩余唯一核心桥接是：

```text
large signed low-mod endpoint defect
=> directed CRTDefect/Tail-anchor/OSPC.
```

这就是从第 `k` 个方阵到第 `k+1` 个方阵建立严格递推关系的最短候选路径。

## 11. Signed-LowMod-Bridge 的端点场化

后续严写见 `docs/monograph/prime-matrix-signed-lowmod-bridge-hard-attack.md`。该文档证明精确恒等式

\[
D_T(I)
=
\sum_{d\mid P_T}\mu(d)
\left(
\left\lfloor {R\over d}\right\rfloor
-
\left\lfloor {L-1\over d}\right\rfloor
-
{|I|\over d}
\right)
=
\sum_{d\mid P_T}\mu(d)
\left(
\left\{{L-1\over d}\right\}
-
\left\{{R\over d}\right\}
\right).
\]

对完整 `q` 行 `I_s=[(s-1)q+1,sq]`，每个低模 `d|P_T` 上的端点误差是

\[
\left\{{(s-1)q\over d}\right\}
-
\left\{{sq\over d}\right\},
\]

而 `q` 与 `d` 互素，故随 `s` 形成单位旋转的 sawtooth 动力系统。于是最后硬点进一步精确化为：

```text
large endpoint sawtooth projection
=> q-rotation + CRT rigidity contradiction.
```

这就是 `SESE-low` 命题。当前已证明的是端点恒等式与低模投影；未证明的是投影到矛盾出口的排斥不等式。

进一步桥接见 `docs/monograph/prime-matrix-directed-endpoint-crtdefect-bridge.md`。该文档证明：

```text
large endpoint sawtooth projection
=> Directed Endpoint CRTDefect / OSPC*.
```

因此本报告中的 `Signed-LowMod-Bridge` 已可严格接到命名出口。剩余若仍有缺口，只能是命名出口 `Directed Endpoint CRTDefect / OSPC*` 的排斥，而不是从低模缺陷到出口的桥接。
