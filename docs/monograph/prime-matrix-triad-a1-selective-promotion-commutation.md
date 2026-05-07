# Triad-A1 选择性晋升交换律

**状态：** `selective_promotion_commutation_resolved_by_finite_split`

唯一选择性晋升缺口已由 CRT 交换律和有限拆分吸收：它不再是独立终端。后继要么回到标准 prime-lift promotion deletion/KL，要么进入 diffuse KLS。

## 1. 交换律

若 signature (ell,y,c) 跳过较小尾素数 r，则先晋升 r。对 r 的每个 residue s，原 ell-fiber residue 在 Qr 层变为 y'=(y-s)r^{-1} mod ell。于是选择性签名被有限拆成 r 个标准后继签名。若原签名有正 limsup 质量，则有限鸽巢给出某个后继签名正 limsup；若所有后继都不持久，则该质量进入 diffuse CleanKLS/DLS。

```text
original signature: (ell,y,c) at Q；
first promote r<ell；
new phase: t'=t+Qs；
need t'+Qr*y' == t+Qy mod ell；
therefore y'=(y-s)r^{-1} mod ell。
```

因此跳过较小素数的选择性晋升不会生成第四出口；它只是有限拆分。

## 2. 汇总

- `selective_row_count=1`。
- `route_counts={'FiniteSplitThenStandardPromotionOrDiffuseKLS': 1}`。
- `all_crt_orders_commute=True`。
- `max_successor_count=13`。

## 3. 明细

| P | signature | first r | ell | successors | route |
| ---: | --- | ---: | ---: | ---: | --- |
| 29 | `17:8:6` | 13 | 17 | 13 | `FiniteSplitThenStandardPromotionOrDiffuseKLS` |

## 4. 后继签名

### P=29 signature=17:8:6

- final_q_direct=`510510`。
- final_q_ordered=`510510`。
- successors=`[{'first_prime_residue': 0, 'successor_signature': '17:15:6'}, {'first_prime_residue': 1, 'successor_signature': '17:11:6'}, {'first_prime_residue': 2, 'successor_signature': '17:7:6'}, {'first_prime_residue': 3, 'successor_signature': '17:3:6'}, {'first_prime_residue': 4, 'successor_signature': '17:16:6'}, {'first_prime_residue': 5, 'successor_signature': '17:12:6'}, {'first_prime_residue': 6, 'successor_signature': '17:8:6'}, {'first_prime_residue': 7, 'successor_signature': '17:4:6'}, {'first_prime_residue': 8, 'successor_signature': '17:0:6'}, {'first_prime_residue': 9, 'successor_signature': '17:13:6'}, {'first_prime_residue': 10, 'successor_signature': '17:9:6'}, {'first_prime_residue': 11, 'successor_signature': '17:5:6'}, {'first_prime_residue': 12, 'successor_signature': '17:1:6'}]`。

## 5. 当前硬点

选择性晋升已不再是独立缺口。剩余是标准晋升后的删除势/NoDeletion-KL 证书，
以及 diffuse 分支的 CleanKLS/DLS 大筛估计。
