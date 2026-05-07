# PDEC 对偶失败吸收合同：大 Fourier 上界障碍只能变成帽集中

**状态：** `pdec_dual_failure_absorbed_to_cap_pdec_or_sae_not_closed`

本文承接 `prime-matrix-named-exit-absorption-contract.md`。上一层已经把持久命名缺陷统一成
有限签名群上的 generalized `PDEC`。现在继续攻最窄硬点：

```text
PDEC-Cert 需要证明同一坏窗集合的 U_CRT<L_PDEC。
```

本文不宣称已经证明所有 `U_CRT<L_PDEC`；它证明若某个方向的上界证书失败，则失败不能成为
新自由出口，只能显化为 Bohr-cap 型相位集中，并回流到：

```text
persistent cap => refined PDEC / ColumnCRT；
sparse cap     => SAE；
口径不一致     => Multiplicity/Stitching 义务。
```

## 1. 同一坏窗口径

固定一个 generalized PDEC 块：

```text
G      : 有限签名群或有限签名集；
S      : 同一坏窗集合或已证明合法的坏窗多重集合；
g(a)   : #{x in S: tau(x)=a}；
M      : sum_a g(a)=|S|；
h, zeta: 非平凡字符与方向；
c(a)   : Re(zeta chi_h(a))。
```

所有下界和上界必须作用在同一个 `g` 上。若下界使用 equation/block-local 多重集合，而上界使用
physical 去重集合，则不能比较；此时先进入：

```text
Multiplicity-Legitimacy / FormalUnit-Stitching。
```

这吸收了 `FO-PDEC` 中已经暴露的口径风险。

## 2. Cap localization 引理

对任意 `-1<=alpha<1`，定义方向帽：

```text
C_alpha(h,zeta)={a in G: c(a)>=alpha}。
```

若

\[
\sum_a g(a)c(a)\ge U,
\]

则

\[
g(C_\alpha)\ge
\max\left(0,{U-\alpha M\over 1-\alpha}\right).
\tag{PFA-1}
\]

**证明。**
帽内 `c(a)<=1`，帽外 `c(a)<alpha`，所以

\[
U\le g(C_\alpha)+\alpha(M-g(C_\alpha))
=\alpha M+(1-\alpha)g(C_\alpha)。
\]

移项即得。

特别地，若 `U=M-delta`，则帽外质量满足

\[
M-g(C_\alpha)\le {\delta\over 1-\alpha}。
\tag{PFA-2}
\]

这就是 `FO-PDEC` 中“质量上界只差 1.02% 时必有短弧聚簇”的一般形式。

## 3. 对偶失败三分

若 `PDEC-Dual-Cert` 在某个 `(h,zeta)` 方向失败，即现有约束只能给出

```text
U_CRT(h,zeta)>=L_PDEC，
```

则取 `U=L_PDEC` 或实际原始可行解投影值，应用 `(PFA-1)`。得到三分：

```text
CapSparse:
  g(C_alpha) 很小或只出现有限坏窗
  => SAE/Endpoint；

CapPersistent:
  g(C_alpha) 在正式反例族中持久
  => 在签名 tau'=(tau, 1_C_alpha) 上形成 refined PDEC；

CapColumn:
  C_alpha 同时固定非零列位移、端点 seam 或第 P 列锚残基
  => ColumnCRT / endpoint PDEC。
```

若三者都不发生，则帽质量不足，代入 `(PFA-1)` 反推出该方向的 `U_CRT<L_PDEC`，原失败不存在。

## 4. 递归细化势函数

把 PDEC 内部也加入势函数：

```text
Psi_PDEC=(
  |G|,
  active_frequency_count,
  cap_width,
  signature_rank,
  unresolved_pdec_mass,
  multiplicity_status
)。
```

每次失败只能做以下一项：

```text
缩小 cap_width；
增加 signature_rank；
降低 unresolved_pdec_mass；
进入 SAE；
进入 ColumnCRT；
暴露 multiplicity/stitching 口径不一致。
```

因此 PDEC 失败不会生成无名循环。若 cap 反复持久，有限签名群上必有固定 cap 签名被鸽巢锁定，
从而成为 refined PDEC；若 cap 不持久，则是 SAE。

## 5. 与 H4-PDEC 证书模板的接口

`h4-pdec-certificate-template.md` 要求：

```text
U_CRT<L_PDEC。
```

本文给出失败输出规则：

```text
失败频率 h；
失败方向 zeta；
帽阈值 alpha；
帽集合 C_alpha；
帽质量下界 g(C_alpha)>=(U-alpha M)/(1-alpha)；
口径：set / multiset / physical；
回流：SAE / refined PDEC / ColumnCRT / Multiplicity-Stitching。
```

因此以后任何 `PDEC-Cert` 失败都必须产生可审稿对象，而不能成为新的“低模异常”黑箱。

## 6. 当前闭合边界

本文完成：

```text
PDEC 对偶上界失败 => Bohr-cap/短弧聚簇；
持久聚簇 => refined PDEC/ColumnCRT；
稀疏聚簇 => SAE；
口径不一致 => Multiplicity/Stitching 义务。
```

本文未完成：

```text
所有 PDEC 块的 U_CRT<L_PDEC；
所有 refined PDEC 的最终对偶证书；
所有 SAE/ColumnCRT 出口排斥。
```

所以当前主链进一步压缩为：

```text
PersistentNamedDefect
=> PDEC-Cert
=> success: 矛盾
   failure: cap concentration
      => SAE / refined PDEC / ColumnCRT / Multiplicity-Stitching。
```

这完成的是 `PDEC` 失败形态的结构吸收，不是最终无条件闭合。

## 7. Cap 细化无循环

新增 `prime-matrix-pdec-cap-refinement-no-cycle.md` 后，`failure => refined PDEC` 不再是开放递归。
在固定有限签名群 `G` 内，连续 cap 只会生成一个 Boolean algebra 分区；每次真正的新 cap
必须严格细分某个原子，所以最多细分 `|G|-1` 次。终止后：

```text
singleton atom => ColumnCRT / explicit PDEC；
内部仍有非零频率 => 继续 cap，矛盾；
内部平坦 => Clean local KLS / 对偶上界成立；
sparse atom => SAE。
```

若必须提升到更大签名群 `G'` 才能继续切分，则该分支正是 `new-layer PDEC` 或 `CleanKLS`，
不属于同层无名循环。
