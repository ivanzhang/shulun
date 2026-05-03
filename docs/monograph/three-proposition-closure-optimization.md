# 三个命题证明链的无条件化优化矩阵

## 0. 审查目标

本文只做证明链优化，不升级终局宣称。三个命题分别是：

1. **PM：方阵行列素数存在性。**
2. **TP：二次筛 A/B 型二点粗素数命题。**
3. **RH：离线零点反例矛盾场。**

三条链共享同一矛盾场思想，但审稿级证明必须分别闭合。尤其：

```text
存在性刚性不能替代有符号分布估计；
完整 CRT 周期均衡不能替代短窗口真实剩余分布；
数值证书不能替代区间外向舍入证明。
```

## 1. 三链统一形态

三条链都可写成同一个五段模板：

```text
反例入口
=> 确定结构层
=> 粗剩余层
=> 总命中/总出口不等式
=> 反例排斥
```

优化的核心是把所有局部刚性放入“确定结构层”，然后只留下一个可审稿的总不等式。

| 主线 | 反例入口 | 确定结构层 | 粗剩余层 | 总不等式 | 当前状态 |
| --- | --- | --- | --- | --- | --- |
| PM | 某行/列无素数 | CRT 非零、GSL、45 度锁、大因子不可复用 | `Y`-rough 尾段锚 | `RHI / PTA-GSL / RSE` | 压缩到 `QLOW-MID-COMP(intervalized)+RRD+OSPC` |
| TP | 后半窗口二点候选为空 | 二禁类锁、`q|w` 降一禁、奇异因子 | 二点 `Y`-rough 剩余与双素曲线 | `TLI / BST / BMD` | 分布子链外部闭合，转移链仍需审查 |
| RH | 离线零点产生异常 | 显式公式入口、CRT ledger、局部出口分类 | prime/CRT 异常负载 | controlled exits / no-cycle | verification package，终局未声明 |

## 2. PM 链的最短当前链条

### 2.1 旧接口压缩

旧的方阵链条可表示为：

```text
PM-1 Matrix model
=> PM-2 CRT nonzero skeleton
=> PM-3 large-factor non-reuse
=> PM-4 diagonal/GSL locks
=> PM-5 tail anchors
=> PM-6 A/B structured reduction
=> PM-7 Structured-EHPD exclusion
=> PM-8 row/column closure
```

现在应把 `PM-5/PM-7` 压成更短的尾段粗数命中链：

```text
GSL + rough complement
=> RHI
=> PM-R2B
=> PTA-GSL
=> BSI
=> RSE
=> QLOW-MID-COMP(intervalized) + RRD + OSPC.
```

这条链的作用是把“全覆盖反例”转写为尾段粗锚平均上的 Selberg/sawtooth 估计。

### 2.2 当前最后三个接口

当前 PM 链不应再写成笼统的 `Structured-EHPD`。最小剩余为：

| 接口 | 内容 | 当前可用成果 | 剩余义务 |
| --- | --- | --- | --- |
| `QLOW-MID-COMP(intervalized)` | `2<u<=12` 紧区间带权常数界 | 网格证书显示 `certified≈0.21--0.23<0.35`；误差预算表显示预留 `0.065` 后最小余量仍为 `0.052304`；Selberg 样本线性系统已精确有理审计；trig/log oracle 半径为 `2.333e-67`；H/Q 增量为 `6.600e-67`；sup-rho 旁路给出 `supBound=0.296630<0.35`；RRD/OSPC 账本给出 `0.0533695` 可分配余量 | `P>=P0` 统一 Selberg 矩常数；按账本证明 `C_RRD<=0.020`、`C_OSPC<=0.020` |
| `RRD` | rough replacement defect | 已定位为替换误差接口 | 需把粗数替换误差写成同一权 convention 下的显式不等式 |
| `OSPC` | oriented small-prime concentration to CRTDefect | 普通 `SPC` 不足，需有向版本 | 需证明有向小素集中必触发 CRTDefect/Tail-anchor 矛盾 |

因此 PM 当前最优硬攻顺序是：

```text
QLOW-MID-COMP 区间化
=> RRD 同权重误差账本
=> OSPC 有向集中排斥
=> PTA-GSL
=> PM-R2B/RHI
=> 行列反例排斥。
```

### 2.3 PM 的无条件化判据

若存在显式常数使

\[
C_{\rm comp}+C_{\rm RRD}+C_{\rm OSPC}<C_{\rm margin},
\]

且所有常数在同一 Selberg 权、同一平滑截断、同一 `R=P^\theta` convention 下成立，则 PM 链可从“压缩接口”升级为“可审稿无条件候选”。

当前尚未满足的关键已经从“建立账本”推进为“逐项填账本”：`docs/monograph/rse-rrd-ospc-margin-ledger.md` 给出目标

\[
C_{\rm RRD}+C_{\rm OSPC}+C_{\rm SelbergUniform}+C_{\rm round}<0.053369509758272926,
\]

并预分配 `0.020+0.020+0.008+0.003=0.051`。因此后续 PM 的真实硬点是证明 `RRD` 同权归一化、`OSPC` 有向出口和 `P>=P0` 统一 Selberg 矩常数均落入该账本。

最新 `RRD` 审查见 `docs/monograph/rse-rrd-same-weight-reduction.md`。关键更新是：旧的一步常数密度替换最坏 `roughDiff/env≈0.200`，不能直接证明 `C_RRD<=0.020`；但振幅恒等式把 `RRD` 精确送入同一 `sum |omega_l|/l` 变差范数。因此 `RRD` 的下一步不是重跑单密度实验，而是证明

\[
C_{\rm RRD-low}+C_{\rm RRD-perp}+C_{\rm RRD-conv}\le 0.020,
\]

其中预算为 `0.006+0.012+0.002`。最小硬点是低模投影 `Pi_{<=Z}` 的二分：低模项小则吸收，低模项大则触发 `OSPC/CRTDefect`。

进一步的低模投影审查见 `docs/monograph/rse-rrd-low-projection-dichotomy.md`。它修正 `OSPC` 归一化为 `E_dir(q,r)>=1+delta_dir`，并把 `Pi_{<=Z}` 定义为小模周期、Buchstab 低层和辅助模有向残基块生成的有限字典正交投影。因此当前最小硬点已精确化为：

```text
低模块预算违例 => 修正后 OSPC* 或直接 CRTDefect；
低模正交余项 => RRD-perp<=0.012。
```

最新 `docs/monograph/rse-low-block-exit-criterion.md` 又把第一项压成代数常数判据：取 `delta_dir=1/4`，若无 `OSPC*` 且

\[
\sum_B \kappa_B m_B\le 0.005366563145999495,
\]

则 `RRD-low<=0.006`。因此 PM 当前最小硬点是证明该加权 CRT 缺陷界，或证明其失败必触发 `Tail-anchor/CRTDefect`。

### 2.4 相邻素数递推路线审查

新增 `docs/monograph/prime-matrix-recursive-lift-audit.md` 审查递推路线：

```text
p=p_k 行命题成立
=> 升级到 q=p_{k+1}
=> 旧核心 [1,p^2] 的素数不会被新筛抹掉
=> 只需处理 (p^2,q^2]？
```

正确部分是旧素数确实不会变成合数；新素数 `q` 在 `q×q` 方阵中主要表现为第 `q` 列，新增压力集中在旧平方边界之后。真正断点是行分块重排：`p` 行是

\[
I_t^{(p)}=[(t-1)p+1,tp],
\]

而 `q` 行是

\[
J_s^{(q)}=[(s-1)q+1,sq].
\]

设 `q=p+g`。`J_s^{(q)}` 含完整 `p` 行当且仅当

\[
(-(s-1)q\bmod p)\le g.
\]

当 `g` 很小时，完整 `p` 行传递比例约为 `(g+1)/p`，因此 `Row(p)` 不能直接推出旧核心中的 `Row(q)`。递推路线必须改写为

```text
Row(p) + Seam(p,q) + Annulus(p,q) => Row(q).
```

其中 `Seam(p,q)` 要证明每个 `q` 行切出的旧核心缝合窗口含旧素数；`Annulus(p,q)` 只处理 `(p^2,q^2]` 新区间。这是一个更清晰的递推框架，但它不是自动闭合。

新增 `docs/monograph/prime-matrix-seam-endpoint-audit.md` 后，`Seam(p,q)` 的最小接口可进一步写成端点屏障 `SEB(p,q)`。设旧 `p` 行 `I_t` 的末个素数位置为 `L_t`、下一行首个素数位置为 `F_{t+1}`，并记

\[
\sigma_t=p-L_t,\qquad \pi_{t+1}=F_{t+1}-1.
\]

若新 `q` 行不含完整旧 `p` 行，其残基为 `r=(s-1)q mod p`，则该窗口无素数当且仅当

\[
L_t\le r,\qquad F_{t+1}>r+q-p,
\]

从而失败必推出

\[
\sigma_t+\pi_{t+1}\ge q.
\]

因此足够证明

\[
\max_{1\le t<p}(\sigma_t+\pi_{t+1})<q.
\tag{SEB}
\]

`p<=10000` 审计中实测 seam 空窗为 `0`，`SEB` 证书失败为 `0`，最强端点压力出现在 `p=37,q=41`，最大端点空段和为 `33`，比值约 `0.805`。审稿状态仍需保守：`SEB` 不是由 `Row(p)` 自动推出，而是新的局部端点素数间隙待证不等式。充分递推链条可写为

```text
Row(p) + SEB(p,q) + Annulus(p,q) => Row(q).
```

但新增 `docs/monograph/prime-matrix-seb-unconditionality-audit.md` 后，应把无条件化目标再修正为更精确的 `ASB(p,q)`。原因是 `SEB` 检查所有旧行边界，相当于要求每个边界两侧相邻素数间隙都不超过 `q`，接近 `G(p^2)<=q` 的强素数间隙控制；实际 `Seam` 只检查新 `q` 行边界给出的残基

\[
r_s=(s-1)q\bmod p.
\]

因此真正最小递推链条应写为

```text
Row(p) + ASB(p,q) + Annulus(p,q) => Row(q).
```

`ASB-Fail` 的反例同时带有 `q` 行漂移残基、两个旧 `p` 行端点合数段和旧/新双分块结构，保留了方阵/CRT 矛盾场可利用的信息。

新增 `docs/monograph/prime-matrix-asb-pressure-audit.md` 与 `docs/monograph/prime-matrix-asb-hard-attack.md` 后，`ASB` 的当前最小硬点进一步压缩为相对高素点覆盖不等式 `ASB-RHC`。对 `ASB` 采样窗口 `J`，取 `z=p^\alpha` 并定义低筛粗剩余

\[
R_z(J)=\{n\in J:(n,\prod_{\ell\le z}\ell)=1\}.
\]

若 `ASB-Fail` 成立，则 `R_z(J)` 中每个数都是合数且必有某个素因子 `z<ell<=p`，故

\[
|R_z(J)|
\le
|D_z(J)|,\qquad
D_z(J)=\bigcup_{z<\ell\le p}(R_z(J)\cap \ell\mathbb Z).
\]

所以只要证明同权相对点覆盖上界

\[
|D_z(J)|
\le (1-\eta)|R_z(J)|,
\tag{ASB-RHC}
\]

就可排除 `ASB-Fail`。遮挡审计同时显示，裸总 incidence 可能超过 `|R_z(J)|`，所以必须控制并集点覆盖或扣除重复命中能量。启发式常数给出关键窗口 `e^{-1}<\alpha<1/2`：低筛仍有正余量，而高素第一矩约为 `log(1/alpha)<1`。因此递推路线的当前最小接口是

```text
ASB-RHC + Annulus(p,q).
```

新增 `docs/monograph/prime-matrix-asb-rhc-alpha-sweep.md` 后，`ASB-RHC` 又可等价改写为粗剩余素数比例下界：

\[
|D_z(J)|=|R_z(J)|-|R_z(J)\cap\mathbb P|,
\]

所以

\[
|D_z(J)|\le(1-\eta)|R_z(J)|
\Longleftrightarrow
|R_z(J)\cap\mathbb P|\ge\eta |R_z(J)|.
\tag{RPD}
\]

`p<=2000`、后排 `25%` 扫描中，`alpha=0.43`、`0.46`、`0.49` 的最坏窗口粗剩余素数比均为 `0.1875`，未出现零粗素数窗口。样本支持 `RPD`，但审稿状态必须保持：`RPD` 已是短窗口粗剩余素数下界，不能由普通覆盖容量自动推出。下一步最小接口应写为

```text
RPD-or-CRTDefect + Annulus(p,q).
```

新增 `docs/monograph/prime-matrix-rpd-failure-structure.md` 后，`RPD` 失败又被拆成粗合数投影问题。`alpha=0.43`、`p<=2000`、后排 `25%` 的最坏 `40` 个窗口中：

- 低筛粗剩余总数 `2002`；
- 素数数 `548`，比例 `0.273726`；
- 粗合数数 `1454`；
- 半素数数 `1248`，占粗合数比例 `0.858322`。

因此递推路线的当前最小接口可进一步写为

```text
Semiprime projection bound
or semiprime over-density => CRTDefect/Tail-anchor/OSPC
+ Annulus(p,q).
```

新增 `docs/monograph/prime-matrix-semiprime-anchor-projection.md` 后，半素数投影进一步拆成锚层效率问题。对粗半素数 `n=ab` 取最小因子 `a` 为锚。最坏窗口样本中：

- 半素数总数 `1248`；
- 锚容量总和 `10785`；
- 总体容量效率 `0.115716`；
- 低锚层 `[0.43,0.50)` 容量最大但效率仅 `0.041676`；
- 高锚层 `[0.90,1.01)` 容量效率最高，为 `0.613707`。

因此当前最小接口再更新为

```text
Anchor-layer semiprime bound
or anchor-layer over-efficiency => CRTDefect/Tail-anchor/OSPC
+ Annulus(p,q).
```

新增 `docs/monograph/prime-matrix-anchor-cofactor-interval-audit.md` 后，锚层效率问题又被精确化为互补素数短区间平均。对每个锚 `a`，

\[
S_a(J)=\pi(\lfloor R/a\rfloor)-\pi(\max(a,\lceil L/a\rceil)-1).
\]

最坏 `40` 个窗口中，互补区间数为 `1647`，整数容量为 `7086`，素互补因子为 `1248`，总素密度为 `0.176122`；但逐窗口半素数/粗合数比例最高达到 `1.000000`。所以递推路线的最新最小接口应写成逐窗口形式：

```text
Average prime-cofactor interval bound
+ M_{>=3} rough-composite budget
or density/energy spike => CRTDefect/Tail-anchor/OSPC
+ Annulus(p,q).
```

新增 `docs/monograph/prime-matrix-mge3-budget-audit.md` 后，`M_{\ge3}` 项也不再作为黑箱。若 `n` 是至少三粗因子点，取最小锚 `a=P^-(n)`，则

\[
M_{\ge3}(J)=\sum_{z<a\le R^{1/3}}
\#\{c:\lceil L/a\rceil\le c\le\lfloor R/a\rfloor,\ c\ \text{composite},\ P^-(c)\ge a\}.
\]

同批最坏窗口中 `M_{\ge3}=206`，占粗合数 `0.141678`，恒等式校验差为 `0`。因此递推路线的最新接口应再压缩为：

```text
prime-cofactor interval bound
+ low-anchor composite-cofactor bound
or corresponding density spikes => CRTDefect/Tail-anchor/OSPC
+ Annulus(p,q).
```

新增 `docs/monograph/prime-matrix-mge3-second-anchor-audit.md` 后，低锚复合互补因子上界进一步化为第二锚粗尾上界：

\[
M_{\ge3}(J)=\sum_{z<a\le b}
\#\{d:\lceil L/(ab)\rceil\le d\le\lfloor R/(ab)\rfloor,\ P^-(d)\ge b\}.
\]

样本中第二锚恒等式校验差为 `0`，整数容量为 `1012`，容量效率为 `0.203557`，尾因子为素数比例 `0.980583`。因此最新接口为：

```text
prime-cofactor interval bound
+ second-anchor b-rough tail bound
or density spikes => CRTDefect/Tail-anchor/OSPC
+ Annulus(p,q).
```

新增 `docs/monograph/prime-matrix-mge3-tail-envelope-audit.md` 后，第二锚粗尾上界可转写为 Mertens/Brun 包络二分。令

\[
V(b)=\prod_{\ell<b}(1-1/\ell).
\]

同批最坏窗口中，实际 `b`-rough 尾数 `206`，Mertens 包络 `165.810608`，所需全局放大常数 `1.242381`；最大层级常数为 `1.700839`，最高窗口尖峰为 `3.400694`。因此最新接口是：

```text
prime-cofactor interval bound
+ aggregated second-anchor Mertens envelope
or localized tail-density spike => CRTDefect/Tail-anchor/OSPC
+ Annulus(p,q).
```

新增 `docs/monograph/prime-matrix-tail-spike-localization-audit.md` 后，局部尖峰不再是一般密度异常，而是 singleton-prime corridor。审计显示：pair 尾区间数 `957`，singleton 粗尾 `182`，其中 singleton 素尾 `181`、singleton 粗合尾 `1`。当尾区间退化为单点 `d` 时，尖峰等价于

\[
\max(\lceil L/d\rceil,\lfloor R/(d+1)\rfloor+1)\le ab\le
\min(\lfloor R/d\rfloor,\lceil L/(d-1)\rceil-1).
\]

因此最新接口为：

```text
prime-cofactor interval bound
+ aggregated Mertens envelope outside singleton corridors
+ singleton-prime corridor bound
or corridor spike => CRTDefect/Tail-anchor/OSPC
+ Annulus(p,q).
```

新增 `docs/monograph/prime-matrix-singleton-corridor-bound-audit.md` 后，singleton-prime 走廊上界获得确定链：

\[
\#\{(a,b):ab\in C_d,\ z<a\le b\le d\}
\le \#\{m\in C_d:(m,P(z))=1\}\le |C_d|.
\]

样本中唯一走廊数 `175`，走廊宽度总和 `542`，合法 semiprime 对数 `181`，semiprime/宽度 `0.333948`；宽度 `1` 走廊由确定宽度界处理，宽度 `>=2` 的 semiprime/`Vz` 为 `1.388255`，混合所需常数 `1.299083`。最新接口为：

```text
prime-cofactor interval bound
+ aggregated Mertens envelope outside singleton corridors
+ singleton corridor z-rough Selberg bound
or sustained z-rough saturation => CRTDefect/Tail-anchor/OSPC
+ Annulus(p,q).
```

新增 `docs/monograph/prime-matrix-singleton-corridor-overlap-audit.md` 后，singleton 侧进一步简化：同一 ASB 窗口内走廊不重叠，走廊宽度和 `542`，同窗口并集宽度 `542`，重叠冗余 `0`，最大重叠度 `1`。因此该侧最新接口为：

```text
prime-cofactor interval bound
+ aggregated Mertens envelope outside singleton corridors
+ z-rough upper sieve on disjoint singleton-corridor unions
or high local density => CRTDefect/Tail-anchor/OSPC
+ Annulus(p,q).
```

新增 `docs/monograph/prime-matrix-disjoint-corridor-selberg-lemma.md` 后，该上筛接口已内联为有限二次型：

\[
\sum_{d\in D}N_d(J;z)
\le
X\Lambda_z(\xi)+E_{\mathcal C(J,D),z}(\lambda^\ast;\xi).
\]

因此 singleton 侧当前最窄接口更新为：

```text
prime-cofactor interval bound
+ aggregated Mertens envelope outside singleton corridors
+ finite Selberg quadratic bound on disjoint singleton corridors
or weighted endpoint defect => CRTDefect/Tail-anchor/OSPC
+ Annulus(p,q).
```

新增 `docs/monograph/prime-matrix-rpd-first-anchor-identity.md` 与 `docs/monograph/prime-matrix-asb-rpd-weighted-sieve-kernel.md` 后，`prime-cofactor interval bound` 与 `aggregated Mertens envelope` 可进一步统一为第一锚粗互补因子恒等式。半素数和 `M_{\ge3}` 不再分别预算；全部粗合数等于

\[
\sum_{z<a\le p}\#\{c\in I_a(J):P^-(c)\ge a\}.
\]

于是递推路线当前最小接口压缩为：

```text
first-anchor weighted rough-cofactor budget
<= lower rough-residue budget
or weighted low-mod defect => CRTDefect/Tail-anchor/OSPC
+ Annulus(p,q).
```

审计 `docs/monograph/prime-matrix-rpd-first-anchor-identity-audit.md` 显示同批压力窗口中粗合数 `1454` 与第一锚粗互补因子 `1454` 完全相等，恒等式差 `0`。因此该压缩不是启发式，而是由最小素因子唯一性给出的确定结构。

新增 `docs/monograph/prime-matrix-rpd-fac-budget-audit.md` 后，当前硬点进一步数值化：同批窗口的 FAC 模型量为 `1075.256057`，全局所需常数 `1.352236`，但逐窗口最大所需常数 `1.695703` 大于 `eta=0.10` 的逐窗口最小允许常数 `1.570917`。因此递推支线不能依赖裸全局平均常数；必须证明分层/端点修正后的逐窗口 FAC-Selberg 预算，或把超预算项转化为加权低模端点缺陷并接入 `CRTDefect/Tail-anchor/OSPC`。

新增 `docs/monograph/prime-matrix-rpd-fac-lowmod-defect-audit.md` 后，后一条出口已有可计算形态：最尖峰窗口 `p=53,q_row=43` 的 FAC 缺陷 `5.333565` 中，`T=17` 低模截断已捕获 `90.9089%`；同批窗口在 `T=101` 的最小捕获率为 `80.4688%`、平均捕获率为 `95.9096%`。所以递推支线的当前最小硬点进一步压缩为

```text
large low-mod endpoint defect D_T
=> directed CRTDefect/Tail-anchor/OSPC.
```

新增 `docs/monograph/prime-matrix-square-annulus-lift-lemma.md` 后，递推链中的 `Annulus(p,q)` 也被压缩。若 `p<q` 为相邻素数且 `n∈(p^2,q^2]` 避开所有 `<=p` 的素因子，则 `n` 是素数或 `q^2`。因此壳层中加入 `q` 后真正非冗余删除的旧筛幸存者只有 `q^2`；`pq` 已被旧素数 `p` 删除。于是剩余壳层接口可改写为：

```text
Annulus-Rough(p,q):
每个相关壳层 q 行段含旧 p-筛幸存者，且不只含 q^2。
```

审计 `docs/monograph/prime-matrix-square-annulus-sieve-lift-audit.md` 在 `max_p=2000` 下验证壳层幸存合数例外失败数为 `0`，完整壳层行空段数为 `0`。这不能替代非空证明，但把 `Annulus` 从“壳层素数存在”降为“旧筛剩余非空”。

新增 `docs/monograph/prime-matrix-annulus-rough-nonempty-hard-attack.md` 后，`Annulus-Rough` 失败被写成负低模端点亏损：若某壳层行段 `I` 没有旧筛幸存者，则

\[
D_{p^+}^{ann}(I)=-|I|\prod_{\ell\le p}(1-1/\ell),
\]

量级约为 `-|I|/log p`。这与 ASB/RPD 的正 FAC 低模尖峰统一成同一桥接：

```text
large signed low-mod endpoint defect
=> directed CRTDefect/Tail-anchor/OSPC.
```

因此递推路线当前最短候选闭合链为：

```text
Row(p)
+ ASB/RPD-or-positive-lowmod-exit
+ Annulus-Rough-or-negative-lowmod-exit
+ Signed-LowMod-Bridge
=> Row(q).
```

新增 `docs/monograph/prime-matrix-signed-lowmod-bridge-hard-attack.md` 后，`Signed-LowMod-Bridge` 被精确端点化：

\[
D_T(I)=
\sum_{d\mid P_T}\mu(d)
\left(\{(L-1)/d\}-\{R/d\}\right).
\]

完整 `q` 行上该端点场随行号 `s` 变成单位旋转 sawtooth 动力系统。已严格完成的是 `large D_T => large low-mod endpoint projection`；最后仍需证明 `SESE-low`：

```text
large endpoint sawtooth projection
=> q-rotation + CRT rigidity contradiction.
```

新增 `docs/monograph/prime-matrix-directed-endpoint-crtdefect-bridge.md` 后，上一步已严格桥接到命名出口：

```text
large endpoint sawtooth projection
=> Directed Endpoint CRTDefect / OSPC*.
```

再新增 `docs/monograph/prime-matrix-dec-ospc-exclusion-hardpoint.md` 后，出口排斥的审稿边界更清楚：单个 `Directed Endpoint CRTDefect` 不能仅由完整 CRT 周期零均值排除，因为零均值只保证全周期相消，不排除单个短窗口锯齿端点尖峰。当前最终硬点应写为：

```text
DEC/OSPC* bad window
=> Persistent DEC
   or Single-window Anchor Escape contradiction.
```

其中 `Persistent DEC` 可推出坏行指示函数的非零 Fourier/CRT 缺陷；`Single-window Anchor Escape` 要证明孤立坏窗不能同时消灭旧核心素数与壳层旧筛幸存者。因此递推路线当前最短候选闭合链更新为：

```text
Row(p)
+ ASB/RPD unless positive DEC/OSPC*
+ Annulus-Rough unless negative DEC/OSPC*
+ PDEC-or-SAE exclusion
=> Row(q).
```

零行延迟路线见 `docs/monograph/prime-matrix-zero-row-crt-audit.md` 与 `docs/monograph/prime-matrix-zero-row-delay-recursive-lemma.md`。实验到 `p<=2000` 未发现 `q×q` 中旧 `p`-筛 `q` 行失败；对 `p<=200` 的 `p` 对齐零行扫描中，已找到的首个零行均晚于 `ceil(q^2/p)`。严格可用的引理是 `QSurv(p,q)=>Row(q)`，即每个 `q` 行含旧筛幸存者且不只含 `q^2` 时，`Row(q)` 成立。审稿边界是：`p` 对齐零行延迟不能单独推出 `QSurv`，因为多数 `q` 行跨越 `p` 行边界；若 `QSurv` 失败，仍需接入 `PDEC-or-SAE` 排斥。

进一步硬点定位见 `docs/monograph/prime-matrix-qsurv-grid-gap-hardpoint.md`。`QSurv` 失败等价于某个素数间隙覆盖完整 `q` 网格行；这不是普通最大素数间隙问题。`docs/monograph/prime-matrix-qsurv-gap-structure-audit.md` 到 `p<=5000` 显示零 `q` 行为 `0`，但最薄行可只有一个素数，且普通 `prime_gap/q` 可超过 `1` 而不导致空网格行。因此最终命题应写为 `GJE-SAE`：排除 `q` 网格对齐荒漠，或证明它必触发 `PDEC-or-SAE`。

新增 `docs/monograph/prime-matrix-gje-sae-terminal-band-decomposition.md` 后，`GJE-SAE` 的真正硬核进一步定位在终端带。若只用一般短区间输入 `SI(theta,C)`，第 `s` 行可覆盖条件为 `C((s-1)q)^theta<=q`，所以 `theta>1/2` 只能覆盖低行段，无法处理 `s≈q`。终端行用 `m=q^2-n` 镜像后变成非零指定类 CRT 覆盖：

```text
[(h-1)q,hq-1] subset union_{ell<=p} {m: m == q^2 mod ell}.
```

因此当前最终接口应写成 `Terminal-SAE/PDEC`。

新增 `docs/monograph/prime-matrix-terminal-sae-split-inequality.md` 后，`Terminal-SAE` 可进一步由分层不等式排除。令 `y=max(2,floor(p/e))`，定义低筛骨架 `G_y(h)` 与尾命中重数 `T_y(h)`。若

```text
G_y(h) > T_y(h)
```

则尾素数 `y<ell<=p` 不可能覆盖全部低筛骨架点。`docs/monograph/prime-matrix-terminal-sae-split-audit.md` 到 `p<=1000` 显示所有终端镜像块均满足该正余量。因此当前最终接口再压缩为 `TSI-or-PDEC`：证明分层余量不等式，或证明余量失败触发持续端点缺陷。

进一步地，`docs/monograph/prime-matrix-terminal-tail-cofactor-identity.md` 把尾命中写成精确互补因子恒等式：

```text
q^2 - m = ell * t,   y < ell <= p,   P^-(t)>y.
```

对 `y=max(2,floor(p/e))`，这些 `t` 落在常数长度区间中；`docs/monograph/prime-matrix-terminal-tail-cofactor-audit.md` 到 `p<=1000` 显示最大区间长度为 `4`，复合 `y`-rough 互补因子最后出现在 `p=19`。因此 `T_y(h)` 的证明义务再压成极短互补素数窗口总和上界。

新增 `docs/monograph/prime-matrix-terminal-sae-cancellation-identity.md` 后，`TSI` 的差值进一步精确为

```text
G_y(h)-T_y(h)=sum_{P^-(n)>y}(1-omega_tail(n)).
```

这使所有一尾因子项严格抵消；当前最终接口从一般骨架/尾命中估计压缩为 `RCI/PDEC`：证明无尾储备数大于多尾碰撞超额，或证明该失败触发持续端点/尾锚缺陷。`docs/monograph/prime-matrix-terminal-sae-cancellation-audit.md` 到 `p<=1500` 仍无失败，并确认该余量不依赖 `n=1,q^2` 端点。

## 3. TP 链的最短当前链条

### 3.1 正确的链条分层

二点筛 A/B 的完整链应分成两段：

```text
结构/容量段:
TP-1 two-point rough pair
=> TP-2 TLI
=> TP-3 BST
=> TP-4 BST-2
=> TP-5 BMD

分布输入段:
TP-5 BMD
<= TP-6 WBE2
<= TP-7 BE2-3
<= TP-8 BE2-3K
<= TP-9 KLS-window.
```

后一段在引用 DI/BFI/Kuznetsov 型外部深定理时可以标注为外部输入版闭合；前一段仍必须审查 `BMD=>BST-2=>BST=>TLI` 是否隐藏了筛余下界或 parity gap。

### 3.2 当前最小硬点

TP 当前最小硬点不是重新证明 `BMD`，而是：

```text
BMD-to-TLI no-hidden-lower-bound audit.
```

它要逐行证明：

1. `BMD` 控制的是双素乘法曲线的有符号分布误差；
2. `BST-2` 使用的 `Y`-rough 剩余主项不是从目标素数对结论反推；
3. Buchstab 转移只使用已证的筛主项、奇异因子和外部分布输入；
4. `TLI` 的总大因子命中严格小于真实剩余候选数。

如果这四点闭合，则外部深定理版 TP 可以升级为：

```text
External-theorem closed candidate.
```

若其中任一点失败，缺口应命名为：

```text
Buchstab-transfer parity gap.
```

### 3.3 `q|w` 刚性的正确位置

当奇素数 `q|w` 时，二禁类 `{0,w}` 合并为一禁类，局部因子由

\[
1-\frac2q
\quad\text{改为}\quad
1-\frac1q.
\]

这给出奇异因子增益

\[
\prod_{q|w,\ q>2}\frac{q-1}{q-2}.
\]

但它只改善固定 `w` 的常数和阈值，不能替代 `w=2` 的最硬情形。因此 TP 的无条件化审查必须先闭合 `w=2`。

## 4. RH 链的最短当前链条

### 4.1 必须保留的状态边界

RH 链当前只能写成：

```text
RH-1 explicit-formula entrance
=> RH-2 CRT field transfer
=> RH-3 controlled exits
=> RH-4 no-cycle ledger
=> RH-5 final RH promotion.
```

其中 `RH-5` 仍为 `Not claimed`。方阵和二点筛刚性可以帮助构造 ledger，但不能自动证明 RH。

### 4.2 controlled exits 四列表

RH 的下一步不是扩展更多出口名称，而是把每个出口写成同一格式：

| 出口 | 输入异常 | 输出吸收 | 使用定理 | 常数账本 |
| --- | --- | --- | --- | --- |
| sparse | 稀疏孔洞/低密异常 | hole/OV 吸收 | 组合容量或大筛 | `C_sparse` |
| dense | 密集投影异常 | projection/FCT/DSO 吸收 | 平方函数或投影正交 | `C_dense` |
| tail | Fourier/Vaaler 高尾 | 尾界吸收 | 截断、平滑、显式公式 | `C_tail` |
| internal | 出口循环 | no-cycle/Lyapunov | 有限下降势函数 | `C_cycle` |

每个出口都必须证明

\[
\text{Load}_{\rm exit}\le \text{Capacity}_{\rm exit},
\]

并且

\[
C_{\rm sparse}+C_{\rm dense}+C_{\rm tail}+C_{\rm cycle}<C_{\rm zero\ anomaly}.
\]

### 4.3 RH 的更强优化方向

若要进一步接近顶刊标准，应尝试把多出口账本压成一个正性准则：

```text
离线零点
=> 某个显式二次型/能量泛函为负
=> CRT/prime ledger 证明同一泛函非负
=> 矛盾。
```

这一路线比逐个出口更集中，但目前尚未构造出完整正性泛函。因此现阶段最稳妥任务仍是 controlled exits 四列表。

## 5. 三链共同常数账本

三个命题若要向无条件化证明闭合，必须共享一个“常数账本”规范：

| 项 | PM | TP | RH |
| --- | --- | --- | --- |
| 平滑截断 | `Phi` 与 `Phihat` | Buchstab/Rosser 平滑 | explicit formula test function |
| 权重 | Selberg `lambda/omega` | well-factorable sieve weights | prime/CRT ledger weights |
| 频率尾 | `QLOW-MID-TAIL` | Kloosterman/Fourier tail | Vaaler/Fourier tail |
| 外向舍入 | `QLOW-MID-COMP` | finite local constants | exit constants |
| 外部输入 | 可选 RSE/平均定理 | DI/BFI/Kuznetsov | explicit formula/zero-free-free identities |

优化要求：每条链内部不得混用不同 convention；跨链引用时必须标明“作为结构解释”还是“作为定理输入”。

## 6. 下一步最优攻坚顺序

按可闭合性和对全稿影响排序：

1. **PM：区间化 `QLOW-MID-COMP`。** 这是当前最窄、最具体、可直接证书化的单点。
2. **PM：把 `RRD/OSPC` 放入同一常数余量表。** 这是 PM 从证书接口走向无条件候选的关键。
3. **TP：做 `BMD=>TLI` 无隐藏下界逐行审查。** 这决定二点筛是否能从外部深定理版 BMD 推到终局。
4. **RH：controlled exits 四列表。** 先形式化，不宣称 RH 终局。

当前最优不是同时硬攻三个终局，而是先把 PM 的三个窄接口压成一个显式常数余量表；它最接近可完全检查，也能为 TP/RH 提供可复用的证书化写法。

## 7. 本轮结论

三个命题的逻辑链已经可以统一优化为：

```text
PM: QLOW-MID-COMP(intervalized)+RRD+OSPC
TP: BMD-to-TLI no-hidden-lower-bound
RH: controlled exits four-column ledger
```

其中 PM 的单点最窄、最适合作为下一步实际突破；TP 是外部深定理版与终局素数对之间的审稿断点；RH 仍是 verification package，必须保持 `Not claimed`。
