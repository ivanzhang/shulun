# H4-PDEC 同口径拆分引理

**状态：** `homogeneous_splitting_obligation_closed`

本文处理 `h4-pdec-bad-window-classification-lemma.md` 中 `C0/C4` 的“口径混合”义务。
结论是：口径混合不是新的数学出口；它是证书工程错误或预处理义务。任何混合坏窗族必须
先按同一 `(Q,\tau,F,\kappa,p)` 口径拆成子族，再分别进入 `PDEC/SAE/LHB/Routed` 分类。

## 1. 口径类型

一个 PDEC 口径类型记为

\[
\theta=(Q_\theta,\tau_\theta,F_\theta,\kappa_\theta,p_\theta,\mathcal W_\theta),
\]

其中 `\mathcal W_\theta` 记录窗口形状、列范围、低骨架定义和归一化约定。该类型给出：

```text
X_theta      : 该口径下的窗口索引域；
S_theta      : 触发该口径低模缺陷的坏窗集合；
g_theta(t)   : #{x in S_theta: tau_theta(x)=t}；
L_PDEC(theta): 该口径对应的 Fourier 下界；
A_theta,b_theta,E_theta,e_theta: 该口径允许的约束行。
```

不同 `theta` 的 `Q`、`\tau`、`F` 或窗口形状只要有一项不同，就不能共享同一个
`g(t)` 或同一套 `A,b,E,e`。

## 2. 拆分规则

设混合集合 `S` 带有类型映射

\[
\Theta:S\to\mathcal T.
\]

定义

\[
S_\theta=\{x\in S:\Theta(x)=\theta\}.
\]

则

\[
S=\bigsqcup_{\theta\in\mathcal T}S_\theta.
\]

空子族丢弃；非空子族分别提交独立证书。

## 3. 拆分定理

**Theorem H4-PDEC-HS（同口径拆分）。**
任何试图把不同口径类型的坏窗集合合并为一个 `PDEC-Dual-Cert` 的证书都是非法证书。
合法替代是按 `S=\bigsqcup S_\theta` 拆分，并对每个非空 `S_\theta` 单独应用
`UPS-1` 与 `H4-PDEC-BWC`。拆分不丢失任何坏窗，也不会制造新的坏窗。

**证明。**
`PDEC-Cert` 的输入要求固定同一个 `Q`、同一个相位映射 `\tau`、同一个测试函数 `F`
和同一个计数向量 `g(t)`。若两个坏窗的 `theta` 不同，则至少有一项输入不一致；把它们
写入同一 `g` 会使 `F(\tau(x))`、Fourier 归一化或约束矩阵的含义发生变化，违反
`h4-pdec-certificate-template.md` 的同一坏窗集合要求。按类型拆分后，每个子族都有自己的
`Q_\theta,\tau_\theta,F_\theta,g_\theta`，满足模板输入。集合分解是按类型映射取纤维，
故互不相交且并为原集合；因此既不丢失也不新增坏窗。证毕。

## 4. 与 `SAE/PDEC` 二分的关系

拆分后，对每个非空 `S_\theta` 独立应用 `UPS-1`：

```text
若 |S_theta| >= beta_theta |X_theta|：
  进入该口径的 persistent/PDEC 分支；

若 0 < |S_theta| < beta_theta |X_theta|：
  进入该口径的 SAE 分支。
```

因此“全局混合 S 很大”不能直接推出单一 PDEC 证书；必须先找到一个同口径 persistent
子族，或把所有非空子族列为 SAE 子义务。若需要由全局密度推出某个同口径 persistent
子族，必须额外提供阈值账本

\[
\sum_{\theta\in\mathcal T}\beta_\theta |X_\theta|<|S|.
\]

没有这张账本时，只能保留逐口径二分结果。

## 5. 更新 `C0/C4`

`h4-pdec-bad-window-classification-lemma.md` 中的失败条件现在解释为：

| 条件 | 原含义 | 闭合处理 |
|---|---|---|
| `C0` | 低模测试函数或 `tau` 不同一 | 强制按 `theta` 拆分；不可作为单个证书 |
| `C4` | `S` 混合多个 `(p,Q,tau)` 口径 | 强制按 `theta` 拆分；拆分后重跑分类 |

因此 `口径混合` 不再是待排斥出口。拆分后仍可能产生：

```text
SAE；
LHB-PDEC；
ColumnCRT/ColumnRadius/TailAnchor/Rankin routed branches。
```

这些才是剩余数学出口。

## 6. 当前结论

已经闭合：

```text
C0/C4 口径混合处理；
混合集合到同口径子证书的无损拆分；
拆分后逐子族应用 UPS-1 与坏窗分类。
```

仍未闭合：

```text
拆分后 SAE 出口排斥；
拆分后 ColumnCRT/ColumnRadius/TailAnchor/Rankin 出口排斥或证书化；
若要从全局混合密度推出同口径 persistent 子族，还需阈值账本。
```

因此下一步最小硬点更新为：

\[
\boxed{\text{排除或证书化拆分后的非 LHB 型数学出口。}}
\]
