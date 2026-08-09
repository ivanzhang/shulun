# MFAC 自由行扩张反模型与语义锚定刚性设计

## 目标

为最小半素数 triad 建立一个条件性元定理：只要 declaration 系统没有把 row universe 与
alpha/delta 行泛函独立、预先且不可扩张地固定，那么仅靠字段完整性、局部自然性、局部
系数律和形式 prepushforward identity，不能推出“所有 noncanonical declaration 必然
canonical factorization 或 rowwise cancellation”。

该反模型的价值是定位证明义务：真正的 no-go 或真正的 source 构造都必须经过
`ActualAlphaDeltaRowRealizationRigidityBeforePushforward`，而不是继续增加 schema 字段。

## 非目标

- 不证明任何实际 arithmetic noncanonical declaration 在数学上不存在。
- 不把自由行反模型称为 actual primitive source、alpha/delta 构造、signed transport、
  `ψ` 平滑误差、零点排除或 RH 结论。
- 不修改当前的 D/E 全局 transport、LPF/Phi 支撑、RIW/Buchstab canonical 公式或终端
  PDEC/CleanKLS 路线。
- 不以 synthetic model 反向否定一个未来可能出现的独立算术恒等式。

## 反模型的显式构造

固定两个不同素数构成的无序集合 `P={p,q}`。对每个
`d in {p,q,p*q}`，引入一个自由 row symbol：

```text
r(P,p), r(P,q), r(P,p*q)
```

令 `V_P` 是这些 row symbols 生成的自由实向量空间，基为
`e(P,p), e(P,q), e(P,p*q)`。定义三项 declaration：

```text
D(P,d) = (
  source=P,
  row=r(P,d),
  branch=b(P,d),
  origin=o(P,d),
  orientation=+1,
  local_factor=1,
  exact_uv=(d,p*q/d),
  return=none
)
```

定义行系数：

```text
c(r(P,p))   = +log(p)
c(r(P,q))   = +log(q)
c(r(P,p*q)) = -log(p*q)
```

并定义自由 prepushforward payload：

```text
T(P) = log(p)e(P,p) + log(q)e(P,q) - log(p*q)e(P,p*q)
```

取线性总和映射 `Sigma_P(e(P,d))=1`，则：

```text
Sigma_P(T(P)) = log(p) + log(q) - log(p*q) = 0
```

因此该模型可保持 global triad 零和，同时保留三个不同、各自非零的 row coefficient。
交换 `p,q` 时，令 `r(P,p)` 与 `r(P,q)`、`b(P,p)` 与 `b(P,q)`、`o(P,p)` 与 `o(P,q)`
同步交换，`r(P,p*q)` 固定；故模型具有素因子交换自然性。

## 条件性元定理

设一个 declaration 公理系统仅要求：

1. 每项有 pre-Cauchy、下游独立、origin、registration、row、orientation、local factor、
   exact `(u,v)` 与形式 prepushforward 字段；
2. declaration 具有素因子交换自然性；
3. row coefficient 等于其 row fiber 内的 `-mu(d) log(d)` 局部和；
4. global payload 在总和投影下守恒；
5. 允许为候选增加新的 row symbol，或未给出限制这种增加的独立算术语义。

则上述自由行构造是该系统的模型。特别地，该系统不能仅凭这些公理推导：

```text
所有 noncanonical declaration 都 canonicalize
OR
所有 triad 都 rowwise cancel
```

这是“当前 schema-only no-go 不足”的条件性模型论结论。第 5 条是关键假设；若将来给出
独立且不可自由扩张的 actual row realization，该自由模型就不再自动适用。

## 必须新增的语义锚定合同

为排除自由行反模型，下一门至少应提供：

```text
fixed_actual_row_universe
no_free_row_extension
independently_defined_alpha_delta_row_functional
declaration_to_actual_row_realization_identity
cross_pair_gluing_compatibility
origin_selector_non_tag_injection
prepushforward_identity_as_fixed_equality
```

含义如下：

| 合同 | 排除的伪构造 |
| --- | --- |
| `fixed_actual_row_universe` | 为每个 `(p,q,d)` 任意新增 row |
| `no_free_row_extension` | 以自由向量空间补写 row basis |
| `independently_defined_alpha_delta_row_functional` | 先造 declaration 再定义 alpha/delta payload |
| `declaration_to_actual_row_realization_identity` | 用布尔 `prepushforward_identity=true` 代替等式 |
| `cross_pair_gluing_compatibility` | 对每个素数对单独造互不相干的模型 |
| `origin_selector_non_tag_injection` | 把 `(p,q,d)` 本身改名为 origin selector |
| `prepushforward_identity_as_fixed_equality` | 在自由 payload 空间中把守恒写成定义 |

只有这些语义字段由独立算术对象给定后，才可开始尝试“所有 admissible noncanonical triad
都不可能存在”的真正不可能证明，或将一个 surviving triad 认定为真实正向 source。

## 最小审计设计

后续审计器必须同时覆盖以下四类输入：

1. **自由三行反模型**：字段与交换自然性均通过，但 `actual_row_universe_fixed=false`；
   它必须证明 schema-only no-go 不可得，而不能被误报为 actual source。
2. **tag 注入变体**：`origin_selector=(p,q,d)`，没有独立函数；必须被标记为
   `origin_tag_injection`。
3. **固定行 universe 缺失 alpha/delta 泛函**：不得被误报为语义锚定闭合。
4. **完整 synthetic semantic anchor**：只有同时给定固定 universe、独立 alpha/delta
   functional、realization identity、cross-pair gluing 与 no-free-extension 时，才允许通过
   `semantic_anchor_contract_complete`。它仍只是 fixture，不是当前语料的实际证明。

当前语料预期：

```text
free_row_countermodel_constructed=true
schema_only_impossibility_proof_available=false
actual_alpha_delta_semantic_anchor_present=false
mathematical_nonexistence_proved=false
rh_proved=false
row_column_unconditional_closed=false
next_positive_gate=ActualAlphaDeltaRowRealizationRigidityBeforePushforward
```

## 产物与验证

用户审阅本规格后，实施阶段新增：

- `experiments/prime_matrix_mfac_free_row_extension_no_go_audit.py`
- `experiments/prime_matrix_mfac_free_row_extension_no_go_audit_test.py`
- `docs/monograph/prime-matrix-mfac-free-row-extension-no-go-audit.json`
- `docs/monograph/prime-matrix-mfac-free-row-extension-no-go-audit.md`

定向测试必须验证自由模型的三项 distinct-row 系数、交换等变、总和投影零和、tag 注入拒绝、
固定语义锚定 fixture 通过及当前语料边界。全族回归仍使用：

```bash
python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v
```
