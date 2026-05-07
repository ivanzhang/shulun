# Triad-A1 固定 Q 方向支撑密度屏障

**状态：** `fixed_q_direction_support_density_barrier_proved_route_open`

本文承接 `prime-matrix-triad-a1-lhb-fourier-cap-scan.md`。扫描显示：在 `Q=2310` 的 LHB 分支中，
低阈值或高阈值 Fourier cap 对小 `P` 有时为空或稀疏，但从中等 `P` 起迅速变成 persistent。

本文把这个现象提升为一般结构引理：在固定低模 `Q` 上，只要 LHB 可完成相位支撑 `A=supp(M)` 变稠，
任何正密度方向支撑 `C_F` 都不能靠相位交集本身闭合；它必然持久相交。

## 1. 相位交集鸽巢引理

设 `G` 是有限相位群，`|G|=Q`。令

```text
A = {t in G : M(t)>0}；
C = C_F(kappa)。
```

则

\[
|A\cap C|\ge |A|+|C|-Q.
\tag{FQB-1}
\]

特别地，若

\[
|A|>Q-|C|+B,
\tag{FQB-2}
\]

则

\[
|A\cap C|>B.
\tag{FQB-3}
\]

所以当 `B` 是稀疏阈值时，`C` 必然是 `PersistentCap`。

**证明。**
由
\[
|A\cup C|=|A|+|C|-|A\cap C|\le Q
\]
直接移项。证毕。

## 2. 对 Fourier cap 的含义

固定阈值 `alpha<1` 的 Fourier 半空间

\[
C_{h,\alpha,\theta}
=
\{t:\cos(2\pi ht/Q+\theta)\ge\alpha\}
\]

通常有正比例大小。只要 `supp(M)` 的补集小于该 cap 的大小减去稀疏阈值，就不可能得到
`EmptyCap/SparseCap`。

因此固定 `Q` 上的方向支撑只能闭合两类情况：

```text
方向支撑 C_F 本身落在 M(t)=0 的特殊零块；
或 C_F 是非常窄、随 P/Q 自适应收缩的支撑。
```

普通固定低模 Fourier 半空间不是这样的对象。

## 3. Q=2310 读数

由 `prime-matrix-triad-a1-lhb-lp-skeleton.md`：

| P | nonzero M phases | zero M phases |
|---:|---:|---:|
| 13 | 4 | 2306 |
| 17 | 28 | 2282 |
| 19 | 140 | 2170 |
| 23 | 232 | 2078 |
| 29 | 150 | 2160 |
| 31 | 596 | 1714 |
| 37 | 810 | 1500 |
| 43 | 2050 | 260 |
| 47 | 2266 | 44 |

当 `P=47` 时，`A=supp(M)` 只缺 `44` 个相位。任何 Fourier cap 只要相位数大于 `60`，
就必然与 `A` 的交集超过稀疏阈值 `16`。

`prime-matrix-triad-a1-lhb-fourier-cap-scan.md` 的默认扫描正验证了这一点：

```text
alpha=0.9, P=47:
  EmptyCap=16；
  SparseCap=0；
  PersistentCap=9220；
  persistent rate=0.998268。
```

这不是偶然统计，而是固定相位空间的密度屏障。

## 4. 对证明路线的排除

由 `(FQB-1)` 可得一个负结论：

```text
固定 Q 的普通方向支撑
不能作为高 P 全局闭合机制。
```

原因是：`Q` 固定时，随着高层补洞变量增多，`Z_LHB` 的相位投影会变稠；一旦 `supp(M)` 稠密，
任何正密度 cap 都自动 persistent。此时若仍想排斥 PDEC，必须增加新信息：

```text
refined PDEC:
  细化到更高签名层 Q' 或更窄 cap；

Column/displacement rows:
  利用列位移非零类和负载阈值；

Tail/cofactor rows:
  利用 Py-d=qm 的互补因子不可复用；

CleanKLS:
  若所有新增层偏斜趋零，则转入平坦大筛。
```

这正是“素数规律无穷层叠”的结构化版本：固定层只能提供有限分辨率；一旦该层投影变稠，证明必须升层、
细化签名或转入分散。

## 5. 递归剥离协议中的位置

在 A1-LHB 分支中，方向支撑审计现在应按以下顺序使用：

```text
1. 计算 C_F cap supp(M)。
2. 若 EmptyCap，当前方向闭合。
3. 若 SparseCap，进入 LocalSurvivor/explicit PDEC。
4. 若 PersistentCap，不能再靠固定 Q 方向支撑；
   必须升层、加入 column/tail 行，或进入 CleanKLS。
```

若第 4 步继续使用同一个固定 `Q` 和同一种正密度 cap，只会循环回密度屏障。

新增 `prime-matrix-triad-a1-newlayer-lift-pilot.md` 后，屏障后的正确动作已被试验验证：
从 `Q=2310` 提升到 `Q=30030` 后，`P=17,19,23,29` 的 `supp(M)` 密度分别下降约
`13.00, 4.95, 3.22, 3.20` 倍。这说明固定层变稠后应升层拆纤维，而不是继续在旧层调 cap。

## 6. 结论

`Q=2310` LHB 分支的新结构结论是：

```text
零块支撑方向可以闭合；
普通固定 Fourier cap 在高 P 上必然 persistent；
PersistentCap 不是失败，而是强制进入更细签名层、列/尾结构行或 CleanKLS 的证据。
```

这把“方向支撑不够强”的经验观察转化成了固定层相位密度屏障。
