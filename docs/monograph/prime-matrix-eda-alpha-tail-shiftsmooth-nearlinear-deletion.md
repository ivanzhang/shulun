# ShiftSmooth 近线性块的大素数删除恒等式

**状态：** `alpha_tail_shiftsmooth_nearlinear_deletion_reduction_open`

本文给出比普通 Selberg 包络更硬的近线性结构。若高块仍满足

\[
\max(d,d+r)<y^2,
\tag{NLD-1}
\]

则每个非 `y`-smooth 数最多含一个大于 `y` 的素因子。因此非光滑事件可精确写成

```text
小互补因子 a × 大素数 ell。
```

这把 `ShiftSmooth(r)` 热门位移转化为两个大素数删除集的亏损或重叠异常。

## 1. 删除集

令

\[
I=(B,2B]\cap((B,2B]-r),
\tag{NLD-2}
\]

即保证 `d` 与 `d+r` 同时落在高块 `(B,2B]` 的 `d` 的集合。定义

\[
\mathcal L_y(I)=\{n\in I:\exists \ell>y,\ \ell\ {\rm prime},\ \ell|n\}.
\tag{NLD-3}
\]

以及右侧平移删除集

\[
\mathcal L_y(I+r)-r
=
\{d\in I:d+r\in\mathcal L_y(I+r)\}.
\tag{NLD-4}
\]

## 2. 近线性精确性

若所有 `n` 满足 `n<y^2`，则 `n` 含有至多一个 `>y` 的素因子。因此

\[
n\ {\rm is}\ y{\rm -smooth}
\quad\Longleftrightarrow\quad
n\notin\mathcal L_y.
\tag{NLD-5}
\]

并且若 `n` 非 `y`-smooth，则唯一写成

\[
n=a\ell,\qquad \ell>y\ {\rm prime},\qquad a<{n\over y}<y.
\tag{NLD-6}
\]

这里 `a` 是小互补因子。

## 3. ShiftSmooth 删除恒等式

令 `C_all(r)` 为不带平方自由与 Möbius 符号的双光滑对数：

\[
C_{\rm all}(r)=
\#\{d\in I:d,d+r\ {\rm both}\ y{\rm -smooth}\}.
\tag{NLD-7}
\]

则在 `(NLD-1)` 下有精确恒等式

\[
C_{\rm all}(r)
=
|I|
-
\left|
\mathcal L_y(I)\cup(\mathcal L_y(I+r)-r)
\right|.
\tag{NLD-8}
\]

因此

\[
C_\sigma(r)\le C_{\rm all}(r).
\tag{NLD-9}
\]

## 4. 热门位移的二分

若 `C_sigma(r)` 过大，则 `C_all(r)` 也大。由 `(NLD-8)`，只能发生：

1. **删除亏损。**  
   `L_y(I)` 或 `L_y(I+r)` 比大素数模型显著偏小。这等价于许多短素数区间
   `(n/a,(n+H)/a]` 中素数不足，进入 `PDEC/SAE` 或外部短区间素数输入。
2. **删除重叠过大。**  
   很多 `d` 同时满足

\[
d=a\ell,\qquad d+r=b\ell',
\tag{NLD-10}
\]

其中 `ell,ell'>y` 为大素数，`a,b<y` 为小互补因子。这是双线性素数相关/ColumnCRT 出口。

这比普通大素数 Selberg 上筛更窄：反例必须解释为什么本应删除的两侧大素数倍数没有足够覆盖，
或为什么两侧删除集异常重叠。

## 5. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_nearlinear_deletion_audit.py
```

用法：

```text
python3 experiments/prime_matrix_alpha_tail_nearlinear_deletion_audit.py --selected '997:4096:-36,5003:8192:-36' --format table
```

它输出两侧删除集大小、重叠、并集和无符号双光滑对数。

样本：

| p | block | shift | near | domain | left del | right del | overlap | union | smooth pairs | same sign | plus | minus |
|---:|---:|---:|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | true | 4060 | 1252 | 1248 | 441 | 2059 | 2001 | 456 | 207 | 249 |
| 5003 | 8192 | -36 | true | 8156 | 1398 | 1394 | 410 | 2382 | 5774 | 1451 | 810 | 641 |
| 10007 | 16384 | -900 | true | 15484 | 2517 | 2439 | 853 | 4103 | 11381 | 2963 | 1685 | 1278 |

这说明无符号双光滑删除恒等式仍偏松；真正的 `D_sigma` 热门位移还依赖平方自由与 Möbius 同符号过滤。
因此删除亏损/重叠之后的下一层硬点应写成：

```text
在删除后剩余的 y-smooth 对中，
平方自由同符号过滤是否异常偏大；
若偏大，则触发 Möbius correlation / ColumnCRT / PDEC。
```

## 6. 审稿边界

已证明：

```text
Near-linear ShiftSmooth hotspot
=> large-prime deletion deficit 或 deletion-overlap anomaly.
```

尚未证明：

```text
删除亏损和删除重叠异常不可能。
```

下一步最小硬点是对 `(NLD-10)` 的删除重叠写出小互补因子双线性素数相关上界；
删除亏损则直接回流 `PDEC/SAE`。
