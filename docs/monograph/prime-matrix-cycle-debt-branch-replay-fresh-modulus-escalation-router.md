# Prime Matrix cycle-debt branch replay fresh-modulus escalation router

**状态：** `finite_columncrt_replay_class_nonterminal_fresh_modulus_escalation_registered`

有限 ColumnCRT replay 类不是全局终端结构。当前有限原子分支已关闭后，剩余持久 replay 若固定在某个登记模数上，每一个未登记的新素数层都会给出与旧模数互素的新 CRT 坐标；因此无限反例链不能在有限模数上稳定，只能不断扩模、触发 PDEC/ColumnCRT 缺陷，或转入尾段筛稳定矛盾。

```text
row_column_unconditional_closed=false
previous_hardpoint=BranchReplayColumnCRTPDECExclusion
finite_atom_branch_closed_for_registered_atoms=true
registered_replay_block_count=6
fresh_prime_sample_count_per_block=8
all_registered_blocks_have_coprime_fresh_layers=true
minimum_first_fresh_log10_gain=2.400
minimum_sample_log10_gain=19.435
finite_crt_terminal_description_excluded=true
persistent_family_requires_unbounded_modulus_or_pdec=true
next_direct_attack_target=UnboundedFreshModulusEscalationPDECOrTailSieveStabilityContradiction
```

## 1. fresh layer lemma

固定有限 CRT replay 类的模数记为 `Q`。任意新素数 `ell` 若不整除 `Q`，则 `ell` 是与旧周期互素的新 CRT 坐标。当 `ell` 进入后续筛层时，持久反例链不能只靠旧的 `mod Q` 信息决定 `ell` 层；它必须扩模、触发 PDEC/ColumnCRT 缺陷，或被尾段筛稳定估计吸收。

## 2. registered blocks

| block | factors | max factor | first fresh primes | old log10 lcm | +first gain | +sample gain |
| --- | ---: | ---: | --- | ---: | ---: | ---: |
| `k13_branch_exclusive` | 22 | 241 | `[251, 257, 263, 269, 271, 277, 281, 283]` | 36.678 | 2.400 | 19.435 |
| `k14_branch_exclusive` | 20 | 283 | `[293, 307, 311, 313, 317, 331, 337, 347]` | 32.582 | 2.467 | 20.031 |
| `k14_branch_plus_entry` | 28 | 88607 | `[88609, 88643, 88651, 88657, 88661, 88663, 88667, 88681]` | 72.064 | 4.947 | 39.582 |
| `k14_branch_plus_entry_plus_assigned` | 30 | 88607 | `[88609, 88643, 88651, 88657, 88661, 88663, 88667, 88681]` | 76.351 | 4.947 | 39.582 |
| `k14_branch_plus_entry_plus_postwall` | 34 | 88607 | `[88609, 88643, 88651, 88657, 88661, 88663, 88667, 88681]` | 85.024 | 4.947 | 39.582 |
| `both_branches_plus_k14_entry_postwall` | 41 | 88607 | `[88609, 88643, 88651, 88657, 88661, 88663, 88667, 88681]` | 99.349 | 4.947 | 39.582 |

## 3. 判定

- 当前 finite atom 分支已经由 post-100000 exact runner 对登记对象关闭。
- 任一登记 replay block 仍只是有限 CRT 类；新素数层必然继续给出互素 CRT 坐标。
- 因此有限 CRT 类不能作为全局终端稳定结构；持久族必须走无界扩模/PDEC，或转入尾段筛稳定矛盾。
- 本步仍不宣称行/列命题闭合；它把最后接口从固定 ColumnCRT 类排斥推进到无界 fresh-modulus escalation。
- 下一主攻点：`UnboundedFreshModulusEscalationPDECOrTailSieveStabilityContradiction`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-coupled-branch-entry-wall-ledger.json` | `afb79d743dda71833cb0dd36a922b5e7ba43bc563f9076e1ff61a5067a6fcef4` |
| `data/prime-matrix-cycle-debt-post100000-tail-atom-exact-ledger.json` | `97b0a494818031721eb7076903f70ede95727b387828197def9d14efeb9a50e9` |
