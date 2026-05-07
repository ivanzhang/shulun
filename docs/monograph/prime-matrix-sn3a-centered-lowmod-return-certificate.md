# SN3-A 中心化低模回流证书：从分散候选剥离 PDEC/ColumnCRT

**状态：** `sn3a_centered_lowmod_return_reduction_not_closed`

本文接续 `SN-3 分散正带大筛桥`。目标是把 SN-3 审计中的中心化低模峰从“现象”升级为确定性证书：

```text
若一个正二进带的中心化 qmod/dmod 桶承担固定比例超额，
则该带不再是无名分散带；
它必须回流到 PDEC 或 ColumnCRT，剩余未解释质量严格下降。
```

## 1. 记号

固定候选行 `(P,y)`、远尾底座 `Y,B` 和正二进带 `J`。带超额为

```text
E_J=A_J-M_J>0。
```

对低模 `W` 的分割：

```text
q-phase bucket:      beta=(q mod W=a), a in U_W；
column bucket:       beta=(d=Py-qm mod W=b), b in Z/WZ。
```

令中心化桶超额为

```text
E_beta=A_beta-M_beta。
```

这里 `q mod W` 的模型必须条件化到单位类：

```text
M_{q mod W=a}
= sum_m W/phi(W) * #{q in I_m: q=a mod W}/log(q_m^-),
  a in U_W。
```

非单位类没有主项，因为远尾 `q` 是大素数。

## 2. SN3-A 剥离引理

**引理 SN3-A。** 若存在低模桶 `beta*` 与阈值 `0<theta<1`，使

```text
E_{beta*} >= theta E_J，
```

则

```text
E_J = E_{beta*} + E_rest,
E_rest <= (1-theta)E_J。
```

因此该正带可以确定性分裂为：

```text
NamedLowModMass = E_{beta*}；
UnresolvedMass  = max(0,E_J-E_{beta*})。
```

若 `beta*` 是 `q mod W` 桶，则 `NamedLowModMass` 是 `PDEC` 候选；若 `beta*` 是
`d mod W` 桶，则是 `ColumnCRT` 候选。

**证明。** 直接由分割恒等式

```text
E_J=sum_beta E_beta
```

移项得到。该引理不使用概率估计，也不使用固定全局常数。

## 3. 有限对比下界

SN3-A 还给出可审稿的低模对比强度。

### qmod/PDEC

设 `G=U_W`，`N=phi(W)`。若

```text
E_{q=a0} >= theta E_J，
```

则扣除单位类平均后有

```text
E_{q=a0} - E_J/N >= (theta-1/N)E_J。
```

当 `theta>1/N` 时，存在非平凡低模对比方向。若这类事件沿最小反例族持久，则有限鸽巢可固定 `(W,a0)`，形成 `W-unit PDEC` 证书。

### dmod/ColumnCRT

设 `G=Z/WZ`，`N=W`。若

```text
E_{d=b0} >= theta E_J，
```

则扣除列残基平均后有

```text
E_{d=b0} - E_J/W >= (theta-1/W)E_J。
```

当 `theta>1/W` 时，固定列位移残基 `b0` 携带正超额。若持久发生，则进入 `ColumnCRT`；若只在有限短窗发生，则回到有限证书/SAE 账本。

## 4. 对 SN-3 势函数的作用

在 `SN-2` 的势函数

```text
Phi=(P, q-window length, -omega(W), unresolved_mass, descent_depth)
```

中，SN3-A 的作用是降低 `unresolved_mass` 或固定一个低模缺陷：

```text
E_J  -> max(0,E_J-E_beta*) <= (1-theta)E_J。
```

因此它不能产生同尺度无名循环。重复出现只有两种可能：

```text
固定 qmod 低模峰持久      => PDEC；
固定 dmod 列位移峰持久    => ColumnCRT。
```

这正好接入 `Promote-modulus` 与 `Project-column` 两个迭代出口。

## 5. 当前证书审计

配套脚本：

```text
experiments/prime_matrix_sn3a_centered_lowmod_return_certificate.py
```

当前报告：

```text
docs/sn3a_centered_lowmod_return_certificate_20260506.md
docs/sn3a_centered_lowmod_return_certificate_20260506.json
```

从 `SN-3` 的 `32` 个分散候选中，按 `theta=0.75` 抽出：

```text
certificate_count = 8
route_counts = {
  centered_columncrt_return: 6,
  centered_pdec_return: 2
}
```

账本质量：

```text
total_excess = 132.550671
total_peak_mass = 121.448880
total_peak_mass/total_excess = 0.916245
total_positive_residual_after_peak = 11.587735
residual/excess = 0.087421
```

也就是说，这 `8` 个回流候选中约 `91.6%` 的正超额已经被命名低模桶吸走；剩余正质量约 `8.7%`。

对比强度：

```text
min_peak_share = 0.752736
max_peak_share = 1.018659
min_contrast_share_lower = 0.719284
max_contrast_share_lower = 0.985326
```

所有回流候选当前都在 `W=30`：

```text
ColumnCRT residues: d mod 30 = 29,28,1,4,2,26；
PDEC residues:      q mod 30 = 29,23。
```

这些是诊断证据，不是最终排斥证明。正式证明还需对 `PDEC/ColumnCRT` 出口给出排斥证书，或证明这些低模峰不能沿最小反例族持久。

## 6. 下一硬点

SN3-A 之后，SN-3 的剩余目标变为：

```text
1. 排斥或吸收 8 个 CenteredLowModReturn 型出口；
2. 对剩余 24 个 TrueDistributedDLS 候选证明高频分散吸收；
3. 若高频吸收失败，则由对偶返回新的 SAE/PDEC/ColumnCRT 或 KLS/dispersion 缺陷。
```

其中第一项已经有确定性剥离引理；第二项才是真正的 `SN3-B TrueDistributedDLS`。
