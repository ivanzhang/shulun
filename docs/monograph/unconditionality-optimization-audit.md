# 行列命题、二次筛与 RH 的无条件化优化审查

## 0. 审查边界

本文档的目标是优化证明链，而不是扩大结论宣称。当前应严格区分三种状态：

- **结构层闭合**：定义、CRT 计数、小素锁、大因子不可复用等可逐行证明；
- **外部深定理闭合**：引用 DI/BFI、显式公式、Vaughan/Heath-Brown 等标准定理后某个接口闭合；
- **终局无条件定理**：所有结构入口、分布估计、常数余量和有限验证全部闭合。

当前最优策略不是继续增加新命名，而是把三条主链都压缩成最少的可审稿不等式。

## 1. 统一优化原则

三条链的共同结构是：

```text
反例入口
=> 小结构确定层
=> 剩余粗结构
=> 总命中/出口容量不等式
=> 反例不可能
```

因此优化重点是：

1. 把可完全证明的小结构层全部确定化；
2. 把剩余粗结构压成一个总命中或总出口不等式；
3. 把所有外部输入写成明确定理模板；
4. 删除任何“存在性刚性替代有符号分布”的隐含跳跃。

## 2. 方阵行列命题：从 Structured-EHPD 压缩到 RHI

### 2.1 当前最有希望的新压缩

广义斜率锁 `GSL` 已把小素因子层几何化：

```text
q<=Y 的小素因子
= 广义斜率锁定块
```

删去小素锁后，反例必须在粗数带

\[
G_Y(I)=\{n\in I:(n,\prod_{q\le Y}q)=1\}
\]

上由大素数补洞：

\[
B_Y(I):=\sum_{Y<p\le P}\#\{n\in G_Y(I):p|n\}\ge |G_Y(I)|.
\]

所以最优目标不等式是：

\[
B_Y(I)<|G_Y(I)|.
\tag{RHI}
\]

这比原来的多接口 `Structured-EHPD` 更短：所有局部刚性都服务于证明 `RHI`。

### 2.2 参数窗口的关键观察

令 `Y=P^alpha`。若粗数带在大素数模上近似均匀，则

\[
\frac{B_Y(I)}{|G_Y(I)|}\approx \sum_{Y<p\le P}\frac1p
\approx \log(1/\alpha).
\]

要有余量，需要

\[
\log(1/\alpha)<1
\quad\Longleftrightarrow\quad
\alpha>e^{-1}.
\]

另一方面，一维线性筛的粗数下界通常需要筛参数

\[
s=\frac{\log |I|}{\log Y}
\]

大于下界筛阈值。对长度约 `P` 的行/列窗口，形式上要求 `1/alpha>2`，即

\[
\alpha<1/2.
\]

于是出现一个非常重要的可攻窗口：

\[
e^{-1}<\alpha<1/2.
\]

例如 `alpha=0.4` 同时满足主项余量与线性筛下界的形式要求。这是当前方阵行列命题最值得硬攻的优化方向。

### 2.3 仍不能省略的硬点

`RHI` 不是单靠 GSL 自动推出。需要两条逐行证明：

**PM-R1（短窗口粗数下界）。**

\[
|G_Y(I)|\ge c_-(\alpha)|I|\prod_{q\le Y}(1-1/q).
\]

**PM-R2（粗数带大素命中上界）。**

\[
B_Y(I)\le(\log(1/\alpha)+\eta)|G_Y(I)|.
\]

其中必须满足

\[
\eta<1-\log(1/\alpha).
\]

PM-R2 是真正硬点。粗略估计

\[
\sum_{Y<p\le P}|I|/p
\]

太大，不能与 `|G_Y(I)|` 比较；必须利用“倍数的互补商也必须避开小素数”的粗数结构，即把

\[
n=pm
\]

中的 `m` 也纳入 `Y`-rough 计数。

### 2.4 方阵链条优化结论

方阵行列命题的最优优化不是继续扩展 D 组命名，而是：

```text
GSL + Tail anchors + non-reuse
=> PM-R1 + PM-R2
=> RHI
=> 行/列反例排除
```

若 `PM-R1/PM-R2` 在 `alpha in (e^{-1},1/2)` 中闭合，则原 `Structured-EHPD` 可以被降级为历史框架或辅助解释，主证明链会显著缩短。

## 3. 二次筛问题：把 BMD 与最终素数对提升严格分离

### 3.1 二点筛的主项门槛

二点筛中每个素数通常给两个禁类 `0,w mod p`，最硬情形是 `p∤w`。因此模型命中常数为

\[
2\log(1/\alpha).
\]

要有容量余量，需要

\[
2\log(1/\alpha)<1
\quad\Longleftrightarrow\quad
\alpha>e^{-1/2}\approx0.6065.
\]

这解释了为什么二点筛比行列命题更硬。

### 3.2 当前必须修正的状态边界

`BMD/WBE2/KLS-window` 闭合的是一个重要的分析分布接口，但它不能被含糊写成“已经无条件证明孪生素数”。原因很简单：

- 固定 `w=2` 的二点筛命题若完全闭合，将推出孪生素数型结论；
- 标准 DI/BFI 型分布定理本身不可能单独绕过筛法 parity barrier；
- 因此必须逐项复核 `BMD=>BST-2=>BST=>TLI` 中是否隐藏了筛余下界、真实剩余支撑或 Buchstab 转移稳定性假设。

准确表述应为：

```text
DI/BFI 可闭合 BMD 子接口；
二点筛终局仍需审查 BMD 到 TLI 的无隐藏下界转移。
```

### 3.3 二点筛最优优化链

建议把二点筛重写为五个无条件化义务：

| 编号 | 义务 | 说明 |
| --- | --- | --- |
| TP-U1 | 二相位 GSL 小素锁 | `0,w mod q` 的小素层完全几何化 |
| TP-U2 | 奇异因子与 `q|w` 塌缩 | 把局部一禁类/二禁类常数全部显式化 |
| TP-U3 | BMD/WBE2 分布输入 | 可引用 DI/BFI；自足版需 KLS-window |
| TP-U4 | Buchstab 转移无隐藏下界 | 证明 `BMD` 真的推出 `BST-2`，不偷用素数对下界 |
| TP-U5 | TLI 容量余量 | 证明总大因子命中小于真实粗候选数 |

其中最小硬点不是 TP-U3，而是 TP-U4/TP-U5 的组合：它决定了外部深定理版 BMD 是否足以推出最终二点筛非空。

### 3.4 二点筛优化结论

二点筛下一步不应继续重复证明 `BMD`，而应做一次严格的“BMD 到 TLI 无隐藏下界审查”。若该审查通过，才可把外部 DI/BFI 输入真正转化为二点筛终局；若不通过，缺口必须命名为 `Buchstab-transfer parity gap`。

## 4. RH 问题：必须转为 controlled exits 的形式化，而非继续扩展局部刚性

### 4.1 当前 RH 链条的真实瓶颈

RH 链条已经有显式公式入口、CRT ledger、controlled exits 和 GEE 合成框架。但终局不能升级的原因不是缺少更多局部图像，而是：

```text
每个 controlled exit 是否真能无条件吸收离线零点产生的异常
```

尚未达到独立审稿级证明。

### 4.2 最优形式化方向

RH 链条应改写为四列表：

| 出口 | 输入异常 | 输出吸收 | 使用定理 |
| --- | --- | --- | --- |
| sparse exit | 稀疏孔洞/低密局部异常 | ACC/Hole/OV 吸收 | 组合容量或大筛 |
| dense exit | 密集投影异常 | DGap/PI/FCT/DSO 吸收 | 正交投影/平方函数 |
| tail exit | Vaaler/Fourier 高尾 | C9 吸收 | Fourier 截断与 KL/Vaaler |
| internal exit | 内部循环 | Lyapunov/no-cycle | 有限下降势函数 |

每一行必须给出：

\[
\text{exit load lower bound}
\le
\text{exit capacity upper bound}.
\]

并且所有常数必须使用同一个 baseline convention。

### 4.3 可考虑的更强框架

若要让 RH 链条更接近标准可审查数学，最值得考虑的是把 contradiction-field ledger 接到 Weil/Li 型正性准则：

```text
离线零点
=> 某个显式二次型负值
=> CRT/prime ledger 证明同一二次型非负
=> 矛盾
```

这比“所有局部出口都排除”更集中。若能找到这样的正性二次型，RH 链条会从多出口工程压缩为一个正性定理。

### 4.4 RH 优化结论

RH 方向当前不能通过增加方阵或二点筛刚性直接升级为无条件证明。最优推进是：

1. 把每个 controlled exit 写成独立定理；
2. 统一 baseline 与常数；
3. 尝试把 GEE/no-cycle 合成为一个正性二次型或能量不等式；
4. 保留 `Not claimed` 状态，直到每个出口被独立证明。

## 5. 三条链的共同下一步

当前最小、最有效的工程任务如下。

| 主线 | 下一步最优接口 | 成功后效果 |
| --- | --- | --- |
| 方阵行列 | `PM-R1/PM-R2 => RHI` | 可能替代大部分 Structured-EHPD 复杂接口 |
| 二点筛 | `BMD=>TLI` 无隐藏下界审查 | 判断外部 DI/BFI 是否足以推进二点筛终局 |
| RH | controlled exits 四列表与正性二次型尝试 | 把 RH 从 verification package 压缩为少数定理义务 |

## 6. 本轮最重要的结论

最有希望的直接优化是方阵行列的 `RHI` 路线，因为它有明确参数窗口：

\[
e^{-1}<\alpha<1/2.
\]

二点筛的关键不是再证明 KLS，而是审查 `BMD` 到 `TLI` 是否隐藏 parity barrier。RH 的关键不是增加局部刚性，而是把 controlled exits 定理化或转为正性准则。

因此下一步若继续攻坚，建议优先顺序为：

1. **方阵行列 `PM-R1/PM-R2`。**
2. **二点筛 `BMD=>TLI` 无隐藏下界审查。**
3. **RH controlled exits 四列表形式化。**

## 7. 最新单点硬核后的优先级修正

后续 `PTA-GSL=>BSI=>RSE` 的硬攻把方阵行列链条进一步压缩。当前最细接口不再是笼统的 `PM-R2B`，而是：

```text
QLOW-MID-COMP(intervalized) + RRD + OSPC.
```

其中 `QLOW-MID-COMP` 已有紧区间网格证书：

```text
2<u<=12, certified≈0.21--0.23<0.35.
```

进一步的误差预算表显示：

```text
total interval budget=0.065,
worst post-budget slack=0.052304.
```

Selberg 子项已有精确有理审计：有限样本中的 `Aλ=q0e1` 和 `λ1=1` 残差为零。因此后续区间化的最硬数值部分已从浮点线性代数转移到 `Phihat` 求积、`sin/cos/log` 包络和 `P>=P0` 统一矩常数。

随后 trig/log 子项也已建立纯有理 oracle：最大半径 `2.333e-67`，远小于 `0.016250` 的预算。该 oracle 已接入 `H/Q`，归一化乘积增量为 `6.600e-67`。进一步的 sup-rho 旁路给出 `supBound=0.296630<0.35`，使 `QLOW-MID-COMP` 紧区间不再依赖 `Phihat` 数值求积。新增 `docs/monograph/rse-rrd-ospc-margin-ledger.md` 把后续主链余量写成 `C_RRD+C_OSPC+C_SelbergUniform+C_round<0.053369509758272926`。新增 `docs/monograph/rse-rrd-same-weight-reduction.md` 说明 `RRD` 同权归一化成立，但旧单密度替换不够，必须拆成 `RRD-low/perp/conversion`。新增 `docs/monograph/rse-rrd-low-projection-dichotomy.md` 修正 `OSPC` 归一化并建立低模正交投影二分。新增 `docs/monograph/rse-low-block-exit-criterion.md` 给出 `RRD-low` 的加权 CRT 缺陷吸收阈值 `0.005366563145999495`。现在数值侧最实质剩余是 `P>=P0` 统一 Selberg 矩常数；主链侧剩余是该加权 CRT 缺陷界、`RRD-perp` 正交上界与 `OSPC` 有向出口。

因此优先级应修正为：

1. **先区间化 `QLOW-MID-COMP`。** 这是最窄且可证书化的单点。
2. **逐项填入 `RRD/OSPC` 常数余量表。** 账本已建立；当前应先证明 `sum_B kappa_B m_B<=0.005366563145999495` 或其失败触发 `Tail-anchor/CRTDefect`，再证明 `RRD-perp<=0.012`。只有 `C_RRD<=0.020`、`C_OSPC<=0.020`、`C_SelbergUniform<=0.008` 与 `C_round<=0.003` 在同一 convention 下成立，PM 才能升级为可审稿无条件候选。
3. **随后审查 TP 的 `BMD=>TLI`。** 该审查决定外部 DI/BFI 输入能否真正推进二点筛终局。
4. **最后形式化 RH controlled exits。** RH 不因 PM/TP 局部进展自动升级。

最新统一矩阵见 `docs/monograph/three-proposition-closure-optimization.md`。
