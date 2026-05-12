# Prime Matrix strict prefix 残洞转移路由器

**状态：** `prefix_residual_transfer_closed_as_weighted_injection_capacity_multiplier_open`

`PrefixResidualToBoundaryFormalUnitObligationTransfer` 可在加权义务层闭合：任意 prefix 残洞 c 在早期零行假设下都有最小覆盖标签 tau_z(c) in (z,P)，并可带着 label_band 与 capacity_multiplier_id 注入 formal-unit obligation 域。这没有完成类型压缩，因为 completed-internal 标签可能高复用，quotient/reuse 也可能塌缩实例数。所以下一真正窄点是容量乘子纪律；并行保留 prefix anti-collapse。

```text
prefix_residual_selector_closed=true
label_band_dichotomy_closed=true
prefix_residual_to_weighted_formal_unit_obligation_transfer_proved=true
prefix_transfer_effective_for_type_compression_proved=false
registered_prefix_capacity_multiplier_discipline_proved=false
prefix_weighted_obligation_to_effective_type_instance_anticollapse_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 转移公式

若假设第 x 行是早期零行，且 `z<x<P`，定义

```text
R_{x,z}={1<=c<P: for every prime q<=z, q does not divide xP+c}.
```

则对每个 `c in R_{x,z}`，早期零行强制存在素数 `q in (z,P)` 整除 `xP+c`。取最小这样的 q，记为 `tau_z(c)`，得到 canonical prefix atom。

## 2. schema

| field | meaning |
| --- | --- |
| `prefix_cutoff_z` | 记录本次上游残洞势使用的 cutoff；避免把不同 z 的义务混计。 |
| `prefix_residual_column_c` | 记录 c in R_{x,z}，即 no q<=z divides xP+c。 |
| `canonical_prefix_label_tau_z` | 取最小 q in (z,P) with q divides xP+c；早期零行保证其存在。 |
| `label_band` | 区分 completed-internal band z<q<=x 与 incomplete-external band x<q<P。 |
| `capacity_multiplier_id` | 登记 q 在当前 row/prefix 中的复用容量；该字段只登记，不在本步给上界。 |
| `formal_unit_payload_hash` | 把 prefix atom 并入原 O(w) payload，保留 return/quotient/no-loss 账本。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PrefixTransferInputActive` | `true` | `false` | 上一层把自然残洞质量改写后的直接攻击点定为 prefix 残洞转移。 | PrefixResidualToBoundaryFormalUnitObligationTransfer |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍只在任意假设早期零行 witness 下构造义务，不用真实缺席数据。 | 保持 row_column_unconditional_closed=false。 |
| `PrefixResidualSelectorClosed` | `true` | `true` | 若 c in R_{x,z} 且该行为早期零行，则存在 q in (z,P) divides xP+c；取最小 q 得 canonical tau_z(c)。 | PrefixCanonicalLabelSelectorClosed |
| `LabelBandDichotomyClosed` | `true` | `true` | canonical tau_z(c) 唯一落在 z<q<=x 或 x<q<P；前者是 completed-internal label，后者是原 CLB 高标签。 | 后续容量账本必须分别处理两个 label band。 |
| `FormalUnitEmbeddingInterfaceImported` | `true` | `true` | witness obligation 域已有 physical atoms、return records 与 quotient records，可容纳 prefix atom 字段。 | 需要写入 prefix_cutoff_z 与 capacity_multiplier_id。 |
| `NoLossAccountingImported` | `true` | `true` | 义务进入 O_z(w) 后只能成为 source、return 或 quotient/reuse，不允许静默丢失。 | no-loss 是加权守恒，不是不同实例下界。 |
| `PrefixResidualWeightedTransferClosed` | `true` | `true` | 每个 prefix 残洞 canonically 注入一个加权 formal-unit obligation atom，且保留 label band 与容量乘子字段。 | PrefixResidualToWeightedFormalUnitObligationInjection |
| `PrefixTransferEffectiveForTypeCompressionCurrentCorpusProved` | `false` | `false` | 尚未证明这些加权 prefix atoms 可直接提供类型压缩所需的有效不同实例数。 | RegisteredPrefixCapacityMultiplierDiscipline AND PrefixWeightedObligationToEffectiveTypeInstanceAntiCollapse |
| `PrefixCapacityMultiplierCurrentCorpusProved` | `false` | `false` | completed-internal labels q<=x 可在同一行内多次命中；必须证明容量乘子不会吞掉 prefix 势。 | RegisteredPrefixCapacityMultiplierDiscipline |
| `PrefixAntiCollapseCurrentCorpusProved` | `false` | `false` | 尚未证明 quotient/reuse 不会把大量 prefix atoms 压成过少 row-free type instances。 | PrefixWeightedObligationToEffectiveTypeInstanceAntiCollapse |
| `PrefixResidualTransferHardpointStatus` | `true` | `true` | 原 hardpoint 的加权转移层已闭合；强形式的有效实例转移仍开放。 | PrefixResidualEffectiveTypeInstanceTransfer |

## 4. 下一最窄点

```text
RegisteredPrefixCapacityMultiplierDiscipline
```

并行保留：

```text
PrefixWeightedObligationToEffectiveTypeInstanceAntiCollapse
```

审稿边界：本步只闭合 prefix 残洞到加权义务的注入，不闭合有效不同实例下界，也不闭合行/列无条件命题。
