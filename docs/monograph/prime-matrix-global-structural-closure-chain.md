# 行命题全局结构闭合链：非固定常数版

**状态：** `global_structural_strategy_reduction_not_closed`

本文回应新的路线要求：不要把全局闭合寄托在某个固定常数、固定区段或固定概率模型上，而应从所有已知结构刚性中抽取一条最小反例不能无限逃逸的逻辑链。

核心观点：

```text
固定常数只用于审计和定位风险；
正式闭合应使用自归一化余量、最小反例、递归下降和命名缺陷出口。
```

## 1. 已闭合的严格结构

### 1.1 全量 CRT 与 MinRep 屏障

`prime-matrix-zero-row-full-crt-diagonal-minrep.md` 已证明：

```text
零行
<=> 存在完整覆盖 CRT 证书 tau
<=> x 落在 tau 的 CRT 残基类。
```

首零行在第 `p` 行以后等价于：

```text
所有完整覆盖证书 tau 的最小正代表 r_tau^+ > p。
```

因此任何早期反例都不是模糊统计对象，而是一个具体的完整覆盖标签函数 `tau`，并带有 `r_tau^+<=p` 的 MinRep 缺陷。

### 1.2 第P列圆柱平移

`prime-matrix-pcolumn-anchor-wheel-field.md` 已证明：

\[
xP+c=Py-d,\qquad y=x+1,\ d=P-c.
\]

任意轮 `W` 下，

\[
S_W(P,y)\equiv S_W(P,2)+P(y-2)\pmod W.
\]

所以所有行不是彼此孤立的随机短区间，而是同一个第一行骨架在圆柱面上的平移轨道。

### 1.3 动态轮容量蕴含

`prime-matrix-pcolumn-anchor-dynamic-capacity.md` 已证明：

```text
若 T_Y(P,y)<|S_Y(P,y)|，
则行 y-1 存在素数洞。
```

这里 `Y=P^0.43` 只是当前审计选择；正式结构不依赖固定指数。一般可取任意动态底座 `Y(P)`，只要：

```text
低素底座确定骨架；
剩余高素总命中若小于骨架，零行不可能。
```

### 1.4 远尾互补因子反演

`prime-matrix-pcolumn-nearcutoff-fartail-cofactor.md` 已证明远尾恒等式：

\[
Py-d=qm,\quad q>10Y,\quad 1\le d<P
\]

等价于

\[
\left\lceil {Py-P+1\over m}\right\rceil
\le q\le
\left\lfloor {Py-1\over m}\right\rfloor,
\]

其中 `q` 是素数，`m` 避开所有低素。远尾高素偏差因此不再是无结构噪声，而是 `Y`-rough 互补因子 `m` 上的短素数区间计数。

### 1.5 递归下降

`prime-matrix-total-zero-row-recursive-descent-route.md` 与 `prime-matrix-rpz-dual-track-closure-route.md` 给出两类严格下降对象：

```text
TotalDescent-TM:
  高层零行 => 某个下层 h 的强制零行命中头部或尾镜像。

RPZ-LowerDescent:
  若完整下层行避开端点穿孔，则下层零行成立；
  若下降失败，首阻断是 grid_fail seam，进入 SAE/PDEC/ColumnCRT。
```

若下降到 `p=2`，直接矛盾；若下降阻断，则不产生新自由逃逸，而进入有限相位 seam/PDEC/ColumnCRT 出口。

## 2. 非固定常数的主二分

对任意候选早期零行 `(P,y)`，不固定某个全局常数，而定义本行自归一化允许量：

\[
C_{\rm allow}(P,y)
=
{ |S_Y(P,y)|-T_{\le B Y}(P,y)\over Model_{>BY}(P,y) },
\tag{GSC-1}
\]

其中 `B` 也可随证明阶段选择，不必固定为 `10`。若

\[
T_{>BY}(P,y)
<
C_{\rm allow}(P,y)\,Model_{>BY}(P,y),
\]

则 `T_Y<S_Y`，该行有素数洞。

若失败，则失败不是“常数不够好”，而是具体结构事件：

```text
tail/model >= C_allow(P,y)。
```

把失败写成

\[
\sum_m \left(\pi(I_m)-{|I_m|\over\log q_m^-}\right)
\ge
(C_{\rm allow}-1)Model_{tail}
\tag{GSC-2}
\]

于是必有以下至少一个出口：

1. **cofactor-anchor：** 少数 `m` 或少数 `m/y` 层长期超额；
2. **SAE：** 超额只发生在有限孤立短窗口；
3. **PDEC：** 超额由低模相位反复支撑，产生非零 Fourier/CRT 缺陷；
4. **ColumnCRT：** 超额与第 `P` 列锚残基/列位移同步；
5. **递归下降：** 超额行对应的覆盖证书可剥离到下层零行，最终到 `p=2` 或阻断出口。

这就是非固定常数版本的闭合口：证明 `GSC-2` 的失败必落入命名出口，而不是证明某个固定 `1.05` 永远成立。

## 3. 最小反例不能无限逃逸

假设存在最小早期反例 `P`。取其完整覆盖 CRT 证书 `tau` 中最小代表 `y-1<=P`。

### Step A：容量门

若动态骨架满足

```text
T_Y(P,y)<|S_Y(P,y)|，
```

则反例不存在。

所以最小反例必须满足容量超预算或近等号。

### Step B：互补因子门

容量超预算分解为：

```text
近端 q<=BY 命中 + 远尾 q>BY 命中。
```

远尾由互补因子反演变成 `Y`-rough `m` 的短素数区间总计数。若该总计数未超过自归一化允许量，反例不存在。

所以最小反例必须产生 `m` 层超额。

### Step C：持久性门

若 `m` 层超额只在有限孤窗发生，则进入 `SAE`；若沿无限最小反例族持续发生，则有限相位鸽巢给出固定低模/列位移/互补因子锚：

```text
persistent excess => PDEC or ColumnCRT。
```

所以最小反例不能继续以“无结构波动”逃逸。

### Step D：递归门

若覆盖证书不是由命名缺陷支撑，则它必须在相邻壳层下降中产生下层强制零行，或在第一处失败处产生 seam 阻断。前者下降到 `p=2` 矛盾，后者进入已物化的 seam/PDEC/ColumnCRT 账本。

因此反例只剩：

```text
PDEC / SAE / ColumnCRT / cofactor-anchor
```

这些不是新逃逸，而是证书排斥义务。

## 4. 当前全局硬点排序

按非固定常数逻辑，下一步不应继续问“`1.05` 是否永远成立”，而应攻击以下一般命题：

```text
G1. Self-Normalized Tail Dichotomy
    若 tail >= C_allow(P,y) * Model_tail，
    则存在可命名的 m-band / residue / column displacement defect。

G2. NonHit-Phase Descent
    若容量路线不能直接闭合，正式覆盖证书进入 TotalDescent-TM；
    若 TotalDescent-TM 失败，第一失败相位进入 seam/PDEC/ColumnCRT。

G3. No-Cycle Defect Ledger
    命名缺陷不能重新生成同层无名反例；
    每次要么降低素数层，要么固定一个有限相位/位移/互补因子锚。

G4. Certificate Exclusion
    对 PDEC、SAE、ColumnCRT、cofactor-anchor 分别提交排斥证书。
```

这四项组合后，证明不再依赖某个固定常数，而是依赖：

```text
容量不足 => 有素数洞；
容量超额 => 可命名结构缺陷；
无缺陷 => 递归下降；
下降到底 => p=2 矛盾；
下降阻断 => 命名结构缺陷。
```

## 5. 与“无穷层叠规律”的对应

素数没有单一固定模式，但每一层筛都会留下新的刚性：

```text
低素层：动态轮骨架；
高素层：斜线命中；
远尾层：互补因子短素数区间；
相位层：Fourier/CRT/PDEC；
列位移层：ColumnCRT；
递归层：相邻素数壳下降；
端点层：SAE 或 seam。
```

这不是寻找一个固定公式描述所有素数，而是证明：

```text
任何企图形成早期零行的配置，
必须同时在所有层级同步；
只要某层不同步，就有素数洞；
若所有层同步，则同步本身成为可命名缺陷。
```

这就是当前最适合全局闭合的结构路线。

## 6. 本轮新增：自归一化尾项账本

新增 `prime-matrix-self-normalized-tail-dichotomy.md` 后，固定常数路线被进一步压成严格预算引理：

```text
若第 x=y-1 行为零行，则
N_{<=BY}(P,y)+A_{>BY}(P,y) >= |S_Y(P,y)|。
```

因此当 `M_{>BY}>0` 时，早期零行必然满足

```text
A_{>BY}(P,y) >= C_allow(P,y) M_{>BY}(P,y),
C_allow(P,y)=(|S_Y|-N_{<=BY})/M_{>BY}。
```

这是一个不含固定常数的确定性条件。证明目标变成：

```text
自归一化远尾超额
=> 分散大筛吸收 或 cofactor-anchor/SAE/PDEC/ColumnCRT/TotalDescent 出口。
```

新增 `experiments/prime_matrix_global_structural_chain_audit.py` 物化该路由账本。当前审计
`P=5003,10007,20011,50021,100003,200003` 的 top-16 风险行共 `96` 行，全部为
`capacity_closed`；同时 `P=5003` 全行路由显示最强风险行仍为 `y=41`，`S=741,T=695,margin=46`。

同一账本还给出集中峰诊断：

```text
max_m_share      =0.050898 at P=5003,y=33
max_band_share   =0.333333 at P=5003,y=59
max_qmod30_share =0.150769 at P=5003,y=58
max_dmod30_share =0.160000 at P=5003,y=58
```

到 `P=200003`，这些峰降为：

```text
max_m_share=0.007967, max_band_share=0.164639,
max_qmod30_share=0.130234, max_dmod30_share=0.130667。
```

这说明当前远尾正偏差更像多层分散波动，而不是单个互补因子或单个低模相位锚主导。下一步应优先把
“无锚分散远尾”写成可吸收的大筛/能量账本；若该账本失败，再由失败桶进入 PDEC/SAE/ColumnCRT。

更精确地，设

```text
E_tail=A_{>BY}-M_{>BY},
R=(C_allow-1)M_{>BY}。
```

则恒等式

```text
R-E_tail=|S_Y|-T_Y
```

把自归一化尾项和原始容量余量完全等同。最紧样本 `P=20011,y=71` 中
`E_tail=34.759866`、`R=146.759866`，差值正好为容量余量 `112`。

账本还显示：

```text
max sum_m E_m^+/R      =1.110155
max sum_band E_band^+/R=0.248700。
```

这暴露新的最小硬点：单个 `m` 层太细，正波动会过账；但 `m/y` 二进带层出现强有符号抵消。下一步应优先证明

```text
sum_{dyadic m/y band} E_band^+ < R(P,y)
```

或把唯一失败带送入 `cofactor-anchor/SAE/PDEC/ColumnCRT`。

该判据已经在 `prime-matrix-self-normalized-tail-dichotomy.md` 中命名为 `SN-2 BandPositive`。它是纯确定性充分条件：

```text
A_{>BY}=M_{>BY}+sum_j E_j <= M_{>BY}+sum_j E_j^+。
```

若 `sum_jE_j^+<R=(C_allow-1)M_{>BY}`，则 `A_{>BY}<C_allow M_{>BY}`，与零行必要条件矛盾。当前审计最小带级吸收余量为 `40.980801`，所以后续最优目标是证明带内 signed cancellation 或缺陷化失败带。

新增 `prime-matrix-sn2-iterative-defect-descent.md` 后，下一硬点被组织成势函数下降：

```text
Phi=(P, q-window length, -omega(W), unresolved_mass, descent_depth)。
```

从最小反例出发，若 `SN-2` 失败，则每次迭代只能：

```text
缩短 q 窗       => 有限步进入 SAE；
提升模数 W     => 持久非零频率进入 PDEC；
固定位移 d     => 持久位移进入 ColumnCRT；
投影覆盖证书 tau => TotalDescent 到 p=2 或 grid_fail seam；
分散吸收       => 未解释质量不足以支付 R。
```

因此“继续迭代”本身就是构造矛盾点的算法，而不是统计逼近。当前 SN-2 带结构审计中，
`163` 个正带被分成 `131` 个短窗候选和 `32` 个分散大筛候选；下一正式目标为
`SN-3 DistributedBandLargeSieve` 或其对偶失败出口定理。

该结果仍是审计证据，不是最终证明；但它确认了当前最窄硬点已经不是固定常数，而是
`Self-Normalized Tail Dichotomy` 后的“无名远尾超额排斥”。

## 7. SN-3 分散候选的再压缩

新增 `prime-matrix-sn3-distributed-band-large-sieve-bridge.md` 与
`experiments/prime_matrix_sn3_distributed_band_projection_audit.py` 后，上一节的
`32` 个 `DistributedBandLargeSieve` 候选被重新投影到：

```text
q 短窗；
q mod W；
d=Py-qm mod W。
```

关键是低模模型必须使用单位类条件主项：

```text
q 为大素数 => q mod W 只落在 U_W；
模型量不能平均给非单位类。
```

默认审计 `W=30,210` 得：

```text
distributed_candidate_count = 32
centered route counts = 24 TrueDistributedDLS, 6 ColumnCRT-return, 2 PDEC-return
centered_return_share = 0.75
max E_J/R = 0.132524
max E_J/sqrt(M_J) = 1.310464
max centered projection peak share = 1.018659
```

因此 SN-3 的实际结构不是单层“分散大筛”，而是：

```text
SN3-A:
  中心化 qmod/dmod 峰若承担固定比例 E_J，
  则进入 PDEC/ColumnCRT；

SN3-B:
  所有中心化低维峰都小的剩余部分，
  才进入真正高频 DLS/KLS 分散吸收。
```

这与全局闭合链兼容：任何远尾超额先被投影成低维命名缺陷；若没有低维缺陷，才要求高频分散估计。失败仍不是无名出口，而是 `SAE/PDEC/ColumnCRT/high-frequency dispersion` 证书。

新增 `prime-matrix-sn3a-centered-lowmod-return-certificate.md` 后，低维命名缺陷的剥离也已账本化：

```text
若 E_beta* >= theta E_J，
则未解释质量从 E_J 降到 max(0,E_J-E_beta*) <= (1-theta)E_J。
```

当前 `theta=0.75` 的 `8` 个 SN3-A 回流候选中，命名峰吸收 `91.6%` 的正质量，剩余正质量仅
`8.7%`。这使全局链更明确：

```text
SN-1/SN-2 需要正带支付 R
=> SN-3 投影
=> SN3-A 低模峰剥离为 PDEC/ColumnCRT
=> 剩余 TrueDistributedDLS 才进入高频吸收。
```

新增 `prime-matrix-sn3b-true-distributed-residual-target.md` 后，高频吸收对象也已精确化：

```text
原分散正质量 561.852711；
SN3-A 剥离后剩余 440.889774；
最大行级剩余责任比 0.187188。
```

最紧行 `P=10007,y=75` 的剩余全部来自 `2` 个真分散带，没有低模回流残余。因此下一全局硬点是证明这类多带高频同步不能持久；若持久，则必须显化为 `KLS/dispersion` 高频缺陷并返回命名出口链。

新增 `prime-matrix-sn3c-multiband-sync-split.md` 后，这个多带高频同步又被压成：

```text
q 壳重叠 => SAE；
低模签名同步 => PDEC/ColumnCRT；
q 壳分离且低模不同步 => KLS-Multishell。
```

最紧 `P=10007,y=75` 正是第三类：两个 q 壳 `[1237,2444]` 与 `[4970,9500]` 相隔 `2525`，
q-window 余弦为 `0`，最大低模余弦仅 `0.432620`。因此全局链当前的最窄未闭合输入是
`KLS-Multishell`，不是固定常数或低模轮筛缺口。

新增 `prime-matrix-sn3d-kls-multishell-frequency-bridge.md` 后，`KLS-Multishell` 又被有限 Fourier
分解为：

```text
HighFrequencyColumn/PDEC 或 L2Flat CleanMultishellKLS。
```

当前两个 KLS 样本的 `d mod P` 非零频率都很强：

```text
P=10007,y=75:  |Rhat(49)|/E=1.374721；
P=50021,y=128: |Rhat(119)|/E=2.056175。
```

因此目前全局链的无名高频残余已经转成命名高频列相位出口；最终仍需排斥该出口，或证明
L2-flat clean KLS 输入。

新增 `prime-matrix-sn3e-highfreq-bohrcap-no-cycle.md` 后，高频列相位出口也不再是无名形态：

```text
HighFrequencyColumn
=> 持久 Bohr-cap/PDEC/ColumnCRT
   或孤立 Bohr-cap/SAE
   或 L2-flat CleanKLS。
```

这给出当前最完整的结构闭合机：

```text
零行最小反例
=> SN-1/SN-2 自归一化正带责任
=> SN3-A 低模剥离
=> SN3-B 真分散残余
=> SN3-C 多带同步分裂
=> SN3-D 高频列相位或 clean KLS
=> SN3-E Bohr-cap 无循环
=> PDEC/ColumnCRT/SAE 或 CleanKLS 或 TotalDescent。
```

因此已经闭合的是“无名逃逸不可能”；尚未无条件闭合的是排斥所有命名出口或证明 CleanKLS/TotalDescent 的最终输入。

## 8. 无名逃逸闭合机

新增 `prime-matrix-unnamed-escape-closure-machine.md` 后，SN-1 到 SN3-E 被合并为统一势函数链：

```text
Phi=(
  P,
  active_shell_count,
  q_window_length,
  -lowmod_rank,
  -frequency_rank,
  unresolved_mass,
  descent_depth
)。
```

每一步要么容量闭合、要么窗口缩短、要么模数/频率 rank 增加并形成命名缺陷、要么未解释质量下降、要么进入 clean KLS、要么下降到更小素数层。因此最小反例不能无限保持无名。

当前可诚实表述为：

```text
无名逃逸闭合：已完成；
命名出口全部排斥：未完成；
最终无条件行命题：仍需完成出口排斥或 CleanKLS/TotalDescent。
```

## 9. 命名出口吸收合同

新增 `prime-matrix-named-exit-absorption-contract.md` 后，第 8 节的输出不再停在一串出口名称，
而是进入统一吸收方程：

```text
最小早期零行反例
=> 容量矛盾
   or Abs(E(P,y))。
```

其中

```text
Abs(E)
in {
  SAE-Cert,
  PDEC-Cert,
  ColumnCRT-Cert,
  CleanMultishellKLS,
  p=2 下降矛盾
}。
```

具体对应为：

```text
Bohr-cap       => PDEC/ColumnCRT/SAE or CleanKLS；
Endpoint seam  => PDEC/ColumnCRT/SAE；
CofactorAnchor => TailAnchor-Cert or PDEC/ColumnCRT/SAE；
TotalDescent   => p=2 contradiction or EndpointSeam。
```

这一步把“层叠轮筛相位刚性”和“圆柱斜线容量余量”合并到同一夹击模型：若多层单位类峰逐层稀释，
则进入高维分散/CleanKLS；若不稀释并持续同步，则形成 `W-unit PDEC` 或 `ColumnCRT`。
合同还补入统一缺陷向量引理：任意持久命名缺陷都可写成有限签名群 `G` 上的零均值测试函数偏斜，
从而由 Fourier 下界进入 generalized `PDEC`；稀疏命名缺陷则进入 `SAE`。
所以后续不应继续寻找新出口，而应完成下列三类终端输入之一：

```text
1. SAE/PDEC/ColumnCRT/TailAnchor 证书排斥；
2. CleanMultishellKLS；
3. 无命名缺陷时 TotalDescent 必下降到 p=2。
```

当前状态升级为：

```text
无名逃逸闭合 + 命名出口吸收合同完成；
终端证书排斥仍未完成。
```

## 10. PDEC 失败也回流

新增 `prime-matrix-pdec-dual-failure-absorption-contract.md` 后，终端 `PDEC-Cert` 的失败形态也被
结构化。若某方向上不能证明 `U_CRT<L_PDEC`，则坏窗计数必在该 Fourier 方向的 cap 中集中：

```text
g(C_alpha)>=(U-alpha M)/(1-alpha)。
```

于是：

```text
持久 cap       => refined PDEC / ColumnCRT；
稀疏 cap       => SAE；
口径不一致     => Multiplicity-Stitching；
没有足够 cap   => 原方向上界成立。
```

这一步的意义是：即使攻 `PDEC` 上界失败，也不会退回无名低模异常，而是产生更窄的帽集中证书。
当前最终闭合仍需排斥这些 refined 出口或证明它们不能无限递归。

## 11. PDEC cap 细化无循环

新增 `prime-matrix-pdec-cap-refinement-no-cycle.md` 后，上一节的 refined `PDEC` 递归也被压住。
固定签名群 `G` 内，cap 细化只是在 `G` 上生成有限 Boolean algebra；每次真细化都增加原子数，
最多发生 `|G|-1` 次。终止原子若为 singleton，则是 explicit `PDEC/ColumnCRT`；若非 singleton
且仍有非零频率，则还能继续切分，矛盾；若无非零频率，则进入 local `CleanKLS` 或对偶上界成立。

若证明需要不断升到更大轮层 `G'`，则不是同层循环，而是：

```text
new-layer PDEC / ColumnCRT
or high-dimensional dispersion / CleanKLS。
```

因此当前全局结构链已达到：

```text
无名逃逸不能循环；
命名出口有统一吸收接口；
PDEC 失败只能 cap 化；
cap 细化在固定层不能无限循环。
```

最终仍需填入终端证书排斥。

## 12. New-layer PDEC 塔熵二分

新增 `prime-matrix-newlayer-pdec-tower-entropy-contract.md` 后，无穷层叠轮筛也被纳入同一结构账本。
沿签名层

```text
G_0<G_1<G_2<...
```

每个新增素因子层的条件偏斜都有熵成本：

```text
H_{n+1}=sum_A g_n(A)/M * sum_b p_A(b)log(p_A(b)/mu_A(b))。
```

于是无限塔二分为：

```text
sum H_n 发散
  => finite/profinite PDEC 或 ColumnCRT；

sum H_n 收敛
  => 新增层偏斜趋零，进入 CleanKLS/DLS；

层间口径不一致
  => Multiplicity/Stitching。
```

这一步把“素数规律无穷层叠”的直觉转成可审稿结构：每一层如果要帮助覆盖，就必须留下可累计相位信息；
若不留下，就只能是高维分散，不能作为零行补洞主力。

## 13. Multiplicity-Stitching 不是终端出口

新增 `prime-matrix-multiplicity-stitching-absorption-contract.md` 后，证书口径问题也被吸收。任何拼接/多重
不一致必须先固定同一个 formal unit：

```text
Omega, tau, weight w, g(a)=sum_{tau(omega)=a}w(omega)。
```

若能证明重复项是独立约束行，则进入 `weighted PDEC`；若不能，则商掉重复坐标，进入
`primitive/physical PDEC` 或 `CleanKLS`；若同一物理候选/列位移/尾锚跨层复用，则复用本身进入
`ColumnCRT/SAE/TailAnchor/CofactorAnchor`。

所以当前终端列表进一步更新为：

```text
explicit/profinite/weighted/primitive PDEC；
ColumnCRT；
SAE；
CleanKLS/DLS；
TailAnchor/CofactorAnchor。
```

## 14. TailAnchor/CofactorAnchor 吸收

新增 `prime-matrix-tailanchor-cofactor-absorption-contract.md` 后，尾锚和互补因子锚也被移出终端列表。
远尾恒等式

```text
Py-d=qm
```

给出 `m/y band`、`m mod Q`、`q mod Q`、`d mod Q/P` 四类签名。若某个签名持久承担正超额，
则是 `cofactor PDEC / low-mod PDEC / ColumnCRT`；若只孤立承担，则是 `SAE-anchor`；
若没有锚同步，则只能进入 `CleanKLS/DLS` 或容量矛盾。

因此终端列表现在压成：

```text
PDEC family: explicit/profinite/weighted/primitive/cofactor；
ColumnCRT；
SAE；
CleanKLS/DLS。
```

## 15. ColumnCRT 并入 displacement PDEC

新增 `prime-matrix-columncrt-displacement-pdec-absorption.md` 后，`ColumnCRT` 也不再作为独立终端。
对列点 `n_c=Hq+c` 和同列素数见证 `pi_c=r_cq+c`，列位移为：

```text
d_c=r_c-H。
```

CD0 给出 `d_c not == 0 mod ell`。若某个非零位移余类 `(ell,d_c mod ell)` 持久过载，
它就是 `displacement PDEC`；若孤立过载，则是 `SAE-column`；若不过载，则作为
`PDEC-Dual-Cert` 的列约束行。

当前终端列表压成：

```text
PDEC family:
  explicit/profinite/weighted/primitive/cofactor/displacement；
SAE family；
CleanKLS/DLS。
```

## 16. SAE 改写为 LocalSurvivorCert

新增 `prime-matrix-sae-local-certificate-reduction.md` 后，`SAE family` 也被改写成局部证书义务。
对孤立坏窗 `I`，设候选点集合为 `C(I)`，各类阻塞者为：

```text
low-factor / tail-cofactor / column / endpoint-seam / core-overlap blockers。
```

若存在 `n0 in C(I)` 不被任何 blocker 覆盖，则给出 `LocalSurvivorCert`，孤窗闭合。若覆盖失败，
承担覆盖的 blocker 必按签名进入：

```text
low-mod/cofactor/displacement/endpoint PDEC；
或更小支撑的 SAE；
或 TotalDescent/RPZ lower descent。
```

固定孤窗内候选集有限，不能无限下降；若同类孤窗沿反例族无限复现，则不再是 sparse，而是 PDEC。

当前终端列表压成：

```text
PDEC family；
LocalSurvivorCert family；
CleanKLS/DLS。
```

## 17. CleanKLS/DLS 证书化

新增 `prime-matrix-cleankls-dls-certificate-contract.md` 后，`CleanKLS/DLS` 被固定为证书对象。
它必须在所有命名缺陷剥离后核验：

```text
K1 ranges；
K2 lowmod orthogonality；
K3 no short-window cap；
K4 no column/Bohr cap；
K5 coefficient L2-flat；
K6 gcd/unit strata；
K7 formal unit consistency。
```

若通过，则提交内部大筛界或明确外部 `KLS/DI/BFI` 输入；若失败，则失败项回流
`PDEC/SAE/Multiplicity`。因此最终主链现在是：

```text
PDEC family；
LocalSurvivorCert family；
CleanKLS/DLS certificates or explicit ExternalKLS input。
```

## 18. 终端三证书总收束

新增 `prime-matrix-terminal-certificate-triad.md` 后，所有终端出口被统一为一个审稿三分：

```text
Persistent => PDEC family certificates；
Sparse     => LocalSurvivorCert family；
Flat       => CleanKLS/DLS certificates or explicit ExternalKLS input。
```

这里 `Persistent` 指同一有限/可升层签名持续承担正比例责任；`Sparse` 指只在孤窗、短弧、端点或有限
列块中出现的局部责任；`Flat` 指低模峰、短窗 cap、列/Bohr cap、尾锚、gcd/unit 异常和 formal
unit 混合都已剥离后的平坦残余。

三类失败项也被固定回流：

```text
PDEC fail       => cap localization => refined PDEC / LocalSurvivor / CleanKLS；
Local fail      => blocker复现成PDEC，或支撑缩小，或TotalDescent seam；
CleanKLS fail   => admission/dual failure => PDEC / LocalSurvivor / Multiplicity回流。
```

因此当前全局结构链的最强形式是：

```text
早期零行最小反例
=> 统一覆盖账本
=> 持久/稀疏/平坦三分
=> PDEC / LocalSurvivor / CleanKLS 三终端证书
=> 证书失败仍在三终端内回流，无第四出口。
```

这一步完成的是终端接口总收束。仍未完成的是三类证书全集，尤其是：

```text
Triad-A1: 同一坏窗集合的 PDEC capacity upper U_CRT；
Triad-B1: 所有稀疏孤窗的 LocalSurvivor witness；
Triad-C1: clean residual 的统一 L2-flat 大筛界或外部输入。
```

## 19. Triad-A1 同一坏窗容量上界路线

新增 `prime-matrix-triad-a1-pdec-capacity-upper-route.md` 后，PDEC 终端中的最窄硬点被进一步结构化。
`U_CRT` 不能来自背景全集或完整 CRT 周期的均匀性，必须作用在与 `L_PDEC` 相同的坏窗推前计数
`g(t)` 上。可进入上界系统的行只有三类：

```text
Tautology          : 非负性与质量范围；
Attachment         : 已证明 S subset Z 后继承 Z 的相位/块容量；
ConditionalRouting : 违反即进入已剥离出口的条件行。
```

因此 `Triad-A1` 的闭合协议为：

```text
homogeneous split；
Same-Set Law；
phase/block/column/tail compatible rows；
LP/dual upper U_CRT(h,zeta;theta)；
U_CRT<L_PDEC。
```

若失败，必须输出：

```text
AttachmentFail；
PhaseCompatFail；
CapacityInsufficient => DualCap；
RoutingGap。
```

这些失败分别回流到 refined PDEC、LocalSurvivor、PDEC dual-failure/cap 或尚未剥离的命名出口。
这一步仍是路线合同，不是全局 `U_CRT<L_PDEC` 证书。

## 20. Triad-A1 LHB 分支容量骨架

新增 `prime-matrix-triad-a1-lhb-branch-capacity-skeleton.md` 后，A1 中最接近证书化的一支被拆出。
对 `Q=2310` 的 LHB-typed 分支，已有文件给出：

```text
h4-pdec-bad-window-classification-lemma.md:
  非 LHB 型坏窗路由到 SAE/ColumnCRT/ColumnRadius/TailAnchor/Rankin；

h4-pdec-lhb-attachment-lemma.md:
  LHB 型坏窗满足 S subset Z_LHB；

h4-pdec-lhb-multiplicity-cap-certificate.md/json:
  P in {13,17,19,23,29,31,37,43,47} 的 M(t) 投影容量。
```

于是同一坏窗计数 `g(t)` 可合法加入：

```text
g(t)<=M(t)；
sum_{WHOLEDEF}g(t)<=0；
sum_{BRIDGED}g(t)<=0。
```

该分支已闭合的是 `Attachment` 与两个零块容量行；未闭合的是完整
`U_CRT<L_PDEC` 对偶比较，以及有限 P 列表外的符号化扩展。若 LP 最优值仍超阈值，输出支撑相位即
`DualCap`，回到 refined PDEC/LocalSurvivor。

新增 `experiments/prime_matrix_triad_a1_lhb_lp_skeleton.py` 后，LHB LP 骨架已经机器化输出到
`prime-matrix-triad-a1-lhb-lp-skeleton.md/json`。该审计明确一个新的硬阻断：

```text
仅有 g(t)<=M(t) 的 box-only 容量行不能强制 Fourier 抵消；
只要 M(t)>0，单相位支撑就是可行解，且 |g_hat(h)|=mass。
```

因此 A1-LHB 下一步不应继续寻找全局常数，而应补入 `theta` 方向支撑、列位移相位兼容行、
尾/互补因子不可复用行，或直接提交方向弧对偶证书。

新增 `prime-matrix-triad-a1-lhb-direction-support-contract.md` 后，方向支撑被写成正式行：

```text
C_F(kappa)={t:Re F(t)>=kappa}；
g(t)=0 outside C_F(kappa)；
supp(g) subset C_F(kappa) cap supp(M)。
```

这一步把 `box-only` 阻断转成具体相位交集问题。若交集为空则 LHB 分支闭合；若稀疏则进入
LocalSurvivor/explicit PDEC；若持久则进入 refined PDEC/DualCap；若平坦则进入 CleanKLS。

新增 `experiments/prime_matrix_triad_a1_lhb_direction_support_audit.py` 后，默认测试
`C_F=WHOLEDEF union BRIDGED` 在所有 `Q=2310` 已列出 P 上均为 `EmptyCap`。这不是全体 PDEC
闭合，而是确认一个具体子分支：

```text
若 PDEC 方向强制支撑落在 WHOLEDEF/BRIDGED 零容量块，
则 LHB 分支中没有坏窗质量。
```

剩余方向必须提交真实 `F,kappa,C_F` 后再审计交集。

新增 `experiments/prime_matrix_triad_a1_lhb_fourier_cap_scan.py` 后，低模 Fourier 半空间方向的
`C_F cap supp(M)` 被系统扫描。该扫描的作用不是替代真实 PDEC 方向，而是判定方向支撑路线的强弱：

```text
EmptyCap      => 方向分支闭合；
SparseCap     => LocalSurvivor/explicit PDEC；
PersistentCap => 继续 refined PDEC、column/tail rows 或 CleanKLS。
```

若高阈值 Fourier cap 在高 P 上仍多为 Persistent，就说明素数小模层叠产生的 `supp(M)` 已经很密；
必须使用列位移、尾互补因子或更高层结构继续夹击，不能靠单层 Fourier 半空间闭合。

新增 `prime-matrix-triad-a1-fixed-q-density-barrier.md` 后，这个现象被证明为固定相位层的一般屏障：

```text
|A cap C| >= |A| + |C| - Q,  A=supp(M)。
```

当固定 `Q` 上 `A` 变稠时，任何正密度方向支撑都会 persistent。该引理明确排除了“在同一固定
低模层上靠普通 Fourier cap 全局闭合”的路线，强制下一步进入升层 PDEC、列位移、尾互补因子或
CleanKLS。

新增 `prime-matrix-triad-a1-newlayer-lift-pilot.md` 后，升层路线得到第一批可计算验证：

```text
Q=2310 -> Q=30030；
P=17,19,23,29 的 supp(M) 密度下降约 13.00, 4.95, 3.22, 3.20 倍；
WHOLEDEF/BRIDGED 零块方向仍为 EmptyCap。
```

因此固定层屏障不是死路，而是触发 `new-layer PDEC tower` 的条件：新层若重新稀疏，则继续支撑审计；
若不稀疏，则偏斜进入熵账本或平坦 CleanKLS。

## 21. Triad-A1 Lift-A fiber 删除门控

新增 `prime-matrix-triad-a1-newlayer-fiber-deletion-lemma.md` 和
`experiments/prime_matrix_triad_a1_newlayer_fiber_audit.py` 后，升层路线被压成精确恒等式。设
`Q'=rQ`，旧层支撑 `A_Q={t:M_Q(t)>0}`，新层支撑 `A_Q'={u:M_Q'(u)>0}`，并定义

```text
s(t)=#{b: M_Q'(t+bQ)>0}；
N=A_Q' \ pi^{-1}(A_Q)。
```

则无条件有：

```text
|A_Q'| = sum_{t in A_Q}s(t) + |N|。
```

所以若 `N=empty` 且平均 `s(t)/r<1`，新层支撑密度按精确账本下降；若 `s(t)/r` 接近 1 且 fiber
熵接近均匀，则进入 CleanKLS/DLS；若 `N` 非空，则触发 Stitching/坐标商/复用缺陷吸收。

`Q=2310 -> Q=30030` 审计结果：

```text
P={17,19,23,29}；
all_monotone_lift_support=True；
all_classified_resparse=True；
density drop = 13.00, 4.94565, 3.22222, 3.19672。
```

这一步把“固定 Q 变稠后必须升层”的策略变成可迭代门控：

```text
FixedQ Persistent
=> Lift fiber audit
=> FiberDeletion / NewLayerPDEC-entropy / CleanKLS / Stitching。
```

它仍未给出最终 `U_CRT<L_PDEC`，但排除了“升层后无名循环”的一类逃逸：每次升层必须支付删除、
偏斜、平坦或口径不一致中的一种账。

## 22. Triad-A1 Lift-B 投影单调性与两层塔复核

新增 `prime-matrix-triad-a1-newlayer-projection-monotonicity-lemma.md` 后，`Lift-A` 中的
`N` 项在当前 LHB allowed-set 口径下被一般证明消掉。令

```text
B_P=prod_{ell<P}ell；
C_P={R mod B_P: R 对所有列给出小素因子覆盖}；
M_Q(t)=#{R in C_P: R=t mod Q}。
```

若 `Q|Q'|B_P`，则

```text
pi(supp(M_Q')) subset supp(M_Q)。
```

所以同一 `C_P` 的轮筛塔中：

```text
N=empty；
|supp(M_Q')|=sum_{t in supp(M_Q)}s(t)；
density(M_Q')=density(M_Q)*average(s(t)/r)。
```

这把升层门控从四分压成更硬的二分：

```text
FiberDeletion；
NoDeletion => new-layer PDEC entropy or CleanKLS。
```

新增 `experiments/prime_matrix_triad_a1_newlayer_tower_gate.py` 后，两层有限塔已汇总：

```text
2310 -> 30030:  FiberDeletionLayer, min density drop 3.19672；
30030 -> 510510: FiberDeletionLayer, min density drop 6.13889。
```

这仍不是无限塔证明，但它将下一硬点精确化为：

```text
对任意后继新增素因子 r，
若平均 s(t)/r 不持续小于 1，
则必须从 fiber 条件分布提取 KL 偏斜 PDEC；
若 KL 偏斜消失，则进入 CleanKLS/DLS。
```

## 23. Triad-A1 Lift-C 无限塔删除-熵二分

新增 `prime-matrix-triad-a1-infinite-tower-deletion-entropy-dichotomy.md` 与
`experiments/prime_matrix_triad_a1_infinite_tower_budget.py` 后，`Lift-B` 的有限层门控被提升成极限账本。
沿同一 `C_P` 投影塔，设第 `n` 层平均 fiber 幸存率为

```text
a_n = average_{t in A_n}(s_n(t)/r_n)。
```

由投影单调性和 fiber 恒等式：

```text
density(A_N)=density(A_0)*product_{n<N} a_n。
```

定义删除势：

```text
D_n=-log a_n。
```

则严格二分：

```text
sum D_n = infinity
  => density(A_N)->0，进入 Sparse/LocalSurvivor/容量矛盾；

sum D_n < infinity
  => a_n->1，进入 NoDeletion；
     NoDeletion 再按 KL 成本进入 new-layer PDEC 或 CleanKLS。
```

有限预算审计：

```text
P=19: 2310->510510 product survival 0.016031, density drop 62.379；
P=23: 2310->510510 product survival 0.0505539, density drop 19.7809。
```

这一步的结构意义是：允许无穷层叠，但无穷层叠不能免费。每一层要么支付删除势 `D_n`，要么在
NoDeletion 分支支付 KL 信息成本；若两者都趋零，就进入高维平坦 `CleanKLS/DLS`。

## 24. Triad-A1 Lift-D NoDeletion-KL 门控

新增 `prime-matrix-triad-a1-nodeletion-kl-dichotomy.md` 与
`experiments/prime_matrix_triad_a1_nodeletion_kl_gate.py` 后，`Lift-C` 留下的 `NoDeletion` 分支被进一步
规范化。若删除势可求和，则 `a_n->1`，支撑几乎不再被删；此时看正式坏窗质量在新增 fiber 上的
条件分布 `p_{n,t}` 相对结构基准 `mu_{n,t}` 的 KL 成本：

```text
H_n=sum_t g_n(t)/M * KL(p_{n,t} || mu_{n,t})。
```

任意新增层 cap 若持续超过基准质量，就由二元 KL 下界支付正成本。因此：

```text
sum H_n = infinity
  => new-layer/profinite PDEC；

sum H_n < infinity
  => 条件分布趋平，进入 CleanKLS/DLS admission。
```

当前已物化两层的机器门控：

```text
gate_counts={'FiberDeletion': 6}；
current_nodeletion_triggered=False。
```

所以目前还没有进入 `NoDeletion`；但若后续层删除停止，已经没有无名出口，只能走 PDEC 或 CleanKLS。

## 25. Triad-A1 Lift-D 后终端路由

新增 `experiments/prime_matrix_triad_a1_terminal_router.py` 与
`prime-matrix-triad-a1-terminal-reduction-after-liftd.md` 后，A1 new-layer 分支已接入终端三证书路由器。
当前机器路由为：

```text
route_counts={'LiftFiberDeletion': 6}；
triad_counts={'ContinueLiftOrSparse': 6}；
current_terminal_claim=current_layers_all_deleting。
```

解释是：当前已物化层尚未产生可提交的 PDEC 或 CleanKLS 实例，仍在删除势账本推进。若后继层删除势
发散，则支撑密度趋零，回到 Sparse/LocalSurvivor 或容量矛盾；若删除停止，则由 Lift-D 强制进入：

```text
NoDeletionKLPDEC            => Triad-A PDEC；
NoDeletionCleanKLSCandidate => Triad-C CleanKLS；
NoDeletionMixedKL           => refined cap / next layer, then A or C。
```

所以 A1 new-layer 分支当前最窄下一目标不是再找固定常数，而是：

```text
DeletionPotential:
  证明最小反例族的删除势必发散；
  或把失败层输出为 NoDeletion 后交给 PDEC/CleanKLS。
```

## 26. DeletionPotential promoted-prime 必要性

新增 `prime-matrix-triad-a1-deletion-potential-essentiality.md` 与
`experiments/prime_matrix_triad_a1_deletion_potential_profile.py` 后，删除势的来源被进一步局部化。
当 `Q'=rQ` 时，新增素因子 `r` 的每个 fiber residue 只覆盖旧洞集 `H_Q(t)` 的一个 `r`-残基类：

```text
R_b(H)={c in H_Q(t): ((t+bQ-1)P+c)=0 mod r}。
```

该 fiber 幸存当且仅当：

```text
H_Q(t) \ R_b(H) 可由 Tail_{>r} 完成。
```

因此删除率就是 promoted prime residue choice 的必要性比例。当前两层审计显示，大多数
`zero-cover` residue 都死亡，而 `positive-cover` residue 几乎都幸存：

```text
2310->30030:
  P=17 zero-cover survival 0；
  P=19 zero-cover survival 0.062016；
  P=23 zero-cover survival 0.112628；
  P=29 zero-cover survival 0.058824；

30030->510510:
  P=19 zero-cover survival 0.023066；
  P=23 zero-cover survival 0.054514。
```

这说明当前删除势不是统计噪声，而是“新增素因子必须命中旧洞”的结构必要性。下一硬点被压成：

```text
TailIndependentCompletion:
  证明 Tail_{>r} 不能长期在 zero-cover residue 上独立完成旧洞集；
  若能独立完成，则该层已经是 NoDeletion，进入 PDEC/CleanKLS。
```

## 27. TailIndependentCompletion 例外项

新增 `prime-matrix-triad-a1-tail-independent-completion.md` 与
`experiments/prime_matrix_triad_a1_tail_independent_completion_audit.py` 后，上一节的 zero-cover 幸存被拆成
平凡 `H=empty` 与真正非空旧洞的 Tail 独立完成。对非空旧洞集 `H_Q(t)`，有结构界：

```text
surviving residues subset Occ_t union TI_t；
Occ_t={b: promoted prime r 命中旧洞}；
TI_t={b: r 不命中旧洞，但 Tail_{>r} 独立完成 H_Q(t)}。
```

因此：

```text
s(t)/r <= |Occ_t|/r + |TI_t|/r <= |H_Q(t)|/r + |TI_t|/r。
```

当前两层 `TI_t` 审计：

```text
2310->30030:
  P=17 TI rate 0；
  P=19 TI rate 0.062016；
  P=23 TI rate 0.112628；
  P=29 TI rate 0.058824；

30030->510510:
  P=19 nonempty TI rate 0, trivial H=empty survivors 136；
  P=23 TI rate 0.054514。
```

这把下一硬点再压窄为：

```text
HoleResidueOccupancy:
  若 |H_Q(t)|/r 和 |TI_t|/r 都不接近 1，则删除势增长；
  若 |H_Q(t)|/r 接近 1，则旧洞集过密，应触发容量/PDEC；
  若 |TI_t|/r 接近 1，则进入 NoDeletion-KL。
```

## 28. HoleResidueOccupancy 删除势屏障

新增 `prime-matrix-triad-a1-hole-residue-occupancy.md` 与
`experiments/prime_matrix_triad_a1_hole_residue_occupancy_audit.py` 后，上一节中的 `|Occ_t|/r`
已经被物化为旧洞列在 promoted prime `r` 上的 residue 占用：

```text
Occ_t={b: exists c in H_Q(t), ((t+bQ-1)P+c)=0 mod r}；
S_t subset Occ_t union TI_t；
|Occ_t| <= |{c mod r: c in H_Q(t)}| <= min(|H_Q(t)|, r)。
```

当前两层证书给出：

```text
2310->30030:
  P=17 union=0.076923, deletion_lb=0.923077；
  P=19 union=0.202198, deletion_lb=0.797802；
  P=23 union=0.310345, deletion_lb=0.689655；
  P=29 union=0.343590, deletion_lb=0.656410；

30030->510510:
  P=19 union=0.058824, deletion_lb=0.941176；
  P=23 union=0.162896, deletion_lb=0.837104。
```

因此当前升层不是模糊统计删除，而是确定性夹击：

```text
旧洞 residue 占用小；
Tail 独立完成小；
=> 大量 zero-cover fiber 被强制删除。
```

若沿无限层塔删除势最终不能发散，则必须进入：

```text
OccupancySaturation:
  旧洞集在新增 r-residue 上近乎满占用；
  这要求 |H_Q(t)| 近 r，并触发容量/PDEC/ColumnCRT 压力。

TailIndependence:
  promoted prime 在大量 fiber 上非必要；
  这已由 NoDeletion-KL 接入 PDEC/CleanKLS。
```

所以 A1 new-layer 分支的下一硬点进一步缩小为：

```text
HRO-A:
  证明 OccupancySaturation 不能持久保持无名；
  它要么造成低层容量矛盾，要么显化为 PDEC/ColumnCRT。
```

## 29. OccupancySaturation 压力引理

新增 `prime-matrix-triad-a1-occupancy-saturation-pressure.md` 后，`HRO-A` 也被压成平均缺口引理。
若一层中删除几乎停止：

```text
avg |S_t|/r >= 1-delta
```

同时 Tail 独立完成没有接管：

```text
avg |TI_t|/r <= epsilon，
```

则由 `S_t subset Occ_t union TI_t` 必有：

```text
avg |Occ_t|/r >= 1-delta-epsilon。
```

进一步，对任意 `eta>0`：

```text
比例{t: |Occ_t|/r < 1-eta} <= (delta+epsilon)/eta。
```

所以无删除且非 `TI` 的层，必须让多数旧活跃相位达到旧洞 residue 近满占用。又因

```text
|Occ_t| <= |{c mod r: c in H_Q(t)}| <= min(|H_Q(t)|,r)，
```

这强制：

```text
多数 t 满足 |H_Q(t)| >= (1-eta)r，
且旧洞几乎打满 c mod r。
```

该事件只有两个后续：

```text
Tail capacity insufficient:
  多数 fiber 不能完成残余旧洞，删除势继续增长；

Tail capacity sufficient:
  Tail CRT 选择在 (t,b,H_Q(t)) 上出现持久条件同步，
  进入 NoDeletion-KL / PDEC / CleanKLS。
```

这一步把用户提出的“层叠轮筛刚性”接进 A1 new-layer 分支：每一层新增素数都迫使旧洞集通过
`占用小则删除、占用满则容量/KL 缺陷化` 的二分门。

## 30. TailCapacityPressure：近满占用后的容量/KL 吸收

新增 `prime-matrix-triad-a1-tail-capacity-pressure.md` 与
`experiments/prime_matrix_triad_a1_tail_capacity_pressure_audit.py` 后，`OccupancySaturation` 的后续也被
写成确定性 set-cover 门。

对每个 promoted fiber：

```text
Residual_b=H_Q(t)\R_b(H)；
b 幸存 <=> Tail_{>r} 完成 Residual_b。
```

Tail 容量门：

```text
若 |Residual_b| > sum_{ell in Tail} max_a |C_ell(a)|，
则 b 必死。
```

Hall 子集门：

```text
若存在 W subset Residual_b，
|W| > sum_ell max_a |C_ell(a) cap W|，
则 b 必死。
```

KL 门：

```text
若 b 幸存且完成 Tail 选择数为 m_b，
则正式质量相对 Tail 均匀基准支付 KL >= log(M_tail/m_b)。
```

当前两层证书：

```text
consistency_mismatch_count=0；
所有死亡槽位 Hall-certified；
hall_uncertified_dead_slots=0；
非平凡幸存槽位 avg KL floor:
  P=19: 2.771622；
  P=23: 4.937726；
  P=29: 6.996641；
  第二层 P=23: 2.889912。
```

于是 A1 new-layer 删除势链已压成：

```text
Occ+TI 不满
  => 删除势增长；

TI 近满
  => NoDeletion-KL / CleanKLS；

Occ 近满
  => TailCapacityPressure；
     容量失败 => 删除势增长；
     容量成功但完成集合小 => KL/PDEC/CleanKLS。
```

这完成了“旧洞近满占用”这个中间逃逸口的吸收。仍未闭合的是终端证书全集：

```text
PDEC 排斥；
CleanKLS/DLS 大筛；
Sparse/LocalSurvivor 拼接。
```

## 31. TailUnitDensity：容量成功但 KL 不大的再压缩

新增 `prime-matrix-triad-a1-tail-unit-density-kl-floor.md` 与
`experiments/prime_matrix_triad_a1_tail_unit_density_gate.py` 后，`TailCapacityPressure` 的 KL 门获得
不依赖具体残余洞形状的统一下界。

对任一非空 `Residual_b`，取一个洞 `c0`。所有 Tail 素数都不命中 `c0` 的密度为：

```text
u_tail=prod_{ell in Tail}(1-1/ell)。
```

于是：

```text
m_b/M_tail <= 1-u_tail；
KL >= -log(1-u_tail)。
```

当前证书：

```text
all_unit_density_bounds_pass=True；
非空残余洞幸存的实际完成比例均不超过 1-u_tail。
```

这把“容量成功但 KL 不大”的逃逸压成：

```text
非空残余洞幸存 + u_tail 不小
  => 正 KL 成本，进入 PDEC；

非空残余洞幸存质量消失
  => 回到 promoted-prime 删除/空残余洞分支；

u_tail -> 0 且没有命名偏斜
  => Tail 层趋于平坦，进入 CleanKLS/DLS admission。
```

因此 A1 new-layer 分支现在没有中间逃逸口；只剩终端三证书：

```text
PDEC；
CleanKLS/DLS；
Sparse/LocalSurvivor。
```

## 32. Triad-A1 终端无循环账本

新增 `prime-matrix-triad-a1-terminal-no-cycle-ledger.md` 与
`experiments/prime_matrix_triad_a1_terminal_no_cycle_ledger.py` 后，A1 路线中已经物化的中间门被合并成
一个无循环账本：

```text
FixedQZeroBlockDirection:
  零容量块方向在 LHB 分支为空；

FixedQDensityBarrier:
  固定 Q 普通 Fourier cap 出现持久交集；
  不能同层循环，必须升层、加 column/tail 行或进 CleanKLS；

NewLayerTower:
  当前已物化升层均为 FiberDeletionLayer；

HoleResidueOccupancy:
  Occ+TI 不满则删除；趋满则进入 OccupancySaturation/TailIndependence；

TailCapacityPressure:
  残余洞容量/Hall 失败则死亡；容量成功则支付 Tail KL；

TailUnitDensity:
  非空残余洞幸存且 u_tail 不小则支付 KL；
  KL 小只能进入空残余洞或 CleanKLS；

TerminalRouter:
  删除停止强制进入 PDEC/CleanKLS；
  删除发散进入 Sparse/LocalSurvivor 或容量矛盾。
```

机器账本输出：

```text
all_materialized_gates_pass=True。
```

关键读数：

```text
NewLayerTower:
  2310->30030 min drop 3.19672；
  30030->510510 min drop 6.13889；

HoleResidueOccupancy:
  max_union_bound_rate=0.343590；
  min_certified_deletion_lb_rate=0.656410；

TailCapacityPressure:
  all_consistent_with_lift_m_vector=True；
  all_dead_slots_hall_certified=True；

TailUnitDensity:
  all_unit_density_bounds_pass=True。
```

因此当前 A1 分支已经达到：

```text
中间逃逸关闭；
同层循环关闭；
终端三证书仍开。
```

后续不能再停在固定 Q cap、升层口径、旧洞占用、Tail 容量或 Tail KL 的解释层。真正剩余只剩：

```text
PDEC family U_CRT<L_PDEC；
CleanKLS/DLS admission + 大筛证书；
Sparse/LocalSurvivor witness 或 blocker deficit。
```

## 33. Sparse 终端压缩为 LocalSurvivor/PDEC

新增 `prime-matrix-triad-a1-sparse-local-survivor-entry.md` 后，删除势发散后的 `Sparse` 终端也不再是黑箱。

沿升层塔有：

```text
density(A_N)=density(A_0)*prod_{n<N}a_n。
```

若：

```text
sum -log(a_n)=infinity，
```

则 `density(A_N)->0`。这时仍要支撑早期零行，只能出现：

```text
IsolatedSparse:
  坏窗落在有限/短尺度孤立窗口；
  => LocalSurvivorCert；

PersistentSparse:
  某个低模、列位移、尾锚、端点或 seam 模式在无限反例族中复现；
  => PDEC family。
```

因此 A1 的删除势终端进一步压成：

```text
删除势发散 => SparseLocal；
SparseLocal witness 成立 => 零行失败；
SparseLocal 被 blocker 覆盖 => blocker 持久则 PDEC，非持久则更小 LocalSurvivor。
```

这一步把三终端改写为更具体的证书全集：

```text
PDEC family；
CleanKLS/DLS；
LocalSurvivorCert。
```

## 34. PDEC DualCap 失败输出物化

新增 `prime-matrix-triad-a1-pdec-dualcap-route.md` 与
`experiments/prime_matrix_triad_a1_pdec_dualcap_extractor.py` 后，`PDEC family U_CRT<L_PDEC` 的失败形态
已在 `Q=2310` LHB 分支中物化。

若固定 `Q` 对偶比较失败，必须输出：

```text
DualCap = C_{h,alpha,dir} cap supp(M)。
```

当前提取器从 Fourier-cap 扫描中重建最重/最大 cap，得到：

```text
aggregate_class_counts={
  SparseCap: 16,
  PersistentCap: 68,
  ForcedPersistentByDensityBarrier: 24
}

aggregate_route_counts={
  LocalSurvivorOrExplicitPDEC: 16,
  RefinedPDECOrColumnTailRows: 68,
  LiftOrColumnTailOrCleanKLS: 24
}
```

这给出 PDEC 终端的实际下一步：

```text
SparseCap:
  生成 LocalSurvivor witness 或 explicit finite PDEC；

PersistentCap:
  补 refined PDEC / column-tail 相位兼容行；

ForcedPersistentByDensityBarrier:
  固定 Q 层不能同层循环；
  必须升层、加 column/tail 行或进入 CleanKLS。
```

因此 `PDEC` 终端硬点已经从抽象 `DualGap` 推进为具体 cap 路由账本。仍需提交这些路由的最终排斥证书。

## 35. SparseCap 早期出口关闭

新增 `experiments/prime_matrix_triad_a1_sparsecap_local_survivor_audit.py` 与
`prime-matrix-triad-a1-sparsecap-local-survivor.md/json` 后，`DualCap` 中的
`SparseCap => LocalSurvivor/explicit PDEC` 路由已继续压缩为有限相位原子。

审计规则是：

```text
row = phase + Q*y；
y=0 且 phase<=P 代表 P 行以内真实早期行；
若该行不完成，则输出未覆盖列 LocalSurvivor witness；
若完成只发生在 y>0 或 phase>P，则登记为 finite PDEC atom。
```

当前结果：

```text
sparse_descriptor_count=16；
unique_sparse_cap_count=3；
unique_phase_atom_count=26；
early_completion_conflict_count=0；
unique_early_completion_conflict_count=0；
all_sparse_caps_closed_for_pxP=True；
local_survivor_witness_count=1；
unique_local_survivor_witness_count=1；
finite_pdec_atom_count=35；
unique_finite_pdec_atom_count=25。
```

最关键结构读数：

```text
P=13:
  sparse support = [169,702,1609,2142] mod 2310；
  first completion row = 169 = P^2；

P=17:
  唯一 phase<=P 的 sparse 原子为 phase=13；
  y=0 不完成，未覆盖列为 col=7；
  真正完成需要 y=1，row=2323>P。
```

因此在当前 `Q=2310` LHB-PDEC 失败帽中，稀疏分支不能在 `P×P` 早期方阵内形成零行：

```text
SparseCap 早期命中:
  给出 LocalSurvivor witness；

SparseCap 完成态:
  全部发生在 P 之后；
  若无限持久复现，只能作为 finite PDEC / column-tail 输入。
```

这一步直接吻合方阵斜线/圆柱覆盖直觉：`P=13` 的第一个稀疏完整覆盖点正是 `P^2`，而不是 `P` 行以内。剩余硬点继续缩小为：

```text
PersistentCap 的 refined PDEC / column-tail 行；
ForcedPersistentByDensityBarrier 的升层或 CleanKLS admission；
finite PDEC packet 的正式 U_CRT<L_PDEC 比较。
```

## 36. ForcedCap 升层账本化

新增 `experiments/prime_matrix_triad_a1_forcedcap_lift_audit.py` 与
`prime-matrix-triad-a1-forcedcap-lift-audit.md/json` 后，`ForcedPersistentByDensityBarrier`
不再只是“固定层太稠”的诊断。

审计动作：

```text
source Q=2310；
target Q'=30030=13Q；
t mod Q -> t+Q*s, 0<=s<13；
只判定 lift support 是否非空，不计算完整 multiplicity。
```

当前结果：

```text
forced_cap_count=24；
all_old_intersections_recomputed=True；
lift_class_counts={
  LiftPersistentNeedsColumnTailOrNextLift: 24
}。
```

P 级支撑读数：

```text
P=43:
  target support density=0.500433；
  top forced cap lift survival 约 0.56-0.64；
  lift deletion 约 0.36-0.44；

P=47:
  target support density=0.712155；
  top forced cap lift survival 约 0.73-0.83；
  lift deletion 约 0.17-0.27。
```

结构含义：

```text
一层升层没有把 forced cap 直接变成 sparse；
但固定 Q=2310 的密度屏障已经转化为可计量的 fiber 删除账本；
若继续持久，不能回到同层 cap 循环，必须进入 column-tail 行、next-lift、PDECEntropy 或 CleanKLS。
```

这一步关闭的是“ForcedCap 可以在固定 Q 同层反复解释”的逃逸口；它尚未排除这些持久帽本身。当前真正剩余的 PDEC 主硬点已经进一步收缩为：

```text
Persistent/ForcedPersistent cap 的 column-tail 相位兼容行；
或沿升层塔证明 survival 连续产生删除势；
或在持久停止下降时提交 PDECEntropy/CleanKLS 证书。
```

## 37. PersistentCap 的 ColumnTail 支付方程

新增 `experiments/prime_matrix_triad_a1_persistent_columntail_payment_audit.py` 与
`prime-matrix-triad-a1-persistent-columntail-payment.md/json` 后，`PersistentCap` 的
`refined PDEC / column-tail rows` 路由已经从口头标签推进为支付方程。

对每个 persistent cap `C` 定义：

```text
D_C = sum_{phase in C} M(phase) * |H_low(phase)|。
```

这里 `D_C` 是 cap 内所有完成态必须支付的低洞需求。每个低洞必须由某个高素数 residue 覆盖，所以出现无常数的结构二分：

```text
固定 tail / column residue 持久过载
  => TailAnchor / ColumnCRT displacement PDEC；

所有 residue 都分散支付
  => CleanKLS / DLS admission。
```

当前机器审计：

```text
persistent_cap_count=68；
unique_phase_signature_count=1915；
all_intersections_recomputed=True；
all_phase_m_counts_match=True；
route_counts={
  ColumnTailPigeonholeRowOrDistributedCleanKLS: 68
}。
```

P 级有效支撑读数：

```text
P=17: min effective residue support = 7.000；
P=19: min effective residue support = 14.857；
P=23: min effective residue support = 24.774；
P=29: min effective residue support = 28.847；
P=31: min effective residue support = 22.011；
P=37: min effective residue support = 28.352。
```

其中

```text
effective support = total_hole_demand / max_single_bucket_payment。
```

这不是固定全局阈值，而是本层本 cap 自带的分散桶数下界。特别是 `P>=23` 后，单个 residue
只能承担约 `3.5%--4.5%` 的需求；若正式反例族仍要持久复现这些 cap，要么抽出固定 top
支付签名进入 PDEC，要么承认支付跨多 residue/多壳分散并进入 CleanKLS/DLS。

因此 `PersistentCap` 的下一硬点已压缩为：

```text
证明 top 支付签名持久 => 同一 formal unit 的 Tail/Column PDEC；
或证明 top 支付签名不持久 => 多壳分散 CleanKLS/DLS admission。
```

## 38. TopPrime 持久支付被升层吸收

新增 `experiments/prime_matrix_triad_a1_topprime_promotion_gate.py` 与
`prime-matrix-triad-a1-topprime-promotion-gate.md/json` 后，上一节的 `top 支付签名持久`
已经进一步压缩。

关键发现：

```text
68 个 PersistentCap 的 top-prime 支付签名全部等于 13；
13 正是 Q=2310 之外的最小新素数；
all_top_prime_is_next_high_prime=True。
```

因此如果 top-prime 支付持久，正确动作不是保留一个新终端，而是晋升轮筛：

```text
Q'=13Q=30030；
t mod Q -> t+Q*s, 0<=s<13。
```

targeted lift 审计结果：

```text
cap_count=68；
promotion_class_counts={
  PromotionFiberDeletion: 68
}。
```

P 级删除读数：

```text
P=17: survival=0.076923；
P=19: survival in [0.204743,0.238462]；
P=23: survival in [0.327427,0.384615]；
P=29: survival in [0.302294,0.356838]；
P=31: survival in [0.292721,0.414750]；
P=37: survival in [0.239126,0.351648]。
```

结构含义：

```text
top-prime persists
  => promote next prime into Q
  => fiber deletion
  => Sparse/删除势/PDEC 或继续升层；

top-prime does not persist
  => 支付不能固定在一个新素数；
  => 多 residue / 多壳分散，进入 CleanKLS/DLS admission。
```

这正是无固定常数的递归剥离链：每层若出现稳定新素数支付，就把该素数纳入下一层轮筛；
若稳定支付消失，则剩余对象已经趋于多壳分散；若某个 residue/cap 停止分散又持久出现，则回流 PDEC。

于是 `PersistentCap` 的主逃逸进一步缩成：

```text
新素数持续出现 => 升层删除势；
新素数不持续   => CleanKLS/DLS；
固定 residue 持续 => PDEC。
```

## 39. 递归晋升二分

新增 `prime-matrix-triad-a1-recursive-promotion-dichotomy.md` 后，上述结果被整理成一般递归链：

```text
A. top prime persists
   => promote Q to rQ
   => fiber deletion / sparse / next layer；

B. fixed residue or column signature persists
   => TailAnchor / ColumnCRT displacement / refined PDEC；

C. no fixed signature persists
   => 多 prime/residue/column 分散
   => CleanKLS/DLS admission。
```

这条链的关键是：不需要一个固定常数描述所有层。每层只登记本层的支付签名、fiber 幸存率和有效支撑。
若新素数稳定承担支付，就晋升轮筛；若晋升持续删除，删除势累积；若删除停止，则进入 NoDeletion-KL；
若固定 residue/column 签名出现，则回到 PDEC；若都没有，则只剩 clean 多壳分散。

因此当前总链的无名逃逸进一步减少为：

```text
top-prime 持久支付不是终端；
固定 Q 同层 cap 循环不是终端；
无限升层不是无名终端；
只能落入 LocalSurvivor、PDEC、CleanKLS/DLS 或删除势塔。
```

## 40. 晋升删除势账本

新增 `experiments/prime_matrix_triad_a1_promotion_deletion_potential_ledger.py` 与
`prime-matrix-triad-a1-promotion-deletion-potential-ledger.md/json` 后，递归晋升链拥有显式势函数。

对每层 top-prime 晋升定义：

```text
a_n = lift_survival_rate；
D_n = -log(a_n)。
```

当前 `Q=2310 -> 30030` 层：

```text
cap_count=68；
all_positive_deletion_potential=True；
global_min_deletion_potential_current_layer=0.8800788718999966；
global_max_survival_current_layer=0.4147501982553529。
```

这一步的证明价值不是提取固定常数，而是补上递归剥离的势函数：

```text
sum D_n = infinity
  => 支撑密度趋零，回到 Sparse/LocalSurvivor/PDEC；

sum D_n < infinity
  => D_n->0, a_n->1
  => NoDeletion-KL / CleanKLS；

固定 residue/cap 持久
  => PDEC。
```

于是“top-prime 晋升无限持续但越来越弱”也不再是逃逸口；它正是 NoDeletion 的定义域。

## 41. NoDeletion-KL 的互信息见证化

新增 `experiments/prime_matrix_triad_a1_nodeletion_kl_witness_extractor.py` 与
`prime-matrix-triad-a1-nodeletion-kl-witness-extractor.md/json` 后，`NoDeletion` 分支中的 KL 硬点
被进一步拆成可定位见证。对新增 fiber residue `B` 与旧相位 `T`：

```text
H_cond = E_T KL(B|T || U_B)
       = KL(B || U_B) + I(T;B)。
```

于是无限层叠若删除停止，只有三种结构归宿：

```text
Global residue 偏斜持久
  => GlobalResiduePDEC；

旧相位-新增 residue 互信息持久
  => refined (old_phase,residue) PDEC；

两者都趋零
  => CleanKLS/DLS admission。
```

当前已物化两层审计：

```text
gate_route_counts={'FiberDeletionCurrentLayer': 6}；
shape_route_counts={'PhaseResidueMutualPDECWitness': 6}；
max_global_residue_normalized_kl=0.0388557；
min_phase_residue_mutual_normalized_kl=0.412500；
max_kl_chain_abs_error=0。
```

这说明当前层还不需要 NoDeletion 终端，因为删除势仍在支付；但 KL 形状已经显示，偏斜主要藏在
`(old_phase,residue)` 同步，而不是全局 residue 质量峰。正式结构链因此升级为：

```text
晋升删除势发散
  => Sparse/LocalSurvivor/PDEC；

晋升删除势不发散
  => NoDeletion；
     Global KL 累计      => PDEC；
     Phase-residue I 累计 => refined PDEC；
     二者趋零             => CleanKLS/DLS。
```

所以“无穷层叠但无固定常数”的可能性被压成了信息账本：每一层要么删除支撑，要么留下可命名相位信息，
要么趋于 clean 平坦；没有第四类无名逃逸。

## 42. PhaseResidueMutual 无循环

新增 `prime-matrix-triad-a1-phase-residue-mutual-no-cycle.md` 后，第 41 节中的互信息分支也被写成
滤过无循环引理。`Q'=rQ` 时：

```text
(old phase t, new residue b) <=> new phase u=t+bQ mod Q'。
```

所以 `I(T;B)` 峰不是新终端，而是下一层轮筛上的普通 cylinder atom。它若持久承担正质量，就成为
`refined/profinite PDEC`；它若在下一层被删除，就支付删除势；它若不持久，则质量趋于分散并进入
`CleanKLS/DLS`。

无限层形式为：

```text
sum H_n = infinity
  => finite/profinite cylinder PDEC；

sum H_n < infinity
  => H_n->0，固定复杂度 cylinder/cap 趋平
  => CleanKLS/DLS admission。
```

这一步进一步封死“互信息峰不断换壳但不留下固定规律”的逃逸：换壳本身就是模数提升；一旦在任何有限截断上累计正信息，
就得到可命名 PDEC，若所有有限截断都不累计，则进入 clean 平坦。

## 43. PhaseResidueMutual 原子提升审计

新增 `experiments/prime_matrix_triad_a1_phase_residue_mutual_atom_lift_audit.py` 与
`prime-matrix-triad-a1-phase-residue-mutual-atom-lift-audit.md/json` 后，第 42 节获得机器账本。

审计对象是 `NoDeletion-KL` 见证器抽出的 top 互信息原子。对每个原子核验：

```text
u=t+bQ；
M_{Q'}(u)=atom_mass。
```

当前结果：

```text
atom_count=36；
with_next_layer_count=12；
all_lift_identities_hold=True；
route_counts={
  NoNextLayerDataProfiniteObligation: 24,
  NextLayerCleanFiberCandidate: 6,
  NextLayerRefinedPDECEntropy: 6
}。
```

已有下一层数据的分裂非常清楚：

```text
P=19:
  下一层 fiber 全支撑且均匀，next KL=0
  => CleanKLS 候选；

P=23:
  下一层 fiber 全支撑但有单 residue 峰，next KL=0.309287
  => refined/profinite PDEC entropy 或继续升层。
```

因此互信息峰已经从“无穷缠绕直觉”变成可迭代方程：

```text
提升成新相位原子；
下一层删除 => 删除势；
下一层均匀 => CleanKLS；
下一层偏斜 => refined PDEC / next lift。
```

没有下一层数据的 `24` 个原子被标为 `ProfiniteObligation`，不是新出口；正式无限塔必须按同一提升规则处理。

## 44. PhaseResidue 完整 CRT 终端展开

新增 `experiments/prime_matrix_triad_a1_phase_residue_full_crt_terminal_audit.py` 与
`prime-matrix-triad-a1-phase-residue-full-crt-terminal-audit.md/json` 后，第 43 节的已有下一层数据又被压到完整
CRT 终端。

对每个原子：

```text
u at Q'；
v=u+sQ'；
w=v+y*nextQ。
```

审计核验：

```text
completion_count(v)=#{y: w 是完整 CRT 零行相位}。
```

当前结果：

```text
rows_with_next_count=12；
source_route_counts={
  NextLayerCleanFiberCandidate: 6,
  NextLayerRefinedPDECEntropy: 6
}；
route_counts={FullCRTTerminalFarBeyondPxP: 12}；
all_terminal_mass_identities_hold=True；
all_residue_mass_identities_hold=True；
all_terminal_phases_gt_p=True；
all_terminal_phases_gt_p2=True；
min_terminal_phase=3659；
min_terminal_phase_over_p2=10.1357。
```

这一步把当前已有数据中的 `CleanFiberCandidate` 和 `RefinedPDECEntropy` 都排除了早期出口：

```text
它们确实是零行相位；
但全部发生在 P^2 之后；
因此只能作为远处 finite/profinite PDEC 数据包，
不能作为 P 行以内零行。
```

剩余未闭合的是没有下一层数据的 `ProfiniteObligation`，以及一般无限层的 PDEC/CleanKLS/LocalSurvivor 终端证书。

## 45. NoNext ProfiniteObligation 局部解析

新增 `experiments/prime_matrix_triad_a1_no_next_profinite_obligation_resolver.py` 与
`prime-matrix-triad-a1-no-next-profinite-obligation-resolver.md/json` 后，第 44 节剩下的
`NoNextLayerDataProfiniteObligation` 也不再是数据缺口。

解析方法不生成整层 `m_vector`，只对每个当前原子局部展开剩余高素 fiber：

```text
atom u at Q'；
R={ell<P: ell does not divide Q'}；
w=u+yQ'；
completion_count(u)=#{y mod prod(R): w 完整覆盖}。
```

当前结果：

```text
obligation_count=24；
resolved_count=24；
route_counts={FullCRTTerminalFarBeyondPxP: 24}；
all_mass_identities_hold=True；
all_terminal_phases_gt_p=True；
all_terminal_phases_gt_p2=True；
min_terminal_phase=2323；
min_terminal_phase_over_p2=8.03806。
```

结合第 44 节，当前 `NoDeletion-KL` 见证器抽出的全部 top phase-residue 互信息原子已经关闭早期出口：

```text
12 个已有下一层数据原子 => 完整 CRT 终端相位，全部 >P^2；
24 个无下一层数据原子   => 局部剩余高素 fiber 展开，全部 >P^2。
```

这一步的结构意义很直接：即便素数规律在小模连乘同余中继续层叠，当前这些互信息峰一旦沿 CRT fiber
追到底，落点全部是远处零行相位包，而不是 `P×P` 方阵内的早期零行。剩余全局任务仍是把这个局部
top-atom 结论推广到所有可能 PDEC/CleanKLS/LocalSurvivor 终端，而不是宣称行命题已经完全闭合。

## 46. 当前有限升层的全原子早期出口关闭

新增 `experiments/prime_matrix_triad_a1_all_phase_residue_terminal_audit.py` 与
`prime-matrix-triad-a1-all-phase-residue-terminal-audit.md/json` 后，第 45 节的 top-atom 结论被升级为
当前有限升层的全原子结论。

审计对象：

```text
Q=30030 的全部非零 M_Q(u)，P=17,19,23,29；
Q=510510 的全部非零 M_Q(u)，P=19,23。
```

对每个非零相位，局部展开剩余高素 CRT fiber：

```text
w=u+yQ；
M_Q(u)=#{y: w 完整覆盖}。
```

当前结果：

```text
total_nonzero_phase_count=5030；
total_terminal_count=14348；
all_total_mass_identities_hold=True；
all_phase_mass_identities_hold=True；
all_terminal_gt_p=True；
all_terminal_gt_p2=False；
total_terminal_le_p_count=0；
total_terminal_le_p2_count=2；
global_min_terminal_phase=59。
```

P 级最小终端相位：

```text
Q=30030, P=17: min=1211；
Q=30030, P=19: min=3659；
Q=30030, P=23: min=59；
Q=30030, P=29: min=5210；
Q=510510, P=19: min=3659；
Q=510510, P=23: min=59。
```

这里 `P=23` 的 `59` 是完整 CRT 中已知的早期零行，但它满足 `59>P=23`，所以不破坏行命题。该结果说明：

```text
当前已物化升层全 phase-residue 支撑
=> 完整 CRT 终端相位全部在第 P 行之后；
=> 当前有限层不能给出 P 行以内零行。
```

剩余全局硬点不再是当前 `Q=30030,510510` 层的 phase-residue 支撑，而是如何把同样的 fiber 终端展开/容量排斥
推广到所有后继层、所有 PDEC 方向、所有 CleanKLS 与 LocalSurvivor 终端。

## 47. 边界终端 LocalSurvivor 引理

新增 `prime-matrix-triad-a1-boundary-terminal-local-survivor-lemma.md` 后，第 46 节的物化结论被抽象为
一个可反复调用的边界引理。

核心结构是：

```text
Q>P；
terminal row r = u + yQ；
1<=r<=P 只能发生在 y=0 且 1<=u<=P。
```

因此任意后继层相位支撑 `A_Q` 要产生前 `P` 行零行，唯一入口是：

```text
存在 u in A_Q cap [1,P]，且第 u 行 y=0 完整覆盖。
```

若每个这样的 `u` 都有一个未覆盖列 `c`，即

```text
ell 不整除 (u-1)P+c  对所有 ell<P，
```

则该相位支撑的全部早期出口关闭；后继 CRT fiber 即使能补洞，也只能出现在 `u+Q,u+2Q,...`，
全部大于 `P`。

当前物化审计给出的读数为：

```text
Q=2310,30030,510510；
total_phase_le_p_count=113；
total_y0_completion_le_p_count=0；
all_phase_le_p_have_local_survivor=True；
all_terminal_lower_bounds_gt_p=True。
```

这一步把用户提出的“方阵斜线覆盖与圆柱环绕覆盖夹击”压成严格命题：圆柱绕行不能回到前 `P` 行，
而方阵首端只要留下一个 LocalSurvivor 列，就排除该相位的早期零行。

当前新增的是一般边界入口，不是最终行命题闭合。剩余任务是把所有可能的 PDEC/CleanKLS/SparseLocal
终端都送入这个边界判据、完整 CRT 终端展开，或三终端证书排斥。

## 48. 局部 Fiber 终端展开合同

新增 `prime-matrix-triad-a1-local-fiber-terminal-expansion-contract.md` 后，第 44 至 47 节被合并为统一接口。

设

```text
B_P=prod_{ell<P}ell，Q|B_P；
C_P={完整小素因子覆盖零行的行残基 mod B_P}。
```

对任意相位原子 `u mod Q`，不用生成整层后继 `m_vector`，只需枚举剩余高素 fiber：

```text
R_Q={ell<P: ell 不整除 Q}；
B_Q=prod R_Q；
w=u+yQ, 0<=y<B_Q。
```

局部计数

```text
E_Q(u)=#{y: w in C_P}
```

必须等于同一 formal unit 下的投影质量 `M_Q(u)`。若展开得到的所有正终端代表都大于 `P`，
则该 phase atom 的早期出口关闭。

这个合同统一解释了三类机器结果：

```text
已有下一层数据原子       => 完整 CRT 终端展开；
NoNextLayerData 原子      => 局部剩余高素 fiber 解析；
完整已物化 phase support => 全原子局部展开；
Q>P 边界相位             => 只需 y=0 LocalSurvivor 检查。
```

因此“没有下一层 `m_vector`”不再是证明缺口。只要当前分支给出相位原子和同一 `C_P` 口径，
就能局部追踪到底；若追踪不到同一口径，则回到 Multiplicity-Stitching，而不是产生第四类出口。

当前状态可写成：

```text
当前已抽出的 phase/fiber 原子：
  mass identity 成立；
  terminal rows 全部 >P；
  P 行以内出口关闭。

全局仍未闭合：
  PDEC/CleanKLS/LocalSurvivor/formal-unit 证书全集仍需补齐。
```

## 49. PDEC 质量来源合同与当前 DualCap 路由

新增 `prime-matrix-triad-a1-pdec-mass-source-contract.md` 与
`experiments/prime_matrix_triad_a1_pdec_mass_source_router.py` 后，PDEC 帽进入 BTLS/LFTE 前的合法性条件被固定：

```text
PDEC cap 必须先证明 AttachedMass：
  S subset Omega；
  M_Q(t)=#{omega in Omega: tau(omega)=t}；
  g(t)<=M_Q(t)。

若没有同一 formal unit：
  回到 Multiplicity-Stitching；
  不能使用 BTLS/LFTE 或 PDEC dual upper。
```

当前路由器核验 `Q=2310` DualCap 三族：

```text
SparseCap: 16；
PersistentCap: 68；
ForcedPersistentByDensityBarrier: 24。
```

路由结果：

```text
all_current_dualcap_mass_sources_verified=True；
all_current_dualcap_pxp_exits_closed=True。
```

具体含义：

```text
SparseCap
  => SparseLocalSurvivor / finite PDEC beyond P；

PersistentCap
  => cap subset supp(M_Q)，全支撑 BTLS 关闭 P 行出口；
     终端转 ColumnTail/TailAnchor PDEC 或 CleanKLS；

ForcedPersistentByDensityBarrier
  => 旧层 BTLS 先关闭 P 行出口；
     lift 后只能产生删除势/KL/CleanKLS/column-tail 义务。
```

新增的 lift 单调继承也很关键：

```text
Q>P, Q'=rQ, v=u+bQ；
若 v<=P，则 b=0 且 u=v。
```

所以一个在旧层首端 `y=0` 已有 LocalSurvivor 的相位，升层细分后不能重新打开前 `P` 行出口。

当前推进的诚实边界：

```text
当前 DualCap 三族的 P×P 早期出口关闭；
PDEC / ColumnTail / CleanKLS 终端证书仍未全集排除。
```

## 50. PersistentCap 终端路由合并

新增 `prime-matrix-triad-a1-persistentcap-terminal-router-contract.md` 与
`experiments/prime_matrix_triad_a1_persistentcap_terminal_router.py` 后，当前 `PersistentCap` 的中间路由被合并。

路由链为：

```text
PersistentCap
=> AttachedMass: g(t)<=M_Q(t)
=> BTLS: P×P 边界出口关闭
=> ColumnTail payment equation
=> fixed residue/column PDEC
   or top-prime persists
   or distributed CleanKLS
=> top-prime=next high prime 时 promote Q to rQ
=> PromotionFiberDeletion / NoDeletion-KL / CleanKLS / PDEC。
```

当前机器核验：

```text
mass_source_persistent_count=68；
payment_persistent_count=68；
promotion_cap_count=68；
deletion_cap_count=68；
all_counts_match=True；
all_current_persistent_caps_routed=True。
```

所有门控均为真：

```text
mass_source_verified=True；
pxp_exit_closed_by_btls=True；
payment_intersections_recomputed=True；
payment_phase_m_counts_match=True；
top_prime_is_next_high_prime=True；
promotion_all_fiber_deletion=True；
promotion_deletion_potential_positive=True。
```

因此当前 `68` 个 PersistentCap 已退出三个中间逃逸：

```text
早期 P×P 出口      => BTLS 关闭；
固定 Q 同层循环     => TopPrime 晋升；
top-prime 独立终端  => PromotionFiberDeletion 删除势账本。
```

剩余全局义务更窄：

```text
证明晋升删除势塔发散；
或在删除势停止时提交 NoDeletion-KL / CleanKLS；
或对固定 residue/column 签名提交 TailAnchor/ColumnCRT PDEC。
```

这仍不是最终行命题闭合；它关闭的是当前 PersistentCap 的中间路由。

## 51. ForcedCap 终端路由合并

新增 `prime-matrix-triad-a1-forcedcap-terminal-router-contract.md` 与
`experiments/prime_matrix_triad_a1_forcedcap_terminal_router.py` 后，当前
`ForcedPersistentByDensityBarrier` 分支也被接入统一终端路由。

路由链为：

```text
ForcedPersistentByDensityBarrier
=> AttachedMass: g(t)<=M_Q(t)
=> BTLS: P×P 边界出口关闭
=> DensityBarrier: fixed-Q same-cap closure impossible
=> lift Q to Q'=rQ
=> ColumnTailExposure
=> ExposureDominance: 单桶实际支付排除
=> multi-bucket PDEC / next persistent / NoDeletion-KL / CleanKLS。
```

当前机器核验：

```text
mass_source_forced_count=24；
forced_lift_cap_count=24；
forced_exposure_cap_count=24；
forced_dominance_cap_count=24；
all_counts_match=True；
all_current_forced_caps_routed=True。
```

所有门控均为真：

```text
mass_source_verified=True；
pxp_exit_closed_by_btls=True；
boundary_terminals_excluded=True；
boundary_phase_le_p_has_local_survivor=True；
old_intersections_recomputed=True；
all_forced_lifts_persistent=True；
columntail_exposure_materialized=True；
single_residue_actual_payment_excluded=True；
single_column_residue_actual_payment_excluded=True。
```

读法：

```text
P×P 早期出口  => BTLS 关闭；
固定 Q 同层循环 => DensityBarrier 强制 lift；
一层 lift 后仍持久 => 下一义务是 multi-bucket PDEC / next-lift / CleanKLS。
```

因此 forced cap 与 persistent cap 的差别已经明确：

```text
PersistentCap 当前 top-prime 晋升给出正删除势；
ForcedCap 当前一层 lift 仍持久，但单桶 tail 支付已排除，必须进入多桶 PDEC、next-lift 删除/KL 或 CleanKLS。
```

这仍不是 forced 分支排斥；它关闭的是 forced 分支的早期出口与同层循环。

## 52. ForcedCap ColumnTail 暴露物化

新增 `prime-matrix-triad-a1-forcedcap-columntail-payment-contract.md` 与
`experiments/prime_matrix_triad_a1_forcedcap_columntail_payment_audit.py` 后，ForcedCap 的
`column-tail` 义务不再只是标签。

对每个 forced cap `C`，同样定义支付需求：

```text
D_C = sum_{phase in C} M(phase) * |H_low(phase)|。
```

当前审计覆盖 `P=43,47` 的全部 `24` 个 forced cap，并核验：

```text
old intersection size/mass 重算一致；
每个低洞列对每个高素数诱导唯一可支付 residue；
每个 cap 输出 top prime/residue/column-residue 暴露签名。
```

机器读数：

```text
forced_cap_count=24；
all_intersections_recomputed=True；
route_counts={ForcedColumnTailExposurePDECOrDistributedCleanKLS: 24}；

P=43: max residue exposure share <= 0.091484，
      max column-residue exposure share <= 0.101367；
P=47: max residue exposure share <= 0.095953，
      max column-residue exposure share <= 0.118158。
```

结构二分：

```text
固定 tail/column residue 暴露签名实际持久过载
  => TailAnchor / ColumnCRT PDEC；

支付不持久且分散
  => CleanKLS / DLS；

升层后结构改变
  => next-lift deletion/KL。
```

这一步仍不排除 forced cap；它把 forced 分支下一步的 `column-tail` 终端输入物化为轻量暴露账本。

## 53. ForcedCap 暴露支配实际支付

新增 `prime-matrix-triad-a1-forcedcap-exposure-dominance-contract.md` 与
`experiments/prime_matrix_triad_a1_forcedcap_exposure_dominance_router.py` 后，暴露账本被提升为实际支付的上界约束。

结构律：

```text
ActualPayment(bucket) <= Exposure(bucket)；
D_C <= sum ActualPayment(bucket)；
因此 bucket_count >= ceil(D_C / max Exposure)。
```

当前机器核验：

```text
forced_cap_count=24；
all_single_residue_actual_payment_excluded=True；
all_single_column_residue_actual_payment_excluded=True；
global_min_actual_residue_buckets_by_exposure=11；
global_min_actual_column_residue_buckets_by_exposure=9。
```

这一步不靠固定常数；每个 cap 使用自己的 `D_C/max_exposure` 动态下界。结论是：

```text
ForcedCap 不能由单 residue 或单 column-residue 支付完成；
若支付持久，必须是 multi-bucket formal unit；
若没有持久 multi-bucket 集合，则进入 distributed CleanKLS/DLS。
```

所以 ForcedCap 的最后形态进一步压成：

```text
multi-bucket TailAnchor/ColumnCRT/refined PDEC；
或 distributed CleanKLS/DLS；
或 next-lift deletion/KL。
```

## 54. ForcedCap 多桶 PDEC / CleanKLS 结构二分

新增 `prime-matrix-triad-a1-forcedcap-multibucket-pdec-clean-split.md` 后，
ForcedCap 的最后硬点被改写为一个递归二分合同，而不是继续寻找固定常数。

输入对象：

```text
Omega_C = tail 低洞支付原子集合；
D_C     = |Omega_C|；
B_C     = 可支付 bucket 集合；
E_C(b)  = bucket b 的暴露质量；
A_C(b)  = bucket b 的实际支付质量。
```

已知：

```text
A_C(b) <= E_C(b)；
sum_b A_C(b)=D_C；
bucket_count >= ceil(D_C / max_b E_C(b))。
```

升层 `Q_i | Q_{i+1}` 给出 bucket 投影：

```text
pi_i: B_{i+1} -> B_i。
```

于是剩余反例只能落在三类：

```text
MultiBucketPersistent:
  存在投影兼容的有限多桶 formal unit 长期承担支付
  => multi-bucket TailAnchor / ColumnCRT / refined PDEC；

DistributedPayment:
  没有持久有限桶组，支付向越来越多的新桶扩散
  => CleanKLS / DLS；

LiftDeletion / NoDeletion-KL:
  升层切掉正质量则删除势递减；
  若长期不删除则进入 NoDeletion-KL / CleanKLS。
```

递归闭合方程为：

```text
ZeroRow_i
=> MultiBucketPersistent_i
   or DistributedPayment_i
   or (ZeroRow_{i+1} with Phi_{i+1} <= Phi_i - Delta_i)
   or NoDeletionKL_i。
```

因此下一组终端硬点被锁定为：

```text
MBCS-1: multi-bucket PDEC 容量不等式 U_CRT(S)<L_PDEC(S)；
MBCS-2: no persistent signature => CleanKLS/DLS admission；
MBCS-3: lift deletion potential 发散或 no-deletion KL。
```

这一步的结构意义是：不再把素数规律假设为某个固定模式，而是在无穷轮层投影中使用
“持久则代数化、非持久则扩散化、升层删除则势递减”的递归夹击。

## 55. 多桶 PDEC 容量路线

新增 `prime-matrix-triad-a1-multibucket-pdec-capacity-route.md` 后，`MBCS-1` 被细化成
向量容量问题。

旧 PDEC 的变量是：

```text
g(t)=#{x in S: tau(x)=t}。
```

多桶实际支付必须改成支付图与向量计数：

```text
Gamma subset Omega_C x B_C；
g_b(t)=#{omega: tau(omega)=t and (omega,b) in Gamma}；
G(t)=sum_b g_b(t)。
```

合法容量行包括：

```text
g_b(t)>=0；
g_b(t)<=E_b(t)；
sum_b g_b(t)<=M(t)；
column/tail/cofactor/displacement 条件行；
formal-unit compatibility 行。
```

多桶 PDEC 的目标为：

```text
U_CRT^multi(h,zeta;S) < L_PDEC^multi(S)。
```

若失败，必须输出可路由形态：

```text
SingleBucketReturn      => 与单桶排除冲突或回到单桶 PDEC；
CorrelatedBucketBlock   => 细化为更小 multi-bucket formal unit；
ColumnTailMissingRow    => 补 TailAnchor / ColumnCRT / cofactor 条件行；
DiffuseExtremizer       => CleanKLS/DLS。
```

所以持久多桶分支不再是模糊终端；它被压成一个机器可复核的 LP/对偶骨架。

## 56. ForcedCap 多桶 LP 骨架物化

新增 `experiments/prime_matrix_triad_a1_multibucket_pdec_skeleton.py` 与
`prime-matrix-triad-a1-multibucket-pdec-skeleton.md/json` 后，第 55 节的多桶向量变量已被机器物化。

该审计从原始 `dualcap` 与 `multiplicity` 数据重算每个 forced cap 的全量 phase-bucket 暴露矩阵，
而不是读取旧报告的 top bucket 摘要。每个 cap 同时生成：

```text
residue bucket skeleton；
column-residue bucket skeleton。
```

当前核验：

```text
forced_cap_count=24；
matrix_row_count=48；
all_existing_exposure_references_match=True；
all_phase_exposure_identities_hold=True；
all_single_bucket_payments_excluded=True。
```

桶类型结果：

```text
residue:
  min actual buckets >= 11；
  max exposure share <= 0.0959528；
  max variable count = 125486；

column_residue:
  min actual buckets >= 9；
  max exposure share <= 0.118157；
  max variable count = 125486。
```

因此 `MBCS-1` 的下一步已经不是“定义多桶 PDEC”，而是直接攻：

```text
在已哈希化的 E_b(t), M(t), g_b(t) 约束系统上，
证明 U_CRT^multi(h,zeta;S) < L_PDEC^multi(S)，
或输出 SingleBucketReturn / CorrelatedBucketBlock / ColumnTailMissingRow / DiffuseExtremizer。
```

这一步继续遵守无固定常数路线：每个 cap 使用自己的 `D/max_b E_b` 和自己的向量 LP 骨架。

## 57. 裸多桶 LP 投影坍缩

新增 `experiments/prime_matrix_triad_a1_multibucket_projection_collapse_router.py` 与
`prime-matrix-triad-a1-multibucket-projection-collapse-router.md/json` 后，`MBCS-1` 的一个假强化路径被排除。

结构律：

```text
0<=g_b(t)<=E_b(t)；
G(t)=sum_b g_b(t)；
sum_b g_b(t)<=M(t)；
sum_b E_b(t)>=M(t)
=> 0<=G(t)<=M(t)。
```

也就是说，如果目标只看 `G(t)`，而没有 formal-unit 兼容行或列/尾条件行，裸多桶 LP 会投影回普通相位质量上界。

当前核验：

```text
matrix_row_count=48；
all_single_bucket_payments_excluded=True；
all_phase_capacity_surplus=True；
all_bare_projection_collapses=True；
route_counts={NeedsFormalUnitCompatibilityOrCleanKLS: 48}。
```

结论：

```text
单桶支付排除已经成立；
但“多桶变量数量增加”本身不是闭合力量；
闭合力量必须来自持久多桶 formal unit compatibility，
或来自无持久兼容签名时的 DistributedPayment => CleanKLS/DLS。
```

因此下一硬点被进一步压成：

```text
MFU-1: 构造投影兼容的多桶 formal unit 行；
MFU-2: 对该 formal unit 证明 U_CRT^multi<L_PDEC^multi；
MFU-3: 若无法构造持久 formal unit，则证明支付分散并进入 CleanKLS/DLS。
```

## 58. 多桶 Formal Unit 投影二分与候选行

新增 `prime-matrix-triad-a1-multibucket-formal-unit-dichotomy.md` 后，MFU 被定义为升层塔中的投影兼容桶组：

```text
Q_0 | Q_1 | Q_2 | ...；
pi_n: B_{n+1}->B_n；
S_n subset B_n；
pi_n(S_{n+1}) subset S_n；
limsup mu_n(S_n) >= eta > 0。
```

因此多桶分支只剩二分：

```text
PersistentFormalUnit:
  存在投影兼容正质量桶组
  => multi-bucket PDEC / refined ColumnTail-Cofactor row；

DistributedPayment:
  任意固定有限签名后继质量趋零
  => CleanKLS/DLS；
  若大筛对偶失败，又输出持久有限签名回到 PDEC。
```

新增 `experiments/prime_matrix_triad_a1_multibucket_mfu_candidate_audit.py` 与
`prime-matrix-triad-a1-multibucket-mfu-candidate-audit.md/json` 后，当前有限层候选行已物化。

该审计重算 `phase-bucket` 暴露矩阵并计算：

```text
I(phase;bucket)。
```

机器核验：

```text
matrix_row_count=48；
all_rows_have_finite_layer_correlation=True；
route_counts={FiniteLayerMFUCandidateNeedsActualPaymentStitching: 48}。
```

桶类型读数：

```text
residue:
  MI in [1.22721, 1.26555]；
  normalized MI in [0.221783, 0.236679]；

column_residue:
  MI in [0.955803, 1.24288]；
  normalized MI in [0.182715, 0.23244]。
```

读法：

```text
暴露图存在有限层相关候选；
但还未证明实际支付图 Gamma 持久跟随这些候选；
若 Gamma 持久跟随 => MFU/PDEC；
若 Gamma 不持久跟随任意有限候选 => DistributedPayment/CleanKLS-DLS。
```

所以真正下一硬点现在是：

```text
APS-1: ActualPaymentStitching；
证明实际支付若覆盖全部低洞，必然持久落入某个 MFU 候选行；
或证明它不能持久落入任何候选行，从而满足 CleanKLS/DLS 准入。
```

## 59. ActualPaymentStitching 路由

新增 `prime-matrix-triad-a1-actual-payment-stitching-contract.md` 与
`experiments/prime_matrix_triad_a1_actual_payment_stitching_router.py` 后，ForcedCap 多桶分支的当前入口已合并成 APS。

APS 区分三层对象：

```text
Omega_C = 低洞需求原子；
B_C     = 可支付 bucket；
E       subset Omega_C x B_C，可支付暴露边；
Gamma   subset E，实际支付边。
```

已有审计处理的是 `E`；最终覆盖需要的是 `Gamma`。

当前路由器核验：

```text
skeleton_matrix_row_count=48；
collapse_matrix_row_count=48；
mfu_matrix_row_count=48；
forced_signature_matrix_row_count=48；
all_counts_match=True；
all_current_forced_multibucket_rows_routed_to_aps=True。
```

门控全真：

```text
single_bucket_payments_excluded=True；
bare_projection_collapses=True；
finite_layer_mfu_candidates_exist=True；
fiber_completion_counts_match_m_vector=True；
fiber_residue_bucket_lower_bound_active=True；
fiber_column_residue_bucket_lower_bound_active=True；
gamma_forced_share_large=True；
forced_signature_or_small_ambiguous_gate_active=True。
```

新增 `experiments/prime_matrix_triad_a1_forced_gamma_signature_router.py` 与
`prime-matrix-triad-a1-small-ambiguous-cleankls-admission.md` 后，APS 不再只停留在
“Gamma 自由度小”：

```text
global_max_ambiguous_gamma_share_upper_bound=0.0552843；
global_min_forced_gamma_share_lower_bound=0.944716；
global_min_signature_signal_minus_ambiguous_budget=0.130733；
global_min_signature_signal_to_ambiguity_ratio=3.51497；
route_counts={ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission: 48}。
```

新增 `experiments/prime_matrix_triad_a1_small_ambiguous_clean_admission_router.py` 后，
small-ambiguous 后继也接入 NoDeletion-KL：

```text
all_current_small_ambiguous_routed=True；
gate_counts={FiberDeletion: 6}；
current_nodeletion_triggered=False；
shape_route_counts={PhaseResidueMutualPDECWitness: 6}；
min_phase_residue_mutual_normalized_kl=0.412500。
```

读法：

```text
当前层没有 clean KLS 终端输入；
若删除势继续有效 => 递归升层/删除势推进；
若删除势停止且 KL/互信息偏斜持久 => refined/new-layer PDEC；
只有 deletion 停止且 KL/互信息平坦 => 真正 CleanKLS/DLS。
```

所以 ForcedCap 多桶分支的剩余二分为：

```text
Persistent Gamma follows finite MFU candidate
  => multi-bucket PDEC / refined TailAnchor-ColumnCRT-Cofactor row；

Gamma does not persist on any finite candidate
  => DistributedPayment / CleanKLS-DLS。
```

这一步避免了一个关键逻辑错误：

```text
可支付暴露 Exposure != 实际支付 ActualPayment。
```

行命题闭合不能从 exposure 候选直接跳到 PDEC；必须补 `Gamma` 的持久缝合或分散大筛。

## 60. FiberConsistent ActualPayment 支配

新增 `experiments/prime_matrix_triad_a1_forcedcap_fiber_consistent_payment_audit.py` 与
`prime-matrix-triad-a1-forcedcap-fiber-consistent-payment.md/json` 后，APS 中的 `Gamma` 约束被推进到同一
CRT fiber 层。

结构事实：

```text
phase t 固定；
row=t+Qy；
同一个 y mod high_period 必须覆盖该 phase 的全部低洞。
```

这比裸 exposure 强，因为 exposure 只说某条边可支付，而 fiber-consistent incidence 要求这些边来自真实完成态。

当前核验：

```text
forced_cap_count=24；
unique_phase_cache_count=4316；
all_intersections_recomputed=True；
all_completion_counts_match_m_vector=True；
route_counts={FiberConsistentPaymentMFUOrDistributedCleanKLS: 24}。
```

新增 `experiments/prime_matrix_triad_a1_forcedcap_fiber_dominance_router.py` 与
`prime-matrix-triad-a1-forcedcap-fiber-dominance-router.md/json` 后，fiber-consistent incidence 进一步给出实际支付桶数下界：

```text
ActualPayment(bucket) <= FiberConsistentCover(bucket)；
bucket_count >= ceil(D_C / max FiberConsistentCover)。
```

机器读数：

```text
global_min_actual_residue_buckets_by_fiber=42；
global_min_actual_column_residue_buckets_by_fiber=24；
global_max_residue_fiber_cover_share=0.0240372；
global_max_column_residue_fiber_cover_share=0.0433302。
```

APS 路由器已接入该门控：

```text
fiber_completion_counts_match_m_vector=True；
fiber_residue_bucket_lower_bound_active=True；
fiber_column_residue_bucket_lower_bound_active=True。
```

因此 ForcedCap 多桶分支被进一步夹紧：

```text
若 Gamma 持久跟随某个 fiber-consistent 多桶签名
  => MFU/PDEC/refined column-tail row；

若 Gamma 不持久跟随任何有限 fiber-consistent 签名
  => DistributedPayment/CleanKLS-DLS。
```

这一步仍不是最终闭合；它把 APS 的候选对象从“可支付暴露边”收缩成“真实 fiber 完成态诱导边”。

## 61. Gamma 自由度上界

新增 `experiments/prime_matrix_triad_a1_forcedcap_gamma_freedom_router.py` 与
`prime-matrix-triad-a1-forcedcap-gamma-freedom-router.md/json` 后，APS 的实际支付选择自由度被进一步定量压缩。

对每个完成态-低洞对，令：

```text
k = 覆盖该洞的高素数边数，k>=1。
```

只有 `k>=2` 的洞才有实际支付选择自由。设：

```text
D = completion-hole demand；
C = fiber-consistent cover incidence = sum k。
```

则：

```text
ambiguous_pairs <= C-D；
ambiguous_share <= C/D - 1；
forced_share >= 2 - C/D。
```

当前机器读数：

```text
forced_cap_count=24；
global_max_ambiguous_gamma_share_upper_bound=0.0552843；
global_min_forced_gamma_share_lower_bound=0.944716。
```

APS 路由器已接入新门控：

```text
gamma_forced_share_large=True。
```

因此当前 ForcedCap 的实际支付图 `Gamma` 不再是一个自由匹配问题：

```text
至少约 94.47% 的支付边由唯一覆盖强制决定；
最多约 5.53% 的洞存在选择自由。
```

剩余硬点继续压成：

```text
强制主体持久落入有限 MFU 签名
  => multi-bucket PDEC / refined row；

少量 ambiguous 自由度足以逃避所有有限签名
  => DistributedPayment / CleanKLS-DLS；

若 CleanKLS 对偶失败
  => 输出持久签名回到 PDEC。
```

## 62. A1 终端汇合与无第四出口

新增 `experiments/prime_matrix_triad_a1_forced_gamma_signature_router.py` 后，Gamma 小自由度已经接到有限签名门槛：

```text
signature_matrix_row_count=48；
route_counts={ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission: 48}；
global_min_signature_signal_minus_ambiguous_budget=0.130733；
global_min_signature_signal_to_ambiguity_ratio=3.51497。
```

新增 `experiments/prime_matrix_triad_a1_small_ambiguous_clean_admission_router.py` 后，small-ambiguous 后继接入
NoDeletion-KL：

```text
all_current_small_ambiguous_routed=True；
gate_counts={FiberDeletion: 6}；
current_nodeletion_triggered=False；
shape_route_counts={PhaseResidueMutualPDECWitness: 6}；
min_phase_residue_mutual_normalized_kl=0.412500。
```

因此 small-ambiguous 不能作为独立逃逸：

```text
当前层 FiberDeletion => 继续升层/删除势；
NoDeletion + KL/MI 偏斜 => refined/new-layer PDEC；
NoDeletion + KL/MI 平坦 => CleanKLS/DLS。
```

新增 `experiments/prime_matrix_triad_a1_terminal_confluence_router.py` 后，A1 当前物化链被汇合到终端三证书：

```text
all_current_pxP_exits_closed=True；
all_materialized_branches_routed_to_terminal_triad=True；
no_fourth_exit_current_a1_chain=True。
```

汇合律为：

```text
Persistent actual Gamma => A:PDEC；
Sparse/DualCap sparse   => B:LocalSurvivor or A:PDEC；
FiberDeletion diverges  => B:LocalSurvivor / capacity contradiction；
NoDeletion + KL/MI bias => A:PDEC；
NoDeletion + flat       => C:CleanKLS/DLS。
```

这一步完成的是当前 A1 物化链的“无第四出口”接线，不是最终无条件证明。剩余终端证书仍为：

```text
A:PDEC family same-set capacity upper U_CRT<L_PDEC；
B:LocalSurvivor witness/blocker-deficit；
C:CleanKLS/DLS admission + large-sieve or explicit external input。
```

当前最窄入口仍是：

```text
Triad-A1 PDEC same-set capacity upper。
```

## 63. A1 同集容量前沿

新增 `experiments/prime_matrix_triad_a1_pdec_same_set_capacity_frontier_router.py` 后，`PDEC same-set capacity`
不再是泛化缺口，而被拆成可检查前沿：

```text
all_known_frontiers_routed=True；
terminal_dual_gap=ContinuousDirectionArcDual。
```

连续方向弧提交前的前沿表：

```text
SameSetAttachment        => ready_current_lhb_branch；
ZeroBlockCapacityRows    => closed_subbranch；
BoxOnlyCapacity          => structurally_insufficient；
FourierCapDualFailure    => dualcap_materialized；
CurrentPXPExit           => closed；
TerminalConfluence       => no_fourth_exit；
ContinuousDirectionArcDual => not_submitted。
```

关键读数：

```text
all_zero_blocks_ready=True；
box_only_global_closure=False；
box_only_obstruction_count=9；
dualcap_class_counts={
  ForcedPersistentByDensityBarrier: 24,
  PersistentCap: 68,
  SparseCap: 16
}。
```

这给出一个重要结构判断：

```text
box-only 容量行在结构上不可能闭合 A1；
因为每个 P 都有单相位 g(t) 可行见证，
其 Fourier 模长不产生抵消。
```

所以 A1 不能继续靠调常数或固定低模层 box cap 推进。当时的下一唯一有效目标是：

```text
ContinuousDirectionArcDual：
  在连续方向弧上提交 U_CRT<L_PDEC；
  或让失败输出更窄的 column/tail/cofactor DualCap。
```

终端汇合路由器也已接入该前沿，当前仍保持：

```text
all_current_pxP_exits_closed=True；
all_materialized_branches_routed_to_terminal_triad=True；
no_fourth_exit_current_a1_chain=True。
```

## 64. A1 连续方向弧前沿已物化

新增 `experiments/prime_matrix_triad_a1_continuous_direction_arc_dual.py` 后，
`ContinuousDirectionArcDual` 不再只是“未提交”的方向缺口，而被精确审计为当前 box 行下的连续半平面支持函数：

```text
U_box(h,zeta)=sum_t M(t) max(0, Re(e^{i zeta}e(ht)))；
U_box(h)=max_zeta U_box(h,zeta)。
```

运行结果：

```text
status=continuous_direction_arc_box_dual_materialized_not_closed；
route_counts={
  PersistentContinuousDualCapNeedsColumnTailOrCleanKLS: 8,
  SparseContinuousDualCapToLocalSurvivor: 1
}；
global_max_box_dual_value_over_total_m=0.998391；
global_min_best_cap_phase_count=4。
```

因此这一步给出的不是最终 PDEC 闭合，而是一个更窄的结构结论：

```text
方向采样密度不是失败原因；
仅 0<=g(t)<=M(t) 的 box 同集容量行不能推出 U_CRT<L_PDEC；
失败对象已经是连续方向 persistent cap；
下一硬点必须加入 column/tail/cofactor 同集合法结构行，
或证明剩余平坦残差进入 CleanKLS/DLS。
```

前沿路由器同步更新后：

```text
ContinuousDirectionArcDual => continuous_dualcap_materialized_not_closed；
terminal_dual_gap => ColumnTailCofactorOrCleanKLSStructureRows。
```

这把 A1 当前最窄入口从“补连续方向对偶”推进到：

```text
把连续弧 persistent cap 与真实支付图的 column/displacement compatibility、
tail/cofactor nonreuse、actual Gamma forced-signature 约束接起来；
若这些约束无法制造 PDEC 抵消，则剩余对象必须是 flat residual CleanKLS/DLS。
```

## 65. A1 连续弧 ColumnTail 桥接

新增 `experiments/prime_matrix_triad_a1_continuous_columntail_bridge.py` 后，
连续方向弧 persistent cap 已经接到低洞的 column-tail 暴露账本。

核心接口不再使用固定阈值常数，而使用递归剥离二分：

```text
continuous cap C
=> low-hole demand D_C
=> actual tail payment measure mu_C on (prime,residue,column-residue)
=> limsup positive signature -> column/tail PDEC
=> all fixed signatures vanish -> diffuse CleanKLS/DLS。
```

运行结果：

```text
status=continuous_dualcap_columntail_bridge_materialized；
cap_report_count=9；
all_cap_recomputations_match=True；
route_counts={
  ContinuousCapActualPaymentSelectionDichotomy: 8,
  NoTailDemandSparseOrLocalSurvivor: 1
}。
```

P 级读数显示，除 `P=13` 的无 tail demand 稀疏/局部分支外，
所有最强连续弧 cap 都有正低洞需求，并进入真实支付选择二分：

```text
P=17 max_payment_signature_share=0.0357143；
P=19 max_payment_signature_share=0.0441176；
P=23 max_payment_signature_share=0.0274159；
P=29 max_payment_signature_share=0.0357788；
P=31 max_payment_signature_share=0.0249140；
P=37 max_payment_signature_share=0.0195775；
P=43 max_payment_signature_share=0.0105805；
P=47 max_payment_signature_share=0.0164943。
```

这些数值不是闭合常数，而是提示当前暴露候选桶高度分散。结构性结论是：

```text
若真实支付在无限反例子族中反复集中于某个签名，
  则该签名给出 column/tail PDEC 输入；

若所有固定签名都能被递归剥离到零质量，
  则支付测度扩散，进入 CleanKLS/DLS 输入。
```

前沿路由器同步更新后：

```text
ContinuousColumnTailBridge => actual_payment_selection_materialized；
terminal_dual_gap => ActualPaymentSelectionOrCleanKLSAdmission。
```

因此当前最窄硬点已经从“补 column-tail 结构行”推进为：

```text
ActualPaymentSelection:
  从暴露候选桶提升到真实支付测度；
  证明 limsup 正质量签名产生合法 PDEC 行；
  证明所有签名递归剥离为 0 时满足 CleanKLS/DLS 输入条件。
```

## 66. A1 连续弧 ActualPaymentSelection 构造完成

新增 `experiments/prime_matrix_triad_a1_continuous_actual_payment_selection.py` 后，
上一节的“暴露候选桶”已经提升为真实支付测度。

构造律：

```text
completion y=(y_ell)_ell；
hole c in H_low(t)；
pay(c,y)=first ell such that ell covers c under y_ell；
mu_C(bucket)=# canonical payments in bucket。
```

该规则对每个完成态和每个低洞都选择唯一支付桶，因此得到恒等式：

```text
payment_count=sum_phase M(phase)*|H_low(phase)|。
```

运行结果：

```text
status=continuous_actual_payment_measure_constructed；
cap_report_count=9；
all_cap_recomputations_match=True；
all_payment_counts_match_demand=True；
route_counts={
  ActualPaymentMeasureDichotomySubmitted: 8,
  NoTailDemandSparseOrLocalSurvivor: 1
}。
```

P 级 actual payment 读数：

```text
P=17 max_actual_signature_share=0.0357143，effective_support=28；
P=19 max_actual_signature_share=0.0254011，effective_support=39.3684；
P=23 max_actual_signature_share=0.0103149，effective_support=96.9474；
P=29 max_actual_signature_share=0.0122877，effective_support=81.3824；
P=31 max_actual_signature_share=0.0180444，effective_support=55.4189；
P=37 max_actual_signature_share=0.0122645，effective_support=81.5362；
P=43 max_actual_signature_share=0.00316956，effective_support=315.501；
P=47 max_actual_signature_share=0.00598387，effective_support=167.116。
```

这些数值说明当前 canonical 支付测度高度分散，但仍不是最终证明。结构上，当前硬点已经缩成两个终端引理：

```text
A. positive-limsup finite signature -> legal column/tail PDEC row；
B. all finite signatures vanish -> CleanKLS/DLS admission + large-sieve close。
```

前沿路由器同步更新后：

```text
ContinuousActualPaymentSelection => actual_payment_measure_constructed；
terminal_dual_gap => PositiveLimsupPDECOrDiffuseCleanKLS。
```

这一步完成了 `ActualPaymentSelection` 的构造部分；剩余不是“如何定义真实支付”，
而是证明上述两个终端分支都不能支持 `P×P` 内零行反例。

## 67. A1 连续 actual-payment 终端二分闭合

新增 `experiments/prime_matrix_triad_a1_continuous_terminal_dichotomy_router.py` 后，
`PositiveLimsupPDECOrDiffuseCleanKLS` 被压成确定性的有限投影塔二分。

二分律：

```text
canonical payment measures mu_i on finite projection B_i；
either exists b in B_i with limsup mu_i(b)>0
  => positive-limsup finite signature => column-tail PDEC；
or for every fixed finite projection atom b, mu_i(b)->0
  => max atom -> 0 and L2 -> 0 on finite projections => CleanKLS/DLS admission。
```

该二分只用有限集合鸽巢与逆系统投影，不使用固定全局常数。
因此它关闭的是逻辑出口，而不是替代终端估计。

运行结果：

```text
status=continuous_terminal_dichotomy_admission_closed_capacity_open；
route_counts={
  NoTailDemandSparseOrLocalSurvivor: 1,
  PositiveLimsupPDECOrDiffuseCleanKLSDichotomy: 8
}；
global_max_actual_signature_share=0.0357143；
global_min_effective_signature_support=28；
global_min_inverse_l2_signature_support=28。
```

已闭合子命题：

```text
canonical actual payment measure constructed；
payment_count equals low-hole demand；
no third terminal route in the finite-projection dichotomy；
diffuse branch supplies L2-flat admission language；
positive-limsup branch supplies legal finite column-tail PDEC row input。
```

剩余终端义务被进一步削成：

```text
PDEC-CAP:
  prove the resulting column-tail PDEC capacity inequality U_CRT<L_PDEC；

KLS-EXT:
  prove or import the CleanKLS/DLS large-sieve bound for diffuse payment measures。
```

前沿路由器同步更新后：

```text
ContinuousTerminalDichotomy => terminal_dichotomy_admission_closed_capacity_open；
terminal_dual_gap => PDECCapacityOrKLSLargeSieve。
```

这一步说明当前 A1 连续 actual-payment 分支已经没有“第三逃逸口”：

```text
集中 => PDEC-CAP；
完全分散 => KLS-EXT；
无 tail demand => Sparse/LocalSurvivor。
```

所以接下来的真正终端硬攻不能再停留在路由、归档或候选定义上，
必须直接攻击 `PDEC-CAP` 的容量不等式，或 `KLS-EXT` 的 clean 大筛估计。

## 68. A1 positive-limsup PDEC 输入账本

新增 `experiments/prime_matrix_triad_a1_continuous_pdec_signature_input_ledger.py` 后，
上一节的 positive-limsup 有限签名不再只是抽象分支，而被物化为具体的 column-tail PDEC 输入行。

输入律：

```text
positive-limsup finite signature b=(prime,residue,column-residue)
=> g_b(t)=# canonical actual payments at phase t using b
=> finite column-tail formal row
=> PDEC capacity comparison U_CRT<L_PDEC still required。
```

机器结果：

```text
status=continuous_positive_limsup_pdec_inputs_materialized_capacity_open；
cap_count=8；
signature_row_count=40；
route_counts={FiniteSignaturePDECInputMaterialized: 40}；
global_min_signature_fourier_abs_over_total=0.986379；
global_max_signature_fourier_abs_over_total=1。
```

读法：

```text
正 limsup 签名的合法性问题已关闭：
  它来自真实完成态、真实低洞、真实 canonical payment bucket；

每个 top finite signature 都有极强非零 Fourier 相位剖面：
  因而确实是 PDEC 输入，而不是 diffuse KLS 输入；

仍未完成的是容量比较：
  U_CRT(g_b;h,zeta)<L_PDEC(g_b)。
```

前沿路由器同步更新后：

```text
ContinuousPDECSignatureInput => positive_limsup_pdec_inputs_materialized_capacity_open；
terminal_dual_gap => PDECCapacityOrKLSLargeSieve。
```

当前终端硬点被压到最硬的两个估计本体：

```text
PDEC-CAP:
  对已物化的 g_b(t) 证明同集容量上界 U_CRT<L_PDEC；

KLS-EXT:
  对 diffuse actual-payment 测度证明 CleanKLS/DLS 大筛吸收。
```

除此之外，连续 actual-payment 分支当前没有剩余路由缺口。

## 69. A1 positive-limsup 签名 Prime-Lift 刚性

在 `experiments/prime_matrix_triad_a1_continuous_pdec_signature_input_ledger.py` 中补入同余字段后，
所有 positive-limsup PDEC 输入签名都满足唯一 prime-lift 同余：

```text
signature b=(ell,y,c)；
row=t+Qy；
(row-1)P+c=0 mod ell；
therefore t=1-cP^{-1}-Qy mod ell。
```

随后新增 `experiments/prime_matrix_triad_a1_continuous_prime_lift_router.py`，把这些有限签名路由到升层接口。

机器结果：

```text
status=continuous_pdec_signatures_routed_to_prime_lift_gate；
signature_row_count=40；
all_signature_rows_have_prime_lift_congruence=True；
promoted_prime_counts={13: 39, 17: 1}；
route_counts={
  StandardNextPrimePromotionDeletionKLReady: 39,
  SelectivePrimePromotionNeedsCommutationBeforeDeletionKL: 1
}。
```

结构意义：

```text
positive-limsup finite signature
=> 不是自由 PDEC 尖峰
=> 是新增素数 ell 的 residue 锁定
=> 标准下一素数行接 PromotionDeletionPotential / NoDeletion-KL / CleanKLS；
=> 选择性素数行需补晋升交换律，或回流 cofactor-order/PDEC。
```

唯一选择性行是：

```text
P=29, signature=17:8:6；
next_high_prime=13；
promoted_prime=17；
signature_payment_mass=204；
fourier_abs_over_total=1。
```

前沿路由器同步更新后：

```text
ContinuousPrimeLiftCongruence => prime_lift_deletion_kl_ready_with_selective_commutation_gap；
terminal_dual_gap => PrimeLiftDeletionKLOrKLSLargeSieve。
```

当前剩余硬点因此再次缩窄为：

```text
1. 标准 ell=13 晋升行：证明当前连续签名版本的 promotion deletion/KL 接线；
2. 选择性 ell=17 行：证明先晋升 13 再晋升 17 与直接晋升 17 的终端路由交换律；
3. diffuse 分支：证明/接入 CleanKLS/DLS 大筛估计。
```

这一步没有完成最终行命题，但把 positive-limsup PDEC-CAP 的抽象容量缺口转化为更具体的升层刚性缺口。

## 70. A1 选择性晋升交换律闭合

新增 `experiments/prime_matrix_triad_a1_selective_promotion_commutation.py` 后，
上一节唯一的选择性晋升行也被吸收。

选择性行：

```text
P=29；
original signature=17:8:6；
first smaller tail prime r=13；
promoted prime ell=17。
```

交换律：

```text
original signature: (ell,y,c) at Q；
first promote r<ell；
new phase: t'=t+Qs；
need t'+Qr*y' == t+Qy mod ell；
therefore y'=(y-s)r^{-1} mod ell。
```

机器结果：

```text
status=selective_promotion_commutation_resolved_by_finite_split；
selective_row_count=1；
route_counts={FiniteSplitThenStandardPromotionOrDiffuseKLS: 1}；
all_crt_orders_commute=True；
max_successor_count=13。
```

结构意义：

```text
选择性晋升不是新终端；
它先按较小尾素数 r 的 residue 拆成 r 个后继签名；
若原签名有正 limsup 质量，有限鸽巢给出某个后继签名正 limsup；
该后继回到标准 prime-lift promotion deletion/KL；
若所有后继都不持久，则进入 diffuse CleanKLS/DLS。
```

前沿路由器同步更新后：

```text
SelectivePromotionCommutation => selective_promotion_resolved_by_finite_split；
terminal_dual_gap => StandardPrimeLiftDeletionKLOrKLSLargeSieve。
```

于是当前 A1 连续 actual-payment 分支的剩余硬点进一步缩成：

```text
1. 标准 prime-lift 晋升删除/KL：证明 39 个 ell=13 行以及选择性拆分后继行接入删除势或 NoDeletion-KL；
2. diffuse 分支：证明/接入 CleanKLS/DLS 大筛估计。
```

选择性晋升交换律不再是独立障碍。

## 71. A1 标准 Prime-Lift 删除势账本

新增 `experiments/prime_matrix_triad_a1_standard_prime_lift_deletion.py` 后，
标准 prime-lift 分支被接入删除势账本。

删除势律：

```text
fixed residue modulo ell
=> survival <= 1/ell after promoting ell
=> deletion potential D >= log(ell)。
```

机器结果：

```text
status=standard_prime_lift_positive_deletion_potential_materialized；
standard_row_count=39；
commuted_successor_row_count=13；
deletion_row_count=52；
route_counts={PositiveDeletionPotentialOrNoDeletionKL: 52}；
promoted_prime_counts={13: 39, 17: 13}；
global_min_deletion_potential_lower_bound=2.564949；
global_max_survival_upper_bound=0.0769231。
```

结构意义：

```text
positive-limsup finite signature
=> prime-lift fixed residue；
=> 当前标准行支付正删除势；
=> 若无限层持续标准固定 residue，则删除势发散；
=> 若删除停止，则进入 NoDeletion-KL/PDEC 或 diffuse CleanKLS/DLS。
```

前沿路由器同步更新后：

```text
StandardPrimeLiftDeletion => positive_deletion_potential_or_nodeletion_kl；
terminal_dual_gap => NoDeletionKLOrKLSLargeSieve。
```

于是 A1 连续 actual-payment 分支的 `positive-limsup` 侧已经从：

```text
PDEC-CAP abstract capacity
```

被递归剥离为：

```text
positive deletion potential
  or NoDeletion-KL/PDEC
  or diffuse CleanKLS/DLS。
```

当前剩余硬点为：

```text
1. 删除停止时的 NoDeletion-KL/PDEC 终端；
2. diffuse CleanKLS/DLS 大筛估计。
```

这一步仍不是最终闭合；它把正 limsup PDEC 侧的容量硬点转成删除势/无删除-KL硬点。

## 72. A1 连续 NoDeletion 终端路由

新增 `experiments/prime_matrix_triad_a1_continuous_nodeletion_terminal_router.py` 后，
第 71 节留下的 `NoDeletion-KL` 不再作为独立出口停留。

输入账本：

```text
prime-matrix-triad-a1-standard-prime-lift-deletion.json；
prime-matrix-triad-a1-nodeletion-kl-gate.json；
prime-matrix-triad-a1-nodeletion-kl-witness-extractor.json；
prime-matrix-triad-a1-small-ambiguous-clean-admission-router.json；
prime-matrix-triad-a1-all-phase-residue-terminal-audit.json。
```

机器结果：

```text
status=continuous_prime_lift_nodeletion_terminal_routed_clean_kls_open；
deletion_row_count=52；
route_counts={PositiveDeletionPotentialOrNoDeletionPDECOrCleanKLS: 52}；
global_min_deletion_potential_lower_bound=2.564949；
global_max_survival_upper_bound=0.0769231；
no_independent_nodeletion_gap=True；
terminal_dual_gap_after_router=CleanKLSDLSLargeSieveOrExternalKLSInput。
```

核心结构链：

```text
positive-limsup finite signature
  => prime-lift fixed residue；

fixed residue promoted by ell
  => survival <= 1/ell
  => deletion potential D >= log(ell)；

sum D_n = infinity
  => support density is exhausted；

sum D_n < infinity
  => a_n -> 1
  => NoDeletion。
```

进入 `NoDeletion` 后，不再允许无名逃逸。KL 链式恒等式给出：

```text
E_t KL(B|t || U_B)
  = KL(B || U_B) + I(T;B)。
```

于是：

```text
KL(B||U_B) 持久累计
  => GlobalResidue / new-layer PDEC；

I(T;B) 持久累计
  => refined (old_phase,residue) PDEC；

二者同时趋零
  => CleanKLS/DLS admission。
```

当前有限层证据：

```text
current_layers_delete_before_nodeletion=True；
gate_counts={FiberDeletion: 6}；
shape_route_counts={PhaseResidueMutualPDECWitness: 6}；
kl_chain_identity_exact=True；
phase_residue_atoms_terminalized_beyond_p=True；
total_terminal_le_p_count=0。
```

解释：

```text
当前层本身仍由 FiberDeletion 推进；
若未来删除停止，KL/互信息偏斜会回流 refined PDEC；
只有 KL/互信息平坦时才进入 CleanKLS/DLS。
```

前沿路由器同步更新后：

```text
ContinuousNoDeletionTerminal => nodeletion_terminal_routed_clean_kls_open；
terminal_dual_gap => CleanKLSDLSLargeSieveOrExternalKLSInput。
```

这一步的意义是：

```text
NoDeletion-KL 不是第三终端；
PDEC 偏斜分支回到递归 PDEC family；
真正剩余独立终端硬点压到 CleanKLS/DLS 大筛证书，
或一个明确登记、可复核的外部 KLS/DI/BFI 输入。
```

这仍不是最终行命题闭合。下一步必须直接构造 `CleanKLS/DLS-Cert`，
或者把可用的外部大筛定理精确适配到当前 formal unit。

## 73. A1 CleanKLS 外部输入与自足原子压缩

新增 `experiments/prime_matrix_triad_a1_clean_kls_external_input_router.py` 后，
第 72 节留下的 `CleanKLS/DLS 大筛证书或外部输入` 被进一步压缩。

机器结果：

```text
status=a1_clean_kls_external_input_registered_self_contained_atom_open；
external_kls_input_registered=True；
all_admission_verified_or_routed=True；
terminal_gap_after_router=KuznetsovLSAtomSC9OrExternalCitation。
```

该路由器不是把外部谱大筛当作已自证，而是把 A1 clean 分支的准入条件逐项登记：

```text
K1 dyadic ranges；
K2 lowmod orthogonality；
K3 no short-window cap；
K4 no column/tail cap；
K5 coefficient L2-flat；
K6 gcd/unit strata；
K7 same formal unit；
K8 no promotable top-prime residue；
K9 no phase-residue mutual information。
```

每一项的失败出口均已命名：

```text
K2 fail => finite signature PDEC；
K3 fail => LocalSurvivor / SAE / refined PDEC；
K4 fail => ColumnCRT / tail-anchor PDEC；
K5 fail => coefficient concentration PDEC / SAE；
K6 fail => gcd-stratum PDEC or finite exception；
K7 fail => Multiplicity/Stitching absorption；
K8 fail => prime-lift deletion / NoDeletion router；
K9 fail => refined phase-residue PDEC。
```

因此真正的 clean 输入只在所有低维、列尾、升层、互信息峰都被剥离后出现。此时 A1 residual
可写成同一 formal unit 上的 Kloosterman/dispersion 型变量表：

```text
ell          => Kloosterman 可逆变量；
m            => 互补因子 / linear completion 变量；
d            => column displacement；
R            => CRT/gcd 剥离后的有效模数；
h            => 非零 Fourier/Bohr 频率；
W(m,ell)     => dyadic/smooth window；
a_ell,b_m    => L2-flat coefficients。
```

外部深定理版的闭合语义：

```text
接受窗口化 DI/BFI/Kuznetsov spectral/dispersion large sieve
=> clean A1 Kloosterman block = O(q/log^2 y)
=> 不能承载 q/log y 级 clean residual
=> A1 clean branch absorbed。
```

完全自足版的真实剩余：

```text
prove Kuznetsov-LS atom (SC-9)
```

也就是已有
`prime-matrix-h3-dsb-hlc-kls-core-self-contained-spine.md` 中的唯一未内联谱大筛原子。
前沿路由器同步更新后：

```text
A1CleanKLSExternalInput => external_kls_input_registered_self_contained_atom_open；
terminal_dual_gap => KuznetsovLSAtomSC9OrExternalCitation。
```

于是 A1 内部路由硬点已经不再是：

```text
NoDeletion-KL；
CleanKLS admission；
generic large sieve。
```

而是单一终端：

```text
Kuznetsov-LS atom (SC-9)，
或给出可复核的外部 DI/BFI/Kuznetsov 引用。
```

这一步仍不是完全自足行命题证明；它完成的是 A1 clean 分支到唯一谱大筛原子的硬压缩。

## 74. A1 Kuznetsov-LS 原子前沿压缩

新增 `experiments/prime_matrix_triad_a1_kuznetsov_ls_atom_frontier_router.py` 后，
第 73 节的 `Kuznetsov-LS atom (SC-9)` 不再只是一个大名词，而被接到既有谱链条的最窄阻断点。

机器结果：

```text
status=a1_sc9_frontier_routed_to_ncblk_or_external_dibfi；
all_sc9_subatoms_routed=True；
terminal_gap_after_router=NCBLKOrExternalDIBFIOriginalDispersion。
```

`SC-9` 已展开为：

```text
KZ-A: Kloosterman modulus smoothing and L2 bookkeeping；
KZ-B: Kuznetsov trace formula specialization；
KZ-C: Bessel transform window decay；
KZ-D: spectral large sieve with oldform/Eisenstein bookkeeping；
KZ-E: well-factorable dispersion logarithmic saving。
```

其中当前状态为：

```text
KZ-A => elementary smoothing closed；
KZ-B => trace specialization document closed；
KZ-C => Bessel decay document closed；
KZ-D => pretrace/spectral large-sieve chain closed；
KZ-E => reduced to NC-BLK or external DI/BFI。
```

KZ-E 内部路线已经排除的伪出口：

```text
BD-CEN identity:
  h=0 frequency centering is not same-(u,v) block centering；

SOURCE-CEN identity:
  changes the WFD target rather than rewriting it；

raw BLK-energy-core:
  false for arbitrary coefficient arrays by single-block single-atom test。
```

所以完全自足版的真实剩余不是：

```text
generic Kuznetsov；
generic spectral large sieve；
raw block energy；
source centering identity。
```

而是：

```text
NC-BLK:
prove actual WFD coefficients are block-nonconcentrated strongly enough
to give arbitrary logarithmic saving in the same-(u,v) block energy。
```

外部深定理版则为：

```text
cite original DI/BFI dispersion theorem
or an equivalent windowed Kloosterman spectral/dispersion theorem
that already contains the required block variance subtraction。
```

前沿路由器同步更新后：

```text
A1KuznetsovLSAtomFrontier => sc9_routed_to_ncblk_or_external_dibfi；
terminal_dual_gap => NCBLKOrExternalDIBFIOriginalDispersion。
```

这一步继续保持边界：没有宣称完全自足闭合；但已经把 A1 clean 分支从 `CleanKLS`、
`SC-9` 这样的大缺口压成一个具体可审稿命题 `NC-BLK`，或明确的外部 DI/BFI 引用义务。

## 75. A1 NC-BLK 投影缺口审计

新增 `experiments/prime_matrix_triad_a1_ncblk_projection_gap_router.py` 后，
第 74 节留下的 `NC-BLK` 被进一步检查其能否由 A1 diffuse 的 fixed-projection 平坦直接推出。

机器结果：

```text
status=ncblk_requires_moving_block_spread_or_external_dibfi；
fixed_projection_gap_exists=True；
current_internal_ncblk_closed=False；
terminal_gap_after_router=MovingBlockSpreadNCBLKOrExternalDIBFIOriginalDispersion。
```

核心发现：

```text
A1 diffuse branch controls fixed finite signatures；
NC-BLK asks for moving same-(u,v) block non-concentration；
fixed projection flatness does not control moving labels。
```

也就是说，沿无限层：

```text
每个固定有限投影原子质量趋零
```

并不能推出：

```text
所有随尺度移动的 balanced block b=(u,v) 都有 log^{-A} 块能量节省。
```

原因是 `(u,v)` 块标签随 `y,Q,R` 增长而移动；一个反例族可以避开任意固定投影检测，
却始终把责任转移到新的移动块上。这个缺口正是 `NC-BLK` 的真实内容。

当前已排除的内部伪路线仍然有效：

```text
BD-CEN identity 不成立；
SOURCE-CEN 会改变目标对象；
raw BLK-energy-core 被单块单原子测试阻断。
```

因此可接受的下一输入只有两类：

```text
MovingBlockSpread:
  从实际 WFD/Type-I-II/Fourier/well-factorable 系数来源证明
  每个 moving same-(u,v) block 的局部均值/块能量足够分散；

ExternalDIBFIOriginalDispersion:
  引用原始 DI/BFI dispersion 定理，且该定理必须直接处理未中心化 WFD 目标，
  或已经包含同 `(u,v)` 块局部方差扣除。
```

前沿路由器同步更新后：

```text
A1NCBLKProjectionGap => moving_block_spread_or_external_dibfi_required；
terminal_dual_gap => MovingBlockSpreadNCBLKOrExternalDIBFIOriginalDispersion。
```

这一步是负向但关键的硬推进：它排除了“fixed-projection flat => NC-BLK”的隐藏跳步，
把自足版最后硬点改写为更准确的 `MovingBlockSpreadNCBLK`。

## 76. A1 MovingBlockSpread 投影不可见性阻断

新增 `experiments/prime_matrix_triad_a1_moving_block_spread_obstruction.py` 后，
第 75 节的 `MovingBlockSpreadNCBLK` 被直接硬攻。结论是：它不能由当前 fixed-projection
diffuse ledger 自动推出。

机器结果：

```text
status=moving_block_spread_not_implied_by_fixed_projection_diffuse；
next_internal_target=SourceBlockEntropyNCBLK；
terminal_gap_after_router=SourceBlockEntropyNCBLKOrExternalDIBFIOriginalDispersion。
```

核心模型是投影不可见性：

```text
fixed projection ledger sees only total mass per fixed signature；
moving-block NC-BLK needs energy per growing block b=(u,v)；
hidden moving fibers can concentrate while fixed signatures keep diffusing。
```

具体地，对每个尺度取一批新 fixed signatures，每个 signature 下有随尺度增长的 hidden
moving-block fiber。构造两种模型：

```text
Spread model:
  每个 fixed signature 的质量均匀分散到 hidden moving blocks；

Concentrated model:
  每个 fixed signature 的质量集中到一个 moving block。
```

二者在 fixed-projection ledger 上相同，但 moving-block 二能量相差 `hidden_fiber_size` 倍。
并且 concentrated model 仍可让任意命名 fixed signature 最终不再出现，从而不违反
fixed-projection diffuse 语义。

这说明：

```text
fixed-projection diffuse
  does not imply arbitrary-log moving-block energy saving。
```

因此 `MovingBlockSpreadNCBLK` 还不是最终原子。真正内部目标变为：

```text
SourceBlockEntropyNCBLK:
actual WFD/Type-I-II/Fourier/well-factorable coefficients distribute over
moving same-(u,v) blocks with enough entropy to force block-energy log saving。
```

外部路线仍为：

```text
ExternalDIBFIOriginalDispersion:
引用原始 DI/BFI dispersion，且必须直接提供未中心化 WFD 目标的估计，
或包含同 `(u,v)` 块局部方差扣除。
```

前沿路由器同步更新后：

```text
A1MovingBlockSpreadObstruction => source_block_entropy_or_external_dibfi_required；
terminal_dual_gap => SourceBlockEntropyNCBLKOrExternalDIBFIOriginalDispersion。
```

这一步不是后退，而是排除另一个隐藏跳步：`fixed projection flat` 只控制可命名的固定签名，
不控制随尺度移动的内部 factorization block。继续无黑箱硬攻时，必须直接证明源头块熵。

## 77. A1 SourceBlockEntropy 条件闭合与形式输入阻断

新增 `experiments/prime_matrix_triad_a1_source_block_entropy_router.py` 后，
第 76 节留下的 `SourceBlockEntropyNCBLK` 被拆成一个正向闭合律和一个负向阻断律。

机器结果：

```text
status=source_block_entropy_not_forced_by_formal_wfd_inputs；
next_internal_target=ExactWFDSourceEntropy；
terminal_gap_after_router=ExactWFDSourceEntropyOrExternalDIBFIOriginalDispersion。
```

正向闭合律是：

```text
M_b = Cauchy capacity of moving block b=(u,v)
M   = sum_b M_b
if max_b M_b/M <= log(y)^(-2A), then
  sum_b |S_b|^2 <= sum_b M_b^2 <= log(y)^(-2A) M^2.
```

因此 `SourceBlockEntropyNCBLK` 是一个正确的充分条件：若能从实际源头系数证明每个 moving
same-`(u,v)` 块的容量份额都有任意对数小上界，则 `NC-BLK` 立即闭合。

但负向阻断同时说明：

```text
formal WFD/Type-I-II/Fourier inputs do not imply SourceBlockEntropyNCBLK.
```

原因是当前形式模板只提供：

```text
well-factorable convolution permits bounded point-supported factors at template level；
Type-I/II decomposition is algebraic and does not create block entropy；
Fourier smoothing controls h, not the moving block b=(u,v)；
fixed-projection diffuse cannot see a block label moving with the scale。
```

构造 moving-delta well-factorable 模型：每个尺度选择一个新的 `(u_y,v_y)`，令有界卷积因子
集中在该因子对上。它在形式 WFD 模板、Type 分块和 Fourier 平滑层面没有被禁止，却使

```text
max moving block capacity share = 1
```

从而与所需的

```text
max moving block capacity share <= log(y)^(-2A)
```

直接矛盾。该模型还可随尺度移动，避开所有固定有限投影检测。

所以当前终端被继续压缩为：

```text
ExactWFDSourceEntropy:
  prove the exact Rosser/Iwaniec-Buchstab + Type-I/II + Fourier coefficients
  cannot concentrate on a moving same-(u,v) block；

ExternalDIBFIOriginalDispersion:
  cite an original DI/BFI dispersion theorem that supplies the needed block variance saving directly.
```

前沿路由器同步更新后：

```text
A1SourceBlockEntropyRouter => exact_wfd_source_entropy_or_external_dibfi_required；
terminal_dual_gap => ExactWFDSourceEntropyOrExternalDIBFIOriginalDispersion。
```

这一步完成了 `SourceBlockEntropy => NC-BLK` 的条件证明，同时排除了“形式 well-factorable
结构自动给源头熵”的隐藏跳步。继续无黑箱硬攻时，不能再停留在抽象 WFD 模板，必须进入精确筛权
与 Type/Fourier 系数的反集中证明。

## 78. A1 ExactWFDSourceEntropy 化为精确因子支撑下界

新增 `experiments/prime_matrix_triad_a1_exact_wfd_source_entropy_router.py` 后，
第 77 节留下的 `ExactWFDSourceEntropy` 被继续压缩。关键发现是：这一步不再是谱相消问题；
若精确 well-factorable 因子在每个 surviving balanced block 内有足够支撑，则单块容量份额
自动为任意对数小。

机器结果：

```text
status=exact_wfd_source_entropy_reduced_to_factor_support_lower_bound；
next_internal_target=ExactFactorSupportLowerBound；
terminal_gap_after_router=ExactFactorSupportLowerBoundOrExternalDIBFIOriginalDispersion。
```

闭合律如下。令 `L=log y`，若

```text
|alpha_u|, |delta_v| <= L^C；
sum_u |alpha_u| >= U/L^C；
sum_v |delta_v| >= V/L^C；
```

则任一 moving pair 的容量份额满足

```text
max_{u,v} |alpha_u delta_v| / (sum|alpha| sum|delta|)
  <= L^(4C)/(UV).
```

因此若 balanced ranges 满足

```text
U,V >= L^B,   B >= A+2C,
```

就得到

```text
max moving block share <= L^(-2A),
```

从而推出：

```text
ExactFactorSupportLowerBound
  => ExactWFDSourceEntropy
  => SourceBlockEntropyNCBLK
  => NC-BLK.
```

当前仍未闭合的原因也很明确：

```text
当前 A1/KLS ledger 有 balanced dyadic range、divisor bound、fixed-residue L2-flat；
但没有逐 surviving balanced block 的 exact factor support lower bound；
K4 的 fixed-residue L2-flat 也不是 moving factor-pair support theorem。
```

所以新的最窄内部目标是：

```text
ExactFactorSupportLowerBound:
  for exact Rosser/Iwaniec-Buchstab factors and the attached Type/Fourier capacities,
  prove surviving balanced u- and v-ranges have enough absolute support/mass.
```

外部路线保持不变：

```text
ExternalDIBFIOriginalDispersion:
  cite a matched original DI/BFI dispersion theorem supplying the needed block variance saving.
```

前沿路由器同步更新后：

```text
A1ExactWFDSourceEntropyRouter => exact_factor_support_or_external_dibfi_required；
terminal_dual_gap => ExactFactorSupportLowerBoundOrExternalDIBFIOriginalDispersion。
```

这一步把“精确源头熵”从抽象熵命题降为初等但必须逐项证明的筛权支撑命题。继续无黑箱硬攻时，
下一步不应回到数值统计或谱大筛，而应证明精确筛权因子在平衡区间内不能退化为 moving atom。

## 79. A1 ExactFactorSupport 的 K4/K6 投影错配

新增 `experiments/prime_matrix_triad_a1_exact_factor_support_router.py` 后，
第 78 节留下的 `ExactFactorSupportLowerBound` 被继续审计。结论是：它不能由当前
`K4` residue-flat 和 `K6` dyadic-bookkeeping 自动推出。

机器结果：

```text
status=exact_factor_support_not_implied_by_k4_k6_without_incidence_bridge；
next_internal_target=FactorResidueIncidenceBridgeOrCanonicalRIWFactorSupport；
terminal_gap_after_router=FactorResidueIncidenceBridgeOrCanonicalRIWFactorSupportOrExternalDIBFIOriginalDispersion。
```

核心阻断是投影错配：

```text
K4 flatness lives on residue/phase atoms;
ExactFactorSupport lives on moving factor-pair atoms b=(u,v);
K6 limits the number of dyadic blocks, not the internal support of each block;
therefore K4+K6 need an incidence bridge before they can imply factor support.
```

构造模型如下：

```text
residue layer:
  有 log(y)^B 个 residue atoms，质量均匀分布，因此 K4-flat 成立；

factor-pair layer:
  所有 residue atoms 都来自同一个 moving factor pair (u_y,v_y)，
  因此 moving factor share = 1，ExactFactorSupport 失败。
```

这个模型不违背 K6，因为 K6 只限制 dyadic/tail-label 分块数为多对数级，并不说明每个 surviving
dyadic block 内部必须有多少 `u`、`v` 支撑。

因此当前可接受的内部输入只有两类：

```text
CanonicalRIWFactorSupportLowerBound:
  直接证明 exact Rosser/Iwaniec-Buchstab well-factorable factors
  在每个 surviving balanced block 内有 log-power 绝对支撑下界；

FactorResidueIncidenceBridge:
  证明若 moving factor support 太小，则必触发既有 K4 coefficient concentration
  或 K6 tail-label concentration，从而不能留在 clean branch。
```

外部路线仍为：

```text
ExternalDIBFIOriginalDispersion:
  原始 DI/BFI dispersion 直接提供 block variance saving，绕过内部支撑证明。
```

前沿路由器同步更新后：

```text
A1ExactFactorSupportRouter => factor_residue_incidence_or_canonical_riw_support_required；
terminal_dual_gap => FactorResidueIncidenceBridgeOrCanonicalRIWFactorSupportOrExternalDIBFIOriginalDispersion。
```

这一步排除了“residue 平坦 + dyadic 账本 = moving factor 支撑”的偷换。继续无黑箱硬攻时，
下一步必须证明因子-残基 incidence 桥，或直接证明 canonical Rosser-Iwaniec/Buchstab 因子支撑下界。

## 80. A1 FactorResidueIncidence 被内部 fiber 阻断

新增 `experiments/prime_matrix_triad_a1_factor_residue_incidence_router.py` 后，
第 79 节留下的 `FactorResidueIncidenceBridge` 被直接审计。结论是：朴素的 bounded-incidence
桥不能成立，因为一个 moving `(u,v)` 块内部本来就含有随尺度增长的 residue/phase fiber。

机器结果：

```text
status=factor_residue_incidence_bridge_blocked_by_internal_atom_fiber；
next_internal_target=CanonicalRIWFactorSupportLowerBound；
terminal_gap_after_router=CanonicalRIWFactorSupportLowerBoundOrExternalDIBFIOriginalDispersion。
```

内部 fiber 阻断律：

```text
one moving factor pair b=(u,v)
  contains many internal atoms (h, ell, x, z, completion labels);
mass can be flat on those internal K4 atoms
  while remaining concentrated on b;
therefore K4/K6 do not imply ExactFactorSupport through naive incidence.
```

也就是说，若某个 `(u_y,v_y)` 块承载全部 factor-pair 质量，它仍可以把质量均匀摊到该块内部的
`h,ell,x,z` 或 completion 原子上，使 K4 residue/phase 层看起来完全平坦。因此：

```text
small moving factor support
  does not force K4 coefficient concentration；
small moving factor support
  does not force K6 tail-label over-splitting。
```

K6 也不能排除它，因为该模型只使用一个 dyadic block，并没有产生过多分块。

所以当前无黑箱内部路线只剩一个真正入口：

```text
CanonicalRIWFactorSupportLowerBound:
  prove exact Rosser/Iwaniec-Buchstab well-factorable factors
  have broad balanced support in every surviving block.
```

外部路线仍为：

```text
ExternalDIBFIOriginalDispersion:
  原始 DI/BFI dispersion 直接提供 block variance saving。
```

前沿路由器同步更新后：

```text
A1FactorResidueIncidenceRouter => canonical_riw_factor_support_or_external_dibfi_required；
terminal_dual_gap => CanonicalRIWFactorSupportLowerBoundOrExternalDIBFIOriginalDispersion。
```

这一步把“从 clean K4/K6 反推 factor support”的最后伪出口排除。继续完全无黑箱硬攻时，
不能再依赖 residue 投影、dyadic 分块或 incidence 口径，必须直接证明 exact
Rosser-Iwaniec/Buchstab 因子本身的平衡支撑下界。
