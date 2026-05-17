# Prime Matrix cycle-debt fresh-layer 本地投影碰撞路由器

**状态：** `registered_fresh_layer_local_projection_collision_excluded_remote_columncrt_open`

registered branch replay 的 fresh-layer 本地投影碰撞已排除：全部 fresh prime sample 与本地周期 5680 互素，且首个 fresh prime 已大于对应支撑宽度和审计槽数；因此局部窗口内 a+j*5680 mod ell 是单射。剩余 fresh-layer PDEC 只能是支撑运动逃逸、远程 ColumnCRT/PDEC 或未登记 moving family。

```text
previous_hardpoint=FreshLayerPDECColumnCRTExclusion
period_p=5680
registered_block_count=6
all_sample_fresh_primes_coprime_to_period_p=true
all_first_fresh_primes_exceed_support_width=true
all_first_fresh_primes_exceed_audit_slots=true
all_registered_samples_injective_on_local_windows=true
minimum_first_fresh_minus_support_width=178
minimum_first_fresh_minus_audit_slots=178
local_fresh_layer_projection_collision_excluded=true
fresh_layer_pdec_fully_excluded=false
row_column_unconditional_closed=false
next_direct_attack_target=FreshLayerSupportMotionEscapeOrRemoteColumnCRTPDECExclusion
```

## 1. 单射引理

设本地周期步长为 `M=5680`，fresh prime 为 `ell`。若 `gcd(M,ell)=1` 且局部窗口长度 `W<ell`，则槽坐标 `j -> a+jM (mod ell)` 在 `0<=j<W` 上单射。否则若两个槽同余，则 `ell | (j1-j2)M`，由互素性得 `ell | (j1-j2)`；但 `|j1-j2|<W<ell`，只能 `j1=j2`。

## 2. block 读数

| block | support | audit slots | first fresh | first-support | first-audit | sample injective |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `both_branches_plus_k14_entry_postwall` | 151 | 190 | 88609 | 88458 | 88419 | `true` |
| `k13_branch_exclusive` | 73 | 73 | 251 | 178 | 178 | `true` |
| `k14_branch_exclusive` | 70 | 70 | 293 | 223 | 223 | `true` |
| `k14_branch_plus_entry` | 78 | 78 | 88609 | 88531 | 88531 | `true` |
| `k14_branch_plus_entry_plus_assigned` | 78 | 107 | 88609 | 88531 | 88502 | `true` |
| `k14_branch_plus_entry_plus_postwall` | 78 | 117 | 88609 | 88531 | 88492 | `true` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FreshLayerPDECImportedAsOnlyBranchReplayExit | `true` | `true` | 上一同步已移除 tail-sieve 出口，branch-replay 子分支只剩 fresh-layer PDEC/ColumnCRT。 | FreshLayerPDECColumnCRTExclusion |
| FreshPrimesCoprimeToLocalPeriod | `true` | `true` | 全部登记 fresh prime sample 均与本地周期 5680 互素，因此局部槽坐标按周期步长在模 fresh prime 上可逆。 | closed for registered samples |
| FreshPrimeExceedsLocalSupport | `true` | `true` | 每个登记 block 的首个 fresh prime 已大于对应 primitive support 宽度和审计槽数；样本 fresh primes 更大。 | closed for registered blocks |
| LocalFreshLayerProjectionCollisionExcluded | `true` | `true` | 若槽坐标为 a+jM，gcd(M,ell)=1 且窗口长度小于 ell，则 j->a+jM mod ell 在该窗口内单射，不能产生本地投影碰撞。 | closed for registered support windows |
| SupportMotionOrRemoteColumnCRTStillOpen | `false` | `false` | fresh-layer PDEC 若仍持续，只能来自支撑运动逃逸、远程 P-space ColumnCRT 复现或未登记的新 block family。 | FreshLayerSupportMotionEscapeOrRemoteColumnCRTPDECExclusion |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只排除 registered fresh layers 的本地投影碰撞，不排除远程 ColumnCRT/PDEC 或新 moving-family。 | FreshLayerSupportMotionEscapeOrRemoteColumnCRTPDECExclusion |

## 4. 剩余接口

```text
FreshLayerSupportMotionEscapeOrRemoteColumnCRTPDECExclusion
```

本证书只排除 registered blocks 的本地 fresh-layer 投影碰撞。若 fresh-layer PDEC 仍持续，必须表现为支撑运动逃逸、远程 P-space ColumnCRT 复现或未登记 moving family。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-branch-replay-support-gap-ledger.json` | `5c2b502fbc787652b7d07f25d4886746cb64500f280b0128d131869f6b769105` |
| `data/prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-ledger.json` | `bfc13d727a480ee6bb358d5f01a826b5e14b0a2bdef7dd8961c4f58c5ba116d9` |
| `data/prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-ledger.json` | `99d31e9d86f0802049d5640413f3913f393f76bf62dcccab82f844ce2ff91cb4` |
