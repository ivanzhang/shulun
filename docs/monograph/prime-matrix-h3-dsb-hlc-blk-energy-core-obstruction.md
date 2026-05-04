# BLK-energy-core：块能量出口的无黑箱核查与阻断

**状态：** `blk_energy_core_requires_new_nonconcentration_input`

本文继续只攻击 `SOURCE-CEN` 被反证后的当前最窄无黑箱目标：

```text
BLK-energy-core:
prove the same-(u,v) block mean / block energy has arbitrary logarithmic saving.
```

结论是：

```text
裸 BLK-energy-core 不能从当前 WFD/KZ-E 的 admissible 系数范围推出；
若要保留内部路线，必须新增并证明真实系数的块非集中定理 NC-BLK。
```

这一步不是改换命题，而是把“块能量可直接估小”这个最后接口拆成一个可审稿的必要条件。

## 1. 当前块能量对象

沿用 `BD-CEN` 与 `SOURCE-CEN` 文件的记号。平方前对象可写为

\[
\mathcal S=\sum_{b}\mathcal S_b,\qquad
\mathcal S_b=\sum_{\theta\in\Theta_b}A_{b,\theta}e(\Phi_{b,\theta}),
\tag{BEC-1}
\]

其中

\[
b=(u,v)
\tag{BEC-2}
\]

是平方根 well-factorable 分解后的模数块。平方核恒等式为

\[
|\mathcal S|^2
=
\sum_b|\mathcal S_b|^2
+
\sum_{b\ne b'}\mathcal S_b\overline{\mathcal S_{b'}}.
\tag{BEC-3}
\]

同块项

\[
\mathcal E_{\rm blk}:=\sum_b|\mathcal S_b|^2
\tag{BEC-4}
\]

就是 `BD-CEN` 想扣除、`SOURCE-CEN` 想在源头消去、`BLK-energy-core` 想直接估小的对象。

裸 `BLK-energy-core` 至少需要给出如下强度：

\[
\mathcal E_{\rm blk}
\ll_A
{\mathcal B(UV,S,H)^2\over \log^{2A}y},
\tag{BEC-5}
\]

其中 `\mathcal B(UV,S,H)` 是上一层 raw 二范数尺度；它不能隐藏额外的 `\log^{A}y`
放大，否则取平方根后不能回收 KZ-E 所需的任意对数节省。

## 2. 单块阻断

**引理 BEC-1。** 若 `BLK-energy-core` 被表述为对平方核层任意形式系数数组成立，
则 `(BEC-5)` 不成立。

**证明。** 取一个 admissible 块 `b_0`，并取块内一个允许频率 `\theta_0`，令

\[
A_{b_0,\theta_0}=1,\qquad
A_{b,\theta}=0\quad\text{otherwise}.
\tag{BEC-6}
\]

该测试只使用一个非零 `h`、一个 `s` 或 completion 变量和一个模数块。它是平方核层
`A_{b,\theta}` 形式命题的合法稳定性测试。若坚持原始 well-factorable 筛权或平滑频率权不允许
如此集中，则这正是一个必须从上游逐行证明的额外非集中输入，不能在平方核层免费假设。

于是

\[
\mathcal S_{b_0}=e(\Phi_{b_0,\theta_0}),\qquad
\mathcal E_{\rm blk}=1.
\tag{BEC-7}
\]

而 raw 二范数尺度在该单原子测试上同阶为

\[
\mathcal B(UV,S,H)^2\asymp 1
\tag{BEC-8}
\]

至多差一个固定结构常数或多对数账本。令 `A` 任意增大，`(BEC-5)` 将要求

\[
1\ll_A \log^{-2A}y,
\tag{BEC-9}
\]

当 `y` 足够大时矛盾。证毕。

## 3. 正性阻断

更强地，`(BEC-4)` 是非负平方和。把块内权重吸入 `A_{b,\theta}` 后，记归一化块均值为

\[
\mu_b={1\over W_b}\sum_{\theta\in\Theta_b}A_{b,\theta}e(\Phi_{b,\theta}),
\tag{BEC-10}
\]

则有精确恒等式

\[
\sum_b|\mathcal S_b|^2
=
\sum_b W_b^2|\mu_b|^2.
\tag{BEC-11}
\]

因此块能量不含跨块相位差。它只能依赖每个块内部的真实相消；不能由 `OSQK-core` 或
`TFQK-core` 的跨块振荡事后补救。若没有源头中心化，也没有真实块内非集中定理，正性项
不会自动给出任意 `\log^{-A}`。

## 4. 合法替代：NC-BLK

当前内部路线若不引用外部 DI/BFI，必须把 `BLK-energy-core` 替换为一个真实可证明的上游输入：

**NC-BLK（block non-concentration theorem）。** 对 KZ-E/WFD 中实际产生的系数和相位，而非任意
抽象 admissible 单原子，证明

\[
\sum_{u\sim U}\sum_{v\sim V}
\left|
\sum_{\theta\in\Theta_{u,v}}
A_{u,v,\theta}e(\Phi_{u,v,\theta})
\right|^2
\ll_A
{\mathcal B(UV,S,H)^2\over \log^{2A}y}.
\tag{BEC-12}
\]

要证明 `(BEC-12)`，必须至少给出以下一项真实结构：

1. **系数非集中。** 上游 Type-I/II、Fourier 与 well-factorable 卷积强制每个 `(u,v)` 块内有
   足够多互异相位，且不能退化为单块单原子；
2. **块内谱相消。** 对固定 `(u,v)` 的 `h,s` 或 completion 变量建立平均抵消，而不是只在
   不同块之间抵消；
3. **原始 dispersion 定理。** 从 DI/BFI 型原始方差定理直接得到 `(BEC-12)` 或绕过
   `(BEC-4)`。

这些都不是当前文档已有恒等式。

## 5. 审稿结论

本步完成 `BLK-energy-core` 的最窄无黑箱核查：

```text
raw BLK-energy-core is false as an arbitrary coefficient-array theorem.
```

因此在 `BD-CEN` 与 `SOURCE-CEN` 均被反证后，当前完全自足路线的唯一内部剩余不是“直接证明
裸块能量估计”，而是：

```text
NC-BLK:
prove actual WFD coefficients are block-nonconcentrated strongly enough to imply (BEC-12).
```

若不能证明 `NC-BLK`，则只能把 H3-HLC/KZ-E 标为：

```text
external-theorem closed via a precisely matched DI/BFI dispersion theorem,
not self-contained closed.
```

这把当前剩余义务压缩到一个真实、可逐行审查的最窄接口：证明实际系数的块内非集中，或者
承认该部分依赖外部深定理。
