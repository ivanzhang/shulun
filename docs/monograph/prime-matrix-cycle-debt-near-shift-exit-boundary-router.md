# Prime Matrix cycle-debt near-shift exit-boundary router

**状态：** `near_shift_hits_exit_primes_or_requires_fresh_cover`

对任一正债务 residue，原始 debt 前缀之后紧接着是该行的首个 relief prime。因此任意 1..15 周期的小平移都会让所有 debt>=K 的行在平移词内部撞上 exit prime；而 K>15 到 near limit=16 时，旧前缀已经完全不能提供复用支撑。故 moving 分支不是旧 CRT cover 的轻微滑动；它必须替换部分或全部支撑行，成为 fresh moving cover PDEC 或真正全局 support-motion SAE。

```text
row_column_unconditional_closed=false
previous_hardpoint=SparseReplaySAEOrMovingTransverseCoverPDEC
period_p=5680
near_shift_limit_cycles=16
near_shift_limit_p=90880
positive_cycle_debt_residue_count=27
total_cycle_debt_mass=101
max_cycle_debt=15
tested_nonzero_near_shift_count=16
all_near_shifts_close_old_prefix_reuse=true
shift_1_exit_prime_collision_row_count=27
shift_1_exit_prime_collision_debt_mass=101
shift_max_cycle_debt_exit_prime_collision_row_count=1
shift_max_cycle_debt_exit_prime_collision_debt_mass=15
shift_near_limit_fresh_cover_required_row_count=27
shift_near_limit_fresh_cover_required_debt_mass=101
moving_branch_must_replace_some_or_all_support_rows=true
next_direct_attack_target=FreshMovingCoverPDECOrGlobalSupportMotionSAE
```

## 1. shift audit

| shift K | exit rows | exit debt mass | fresh rows | fresh debt mass | old prefix reusable |
| ---: | ---: | ---: | ---: | ---: | :---: |
| 1 | 27 | 101 | 0 | 0 | false |
| 2 | 18 | 92 | 9 | 9 | false |
| 3 | 12 | 80 | 15 | 21 | false |
| 4 | 9 | 71 | 18 | 30 | false |
| 5 | 7 | 63 | 20 | 38 | false |
| 6 | 6 | 58 | 21 | 43 | false |
| 7 | 5 | 52 | 22 | 49 | false |
| 8 | 4 | 45 | 23 | 56 | false |
| 9 | 3 | 37 | 24 | 64 | false |
| 10 | 2 | 28 | 25 | 73 | false |
| 11 | 2 | 28 | 25 | 73 | false |
| 12 | 2 | 28 | 25 | 73 | false |
| 13 | 2 | 28 | 25 | 73 | false |
| 14 | 1 | 15 | 26 | 86 | false |
| 15 | 1 | 15 | 26 | 86 | false |
| 16 | 0 | 0 | 27 | 101 | false |

## 2. row exit boundary

| residue | debt | first formal P | exit prime cycle | exit prime P | gap=debt*5680 |
| ---: | ---: | ---: | ---: | ---: | :---: |
| 1 | 2 | 10367 | 2 | 21727 | true |
| 2 | 2 | 11007 | 2 | 22367 | true |
| 8 | 4 | 14847 | 4 | 37567 | true |
| 13 | 1 | 12367 | 1 | 18047 | true |
| 15 | 7 | 13647 | 7 | 53407 | true |
| 16 | 3 | 14287 | 3 | 31327 | true |
| 17 | 9 | 14927 | 9 | 66047 | true |
| 19 | 4 | 10527 | 4 | 33247 | true |
| 20 | 6 | 11167 | 6 | 45247 | true |
| 23 | 13 | 13087 | 13 | 86927 | true |
| 24 | 2 | 13727 | 2 | 25087 | true |
| 25 | 1 | 14367 | 1 | 20047 | true |
| 29 | 1 | 11247 | 1 | 16927 | true |
| 41 | 5 | 13247 | 5 | 41647 | true |
| 42 | 2 | 13887 | 2 | 25247 | true |
| 43 | 3 | 14527 | 3 | 31567 | true |
| 47 | 3 | 11407 | 3 | 28447 | true |
| 49 | 1 | 12687 | 1 | 18367 | true |
| 52 | 1 | 14607 | 1 | 20287 | true |
| 54 | 1 | 10207 | 1 | 15887 | true |
| 57 | 1 | 12127 | 1 | 17807 | true |
| 58 | 8 | 12767 | 8 | 58207 | true |
| 60 | 1 | 14047 | 1 | 19727 | true |
| 62 | 2 | 15327 | 2 | 26687 | true |
| 63 | 2 | 10287 | 2 | 21647 | true |
| 64 | 1 | 10927 | 1 | 16607 | true |
| 67 | 15 | 12847 | 15 | 98047 | true |

## 3. 判定

- 每个正债务行的旧 composite prefix 之后立即是 exit prime；平移旧前缀会把这个 prime 拉入词内。
- 对 `K=1`，27 行全部被 exit prime 撕裂；对 `1<=K<=15`，所有 `debt>=K` 的行被撕裂。
- 对 `K=16`，没有旧 composite prefix 可复用，27 行都必须 fresh cover。
- 因此 moving 分支不能靠同一 CRT cover 近程滑动维持；它必须替换支撑行或进入全局 support-motion。
- 本步仍不宣称行/列命题无条件闭合；它把 moving 分支压成 fresh moving cover PDEC/SAE。
- 下一主攻点：`FreshMovingCoverPDECOrGlobalSupportMotionSAE`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-crt-cover-pressure-ledger.json` | `e2731895ab36398581674261c359b074ef71dba80c47601be4992723de15ddd8` |
| `data/prime-matrix-cycle-debt-sparse-replay-barrier-ledger.json` | `7c656a73b8e78d480ae54a8a36f843bf66f8b024a6d3fde6c204774ee6cc213e` |
