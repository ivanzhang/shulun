# MFAC W1→W2 初等绝对值包络障碍审计证书

finite_inequality_status=verified_finite
finite_growth_status=finite_growth_witnessed
nonuniformity_obligation_status=open
w1_to_w2_status=unproved
rh_proved=false

## 边界

本证书只核验有限 Möbius 尾和、三角不等式包络与有限 dyadic 读数。
有限增长见证不证明 D→∞ 发散，也不证明不存在统一 L² 上界。
本模块不证明 W1→W2、Chebyshev 能量桥或 RH。

## 使用示例

```bash
python3 experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit.py \
  --limit 512 --dyadic-levels 5
```
