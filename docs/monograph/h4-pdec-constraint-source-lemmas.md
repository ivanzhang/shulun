# H4-PDEC 约束来源引理

**状态：** `h4_pdec_first_source_lemmas_completed`

本文补齐 `PDEC-Dual-Cert` 中 `A g<=b, E g=e` 的第一层来源证明。目标是把“哪些约束行可以进入正式对偶证书”写成可审稿规则。本文不证明这些约束已经足够推出 `U_CRT<L_PDEC`；它只证明若约束的来源条件成立，则该行对同一坏窗计数向量 `g` 有效。

## 1. 统一对象

固定低模周期 `Q`、有限索引域 `X`、相位映射

\[
\tau:X\to \mathbb Z/Q\mathbb Z
\]

和 persistent 坏窗集合 `S\subset X`。定义

\[
g(t)=\#\{x\in S:\tau(x)=t\}.
\]

所有证书行必须作用于这个 `g`。若某一行作用于背景全集、完整 CRT 周期、或另一个候选集合，则必须先证明 `S` 是其子集或投影，否则该行不能进入 `PDEC-Dual-Cert`。

## 2. Mass 与非负性来源

**Lemma H4-PDEC-S1（推前质量行）。**
对任意 `S`，都有

\[
g(t)\ge0,\qquad \sum_{t\bmod Q}g(t)=|S|.
\]

若 persistent 分支只给出 `|S|` 的范围

\[
S_{\min}\le |S|\le S_{\max},
\]

则正式线性系统只能加入

\[
\sum_t g(t)\ge S_{\min},\qquad \sum_t g(t)\le S_{\max},
\]

不能加入精确质量等式。

**证明。**
`g` 是 `S` 在 `tau` 下的推前计数。每个 `x\in S` 唯一落入一个相位，求和即得质量等式；若只知道范围，则只能保留范围不等式。证毕。

## 3. 相位容量来源

设 `Z\subset X` 是已经由独立引理、有限证书或外部定理界定的允许坏窗全集，并且 `S\subset Z`。记

\[
C_Z(t)=\#\{x\in Z:\tau(x)=t\}.
\]

**Lemma H4-PDEC-S2（相位容量继承）。**
若 `S\subset Z`，则对每个相位 `t`，

\[
g(t)\le C_Z(t).
\]

更一般地，对任意相位块 `T\subset \mathbb Z/Q\mathbb Z`，

\[
\sum_{t\in T}g(t)\le \#\{x\in Z:\tau(x)\in T\}.
\]

**证明。**
左侧计数的是 `S` 中落入指定相位或相位块的元素数。由 `S\subset Z`，它不超过 `Z` 中落入同一区域的元素数。证毕。

**审稿要求。**
有限枚举得到的 `phase_cap_t` 可以作为有限范围证书；若用于无限族，必须把 `Z` 和 `C_Z(t)` 替换成符号化容量定理。

## 4. Mirror 等式与成对容量来源

设 `m:X\to X` 是 involution，`\rho` 是 `Z/QZ` 上的 involution，并满足

\[
\tau(m(x))=\rho(\tau(x)).
\]

**Lemma H4-PDEC-S3（镜像闭合行）。**
若 `S` 在 `m` 下闭合，即 `m(S)=S`，则

\[
g(t)=g(\rho(t)).
\]

若只知道 `S\subset Z` 且 `Z` 不一定逐点镜像闭合，则只能使用成对容量

\[
g(t)+g(\rho(t))
\le
\#\{x\in Z:\tau(x)\in\{t,\rho(t)\}\}.
\]

**证明。**
在强条件下，`m` 给出 `S` 中相位 `t` 元素与相位 `rho(t)` 元素的一一对应，故计数相等。弱条件下，用 Lemma H4-PDEC-S2 作用于相位块 `{t,rho(t)}` 即得成对容量。证毕。

**审稿要求。**
`conditional mirror` 行只能在坏窗族已经证明镜像闭合时进入等式矩阵 `E g=e`。否则必须降级为成对容量不等式，不能把完整 CRT 周期的镜像对称直接转移给任意子集 `S`。

## 5. Low-hole bucket 容量来源

令 `h_Q(t)` 是低骨架在相位 `t` 的剩余洞数。对阈值 `m` 定义

\[
T_m=\{t:h_Q(t)\ge m\}.
\]

**Lemma H4-PDEC-S4（bucket 容量行）。**
若已证明允许全集 `Z` 满足

\[
\#\{x\in Z:\tau(x)\in T_m\}\le B_m,
\]

且 `S\subset Z`，则

\[
\sum_{t\in T_m}g(t)\le B_m.
\]

特别地，若某个符号化 Hall/CRT 容量定理证明 `B_m=0`，则所有 persistent 坏窗都不能落在 `h_Q(t)>=m` 的相位上。

**证明。**
这是 Lemma H4-PDEC-S2 对相位块 `T_m` 的直接应用。证毕。

**审稿要求。**
`prime-matrix-bpn-pdec-real-constraint-rows.md` 中 `P=23,Q=210` 的 `low-hole>=5` 上界为 `0`，目前只属于有限样本真实行。要进入全局 H4 证书，必须引用或证明相应的 Hall/CRT 容量定理。

## 6. 出口路由约束来源

有些约束不是直接计数容量，而来自“若违反就离开当前分支”的路由定理。

**Lemma H4-PDEC-S5（路由保留行）。**
设 `R(g)<=B` 是一个线性不等式。若已经证明

\[
R(g)>B\Longrightarrow \mathcal E
\]

且当前 `PDEC-Dual-Cert` 只处理排除了出口 `\mathcal E` 的剩余分支，则可在该剩余分支加入

\[
R(g)\le B.
\]

**证明。**
若剩余分支中存在 `R(g)>B`，路由定理推出出口 `\mathcal E`，与“当前只处理非 `\mathcal E` 分支”矛盾。因此剩余分支必满足 `R(g)<=B`。证毕。

**适用范围。**
该规则可接入：

```text
tail-anchor non-reuse；
core-overlap return；
Rankin low-mod spike routing；
H5.1/H5.4 的 OSPC* 或 weighted CRTDefect 吸收。
```

但每次使用都必须同时列出具体路由定理和被排除的出口名称。若出口本身尚未排除，只能写成分支条件，不能写成全局无条件约束。

## 7. 第一批可安全进入的行

在不增加新数学假设的前提下，当前已经可安全进入 `PDEC-Dual-Cert` 的行分三类：

1. **恒真行：** `g(t)>=0` 与质量范围行；
2. **有限证书行：** 对明确有限范围、明确 `Z` 的 `phase_cap`、`mirror_pair_cap`、`low-hole bucket`；
3. **条件路由行：** 在排除某个出口后的剩余分支中，由已证明路由定理产生的线性上界。

当前还不能无条件进入全局证书的是：

```text
任意坏窗子集的 mirror equality；
由完整 CRT 周期均衡推出的子集均衡；
有限样本 phase cap 直接推广到无限 P；
尚未注明出口排除条件的 tail/core/Rankin 约束。
```

## 8. 下一步最小硬点

本文件闭合的是“约束行合法性规则”。下一步必须把 `prime-matrix-bpn-pdec-constraint-ledger.md`
中的每一类原子逐行标注为：

```text
unconditional tautology；
finite certificate；
symbolic capacity theorem；
conditional routing row；
not yet admissible。
```

完成该标注后，才能生成正式的 `A,b,E,e` 表，并进入 `PDEC-Dual-Cert` 的全频率对偶主控。
