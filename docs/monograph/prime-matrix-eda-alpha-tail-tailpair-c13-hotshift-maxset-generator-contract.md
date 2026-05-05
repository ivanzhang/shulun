# AlphaTail `C13` 全最大热门集生成器合同

**状态：** `hotshift_maxset_sample_closed_global_open`

为彻底移除“多个绝对热门差值并列时 tie-break 可能遗漏”的接口，本文把目标生成规则升级为：

```text
对每个 p，输出所有达到最大 C_D(r) 的绝对差值 |r|；
每个绝对差值只取负向代表 -|r|；
正向代表由 HotShiftMirror 归一化。
```

这样若未来出现多个不同绝对热门差值并列，生成器不是任意选择一个，而是全部输出。

## 1. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_maxset_generator_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_maxset_generator_contract.py \
  --p-list 997,5003,10007 --finite-p-cut 1000 --eta 0.04 --format table
```

## 2. 当前样本结果

```text
highp_selected=5003:8192:-36,10007:16384:-900；
token_count=2；
have_maxset=True；
abs_unique=True；
full_postlow=True；
small_slack=True；
sample_chain=True；
target_rule_closed=False。
```

逐点最大绝对热门差值：

```text
p=997:   max_abs_diffs={36}；
p=5003:  max_abs_diffs={36}；
p=10007: max_abs_diffs={900}。
```

## 3. 对生成器缺口的影响

该合同消除了“多个绝对热门差值并列时只选一个”的遗漏风险：

```text
HotShiftMaxSet:
  并列绝对热门差值全部输出。
```

剩余不再是 tie-break，而是两个更实质的全局义务：

```text
HMG-G1: 证明行命题反例必须触发 HotShiftMaxSet 中某个窗口；
HMG-G2: 证明 HotShiftMaxSet 输出的所有高 P 窗口满足 C13 局部链，
        或给 PDEC/SAE/有限出口。
```
