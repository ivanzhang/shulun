# SN3-E 高频 Bohr-cap 无循环：列频率出口的统一归宿

**状态：** `sn3e_highfreq_bohrcap_no_cycle_reduction_not_closed`

本文回应“不要越分越多”的要求：`HighFrequencyColumn/PDEC` 不是新分支，而是 SN3 迭代机中的一个终端命名出口。它只有三种归宿：

```text
持久 Bohr-cap  => PDEC/ColumnCRT；
孤立 Bohr-cap  => SAE/endpoint；
无 Bohr-cap    => L2-flat CleanKLS。
```

## 1. Jordan-Bohr 局部化引理

设 `r(d)` 是列残余，写 Jordan 分解

```text
r=r_+-r_-,
V=sum_d r_+(d)+sum_d r_-(d)。
```

若非零频率 `h` 满足

```text
L=|sum_d r(d)e(-hd/P)|>0，
```

取相位 `zeta` 使

```text
Re zeta sum_d r(d)e(-hd/P)=L。
```

对 `0<=alpha<1` 定义两个 Bohr 帽：

```text
C_+(h,zeta,alpha)={d: Re(zeta e(-hd/P))>=alpha},
C_-(h,zeta,alpha)={d: Re(zeta e(-hd/P))<=-alpha}。
```

则有确定性下界：

```text
r_+(C_+) + r_-(C_-) >= max(0,(L-alpha V)/(1-alpha))。
```

**证明。** 对正测度部分，帽外相位实部至多 `alpha`；对负测度部分，只有反帽能给正贡献，反帽外的 `-Re` 至多 `alpha`。于是

```text
L <= alpha V + (1-alpha)(r_+(C_+)+r_-(C_-))。
```

移项即得。

## 2. 三归宿

该引理把高频列相位变成几何对象：

```text
正帽 C_+:
  实际正残余集中在某个高频列 Bohr 弧中；
  若沿最小反例族持久，固定 (h,alpha,phase bucket) 后给 PDEC/ColumnCRT；
  若只孤立出现，则是 SAE/endpoint 证书。

负反帽 C_-:
  模型过量或端点负残余集中；
  它不能支付零行覆盖，若持久则给反向 PDEC/endpoint 缺陷；
  若孤立则进入 SAE/endpoint。

无帽集中:
  所有非零列频率低，残余 L2-flat；
  进入 CleanMultishellKLS。
```

因此 `HighFrequencyColumn` 不会产生无名循环。它要么固定缺陷，要么降低未解释质量，要么进入唯一 clean KLS 输入。

## 3. 与势函数的关系

SN2/SN3 势函数可统一写成：

```text
Phi=(P, shell_count, lowmod_rank, frequency_state, unresolved_mass, descent_depth)。
```

每一步：

```text
SN3-A 低模峰       => lowmod_rank 增加或 unresolved_mass 下降；
SN3-C 壳重叠       => shell_count 下降，进入 SAE；
SN3-D 非零列频率   => frequency_state 固定，进入 Bohr-cap；
SN3-E Bohr-cap     => PDEC/ColumnCRT/SAE 或 L2-flat KLS；
TotalDescent       => P 下降。
```

若某一步试图无限重复：

```text
同一低模/频率持久  => PDEC/ColumnCRT；
短窗/孤帽反复      => SAE；
clean KLS 反复失败 => 新非零频率或系数集中，回到命名出口；
下降反复           => P 降到 2。
```

这就是一般性结构链条：不是找固定常数，而是证明反例不可能无名循环。

## 4. 当前审计

配套脚本：

```text
experiments/prime_matrix_sn3e_highfreq_bohrcap_certificate.py
```

当前报告：

```text
docs/sn3e_highfreq_bohrcap_certificate_20260506.md
docs/sn3e_highfreq_bohrcap_certificate_20260506.json
```

对两个 SN3-D 高频样本，Bohr-cap 账本显示：

```text
P=10007,y=75,h=49:
  alpha=0: positive cap captures 58.0008% of positive mass,
           total Jordan cap captures 54.6682% of variation。

P=50021,y=128,h=119:
  alpha=0: positive cap captures 52.4712% of positive mass,
           total Jordan cap captures 51.6210% of variation。
```

这说明当前高频样本不是平坦噪声，而是可以物化为 Bohr-cap/PDEC/ColumnCRT 证书的相位集中。

## 5. 诚实闭合边界

本文闭合的是“高频出口无名循环”的逻辑：

```text
HighFrequencyColumn 不再是开放形态；
它必须成为 Bohr-cap/PDEC/ColumnCRT/SAE，
或退化为 L2-flat CleanKLS。
```

但最终无条件行命题仍需以下至少一项：

```text
1. 排斥所有持久 Bohr-cap/PDEC/ColumnCRT 证书；
2. 证明 CleanMultishellKLS 输入；
3. 或证明 TotalDescent 在无上述缺陷时必下降到底并矛盾。
```

所以当前最合理的“全局闭合”表述是条件闭合/无名逃逸闭合，而不是已经完成无条件终局证明。
