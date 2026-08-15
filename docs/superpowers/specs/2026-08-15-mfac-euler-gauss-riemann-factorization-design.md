# MFAC Euler–Gauss–Riemann 三层因子化审计设计

## 目标

新增独立审计器，精确登记并在有限范围核验以下三层分解：

\[
\Lambda=\mathcal D(-\mu\log),\qquad
\sum_{n\le X}|\mathcal Da(n)|^2=
\sum_{d,e\le X}a_d\overline{a_e}\left\lfloor\frac X{[d,e]}\right\rfloor,
\]

以及对 \(\Re s>1\) 的 Mellin 恒等式

\[
\int_1^\infty(\psi(x)-x)x^{-s-1}dx
=\frac1s\left(-\frac{\zeta'}{\zeta}(s)-\frac{s}{s-1}\right).
\]

模块将离散化校正精确写成

\[
\psi(x)-x=
\mathcal S\!\left(\mathcal D(-\mu\log)-1\right)(x)+\lfloor x\rfloor-x.
\]

## 可验证范围

- 对有限 `limit`，直接检验 `divisor_transform(-mu_log)` 与 `von_mangoldt` 的逐点一致；
- 对同一系数，检验直接平方和与 LCM Gram 二次型一致；
- 对整数与半整数采样点，检验离散前缀和加 `floor(x)-x` 的校正恒等式；
- 验证 Mellin 公式仅登记在 `real_part > 1`，并明确把 `sigma > 1/2` 的加权尺度可和性列为开放门。

## 合同边界

审计器必须拒绝 RH、零点、零自由区域、显式公式、已得到 Mellin 收缩和有限数值剖面
作为证明来源，且拒绝以输入字段声称 `w3_closed` 或 `rh_proved`。

输出固定保留：

```text
euler_gauss_riemann_factorization_status=finite_exact_identity_registered
cross_scale_prefix_coercivity_status=unproved
actual_mellin_half_plane_contraction_status=unproved
rh_proved=false
```

## 非目标

不证明对任意 \(\sigma>1/2\) 的加权 \(L^2\) 可和性；不证明 W3、零自由区域或 RH。Mellin
公式在 \(\Re s>1\) 的精确表示不自动给出向左延拓或任何谱收缩。

## 产物

- `experiments/prime_matrix_mfac_euler_gauss_riemann_factorization_audit.py`
- `experiments/prime_matrix_mfac_euler_gauss_riemann_factorization_audit_test.py`
- `docs/monograph/prime-matrix-mfac-euler-gauss-riemann-factorization-audit.json`
- `docs/monograph/prime-matrix-mfac-euler-gauss-riemann-factorization-audit.md`

使用示例：

```bash
python3 experiments/prime_matrix_mfac_euler_gauss_riemann_factorization_audit.py \
  --limit 96
```
