# Triad-A1 标准 Prime-Lift 删除势账本

**状态：** `standard_prime_lift_positive_deletion_potential_materialized`

连续 positive-limsup 的标准 prime-lift 分支已接入删除势账本。39 个当前标准行给出 D>=log(13)，选择性拆分的 13 个后继给出 D>=log(17)。剩余终端是 NoDeletion-KL/PDEC 或 diffuse CleanKLS/DLS 大筛。

## 1. 删除势律

标准 prime-lift 签名固定 promoted prime ell 的一个 fiber residue。把 ell 晋升进低模周期时，完整 ell-fiber 中至多 1/ell 落在该固定 residue。因此该签名支付删除势 D>=log(ell)。若无限层持续出现标准固定 residue，删除势发散；若固定 residue 不再持久，则回到 diffuse CleanKLS/DLS；若删除停止但分布偏斜，则进入 NoDeletion-KL/PDEC。

```text
fixed residue modulo ell
=> survival <= 1/ell after promoting ell
=> deletion potential D >= log(ell)。
```

## 2. 汇总

- `standard_row_count=39`。
- `commuted_successor_row_count=13`。
- `deletion_row_count=52`。
- `route_counts={'PositiveDeletionPotentialOrNoDeletionKL': 52}`。
- `promoted_prime_counts={13: 39, 17: 13}`。
- `global_min_deletion_potential_lower_bound=2.56495`。
- `global_max_survival_upper_bound=0.0769231`。

## 3. 删除势行

| P | signature | ell | source | survival upper | D lower | route |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| 17 | `13:1:7` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 17 | `13:2:8` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 17 | `13:5:6` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 17 | `13:4:12` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 17 | `13:10:3` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 19 | `13:11:10` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 19 | `13:1:9` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 19 | `13:4:11` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 19 | `13:8:8` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 19 | `13:10:9` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 23 | `13:0:1` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 23 | `13:12:9` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 23 | `13:8:12` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 23 | `13:4:11` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 23 | `13:10:11` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `13:0:2` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `13:12:1` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `13:0:4` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `13:12:12` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 31 | `13:2:4` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 31 | `13:7:2` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 31 | `13:5:3` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 31 | `13:10:1` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 31 | `13:12:4` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 37 | `13:7:2` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 37 | `13:5:9` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 37 | `13:8:8` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 37 | `13:4:3` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 37 | `13:3:10` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 43 | `13:5:1` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 43 | `13:7:3` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 43 | `13:0:1` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 43 | `13:12:3` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 43 | `13:2:2` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 47 | `13:4:4` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 47 | `13:8:4` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 47 | `13:0:5` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 47 | `13:12:3` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 47 | `13:12:12` | 13 | `standard_next_prime_signature` | 0.0769231 | 2.56495 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `17:15:6` | 17 | `selective_commutation_successor` | 0.0588235 | 2.83321 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `17:11:6` | 17 | `selective_commutation_successor` | 0.0588235 | 2.83321 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `17:7:6` | 17 | `selective_commutation_successor` | 0.0588235 | 2.83321 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `17:3:6` | 17 | `selective_commutation_successor` | 0.0588235 | 2.83321 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `17:16:6` | 17 | `selective_commutation_successor` | 0.0588235 | 2.83321 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `17:12:6` | 17 | `selective_commutation_successor` | 0.0588235 | 2.83321 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `17:8:6` | 17 | `selective_commutation_successor` | 0.0588235 | 2.83321 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `17:4:6` | 17 | `selective_commutation_successor` | 0.0588235 | 2.83321 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `17:0:6` | 17 | `selective_commutation_successor` | 0.0588235 | 2.83321 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `17:13:6` | 17 | `selective_commutation_successor` | 0.0588235 | 2.83321 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `17:9:6` | 17 | `selective_commutation_successor` | 0.0588235 | 2.83321 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `17:5:6` | 17 | `selective_commutation_successor` | 0.0588235 | 2.83321 | `PositiveDeletionPotentialOrNoDeletionKL` |
| 29 | `17:1:6` | 17 | `selective_commutation_successor` | 0.0588235 | 2.83321 | `PositiveDeletionPotentialOrNoDeletionKL` |

## 4. 当前硬点

标准 prime-lift positive-limsup 分支已不再是开放 PDEC-CAP 缺口。
它要么持续支付删除势，要么在删除停止时进入 NoDeletion-KL/PDEC 或 diffuse CleanKLS/DLS。
下一步只剩将 NoDeletion-KL 与 CleanKLS/DLS 的终端估计补齐。
