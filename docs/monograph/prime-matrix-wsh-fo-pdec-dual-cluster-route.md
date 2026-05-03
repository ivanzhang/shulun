# FO-PDEC 对偶短弧聚簇路线

**状态：** `ucrit_obstruction_identified_dual_cluster_exclusion_open`

本文继续硬攻 `FO-PDEC` 的最后 `U_CRT,199` 上界，不更换命题。结论是：当前显式阈值已接近
质量上界，剩余必须排斥一个非常具体的对偶短弧聚簇。

## 1. 质量上界缺口

对最佳投影 `ell=199,h=95`，显式阈值账本给出

\[
  M_{199}=3.959247567099438。
\]

同一向量的质量为

\[
  |E_{199}|=4。
\]

因此纯质量上界只给

\[
  U_{\rm mass}=4,
\]

距离闭合只差

\[
  4-M_{199}=0.04075243290056196。
\]

也就是说，必须证明约 `1.02%` 的真实结构节省。非负性、质量行、支撑行都不足以给出这一节省。

## 2. 对偶短弧结构

新增脚本：

```text
experiments/prime_matrix_wsh_fo_pdec_dual_cluster_audit.py
```

输出：

```text
docs/monograph/prime-matrix-wsh-fo-pdec-dual-cluster-audit.md
docs/monograph/prime-matrix-wsh-fo-pdec-dual-cluster-audit.json
```

审计结果：

```text
ell = 199
mass = 4
support size = 3
best h = 95
max Fourier = 3.959247567099438
mass defect = 0.04075243290056196
dual arc length = 11
dual arc fraction = 0.05527638190954774
original residues = 40(2), 126(1), 61(1)
dual residues = 19(2), 30(1), 24(1)
```

最佳频率把三个原始残基送入长度 `11` 的短弧 `[19,30]`。这解释了为什么 Fourier 模几乎达到
质量上界。

## 3. 证明级聚簇引理

**引理 DC-1（大 Fourier 迫使短弧聚簇）.**
设 `g` 是模素数 `ell` 上的非负计数，质量为 `m`。若某个非零频率 `h` 满足

\[
  |\widehat g(h)|\ge m-\delta，
\]

则旋转相位后有

\[
  \sum_\rho g(\rho)\left(1-\cos\theta_\rho\right)\le \delta,
  \qquad
  \theta_\rho=2\pi h\rho/\ell-\arg\widehat g(h)。
\]

特别地，除非存在可忽略的小质量外，`h rho` 必集中在短弧内。

**证明.**
令 `alpha=arg \widehat g(h)`。则

\[
  |\widehat g(h)|
  =
  \Re(e^{-i\alpha}\widehat g(h))
  =
  \sum_\rho g(\rho)\cos\theta_\rho。
\]

由 `sum g=m` 与 `|\widehat g(h)|>=m-\delta`，移项即得

\[
  \sum_\rho g(\rho)(1-\cos\theta_\rho)\le\delta。
\]

证毕。

该引理说明：要证明 `U_CRT,199<3.959...`，等价于排除或吸收这种短弧聚簇。

## 4. 剩余目标：DualCluster-Exclusion

现在最后硬点应写成：

```text
DualCluster-Exclusion(ell=199,h=95):
同一坏窗集合 g_199 不能在 h=95 的对偶圆周中落入长度 11 的短弧，
除非触发 SAE/Endpoint 或更强 PDEC-Dual-Cert。
```

可用约束必须来自：

1. `SAE/Endpoint`：短弧只出现一次或少数次，则归入稀疏端点逃逸；
2. `PDEC-Dual-Cert`：短弧在相邻行、镜像块或递归壳层中持续出现，则形成 persistent 低模缺陷；
3. `tail non-reuse`：若同一解释因子/尾因子持续复用，则进入 Tail-anchor；
4. `column cap`：若同一列投影承载短弧聚簇，则进入列容量缺陷。

## 5. 当前诚实状态

已完成：

```text
FO-PDEC 方程层；
FO-PDEC 能量产生；
显式 Fourier 下界；
U_CRT 障碍定位为长度 11 对偶短弧聚簇。
```

未完成：

```text
DualCluster-Exclusion 或 SAE/Endpoint 吸收。
```

因此当前仍不能宣称全局无条件闭合。下一步唯一合理硬攻是证明上述对偶短弧聚簇不可能在
正式反例链中持久存在，或把非持久实例完全归入 `SAE/Endpoint`。

## 6. 多重计数合法性更新

新增：

```text
experiments/prime_matrix_wsh_fo_pdec_primitive_cluster_audit.py
docs/monograph/prime-matrix-wsh-fo-pdec-primitive-cluster-audit.md/json
docs/monograph/prime-matrix-wsh-fo-pdec-multiplicity-legitimacy.md
```

后，短弧聚簇的多重性已经查明。最佳投影的 `mass=4` 来自 equation/block-local 口径；
若按物理候选去重，则只剩：

```text
physical mass = 2
physical Fourier = 1.9699193446802263
```

因此最后硬点必须再加一个审稿条件：

```text
Multiplicity-Legitimacy:
证明正式 PDEC 坏窗集合允许 equation/block-local 多重计数；
否则改用 physical 阈值或把重复项送入 SAE/Endpoint。
```

这一步是必要的，否则 `PDEC` 下界和 `U_CRT` 上界可能作用于不同集合。
