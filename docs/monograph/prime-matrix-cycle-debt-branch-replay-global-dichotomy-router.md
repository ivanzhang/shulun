# Prime Matrix cycle-debt branch replay global dichotomy router

**状态：** `global_registered_replay_reduced_to_columncrt_pdec_or_finite_atom_check`

本步把孤立原子从全局反例链中剥离：登记的终端阻断包只有有限个。若某个登记包在全局反例链中无限复现，则周期 replay lemma 立即把它提升为 P 坐标中的固定 ColumnCRT 类，最小 P-space 模数约 10^36.336；若没有登记包无限复现，则这些登记原子只是有限项，不能作为全局结构逃逸，只能进入有限基例检查。若阻断包改变，则回流 PDEC/SAE 或新命名 router。

```text
row_column_unconditional_closed=false
previous_hardpoint=BranchReplayColumnCRTPDECExclusionOrIsolatedTerminalAtomAbsorption
period_p=5680
registered_replay_block_count=6
minimum_cycle_replay_modulus_log10=32.582
minimum_p_space_columncrt_modulus_log10=36.337
maximum_p_space_columncrt_modulus_log10=103.103
persistent_registered_replay_routes_to_columncrt_pdec=true
isolated_atoms_cannot_form_infinite_registered_family=true
finite_atom_base_check_required=true
next_direct_attack_target=BranchReplayColumnCRTPDECExclusionOrFiniteAtomBaseCheck
```

## 1. global dichotomy

- 登记的终端 replay block 是有限集合。
- 若某个登记 block 在全局反例链中无限复现，则周期坐标 `T == 0 mod lcm(B)` 提升为 `P` 坐标中的固定 `period_p*lcm(B)` ColumnCRT 类。
- 若没有登记 block 无限复现，则登记原子只剩有限项；它们不能构成全局结构逃逸，必须进入有限基例检查。
- 若后续阻断包改变，则不属于同一 replay block，回流 `PDEC/SAE` 或生成新的命名 router。

## 2. P-space ColumnCRT blocks

| block | support width | audit slots | log10 cycle replay | log10 P-space modulus |
| --- | ---: | ---: | ---: | ---: |
| `k13_branch_exclusive` | 73 | 73 | 36.678 | 40.432 |
| `k14_branch_exclusive` | 70 | 70 | 32.582 | 36.337 |
| `k14_branch_plus_entry` | 78 | 78 | 72.064 | 75.819 |
| `k14_branch_plus_entry_plus_assigned` | 78 | 107 | 76.351 | 80.105 |
| `k14_branch_plus_entry_plus_postwall` | 78 | 117 | 85.024 | 88.778 |
| `both_branches_plus_k14_entry_postwall` | 151 | 190 | 99.349 | 103.103 |

## 3. 判定

- 本步不排斥远程 ColumnCRT/PDEC；它证明远程无限复现必须被登记为该类结构缺陷。
- 孤立有限原子不再是全局结构出口，但仍需要有限基例检查；因此不能宣称行/列命题已经无条件闭合。
- 下一主攻点：`BranchReplayColumnCRTPDECExclusionOrFiniteAtomBaseCheck`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-branch-replay-support-gap-ledger.json` | `5c2b502fbc787652b7d07f25d4886746cb64500f280b0128d131869f6b769105` |
