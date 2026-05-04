# BD-CEN：dispersion 块中心化身份核查

**状态：** `bd_cen_refuted_for_current_unblocked_wfd_object`

本文继续只攻击同一个最窄剩余：

```text
BD-CEN: KZ-E/dispersion 方差恒等式是否已经扣除同 (u,v) 块局部方差。
```

结论必须诚实：

```text
当前 KZ-E 文档只证明 h=0 主项抵消；
尚未证明同 (u,v) 块对角的中心化扣除。
```

因此 `BD-CEN` 不能标记为已闭合。若后续要继续沿平方核路线证明 `KFLS/BSC/WFD/KZ-E`，必须
补一个新的精确恒等式，说明实际 dispersion 变量已经是块中心化变量；否则同块对角不能从
平方核中删去。

## 1. BD-CEN 需要证明的身份

沿用

\[
\mathcal S_{\rm nd}=\sum_b\mathcal S_b,\qquad b=(u,v),
\tag{BDC-1}
\]

其中

\[
\mathcal S_b=\sum_{\xi\in\Xi_b}A_\xi e(\Phi(\xi)).
\tag{BDC-2}
\]

平方恒等式为

\[
|\mathcal S_{\rm nd}|^2
=
\sum_b|\mathcal S_b|^2
+
\sum_{b\ne b'}\mathcal S_b\overline{\mathcal S_{b'}}.
\tag{BDC-3}
\]

`BD-CEN` 要求 KZ-E 的真实 dispersion 方差不是 `(BDC-3)` 的全平方，而是已经扣除了

\[
\sum_b|\mathcal S_b|^2.
\tag{BDC-4}
\]

等价地，必须有一个文内恒等式：

\[
\mathcal E_{\rm disp}^{\rm centered}
=
|\mathcal S_{\rm nd}|^2
-
\sum_b|\mathcal S_b|^2
=
\sum_{b\ne b'}\mathcal S_b\overline{\mathcal S_{b'}}.
\tag{BDC-5}
\]

这就是需要逐行证明的最窄目标。

## 2. 当前 KZ-E 已经证明的内容

`prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md` 第 3 节给出的方差项是

\[
\mathcal E
=
\sum_{r_1,r_2}
\lambda_{r_1}\overline{\lambda_{r_2}}
\sum_{s_1,s_2}
\beta_{s_1}\overline{\beta_{s_2}}
\sum_{0<|h|\le H}
\omega_h\,\mathcal C(h;s_1,s_2;r_1,r_2).
\tag{BDC-6}
\]

并明确说明：

```text
h=0 主项已与主项抵消；h≠0 是唯一需要谱平均抵消的部分。
```

也就是说，当前 KZ-E 已闭合的是 Fourier 频率方向的中心化：

\[
\Pi_{h=0}\ \text{被扣除}.
\tag{BDC-7}
\]

但 `BD-CEN` 需要的是块索引方向的中心化：

\[
\Pi_{\rm blk}:\ (u,v)=(u',v').
\tag{BDC-8}
\]

`(BDC-7)` 与 `(BDC-8)` 是不同投影。`h\ne0` 不能推出 `(u,v)\ne(u',v')`；同一个 `(u,v)` 块内
仍有大量非零频率、不同 completion 变量和不同局部单位变量的交叉项。

## 3. `h=0` 抵消不等于块中心化

**引理。** 从 `(BDC-6)` 和 `h\ne0` 不能推出 `(BDC-5)`。

**证明。**

`(BDC-6)` 的求和仍允许两个平方核变量具有同一模数块：

\[
(u,v)=(u',v'),\qquad h,h'\ne0.
\tag{BDC-9}
\]

这些项属于 `(BDC-4)` 的块对角部分，但它们没有 `h=0`。因此频率主项剥离只删除
`\Pi_{h=0}`，没有删除 `\Pi_{\rm blk}`。

代数上，两个投影作用在不同坐标上：

\[
\Pi_{h=0}\Pi_{\rm blk}\ne \Pi_{\rm blk},\qquad
1-\Pi_{h=0}\ne 1-\Pi_{\rm blk}.
\tag{BDC-10}
\]

所以当前 KZ-E 的文字不能推出块中心化身份 `(BDC-5)`。证毕。

## 4. 为什么不能事后补删块对角

若没有 `(BDC-5)`，从全平方 `(BDC-3)` 改成跨块平方

\[
\sum_{b\ne b'}\mathcal S_b\overline{\mathcal S_{b'}}
\tag{BDC-11}
\]

不是估计，而是改变对象。块对角

\[
\sum_b|\mathcal S_b|^2
\tag{BDC-12}
\]

是非负量；它不能由相位符号在同一平方层中抵消。上一层已经证明它不能被要求对任意 admissible
系数具有任意 `log^{-A}` 节省。因此，除非原始 dispersion 恒等式本身给出 `(BDC-5)`，否则
`BCFQK-core=>KFLS-core` 的证明不能成立。

## 5. 修正后的当前义务

当前最窄义务不是 `OSQK-core`，而是先完成：

```text
BD-CEN:
prove (BDC-5) from the original dispersion identity before square-root factorization.
```

若 `BD-CEN` 成立，则后续解析硬点仍为：

```text
OSQK-core + TFQK-core.
```

若 `BD-CEN` 不成立，则平方核路线必须改写为更强但不同的目标：

```text
BLK-energy-core + OSQK-core + TFQK-core,
```

其中 `BLK-energy-core` 要直接证明 `sum_b |S_b|^2` 本身也有足够对数节省。该目标强于
`BD-CEN` 路线，且当前没有证明。

## 6. 审稿结论

本步完成了 `BD-CEN` 的严格核查：

```text
BD-CEN is not proved by the current KZ-E spine.
```

后续 `prime-matrix-h3-dsb-hlc-bd-cen-no-go-route-fork.md` 进一步证明：在当前未块中心化的
WFD/KZ-E 对象和当前 admissible 系数范围下，`BD-CEN` 不只是未证明，而是被单块非零反例
阻断。

因此该阶段完全自足链的第一阻断点更新为：

```text
SOURCE-CEN or BLK-energy-core or external DI/BFI.
```

不能在没有新输入的情况下继续声称 `BCFQK-core=>KFLS-core` 已闭合。下一步若继续硬攻，必须
三选一：证明原始对象已经是块条件中心化的 `SOURCE-CEN`；新增并证明非集中条件以支持
`BLK-energy-core`；或明确切换到外部 DI/BFI 定理。

后续核查进一步收紧：`SOURCE-CEN` 在当前对象下不是恒等式，裸 `BLK-energy-core` 不能作为
平方核层任意系数数组定理成立。当前内部无黑箱路线的真实剩余应写为 `NC-BLK`，即从实际 WFD
系数证明块非集中；否则该分支只能作为外部 DI/BFI 定理版闭合。
