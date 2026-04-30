# BG/RKS 分区逐块匹配附录

本附录把 Tail-log4 中 RKS/BG 输入按 dyadic Type I/II 块逐项匹配到外部定理 `EXT-KL`、`EXT-BG`、`EXT-Vaughan`。它补强 `docs/rks-bridge-partition.md` 与 `docs/rks-parameter-audit.md` 的最终审稿接口。

## 1. 块参数

Vaughan 分解后，每个 dyadic 块写作

`S(M,N)=Σ_{m~M}Σ_{n~N} a_m b_n e_P(c m^{-1}n^{-1})`, `MN≈P`,

其中系数满足 divisor-bounded 条件，所有 dyadic、Vaughan、矩形变差与除数损失进入 RKS 参数账本。

## 2. 四类覆盖

| 块类型 | 参数范围 | 使用定理 | 输出 |
| --- | --- | --- | --- |
| RKS-1 短侧 Weil | `min(M,N)<=P^{1/18}` | `EXT-KL` 完成和逐短变量求和 | `<=P/log^{44+C}P` |
| RKS-2 双线性 BG | `P^{1/18}<min(M,N)<=P^{7/12-ε}` 且长侧足够 | `EXT-BG` 双线性倒数 Kloosterman | 固定对数节省 |
| RKS-3 多线性 BG | 平衡区或可再分裂区 | `EXT-BG` 多线性 `Kloost 1/2` | 固定对数节省 |
| RKS-4 低体积/端点 | 总体积或有效支撑低于主项阈值 | 平凡估计 + Tail-log4 余量 | 可吸收 |

## 3. 短侧 Weil 块

**Lemma RKS1。** 若 `M<=P^{1/18}`，则

`|S(M,N)| <= M P^{1/2} log^C P <= P^{5/9}log^CP`。

因此对充分大 `P`，`|S(M,N)|<=P/log^{44+C_0}P`。

**证明。** 固定短变量 `m`，长变量和是不完全 Kloosterman 和，由 `EXT-KL` 给 `P^{1/2}log^CP`。对 `M` 个短变量求和得第一式。`M<=P^{1/18}` 给 `P^{5/9}`。幂节省 `P^{4/9}` 吸收任意固定对数幂。证毕。

## 4. BG 双线性块

**Lemma RKS2。** 在 RKS-2 参数范围内，`EXT-BG` 的双线性倒数 Kloosterman 定理适用，给出

`|S(M,N)| <= MN/log^{B}P`

其中 `B` 可取大于 RKS 账本所需的固定值。

**证明。** RKS-2 正是 `docs/rks-bridge-partition.md` 中 BG 双线性覆盖区：短侧超过 `P^{1/18}`，长侧在 `MN≈P` 下满足 BG 的不平衡双线性阈值。系数由 Vaughan 分解产生并满足 divisor-bounded 条件；该损失已在 `C_vaughan_blocks`、`C_divisor_coeff` 和 `C_rect_variation` 中计入。调用 `EXT-BG` 得结论。证毕。

## 5. BG 多线性块

**Lemma RKS3。** 对平衡区或可多线性分裂区，`EXT-BG` 多线性倒数 Kloosterman 定理给出固定节省，且损失被 `K_sieve_log_saving=128` 吸收。

**证明。** 平衡区可按 Vaughan/Heath-Brown 型分裂产生三个或更多变量，使变量乘积超过 BG 多线性阈值。`EXT-BG` 给固定幂节省，强于任意固定对数节省。分裂产生的 dyadic 与 divisor-bounded 损失由 RKS 参数账本计入。证毕。

## 6. 端点低体积块

**Lemma RKS4。** 若块体积或有效支撑低于主项阈值，则平凡估计给出的贡献被 Tail-log4 误差预算吸收。

**证明。** 平凡估计为有效支撑大小。端点低体积定义即该大小 `<=P/log^{44+C}P`；对所有 dyadic 块求和只产生 RKS 账本中的固定对数损失。证毕。

## 7. RKS 参数结论

四类块覆盖所有 Vaughan Type I/II dyadic 区域。总对数损失由 `docs/rks-parameter-audit.md` 给出为 `74`，严格小于 `K_sieve_log_saving=128`。因此 Tail-log4 所需 RKS-log 输入完成逐块匹配。
