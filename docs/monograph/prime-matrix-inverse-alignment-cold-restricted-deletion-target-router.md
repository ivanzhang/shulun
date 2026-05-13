# Prime Matrix inverse alignment cold-restricted 删除目标路由器

**状态：** `cold_restricted_exact_x_deletion_target_table_closed_lower_bound_open`

Cold-restricted exact-x 目标已经被量化：对每个 exact x 样本，若原始后缀容量为整数 C，要得到严格 `U_np<M#`，至少要删除 `floor(C-M#)+1` 个后缀容量单位。这把抽象的 cold deletion 需求变成可验目标表。当前仍未证明真实 cold/no-return/回流纪律一定达到该删除下界；下一最窄点是 `ColdRestrictionDeletionLowerBoundAgainstExactXTable`。

```text
exact_x_raw_capacity_obstruction_imported=true
required_deletion_formula_closed=true
exact_x_deletion_target_table_closed=true
cold_return_routes_imported=true
cold_restricted_exact_x_supply_deletion_ledger_closed=true
cold_restriction_deletion_lower_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 所需删除量表

| P | X(P) | z | M# | raw C | required deletion | remaining C | deletion fraction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `168` | `3` | `2.666666666667` | `5` | `3` | `2` | `0.6` |
| `17` | `1210` | `3` | `3.166666666667` | `7` | `4` | `3` | `0.571428571` |
| `19` | `3658` | `3` | `2.666666666667` | `11` | `9` | `2` | `0.818181818` |
| `23` | `58` | `3` | `3.566666666667` | `14` | `11` | `3` | `0.785714286` |
| `29` | `5209` | `4` | `3.233333333333` | `20` | `17` | `3` | `0.85` |
| `31` | `60794` | `4` | `4.0` | `21` | `18` | `3` | `0.857142857` |
| `37` | `73916` | `4` | `4.595238095238` | `26` | `22` | `4` | `0.846153846` |
| `41` | `170880` | `4` | `5.041666666667` | `30` | `25` | `5` | `0.833333333` |
| `43` | `162932` | `5` | `4.916666666667` | `24` | `20` | `4` | `0.833333333` |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ExactXRawCapacityObstructionImported` | `true` | `true` | 上一层已证明 raw suffix 容量路线不足。 | ColdRestrictedExactXSupplyDeletionLedger |
| `RequiredDeletionFormulaClosed` | `true` | `true` | 若 raw capacity 为整数 C，严格余量需要删除至少 floor(C-M#)+1 个单位。 | ColdRestrictionDeletionLowerBoundAgainstExactXTable |
| `ExactXDeletionTargetTableClosed` | `true` | `true` | 样本 exact x 的所需 cold 删除量已生成。 | ColdRestrictionDeletionLowerBoundAgainstExactXTable |
| `ColdReturnRoutesImported` | `true` | `true` | 可用删除来源只能是 cold/no-return guard、热/固定回流、共同核无免费循环与 PDEC/SAE。 | ColdSupplySameParameterNumericEnvelope |
| `ColdRestrictedExactXSupplyDeletionLedgerClosed` | `true` | `true` | 删除量目标表闭合，但删除量下界尚未证明。 | ColdRestrictionDeletionLowerBoundAgainstExactXTable |
| `ColdRestrictionDeletionLowerBoundProved` | `false` | `false` | 尚未证明真实 cold 限制至少删除目标表所需单位。 | ColdRestrictionDeletionLowerBoundAgainstExactXTable |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 非持久删除量下界、持久 moving atom 与 DStructure/Rankin 仍未全部闭合。 | ColdRestrictionDeletionLowerBoundAgainstExactXTable AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一步

- 主攻：`ColdRestrictionDeletionLowerBoundAgainstExactXTable`。
- 任务：证明真实 cold 限制、命名回流与无免费共同核循环至少删掉目标表所需容量。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-inverse-alignment-cold-restricted-envelope-return-sync-router.json` | `427de4e97989bc2758b50d69b59ac2d4854fce5454eff1d9c45d40f167550664` |
| `docs/monograph/prime-matrix-inverse-alignment-exact-x-budget-interface-router.json` | `9d8332f7813532faf0efab89112cc12b2ce6b2756b7330fff2471e37c36bc5fe` |
| `docs/monograph/prime-matrix-inverse-alignment-exact-x-runner-obstruction-router.json` | `fddf8fc9faec48154d0c44f1d40cf876516bca159b1d9926ee801078395e8828` |
| `docs/monograph/prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json` | `5be154f20bb3ff27a7c356dc2fc1d9b2a963be039e3c4f94ec2d941a7e47f721` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json` | `c2ef211342a04f992f35f62a595d3c1647663d1a9fde5d1e78ff57c735bf63d6` |
| `experiments/prime_matrix_inverse_alignment_cold_restricted_deletion_target_router.py` | `eba11bbe1b5daa177c6ba56d3225d38e637f1a4ef8ca3482fcb2b473f83ebb20` |
