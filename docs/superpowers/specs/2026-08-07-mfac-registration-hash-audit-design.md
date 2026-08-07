# MFAC Registration Hash Audit Design

**目标：** 审计现有 formal-unit hash、source-tuple hash 与 source-record hash 是否前向编码 actual emitter registration；若没有，明确给出首缺 registration 字段，并禁止用哈希或 payload 反向补出 primitive source 身份。

**非目标：** 本工作不证明哈希函数数学上不可逆、不构造 RH 反例、不声称任何 raw carrier 或 D/E word 已是 actual noncanonical primitive row。

## 核心区分

现有哈希纪律锁定的是反证分支中的容器与坐标：

```text
formal_unit_id
source_tuple_hash
source_record_hash
return_record_hash
```

actual primitive registration 则至少需要：

```text
emitter_id
primitive_slot
same_formal_unit_certificate
```

若上述 registration 三元组不在前向构造器或 record 中显式输出，哈希只能标识容器，不能定义 actual source ownership。

## 审计输入与判据

审计器读取：

- `prime-matrix-canonical-formal-unit-hash-stability-router.json`；
- `prime-matrix-strict-actual-emitter-source-table-router.json`；
- `prime-matrix-mfac-actual-record-constructor-audit.json`；
- 已登记的 `prime_matrix_actual_noncanonical_atomic_record_constructor` manifest。

当前语料判定为负，必须同时满足：

```text
hash_contains_registration_fields=false
actual_source_table_constructed=false
registration_recoverable_from_hash=false
earliest_missing_registration_field=emitter_id
```

合成 manifest 正例只有同时提供 `emitter_id`、`primitive_slot`、`same_formal_unit_certificate`，并且构造器无 downstream dependency 时才允许通过。

## 禁止路径

下列对象不能补写 registration：

```text
payment
Gamma
pushforward image
Cauchy/dispersion output
terminal/origin table
zero-row coverage geometry
external spectral estimate
```

若 manifest 依赖任一对象，审计器必须拒绝其 registration。

## 成功标准

- 当前语料的机器证书明确报告 registration 无法由 hash 恢复。
- 合成正例证明审计判据不是恒负。
- 具有相同 hash 字段但缺少 registration 三元组的 manifest 必须失败。
- 文档只作“当前语料未提交前向 registration 证据”的结论，不作数学不可能、零点排除或 RH 结论。

## 后续数学门

本审计若通过，下一唯一正向输入为：

```text
PreCauchyCarrierColoredWordSameFormalUnitSourceRegistrationOrNamedReturn
```

其内容必须是一个独立的前向发射律：

```text
(W, carrier, D/E-word) -> (emitter_id, primitive_slot, same_unit_certificate) | named return
```
