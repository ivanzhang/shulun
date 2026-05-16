# Prime Matrix 非 PDEC 平方根相位支撑归约

## 0. 本步边界

本文继续攻击上轮压出的 Prime Matrix 最窄硬点：

```text
NonPDECSquareRootPhaseSupportBound.
```

目标不是宣称行/列命题已经无条件闭合，而是把 `SuperSqrtPressureProductPDECExclusion` 再压窄一层：真正需要控制的不是粗形式乘积

\[
M_q^{\rm form}=A_gA_f,
\]

而是实际能承载反例链的非 PDEC paired packet 数

\[
N_q=|\Pi_q|.
\]

这里 `Pi_q` 是已经通过 generator/fill 双槽、CRT 相位锁和非复用条件的实际压力包集合。

结论是：

```text
如果每个非 PDEC actual packet 都落入 primitive AffineTwin 双槽支撑，
则 N_q <= sqrt(q(q-2))。
```

因此平方根门的真正剩余不再是抽象的 `M_q` 控制，而是：

```text
ProductAccountingTightening
or PrimitiveTwinSlotSupportEscape-PDEC/SAE.
```

## 1. 已有输入

当前仓库已经有三项关键输入。

### 1.1 固定双槽相位锁

文件：

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-router.md
```

已经证明当前 primitive AffineTwin 双槽满足：

```text
generator modulus = q-2
fill modulus      = q
CRT modulus       = q(q-2)
pair support width = (q+9)/2
```

对当前 `q=31`，宽度为 `20`，CRT 模数为 `899`，因此固定双槽图样在相位支撑内至多有一个代表。

### 1.2 平方根乘积门

文件：

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-router.md
```

已经把 SAE 可求和压成：

\[
M_q^2\le q(q-2).
\]

若成立，则

\[
{M_q\over q(q-2)}\le {1\over\sqrt{q(q-2)}}\le {1\over q-2},
\]

再由 Brun/Selberg twin reciprocal ceiling 吸收。

### 1.3 两侧压力乘积

文件：

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-router.md
```

已经证明平方根门等价于：

\[
{A_g^2\over q-2}{A_f^2\over q}\le 1.
\]

若失败，失败形态是相邻 twin epochs 的同步 residue-pressure collision。

## 2. 关键修正：formal product 与 actual packet 分离

此前账本中使用的

\[
M_q^{\rm form}=A_gA_f
\]

是形式上界：它枚举 generator 侧 residue 与 fill 侧 residue 的所有可能配对。

但反例链真正能消耗 SAE/Rankin 质量的对象不是所有形式配对，而是实际同时满足以下条件的 packets：

1. 两侧槽都存在；
2. 两侧 CRT 条件相容；
3. 共同 phase support 非空；
4. 没有 repeated-residue/reset；
5. 没有固定投影复现导致 `ColumnCRT/PDEC`；
6. packet 没有逃出 primitive AffineTwin 双槽模型。

定义这些实际 packets 的集合为 `Pi_q`，并记

\[
N_q=|\Pi_q|.
\]

则永远有

\[
N_q\le M_q^{\rm form}.
\]

因此若 `M_q^{form}` 超过平方根而 `N_q` 未超过平方根，问题不是数学反例，而是账本上界过粗。此时应执行 `ProductAccountingTightening`，把 SAE 质量从 `M_q^{form}/q(q-2)` 改为 `N_q/q(q-2)`，或者把多余形式配对登记为虚配对，不再计入实际负载。

## 3. 支撑宽度小于平方根门

设 primitive AffineTwin 双槽的共同相位支撑宽度为

\[
W_q={q+9\over2}.
\]

对所有 `q>=13`，有

\[
W_q\le \sqrt{q(q-2)}.
\]

证明很直接。平方后等价于

\[
(q+9)^2\le4q(q-2),
\]

即

\[
3q^2-26q-81\ge0.
\]

该二次式在 `q>=13` 单调增大，且

\[
3\cdot13^2-26\cdot13-81=88>0.
\]

所以 `q>=13` 时成立。

AffineTwin 当前候选从 `q=31` 起；更小 `q<13` 若出现，应进入有限例外/低模 PDEC 账本，而不能作为无限逃逸族。

## 4. 非 PDEC 注入

令 `Omega_q` 为 primitive AffineTwin 双槽相位支撑中的整数相位集合，因此

\[
|\Omega_q|\le W_q.
\]

对实际 packet `a in Pi_q`，取其共同相位代表：

\[
\pi_q(a)\in\Omega_q.
\]

若存在两个不同 actual packets `a_1 != a_2` 满足

\[
\pi_q(a_1)=\pi_q(a_2),
\]

则二者在同一 `q(q-2)` CRT 相位和同一短相位支撑内复现。固定图样的 CRT 模数已经大于支撑宽度，因此这种复现不能作为两个自由 packets 存在；它必须进入：

```text
repeated-residue/reset-PDEC
or fixed projection ColumnCRT/PDEC.
```

所以在排除 PDEC/ColumnCRT 后，投影 `pi_q` 是注入：

\[
\Pi_q\hookrightarrow\Omega_q.
\]

于是

\[
N_q=|\Pi_q|\le|\Omega_q|\le W_q.
\]

结合第 3 节得到：

\[
N_q\le\sqrt{q(q-2)}\qquad(q\ge13).
\]

这就是非 PDEC actual packet 版本的平方根门。

## 5. 新归约定理

**NonPDEC Actual-Packet Square-Root Support Reduction.**
固定 AffineTwin `q>=13`。假设：

1. 所有实际压力包均进入 primitive AffineTwin 双槽支撑；
2. 同一 primitive 投影复现已经路由为 `PDEC/ColumnCRT`；
3. SAE 质量按 actual packet 数 `N_q` 计，而不是按粗形式乘积 `M_q^{form}` 计。

则

\[
N_q^2\le q(q-2),
\]

并且 moving AffineTwin actual packets 的 SAE 质量满足

\[
{N_q\over q(q-2)}
\le {1\over\sqrt{q(q-2)}}
\le {1\over q-2}.
\]

接受 Brun/Selberg twin reciprocal ceiling 时，该 moving actual-packet 尾和被吸收。

## 6. SuperSqrt 失败的三分

若观察到形式平方根失败

\[
(M_q^{\rm form})^2>q(q-2),
\]

则现在只有三种可能。

### 6.1 账本上界过粗

\[
M_q^{\rm form}>\sqrt{q(q-2)}
\quad\text{but}\quad
N_q\le\sqrt{q(q-2)}.
\]

这不是反例结构，而是 bookkeeping looseness。处理方式：

```text
ProductAccountingTightening.
```

即将实际 SAE 质量改用 `N_q`，并把没有实际共同相位支撑的形式配对删除。

### 6.2 投影碰撞

\[
N_q>\sqrt{q(q-2)}
\quad\text{and all packets are primitive-supported}.
\]

由于 `N_q>sqrt(q(q-2))>=W_q>=|\Omega_q|` 不可能注入，必有投影碰撞，因此进入：

```text
ProjectionCollision-PDEC / ColumnCRT.
```

### 6.3 primitive 支撑逃逸

某些 actual packets 不落入 `(q+9)/2` 的 primitive 双槽支撑。这就是新的最窄真实硬点：

```text
PrimitiveTwinSlotSupportEscape-PDEC/SAE.
```

它必须被证明不可能，或被登记为新的 moving-slot/endpoint/lowmod 出口，而不能再混在 `SuperSqrt` 中。

## 7. 与临界误差原则的连接

临界误差框架要求使用 actual load，而不是粗上界：

\[
\mathcal E_q=
{N_q^2\over q(q-2)}-1.
\]

若 `N_q` 被 primitive 支撑和非 PDEC 注入控制，则

\[
\mathcal E_q\le0.
\]

因此正临界误差只能来自：

```text
actual support escape
or projection collision
or accounting uses M_form instead of N_q.
```

这比旧表述更窄。旧硬点是：

```text
SuperSqrtPressureProductPDECExclusion.
```

新硬点是：

```text
ActualPacketProjectionExhaustion
+ ProductAccountingTightening
+ PrimitiveTwinSlotSupportEscape routing.
```

## 8. 下一步最窄主攻

下一步应直接证明：

```text
PrimitiveTwinSlotSupportExhaustion.
```

可审稿版本为：

> 每个能在 AffineTwin branch 中实际承担反例补洞负载、且未触发 repeated-residue/reset/ColumnCRT 的 generator-fill packet，必满足已登记的 primitive depth identities，并落入宽度 `(q+9)/2` 的共同相位支撑。

若证明完成，则：

```text
PrimitiveTwinSlotSupportExhaustion
=> N_q <= (q+9)/2
=> N_q <= sqrt(q(q-2))
=> Brun/Selberg absorbs moving actual packets
=> SuperSqrt branch collapses to PDEC/SAE/accounting tightening.
```

若失败，失败对象已经具体化为：

```text
PrimitiveTwinSlotSupportEscape-PDEC/SAE.
```

这就是当前行/列命题主线的最新最窄、最可攻硬点。

## 9. 当前状态

本步完成：

- 区分 formal product `M_q^{form}` 与 actual packet count `N_q`；
- 证明 primitive 支撑宽度 `(q+9)/2` 在 `q>=13` 时低于平方根门；
- 证明非 PDEC 投影注入推出 `N_q<=sqrt(q(q-2))`；
- 将 `SuperSqrt` 失败三分为 accounting looseness、projection collision、primitive support escape。

本步未完成：

- 全局证明所有 actual packets 都 primitive-supported；
- 把现有 SAE/Rankin 账本全部从 `M_q^{form}` 切换为 `N_q` 后重新核验；
- 排斥 `PrimitiveTwinSlotSupportEscape-PDEC/SAE`。

因此行/列命题仍未无条件闭合，但最新剩余已从抽象超平方根压力乘积，压缩为实际包投影耗尽与 primitive 支撑逃逸。
