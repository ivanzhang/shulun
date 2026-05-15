# Prime Matrix square-phase low-alpha z=61 square residue phase lock

**状态：** `z61_square_window_reduced_to_crt_phase_lock_open`

平方窗口进一步压成有限 CRT 相位锁：`M=57684=2^2*3*11*19*23`，`delta=527=17*31`，`p^2≡-527 (mod M)` 在每个素幂因子上只有两个根，总共 `32` 个 CRT 根相位。样本选中 `p mod M=26951`，并且 `floor(p/M)=span=3`，所以 `p=3M+26951`。下一步硬点变为全局 CRT 相位锁容量界，或登记 CRTPhase-PDEC。

```text
square_residue_phase_lock_group_count=1
all_square_residue_phase_locks_closed=true
square_residue_phase_lock_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. CRT 相位锁

| p | M | delta | quotient | span | residue | root count | density | closed |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 200003 | 57684 | 527 | 3 | 3 | 26951 | 32 | 0.000555 | true |

## 2. 素幂根

| prime power | roots | selected | valid |
| ---: | --- | ---: | --- |
| 4 | `[1, 3]` | 3 | true |
| 3 | `[1, 2]` | 2 | true |
| 11 | `[1, 10]` | 1 | true |
| 19 | `[9, 10]` | 9 | true |
| 23 | `[5, 18]` | 18 | true |

## 3. 自足小引理

平方窗口给出 `p^2≡-delta (mod M)`。若 `M` 的素幂分解固定，则合法 `p mod M` 必须落入各素幂根集的 CRT 组合。同时端点窗口要求 `floor(p/M)=span`，于是 `p=span*M+r`。因此该层失败对象不再是自由素数 `p`，而是少数 CRT 根相位中的素数。

## 4. 证明边界

- 已闭合：样本平方窗口等价于一个具体 CRT 根相位与商锁定。
- 未闭合：全局 CRT 相位锁容量界，或 CRTPhase-PDEC 排斥。
- 下一目标：`SquareResiduePhaseLockGlobalBoundOrCRTPhasePDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json` | `26ed4354b18ce54dc2ea66ce943e628fc02f80cacee97084cc3331a15cd17b83` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_square_residue_phase_lock_router.py` | `ca9aac392aba2576dbc3568cba3a06f629683307b8191e901901ae3ed6680616` |
