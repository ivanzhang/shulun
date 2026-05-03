# FO-PDEC 多重计数合法性审查

**状态：** `multiplicity_legitimacy_required_for_pdec_threshold`

本文继续硬攻 `FO-PDEC`，处理显式阈值账本中的一个关键审稿风险：最佳投影
`ell=199,h=95` 的质量 `4` 是否由四个独立坏窗方程构成，还是包含嵌套块或跨层复用的同一物理候选。

## 1. 为什么必须审查多重性

`PDEC` 证书模板要求下界和上界作用于同一个坏窗集合 `S`。如果 `S` 是多重方程集合，则
嵌套块、跨层复用可以计入质量；如果 `S` 是物理候选集合，则必须去重。两种口径不能混用。

因此要使用

\[
  M_{199}=3.959247567099438
\]

必须证明正式反例链抽取出的 `S` 的确是 equation/block-local 多重集合，而不是 physical
候选集合。

## 2. Primitive cluster 审计

新增脚本：

```text
experiments/prime_matrix_wsh_fo_pdec_primitive_cluster_audit.py
```

输出：

```text
docs/monograph/prime-matrix-wsh-fo-pdec-primitive-cluster-audit.md
docs/monograph/prime-matrix-wsh-fo-pdec-primitive-cluster-audit.json
```

对 `ell=199,h=95` 审计四种口径：

| mode | mass | Fourier | mass defect | dual arc |
| --- | ---: | ---: | ---: | ---: |
| equation | 4 | 3.959247567099438 | 0.04075243290056196 | 11 |
| block-local | 4 | 3.959247567099438 | 0.04075243290056196 | 11 |
| layer-local | 3 | 2.9698366905785227 | 0.03016330942147727 | 11 |
| physical | 2 | 1.9699193446802263 | 0.030080655319773664 | 11 |

物理候选只有两个：

```text
candidate 1664237, factor 199;
candidate 250541, factor 199.
```

其中 `1664237` 由嵌套长块重复出现，`250541` 在不同筛层中复用。

## 3. 结论：阈值口径二分

当前必须把最后硬点拆成精确二分：

```text
Multiplicity-Legitimacy:
正式坏窗集合 S 是否允许 equation/block-local 多重计数？
```

若答案是“允许”，则保留强阈值：

\[
  U_{\rm CRT,199}<3.959247567099438。
\]

若答案是“不允许”，必须使用 primitive 口径：

\[
  U_{\rm CRT,199}^{\rm phys}<1.9699193446802263。
\]

两种口径都仍是短弧聚簇问题，但常数不同。

## 4. 可证明的充分条件

要合法使用多重方程口径，需证明至少一项：

1. **嵌套块独立性。** 不同长块在 Hall/PDEC 证书中代表不同约束行，不能合并；
2. **层局部独立性。** 同一物理候选在不同 `q` 层产生不同行相位约束，属于不同坏窗；
3. **多重集合证书。** `PDEC` 模板中的 `S` 明确允许带 multiplicity，且 `U_CRT` 上界也按同一 multiplicity 计算。

若三项都不能证明，则必须使用 physical 去重口径，并把嵌套/跨层重复改写为 `SAE/Endpoint`
或递归壳层重复出口。

## 5. 当前真实剩余

当前不能直接宣称

```text
U_CRT,199 < 3.959247567099438
```

因为这依赖多重计数合法性。现在的最小硬点是：

```text
prove multiplicity legitimacy
or close primitive threshold
or absorb duplicates by SAE/Endpoint.
```

该审查没有削弱主线；它防止在最后一步用错误的集合口径完成“伪闭合”。全局无条件证明必须先通过这一步。

## 6. Formal unit 一致性更新

进一步新增：

```text
experiments/prime_matrix_wsh_fo_pdec_formal_unit_audit.py
docs/monograph/prime-matrix-wsh-fo-pdec-formal-unit-audit.md/json
docs/monograph/prime-matrix-wsh-fo-pdec-formal-unit-route.md
```

审计结果显示，强阈值 `3.959...` 不仅依赖多重计数，还依赖跨 `q` 层的有限证书库聚合：

```text
global_library_raw: mass=4, Fourier=3.959247567099438
q_row_coordinate_dedup / block_local / offset_row: best Fourier=1.0
```

因此正式 `PDEC` 使用强阈值前必须再证明：

```text
FormalUnit-Stitching:
跨 q 层事件确实属于同一个持久坏窗族；

NestedBlock-Independence:
嵌套块重复确实代表独立 Hall/PDEC 约束行。
```

若这两个接口不能闭合，强阈值只能作为诊断聚簇，不能作为全局无条件证明的下界。
