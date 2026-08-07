# MFAC Actual Record Constructor Audit Design

**目标：** 审计现有 formal-unit 路由是否真的构造了从假设 early-zero-row witness 到 actual noncanonical atomic source record 的前向映射；若没有，则给出最早缺失字段和禁止的后验依赖。

**非目标：** 本工作不构造数值反例、不声称 RH、不会把 schema、全局 Möbius 项或 LPF 无符号 ownership 命名为 actual noncanonical primitive record。

## 问题定义

在反证分支中，数值化的真实 witness 不可作为前提。要求的对象是条件性但构造性的函数：

```text
W -> AtomicNoncanonicalRecord(W) | NamedReturn(W)
```

其中 `W` 是任意假设 early-zero-row witness。`AtomicNoncanonicalRecord` 必须在 Cauchy/dispersion、payment、pushforward、terminal table 之前产生；`NamedReturn` 必须是 PDEC、SAE、Rankin 或其它已命名失败出口。

## 审计结论的层级

1. `schema_closed`：字段名与哈希纪律存在。
2. `router_closed`：来源族与回流路由已列出。
3. `witness_to_record_constructor_present`：代码或证书接受 witness 并逐字段生成 record。
4. `actual_noncanonical_atomic_record_present`：至少一个生成 record 同时具备来源选择、非规范成员资格、pre-Cauchy 时间锁和原子 payload。

只有第 4 层可定义 branch alphabet。第 1、2 层均不能推出第 3、4 层。

## 最小 record 合约

审计器将要求原子记录具备以下字段：

```text
witness_id
formal_unit_id
source_family_id
origin_selector
source_class=actual_noncanonical
pre_cauchy_timestamp
basis_word
divisor_history
branch_key
orientation
local_factor
signed_coefficient
exact_u
exact_v
row_key
named_return
```

`origin_selector` 是首要字段：它必须在同一 formal unit 和 source family 内，前向确定具体 primitive summand；没有它，basis word、branch key 和 signed payload 都没有定义域。

## 禁止依赖

构造器或 record 字段不得读取、反推或由下列对象填补：

```text
payment
Gamma
pushforward image
Cauchy/dispersion output
terminal/origin table
zero-row coverage geometry
external spectral estimate
```

来自这些对象的任何字段都标记为 `downstream_recovery_used=true`，不能作为合法构造。

## 方案 A 的实现范围

新增一个独立 Python 审计器及其 unittest：

- 读取现有 formal-unit、universal-extractor、source-tuple、actual-constructor 与 LPF ownership 路由证书；
- 静态核验是否存在 witness 参数、record 产物、原子字段以及非循环依赖；
- 输出 JSON/Markdown 证书，包含 `witness_to_record_constructor_present`、`actual_noncanonical_atomic_record_present`、`earliest_missing_field` 与 `branch_alphabet_domain_defined`；
- 对当前语料预期输出负面结论：最早缺失字段是 `origin_selector`，且 branch alphabet 尚无定义域；
- 明确把现有 global Möbius D/E record 与 LPF ownership 标记为不可替代 actual noncanonical record 的旁路证据。

## 成功标准

- 审计器不接受仅有 `closed/proved` 布尔值的路由 JSON 作为 witness-to-record 构造证据。
- 审计器能够区分空 record inventory、缺 witness 输入和缺 primitive payload 三类失败。
- 输出不使用任何数值反例或 RH 结论。
- 测试覆盖当前语料的主结论，以及一个合成的完整 record 正例，确保审计标准不是“永远失败”。

## 预期后续门

若方案 A 的负面证书成立，唯一合法主攻点更新为：

```text
PreCauchyActualNoncanonicalAtomicRecordConstructorOrNamedReturn
```

其数学内容不是扩展 schema，而是证明一个不读取下游数据的选择/发射律：

```text
Select(W) -> origin_selector -> atomic payload rows | named return
```
