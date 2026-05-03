# BPN Rankin smooth-core 账本验收定理

**状态：** `rankin_ledger_acceptance_reduced_to_checkable_certificate`

本文把 `finite Rankin smooth-core ledger constants` 写成正式可验收的证明义务。
结论是：

```text
若每个颜色类都有通过的 Rankin 证书，
则 Colored disjoint-corridor core-sieve budget 闭合。
若证书不通过，则失败必须登记为常数缺口或 low-mod core CRTDefect。
```

## 1. 单颜色类证书

一个颜色类证书包含：

```text
P, K, intervals=[A_j,B_j], phase_moduli, allowed_budget, s-grid。
```

对应的不相交走廊并集为

\[
\mathcal C=\bigsqcup_j [A_j,B_j]\cap\mathbb Z.
\]

定义 smooth-core 指示

\[
\sigma_K(d)=1_{d|M_{<P}}1_{\mu(d)^2=1}1_{\omega(d)\le K}1_{\mathrm{phase}(d)}.
\]

证书计算两类量：

\[
N_K(\mathcal C)=\sum_{d\in\mathcal C}\sigma_K(d),
\]

以及对每个 `s>0` 的安全 Rankin 账本

\[
\mathcal R_s(\mathcal C;K)
=
\sum_j\sum_{d\in[A_j,B_j]}\sigma_K(d)\left({B_j\over d}\right)^s.
\tag{1}
\]

由于 `d<=B_j`，逐项有 `1<=(B_j/d)^s`，故

\[
N_K(\mathcal C)\le \mathcal R_s(\mathcal C;K).
\tag{2}
\]

## 2. 验收定理

**Theorem RLA-1（单颜色类验收）。**
若证书给出某个 `s` 满足

\[
\mathcal R_s(\mathcal C;K)\le B_{\rm allow},
\tag{3}
\]

则该颜色类满足

\[
N_K(\mathcal C)\le B_{\rm allow}.
\]

**证明。**
由 `(2)` 与 `(3)` 立即得到。证毕。

**Corollary RLA-2（多颜色类验收）。**
若颜色类 `c=1,\dots,m` 分别有预算 `B_c`，并且

\[
\mathcal R_{s_c}(\mathcal C_c;K)\le B_c
\qquad(1\le c\le m),
\]

则

\[
\sum_{c=1}^m N_K(\mathcal C_c)\le \sum_{c=1}^m B_c.
\]

因此只要 `\sum_c B_c` 不超过主链允许预算，着色走廊出口闭合。

## 3. 失败分类

若某颜色类证书不通过，即

\[
\min_s\mathcal R_s(\mathcal C;K)>B_{\rm allow},
\tag{4}
\]

则不能把该颜色类写成已闭合。只能进入二分：

```text
Rankin constants obstruction:
  调整 s-grid、细分走廊、重新分配预算；

low-mod core CRTDefect:
  residue spike table 出现超过阈值的相位尖峰。
```

后者已经由 `prime-matrix-bpn-lowmod-core-crtdefect-bridge.md` 并入 `PDEC-or-SAE`。

## 4. 与脚本的对应

脚本 `experiments/prime_matrix_bpn_rankin_ledger_certificate_audit.py` 输出：

- `core_count_exact`：精确 `N_K(\mathcal C)`；
- `rankin_best_grid.rankin_ledger`：网格内最小 `\mathcal R_s`；
- `allowed_budget`；
- `rankin_budget_pass`；
- `phase_reports`。

审稿验收规则：

```text
rankin_budget_pass == true
=> 该颜色类预算闭合；

rankin_budget_pass == false 且 phase spike 超阈值
=> 登记 low-mod core CRTDefect；

rankin_budget_pass == false 且无 phase spike
=> 常数账本未闭合，需细分或换参数。
```

## 5. 当前主链含义

本文已经把 `finite Rankin smooth-core ledger constants` 从非形式化常数任务变为
可验收证书任务。当前全局剩余不再是“定义 Rankin 账本”，而是：

```text
为正式反例诱导出的全部颜色类生成通过证书；
未通过者必须触发 low-mod core CRTDefect 或继续细分。
```

与 `PDEC-or-SAE` 排斥合并后，BPN-BK 的最终审稿义务变为：

```text
Rankin certificates for all colored corridors
+ PDEC/SAE exclusion for all low-mod exits。
```
