# 三命题临界误差前沿审计与下一硬点压缩

## 0. 审计边界

本文基于当前仓库中的合著主稿和前沿研究文档，重新梳理三个目标命题的证明链条，并把最新的“无穷叠加筛、自反馈矛盾场、临界密度、临界误差”洞见转化为可审稿的下一步证明义务。

必须保持以下边界：

- Prime Matrix 行/列命题尚未无条件闭合；
- 二点筛/素数对方向尚未完全自足闭合，当前可达到的是外部 DI/BFI 深定理版的 BMD 分布输入闭合，终局仍需审查 `BMD=>TLI`；
- RH 矛盾场仍是 verification package，不能跳过 controlled exits 的逐行独立验证。

本文的新增贡献是把“临界密度”推进到“临界误差”层：反例若制造超过临界固定点可承载的局部覆盖或缺口，它不能以无名误差存在；它必须显化为某个已经登记的结构性缺陷，或暴露出一个新的、可命名、可审查的缺口。

## 1. 当前合著稿三条链的真实状态

### 1.1 Prime Matrix 行/列链

主稿已经把行/列反例放入统一 contradiction field：

```text
row/column counterexample
=> CRT skeleton + local rigidity
=> PDEC / ColumnCRT / SAE / Rankin / finite certificate exits
=> structured hard interfaces
```

最新前沿集中在 AffineTwin/fill-catchup 支线。已经完成的压缩是：

```text
threshold crossing
=> pressure packet
=> sqrt-product gate
=> Brun/Selberg twin reciprocal ceiling
   or SuperSqrt/PressureProduct-PDEC.
```

具体代数为：对 AffineTwin 模数 `q`，令

```text
g=q-2, f=q, M_q=A_g A_f.
```

安全门为

\[
M_q^2\le q(q-2).
\]

若安全门成立，则 SAE 质量

\[
\mu_q={M_q\over q(q-2)}
\le {1\over\sqrt{q(q-2)}}\le {1\over q-2},
\]

由 Brun/Selberg 二维上筛和分部求和吸收。若失败，则

\[
{A_g^2\over g}{A_f^2\over f}>1,
\]

这正是 `SuperSqrt/PressureProduct-PDEC`。

因此当前 Prime Matrix 最窄剩余不是笼统的“补洞太多”，而是：

```text
SuperSqrtPressureProductPDECExclusion
```

并行的去外部化工程是：

```text
SelfContainedBrunSelbergTwinReciprocalCeiling
```

### 1.2 二点筛链

二点筛的目标不是单点 `1/log x`，而是二禁类筛的临界密度：

\[
V_w(y)=\prod_{q\le y}\left(1-{\nu_q(w)\over q}\right)
\asymp {\mathfrak S(w)\over(\log y)^2}.
\]

旧硬点 `RB-TLI` 已经被压到更精确的 Buchstab semiprime transition：

```text
TLI
<= BST
<= BST-2
<= BMD
<= WBE2
<= BE2-3
<= BE2-3K
<= KLS-window
<= DI/BFI external package.
```

对最硬的 `w=2`，取 `Y=P^alpha` 且 `alpha>2/3`，若新大素数 `p in (Y,P]` 命中 `x` 或 `x-2`，互补商必须为素数。因此大素数命中层不是任意覆盖，而是半素数转移。

相应的两侧 Buchstab 主常数为

\[
K(\alpha)=
{2\log((2-\alpha)/\alpha)\over
1+\log((2-\alpha)/\alpha)}.
\]

例如：

```text
alpha=0.75: K=0.67622...
alpha=0.80: K=0.57698...
alpha=0.85: K=0.46423...
```

这给出巨大余量 `1-K(alpha)`。当前最后危险点不是局部 CRT，而是：

```text
BMD=>TLI transfer without hidden denominator/parity gap.
```

也就是说，外部 DI/BFI 可以关闭 BMD 分布输入，但仍必须证明从 BMD 到 TLI 的 Buchstab 转移没有偷偷使用目标素数对非空性。

### 1.3 RH 矛盾场链

RH 稿件已经把 off-critical zero 产生的 prime anomaly 接入 CRT rough-composite ledger：

```text
off-critical zero
=> smooth prime anomaly
=> CRT rough-composite excess
=> sparse/dense/tail/internal/global exits
=> GEE no-cycle ledger.
```

这条链的状态是 verification package。临界密度视角可解释异常来源：离线零点制造相对 `1/log x` 固定点的素数计数偏差；但终局证明仍取决于所有 controlled exits 是否在同一负载 convention 下逐项成立。

当前不能把 RH 线从“验证稿”提升为“无条件终稿”。

## 2. 临界误差的统一定义

临界密度回答的是平均固定点：

\[
\rho(x)\sim {1\over\log x}.
\]

临界误差回答的是局部反例超过固定点承载能力多少。统一写成：

\[
\mathcal E =
{\mathrm{actual\ load}\over \mathrm{critical\ capacity}}-1.
\]

若 `E<=0`，该层可由临界模型承载；若 `E>0`，必须出现结构性解释。

三条线的对应如下。

| 方向 | actual load | critical capacity | 临界误差 |
|---|---:|---:|---:|
| Prime Matrix AffineTwin | `M_q^2` | `q(q-2)` | `(A_g^2/g)(A_f^2/f)-1` |
| 二点筛 TLI | `E_{U_Y} D_Y^P` | `K(alpha)` 或终局门 `1` | `E D-K(alpha)` 与 `E D-1` |
| RH | routed anomaly load | named exit capacity | `Load(E)/Cap(E)-1` |

这个定义的作用是：不再允许“误差很大但没有结构”。一旦临界误差为正，它必须进入以下四类之一：

```text
fixed low/mid CRT defect       -> PDEC / ColumnCRT
moving high-factor slot mass   -> SAE / Rankin / Brun-Selberg / KLS
denominator or baseline collapse -> critical denominator defect
unclosed analytic route        -> controlled exit / external theorem interface
```

## 3. 核心原则：临界误差必须结构化

**CriticalErrorToStructuredDefect Principle.**
在已经做过零频主项扣除的 contradiction field 中，若某个反例产生正临界误差

\[
\mathcal E>0,
\]

则该误差不能作为匿名余项保留。它必须触发以下至少一个事件：

1. **固定相位复现。** 若同一低/中模相位反复承担误差，则形成 `PDEC/ColumnCRT`。
2. **移动槽质量不可求和。** 若相位不断移动以避免固定复现，则产生 `SAE/Rankin` 质量，或进入 Brun/Selberg/KLS 型平均抵消。
3. **分母临界坍缩。** 若实际幸存集低于 Buchstab/临界模型分母，则该负误差本身是低模相关缺陷，必须写成对偶筛证书。
4. **出口表不完备。** 若前三者都不发生，则当前 contradiction field 缺少一个出口；该失败形态必须被命名，而不是继续当作普通误差。

证明逻辑是能量/鸽巢级的：总误差先分解为零频、非零频固定相位和移动相位三部分。零频被临界主项扣除；非零频若集中，则有 Fourier/CRT 证书；若不集中，只能通过大量移动槽携带，而移动槽总质量必须进入可求和账本或外部平均定理。故正临界误差的唯一自由度是“显化为哪一种结构”，不是“是否显化”。

这条原则本身不是最终定理；它是三命题下一步共同的审稿骨架。

## 4. Prime Matrix 的新最窄攻击点

### 4.1 从 SuperSqrt 到相位支撑宽度

`SuperSqrtPressureProductPDECExclusion` 可以再压成一个更可攻的支撑宽度命题。

对每个 AffineTwin `q`，令 `S_q` 为 crossing 后仍未被 reset/ColumnCRT 吸收的 paired-side atoms。每个 atom 有一个合成相位投影

\[
\pi_q(a)\in \Omega_q,
\]

其中 `Omega_q` 是该 `q` 在非 PDEC 条件下允许承载的槽相位支撑。

若没有 PDEC/ColumnCRT，则同一投影不能被两个不同 atoms 复用；否则它们在模 `q(q-2)` 或其固定投影上给出同相位复现。因此有注入：

\[
S_q\hookrightarrow \Omega_q.
\]

于是若能证明非 PDEC 支撑宽度界

\[
|\Omega_q|\le \lfloor\sqrt{q(q-2)}\rfloor,
\]

立即得到

\[
M_q=|S_q|\le \sqrt{q(q-2)},
\]

从而关闭 SuperSqrt 分支。

### 4.2 失败形态已经命名

这一步的失败只有两种：

```text
projection collision
=> PDEC / ColumnCRT

wide support |Omega_q|>sqrt(q(q-2))
=> WideSupport-SAE / moving-slot mass
```

因此新的最窄命题应命名为：

```text
NonPDECSquareRootPhaseSupportBound
```

它比直接排斥 `SuperSqrt` 更窄：我们不再试图抽象地证明 `M_q` 小，而是证明“没有 PDEC 时可用相位槽本来就不超过平方根门”。

### 4.3 与无穷叠加筛的关系

无穷叠加筛的作用在这里具体化为：越往后，允许 atoms 同时避开所有旧模条件的相位支撑越窄；若还要不断移动以避免复现，则每次移动都支付新模或新槽质量。

也就是说，反例想要保持全覆盖，必须同时满足：

```text
支撑窄到不能容纳超平方根压力；
又宽到不发生相位碰撞；
又移动到不形成固定 PDEC；
又轻到不触发 SAE/Rankin。
```

这四个条件互相挤压，正是当前 Prime Matrix 线的临界误差矛盾点。

## 5. 二点筛的临界误差压缩

### 5.1 TLI 的两个临界门

对 `Y=P^alpha`，令

\[
D_Y^P(x)=\#\{Y<p\le P:p\mid x(x-2)\}.
\]

TLI 只需要

\[
{\mathbb E}_{x\in U_Y}D_Y^P(x)<1.
\]

Buchstab 主项预测

\[
{\mathbb E}_{U_Y}D_Y^P(x)=K(\alpha)+o(1),
\]

而 `K(alpha)<1`。所以二点筛的临界误差分成两层：

```text
main critical error:      ED - K(alpha)
terminal critical error:  ED - 1
```

只要证明主误差小于 `1-K(alpha)`，TLI 即闭合。

### 5.2 BMD 已控制分子，剩余是分母临界地板

BMD/KLS 路线控制的是双素变量在乘法曲线

\[
pm\equiv2\pmod d
\]

上的加权分布。它主要作用于大素数命中分子。

要从 BMD 推出 TLI，还需要独立确认：

\[
|U_Y(I)|\ge (1-\delta)\mathcal M_Y(I),
\]

其中 `M_Y(I)` 是同一 Buchstab/二禁类模型分母，且

\[
K(\alpha)+\varepsilon < 1-\delta.
\]

这就是新的最窄 H8 形态：

```text
CriticalDenominatorFloor + BMD numerator control => TLI.
```

如果分母地板失败，则失败本身不是普通误差，而是：

```text
old-prime two-residue critical denominator defect
```

它应当被对偶化为低模相关能量或筛权二次型缺陷。

### 5.3 分母失败的结构化证书

设 `1_{U_Y}` 由二禁类筛权近似。若

\[
|U_Y|<(1-\delta)\mathcal M_Y,
\]

则某个对偶筛权或二次型必须产生负偏差：

\[
\sum_{d_1,d_2\le D}
\lambda_{d_1}\lambda_{d_2}
R(\operatorname{lcm}(d_1,d_2))
\le -c\delta\mathcal M_Y.
\]

该偏差只能来自：

```text
low-mod CRT correlation
character/Fourier spectrum
endpoint smoothing concentration
or parity-level insufficiency of the chosen sieve weights.
```

前三者可并入 `PDEC/ColumnCRT/KLS-window` 类型的结构缺陷；第四者则说明当前筛权无法给出所需分母地板，必须被登记为 `ParityTransferGap`，不能伪装成已闭合。

因此二点筛下一步不应再改名，而应直接证明或登记：

```text
BMDToTLI-CriticalDenominatorFloor
```

## 6. RH 线的临界误差定位

RH 线中，off-critical zero 给出

\[
\Delta=X^{\beta-o(1)},\qquad \beta>1/2.
\]

这是相对平方根临界误差的正幂超额。经过 CRT rough-composite ledger 后，它必须进入 `LV/NRC/PI/DSO/CE/LSMP/FCT/SC/A` 等出口。

临界误差视角给出的审稿要求是：

```text
每个 exit 的 capacity 必须用同一 baseline-subtracted load convention 表述；
每个 transfer 必须 source-deleting；
每个 internal descent 必须有严格下降势；
每个 analytic tail 必须有可求和或外部定理来源；
最终 no-cycle ledger 不能调用未闭合的 Prime Matrix 或二点筛结论。
```

若某个出口只能在“平均上看似可控”但没有同一负载 convention 下的定理，就不能把 RH 稿件提升为无条件终稿。

## 7. 统一矛盾场矩阵

| 临界误差来源 | 固定相位出口 | 移动相位出口 | 解析平均出口 | 尚未闭合硬点 |
|---|---|---|---|---|
| PM AffineTwin pressure product | `PDEC/ColumnCRT` | `SAE/Rankin` | Brun/Selberg twin reciprocal | `NonPDECSquareRootPhaseSupportBound` |
| PM low/mid endpoint defect | `LowMod/PDEC` | endpoint SAE | finite/Rankin certificate | exact endpoint/global constants |
| TP numerator large incidence | BMD-Zero | BMD-Char | DI/BFI -> KLS-window | BMD external/self-contained status |
| TP denominator collapse | denominator PDEC | smoothing/endpoint defect | beta/Buchstab lower sieve | `CriticalDenominatorFloor` |
| RH prime anomaly | CRT/PI/FCT/SC | CE/LSMP/LV/DSO | explicit formula, Vaaler, GEE | controlled exits referee verification |

这个矩阵的价值是把“反例链与真实链的矛盾”统一为一个判断：

```text
正临界误差是否有合法承载通道？
```

若没有，反例不存在；若有，则该通道必须成为下一硬点，而不是换命题。

## 8. 本轮得到的下一步证明目标

### 8.1 Prime Matrix

最值得直接攻的命题是：

```text
NonPDECSquareRootPhaseSupportBound.
```

证明格式：

1. 定义每个 AffineTwin `q` 的非 PDEC paired atom 投影 `pi_q`；
2. 证明无 PDEC 时 `pi_q` 注入；
3. 证明非 PDEC 相位支撑 `Omega_q` 的宽度不超过 `sqrt(q(q-2))`；
4. 推出 `M_q^2<=q(q-2)`；
5. 剩余 moving 包由 Brun/Selberg 或自足二维上筛吸收。

失败即：

```text
ProjectionCollision-PDEC
or WideSupport-SAE.
```

### 8.2 二点筛

最值得直接攻的命题是：

```text
BMDToTLI-CriticalDenominatorFloor.
```

证明格式：

1. 用 BMD/KLS 给出分子大素数命中上界；
2. 用同一 Buchstab convention 给出 `U_Y` 分母地板；
3. 检查 `K(alpha)+epsilon < 1-delta`；
4. 若分母地板失败，把失败转成低模二次型/character defect，而不是隐藏在 parity barrier 中。

### 8.3 RH

最值得直接攻的工作不是新增直觉，而是：

```text
ControlledExitCriticalLoadNormalization.
```

证明格式：

1. 把所有 exits 的 load 写成同一 baseline-subtracted 量；
2. 对每个 exit 给出 capacity 或 strict descent；
3. 证明 transfer source-deleting；
4. 检查 final no-cycle ledger 不引用未闭合命题。

## 9. 当前结论

本轮没有宣称三个命题已经无条件闭合。真正推进是：

```text
临界密度固定点
=> 临界误差正负门
=> 正临界误差必须结构化
=> 三条线各自压到最窄可审稿接口
```

最新最窄主攻点为：

```text
Prime Matrix:
  NonPDECSquareRootPhaseSupportBound

Two-point sieve:
  BMDToTLI-CriticalDenominatorFloor

RH:
  ControlledExitCriticalLoadNormalization
```

这三个接口是同一个矛盾场的三个投影：反例必须制造超临界误差，而真实结构链要求超临界误差显化为固定相位、移动质量、解析平均或受控出口。若每个出口都被排除或吸收，反例链即与真实链直接矛盾。

## 10. Prime Matrix 本轮续钻更新

后续文件

```text
docs/monograph/prime-matrix-nonpdec-sqrt-phase-support-reduction.md
```

把第一项 `NonPDECSquareRootPhaseSupportBound` 再压窄为 actual packet 版本。

关键修正是区分：

```text
M_q^{form}=A_g A_f   形式 residue 配对上界
N_q                  实际非 PDEC pressure packet 数
```

临界误差应使用 actual load：

\[
\mathcal E_q={N_q^2\over q(q-2)}-1,
\]

而不是自动使用可能过粗的 `M_q^{form}`。对 primitive AffineTwin 双槽，已有相位锁给出

\[
W_q={q+9\over2}.
\]

且对 `q>=13`，

\[
W_q\le\sqrt{q(q-2)}.
\]

因此只要证明每个 actual non-PDEC packet 都落入 primitive 双槽支撑，并且同一投影复现已经路由为 PDEC/ColumnCRT，就得到：

\[
N_q\le W_q\le\sqrt{q(q-2)}.
\]

于是形式 SuperSqrt 失败只剩三种解释：

```text
ProductAccountingTightening       形式上界过粗，不是实际负载；
ProjectionCollision-PDEC          actual packets 投影碰撞；
PrimitiveTwinSlotSupportEscape    actual packet 逃出 primitive 支撑。
```

所以 Prime Matrix 最新最窄硬点从

```text
NonPDECSquareRootPhaseSupportBound
```

进一步变成：

```text
PrimitiveTwinSlotSupportExhaustion
+ ProductAccountingTightening
+ PrimitiveTwinSlotSupportEscape-PDEC/SAE routing.
```

这仍未闭合行/列命题，但它把超平方根压力从“抽象乘积过大”压成了“实际包是否全部落在可注入相位支撑内”的更窄问题。
