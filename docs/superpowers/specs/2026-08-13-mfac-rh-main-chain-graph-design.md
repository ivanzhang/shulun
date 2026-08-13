# MFAC 全项目 RH 主链依赖图设计

**日期：** 2026-08-13

**状态：** 已确认设计，待用户审阅书面规格

## 1. 目的与范围

本阶段把阶段 1 的 `prime-matrix-mfac-project-inventory-audit.json` 作为唯一模块状态输入，
以预注册人工对照表将全部库存模块映射到 RH 主链义务、循环/不足边或明确旁路角色。
它不从文件名、源码、Markdown 或证书状态文本推断数学蕴含；状态文本只由阶段 1 库存
原样携带，不能自动推进任何主链节点。

图谱覆盖固定节点：

- `W0`：独立实际见证；
- `W1`：统一去常数强制性或固定 Möbius 尾和 L² 门槛；
- `W2`：实际 Chebyshev 能量桥；
- `W3`：dyadic 到 Mellin 可和性；
- `W4`：Mellin 控制到零自由区域；
- `W5`：零自由区域到 RH；
- `C1`--`C7`：既有 RH 义务规格中的循环、条件或有限证据不足边；
- `no_direct_rh_role`：只能提供局部结构、构造审计或反模型信息，不能直接成为 RH 正向边的模块角色。

## 2. 唯一输入与严格覆盖

审计器仅读取阶段 1 库存 JSON 的 `modules` 列表。启动时比较其模块名集合与内部
`MODULE_ROLE_REGISTRY` 的键集合：

- 库存有而登记表没有的模块进入 `unmapped_modules`，审计立即失败；
- 登记表有而库存没有的模块进入 `stale_registry_modules`，审计立即失败；
- 只有两者集合严格相等时，才生成 JSON/Markdown 图谱。

每个模块登记为一个非空角色序列；允许多个角色，并且每个角色是以下结构：

```text
{
  "node": "W0" | ... | "W5" | "C1" | ... | "C7" | "no_direct_rh_role",
  "relation": "forward_obligation" | "conditional_dependency" |
              "cycle_detected" | "insufficient_not_cycle" | "no_direct_rh_role",
  "rationale": "人工审阅的明确角色说明"
}
```

禁止从库存分类自动生成角色。预注册表是唯一角色来源；库存仅提供模块可用状态和
阶段 1 的 RH 阻断理由。

## 3. 预注册模块角色

当前阶段 1 库存的 19 个模块必须全部逐项登记：

| 模块 | 预注册角色 |
| --- | --- |
| `actual_lcm_gram_energy` | `W0` forward；`W1` forward |
| `actual_record_constructor` | `W0` forward；`C1` cycle_detected |
| `centered_divisibility_covariance` | `W1` forward；`C1` cycle_detected |
| `colored_divisor_word_transport` | `no_direct_rh_role` |
| `global_free_mellin_mode_no_go` | `C6` insufficient_not_cycle；`W3` forward |
| `lcm_offconstant_projection_circularity` | `C1` cycle_detected；`W1` forward |
| `mertens_conditional_l2_upper` | `W1` conditional_dependency；`C7` conditional_dependency |
| `mertens_randomness_contraction` | `W3` conditional_dependency；`C7` conditional_dependency |
| `mobius_tail_l2` | `W1` forward；`C7` conditional_dependency |
| `orientation_provenance_no_go` | `C1` cycle_detected；`no_direct_rh_role` |
| `primitive_normalization_underdetermination` | `W0` forward；`no_direct_rh_role` |
| `project_inventory` | `no_direct_rh_role` |
| `registration_hash` | `no_direct_rh_role` |
| `rough_cofactor_mobius_signed_transport` | `W0` forward；`no_direct_rh_role` |
| `semiprime_local_naturality_factorization` | `W0` conditional_dependency；`no_direct_rh_role` |
| `semiprime_triad_dispatch` | `W0` forward；`no_direct_rh_role` |
| `square_base_seed_binding` | `W0` forward；`no_direct_rh_role` |
| `truncated_mobius_log_coercivity` | `W1` forward；`C5` insufficient_not_cycle |
| `uniform_offconstant_coercivity` | `W1` forward；`C5` insufficient_not_cycle |

该表只标记可审计的关系，不把任一 `forward_obligation` 解读为“义务已证明”。
特别是 `W2`、`W4`、`W5` 当前没有支持模块，不得以表格空白外推任何完成状态。

## 4. 主链、状态与循环规则

固定主链边为：`W0→W1→W2→W3→W4→W5→RH`。每条边记录前置、目标、
支持模块、禁止输入、当前状态和阻断理由。

节点状态由以下保守规则决定：

1. 有任一关联模块的阶段 1 分类为 `conditional_or_external_dependency`，或该节点
   含 `conditional_dependency` 角色时，状态至少为 `conditional`；
2. 有任一 `cycle_detected` 角色或对应 `C1`--`C4` 循环边时，状态为
   `cycle_detected`，但循环边不被当作正向支持；
3. 只有有限审计、开放证书或 `insufficient_not_cycle` 信息时，状态为 `unproved`；
4. 没有任何支持模块时，状态为 `not_started`；
5. `proved` 只允许未来明确提供独立、无循环、全称证明与可核查引用时手工登记；
   本阶段的实现不产生 `proved`。

固定循环/不足边保持既有语义：

- `C1`：Chebyshev 误差或目标量回灌到 W0/W2；
- `C2`：待建立 Mellin 范数回推 W2；
- `C3`：零点/零自由区回推 W3/W4；
- `C4`：RH 或等价平方根消去输入回灌 W1--W5；
- `C5`：有限剖面不足以建立 W1/W3/W4；
- `C6`：自由乘法模型不足以建立实际 W3；
- `C7`：Mertens/PNT 消去只能作条件依赖，不能认证 MFAC 自足 L² 尾和界。

`W2`、`W4`、`W5` 的无模块支持是主链的最短明确阻断路径；图谱必须将其写为
`W1→W2` 的 `unproved` 边，而不是假装跳过 W2 到达 Mellin 或零点结论。

## 5. 产物与 RH 边界

默认 CLI 生成：

- `docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.json`；
- `docs/monograph/prime-matrix-mfac-rh-main-chain-graph-audit.md`。

JSON 至少包含库存路径、模块数、预注册映射版本、逐模块角色和库存分类、`W0`--`W5`
节点表、主链边、`C1`--`C7` 表、`unmapped_modules`、`stale_registry_modules`、
`shortest_blocking_path`、`rh_chain_closed` 和 `rh_proved`。Markdown 提供逐模块表、
节点/边表、循环边表与最短阻断路径。

顶层始终满足：

```text
rh_chain_closed=false
rh_proved=false
```

即使阶段 1 的某一未来记录出现 `rh_proved=true`，它也只能由阶段 1 标为人工复核，
不能更改本图的顶层结论。本图不验证数学证明，故不具有认证 RH 的能力。

## 6. 测试与验收

测试在临时库存 JSON 上覆盖：

1. 当前全量 19 模块的预注册登记与多角色保留；
2. 缺失库存模块或多余登记模块会阻断生成；
3. 条件依赖不推进 W1/W3 成 `proved`；
4. `cycle_detected` 和 `insufficient_not_cycle` 与正向义务严格区分；
5. 无 W2/W4/W5 支持时主链出现明确未闭合边和最短阻断路径；
6. 输入库存出现 `rh_proved=true` 仍不会使图谱的 `rh_proved` 为真；
7. JSON/Markdown 证书、CLI 以及库存路径声明可复现；
8. 全量 MFAC 测试仍通过。

阶段 2 完成后只暂存本规格、本计划、新审计器、新测试和两种图谱证书，运行
`git diff --check` 与全量 MFAC 回归后单独提交。既有未提交文件不得进入该提交。

## 7. 非目标

- 不证明或计算 W0--W5 中的任何开放全称定理；
- 不改变阶段 1 库存分类、不执行被映射模块、不从源代码自动分配数学角色；
- 不把 `forward_obligation`、有限恒等式、条件消去、无反例扫描或人工声明升级为
  独立无循环证明；
- 不生成 Graphviz、网络图或其他额外可视化；
- 不将图谱解释为 RH、零自由区、Mellin 收缩或 Chebyshev 能量桥的证明。

## 使用示例

```bash
python3 experiments/prime_matrix_mfac_rh_main_chain_graph_audit.py \
  --inventory docs/monograph/prime-matrix-mfac-project-inventory-audit.json \
  --json-out /tmp/mfac-rh-main-chain-graph.json \
  --markdown-out /tmp/mfac-rh-main-chain-graph.md
```

该命令只将预注册映射与库存状态组合成保守依赖图；它不运行模块、不推断新定理，
也不会输出 RH 已证明。
