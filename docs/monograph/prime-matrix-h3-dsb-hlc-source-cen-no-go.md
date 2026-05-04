# SOURCE-CEN：源头块中心化核查与反证

**状态：** `source_cen_refuted_for_current_wfd_target`

本文继续只攻击当前无黑箱路线的最窄目标：

```text
SOURCE-CEN: 原始 KZ-E/WFD 对象是否已经是同 (u,v) 块条件中心化对象。
```

结论是严格否定：

```text
当前 WFD-core (KE-13) 是未块中心化的线性 Kloosterman 窗口；
SOURCE-CEN 会改变目标对象，不能作为等价恒等式加入。
```

因此，在 `BD-CEN` 被反证后，`SOURCE-CEN` 也不能闭合当前无黑箱平方核路线。剩余内部路线只
剩更强的 `BLK-energy-core`，或明确改用外部 DI/BFI 原始 dispersion 定理。

## 1. 当前 WFD-core 的对象

当前 KZ-E spine 中的剩余核是

\[
\mathcal W
=
\sum_{c\sim C}\lambda_c
\sum_{0<|h|\le H}\omega_h
\sum_{\substack{s\sim S\\(s,c)=1}}
\beta_s e_c(a_hs+b_h\bar s).
\tag{SCN-1}
\]

平方根 well-factorable 分解后，`c=uv`，块为

\[
b=(u,v).
\tag{SCN-2}
\]

块内变量记为

\[
\theta=(h,\ell,x,z)\quad\text{或等价 completion/Kloosterman 展开变量}.
\tag{SCN-3}
\]

于是抽象地

\[
\mathcal W=\sum_b\sum_{\theta\in\Theta_b}F_{b,\theta}.
\tag{SCN-4}
\]

注意：`(SCN-1)` 没有出现块均值扣除项。

## 2. SOURCE-CEN 会要求的新对象

SOURCE-CEN 要求使用

\[
F_{b,\theta}^{\circ}
=
F_{b,\theta}
-
\mathbb E_bF
\tag{SCN-5}
\]

其中

\[
\mathbb E_bF
=
{1\over W_b}\sum_{\theta\in\Theta_b}w_{b,\theta}F_{b,\theta}
\tag{SCN-6}
\]

为同一块内的加权均值。此时源头中心化对象为

\[
\mathcal W^\circ
=
\sum_b\sum_{\theta\in\Theta_b}w_{b,\theta}F_{b,\theta}^{\circ}.
\tag{SCN-7}
\]

按定义，

\[
\sum_{\theta\in\Theta_b}w_{b,\theta}F_{b,\theta}^{\circ}=0
\quad\text{for each }b.
\tag{SCN-8}
\]

所以 `SOURCE-CEN` 不是普通估计，而是把原始对象 `(SCN-4)` 替换成另一个对象 `(SCN-7)`。

## 3. 反例：块常数函数

取某个 admissible 块 `b_0`，令

\[
F_{b_0,\theta}=1\quad(\theta\in\Theta_{b_0}),
\qquad
F_{b,\theta}=0\quad(b\ne b_0).
\tag{SCN-9}
\]

则原始 WFD 型对象为

\[
\mathcal W
=
\sum_{\theta\in\Theta_{b_0}}1
=
W_{b_0}\ne0.
\tag{SCN-10}
\]

但源头中心化对象为

\[
\mathcal W^\circ=0.
\tag{SCN-11}
\]

因此

\[
\mathcal W\ne \mathcal W^\circ.
\tag{SCN-12}
\]

这说明 `SOURCE-CEN` 不能作为当前 WFD-core 的恒等改写。

## 4. 对当前具体相位的解释

有人可能认为 `(SCN-9)` 太抽象；但当前 WFD-core 的系数类允许 divisor-bounded `\beta_s`、
well-factorable `\lambda_c` 与平滑 `\omega_h`，并没有规定每个 `(u,v)` 块内必须零均值。即使
Kloosterman 相位使很多块均值较小，这也需要证明；它不是定义恒等式。

更重要的是，`(KE-13)` 的目标是对未中心化和

\[
\sum_{h,s}\omega_h\beta_s e_{uv}(a_hs+b_h\bar s)
\tag{SCN-13}
\]

给出对数节省。若改成

\[
\sum_{h,s}\omega_h\beta_s
\left(
e_{uv}(a_hs+b_h\bar s)-\operatorname{Mean}_{u,v}
\right),
\tag{SCN-14}
\]

则还必须额外估计被减去的块均值项：

\[
\sum_b \operatorname{Mean}_b.
\tag{SCN-15}
\]

这正是块能量/块均值问题，不能免费消失。

## 5. SOURCE-CEN 与原命题的关系

若要使用 SOURCE-CEN，有且仅有两条合法路径：

1. **重新证明原始 dispersion 恒等式。** 从最初的误差定义开始，证明实际进入 KZ-E 的确实是
   `F^\circ` 而不是 `F`；
2. **补充块均值估计。** 证明
   \[
   \left|\sum_b\sum_{\theta\in\Theta_b}w_{b,\theta}\mathbb E_bF\right|
   \ll_A
   {\mathcal B(UV,S,H)\over\log^A y}.
   \tag{SCN-16}
   \]

第 2 条就是 `BLK-energy-core` 或块均值版本的同等强度问题。

当前文档没有第 1 条；第 2 条也没有证明。因此：

\[
\boxed{\text{SOURCE-CEN is false as an identity for current WFD-core.}}
\tag{SCN-17}
\]

## 6. 审稿结论

本步完成 `SOURCE-CEN` 的直接硬攻：

```text
SOURCE-CEN cannot close the current no-black-box chain.
```

当前内部无黑箱路线在本文件完成时唯一剩余可写为：

```text
BLK-energy-core:
prove block mean / block energy has arbitrary logarithmic saving,
or add a genuine non-concentration hypothesis and prove it from upstream structure.
```

后续 `prime-matrix-h3-dsb-hlc-blk-energy-core-obstruction.md` 已进一步说明：裸块能量估计不能作为
平方核层任意系数数组定理成立，因此真实内部目标应写成 `NC-BLK`，即证明实际 WFD 系数的
块非集中。

若不攻 `BLK-energy-core`，则只能明确转为：

```text
external DI/BFI theorem route.
```

这不是后退，而是把错误的“中心化恒等式”出口排除掉，使当前剩余硬点成为一个真实可审查的
块能量问题。
