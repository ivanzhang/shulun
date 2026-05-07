# 行命题命名出口吸收合同：把剩余缺口压成同一证书接口

**状态：** `named_exit_absorption_contract_reduces_to_existing_certificates_not_closed`

本文承接 `prime-matrix-unnamed-escape-closure-machine.md`。前一层已经证明：

```text
最小早期零行反例不能无限保持无名；
它必须在有限步内进入 SAE/PDEC/ColumnCRT/Bohr-cap/CleanKLS/TotalDescent 等命名出口。
```

本文的目标不是再引入新出口，而是把所有命名出口接到已有证书模板。这样剩余硬点从
“继续寻找分支”改为：

```text
排斥命名出口；
或证明 CleanKLS；
或证明无缺陷时 TotalDescent 下降到 p=2。
```

## 1. 输入对象

从 SN-1 到 SN3-E 或 RPZ/BPN 链条出来的命名事件统一记为

```text
E(P,y) in {
  SAE,
  PDEC,
  ColumnCRT,
  BohrCap,
  CofactorAnchor,
  TailAnchor,
  CleanKLS,
  TotalDescent,
  EndpointSeam
}。
```

这里 `P,y` 来自同一个最小早期零行候选；所有证书必须使用同一个坏窗集合、同一残余函数、
同一列位移或同一下降阻断相位，不能在中途更换口径。

## 2. 吸收表

| 命名出口 | 触发来源 | 吸收目标 | 仍需证明 |
|---|---|---|---|
| `SAE/endpoint` | 短 q 窗、孤立 Bohr 帽、孤立 seam | `SAE-Cert` 或 `RPZ-SAE-FIN` | 每个孤窗存在 survivor/lift/higher-defect，或被有限证书排除 |
| `PDEC` | 持久低模峰、低模同步、seam 单余类、W-unit Fourier 峰 | `h4-pdec-certificate-template.md` | 对同一坏窗集合证明 `U_CRT<L_PDEC` |
| `ColumnCRT` | 持久非零列位移、`d mod W/P` 峰、unit endpoint seam | `h4-pdec-column-defect-routing-contract.md` | 证明非零位移类负载不可能，或回流 `PDEC/SAE` |
| `BohrCap` | SN3-D 高频列频率经 SN3-E 局部化 | 持久帽 `=> PDEC/ColumnCRT`；孤立帽 `=> SAE`；无帽 `=> CleanKLS` | Bohr-cap 不是独立终端，只需吸收到三归宿 |
| `CofactorAnchor/TailAnchor` | 远尾互补因子或尾锚长期承担正超额 | 固定 m-band/尾锚证书，失败回流 `PDEC/ColumnCRT/SAE` | 证明锚定层不能支付 `R(P,y)`，或显化低模/列缺陷 |
| `CleanKLS` | 低维峰和 Bohr 帽都消失后的 L2-flat 多壳残余 | `CleanMultishellKLS` 输入 | 证明平坦多壳残余总正部不足以支付行余量 |
| `TotalDescent` | 覆盖证书可剥到相邻低素层 | `RPZ-LowerDescent` | 下降到 `p=2` 矛盾，或首个 grid-fail seam 回到 `PDEC/ColumnCRT/SAE` |
| `EndpointSeam` | 下降失败的首个 grid-fail seam | `first-grid-fail seam` 单余类包 | 排斥 `12` 类 seam PDEC/ColumnCRT，或证明正式族避开 seam |

因此 `BohrCap`、`EndpointSeam`、`CofactorAnchor` 都不是第三类自由逃逸；它们必须被继续吸收到
`SAE/PDEC/ColumnCRT/CleanKLS/TotalDescent`。

## 3. 命名出口吸收方程

定义吸收算子 `Abs`：

```text
Abs(SAE)          = SAE-Cert；
Abs(PDEC)         = PDEC-Cert；
Abs(ColumnCRT)    = ColumnCRT-Cert or PDEC/SAE；
Abs(BohrCap)      = PDEC/ColumnCRT/SAE or CleanKLS；
Abs(CofactorAnchor)= TailAnchor-Cert or PDEC/ColumnCRT/SAE；
Abs(TotalDescent) = p=2 contradiction or EndpointSeam；
Abs(EndpointSeam) = PDEC/ColumnCRT/SAE。
```

与无名逃逸闭合机合并后得到：

```text
最小早期零行反例
=> 容量矛盾
   or Abs(E(P,y))。
```

继续展开 `Abs`：

```text
最小早期零行反例
=> 素数洞
   or SAE-Cert
   or PDEC-Cert
   or ColumnCRT-Cert
   or CleanMultishellKLS
   or p=2 下降矛盾。
```

这就是当前最窄的全局接口。若前四类证书全部排斥，且 `CleanKLS` 成立或 `TotalDescent`
在无缺陷时必下降到底，则行命题闭合。

## 4. 统一缺陷向量引理

多数命名出口共享同一个代数骨架。令 `G` 是有限 Abel 群或可嵌入 `Z/QZ` 的有限签名集，
`tau:X->G` 是坏窗签名，`F:G->R` 是零均值测试函数：

\[
\sum_{a\in G}F(a)=0。
\]

若坏窗集合

\[
S=\{x\in X:F(\tau(x))\ge \kappa\}
\]

非空，则按阈值 `beta` 二分：

```text
|S|<beta|X|      => SAE；
|S|>=beta|X|     => generalized PDEC。
```

第二项的 Fourier 下界为：

\[
\max_{\chi\ne 1}|\widehat g(\chi)|
\ge
{ \kappa |S| \over \sqrt{|G|-1}\|F\|_2 },
\qquad
g(a)=\#\{x\in S:\tau(x)=a\}.
\]

证明与 `prime-matrix-bpn-unified-pdec-sae-dichotomy.md` 相同：把
\(\sum_{x\in S}F(\tau(x))\) 写成 `g` 与 `F` 的内积，常数频率因 `F` 零均值消失，再用
Cauchy--Schwarz。

各出口的 `G,tau,F` 口径如下：

| 出口 | 签名群/签名集 `G` | `tau` | 零均值测试函数 `F` |
|---|---|---|---|
| 低模 `PDEC` | `Z/QZ` | 坏窗低模相位 | 低模峰函数减平均 |
| `ColumnCRT` | `Z/DZ` 或 `Z/QZ x Z/DZ` | 非零列位移类 | 位移负载指示减平均 |
| `EndpointSeam` | `Z/rZ` | seam 单余类 | `1_{rho}-1/r` |
| `BohrCap` | `Z/PZ` 的相位桶 | 高频列相位 | 帽指示减平均 |
| `W-unit` 层叠轮峰 | `Z/WZ` | `Py-d mod W` | 单位类内偏差延拓并减平均 |
| `CofactorAnchor` | m-band 或低模互补因子签名 | `m/y` 带、`m mod Q` | 锚带超额函数减平均 |

所以持久命名缺陷可以统一写成：

```text
PersistentNamedDefect
=> generalized PDEC on a finite signature group。
```

孤立命名缺陷则统一写成：

```text
SparseNamedDefect
=> SAE。
```

这一步把 `ColumnCRT`、`Bohr-cap`、`EndpointSeam`、`W-unit` 和 `CofactorAnchor` 的持久分支
都压回同一类 `PDEC-Cert` 验收问题；区别只在签名群和结构约束行的来源。

## 5. 递归剥离的可执行规则

对最小反例执行以下固定流程：

```text
1. 用 SN-1/SN-2 检查自归一化容量；
2. 若正带失败，做 SN3-A 低模剥离；
3. 若剩余多带，做 SN3-C/SN3-D 高频分裂；
4. 若出现 Bohr 帽，立刻用 SN3-E 吸收到 PDEC/ColumnCRT/SAE/CleanKLS；
5. 若无低模、无高频、无帽，则只能调用 CleanKLS；
6. 若覆盖证书可下降，则调用 RPZ-LowerDescent；
7. 若下降失败，首阻断 seam 进入 PDEC/ColumnCRT/SAE；
8. 若任一证书失败，失败输出必须给出缺失约束、失败频率、失败位移或孤窗对象。
```

第 `8` 步是防止“越分越多”的关键：证书失败不能生成无名新分支，只能回流为更具体的同类
`SAE/PDEC/ColumnCRT` 行，或补入一个有来源证明的约束行。

## 6. 与层叠轮筛和圆柱覆盖的关系

`P^2±k mod 30,210,2310,...` 与一般第 `P` 列锚点 `Py-d` 是同一个圆柱平移场：

```text
S_W(P,y)=S_W(P,2)+P(y-2) mod W。
```

逐层提升 `W` 时只有两种可能：

```text
单位类峰随 phi(W) 稀释
  => 高维分散，进入 DLS/KLS/CleanKLS；

单位类峰不稀释并沿新素因子层同步
  => 非零 Fourier 峰，进入 W-unit PDEC 或 ColumnCRT。
```

因此层叠轮筛的“结构刚性”并不是另一个独立证明分支，而是命名出口吸收合同中的
`PDEC/ColumnCRT vs CleanKLS` 二分。圆柱斜线覆盖给容量余量，层叠轮筛给相位缺陷；二者夹击后，
早期零行若存在就必须同时支付容量余量并保持多层相位同步，而这种同步本身就是证书对象。

## 7. 当前闭合边界

本文完成的是：

```text
命名出口不再是无结构剩余；
每个命名出口都有唯一允许的证书接口或下降接口。
持久命名缺陷统一为有限签名群上的 generalized PDEC。
```

本文没有完成：

```text
SAE 全局排斥；
PDEC 的全部 U_CRT<L_PDEC；
ColumnCRTDefect 排斥；
CleanMultishellKLS；
无缺陷 TotalDescent 必下降到底。
```

所以当前最强诚实结论仍是：

```text
无名逃逸闭合 + 命名出口吸收合同完成；
最终无条件行命题尚未完成。
```

## 8. PDEC 对偶失败吸收

新增 `prime-matrix-pdec-dual-failure-absorption-contract.md` 后，`PDEC-Cert` 本身也有失败回流规则。
若同一坏窗集合的某个非零频率方向不能证明 `U_CRT<L_PDEC`，则由 cap localization 引理：

```text
sum_a g(a)c(a)>=U
=> g({a:c(a)>=alpha}) >= (U-alpha M)/(1-alpha)。
```

因此上界失败必显化为短弧/Bohr-cap 聚簇。该聚簇只有四个归宿：

```text
persistent cap => refined PDEC；
cap carries fixed displacement/seam => ColumnCRT/endpoint PDEC；
sparse cap => SAE；
set/multiset/physical 口径不一致 => Multiplicity-Stitching 义务。
```

所以 `PDEC` 失败也不能产生新自由出口；它只会细化同一 `PDEC/ColumnCRT/SAE` 合同，或暴露
证书口径不一致。
