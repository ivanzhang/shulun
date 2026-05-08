# Prime Matrix ColumnCRT 到 PDEC/SAE 吸收路由器

**状态：** `columncrt_absorbed_to_pdec_sae_terminal_two_family_remainder`

ColumnCRT 独立终端已吸收到 PDEC/SAE。第一包的独立剩余进一步压成两族：全局 SAE 证书族与包含 displacement/endpoint/cofactor/primitive 的 PDEC 证书族。

## 1. 吸收律

ColumnCRT is not an independent terminal certificate family. A persistent nonzero displacement overload is a displacement PDEC on an enlarged finite signature; a sparse displacement overload is SAE/endpoint; and balanced displacement loads become admissible PDEC-dual constraints. RPZ unit endpoint gates show why threshold tuning alone cannot close the branch, but they do not prevent absorption into endpoint/displacement PDEC or SAE.

```text
columncrt_independent_terminal_removed=true
terminal_package_fully_proved=false
row_column_unconditional_closed=false
```

## 2. 审查表

| gate | closed | evidence | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TerminalPackageStillListsColumnCRT` | `true` | terminal compression output contains ColumnCRT | 上一轮压缩后 ColumnCRT 仍暂列独立证书族。 | decide whether it is genuinely independent |
| `ColumnCRTRoutingContractClosed` | `true` | h4-pdec-column-defect-routing-contract | 列位移缺陷已有同口径、相位兼容和条件路由合同。 | exclusion not supplied by the contract |
| `RPZFixedDisplacementGateMaterialized` | `true` | rpz unit endpoint columncrt gate | RPZ unit seam 的固定非零位移入口已材料化。 | exclude the gate or absorb it |
| `ThresholdTuningDoesNotExclude` | `true` | rpz columncrt threshold obstruction | 调小 L_D 只触发 ColumnCRTDefect，不能给矛盾。 | use endpoint-PDEC, avoidance, or independent theorem |
| `ColumnCRTDisplacementAbsorption` | `true` | columncrt displacement pdec absorption | 持久非零位移过载就是 displacement PDEC；孤立位移过载就是 SAE-column。 | prove displacement PDEC or SAE |
| `PersistentAdmissionAbsorbsColumnCRT` | `true` | persistent terminal admission router | 裸 ColumnCRT 不能准入终端，必须先转成 displacement/primitive PDEC 或 SAE。 | primitive same-formal-unit PDEC |

## 3. 吸收后的独立终端输入

- Global SAE finite/window/local-survivor certificate family
- PDEC family including displacement/endpoint/cofactor/primitive certificates

## 4. 判定

ColumnCRT 的固定非零位移入口是真实结构，但不是第三类独立终端。若它持久，必须作为 displacement PDEC 在同一 formal unit 上提交 `U_CRT<L_PDEC`；若它孤立，则进入 SAE/endpoint；若位移负载平衡，则变成 PDEC 对偶证书的合法约束行。因此第一包下一步只剩 PDEC family 与 SAE family 两族证书。
