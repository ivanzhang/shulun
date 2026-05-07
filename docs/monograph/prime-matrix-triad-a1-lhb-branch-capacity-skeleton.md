# Triad-A1 LHB 分支容量骨架

**状态：** `triad_a1_lhb_capacity_skeleton_partial`

本文承接 `prime-matrix-triad-a1-pdec-capacity-upper-route.md`，选择当前最接近正式 `U_CRT` 上界的
分支：

```text
Q=2310 的 LHB-typed PDEC 分支。
```

目标不是排除全部 PDEC，而是把 A1 的三个子义务在该分支中分开标注：

```text
A1.1 Attachment         : 已由 H4-LHB-Attach 闭合；
A1.2 Phase-compatible rows : Q=2310 有限 P 的 M(t) 与零块容量已物化；
A1.3 Dual comparison    : 仍未提交 U_CRT<L_PDEC。
```

## 1. 分支准入

一个坏窗子族 `S_theta` 可以进入本文骨架，当且仅当它已经通过：

```text
homogeneous split:
  同一 formal unit、同一 tau、同一 p,Q、同一 window shape；

bad-window classification:
  非 SAE；
  非 ColumnCRT/ColumnRadius；
  非 TailAnchor/Rankin；
  满足 LHB-typed 条件 C1--C3。
```

在这些前提下，`h4-pdec-bad-window-classification-lemma.md` 与
`h4-pdec-lhb-attachment-lemma.md` 给出：

\[
S_\theta\subset Z_{\rm LHB}(p,Q).
\tag{LHB-A1}
\]

这正是 A1 的 `Attachment` 输入。

## 2. 同一相位容量

令

\[
g(t)=\#\{x\in S_\theta:\tau(x)=t\}.
\]

由 `(LHB-A1)` 和有限投影证书：

\[
M(t)=\#\{z\in Z_{\rm LHB}(p,Q):\tau(z)=t\},
\]

得到逐相位上界：

\[
g(t)\le M(t).
\tag{LHB-A2}
\]

因此任意相位块 `C` 都有：

\[
\sum_{t\in C}g(t)\le \sum_{t\in C}M(t).
\tag{LHB-A3}
\]

`h4-pdec-lhb-multiplicity-cap-certificate.md/json` 已对下列有限范围物化 `M(t)`：

```text
Q=2310；
P in {13,17,19,23,29,31,37,43,47}。
```

## 3. 已闭合的零块行

在上述有限范围内，证书给出：

```text
WHOLEDEF phase block: bound=0；
BRIDGED phase block : bound=0。
```

于是正式可写入 `A_theta g<=b_theta` 的行是：

\[
\sum_{t\in C_{\rm WHOLEDEF}}g(t)\le0,\qquad
\sum_{t\in C_{\rm BRIDGED}}g(t)\le0.
\tag{LHB-A4}
\]

由于 `g(t)>=0`，这等价于：

```text
S_theta 在 WHOLEDEF 与 BRIDGED 相位块上没有质量。
```

这不是经验规律，而是 `S subset Z_LHB` 与 `M(t)=0` 的集合推论。

## 4. 对 A1 的实际贡献

对任一 PDEC 方向 `(F,kappa)`，若其强制坏相位支撑完全落在
`C_WHOLEDEF union C_BRIDGED` 中，则 `(LHB-A4)` 直接给出：

```text
|S_theta|=0，
```

与 persistent 非空分支矛盾。因此这类 PDEC 分支已在 LHB 分支内排除。

若 `F` 的坏相位支撑还包含其他相位，则 `(LHB-A4)` 只能删除一部分可行域，剩余仍需：

```text
更多 phase/block/column/tail 容量行；
或完整 LP/dual comparison U_CRT<L_PDEC；
或输出 DualCap。
```

所以当前 LHB 骨架的准确结论是：

```text
Attachment closed；
WHOLEDEF/BRIDGED zero-cap rows closed for listed P；
general U_CRT<L_PDEC still open。
```

## 5. 失败回流

在尝试使用本骨架时，所有失败都必须登记：

| 失败 | 含义 | 回流 |
|---|---|---|
| `RangeGap` | `P` 不在已物化有限列表，且无符号化 `M(t)` | 扩展有限证书或证明符号化 LHB 容量 |
| `TypedGap` | 坏窗不是 LHB-typed | `SAE/ColumnCRT/ColumnRadius/TailAnchor/Rankin` |
| `SupportGap` | PDEC 坏相位不只落在零块 | 加入更多合法容量行或进入 LP/dual |
| `DualGap` | 合法行后仍 `U_CRT>=L_PDEC` | `PDEC-Dual-Failure => DualCap` |

这保持了 A1 的无第四出口结构。

## 6. 下一步最小硬点

本分支下一步应直接生成一个 `theta` 级 LP 骨架：

```text
变量:
  g(t), t mod 2310

硬行:
  g(t)>=0；
  mass range；
  g(t)<=M(t)；
  sum_{WHOLEDEF}g(t)=0；
  sum_{BRIDGED}g(t)=0。

待补:
  column compatible rows；
  tail/cofactor nonreuse rows；
  direction-arc dual certificate。
```

若这个 LP 已能给出 `U_CRT<L_PDEC`，则 LHB-typed PDEC 分支闭合；若不能，最优解支撑相位就是下一轮
`DualCap` 或新增合法容量行的具体目标。

新增脚本 `experiments/prime_matrix_triad_a1_lhb_lp_skeleton.py` 将该骨架机器化为：

```text
docs/monograph/prime-matrix-triad-a1-lhb-lp-skeleton.json；
docs/monograph/prime-matrix-triad-a1-lhb-lp-skeleton.md。
```

该脚本还输出一个重要阻断点：只靠 `g(t)<=M(t)` 不能给出全局 Fourier 抵消，因为任何
`M(t)>0` 的相位都允许单相位支撑，单相位支撑的非零频率 Fourier 模长等于自身质量。
所以后续必须补入方向支撑、column/displacement、tail/cofactor nonreuse 或方向弧对偶证书。

新增 `prime-matrix-triad-a1-lhb-direction-support-contract.md` 后，第一类补充行已被固定：

```text
C_F(kappa)={t: Re F(t)>=kappa}；
g(t)=0 outside C_F(kappa)；
supp(g) subset C_F(kappa) cap {M(t)>0}。
```

因此 `box-only obstruction` 的下一步不再抽象：必须为每个 PDEC `theta` 物化 `C_F(kappa)`，
再检查它与 `M(t)>0` 的交集是空、稀疏、持久 cap，还是 flat。

## 7. 结论

`Q=2310` LHB 分支已经完成 A1 的前两级硬点：

```text
Same-Set attachment；
M(t) multiplicity cap；
WHOLEDEF/BRIDGED zero capacity rows。
```

剩余不是再寻找宏观常数，而是对同一个 `g(t)` 做有限 LP/对偶比较，或把失败支撑相位送回
PDEC cap 细化与 LocalSurvivor。
