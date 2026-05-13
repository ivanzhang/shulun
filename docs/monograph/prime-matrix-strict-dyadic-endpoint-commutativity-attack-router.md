# Prime Matrix strict dyadic 乘积窗口端点交换律攻坚路由器

**状态：** `dyadic_endpoint_commutativity_reduced_to_product_window_formula_binding_open`

`DyadicProductWindowEndpointCommutativityLedger` 的纯取整子引理可以闭合：对正整数 `a,b,n`，`floor(floor(n/a)/b)=floor(n/(ab))` 且 `ceil(ceil(n/a)/b)=ceil(n/(ab))`；取 `a,b` 为 2 的幂时，端点外向缩放只依赖总指数。因此只要现有 product window ledger 的 `I_W` 端点确实由这种 dyadic 外向缩放公式生成，dyadic 重排交换律就成立。当前仍缺的是把 `I_W` 与 `C_core(W)` 绑定到该 machine-readable 端点公式；否则端点差异必须作为边界相位缺陷回流。

```text
dyadic_directed_rounding_associativity_closed=true
dyadic_endpoint_commutativity_conditional_on_formula_closed=true
product_window_endpoint_formula_binding_proved=false
cold_core_threshold_order_invariance_proved=false
dyadic_product_window_endpoint_commutativity_ledger_proved=false
row_column_unconditional_closed=false
```

## 证明原子

| name | statement | status | meaning |
|---|---|---|---|
| `floor_associativity` | `floor(floor(n/a)/b)=floor(n/(ab)) for positive integers a,b,n` | `closed_elementary` | 外向左端点若由整数下取整给出，逐步缩放与一次缩放相同。 |
| `ceil_associativity` | `ceil(ceil(n/a)/b)=ceil(n/(ab)) for positive integers a,b,n` | `closed_elementary` | 外向右端点若由整数上取整给出，逐步缩放与一次缩放相同。 |
| `dyadic_commutativity` | `2^a 2^b=2^b 2^a and directed endpoint rounding depends only on a+b` | `closed_if_formula_bound` | dyadic 顺序交换不会改变规范化后的端点。 |
| `formula_binding_gap` | `current corpus says I_W is inherited from product window ledger, but does not expose the endpoint update formula` | `open_binding` | 必须把现有窗口账本绑定到上述外向端点缩放公式。 |
| `defect_route` | `if product window endpoints are not the directed dyadic scaling endpoints, the discrepancy is a boundary phase defect` | `registered_route_open` | 公式绑定失败不能留作自由差异，必须进入 PDEC/ColumnCRT/热核心。 |

## 取整样本审计

| n | first_power | second_power | floor_ok | ceil_ok | floor_value | ceil_value |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | `true` | `true` | 0 | 1 |
| 1 | 1 | 2 | `true` | `true` | 0 | 1 |
| 1 | 2 | 1 | `true` | `true` | 0 | 1 |
| 1 | 3 | 4 | `true` | `true` | 0 | 1 |
| 1 | 4 | 3 | `true` | `true` | 0 | 1 |
| 1 | 5 | 8 | `true` | `true` | 0 | 1 |
| 1 | 8 | 5 | `true` | `true` | 0 | 1 |
| 2 | 1 | 1 | `true` | `true` | 0 | 1 |
| 2 | 1 | 2 | `true` | `true` | 0 | 1 |
| 2 | 2 | 1 | `true` | `true` | 0 | 1 |
| 2 | 3 | 4 | `true` | `true` | 0 | 1 |
| 2 | 4 | 3 | `true` | `true` | 0 | 1 |
| 2 | 5 | 8 | `true` | `true` | 0 | 1 |
| 2 | 8 | 5 | `true` | `true` | 0 | 1 |
| 3 | 1 | 1 | `true` | `true` | 0 | 1 |
| 3 | 1 | 2 | `true` | `true` | 0 | 1 |
| 3 | 2 | 1 | `true` | `true` | 0 | 1 |
| 3 | 3 | 4 | `true` | `true` | 0 | 1 |
| 3 | 4 | 3 | `true` | `true` | 0 | 1 |
| 3 | 5 | 8 | `true` | `true` | 0 | 1 |
| 3 | 8 | 5 | `true` | `true` | 0 | 1 |
| 17 | 1 | 1 | `true` | `true` | 4 | 5 |
| 17 | 1 | 2 | `true` | `true` | 2 | 3 |
| 17 | 2 | 1 | `true` | `true` | 2 | 3 |
| 17 | 3 | 4 | `true` | `true` | 0 | 1 |
| 17 | 4 | 3 | `true` | `true` | 0 | 1 |
| 17 | 5 | 8 | `true` | `true` | 0 | 1 |
| 17 | 8 | 5 | `true` | `true` | 0 | 1 |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `EndpointCommutativityTargetImported` | `true` | `false` | 上一层已把 dyadic 顺序规范化压到窗口端点交换律。 | `DyadicProductWindowEndpointCommutativityLedger` |
| `TerminalWindowObjectExists` | `true` | `true` | 现有材料有 I_W，但只作为继承自 product window ledger 的对象。 | `ProductWindowEndpointDyadicUpdateFormulaBindingLedger` |
| `DyadicDirectedRoundingAssociativityClosed` | `true` | `true` | 若端点由 dyadic 外向整数缩放生成，则逐步缩放与一次缩放等价。 | `DyadicDirectedEndpointRoundingAssociativityLemma` |
| `DyadicEndpointCommutativityConditionalClosed` | `true` | `true` | 在端点生成公式已绑定的条件下，dyadic 重排不改变 I_W。 | `ProductWindowEndpointDyadicUpdateFormulaBindingLedger` |
| `ProductWindowEndpointFormulaBindingProved` | `false` | `false` | 当前语料没有 machine-readable 端点更新公式，无法把 I_W 直接绑定到 dyadic 缩放。 | `ProductWindowEndpointDyadicUpdateFormulaBindingLedger` |
| `ColdCoreThresholdOrderInvarianceProved` | `false` | `false` | C_core(W) 是否随 dyadic 重排不变仍需绑定到同一端点/尺度公式。 | `ColdCoreThresholdDyadicOrderInvarianceBindingLedger` |
| `BoundaryRoundingDefectRouteRegistered` | `true` | `false` | 若端点公式绑定失败，差异必须作为边界相位缺陷回流。 | `DyadicBoundaryRoundingPhaseDefectPDECRoute` |
| `DyadicProductWindowEndpointCommutativityLedgerProved` | `false` | `false` | 取整交换律已闭合，但端点公式绑定与阈值不变性未闭合。 | `ProductWindowEndpointDyadicUpdateFormulaBindingLedger AND ColdCoreThresholdDyadicOrderInvarianceBindingLedger` |
| `DyadicValuationOrderCanonicalizationOrPhaseDefectProved` | `false` | `false` | 端点交换律未完成，dyadic 顺序规范化仍未闭合。 | `DyadicValuationOrderCanonicalizationOrPhaseDefectLedger` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `ProductWindowEndpointDyadicUpdateFormulaBindingLedger AND DyadicPathDependentColdWindowPhaseDefectPDECRoute AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`ProductWindowEndpointDyadicUpdateFormulaBindingLedger`。
- 并行保留：
  - `ColdCoreThresholdDyadicOrderInvarianceBindingLedger`
  - `DyadicBoundaryRoundingPhaseDefectPDECRoute`
  - `DyadicPathDependentColdWindowPhaseDefectPDECRoute`
  - `TerminalColdWindowCompatibilityAntiCascadeLemma`
  - `DyadicPrimePowerColdWindowCascadeExclusionLemma`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-dyadic-cold-window-cascade-attack-router.json` | `d5290090d5795c0bc5bb07b97fd80e6abff01e418cf622d478be09d28906c2ff` |
| `docs/monograph/prime-matrix-strict-dyadic-order-canonicalization-attack-router.json` | `79546568237d185e80dbdda61925d826d911b95389b2966ffc575d87cb77140e` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `experiments/prime_matrix_strict_dyadic_endpoint_commutativity_attack_router.py` | `e0ee879004f1681f1389823bca11123bd04378e9018bb6ea4b486a1fd03b7ea9` |
