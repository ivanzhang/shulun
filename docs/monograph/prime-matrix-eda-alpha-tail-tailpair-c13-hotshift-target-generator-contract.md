# AlphaTail `C13` 热门位移目标生成器合同

**状态：** `hotshift_target_generator_sample_closed_global_open`

本文把当前 `C13` 高 `P` selected 窗口的来源从手填清单推进为一个可审计生成规则：

```text
HotShiftGenerator:
  B = 2^ceil(log2(p+1))；
  D = (B,2B] 中 alpha p-光滑、squarefree、固定 Möbius 符号的集合；
  r = argmax_{s != 0} #{d in D : d+s in D}；
  输出窗口 (p,B,r)。
```

当前使用 `sign=-`、`alpha=0.9`。

## 1. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_target_generator_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_target_generator_contract.py \
  --p-list 997,5003,10007 --finite-p-cut 1000 --eta 0.04 --format table
```

## 2. 当前样本结果

高 `P` 生成结果：

```text
highp_selected=5003:8192:-36,10007:16384:-900；
matches_expected_highp=True；
full_postlow_chain=True；
small_slack=True；
sample_chain=True；
target_rule_closed=False。
```

逐点热门位移：

```text
p=5003:
  B=8192；
  r=-36；
  hot_count=641；
  energy/model=1.510286。

p=10007:
  B=16384；
  r=-900；
  hot_count=1278；
  energy/model=1.508103。
```

`p=997` 在默认 `finite-p-cut=1000` 下不进入高 `P` 生成器义务；它由低 `P`
有限证书系统处理。

## 3. 对目标生成器缺口的影响

该合同闭合的是“当前高 `P` 样本 selected 从何而来”：

```text
HotShiftGenerator(sample)
=> selected highP windows
=> C13 full_postlow_chain(sample)。
```

它尚未证明：

```text
任意行命题反例都必然落入 HotShiftGenerator 输出；
HotShiftGenerator 对所有 p>P_fin 都满足比例结构、SlackFloor、APSingleton 与 Allow<224 有限表覆盖；
热门位移并列时的 tie-break 规则不会遗漏目标窗口。
```

因此该项降低了 `TargetFamilyGenerator` 的黑箱程度，但不把行命题升级为全局证明。
