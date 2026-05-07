# SN-3 分散正带大筛桥：从无名超额到对偶缺陷

**状态：** `sn3_distributed_band_large_sieve_bridge_reduction_not_closed`

本文接续 `SN-2 BandPositive` 与 `SN-2 迭代缺陷下降`。目标不是证明某个固定常数，而是把剩余硬点写成一条可审稿的结构桥：

```text
分散正二进带若仍能支付零行预算，
则要么被带级大筛/分散账本吸收，
要么其对偶失败必返回 SAE/PDEC/ColumnCRT/高频 dispersion 输入。
```

## 1. SN-3 对象

固定候选早期行：

```text
P 为奇素数，y=x+1<P，Y=Y(P)，tail cutoff=BY。
```

远尾互补因子反演给出

```text
Py-d=qm,
ceil((Py-P+1)/m) <= q <= floor((Py-1)/m),
q>BY,
m 为 Y-rough。
```

对二进带

```text
J=[2^j y,2^{j+1}y)
```

定义带内索引集

```text
Omega_J={(m,q): m in J, m 为 Y-rough, q in I_m, q<P}。
```

带内中心化权重为

```text
e_J(m,q)=1_{q prime}-1/log(q_m^-),
q_m^-=max(BY, ceil((Py-P+1)/m))。
```

于是

```text
E_J=sum_{(m,q) in Omega_J} e_J(m,q)=A_J-M_J。
```

SN-2 已证明确定性判据：

```text
若 sum_J E_J^+ < R(P,y)，则该行不是零行。
```

因此 SN-3 只处理 `E_J>0` 的责任带，并把它们分成命名集中出口与分散候选。

## 2. 有限结构投影

对一个正带 `J` 取结构字典：

```text
q 短窗：        q in Q_i；
q 低模相位：    q mod W；
列位移相位：    d=Py-qm mod W；
m/y 带标签：    J 本身。
```

每个分割桶 `beta` 定义中心化桶超额：

```text
E_beta=A_beta-M_beta。
```

命名出口门为：

```text
ShortWindow:
  max_i E_{J,Q_i}^+ 占 E_J^+ 固定比例；

LowPhase/PDEC:
  某个 q mod W 的中心化正超额占 E_J^+ 固定比例；

ColumnCRT:
  某个 d=Py-qm mod W 的中心化正超额占 E_J^+ 固定比例；

Cofactor-anchor:
  某个 J 的 E_J^+ 本身长期承担 R 的固定比例。
```

若这些门都不触发，称 `J` 为 `SN-3 distributed band`。注意这里的“分散”是结构定义，不是概率假设。

## 3. 有限 Hilbert 桥

令 `D` 为一族分散正带。取符号

```text
sigma_J=1_{E_J>0}。
```

则分散正部总量可写成内积：

```text
sum_{J in D} E_J^+
= < e, F_D >,

F_D(m,q)=sigma_J  当 (m,q) in Omega_J。
```

设 `H_low(W,L)` 是由以下测试函数张成的有限空间：

```text
1_{q in Q_i},      1_{q=a mod W},      1_{Py-qm=b mod W},
```

其中 `L` 是短窗尺度。把 `F_D` 分解为

```text
F_D=Pi_low F_D + F_D^perp。
```

于是有严格二分：

```text
<e,F_D>
= <e,Pi_low F_D> + <e,F_D^perp>。
```

第一项若大，必有某个低维桶超额，回到 `SAE/PDEC/ColumnCRT`。这是有限维投影和鸽巢，不需任何解析估计。

第二项是 SN-3 的真正硬输入：

```text
DistributedBandLargeSieve(W,L):
  |<e,F_D^perp>| <= U_D(P,y;Y,B,W,L)。
```

若能证明

```text
U_D + named_low_projection_budget < R(P,y)-named_band_budget，
```

则分散候选不能支付零行预算。

## 4. 对偶失败必有证书

若 `DistributedBandLargeSieve` 失败，即

```text
|<e,F_D^perp>| > U_D，
```

则由有限维对偶性存在一个测试向量 `G`，满足：

```text
G 与所有 q 短窗、q mod W、d mod W 低维桶正交，
但 <e,G> 异常大。
```

展开 `G` 后，失败只能进入四类：

```text
1. q 方向局部化重新出现
   => 短窗细分，进入 SAE；

2. q mod W 或新增轮层 Fourier 频率持久
   => PDEC；

3. d=Py-qm 的列位移频率持久
   => ColumnCRT；

4. 所有低频均被排除后仍有高频相关
   => 需要 dispersion/Kloosterman 型短窗口输入。
```

因此 SN-3 的诚实结论是：

```text
普通“看起来分散”不能作为证明；
必须给出 DLS/KLS 型估计，或把失败作为可审稿的非零频率证书。
```

## 5. 与迭代下降的接合

SN-3 插入 `SN-2` 的位置为：

```text
最小反例
=> SN-1 远尾必须超预算
=> SN-2 正二进带必须支付 R
=> SN-3:
   ShortWindow / PDEC / ColumnCRT / Cofactor-anchor
   or DistributedBandLargeSieve absorption
   or high-frequency DLS/KLS defect
=> 命名出口排斥或 TotalDescent。
```

这保持了用户要求的“持续可行迭代方法”：

```text
每次失败都不是无名失败；
要么缩短 q 窗，
要么提升 W，
要么固定位移类，
要么转入高频双线性输入，
要么下降到更小素数层。
```

## 6. 当前可审稿硬点

SN-3 之后，剩余不是固定常数，而是下面的输入模板。

**SN3-DLS/KLS 输入。** 对任意最小早期反例、任意动态底座 `Y(P)` 和任意经短窗/低模/列位移门过滤后的分散正带族 `D`，有

```text
|<e,F_D^perp>| <= U_D
```

且 `U_D` 与已命名出口预算之和严格小于自归一化余量 `R(P,y)`。

若该输入失败，则失败必须产生以下证书之一：

```text
SAE short-window certificate；
W-unit PDEC Fourier certificate；
ColumnCRT displacement certificate；
high-frequency dispersion/Kloosterman defect certificate。
```

这就是 SN-3 当前闭合口。它严格推进了主链，但不能标注为无条件证明，除非 `SN3-DLS/KLS` 输入或等价缺陷排斥被逐行证明。

## 7. 本轮审计接口

配套脚本：

```text
experiments/prime_matrix_sn3_distributed_band_projection_audit.py
```

它只审计 `SN-2` 留下的 `DistributedBandLargeSieve` 候选，并输出：

```text
分散候选数量；
max E_J/R；
max E_J/sqrt(M_J)；
q 短窗、q mod W、d mod W 的中心化正桶峰；
按 P 汇总的分散正带总量与能量压力。
```

这些数值不构成证明，只用于定位 `SN3-DLS/KLS` 输入最紧的位置。

当前运行：

```text
docs/sn3_distributed_band_projection_audit_20260506.md
docs/sn3_distributed_band_projection_audit_20260506.json
```

参数为：

```text
P=5003,10007,20011,50021,100003,200003,
alpha=0.43, tail_factor=10, top_n=8, W=30,210。
```

结果：

```text
distributed_candidate_count = 32
diagnostic route counts     = 24 TrueDistributedDLS, 6 ColumnCRT-return, 2 PDEC-return
centered_return_share       = 0.75
max E_J/R                 = 0.132524
max E_J/sqrt(M_J)         = 1.310464
total distributed E       = 561.852711
total distributed M       = 20707.147289
max centered projection peak share = 1.018659
```

重要修正：低模模型必须按 `W` 的单位类条件化。远尾 `q` 是大素数，不能把模型量平均给非单位类；否则会把小素禁止类误读成虚假的巨大 PDEC 峰。脚本现用

```text
q mod W 主项：  W/phi(W) * #{q in I: q=a mod W}/log(q_m^-),  a in U_W；
非单位类主项：0。
```

修正后，SN-2 的 32 个“实际计数分散”候选出现新的二分：

```text
1. 若中心化 qmod/dmod 峰接近或超过 E_J，
   则该带应回流到 PDEC/ColumnCRT；

2. 若 q 短窗峰、qmod 峰、dmod 峰都保持低，
   才是真正需要 SN3-DLS/KLS 吸收的高频残余。
```

最紧责任带仍是：

```text
P=5003,y=34,band=[2y,4y):
  E=8.451, M=91.549, E/R=0.132524,
  qwin_peak=0.293439,
  qmod30_peak=0.232226,
  dmod30_peak=0.348108。
```

最大中心化投影峰来自较大 `P` 的低责任带：

```text
P=50021,y=128,band=[2y,4y):
  E/R=0.032900,
  dmod30_peak/E=1.018659。
```

这说明 SN-3 的下一步应分两级硬攻：

```text
SN3-A CenteredLowModReturn:
  用单位类中心化投影把接近整带超额的 qmod/dmod 峰送回 PDEC/ColumnCRT；

SN3-B TrueDistributedDLS:
  对剩余所有低维中心化峰都小的带，证明高频 DLS/KLS 吸收。
```

## 8. SN3-A 中心化低模回流证书

新增：

```text
docs/monograph/prime-matrix-sn3a-centered-lowmod-return-certificate.md
experiments/prime_matrix_sn3a_centered_lowmod_return_certificate.py
docs/sn3a_centered_lowmod_return_certificate_20260506.md/json
```

把上一节的 `8` 个回流候选升级为证书账本。确定性剥离引理为：

```text
若某个中心化低模桶 beta* 满足 E_beta* >= theta E_J，
则 E_J = E_beta* + E_rest, 且 E_rest <= (1-theta)E_J。
```

因此该带不再作为无名分散质量处理：

```text
q mod W 峰 => PDEC；
d mod W 峰 => ColumnCRT；
剩余正质量 => max(0,E_J-E_beta*)。
```

当前 `theta=0.75` 证书账本：

```text
certificate_count = 8
route_counts = 6 ColumnCRT-return, 2 PDEC-return
total_excess = 132.550671
total_peak_mass = 121.448880
total_peak_mass/total_excess = 0.916245
total_positive_residual_after_peak = 11.587735
residual/excess = 0.087421
```

这说明 SN3-A 已经把中心化低模回流部分的 `91.6%` 正质量命名化；真正留给 SN3-B 的是：

```text
原 24 个 TrueDistributedDLS 候选
+ 8 个回流候选剥离低模峰后的很小正残余。
```

SN3-A 仍不是出口排斥证明；它只是把无名超额转成 `PDEC/ColumnCRT` 证书义务，并严格降低未解释质量。

## 9. SN3-B 真分散残余目标

新增：

```text
docs/monograph/prime-matrix-sn3b-true-distributed-residual-target.md
experiments/prime_matrix_sn3b_true_distributed_residual_audit.py
docs/sn3b_true_distributed_residual_audit_20260506.md/json
```

把 SN3-A 剥离后的剩余质量重新汇总：

```text
original_distributed_excess = 561.852711
effective_unresolved_after_sn3a = 440.889774
removed_by_sn3a = 120.962937
removed_share = 0.215293
```

残余构成：

```text
24 个 TrueDistributedDLS 候选
+ 8 个低模回流带剥离后的正残余。
```

最紧行级责任为：

```text
max_row_effective_unresolved_over_required = 0.187188
```

发生在：

```text
P=10007,y=75:
  effective E = 24.763520,
  true bands = 2,
  lowmod residual = 0。
```

所以 SN3-B 的下一硬点不是低模峰，而是：

```text
同一行多个真分散带的高频正偏差叠加能否持续；
若能持续，必须产生 KLS/dispersion 型非零高频证书；
若不能持续，则剩余质量不足以支付 R。
```

## 10. SN3-C 多带同步分裂

新增：

```text
docs/monograph/prime-matrix-sn3c-multiband-sync-split.md
experiments/prime_matrix_sn3c_multiband_sync_audit.py
docs/sn3c_multiband_sync_audit_20260506.md/json
```

多真分散带叠加进一步分裂为：

```text
q 壳重叠       => SAE；
低模签名同步   => PDEC/ColumnCRT；
q 壳分离且低模不同步 => KLS-Multishell。
```

当前审计：

```text
multi_true_row_count = 3
pair_count = 3
pair_route_counts = 2 KLS-Multishell, 1 LowModSync
```

最紧行 `P=10007,y=75` 满足：

```text
[4y,8y): q=[1237,2444]
[1y,2y): q=[4970,9500]
q_shell_gap = 2525
q_window_cosine = 0
max_lowmod_cosine = 0.432620
route = KLS-Multishell。
```

这把下一硬点压成明确的高频输入：

```text
KLS-Multishell:
  分离 q 壳、无低模同步的多个 rough 互补因子短素数区间，
  不能持续同向超额；
  若持续，则显化为 high-frequency dispersion/Kloosterman 缺陷。
```

## 11. SN3-D 高频列相位桥

新增：

```text
docs/monograph/prime-matrix-sn3d-kls-multishell-frequency-bridge.md
experiments/prime_matrix_sn3d_kls_multishell_frequency_audit.py
docs/sn3d_kls_multishell_frequency_audit_20260506.md/json
```

对 `KLS-Multishell` 合并残余按列位移

```text
d=Py-qm
```

做 `d mod P` 非零 Fourier 展开。有限 Parseval 给出确定性二分：

```text
HighFrequencyColumn/PDEC；
或 L2Flat CleanMultishellKLS。
```

当前两个 KLS-Multishell 候选均显示强非零列频率：

```text
P=10007,y=75:
  top h=49, |Rhat(h)|/E=1.374721, flatness=0.014668；

P=50021,y=128:
  top h=119, |Rhat(h)|/E=2.056175, flatness=0.004695。
```

所以样本链已经不再停留在无名 KLS；它回流到高频 Column/PDEC 证书。全局证明仍需排斥该高频出口，或证明所有 L2-flat clean KLS 残余由 `CleanMultishellKLS` 吸收。

## 12. SN3-E 高频 Bohr-cap 无循环

新增：

```text
docs/monograph/prime-matrix-sn3e-highfreq-bohrcap-no-cycle.md
experiments/prime_matrix_sn3e_highfreq_bohrcap_certificate.py
docs/sn3e_highfreq_bohrcap_certificate_20260506.md/json
```

`HighFrequencyColumn` 进一步被确定性局部化。若非零频率大小为 `L`、signed 残余变差为 `V`，则

```text
r_+(Bohr_+) + r_-(Bohr_-) >= max(0,(L-alpha V)/(1-alpha))。
```

因此高频出口只有：

```text
持久 Bohr-cap => PDEC/ColumnCRT；
孤立 Bohr-cap => SAE/endpoint；
无 Bohr-cap => L2-flat CleanKLS。
```

这使 SN3 链变成真正的无循环迭代：任何反例尝试都要么降低未解释质量，要么固定命名缺陷，要么进入唯一 clean KLS 输入。
