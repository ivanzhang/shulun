# MFAC Euler–Gauss–Riemann 三层因子化审计

## 有限核验

- `limit`：`96`
- Euler 反演失配数：`0`
- Gauss LCM Gram 残差：`0.0`
- 离散—连续校正残差：`7.105427357601002e-15`

```text
Lambda=D(-mu*log)
psi(x)-x=S(D(-mu*log)-1)(x)+floor(x)-x
Mellin domain: Re(s)>1
```

## 状态边界

```text
euler_gauss_riemann_factorization_status=finite_exact_identity_registered
cross_scale_prefix_coercivity_status=unproved
actual_mellin_half_plane_contraction_status=unproved
rh_proved=false
```

有限 LCM Gram 正定性控制的是 divisor transform 的局部二次能量；Mellin 公式在
`Re(s)>1` 只给出精确表示。把它推进到 `Re(s)>1/2` 所需的跨 dyadic 尺度前缀和
强制性仍未证明，本证书不证明零自由区域或 RH。

## 使用示例

```bash
python3 experiments/prime_matrix_mfac_euler_gauss_riemann_factorization_audit.py \
  --limit 96
```
