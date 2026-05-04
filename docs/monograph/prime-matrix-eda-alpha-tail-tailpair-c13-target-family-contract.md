# AlphaTail `C13` 目标窗口族合同审计

**状态：** `explicit_selected_contract_closed_target_generation_open`

本文把 `C13` 高 `P` 主链的最后全局化缺口单独抽出：当前脚本能验证给定
`selected` 窗口清单上的合同闭合，但仓库中尚未形式化“完整高 `P` 目标窗口族如何由
`P` 生成 `B,r,m`”的规则。因此本层闭合的是显式样本合同，不是行命题全局闭合。

## 1. 合同对象

对每个高 `P` 窗口 `(p,B,r)`，令低大素块最小素数为 `L`，并取
`m in {4,5}`。目标族生成器必须至少给出以下可审查条件：

```text
TFC-A: B 是 dyadic block，且在当前候选样式中 B=2^ceil(log2(p+1)), p<B<2p；
TFC-B: 6 divides |r|；
TFC-C: B<2L 且 (m-1)|r|<L；
TFC-D: Gate 总池闭合，或 Formal+MidVoid 逐窗口闭合。
```

其中 `TFC-C` 接回 `lift>=2` 结构空性，`TFC-D` 接回 `HighP-PLT` 低筛闭合桥。
若完整目标族生成器只输出满足 `TFC-A/B/C/D` 的窗口，则 `C13` 高 `P` 链条可在该
目标族上闭合。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_target_family_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_target_family_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 3. 当前样本结果

高 `P` 样本只包含 `p=5003,10007`，输出为：

```text
highP_windows=2；
syntax=True；
structural=True；
total_gate=True；
local_formal=True；
row_formal=True；
explicit_contract=True；
target_rule_closed=False。
```

逐窗口：

```text
p=5003:
  B=8192=2^ceil(log2(p+1))；
  p<B<2p；
  6 divides |r|；
  min_block_margin=822；
  min_n_margin=4363；
  gate_pass=False；
  formal_pass=True。

p=10007:
  B=16384=2^ceil(log2(p+1))；
  p<B<2p；
  6 divides |r|；
  min_block_margin=1630；
  min_n_margin=5407；
  gate_pass=True；
  formal_pass=True。
```

因此当前显式高 `P` 压力样本满足：

```text
lift>=2 structural void；
Gate total pool closure；
Formal local closure。
```

## 4. 精确剩余

当前真正剩余不是样本内部预算，而是：

```text
TargetFamilyGenerator:
  给出完整高 P 目标窗口族 W(P)；
  证明 W(P) 不遗漏任何 C13 目标窗口；
  证明每个输出窗口满足 TFC-A/B/C/D；
  若有例外，则列入有限证书或 PDEC/SAE 出口。
```

在该生成器未形式化前，本文只能支持：

```text
当前 explicit-selected 样本合同闭合；
完整行命题全局闭合仍未完成。
```

