# BPN 最终剩余攻坚稿

**状态：** `final_residual_reduced_not_closed`

本文只处理 `BPN-BK/Selberg` 主链的最终剩余。当前不能再把剩余写成新的模糊命题；
所有未闭合项必须落到三类可审稿证书：

```text
PDEC-Cert；
SAE-Cert；
formal Rankin certificates。
```

## 1. 当前已闭合的归约链

已完成的主链为：

```text
边界零行
=> BK-DEC 或 TailCoreBucket/CoreK-Density
=> Directed Endpoint CRTDefect / Tail-anchor / Distributed corridor saturation
=> PDEC/SAE 或 finite Rankin ledger
```

其中：

- `BK-DEC=>Directed Endpoint CRTDefect` 已由端点 sawtooth 分块鸽巢闭合；
- `Tail-anchor concentration` 已并回 `PDEC/SAE`；
- `Distributed corridor saturation` 已拆成高重叠固定核心缺陷或着色不相交走廊预算；
- low-mod core CRTDefect 已经由 Fourier 反演并入统一 `PDEC/SAE`。

因此剩余不是“再证明一个新二分”，而是提交最终排斥证书。

## 2. PDEC 的最小非循环目标

设低模缺陷给出测试函数 `F`，坏窗集合 `S` 满足

\[
\Re F(\tau(x))\ge \kappa,\qquad x\in S.
\]

Fourier 展开已经给出下界

\[
\max_{h\ne0}|\widehat{1_S}(h)|
\ge
\mathcal L_{\rm PDEC}
=
\frac{\kappa |S|}{\sqrt{Q-1}\|F\|_2}.
\]

所以 PDEC 排斥的唯一有效形态是证明同一坏窗指示函数满足

\[
\max_{h\ne0}|\widehat{1_S}(h)|
\le
\mathcal U_{\rm CRT}
<
\mathcal L_{\rm PDEC}.
\]

这一步不能只引用全周期 CRT 均衡。全周期均衡只说明完整周期平均为零，不能排除短边界帽
中存在一个集中坏窗集合。必须使用坏窗由边界零行诱导出的额外结构，例如：

```text
镜像两端帽约束；
列非零同余类均衡；
尾锚不可复用；
固定核心高重叠回流；
正式走廊 Rankin 证书失败时的低模尖峰登记。
```

**最小硬核 PDEC-Upper。**
对每个由 endpoint/core 低模缺陷诱导的坏窗族，证明上述五类结构约束合并后给出
`U_CRT<L_PDEC`。若做不到，必须输出造成失败的具体低模角色、相位和坏窗族。

## 3. SAE 的最小孤窗目标

Sparse 分支不能靠 Fourier 能量自动排除。每个孤立坏窗 `I` 必须满足三选一：

```text
Survivor:
  明确给出 n in I 且 gcd(n,M_<P)=1；

Lift:
  证明 I 的同相位或相邻漂移窗复现，升级为 PDEC；

Higher-defect:
  证明 I 触发尾锚复用、固定核心高重叠或 low-mod core CRTDefect。
```

这里 Sylvester 大因子输入仍不够：它只保证某个数有 `>P` 的素因子，不能排除该数同时含
`<P` 小因子。因此 `SAE-Survivor` 必须附带“小因子排除”或“若有小因子则触发
higher-defect”的证据。

**最小硬核 SAE-Window。**
对每个孤立坏窗构造有限账本：

\[
\text{small-factor blockers}
+\text{tail-anchor blockers}
+\text{core-overlap blockers}
<
|I|.
\]

若该不等式失败，则失败项必须可命名为 higher-defect 并回流到 PDEC。

## 4. Rankin 证书的接入规则

正式着色走廊只接受以下结果：

```text
rankin_budget_pass=true
  => 该颜色类闭合；

rankin_budget_pass=false 且有 low-mod spike
  => low-mod core CRTDefect
  => PDEC/SAE；

rankin_budget_pass=false 且无 spike
  => 常数账本未闭合，必须细分或调参。
```

因此 Rankin 失败不能被口头吸收。它必须变成低模缺陷证书，或保留为明确常数缺口。

## 5. 下一步实际攻坚顺序

最优顺序是：

1. 从正式反例链抽取全部着色走廊列表，生成 Rankin certificate 输入；
2. 对未通过颜色类抽取最大低模尖峰，登记为 low-mod core CRTDefect；
3. 对持续低模缺陷块构造 `PDEC-Cert` 的 Fourier 上界账本；
4. 对剩余孤立坏窗逐个构造 `SAE-Cert`；
5. 只有当三类证书全集通过后，才可把 `BPN(P)` 升级为无条件结论。

当前结论：最终剩余已经证书化，但尚未无条件闭合。

## 6. PDEC 上界的下一层突破

补充文档 `prime-matrix-bpn-pdec-dual-certificate-framework.md` 已把第 3 步继续细分为两类
可审稿证书：

```text
PDEC-Explicit-Cert:
  对具体坏窗相位计数向量 g 直接计算 max_{h!=0}|g_hat(h)|；

PDEC-Dual-Cert:
  对所有满足镜像、列均衡、尾锚不可复用和 Rankin 回流约束的 g，
  用线性对偶主控证明统一 Fourier 上界。
```

脚本 `experiments/prime_matrix_bpn_pdec_certificate_audit.py` 已提供显式证书审计层。它不解决
无限族，但把有限候选和正式反例抽取结果变成可复核的 `U_CRT<L_PDEC` 检查。

## 7. PDEC 对偶约束账本

最新补充 `prime-matrix-bpn-pdec-constraint-ledger.md` 与
`experiments/prime_matrix_bpn_pdec_dual_certificate_audit.py` 后，下一层硬点进一步缩窄为：

```text
把 mirror / column / tail-anchor / core-overlap / Rankin-routing
五类结构约束逐条写成 A,b,E,e；
为每个 h,zeta 提交 lambda,mu 对偶证书；
机器核验逐相位主控和 U_dual<L_PDEC。
```

这一步仍不是无条件闭合；它把“PDEC 上界”变成了可逐行审稿、可机器检查的有限证书格式。
