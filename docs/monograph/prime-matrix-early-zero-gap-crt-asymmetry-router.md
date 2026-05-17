# 早期零行相邻素数载体与 CRT 非对称路由

**状态：** `early_zero_gap_carrier_asymmetry_routed_not_global_proof`

早期零行确实会强制一个跨越该行的相邻素数大间隙载体；但 CRT 周期只复制小素因子覆盖，不复制素数端点。因此该非对称提示本身不是完整矛盾，而是一个路由器：持久相位进入 PDEC/ColumnCRT，孤立相位进入 SAE，非周期素端点回到 H3-DSB/KLS 的 NC-BLK 或外部 DI/BFI 最终硬核。

```text
previous_hardpoint=CycleDebtBranchReplayCurrentMaterializedFrontierZeroWithFutureSchemaFirewall;GlobalFinalInputsStillOpen
early_zero_gap_lemma_proved=true
crt_gap_asymmetry_standalone_contradiction_proved=false
persistent_phase_routes_to_pdec_columncrt=true
sparse_phase_routes_to_sae=true
nonperiodic_endpoint_routes_to_h3_dsb_kls=true
nc_blk_or_external_dibfi_closed=false
row_column_unconditional_closed=false
next_direct_attack_target=EarlyZeroGapCarrierAsymmetryRoutedToH3DSBNCBLKOrExternalDIBFI;GlobalFinalInputsStillOpen
```

## 1. 相邻素数载体引理

设 `P` 为奇素数，第 `k` 行为

\[
I_{P,k}=[(k-1)P+1,kP].
\]

若 `I_{P,k}` 中没有素数，令 `a` 为小于左端点的最大素数，`b` 为大于右端点的最小素数。则 `a,b` 之间没有其它素数，所以它们是相邻素数，且

\[
b-a \ge (kP+1)-((k-1)P)=P+1>P.
\]

这严格化了“早期零行强制跨行相邻素数大间隙”的提示。

## 2. CRT 非对称的精确边界

小素因子覆盖集合只依赖 `mod M_P`，因此零行覆盖图案可以按 CRT 周期重复。但相邻素数端点不是小因子覆盖对象；`a+M_P` 与 `b+M_P` 没有理由仍为素数。这就是非对称的核心：周期复制的是反例覆盖链，不是素数真实链。

因此单个 gap carrier 不能直接推出矛盾。要产生全局结构矛盾，必须证明这些 carrier 相位在无限链中持久复现，或证明非复现时无法支付尾补洞需求。

## 3. 三分流

| case | route | meaning |
| --- | --- | --- |
| 持久同相 gap carrier | `PDEC/ColumnCRT` | 固定端点相位或列位移重复，成为 CRT/Fourier 缺陷。 |
| 孤立 gap carrier | `SAE` | 单窗逃逸，不构成无限反例结构。 |
| 素端点不能周期化但覆盖仍持续 | `H3-DSB/KLS -> NC-BLK or external DI/BFI` | 回到六轮尾补洞与短窗口 Kloosterman/dispersion 硬核。 |

## 4. 有限核查

- `max_p`: `5000`。
- `prime_layers_checked`: `668`。
- `row_windows_checked`: `1547466`。
- `early_zero_rows_found`: `0`。
- `min_prime_count_in_checked_rows`: `1`。
- `max_adjacent_prime_gap_below_max_p_square`: `210`。

最小素数数样本：

| P | row | interval | prime_count | primes_in_row |
| ---: | ---: | --- | ---: | --- |
| 3 | 2 | `[4, 6]` | 1 | `[5]` |
| 3 | 3 | `[7, 9]` | 1 | `[7]` |
| 5 | 2 | `[6, 10]` | 1 | `[7]` |
| 5 | 5 | `[21, 25]` | 1 | `[23]` |
| 7 | 4 | `[22, 28]` | 1 | `[23]` |
| 11 | 11 | `[111, 121]` | 1 | `[113]` |
| 13 | 10 | `[118, 130]` | 1 | `[127]` |
| 17 | 13 | `[205, 221]` | 1 | `[211]` |
| 19 | 16 | `[286, 304]` | 1 | `[293]` |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| EarlyZeroToStraddlingAdjacentPrimeGap | `true` | `true` | 若第 k 行 [(k-1)P+1,kP] 无素数，则其左右最近素数构成跨越该行的相邻素数对，间隙严格大于 P。 | closed |
| GapCarrierBelowSquareForEarlyRows | `true` | `true` | 若 1<k<P，则被跨越的行窗口完全位于 P^2 之前；若右侧素数越过 P^2，则反而进入更强的平方锚/对角分支。 | closed with square-anchor escape |
| CRTPeriodicityOnlyForSmallFactorCover | `true` | `true` | 小素因子覆盖按 M_P 周期重复，但相邻素数端点本身不是 CRT 周期对象。 | closed |
| StandaloneGapAsymmetryContradiction | `false` | `false` | 单个相邻素数大间隙只重述平方根长度短区间素数问题，不能单独推出全局矛盾。 | routes to H3/DSB or named exits |
| PersistentCarrierPhaseRoutesToPDECColumnCRT | `true` | `true` | 若相邻素数载体的端点相位在 CRT 周期中持久复现，则形成固定相位/列位移缺陷，进入 PDEC/ColumnCRT。 | closed as router |
| SparseCarrierPhaseRoutesToSAE | `true` | `true` | 若载体相位只孤立出现，则它是单窗逃逸而非无限结构，进入 SAE。 | closed as router |
| NonperiodicPrimeEndpointRoutesToH3DSBKLS | `true` | `true` | 若端点素性不能周期化，只能回到 H3 六轮尾补洞、DSB/KLS 与 NC-BLK 或外部 DI/BFI 分支。 | H3-DSB-NCBLK-or-external-DIBFI |
| NCBLKOrExternalDIBFIClosed | `false` | `false` | 当前仓库最新完全自足硬核仍是 NC-BLK；若不内证，只能调用外部 DI/BFI dispersion。 | NC-BLK or external DI/BFI |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步把用户的相邻素数/CRT 非对称提示接入现有最终硬核，不关闭全局行/列命题。 | EarlyZeroGapCarrierAsymmetryRoutedToH3DSBNCBLKOrExternalDIBFI;GlobalFinalInputsStillOpen |

## 6. 最新剩余

```text
EarlyZeroGapCarrierAsymmetryRoutedToH3DSBNCBLKOrExternalDIBFI;GlobalFinalInputsStillOpen
```

本证书不关闭全局行/列命题；它只把“早期零行相邻素数载体”提示严格接入现有最终硬核，并排除把单个 CRT 非对称现象误当作完整证明的跳步。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-cycle-debt-branch-replay-current-frontier-zero-router.json` | `fb6ba535d8c13abd69c7238539049a64161b6e1e19595fc403a0394b7a56029a` |
| `docs/monograph/prime-matrix-h3-unified-defect-criterion.md` | `a63a4826397ea9089df238960ed69f677a98d54446d6e6a8b51bab281ba05088` |
| `docs/monograph/prime-matrix-h3-dsb-hlc-blk-energy-core-obstruction.md` | `c424b1aed6378b1e476c86e238dfe7e02cf59f983efffcb6a8b9b7bf18715ca7` |
