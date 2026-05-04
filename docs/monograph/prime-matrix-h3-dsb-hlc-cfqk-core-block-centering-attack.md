# CFQK-core：块中心化与半对角修正硬攻

**状态：** `cfqk_block_centering_route_blocked_without_new_input`

本文继续只攻击同一个剩余：

```text
CFQK-core: centered four-modulus Kloosterman-fraction correlation saving.
```

本步直接处理上一层 `(SQK-21)` 半对角。关键结论是：

```text
同一 (u,v) 块内的半对角不能被要求 log^{-A} 估小；
它必须作为块对角/局部方差被中心化扣除。
```

因此上一层 `CFQK-core` 中的半对角条款需要拆成：

1. `(u,v)=(u',v')` 的块对角中心化恒等式；
2. `u=u', v\ne v'` 或 `v=v', u\ne u'` 的一侧共享模数相关；
3. `u,u',v,v'` 全不同的真四模数非对角相关。

这不是换命题，而是修正平方核层的必要中心化。若不做这一步，任何完全自足证明都会在精确块
对角处被阻断。
后续 `prime-matrix-h3-dsb-hlc-bd-cen-dispersion-centering-audit.md` 已核查：当前 KZ-E spine 只
写明 `h=0` 主项抵消，尚未证明同 `(u,v)` 块局部方差扣除。因此 `BD-CEN` 是当前第一阻断点。
再后续 `prime-matrix-h3-dsb-hlc-bd-cen-no-go-route-fork.md` 证明：对当前未块中心化对象，
`BD-CEN` 被单块非零反例阻断。

## 1. 按模数块重写平方核

沿用 `(SQK-1)`--`(SQK-6)`。令

\[
b=(u,v),\qquad \Xi_b=\{\xi\in\Xi_{\rm nd}: (u_\xi,v_\xi)=b\}.
\tag{BCF-1}
\]

定义块和

\[
\mathcal S_b
=
\sum_{\xi\in\Xi_b}A_\xi e(\Phi(\xi)).
\tag{BCF-2}
\]

于是

\[
\mathcal S_{\rm nd}
=
\sum_b\mathcal S_b,
\tag{BCF-3}
\]

并且平方恒等式为

\[
|\mathcal S_{\rm nd}|^2
=
\sum_b|\mathcal S_b|^2
+
\sum_{b\ne b'}\mathcal S_b\overline{\mathcal S_{b'}}.
\tag{BCF-4}
\]

第一项正是上一层 `(SQK-18)` 所含的全部同块半对角，包含精确对角 `(SQK-12)` 与同
`(u,v)`、不同 `(h,\ell,x,z)` 的所有交叉。

## 2. 同块半对角不能估小

若要求

\[
\sum_b|\mathcal S_b|^2
\ll_A
{\mathcal B(UV,S,H)^2\over\log^{2A}y}
\tag{BCF-5}
\]

对任意 admissible 系数成立，则立即与单原子测试矛盾：取某个固定
`\xi_0` 的 `A_{\xi_0}\ne0`，其他权重为零，则

\[
\sum_b|\mathcal S_b|^2=|A_{\xi_0}|^2,
\tag{BCF-6}
\]

而右侧在任意大 `A` 下要求同一个局部二范数再多出 `log^{-2A}`。这不可能由相位振荡产生，
因为该层没有跨块相位。

因此 `(SQK-21)` 若把 `(u,v)=(u',v')` 的整块半对角也列为需要 `log^{-A}` 的误差，就是过强
陈述。正确做法是把整块对角作为局部方差/主对角在 dispersion 中心化时扣除。

## 3. 块中心化核

定义块对角投影

\[
\Pi_{\rm blk}(\xi,\xi')=1_{(u_\xi,v_\xi)=(u_{\xi'},v_{\xi'})}.
\tag{BCF-7}
\]

块中心化平方核为

\[
K^{\flat}(\xi,\xi')
=
A_\xi\overline{A_{\xi'}}e(\Phi(\xi)-\Phi(\xi'))
-
\Pi_{\rm blk}(\xi,\xi')A_\xi\overline{A_{\xi'}}e(\Phi(\xi)-\Phi(\xi')).
\tag{BCF-8}
\]

等价地，

\[
\sum_{\xi,\xi'}K^{\flat}(\xi,\xi')
=
\sum_{b\ne b'}\mathcal S_b\overline{\mathcal S_{b'}}.
\tag{BCF-9}
\]

这一步把不可估小的块对角从待估核中移除。它必须与 KZ-E 的 dispersion 方差恒等式对齐：
如果方差恒等式已经扣除了局部块方差，则 `(BCF-8)` 是正确核；如果没有扣除，则当前链条仍缺
一个 `BD-CEN` 中心化恒等式。

## 4. 一侧共享模数层

块中心化后仍有真正的半对角：

\[
u=u',\quad v\ne v',
\tag{BCF-10}
\]

以及对偶层

\[
v=v',\quad u\ne u'.
\tag{BCF-11}
\]

以 `(BCF-10)` 为例，相位差为

\[
\Delta_u
=
{\bar vR\over u}
-
{\overline{v'}R'\over u}
+
{\bar uT\over v}
-
{\bar uT'\over v'}.
\tag{BCF-12}
\]

该层仍有三模数结构 `(u,v,v')`，并保留共同模 `u` 上的差相位

\[
{\bar vR-\overline{v'}R'\over u}.
\tag{BCF-13}
\]

因此它不能被同块中心化自动消除；但它已经比真四模数层窄。当前最合理的下一原子是：

**OSQK-core（one-shared-modulus quadratic Kloosterman-fraction core）。**

\[
\left|
\sum_{\substack{\xi,\xi':\,u=u',\,v\ne v'}}
K^{\flat}(\xi,\xi')
\right|
+
\left|
\sum_{\substack{\xi,\xi':\,v=v',\,u\ne u'}}
K^{\flat}(\xi,\xi')
\right|
\ll_A
{\mathcal B(UV,S,H)^2\over\log^{2A}y}.
\tag{BCF-14}
\]

这是半对角剩余的正确形式。

## 5. 真四模数层

剩余真非对角层为

\[
u\ne u',\qquad v\ne v',\qquad (u,v)\ne(u',v').
\tag{BCF-15}
\]

对应核心为：

**TFQK-core（true four-modulus Kloosterman-fraction core）。**

\[
\left|
\sum_{\substack{\xi,\xi':\,u\ne u',\,v\ne v'}}
K^{\flat}(\xi,\xi')
\right|
\ll_A
{\mathcal B(UV,S,H)^2\over\log^{2A}y}.
\tag{BCF-16}
\]

该层才是四个模数全部运动的真正非对角平均。

## 6. 修正后的中心化核心：BCFQK-core

**BCFQK-core（block-centered four-modulus Kloosterman-fraction core）。** 该核心由三项组成：

1. **BD-CEN。** KZ-E/dispersion 方差恒等式在平方核层扣除块对角
   `\sum_b|\mathcal S_b|^2`，使目标核为 `(BCF-8)`；
2. **OSQK-core。** 一侧共享模数层满足 `(BCF-14)`；
3. **TFQK-core。** 真四模数层满足 `(BCF-16)`。

## 7. `BCFQK-core => KFLS-core`

**命题。** 若 BCFQK-core 成立，则 KFLS-core 成立。

**证明。**

1. 用 `(BCF-4)` 把平方核分成块对角和跨块项。
2. BD-CEN 将块对角作为局部方差/主对角扣除或转入自然二范数账本，不再要求它产生
   `log^{-A}`。
3. 跨块项按 `(BCF-10)`、`(BCF-11)`、`(BCF-15)` 分成一侧共享模数层与真四模数层。
4. 调用 OSQK-core 与 TFQK-core 得到
   \[
   \left|\sum_{\xi,\xi'}K^{\flat}(\xi,\xi')\right|
   \ll_A
   {\mathcal B(UV,S,H)^2\over\log^{2A}y}.
   \tag{BCF-17}
   \]
5. 回到已中心化的 dispersion 平方核，取平方根，得到 KFLS-core。

证毕。

## 8. 当前审稿边界

本步完成了：

```text
BCFQK-core => KFLS-core => BSC-core => BWFD-core => WFD-core => KZ-E.
```

并且严格指出上一层把整个 `(u,v)=(u',v')` 半对角要求 `log^{-A}` 是过强的；正确剩余更新为：

```text
SOURCE-CEN or BLK-energy-core or external DI/BFI.
```

其中 `SOURCE-CEN` 要证明原始对象已块条件中心化；`BLK-energy-core` 要证明块能量本身也有
对数节省；外部 DI/BFI 是引用版出口。没有三者之一，不能继续把 `OSQK/TFQK` 接回 `KFLS`。
