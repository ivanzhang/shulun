# BD-CEN：当前对象下的反证与路线分叉

**状态：** `bd_cen_refuted_for_current_unblocked_wfd_object`

本文继续只攻击同一个最窄目标：

```text
BD-CEN identity (BDC-5).
```

目标是判断它能否在当前 KZ-E/WFD 对象下被证明。结论是严格否定：

```text
在当前对象和当前 admissible 系数范围内，BD-CEN 不是未证引理，而是错误身份。
```

原因很简单：`h=0` 主项抵消只是在频率坐标上中心化；`BD-CEN` 要求在模数块 `b=(u,v)` 上
扣除整块局部方差。这两个投影不相同。若允许单个块非零，`(BDC-5)` 立即失败。

## 1. 抽象模型

设平方前的和为

\[
\mathcal S=\sum_{b\in\mathcal B}\sum_{\theta\in\Theta_b} a_{b,\theta},
\tag{BDN-1}
\]

其中：

- `b=(u,v)` 是块索引；
- `\theta` 汇总 `h,\ell,x,z` 等块内变量；
- 当前 KZ-E 只删除 `h=0`，所以 `\Theta_b` 中仍包含所有 `h\ne0` 的块内变量。

记

\[
\mathcal S_b=\sum_{\theta\in\Theta_b}a_{b,\theta}.
\tag{BDN-2}
\]

则恒等式是

\[
|\mathcal S|^2
=
\sum_b|\mathcal S_b|^2
+
\sum_{b\ne b'}\mathcal S_b\overline{\mathcal S_{b'}}.
\tag{BDN-3}
\]

`BD-CEN` 要求真实对象等于第二项：

\[
\mathcal E_{\rm centered}
=
\sum_{b\ne b'}\mathcal S_b\overline{\mathcal S_{b'}}.
\tag{BDN-4}
\]

这等价于原始 dispersion 在进入平方核前已经扣除了

\[
\sum_b|\mathcal S_b|^2.
\tag{BDN-5}
\]

## 2. 反例：单块非零

取一个块 `b_0`，并取一个非零块内频率 `\theta_0`，满足 `h(\theta_0)\ne0`。令

\[
a_{b_0,\theta_0}=1,\qquad
a_{b,\theta}=0\quad\text{otherwise}.
\tag{BDN-6}
\]

则

\[
\mathcal S=1,\qquad
|\mathcal S|^2=1.
\tag{BDN-7}
\]

但跨块项为

\[
\sum_{b\ne b'}\mathcal S_b\overline{\mathcal S_{b'}}=0.
\tag{BDN-8}
\]

所以 `(BDN-4)` 失败。注意该反例没有使用 `h=0`；它完全位于非零频率层。因此
`h=0` 主项抵消不能补救块中心化。

## 3. 投影不交换造成的结构性失败

令 `P_0` 为 `h=0` 投影，`P_{\rm blk}` 为同块对角投影。当前 KZ-E 已证明的中心化是

\[
1-P_0.
\tag{BDN-9}
\]

`BD-CEN` 需要的是

\[
1-P_{\rm blk}.
\tag{BDN-10}
\]

对任意含有两个以上非零频率的同一块，存在向量 `a` 使得

\[
(1-P_0)a=a,\qquad
P_{\rm blk}a=a.
\tag{BDN-11}
\]

于是

\[
(1-P_0)a\ne (1-P_{\rm blk})a.
\tag{BDN-12}
\]

这不是估计强弱问题，而是对象不同。

## 4. 对当前链条的结论

在当前 WFD/BSC/KFLS 链条中，`BD-CEN` 不能作为“待证明但合理”的恒等式保留。它只有两种
可能来源：

1. 原始 dispersion 定义显式引入了块条件均值扣除；
2. admissible 系数类禁止单块非零，并额外证明块能量也有对数节省。

当前文档都没有这两项。因此：

\[
\boxed{\text{BD-CEN is false for the current unblocked WFD object.}}
\tag{BDN-13}
\]

## 5. 路线分叉

当前无黑箱路线必须在这里分叉。

### 路线 A：SOURCE-CEN

回到最原始 dispersion 变量，重新定义误差为块条件中心化误差：

\[
F_{b,\theta}^{\circ}
=
F_{b,\theta}
-
\mathbb E(F_{b,\cdot}\mid b).
\tag{BDN-14}
\]

若能证明原命题使用的正是 `F^\circ`，则 `BD-CEN` 可成立。但这会要求重新核查 KZ-E 第 3 节
的 dispersion 恒等式，而当前文档尚未给出。

### 路线 B：BLK-energy-core

不删除块对角，而是直接证明

\[
\sum_b|\mathcal S_b|^2
\ll_A
{\mathcal B(UV,S,H)^2\over\log^{2A}y}.
\tag{BDN-15}
\]

但该路线在当前“任意 admissible 系数”范围下也被单块反例阻断。若要走此路，必须先新增
非集中条件，例如：

```text
no single (u,v) block can carry more than log^{-A} of the square norm.
```

当前链条没有这样的条件。

### 路线 C：外部 DI/BFI

允许引用 DI/BFI 原始 dispersion 定理，并逐项核对其定理陈述是否已经包含了块局部方差扣除
或绕过了本平方核分解。若引用版成立，它是 external-theorem closed，不是当前完全自足闭合。

## 6. 审稿结论

本步完成最窄目标的直接硬攻：

```text
BD-CEN cannot be proved from the current KZ-E/WFD object.
```

因此当前第一阻断点不再应写成“证明 BD-CEN”，而应写成：

```text
choose and prove SOURCE-CEN, or prove a new non-concentration hypothesis for BLK-energy-core,
or explicitly switch to external DI/BFI.
```

在这三者之一完成前，不能继续声称平方核路线可通向完全自足无黑箱证明。
