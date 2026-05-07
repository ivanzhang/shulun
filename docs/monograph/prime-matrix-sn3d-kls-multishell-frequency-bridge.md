# SN3-D KLS-Multishell 高频频率桥：多壳残余到非零列相位

**状态：** `sn3d_kls_multishell_frequency_bridge_reduction_not_closed`

本文直接攻击 SN3-C 剩下的 `KLS-Multishell`。结论是一个确定性二分：

```text
KLS-Multishell
=> 高频列相位证书
   或 L2-flat clean KLS/dispersion 输入。
```

这一步不是概率统计；它只是对列位移 `d=Py-qm` 上的中心化残余做有限 Fourier 展开。

## 1. 列残余

固定行 `(P,y)` 与若干个 q 壳分离、低模不同步的真分散带 `J`。对列位移

```text
d=Py-qm,     1<=d<P
```

定义合并残余

```text
r(d)=实际命中数(d)-模型命中数(d)。
```

总残余为

```text
E=sum_{1<=d<P} r(d)。
```

若 `E>0` 且想支付 SN-2 余量，则该残余必须要么近似均匀地铺在全部列上，要么在非零列频率上有能量。

## 2. Parseval 二分

令

```text
mu=E/(P-1),
r0(d)=r(d)-mu。
```

对 `h=1,...,P-1` 定义非零列 Fourier 系数：

```text
Rhat(h)=sum_{d=1}^{P-1} r(d) exp(-2 pi i h d/P)。
```

由有限 Parseval，

```text
sum_{h=1}^{P-1} |Rhat(h)|^2
= P * sum_{d=1}^{P-1} |r0(d)|^2。
```

因此存在二分：

```text
HighFrequencyColumn:
  max_{h!=0}|Rhat(h)| >= L_col；

L2FlatKLS:
  sum_d |r0(d)|^2 很小，残余接近均匀，
  进入 clean KLS/dispersion 输入。
```

`HighFrequencyColumn` 是命名出口：它是 `d mod P` 上的非零 Fourier/ColumnCRT 证书。若沿最小反例族持久，频率或有效频率层可由鸽巢固定；若只在孤立窗口发生，则回 `SAE`。

## 3. 与 Kloosterman/dispersion 的关系

若进入 `L2FlatKLS`，则低模、短窗、列频率都已无集中。此时残余对象正是窗口化双线性和：

```text
sum_{m in rough band} sum_{q in I_m}
  (1_{q prime}-model(q,m)) F(m,q),
```

其中 `F` 对短窗、低模 q 相位、低模 d 相位和可见列频率近似正交。要无条件吸收这一项，需要一个 KLS/dispersion 型输入：

```text
CleanMultishellKLS:
  q 壳分离、低模不同步、列频率 L2-flat 的 rough 互补因子短素数区间族，
  其合并中心化误差为 o(R) 或小于当前剩余行余量。
```

若该输入失败，失败本身必须给出新的高频相位、系数集中、端点或短窗缺陷；这些已经回到
`SAE/PDEC/ColumnCRT` 出口。

## 4. 当前审计

配套脚本：

```text
experiments/prime_matrix_sn3d_kls_multishell_frequency_audit.py
```

当前报告：

```text
docs/sn3d_kls_multishell_frequency_audit_20260506.md
docs/sn3d_kls_multishell_frequency_audit_20260506.json
```

结果：

```text
kls_multishell_record_count = 2
max_top_frequency_abs_over_excess = 2.056175
max_partial_fourier_l2_over_excess = 14.275461
min_flatness = 0.004695
max_flatness = 0.014668
```

最紧样本：

```text
P=10007,y=75:
  excess = 24.763520
  flatness = 0.014668
  top frequency h=49
  |Rhat(h)|/E = 1.374721。
```

第二个 KLS 样本：

```text
P=50021,y=128:
  excess = 34.748745
  flatness = 0.004695
  top frequency h=119
  |Rhat(h)|/E = 2.056175。
```

读法：当前两个 `KLS-Multishell` 候选都不是 L2-flat clean KLS 残余；它们已经显示强非零列频率，应回流到高频 `Column/PDEC` 证书，而不是作为无名 KLS 质量保留。

## 5. SN3-D 后的闭合口

SN3-D 把最后硬点压成：

```text
1. 排斥 HighFrequencyColumn/PDEC 证书；
2. 或证明 CleanMultishellKLS 输入；
3. 若 CleanMultishellKLS 失败，失败必须返回高频列相位、短窗、低模或系数集中出口。
```

因此当前已经完成的是“无名 KLS-Multishell 不存在”的结构归约；尚未完成的是对高频列相位出口或 clean KLS 外部输入的最终排斥。不能把本文单独标为全局无条件证明。

## 6. SN3-E：高频 Bohr-cap 无循环

新增 `prime-matrix-sn3e-highfreq-bohrcap-no-cycle.md` 与
`experiments/prime_matrix_sn3e_highfreq_bohrcap_certificate.py` 后，`HighFrequencyColumn`
不再作为开放无名出口保留。对 signed 列残余 `r=r_+-r_-`，若非零频率大小为 `L`、总变差为 `V`，则任意 `alpha<1` 有：

```text
r_+(Bohr_+) + r_-(Bohr_-) >= max(0,(L-alpha V)/(1-alpha))。
```

于是高频出口只有三种归宿：

```text
持久 Bohr-cap => PDEC/ColumnCRT；
孤立 Bohr-cap => SAE/endpoint；
无 Bohr-cap => L2-flat CleanKLS。
```

当前两个高频样本在 `alpha=0` 时：

```text
P=10007,y=75,h=49:
  positive cap captures 58.0008% of positive mass；

P=50021,y=128,h=119:
  positive cap captures 52.4712% of positive mass。
```

因此样本层面高频出口已经物化为 Bohr-cap 证书；结构层面它不再能形成无名循环。
