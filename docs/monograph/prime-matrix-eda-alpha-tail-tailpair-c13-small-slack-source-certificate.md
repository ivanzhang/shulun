# AlphaTail `C13` 小余量前向源槽有限证书

**状态：** `small_slack_source_certificate_sample_closed_global_open`

本文处理 `SourceSlotStructural` 留下的唯一小余量样本窗口：`p=5003`。
粗组合槽上界给出 `K*28=224`，超过该窗口允许删除量 `106.727367`，
所以必须证明实际可激活源槽远少于全部前向源槽。

## 1. 证书枚举

在前向源槽口径下，枚举全部

```text
u in {2,3}, 0<=j2<j1<j<m, ell in low-prime block
```

并用精确域端点约束

```text
q_lo <= ell+(j-j1)|r|/u <= q_hi
```

以及尾素条件

```text
ell+(j-j1)|r|/u in tail primes；
ell+(j-j2)|r|/u in tail primes
```

判定源槽是否激活。该枚举与原 `active_ap_classes()` 的 AP 活跃类定义逐项比对。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_small_slack_source_certificate.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_small_slack_source_certificate.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 3. 当前样本结果

总账：

```text
forward_trials=448；
forward_slots=56；
active_trials=50；
active_sources=28；
enumeration_matches_ap=True；
source_certificate_pass=True。
```

唯一小余量窗口：

```text
p=5003:
  forward_trials=224；
  forward_slots=28；
  active_trials=5；
  active_sources=5；
  inactive_sources=23；
  source_budget=13.340921；
  source_margin=8.340921；
  enumeration_matches_ap=True；
  source_certificate_pass=True。
```

对照大余量窗口：

```text
p=10007:
  forward_slots=28；
  active_sources=23；
  source_budget=159.904544；
  coarse_pay=True；
  source_certificate_pass=True。
```

## 4. 对闭合链的影响

当前样本的 `ActiveClassBound` 现已由三段闭合：

```text
APSingletonStructural:
  q<2ell => 每个 AP 类单点化。

SourceSlotStructural:
  活跃骨架均为前向源槽。

SmallSlackSourceCertificate:
  小余量窗口 p=5003 的实际源槽数为 5 <= Allow/K。
```

该证书仍是当前显式样本的有限闭合，不是完整目标族的全局证明。
完整全局化还需证明：所有小余量窗口可被有限列举完毕，或给出统一的源槽稀疏定理。
