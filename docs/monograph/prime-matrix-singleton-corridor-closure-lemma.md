# Singleton 走廊闭合引理

**状态：** `singleton_corridor_reduced_to_standard_disjoint_sifted_union_bound`

本文把当前 singleton-prime corridor 小硬点写成可审稿的确定引理。该闭合只处理 `M_{\ge3}` 的 singleton 尖峰侧；它不宣称 ASB/RPD 全链已经闭合。

## 1. 设置

固定 ASB 窗口

\[
J=[L,R].
\]

在第二锚分解中，singleton 尾值 `d` 表示

\[
\lceil L/(ab)\rceil=\lfloor R/(ab)\rfloor=d.
\]

等价地，令 `m=ab`，则 `m` 落入闭区间

\[
C_d(J)=
\left[
\max\left(\lceil L/d\rceil,\lfloor R/(d+1)\rfloor+1\right),
\min\left(\lfloor R/d\rfloor,\lceil L/(d-1)\rceil-1\right)
\right].
\]

若右端小于左端，则该走廊为空。

## 2. 不相交引理

**引理 2.1。** 对固定窗口 `J`，不同正整数 `d` 对应的非空走廊 `C_d(J)` 两两不相交。

**证明。** 若 `m in C_d(J)`，则由定义有

\[
\lceil L/m\rceil=d,\qquad \lfloor R/m\rfloor=d.
\]

因此 `d` 同时由 `m` 和固定窗口 `J` 唯一确定。若同一 `m` 又属于 `C_e(J)`，则同理得到

\[
e=\lceil L/m\rceil=\lfloor R/m\rfloor=d.
\]

故 `e=d`。所以 `d\ne e` 时两个走廊无交。证毕。

这一步形式化了“单调商分层”刚性：不同尾值是同一窗口中互斥的商层。

## 3. 唯一分解上界

记

\[
N_d(J;z)=\#\{(a,b): ab\in C_d(J),\ z<a\le b\le d,\ a,b\in\mathbb P\}.
\]

**引理 3.1。** 对任意 `d`，

\[
N_d(J;z)\le \#\{m\in C_d(J): (m,P(z))=1\}.
\]

**证明。** 映射 `(a,b)\mapsto m=ab` 是单射。若 `a,b` 为素数且 `z<a\le b`，则 `m` 没有不超过 `z` 的素因子，即 `(m,P(z))=1`。所以每个合法素因子对注入到右侧集合。证毕。

进一步有平凡界

\[
N_d(J;z)\le |C_d(J)|.
\]

宽度为 `1` 的走廊由该平凡界完全吸收。

## 4. 不相交并集上界

设 `D` 为某个窗口中需要计数的 singleton-prime 尾值集合，并令

\[
\mathcal C(J,D)=\bigcup_{d\in D} C_d(J).
\]

由引理 2.1，`C_d(J)` 两两不相交。于是

\[
\sum_{d\in D} N_d(J;z)
\le
\#\{m\in \mathcal C(J,D):(m,P(z))=1\}.
\tag{SCU}
\]

这就是当前小硬点的闭合形式：singleton-prime corridor 侧不再需要多重覆盖校正，只需对不相交短区间并集作一次 `z`-rough 上筛。

## 5. 标准上筛接口的内联化

对不相交区间族 `\mathcal C`，设

\[
X=|\mathcal C|.
\]

新增 `docs/monograph/prime-matrix-disjoint-corridor-selberg-lemma.md`
后，这一步不再作为黑箱引用。对任意支撑在
`d|P(z), d<\xi` 且 `\lambda_1=1` 的 Selberg 权，有精确二次型上界

\[
\#\{m\in\mathcal C:(m,P(z))=1\}
\le
XQ_z(\lambda;\xi)+E_{\mathcal C,z}(\lambda;\xi).
\tag{Sieve-Corr}
\]

其中

\[
Q_z(\lambda;\xi)=
\sum_{d,e<\xi}{\lambda_d\lambda_e\over [d,e]},
\qquad
E_{\mathcal C,z}(\lambda;\xi)=
\sum_{d,e<\xi}\lambda_d\lambda_e
\left(A([d,e])-{X\over [d,e]}\right).
\]

若取最小化权 `\lambda^\ast`，则主项为有限常数
`X\Lambda_z(\xi)`；若再使用标准一维 Selberg 最小化公式，
可写为 `X/G_z(\xi)`，其中

\[
G_z(\xi)=
\sum_{\substack{d<\xi\\ d\mid P(z)}}{\mu^2(d)\over\varphi(d)}.
\]

端点误差只来自不相交短区间对模 `[d,e]|P(z)` 的端点截断。
若该误差持续超预算，则由同一权重合并得到加权低模缺陷能量

因此 singleton 侧最终二分为：

```text
finite Selberg quadratic bound holds with budget
or weighted endpoint/low-mod defect => CRTDefect/Tail-anchor/OSPC.
```

## 6. 样本核查

审计文件 `docs/monograph/prime-matrix-singleton-corridor-overlap-audit.md` 给出：

- 同窗口走廊数：`175`。
- 宽度和：`542`。
- 并集宽度：`542`。
- 重叠冗余：`0`。
- 最大重叠度：`1`。

审计文件 `docs/monograph/prime-matrix-singleton-corridor-bound-audit.md` 给出：

- 合法 semiprime 对数：`181`。
- semiprime/宽度：`0.333948`。
- 宽度 `>=2` 的 semiprime/`Vz`：`1.388255`。
- 混合包络所需常数：`1.299083`。

这些数据支持上面的结构分解，但证明链中可使用的是第 2--5 节的确定引理；数值只作为余量定位。

## 7. 当前闭合结论

当前小硬点已从

```text
singleton-prime corridor bound
```

闭合为

```text
finite Selberg quadratic bound on disjoint singleton-corridor unions
or weighted low-mod endpoint defect => CRTDefect/Tail-anchor/OSPC.
```

仍未闭合的是更上游的完整 ASB/RPD 链：还需证明素互补因子短区间上界、聚合 Mertens 包络常数、Annulus 命题，以及所有异常出口的排斥。
