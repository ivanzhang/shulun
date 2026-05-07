# SN-2 迭代缺陷下降：从最小反例到结构矛盾

**状态：** `iterative_defect_descent_framework_not_closed`

本文把 `SN-2 BandPositive` 后的剩余硬点从“继续找数值常数”改写为一个确定性的迭代剥离过程。

核心目标：

```text
假设存在最小早期零行反例；
每一步要么给出直接容量矛盾，
要么固定一个命名缺陷，
要么把问题降到更小尺度/更小素数层；
不存在无名无限逃逸。
```

这不是统计逼近路线，而是一个结构性反证路线。

## 1. 起点：最小反例与 SN 预算

假设 `P` 是最小早期零行反例，行号写为 `x=y-1<P`。取动态底座 `Y` 与远尾分割 `B`。

由 `prime-matrix-self-normalized-tail-dichotomy.md`：

```text
S_Y = 低素骨架；
T_Y = 剩余高素一阶命中；
M = M_{>BY}；
A = A_{>BY}；
C_allow=(S_Y-N_{<=BY})/M；
R=(C_allow-1)M；
E=A-M。
```

关键恒等式：

```text
R-E = S_Y-T_Y。
```

若 `S_Y-T_Y>0`，则容量门直接给素数洞，反例不存在。因此最小反例必须满足：

```text
E >= R。
```

再由 `SN-2 BandPositive`，若二进 `m/y` 带满足

```text
sum_j E_j^+ < R，
```

则反例不存在。所以最小反例必须产生一个 `BandPositive` 失败：

```text
sum_j E_j^+ >= R。
```

这一步已经把零行反例压成“正二进带超额账本”，而不是固定常数问题。

## 2. 迭代状态对象

定义一个迭代状态：

```text
State = (P,y,Y,B;  band J; q-window Q; modulus W; displacement side; certificate tau)
```

它携带一个责任质量：

```text
Mass(State)=E_State^+。
```

每一步只允许四种操作：

```text
Split-q-window：把 q 壳分成短窗；
Promote-modulus：把 W 提升到 W*r；
Project-column：登记 d=Py-qm 的列位移类；
Descend-layer：把覆盖证书 tau 投影到下层 TotalDescent-TM。
```

每个操作都有单调量：

| 操作 | 单调量 | 不可能无限逃逸的原因 |
|---|---|---|
| Split-q-window | `q` 窗长度严格缩小 | 缩到长度 `<1` 后成为有限 `SAE` 证书 |
| Promote-modulus | `W` 增加新素因子 | 若相位持续集中，给非零 Fourier/PDEC；若不集中，则被分散吸收 |
| Project-column | 固定非零 `d mod r` 位移 | 持久位移给 `ColumnCRT`；不持久则不再支付覆盖 |
| Descend-layer | 素数层从 `P` 降到 `h<P` | 强归纳下降到 `p=2` 矛盾；首阻断是 grid-fail seam |

因此不存在“同一复杂度、同一尺度、同一相位”的循环。

## 3. 主迭代二分

从最小反例得到的正带集合开始。

### Step 1：带级正部门

若

```text
sum_j E_j^+ < R，
```

直接矛盾。

否则选一个责任带 `J`，满足

```text
E_J^+ > 0。
```

### Step 2：短窗门

把该带对应的反向 `q` dyadic 壳分成短窗 `Q_i`。

若某个短窗承担固定比例正超额：

```text
E_{J,Q_i}^+ >= eta_Q E_J^+，
```

则进入 `Split-q-window`。重复此过程，`q` 窗长度严格下降。若持续发生，有限步后窗口只含有限个素数点，成为 `SAE` 证书对象。

若没有短窗集中，则该带通过短窗分散门。

### Step 3：相位门

对当前分散带检查低模单位相位：

```text
q mod W,    d=Py-qm mod W。
```

若某个非平均相位持续承担正超额，则 `Promote-modulus`：

```text
W -> W*r。
```

若提升后仍在新层相位集中，则 Parseval/Fourier 给 `PDEC`；若集中落在列位移类，则进入 `ColumnCRT`。

若每层提升都不集中，则低模相位不支付该带，进入分散大筛门。

### Step 4：分散大筛门

剩余状态同时满足：

```text
无短 q 窗集中；
无 q mod W 低模集中；
无 d mod W 列位移集中；
正带质量仍必须支付零行预算。
```

这时目标不是继续调常数，而是证明一个结构型不等式：

```text
DistributedBandLargeSieve:
E_State^+ <= U_State,
sum U_State < R。
```

若成立，回到 Step 1 矛盾。

若失败，则失败本身就是能量集中定理的反面：由大筛对偶，必存在短窗、低模频率或列位移方向承载过大能量。这三类已经分别回到 Step 2/3 的命名出口。

### Step 5：覆盖证书下降门

若一个反例企图避开所有正带缺陷，则其完整覆盖 CRT 证书 `tau` 没有外部缺陷支撑。此时接入：

```text
TotalDescent-TM。
```

若下降成功，得到更小素数层 `h<P` 的早期零行，与最小反例性矛盾；若下降失败，`prime-matrix-rpz-dual-track-closure-route.md` 已将首阻断压成：

```text
grid_fail seam => SAE/PDEC/ColumnCRT。
```

因此下降门也没有无名出口。

## 4. 反例不可能无限迭代的势函数

定义势函数：

```text
Phi = (P, q-window length, -omega(W), unresolved_mass, descent_depth)
```

按字典序理解：

1. `Descend-layer` 使 `P` 降低；
2. `Split-q-window` 使 `q-window length` 降低；
3. `Promote-modulus` 使 `omega(W)` 增大，若持续则给 Fourier/PDEC；
4. `Project-column` 固定位移类，若持久则给 ColumnCRT；
5. 分散大筛若成功，`unresolved_mass` 降低到不足以支付 `R`。

所以一条逃逸链只有两种可能：

```text
有限步命中命名出口；
或有限步容量不足，产生素数洞。
```

无限链若存在，必有某个操作无限重复：

| 无限重复 | 结构矛盾 |
|---|---|
| 无限短窗细分 | 窗长趋于 `<1`，变成有限 SAE |
| 无限模数提升且集中 | 非零 Fourier 能量持久，PDEC |
| 无限列位移同步 | 固定非零位移类持久，ColumnCRT |
| 无限下降 | 素数层严格下降，最终到 `p=2` |
| 无限分散吸收失败 | 大筛对偶给短窗/相位/列位移集中，回到命名出口 |

这就是“可持续迭代必构造反例矛盾点”的逻辑核心。

## 5. 与当前审计的接口

新增审计：

```text
experiments/prime_matrix_sn2_band_structure_audit.py
docs/sn2_band_structure_audit_20260506.md
docs/sn2_band_structure_audit_20260506.json
```

审计不是证明，只用于定位当前最可能的下一引理。

当前 top 风险行结果：

```text
SN-2 正二进带共 163 个；
SAE short q-window candidate = 131；
DistributedBandLargeSieve candidate = 32；
PDEC/ColumnCRT mod30 peak 未触发当前阈值。
```

样本说明：

```text
短窗出口是主要责任；
真正未解释的核心只剩 32 个分散带；
这些分散带的最大单带责任占 R 不超过 0.132524。
```

这支持下一条结构引理：

```text
SN-3 DistributedBandLargeSieve:
若一个正二进带既没有短 q 窗集中，
也没有 q mod W 或 d mod W 集中，
则其正超额不能持续支付 SN-2 所需责任；
若该结论失败，失败对偶必回到 SAE/PDEC/ColumnCRT。
```

## 6. 尚未闭合的精确位置

本文完成的是迭代结构闭合框架，不是最终无条件证明。剩余必须补一条正式不等式：

```text
DistributedBandLargeSieve 或其对偶失败出口定理。
```

一旦该不等式闭合，整条链变为：

```text
最小反例
=> SN-1/SN-2 远尾正带责任
=> 迭代剥离
=> 容量矛盾 或 SAE/PDEC/ColumnCRT 或 TotalDescent
=> 命名出口证书/下降到 p=2
=> 反例不存在。
```

这正是非固定常数、非统计逼近的行命题闭合路线。

## 7. SN-3 接续结果

新增 `prime-matrix-sn3-distributed-band-large-sieve-bridge.md` 与
`experiments/prime_matrix_sn3_distributed_band_projection_audit.py` 后，`SN-2` 留下的
`32` 个分散候选不再直接全部送入高频大筛，而是先过单位类中心化投影。

修正后的低模主项为：

```text
q mod W: W/phi(W) * unit residue count / log(q_m^-)，非单位类主项为 0。
```

审计结果：

```text
max E_J/R = 0.132524
max E_J/sqrt(M_J) = 1.310464
max centered projection peak share = 1.018659
centered route counts = 24 TrueDistributedDLS, 6 ColumnCRT-return, 2 PDEC-return
centered_return_share = 0.75
```

这把 SN-3 进一步拆成：

```text
CenteredLowModReturn:
  中心化 qmod/dmod 峰接近整带 E_J，则回流 PDEC/ColumnCRT；

TrueDistributedDLS:
  q 短窗、qmod、dmod 中心化峰均小的残余，才需要 DLS/KLS 高频吸收。
```

因此下一硬点比原来的 `DistributedBandLargeSieve` 更窄：先排斥中心化低模回流，再证明真正高频残余不能支付 `R`。

新增 `prime-matrix-sn3a-centered-lowmod-return-certificate.md` 后，中心化低模回流已有确定性剥离：

```text
E_beta* >= theta E_J => unresolved <= (1-theta)E_J。
```

当前 `theta=0.75` 的 `8` 个回流候选中，低模峰吸收 `91.6%` 正质量，剩余正质量比例 `8.7%`。在势函数中，这对应 `unresolved_mass` 严格下降；若同一低模峰持久，则直接固定为 `PDEC/ColumnCRT` 出口。

新增 `prime-matrix-sn3b-true-distributed-residual-target.md` 后，剩余真分散质量为：

```text
effective_unresolved_after_sn3a = 440.889774,
max row effective/R = 0.187188。
```

最紧行是 `P=10007,y=75` 的两个真分散带叠加。下一步若高频吸收失败，失败必须进入 `KLS/dispersion` 非零频率缺陷；否则 `unresolved_mass` 继续下降。
