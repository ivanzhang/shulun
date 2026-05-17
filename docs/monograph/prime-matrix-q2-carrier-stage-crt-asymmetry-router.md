# Q2 阶载体端点 CRT 不对称路由

**状态：** `q2_carrier_stage_endpoint_inversion_routed_not_global_proof`

把跨越早期零行的相邻素数载体提升到 Q2 阶后，完整 Q2 轮不会复制两个素端点；相反，包含 Q1,Q2 的全轮周期会把端点复制成被自身整除的复合点。因此端点稳定复现分支被直接排除；剩余只能是固定闭覆盖块 ColumnCRT/PDEC、孤立 SAE，或端点/支撑移动后回到 H3-DSB/KLS 与 moving-family 出口。

```text
previous_hardpoint=PeriodLiftCarrierDriftRoutedToPersistentPDECOrSparseSAEOrH3DSBNCBLK;GlobalFinalInputsStillOpen
early_below_square_gap_pcovered_or_square_anchor_escape=true
q2_full_wheel_endpoint_inversion_proved=true
q2_less_wheel_one_sided_endpoint_break_proved=true
all_sample_full_q2_endpoint_prime_replay_impossible=true
all_sample_q2_stage_modulus_exceeds_support_width=true
persistent_q2_carrier_block_routes_to_columncrt_pdec=true
sparse_q2_carrier_block_routes_to_sae=true
moving_endpoint_or_fresh_support_routes_to_h3_dsb=true
row_column_unconditional_closed=false
next_direct_attack_target=Q2StageEndpointInversionRoutedToColumnCRTPDECOrSparseSAEOrMovingEndpointH3DSB;GlobalFinalInputsStillOpen
```

## 1. 早期载体的 Q2 阶边界

设早期第 `k` 行

\[
I_{P,k}=[(k-1)P+1,kP],\qquad 1<k<P,
\]

没有素数。令 `Q1<Q2` 为跨越该行的左右相邻素数。若 `Q2<P^2`，则开间隙
`(Q1,Q2)` 内每个数都是合数且小于 `P^2`，所以其最小素因子小于 `P`。
因此开间隙本身已经是 `P` 阶小因子覆盖块；若 `Q2>=P^2`，则该分支转入平方锚/对角端点问题。

## 2. 全 Q2 轮的端点反转

令

\[
M_{\le Q2}=\prod_{\ell\le Q2,\ \ell\ prime}\ell.
\]

因为 `Q1|M_{<=Q2}` 且 `Q2|M_{<=Q2}`，对任意 `t>=1` 有

\[
Q1+tM_{\le Q2}\equiv0\pmod{Q1},\qquad
Q2+tM_{\le Q2}\equiv0\pmod{Q2}.
\]

所以完整 Q2 阶周期不能复制“两个端点仍为素数”的真实链。它复制的是闭覆盖块的零类端点，而不是相邻素数端点。

若只用 `M_{<Q2}`，左端 `Q1` 已被自身零类固定杀掉；右端 `Q2` 未被周期整除，
但其素性也不由 CRT 强制。这给出单侧断裂，而不是全局矛盾。

## 3. 样本读数

| P | x0 | interval | Q1 | Q2 | gap | Q2 layers from P | log10 M_{<=Q2} | log M-support | full endpoint replay |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 13 | 168 | `[2185, 2197]` | 2179 | 2203 | 24 | 323 | 925.482456 | 2127.783232 | `false` |
| 17 | 1210 | `[20571, 20587]` | 20563 | 20593 | 30 | 2316 | 8859.768552 | 20396.937009 | `false` |
| 19 | 3658 | `[69503, 69521]` | 69499 | 69539 | 40 | 6896 | 30048.185933 | 69184.791428 | `false` |
| 23 | 58 | `[1335, 1357]` | 1327 | 1361 | 34 | 210 | 568.661889 | 1305.83704 | `false` |

这些样本不是早期零行反例；它们只用于验证同一端点机制。共同读数是：Q2 阶模数远大于载体支撑，
且完整 Q2 轮中的端点素性复现全部失败。

## 4. 三分流

| behavior after Q2 stage | route | reason |
| --- | --- | --- |
| 要求覆盖块和两个素端点在全 Q2 轮中同相复现 | `impossible` | `Q1,Q2` 端点复制后分别被自身整除。 |
| 放弃素端点，只让同一闭覆盖块持久复现 | `ColumnCRT/PDEC` | 固定零类端点和固定覆盖块成为同一 formal unit。 |
| 只出现有限次或孤立窗口 | `SAE` | 不能支撑无限反例链。 |
| 移动端点、移动素层或改变支撑以避开端点反转 | `moving-family/H3-DSB/KLS` | 回到端点漂移、尾补洞或短窗 dispersion 硬核。 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| EarlyCarrierOpenGapAlreadyPCoveredBelowSquare | `true` | `true` | 若早期零行 1<k<P 的右端载体 Q2 仍满足 Q2<P^2，则相邻素数开间隙 (Q1,Q2) 内每个合数都有小于 P 的素因子；否则进入平方锚逃逸。 | closed with square-anchor escape |
| Q2FullWheelEndpointInversion | `true` | `true` | 在包含 Q1,Q2 的全 Q2 阶轮 M_{<=Q2} 下，Q1+tM_{<=Q2} 与 Q2+tM_{<=Q2} 对 t>=1 分别被 Q1,Q2 整除，素端点被反转为复合端点。 | closed |
| Q2LessWheelOneSidedEndpointBreak | `true` | `true` | 若只用 M_{<Q2}，左端 Q1 已被自身零类固定杀掉，而右端 Q2 的素性仍不由 CRT 强制。 | closed |
| Q2StageModulusExceedsCarrierSupport | `true` | `true` | Q2 阶轮模数大于闭载体支撑宽度；同一固定相位的非零复现不能在本地支撑内连续滑动。 | closed as local capacity barrier |
| EndpointPrimeReplayContradictionUnderFullQ2Stage | `true` | `true` | 若要求全 Q2 阶周期同时复现小因子覆盖和两个素端点，则与端点自身整除性直接矛盾。 | closed for full-stage endpoint-stable replay |
| PersistentQ2CarrierBlockRoutesToColumnCRTPDEC | `true` | `true` | 若不要求素端点复现，而只让同一闭覆盖块持久复现，则它正是固定零类 ColumnCRT/PDEC 对象。 | closed as router |
| SparseQ2CarrierBlockRoutesToSAE | `true` | `true` | 若 Q2 阶闭覆盖块只孤立出现，则只能登记为 SAE 单窗原子。 | closed as router |
| MovingEndpointOrFreshSupportRoutesToH3DSB | `true` | `true` | 若为避开端点反转而移动端点、移动素层或改变支撑，则回到 moving-family/H3-DSB/KLS 分支。 | H3-DSB-NCBLK or named moving-family PDEC/SAE |
| GlobalRowColumnUnconditionalClosureReached | `false` | `false` | 本步排除的是 Q2 阶端点稳定复现跳步；仍未排斥所有 ColumnCRT/PDEC、SAE 与 moving-family 出口。 | Q2StageEndpointInversionRoutedToColumnCRTPDECOrSparseSAEOrMovingEndpointH3DSB;GlobalFinalInputsStillOpen |

## 6. 最新剩余

```text
Q2StageEndpointInversionRoutedToColumnCRTPDECOrSparseSAEOrMovingEndpointH3DSB;GlobalFinalInputsStillOpen
```

本证书关闭的是 `Q2` 阶端点稳定复现这一最窄跳步；它没有排斥全部 `ColumnCRT/PDEC`、`SAE` 与 moving-family 出口，
因此不构成行/列命题的全局无条件证明。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-early-zero-gap-crt-asymmetry-router.json` | `9f10be0a0445eef5185d4e9d03dab884b330a0ae06b9ff9c7a0ffb910086a804` |
| `docs/monograph/prime-matrix-early-zero-period-lift-carrier-drift-router.json` | `937d22f5dc0bbd7d7c0e6caf3cf7740ed4f0e0f5ca5cc28d6edcf8a42222af2c` |
| `docs/monograph/prime-matrix-zero-row-full-crt-diagonal-minrep.md` | `8fed996d49bd3da39370eb919cac7601759d12152d44d2a39854f3fd236515ab` |
| `docs/monograph/prime-matrix-prime-square-pm-layered-wheel-alignment-router.md` | `d9ebce17d5a9aa5a09722adbfff264622e87429f7deade6d80c399b81c732c58` |
