# LV 低体积原则：Tail-log4/RKS 的端点吸收抽取

本文把 `docs/bg-rks-block-match.md` 中的 RKS-4 与 `docs/rks-parameter-audit.md` 中的端点低体积块抽取为独立编号引理，供 `docs/rh-ov2-main-layer-capacity-interface.md` 引用。

## 1. 原则陈述

**Lemma LV（低体积原则）。** 设某 dyadic 块的目标主尺度为 `X`，要求误差预算为 `X/log^B X`。若该块的有效支撑大小满足

`Vol_eff <= X/log^{B+C}X`，

且该块只额外产生至多 `log^C X` 的 dyadic、平滑、Fourier 或 divisor-bounded 损失，则平凡估计足以给出

`Contribution <= X/log^B X`。

**证明。** 平凡估计给 `Contribution <= Vol_eff · log^C X`。代入假设即得 `<=X/log^BX`。证毕。

## 2. 与 RKS-4 的匹配

在 `docs/bg-rks-block-match.md` 的 RKS-4 中，低体积/端点块定义为有效支撑低于主项阈值的块。RKS 参数账本给出全部附加损失指数为 `74`，而保守预留为 `128`。因此可取

`C=74`, `B=4`

或在 Tail-log4 内部取更强的 `B=44` 后再降到最终 `B=4`。

这说明 RKS-4 不是新的解析输入；它只是平凡估计加对数损失账本。

## 3. OV-2 中的使用形式

在 OV-2 主层容量接口中，低尾层满足

`n=q_1q_2r`, `q_i~Q`, `r~R`, `Q^2R~X`, `R<log^{A_1}X`。

对固定 `r`，双锚乘积处于薄壳 `q_1q_2~X/r`，且 `q_i~Q~(X/R)^{1/2}`。平凡地先选 `q_1`，则 `q_2` 被乘积薄壳限制在 `O(log^C X)` 个平滑可行位置；因此

`Vol_eff(Q,R) << R·Q·log^C X << X^{1/2}R^{1/2}log^C X`。

若 `R<log^{A_1}X`，则

`Vol_eff(Q,R) << X^{1/2}log^{A_1/2+C}X = o(X/log^B X)`

对任意固定 `B` 成立。故这些低尾层满足 Lemma LV 的假设。

## 4. 结论

**Corollary LV-OV2（OV-2 低尾层吸收）。** OV-2 中所有 `R<log^{A_1}X` 的低尾层，以及由 `Q>X^{1/2}log^{-A_0}X` 导致的近平方边界层，均可由 Lemma LV 吸收，除非质量集中到短窗而触发短簇终端。

**证明。** 低尾层由第 3 节直接满足 LV。近平方边界层由 `Q^2R~X` 推出 `R<log^{2A_0}X`，归入低尾层。若平凡支撑估计失效，只能是局部短窗集中，即短簇终端。证毕。
