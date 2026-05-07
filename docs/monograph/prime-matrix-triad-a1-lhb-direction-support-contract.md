# Triad-A1 LHB 方向支撑合同

**状态：** `triad_a1_lhb_direction_support_contract_not_filled`

本文承接 `prime-matrix-triad-a1-lhb-lp-skeleton.md`。上一轮机器骨架确认：

```text
g(t)<=M(t) 与 WHOLEDEF/BRIDGED 零容量行合法；
但仅靠 box-only 容量不能强制 Fourier 抵消。
```

本文件把缺失的第一类结构行固定为 `PDEC direction support`。关键观察是：PDEC 坏窗集合并不是任意
`S subset Z_LHB`；它是由某个零均值测试函数 `F` 与阈值 `kappa` 抽取的同相位坏集。

## 1. 方向支撑行

固定同口径分支

```text
theta=(p,Q,tau,F,kappa,formal unit,window shape)。
```

PDEC 坏窗集合满足

\[
S_\theta=\{x:\Re F(\tau(x))\ge\kappa\}.
\]

令

\[
C_F(\kappa)=\{t\bmod Q:\Re F(t)\ge\kappa\}.
\]

则同一坏窗推前计数

\[
g(t)=\#\{x\in S_\theta:\tau(x)=t\}
\]

满足合法支撑行：

\[
g(t)=0\qquad(t\notin C_F(\kappa)).
\tag{DS-1}
\]

这是 `Tautology/Definition` 类型行，不依赖概率模型，也不依赖背景均匀性。

## 2. 与 LHB 容量相交

在 LHB-typed 分支中已有

\[
g(t)\le M(t).
\]

与 `(DS-1)` 合并后，真实可行支撑被压到

\[
\operatorname{supp}g
\subset
C_F(\kappa)\cap \{t:M(t)>0\}.
\tag{DS-2}
\]

因此有三种情况：

```text
empty intersection:
  LHB 分支直接为空；

sparse intersection:
  进入 LocalSurvivor/SAE 或有限显式 PDEC；

persistent intersection:
  在更小相位支撑上继续做 U_CRT<L_PDEC 或输出 DualCap。
```

`WHOLEDEF/BRIDGED bound=0` 是 `(DS-2)` 的特例：若 `C_F(kappa)` 落在零容量块内，则
`S_theta` 为空。

## 3. Fourier 上界的新形式

加入方向支撑后，对任一非零频率与方向，box 上界从

\[
\sup_{0\le g(t)\le M(t)}
\sum_t c(t)g(t)
\]

降为

\[
\sup_{\substack{0\le g(t)\le M(t)\\g(t)=0\ (t\notin C_F)}}
\sum_t c(t)g(t)
=
\sum_{t\in C_F,\ c(t)>0} c(t)M(t)
\tag{DS-3}
\]

在尚未加入质量等式和其他结构行时，`(DS-3)` 是方向支撑后的第一上界。它仍可能不足以证明
`U_CRT<L_PDEC`，但它给出了明确的失败对象：

```text
D_F(h,zeta)= {t in C_F: M(t)>0 and c_{h,zeta}(t)>0}。
```

若该集合过大或集中，则它本身就是 refined PDEC cap；若它只含有限孤点，则进入 LocalSurvivor。

## 4. 证书输入格式

每个 LHB-PDEC 方向必须登记：

```text
theta_id；
p,Q；
F_values[t] or exact rule for F(t)；
kappa；
C_F(kappa)；
proof that S_theta={x:Re F(tau(x))>=kappa}；
normalization of ||F||_2；
L_PDEC。
```

没有 `C_F(kappa)` 的 PDEC 分支不能进入 A1-LHB 对偶比较，只能标为：

```text
DirectionSupportGap。
```

## 5. 失败回流

| 失败 | 含义 | 回流 |
|---|---|---|
| `DirectionSupportGap` | 未登记 `F,kappa,C_F` | 回到 PDEC 抽取层，补 formal unit |
| `EmptyCap` | `C_F cap supp(M)=empty` | LHB 分支闭合 |
| `SparseCap` | 交集只在有限孤点/短弧 | LocalSurvivor 或 explicit PDEC |
| `PersistentCap` | 交集仍持久承担正质量 | refined PDEC / DualCap |
| `FlatCap` | 支撑无低维峰且 L2-flat | CleanKLS/DLS |

因此方向支撑行也不生成第四出口。

## 6. 当前最小硬点

下一步应从现有 PDEC 抽取文件中为每个 `theta` 物化：

```text
C_F(kappa)；
C_F(kappa) cap supp(M)；
DS-3 的方向上界；
若 DS-3 不足，输出 D_F(h,zeta) 作为 DualCap。
```

这一步会把 `box-only obstruction` 转化为具体的相位交集问题，而不是继续停在抽象 `U_CRT`。

新增脚本 `experiments/prime_matrix_triad_a1_lhb_direction_support_audit.py` 后，交集审计已机器化。
默认把

```text
C_F(kappa)=WHOLEDEF union BRIDGED
```

作为测试支撑，输出 `prime-matrix-triad-a1-lhb-direction-support-audit.md/json`。该默认子分支在当前
`Q=2310`、已列出 P 上全部为 `EmptyCap`，因此它验证了零容量块支撑的 PDEC 方向在 LHB 分支内为空。
一般 PDEC 方向仍需提交真实 `F,kappa,C_F`。

新增 `experiments/prime_matrix_triad_a1_lhb_fourier_cap_scan.py` 后，Fourier 半空间型
`C_F(kappa)` 的压力测试也被机器化。它扫描

```text
C_{h,alpha,dir}={t:cos(2*pi*h*t/Q+dir)>=alpha}
```

与 `supp(M)` 的交集，并分类为 `EmptyCap/SparseCap/PersistentCap`。这不是连续方向的最终证书；
它用于判断“方向支撑本身是否足够”。若高阈值 cap 仍持久，则必须补列位移、尾互补因子或 refined
PDEC 行。

新增 `prime-matrix-triad-a1-fixed-q-density-barrier.md` 后，Fourier-cap 扫描的持久现象被解释为
固定相位层的密度屏障：

```text
|supp(M) cap C_F| >= |supp(M)| + |C_F| - Q。
```

因此当 `supp(M)` 在固定 `Q` 上变稠，任何正密度 `C_F` 都必然 persistent。固定 `Q` 的普通方向
支撑不能成为高 P 全局闭合机制；必须升层、补 column/tail 行或转 CleanKLS。

## 7. 结论

`A1-LHB` 的 LP 行现在分成两层：

```text
capacity rows:
  g(t)<=M(t), zero-cap blocks；

direction support rows:
  g(t)=0 outside C_F(kappa)。
```

容量行解决“哪些相位物理可完成”；方向支撑行解决“PDEC 坏集被迫落在哪些相位”。两者的交集才是
真正的 `U_CRT` 上界对象。
