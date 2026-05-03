# H4-PDEC 证书模板与验收定理

**状态：** `h4_pdec_certificate_template_completed_not_filled`

本文把 H4 的 persistent endpoint CRT defect 排斥任务固定为一个可提交、可复核、不可越界的证书格式。它不宣称 `PDEC` 已被排除；它只规定什么数据与什么不等式足以排除一个给定 persistent 分支。

## 1. 输入对象与量词

一个 `PDEC-Cert` 必须对应一个已经从正式反例链抽取出的 persistent 低模缺陷块 `B`。证书输入为：

```text
Q        : 低模周期，Q>=2；
X        : 坏窗所在的有限索引域；
tau      : 相位映射 X -> Z/QZ；
S        : persistent 坏窗集合或多重集合；
g(t)     : #{x in S: tau(x)=t}；
F        : Z/QZ 上的零均值测试函数；
kappa    : 正数，满足 Re F(tau(x))>=kappa for x in S；
||F||_2  : 与 Fourier 归一化一致的 L2 范数。
```

这里 `S` 必须是同一个坏窗集合。不能用全 CRT 周期背景集合、近似替代集合或另一个方便集合来证明上界。

## 2. PDEC 下界引理

采用 `prime-matrix-bpn-pdec-dual-certificate-framework.md` 的归一化 Fourier 约定。若 `F` 零均值且

\[
\Re\sum_{x\in S}F(\tau(x))\ge \kappa |S|,
\]

则存在非零频率 `h` 使

\[
\max_{h\ne0}|\widehat g(h)|
\ge
L_{\rm PDEC}
:=
\frac{\kappa |S|}{\sqrt{Q-1}\,\|F\|_2}.
\]

**证明。**
把左侧写成相位计数向量与测试函数的内积。因 `F` 零均值，常数频率消失，只剩 `Q-1` 个非零频率。由 Cauchy--Schwarz 与
\[
\sum_{h\ne0}|\widehat F(h)|
\le \sqrt{Q-1}\,\|F\|_2
\]
得到
\[
\kappa |S|
\le
\max_{h\ne0}|\widehat g(h)|\sqrt{Q-1}\,\|F\|_2.
\]
移项即得结论。若脚本采用未归一化 Fourier，必须同时换算 `L_PDEC` 与 `U_CRT`，不能混用常数。

## 3. 上界证书的线性约束

对偶证书使用变量 `g(t)>=0` 的实数松弛。每条线性约束必须附来源标签：

```text
mass       : sum_t g(t)=|S|；
mirror     : 边界两端帽镜像刚性；
column     : P 列非零同余类均衡与列见证；
tail       : 尾锚不可复用容量；
core       : 固定核心高重叠回流；
rankin     : Rankin 失败低模尖峰路由；
rrd_ospc   : H5.1/H5.4 吸收后的 OSPC* 或 weighted CRTDefect 路由。
```

形式上写为

\[
Ag\le b,\qquad Eg=e,\qquad g(t)\ge0.
\]

每一行 `A_i,b_i` 或 `E_j,e_j` 都必须能回指到独立引理、有限证书或外部定理模板。没有来源证明的约束只能标为 heuristic，不能进入正式 `PDEC-Cert`。

## 4. 对偶主控验收

对每个非零频率 `h` 与每个方向 `zeta`，定义

\[
c_{h,\zeta}(t)=\Re\{\zeta e^{2\pi iht/Q}\}.
\]

若存在 `lambda>=0` 与自由变量 `mu`，使逐相位成立

\[
c_{h,\zeta}(t)
\le
(A^\top\lambda)(t)+(E^\top\mu)(t)
\]

且

\[
\lambda\cdot b+\mu\cdot e\le U_{\rm CRT},
\]

则所有满足约束的 `g` 都满足

\[
\Re\{\zeta\widehat g(h)\}\le U_{\rm CRT}.
\]

若该主控覆盖全部 `h!=0` 与全部方向，并且

\[
U_{\rm CRT}<L_{\rm PDEC},
\]

则该 persistent 分支被排除。

## 5. 连续方向的两种合法处理

方向 `zeta` 是连续对象，不能只用有限角度网格直接替代。正式证书只能采用以下两种之一：

1. **解析对偶权重。** 给出依赖 `zeta` 的闭式 `lambda,mu`，逐方向成立。
2. **外向角弧证书。** 用有限角弧覆盖单位圆，并把角弧半径造成的 Lipschitz 误差写入 `U_CRT`。

外向角弧证书必须提供角弧端点、半径、误差上界和严格余量。所有浮点输出必须有有理或区间外向舍入版本。

## 6. 两类可提交证书

`PDEC-Explicit-Cert` 适用于有限候选或正式反例链实际抽出的 `S`：

```text
给出完整 g(t)；
精确计算 max_{h!=0}|g_hat(h)|；
核验 max<U_CRT<L_PDEC。
```

`PDEC-Dual-Cert` 适用于无限族：

```text
证明 A,b,E,e 覆盖全部允许坏窗；
给出所有 h 和方向的 lambda,mu；
核验逐相位不等式与 U_CRT<L_PDEC。
```

当前仓库中的 `prime-matrix-bpn-pdec-dual-certificate-audit.json` 是对偶审计样例，只证明给定线性系统与给定方向证书通过；它不是无限族闭合证书。

## 7. 失败输出与回流规则

若 `PDEC-Cert` 不能通过，失败不能被口头吸收。必须输出：

```text
失败频率 h；
失败方向 zeta 或角弧；
造成 U_CRT>=L_PDEC 的相位主贡献；
缺失或过松的约束行；
该失败应回流到 SAE、Rankin low-mod spike、tail-anchor 或新的 PDEC 约束行。
```

这保证 H4 的下一步攻坚对象是具体不等式，而不是新的未定义出口。

## 8. 当前未闭合项

本模板完成后，H4-PDEC 仍有三项必须补齐：

1. 对正式 persistent 坏窗族逐条证明 `A,b,E,e` 的结构来源；
2. 为全部非零频率与连续方向提交显式或对偶证书；
3. 用同一 Fourier 归一化核验严格余量 `U_CRT<L_PDEC`。

只有这三项全部完成后，才能把 `PDEC exclusion` 从最终硬输入升级为已排除分支。
