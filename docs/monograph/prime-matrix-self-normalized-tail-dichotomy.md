# 自归一化远尾二分：无固定常数的容量闭合接口

**状态：** `self_normalized_tail_dichotomy_reduction_not_closed`

本文把第 `P` 列锚点容量路线从固定常数付款升级为行内自归一化预算。结论不是“证明某个常数永远成立”，而是：

```text
若早期零行存在，则远尾互补因子短素数区间必须超过本行真实可付款余量；
任何超过余量的方式都必须进入可命名的 m-band / 相位 / 列位移 / 递归下降出口。
```

## 1. 记号

令 `P` 为奇素数，考察早期行 `x<P`，写

```text
y=x+1,    n_d=Py-d,    1<=d<P。
```

取任意动态底座 `Y=Y(P)`，定义低素骨架

```text
S_Y(P,y)={d: n_d 不被任何 q<=Y 的素数整除}。
```

把剩余高标签分成近端与远尾：

```text
N_{<=BY}(P,y) = q in (Y,BY] 对 S_Y 的一阶命中数，
A_{>BY}(P,y) = q in (BY,P) 对 S_Y 的一阶命中数。
```

其中 `B>1` 可随证明阶段选择，不要求固定为全局常数。远尾模型写为

```text
M_{>BY}(P,y)=sum_m |I_m|/log(q_m^-)，
```

这里 `I_m` 来自互补因子反演：

```text
ceil((Py-P+1)/m) <= q <= floor((Py-1)/m)。
```

定义本行自归一化允许量：

```text
C_allow(P,y)= (|S_Y(P,y)|-N_{<=BY}(P,y)) / M_{>BY}(P,y)。
```

若 `M_{>BY}=0`，则远尾不存在，判据退化为近端容量判据。

## 2. 严格预算引理

**引理 SN-1。** 若第 `x=y-1` 行是零行，则

```text
N_{<=BY}(P,y)+A_{>BY}(P,y) >= |S_Y(P,y)|.
```

因此，当 `M_{>BY}>0` 时，

```text
A_{>BY}(P,y) >= C_allow(P,y) * M_{>BY}(P,y)。
```

**证明。**
`S_Y` 中的每个 `d` 已经避开所有 `q<=Y`。若整行零行，则每个这样的 `d` 必须由某个高标签 `Y<q<P` 覆盖。高标签覆盖并集大小等于 `|S_Y|`，而一阶命中数 `N+A` 至少等于并集大小，所以 `N+A>=|S_Y|`。移项并代入 `C_allow` 即得结论。

这个引理是完全确定性的；不使用素数分布概率，也不使用固定付款常数。

## 3. 远尾超额方程

由 SN-1，早期零行必满足

```text
sum_m pi(I_m) >= C_allow(P,y) * sum_m |I_m|/log(q_m^-)。
```

等价地，

```text
sum_m (pi(I_m)-|I_m|/log(q_m^-))
>= (C_allow(P,y)-1) M_{>BY}(P,y)。
```

这就是新的硬点。它不要求证明 `A/M<=1.05`，而要求证明：

```text
若上述超额成立，则超额不能保持无名状态。
```

还有一个重要的恒等式。记

```text
E_tail=A_{>BY}-M_{>BY},
R=(C_allow-1)M_{>BY}。
```

则

```text
R-E_tail
= (|S_Y|-N_{<=BY}-M_{>BY})-(A_{>BY}-M_{>BY})
= |S_Y|-N_{<=BY}-A_{>BY}
= |S_Y|-T_Y。
```

也就是说：

```text
自归一化尾项缺口 = 原始斜线容量余量。
```

这把两条路线锁在一起：

```text
若 |S_Y|-T_Y>0，则 E_tail<R，零行不可能；
若零行存在，则 |S_Y|-T_Y<=0，也即 E_tail>=R。
```

## 4. 无名超额账本

对互补因子 `m` 可同时按以下结构分桶：

```text
m/y 二进带；
m mod W 或 q mod W；
d=Py-qm 的列位移 mod W；
q 区间短窗；
覆盖证书 tau 的下层投影。
```

于是远尾超额只有两类：

1. **分散型。** 每个桶都低于其允许 envelope。此时总和应由加权大筛、Selberg 或 Rankin 型账本吸收，推出 `A<C_allow M`，与 SN-1 矛盾。
2. **集中型。** 某个桶超过 envelope。该桶直接成为命名出口：

```text
m-band 超额        => cofactor-anchor；
q 短窗超额         => SAE；
低模相位超额       => PDEC；
列位移同步         => ColumnCRT；
证书可剥离且无缺陷 => TotalDescent-TM。
```

这给出“无名逃逸不允许”的形式：

```text
零行 => 自归一化远尾超额；
远尾超额 => 分散吸收 或 命名出口；
分散吸收 => 非零行；
无命名出口 => 递归下降；
下降到底 => p=2 矛盾；
下降阻断 => seam/PDEC/ColumnCRT。
```

## 5. 与当前审计的关系

新增脚本：

```text
experiments/prime_matrix_global_structural_chain_audit.py
```

当前审计：

```text
docs/global_structural_chain_audit_20260506.md
docs/global_structural_chain_audit_20260506.json
docs/global_structural_chain_audit_p5003_fullrows_20260506.md
docs/global_structural_chain_audit_p5003_fullrows_20260506.json
```

审计结果：

```text
P=5003,10007,20011,50021,100003,200003 的 top-16 风险行：
  route_counts = {'capacity_closed': 96}
  near_capacity_boundary = 89
  tail_positive_excess = 51
```

集中峰诊断：

```text
max_m_share:       0.050898  at P=5003,y=33
max_band_share:    0.333333  at P=5003,y=59
max_qmod30_share:  0.150769  at P=5003,y=58
max_dmod30_share:  0.160000  at P=5003,y=58
max tail/model:    1.033097  at P=10007,y=63
```

自归一化阈值诊断：

```text
最紧 P=20011,y=71:
  E_tail=34.759866
  R=146.759866
  R-E_tail=112=S_Y-T_Y

全样本最大 sum_m E_m^+/R = 1.110155
全样本最大 sum_band E_band^+/R = 0.248700
```

解释：单个 `m` 层过细，会把局部正波动放大到超过 `R`；但按 `m/y` 二进带合并后，正超额大幅抵消。这说明当前最有力的证明层级不是单点 `m`，而是带级 signed cancellation。

并且这些峰随 `P` 增大下降明显：

```text
P=5003   max_m_share=0.050898, max_band_share=0.333333
P=200003 max_m_share=0.007967, max_band_share=0.164639
```

这支持一个新的攻击判断：当前样本中的正远尾不是由单个互补因子锚或单个低模相位支撑，而更像可被分散账本吸收的多层小波动。正式证明仍必须把这种“分散”改写为可审稿的不等式。

最紧样本仍是：

```text
P=20011, y=71,
S=2596, T=2484, margin=112,
C_allow=1.107340,
tail/model=1.025423。
```

此外，`P=5003` 的全行版本显示最强风险行仍为：

```text
y=41, S=741, T=695, margin=46。
```

这些只是不构成证明的审计证据；证明目标已经明确缩成 SN-1 后的分散吸收或命名出口排斥。

## 6. 当前最小硬点

下一步不再追固定常数，而应证明以下一般命题之一：

```text
SN-G1. 对任意最小反例，远尾超额若不进入 m-band/SAE/PDEC/ColumnCRT，
       则可由分散大筛账本吸收。

SN-G2. 若分散大筛账本吸收失败，则失败桶沿无限最小反例族持久，
       有有限低模/列位移鸽巢子列，给出 PDEC 或 ColumnCRT。

SN-G3. 若覆盖证书避开上述缺陷，则 TotalDescent-TM 可执行；
       下降到底矛盾，首个下降阻断回到 seam/PDEC/ColumnCRT。
```

这就是目前最接近全局闭合的非固定常数证明接口。

## 7. 分散吸收证书方程

为了避免“分散”停留在描述层，需要把它写成可审稿的证书。

设 `P,y,Y,B` 固定，并令

```text
R(P,y)=(C_allow(P,y)-1)M_{>BY}(P,y)。
```

由 SN-1，若早期零行存在，则远尾超额

```text
E_tail=sum_m (pi(I_m)-|I_m|/log(q_m^-))
```

必须满足

```text
E_tail >= R(P,y)。
```

取任意有限或可求和分桶 `mathcal P`，例如：

```text
m/y 二进带；
m 单点或 m 短块；
q 短区间；
q mod W；
d=Py-qm mod W；
覆盖证书 tau 的下层投影类。
```

记每个桶的超额为

```text
E_beta=A_beta-M_beta。
```

如果能给出外向 envelope `U_beta`，满足

```text
E_beta^+ <= U_beta     for every beta,
sum_beta U_beta < R(P,y),
```

则早期零行不可能。反过来，若早期零行存在，则至少有一个桶满足

```text
E_beta^+ > U_beta。
```

这就是正式的“无名超额消除”：

```text
所有桶都不过量 => 分散吸收 => 矛盾；
某桶过量       => 该桶就是命名出口证书。
```

特别地，对任意分割都有必要条件：

```text
早期零行 => sum_beta E_beta^+ >= R(P,y)。
```

因为 `E_tail=sum_beta E_beta <= sum_beta E_beta^+`。因此可优先尝试证明带级证书：

```text
sum_{dyadic m/y band} E_band^+ < R(P,y)。
```

若该不等式全局成立，则远尾超额不能支付零行；若失败，则失败带自动成为 `m-band cofactor-anchor` 出口。

桶的解释规则：

```text
m 单点/短块过量       => cofactor-anchor；
q 短区间过量          => SAE；
q mod W 过量          => PDEC；
d mod W 过量          => ColumnCRT；
tau 投影不过量但覆盖  => TotalDescent-TM。
```

因此后续证明可以不寻找固定全局常数，而是寻找一套随 `P,y` 自适应的 envelope：

```text
U_beta(P,y) 既足够精确使 sum U_beta < R，
又足够结构化使任何失败桶可被 PDEC/SAE/ColumnCRT/下降账本接走。
```

当前审计的集中峰下降现象说明优先尝试的 envelope 应该偏向多桶能量吸收，而不是单锚容量界。

## 8. SN-2：带级正部证书

令 `mathcal B` 为 `m/y` 的二进分割：

```text
B_j={m: 2^j y <= m < 2^{j+1}y}。
```

对每个带定义

```text
A_j=sum_{m in B_j} pi(I_m),
M_j=sum_{m in B_j} |I_m|/log(q_m^-),
E_j=A_j-M_j。
```

则有确定性充分判据：

```text
若 sum_j E_j^+ < R(P,y)，则第 x=y-1 行不是零行。
```

**证明。**

```text
A_{>BY}=sum_j A_j
       =sum_j M_j + sum_j E_j
       <=M_{>BY}+sum_j E_j^+。
```

若 `sum_j E_j^+<R=(C_allow-1)M_{>BY}`，则

```text
A_{>BY}<C_allow M_{>BY}。
```

这与 SN-1 的零行必要条件矛盾。

因此，对行命题而言，带级主攻目标可以写成：

```text
SN-2-BandPositive:
  对任何最小早期反例行，
  sum_{dyadic m/y band} E_j^+ < R(P,y)
  除非某个失败带触发 cofactor-anchor/SAE/PDEC/ColumnCRT。
```

当前审计给出强支持：

```text
全样本 max sum_j E_j^+/R = 0.248700。
最小带级吸收余量 R-sum_jE_j^+ = 40.980801。
```

这比单个 `m` 层更合适，因为单层正部存在过细账本问题：

```text
max sum_m E_m^+/R = 1.110155。
```

结论：下一步证明不应在单个 `m` 点上硬压所有正波动，而应证明二进带内部的 signed cancellation。若某个二进带内部不抵消，该带就是新的 `cofactor-anchor` 候选，并可继续按 `q` 短窗、`mod W` 相位和列位移细分。

## 9. 带级互反结构

二进带不是任意分桶。若

```text
m in [lambda y, 2lambda y),
```

则 `q` 被锁定在反向 dyadic 区间附近：

```text
q = Py/m + O(P/m)
  roughly in (P/(2lambda), P/lambda]。
```

更严格地，由互补因子反演，

```text
q_min(m)=ceil((Py-P+1)/m),
q_max(m)=floor((Py-1)/m)。
```

所以同一 `m/y` 带的所有远尾命中都落在一个 `q` dyadic 壳内，且 `q` 壳宽与 `m` 带宽互反。

反向求和可写为：

```text
A_j
= sum_{q prime} #{m in B_j:
       ceil((Py-P+1)/q) <= m <= floor((Py-1)/q),
       m 为 Y-rough }。
```

因此带级正部不是孤立短区间素数尖峰，而是两个刚性结构的交：

```text
q 侧：反向 dyadic 素数壳；
m 侧：Y-rough 滑窗；
相位侧：d=Py-qm 落在 [1,P-1]。
```

这给出下一层证明路线：

```text
若 E_j^+ 大，
则 q dyadic 壳内的素数必须持续命中大量 Y-rough 滑窗；
若这种高命中由少数 q 短窗承担 => SAE；
若由固定 q mod W 或 d mod W 承担 => PDEC/ColumnCRT；
若都不承担 => q 壳内分散大筛吸收。
```

这就是 `SN-2` 后的局部二分：

```text
BandPositive failure
=> ShortWindow(q) or Phase(q mod W) or Column(d mod W) or DistributedBandLargeSieve。
```

在证明闭合链中，`DistributedBandLargeSieve` 是下一硬点；其失败出口已经全部命名。

## 10. 迭代缺陷下降接口

新增 `prime-matrix-sn2-iterative-defect-descent.md` 后，`DistributedBandLargeSieve` 不再是孤立估计，而成为一个可迭代反证过程的一环：

```text
BandPositive failure
=> q 短窗细分 / 模数提升 / 列位移投影 / TotalDescent
=> 容量矛盾 或 SAE/PDEC/ColumnCRT 或 p=2 下降矛盾。
```

该过程的势函数为：

```text
Phi=(P, q-window length, -omega(W), unresolved_mass, descent_depth)。
```

每次迭代要么降低 `P`，要么缩短 `q` 窗，要么提升模数并产生 Fourier/PDEC 压力，要么固定位移类并产生 `ColumnCRT` 压力，要么把未解释质量降到不足以支付 `R`。因此它不是数值逼近过程，而是“无名反例必被构造成命名矛盾点”的结构算法。

当前 `experiments/prime_matrix_sn2_band_structure_audit.py` 给出的定位为：

```text
SN-2 正二进带共 163 个；
SAE short q-window candidate = 131；
DistributedBandLargeSieve candidate = 32；
PDEC/ColumnCRT mod30 peak 未触发当前阈值；
分散候选最大单带责任占 R 不超过 0.132524。
```

所以下一条应攻的正式引理是：

```text
SN-3 DistributedBandLargeSieve:
  若正二进带无短窗集中、无低模相位集中、无列位移集中，
  则该带正超额不能持续支付 SN-2 责任；
  若失败，则大筛对偶返回 SAE/PDEC/ColumnCRT。
```

## 11. SN-3：单位类中心化投影修正

新增 `prime-matrix-sn3-distributed-band-large-sieve-bridge.md` 与
`experiments/prime_matrix_sn3_distributed_band_projection_audit.py` 后，`SN-2` 的
`DistributedBandLargeSieve` 候选被进一步细分。

关键修正是：远尾 `q` 是大素数，所以低模模型不能平均分配到 `W` 的所有剩余类，而必须条件化到单位类：

```text
q mod W 主项 =
  W/phi(W) * #{q in I_m: q=a mod W}/log(q_m^-),  a in U_W；
非单位类主项 = 0。
```

同样，`d=Py-qm mod W` 的模型由单位类 `q mod W` 推送得到。这样得到的是中心化低模投影，而不是单纯实际计数峰。

当前审计：

```text
docs/sn3_distributed_band_projection_audit_20260506.md/json
```

给出：

```text
distributed_candidate_count = 32
centered route counts      = 24 TrueDistributedDLS, 6 ColumnCRT-return, 2 PDEC-return
centered_return_share      = 0.75
max E_J/R                 = 0.132524
max E_J/sqrt(M_J)         = 1.310464
max centered projection peak share = 1.018659
```

读法：

```text
实际计数低峰的分散带，中心化后仍可能出现 qmod/dmod 正桶峰；
这些峰若持续接近整带超额，应回流 PDEC/ColumnCRT；
只有所有中心化低维峰都小的部分，才是真正的 SN3-DLS/KLS 高频残余。
```

因此 `SN-3` 的当前最窄证明接口应写成两级：

```text
SN3-A CenteredLowModReturn:
  中心化 qmod/dmod 峰若承担固定比例 E_J，则进入 PDEC/ColumnCRT；

SN3-B TrueDistributedDLS:
  低维中心化峰全小的剩余带由 DLS/KLS 分散估计吸收；
  若吸收失败，对偶非零频率仍返回 SAE/PDEC/ColumnCRT 或高频 dispersion 缺陷。
```

新增 `prime-matrix-sn3a-centered-lowmod-return-certificate.md` 后，第一层回流已有确定性剥离证书：

```text
E_beta* >= theta E_J
=> E_J-E_beta* <= (1-theta)E_J。
```

当前 `theta=0.75` 的证书报告显示：

```text
8 个 SN3-A 回流候选；
6 个 ColumnCRT-return，2 个 PDEC-return；
total_peak_mass/total_excess = 0.916245；
剩余正质量比例 = 0.087421。
```

因此 SN-3 的未解释质量继续下降：低模回流部分被命名出口吸收，真正的分散大筛硬点只剩
`TrueDistributedDLS` 残余。

新增 `prime-matrix-sn3b-true-distributed-residual-target.md` 后，SN3-A 剥离后的残余账本为：

```text
original_distributed_excess = 561.852711
effective_unresolved_after_sn3a = 440.889774
removed_share = 0.215293
max_row_effective_unresolved_over_required = 0.187188
```

最紧行为 `P=10007,y=75`，由 `2` 个真分散带叠加形成，低模回流残余为 `0`。因此
SN3-B 的主攻点是排斥同一行多真分散带的高频同步，或把同步失败送入 `KLS/dispersion`
非零频率证书。
