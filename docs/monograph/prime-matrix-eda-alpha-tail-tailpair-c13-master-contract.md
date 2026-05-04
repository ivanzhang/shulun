# AlphaTail `C13` 高 P 主合同审计

**状态：** `c13_master_contract_sample_closed_global_open`

本文把 `C13` 高 P 链条中已经建立的接口合并为一个主合同，便于后续全局化审查。

## 1. 主合同

当前高 P 闭合可走两条路线：

```text
TotalGateContract:
  lift>=2 结构空性成立；
  HighP-PLT 的 Gate 总池闭合。

LocalFormalContract:
  lift>=2 结构空性成立；
  每个窗口的 Formal+MidVoid 口径闭合。
```

两条路线任一成立，都给出当前目标族上的 `HighP-PLT` 低筛闭合。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_master_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_master_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 3. 当前样本结果

```text
structural=True；
candidates=1368；
good_mod6=0；
min_block_margin=822；
min_n_margin=4363；
gate_plt=True；
formal_plt=True；
total_gate_contract=True；
local_formal_contract=True；
row_formal_contract=True；
gate_margin=505.963717；
formal_margin=2010.963717。
```

逐窗口：

```text
p=5003:
  gate_pass=False；
  formal_pass=True；
  formal_margin=411.727367。

p=10007:
  gate_pass=True；
  formal_pass=True；
  gate_margin=991.236350；
  formal_margin=1599.236350。
```

## 4. 结论边界

当前压力样本的高 P 链条已经形成闭合合同：

```text
lift>=2:
  由结构判据排除。

lift=1:
  Gate 总池可付款；
  或 Formal+MidVoid 逐窗口付款。

HighP-PLT:
  Gate 总池与 Formal 口径均可接回。
```

但这仍是“当前目标样本”的闭合，不是完整行命题全局闭合。全局化仍需证明完整目标窗口族满足同一合同：

```text
1. lift>=2 结构判据:
   B<2L, (m-1)|r|<L, 6||r|。

2. TotalGateContract:
   sum_F K(G_edge+G_mid)+D_ge2 <= sum_F slack。

3. 或 LocalFormalContract:
   每个窗口 U_edge+N_mid+D_ge2 <= slack。
```

## 5. 下一硬点

最小剩余不再是当前样本内部的计算，而是目标族生成规则：

```text
TargetFamilyRule:
  明确完整高 P 目标窗口族如何由 P 生成 B、r、m。
```

一旦目标族规则固定，就可以逐项证明上述三条合同；若某些窗口不满足，则进入有限证书或
PDEC/SAE 出口。

新增 `prime-matrix-eda-alpha-tail-tailpair-c13-target-family-contract.md` 与脚本
`experiments/prime_matrix_alpha_tail_tailpair_c13_target_family_contract.py` 后，该缺口已被
单独物化为 `TFC-A/B/C/D`：

```text
TFC-A: B 是当前候选 dyadic block，且样本中 B=2^ceil(log2(p+1)), p<B<2p；
TFC-B: 6 divides |r|；
TFC-C: B<2L 且 (m-1)|r|<L；
TFC-D: Gate 总池闭合，或 Formal+MidVoid 逐窗口闭合。
```

当前结果是 `explicit_selected_contract=True`，但 `target_family_rule_closed=False`。因此
该更新压实了最后接口，没有把样本闭合升级为全局闭合。
