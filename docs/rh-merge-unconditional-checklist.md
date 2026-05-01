# RH 合并稿无条件化判据勾销表

本文是 `docs/rh-merged-proof-draft-v1.md` 的审稿工程清单。目标不是宣布 RH 已证，而是把“合并稿条件版”中每一个条件接口转化为可逐项勾销的证明义务。

## 1. 判据总表

| ID | 接口 | 当前证据位置 | 无条件化要求 | 状态 |
|---|---|---|---|---|
| C0 | 全局符号、尺度、权重一致 | `docs/rh-global-normalization-maintext-closure.md` | 合并入主稿第 1 节，消除反向常数依赖 | 待内联 |
| C1 | PC1 Landau--Ingham 振荡 | `docs/rh-c1-c10-c11-final-reference-and-submission-closure.md` | 有限边界已文内；一般情形归 `EXT-PC1-LI` 标准引用 | 引用层闭合，待 BibTeX |
| C2 | PC2 CRT 零频基线 | `docs/rh-pc2-crt-baseline-maintext-appendix.md` | 逐行证明 `C_z-C_z^0=o(Δ)` 且说明边界项被 `X^{β-o(1)}` 吸收 | 待内联 |
| C3 | 覆盖场方程 | `docs/rh-c3-covering-field-definition-closure.md` | 已发现原 `ACC-O+Gap` 写法逐点恒等式风险；改为 `ACC+Hole` 一层划分与 `OV` 二层事件 | 已修正，待内联 |
| C4 | 过疏 PC3/OV2 | `docs/rh-c4-sparse-pc3-ov2-inline-proof.md` | C4.1--C4.4 已内联；非共振引用由 C10 闭合 | 已内联 |
| C5 | 过密 Dual/DGap | `docs/rh-c5-dgap-inline-proof-chain.md` | Lemma C5.1--C5.4 已定理化；C6/C9 已内联，C2/C10 已登记 | 内部已闭合 |
| C6 | 内部终端 `A/PI/FCT/SC` | `docs/rh-c6-internal-terminal-inline-proof.md` | C6.1--C6.4 已内联为统一无循环定理；外部出口由 C7/C10 登记 | 已内联 |
| C7 | 外部事件 `LV/LSMP/CE/DSO/NRC` | LV/LSMP/CE、NRC、PI/DSO 主文链 | 每个失败出口必须回到已编号终端，不能产生新假设 | 待出口核验 |
| C8 | `CapacityFail` | `docs/rh-c8-capacityfail-upgrade-audit.md` | 自由黑箱已排除；C1/C10 引用层已闭合；剩余为 C11 单篇 LaTeX/PDF 审稿工程复核 | 已绑定，待 C11 复核 |
| C9 | Fourier/Vaaler 尾项 | `docs/rh-c9-fourier-vaaler-tail-inline-proof.md` | C9.1--C9.4 已内联；`EXT-Vaaler` 来源由 C10 闭合 | 已内联 |
| C10 | `EXT-*` 外部定理 | `docs/rh-c1-c10-c11-final-reference-and-submission-closure.md` | 已列正式来源与使用边界；待 LaTeX/BibTeX 落地 | 引用层闭合，待工程 |
| C11 | LaTeX 审稿工程 | `paper/rh-proof/C11-REVIEW.md` | 单篇 LaTeX 与 BibTeX 已生成；本机缺 TeX，PDF 编译待有 TeX 环境执行 | 源稿已生成，PDF 待编译 |

## 2. 当前最小闭合割集

当前阻止“无条件证明稿”口径的最小割集为：

`{C11-PDF}`。

其中 C2、C7 的内容仍需在 C11 单篇主稿中内联编号；C10 已给出外部来源与使用边界。

## 3. 优先顺序

1. C3 已完成定义化修正；最终主稿需内联 `ACC+Hole` 与 `OV` 二层账本。
2. C8 已从自由黑箱降级为依赖型义务；C4/C5/C6/C9 已处理，C10 引用层已闭合。
3. C1/C10 已并入最终引用闭合包；C11 已生成单篇 LaTeX/BibTeX 源稿；下一步在 TeX 环境执行 PDF 编译与逐行审稿。
4. 执行 C11-PDF：在 TeX 环境编译 PDF，完成 undefined references、符号表、BibTeX 与逐行审稿。

## 4. 严格口径

在 C0--C11 全部勾销前，只能称为“RH 反例矛盾场合并证明稿/条件闭合稿”。若任一核心容量接口无法逐行证明，则必须降级为条件命题，不能改写为 RH 无条件证明。

## 5. Global-Exit-Exclusion 核心硬点

顶刊审查后，当前真正剩余不是新增结构分支，而是 `docs/rh-global-exit-exclusion-target.md` 中的全局出口排斥定理。必须证明 GEE-0 负担分配和九个出口上界 `GEE-A/PI/FCT/SC/LV/LSMP/CE/DSO/NRC`，才能把“无自由逃逸通道”升级为真正矛盾 `c_0Δ<=o(Δ)`。

## 6. GEE-0 负担分配推进

新增 `docs/rh-gee0-load-distribution.md`。该文定义统一 Chebyshev 权、异常原子集合、路由映射和 `Load(E;X)`，并证明在 PC1/PC2/C3/C4/C5/C9 成立且路由有限重叠时，`Σ_E Load(E;X)>=X^{β-o(1)}`。剩余审稿义务为 PC2 边界误差完全内联与路由重叠常数表。

## 7. GEE-0 bookkeeping 闭合

新增 `docs/rh-gee0-pc2-boundary-and-route-overlap.md`。PC2 边界误差已内联为 `Err_PC2=o(Δ)`，路由有限重叠统一为 `log^{C_route}X`。GEE-0 现在可标记为 bookkeeping 闭合；下一步应攻 `GEE-LV` 与 `GEE-NRC` 两个出口上界。

## 8. GEE-LV 低体积出口

新增 `docs/rh-gee-lv-low-volume-exit-bound.md`。LV 只允许登记满足相对主异常阈值 `Vol_eff log^C X<=Δ/log^{B_LV}X` 的原子；这部分由平凡体积估计给 `Load(LV;X)=o(Δ)`。不满足阈值的原子必须转入 `SC/PI/A/FCT/LSMP/CE`，不再计入 LV。

## 9. GEE-NRC 参数硬障碍

新增 `docs/rh-gee-nrc-nonresonant-exit-bound.md`。`EXT-KL` 给出单包平方根上界，但要得到 `Load(NRC;X)=o(Δ)`，必须逐入口核验 `K_eff,total P_max^{1/2}log^A X=o(Δ)`，或证明 PPI 主层门槛压过 NRC 上界并把失败层转入其它出口。当前 GEE-NRC 是条件参数闭合，不是完全闭合。

## GEE-NRC 参数入口补充

- [x] 单变量 PPI 非共振入口：由平方根完成和与 `β>1/2` 闭合。
- [x] Tail/RKS NRC：由 `LV` 或主层回流分流闭合。
- [x] `NRC-2D`：双变量倒数包不再作为独立 NRC 硬点，已由 MidCap 转出到命名出口；剩余依赖 PI/DSO 与 DSO-SF。
- [x] `DSO-SF`：DSO 非共振包 square-function 无幂损失总量已由 `docs/rh-dso-sf-input-final.md` 补齐。

详见 `docs/rh-gee-nrc-entry-parameter-table.md`。

## NRC-2D 后续清单

- [x] `PPI-Rank`：证明加性分离二维权重有 `log^C X` 分离秩，失败转 `CE/SC/PI/LSMP/LV`。
- [ ] `MidCap-Structure`：证明中间容量层承载固定比例偏差时触发 `LSMP/SC/PI/CE`。
- [x] `NRC-2D-Closure`：已通过 AEX-3 参数表并回 GEE-NRC，作为 Transfer 而非 Sqrt-Sum 闭合。

## NRC-2D PPI-Rank 更新

- [x] `PPI-Rank`：固定复杂度 PPI 窗口给 `log^C X` 分离秩；失败转 `CE/SC/PI/LSMP/LV`。
- [ ] `MidCap-Structure`：证明中间容量层承载固定比例偏差时触发 `LSMP/SC/PI/CE`。

## Capacity-Match 更新

- [x] 高容量分支：`V_Q>=Plog^{B+C}X` 时二维 NRC 相对小。
- [x] 全局低体积分支：`V_Qlog^C X<=Δ/log^B X` 时转 `GEE-LV`。
- [ ] `MidCap-Structure`：中间容量层承载固定比例偏差时触发 `LSMP/SC/PI/CE`。

## MidCap-Structure 更新

- [x] `MidCap-Structure-Reduction`：中间容量层分流到 `LSMP/LV`、`SC`、`PI/DSO`、`CE` 或 Uniform 排斥。
- [ ] `GEE-PI/DSO/SC/LSMP/CE`：接收中间容量分流后的全局出口上界仍需闭合。

## GEE-PI/DSO 清单

- [ ] `Lac-Baseline`：lacunary 零频容量与异常负担不重复计数。
- [ ] `Dense-Carleson`：fixed-template dense pack 的 square-function/Carleson 容量上界。
- [ ] `Anomaly-L2-Control`：非终端异常函数 `L^2` 质量小于 `Δ/log^B X`，失败转结构出口。

## Dense-Carleson 状态更新

- [x] `Dense-Carleson`：dense fixed-template 容量上界由 `PC4-PI-Dense` 接入 GEE。
- [ ] `Baseline-Subtraction`：PI/DSO 零频容量不得重复计入异常负担；只登记超额偏差。

## Baseline-Subtraction 更新

- [x] `Baseline-Subtraction`：PI/DSO 零频容量只作基线扣除，进入 `Load` 的仅为超额偏差。
- [ ] 接收出口上界：`SC/LSMP/CE/FCT/A` 等仍需证明 `o(Δ)`。

## GEE-CE/LSMP 清单

- [x] 可吸收项：低质量、coarea、平方可和尾项满足相对阈值时给 `o(Δ)`。
- [ ] `Seed-Transfer Consistency`：CE/LSMP 输出 seed 必须有限重叠转入对应出口，且不重复计入 CE/LSMP。

## Seed-Transfer 更新

- [x] `Seed-Transfer Consistency`：CE/LSMP seed 有限重叠转入目标出口并从 CE/LSMP 删除。
- [ ] 剩余主出口：`GEE-FCT/GEE-SC/GEE-A` 仍需全局上界。

## GEE-FCT 更新

- [x] `GEE-FCT`：FCT 作为内部 Noether 转移闭合，最终无独立负担。
- [ ] 剩余主出口：`GEE-SC/GEE-A` 仍需全局上界。

## GEE-SC 更新

- [x] `GEE-SC`：短簇容量吸收与内部递归转移闭合。
- [ ] 剩余主出口：`GEE-A` 与全局最终合成审查。

## GEE-A 更新

- [x] `GEE-A`：ACC 同步容量吸收与内部转移闭合。
- [x] 全局 GEE 合成审查：检查九个出口闭合口径无循环、无重复计数、无未接收 seed。

## Global GEE 合成审查清单

- [x] 九出口闭合口径矩阵。
- [x] 事件图无循环总审查：逐环标注下降量或容量消耗。
- [x] 阈值常数总表：统一所有 `Δ/log^B X` 与 `log^C X` 损失。
- [x] Load 口径统一：全文只登记超额偏差。
- [x] 单篇主稿内联化：将关键定义和定理整理成顶刊审稿稿。

## GEE 最终一致性文件补充

- `docs/rh-gee-event-graph-no-cycle-audit.md`：补齐九出口转移图与 Lyapunov 无循环审查。
- `docs/rh-gee-threshold-constant-table.md`：补齐全局阈值常数包与 `B_final` 选择规则。
- `docs/rh-gee-load-convention-unification.md`：补齐最终 `Load` 口径，统一为相对零频基线的超额偏差。

审稿结论：这三项消除了 GEE 合成层面的主要口径不一致；单篇 Markdown 内联稿已补齐第一版。但清单仍不得标记为“RH 无条件证明完成”；最终剩余为正式 LaTeX 迁移、外部输入精确引用与逐条证明核验。

## 单篇主稿内联化更新

- [x] GEE 单篇内联审稿稿：`docs/rh-gee-single-paper-inline-draft.md` 已集中写入统一定义、九出口矩阵、事件图无循环、阈值层级、出口上界与条件合成定理。
- [x] 正式 LaTeX 主稿迁移：已把 GEE Markdown 审稿稿迁入 `paper/rh-proof/rh-contradiction-field.tex`；外部定理精确编号与命名引理逐条证明仍列入下方最小割集。

## 最终无条件化缺口审查更新

- [x] GEE LaTeX 主稿迁移：`paper/rh-proof/rh-contradiction-field.tex` 已新增 `Global Exit Exclusion` 节。
- [x] 最终剩余缺口审查：`docs/rh-unconditional-final-gap-audit.md` 已抽取最小割集。
- [x] `EXT-Precision`：外部定理逐条精确适配已由 `docs/rh-ext-precision-final.md` 补齐。
- [ ] `Local-Exit-Proofs`：九出口局部命题逐条正式证明；当前已归约为 AEX-1、AEX-2、AEX-3。
- [x] `Transfer-Accounting`：seed/内部转移权重守恒和有限重叠逐条证明。
- [x] `Review-Form-Elimination`：LaTeX 中 `Proof sketch for review` 与 `Review proof` 已清零；主定理 `review form` 作为最终警告另列。

## Transfer-Accounting 补强更新

- [x] `Transfer-Accounting`：`docs/rh-transfer-accounting-formal-appendix.md` 已证明 seed/内部转移权重守恒、源目标去重与有限重叠。
- [x] LaTeX 接入：`paper/rh-proof/rh-contradiction-field.tex` 已加入 Transfer-accounting proposition。
- [x] `EXT-Precision`：外部定理逐条精确适配已由 `docs/rh-ext-precision-final.md` 补齐。
- [ ] `Local-Exit-Proofs`：九出口局部命题逐条正式证明；当前已归约为 AEX-1、AEX-2、AEX-3。
- [x] `Review-Form-Elimination`：LaTeX 中 `Proof sketch for review` 与 `Review proof` 已清零；主定理 `review form` 作为最终警告另列。

## Local-Exit-Proofs 第一阶段更新

- [x] `LV/CE/LSMP/FCT/SC/A`：`docs/rh-local-exit-proofs-formal-appendix.md` 已给出低黑箱出口形式化闭合。
- [x] LaTeX 接入：`paper/rh-proof/rh-contradiction-field.tex` 已加入 Low-black-box local exits proposition。
- [ ] `PI/DSO`：无幂损失容量与 square-function 上界。
- [x] `NRC`：逐入口参数匹配已完成归约；单变量 `EXT-KL` 精确适配已由 `docs/rh-ext-kl-precision-final.md` 补齐。
- [x] `EXT-Precision`：外部定理逐条精确适配已由 `docs/rh-ext-precision-final.md` 补齐。
- [x] `Review-Form-Elimination`：LaTeX 中 `Proof sketch for review` 与 `Review proof` 已清零；主定理 `review form` 作为最终警告另列。

## 解析出口归约更新

- [x] `PI/DSO/NRC` 统一归约：`docs/rh-analytic-exit-reduction-table.md` 已抽取 AEX-1、AEX-2、AEX-3。
- [x] LaTeX 接入：`paper/rh-proof/rh-contradiction-field.tex` 已加入 Analytic exit reduction proposition。
- [ ] `AEX-1`：零频扣除后的投影容量不等式；当前已归约为 `PI-Lac/PI-Dense`。
- [x] `AEX-2`：DSO 无幂损失 square-function 总量已由 `DSO-SF` 闭合。
- [x] `AEX-3`：NRC 逐入口参数匹配与单变量 `EXT-KL` 精确适配已补齐；双变量/DSO-E 仍按 Transfer/DSO-SF 路由。
- [x] `EXT-Precision`：外部定理逐条精确适配已由 `docs/rh-ext-precision-final.md` 补齐。
- [x] `Review-Form-Elimination`：LaTeX 中 `Proof sketch for review` 与 `Review proof` 已清零；主定理 `review form` 作为最终警告另列。

## AEX-1 补强更新

- [x] `AEX-1` 账本归约：`docs/rh-aex1-projection-capacity-formal.md` 已把投影容量不等式压缩为 `PI-Lac` 与 `PI-Dense` 两个容量输入。
- [x] LaTeX 接入：`paper/rh-proof/rh-contradiction-field.tex` 已加入 AEX-1 projection capacity proposition。
- [x] `PI-Lac`：lacunary Bessel/Parseval 容量正式证明已由 `docs/rh-pi-lac-input-final.md` 补齐。
- [x] `PI-Dense`：dense fixed-template Carleson/square-function 容量已归约到 `DSO-SF/EXT-KL`。

## AEX-2 补强更新

- [x] `AEX-2` 账本归约：`docs/rh-aex2-dso-squarefunction-formal.md` 已把 DSO square-function 总量压缩为 `DSO-SF` 输入。
- [x] LaTeX 接入：`paper/rh-proof/rh-contradiction-field.tex` 已加入 AEX-2 DSO square-function proposition。
- [x] `DSO-SF`：martingale square-function 基线容量已文内证明。

## AEX-3 补强更新

- [x] `AEX-3` 账本归约：`docs/rh-aex3-nrc-parameter-match-formal.md` 已完成 NRC 四入口参数表。
- [x] LaTeX 接入：`paper/rh-proof/rh-contradiction-field.tex` 已加入 AEX-3 NRC parameter matching proposition。
- [x] `EXT-KL`：单变量 NRC 外部完成和精确适配已由 `docs/rh-ext-kl-precision-final.md` 补齐。
- [x] `DSO-SF`：DSO-E 入口 square-function 基线容量已文内证明。

## 最终剩余输入归并

- [x] 旧未完成项归并：`docs/rh-final-remaining-inputs-table.md` 已把历史清单折叠为真实剩余输入。
- [x] `PI-Lac`：lacunary 投影容量 Bessel/Parseval 界已补齐。
- [x] `PI-Dense`：dense fixed-template Carleson/square-function 容量界已归约到 `DSO-SF/EXT-KL`。
- [x] `DSO-SF`：martingale square-function 基线容量界已文内证明。
- [x] `EXT-Precision`：外部定理精确引用与变量匹配已补齐。
- [~] `Review-Form-Elimination`：proof-sketch/review-proof 已清零；主定理 review-form 暂留为诚实警告。

## PI-Lac 完成更新

- [x] `PI-Lac`：`docs/rh-pi-lac-input-final.md` 已给出 lacunary Bessel/Parseval/有限重叠容量证明。
- [x] LaTeX 接入：`paper/rh-proof/rh-contradiction-field.tex` 已加入 PI-Lac input proposition。
- [x] `PI-Dense`：dense fixed-template Carleson/square-function 容量界已归约到 `DSO-SF/EXT-KL`。
- [x] `DSO-SF`：martingale square-function 基线容量界已文内证明。
- [x] `EXT-Precision`：外部定理精确引用与变量匹配已补齐。
- [~] `Review-Form-Elimination`：proof-sketch/review-proof 已清零；主定理 review-form 暂留为诚实警告。

## PI-Dense 归约更新

- [x] `PI-Dense`：`docs/rh-pi-dense-input-final.md` 已将 dense Carleson/square-function 容量归约到 `DSO-SF` 与 `EXT-KL`。
- [x] LaTeX 接入：`paper/rh-proof/rh-contradiction-field.tex` 已加入 PI-Dense reduction proposition。
- [x] `DSO-SF`：martingale square-function 基线容量界已文内证明。
- [x] `EXT-Precision`：外部定理精确引用与变量匹配已补齐。
- [~] `Review-Form-Elimination`：proof-sketch/review-proof 已清零；主定理 review-form 暂留为诚实警告。

## DSO-SF 完成更新

- [x] `DSO-SF`：`docs/rh-dso-sf-input-final.md` 已给出 martingale square-function 基线容量证明。
- [x] LaTeX 接入：`paper/rh-proof/rh-contradiction-field.tex` 已加入 DSO-SF input proposition。
- [x] `EXT-Precision`：外部定理精确引用与变量匹配已补齐。
- [~] `Review-Form-Elimination`：proof-sketch/review-proof 已清零；主定理 review-form 暂留为诚实警告。

## EXT-Precision 完成更新

- [x] `EXT-Precision`：`docs/rh-ext-precision-final.md` 已给出外部定理精确适配表。
- [x] LaTeX 接入：`paper/rh-proof/rh-contradiction-field.tex` 已加入 EXT-Precision theorem。
- [~] `Review-Form-Elimination`：proof-sketch/review-proof 已清零；主定理 review-form 暂留为诚实警告。

## Review-Form-Elimination 审查更新

- [x] GEE 段 review-form 消除：`paper/rh-proof/rh-contradiction-field.tex` 中 GEE 局部证明已升级为普通 proof。
- [x] 审查报告：`docs/rh-review-form-elimination-audit.md` 已列出仍保留 review-form 的 PC1--PC4/C4--C9 主链。
- [~] 全文 `Review-Form-Elimination`：普通 proof 标记已清零；主定理 review-form 与 submission warning 仍保留。


## EXT-KL 与同尺度 GEE 矛盾更新

- [x] `EXT-KL`：新增 `docs/rh-ext-kl-precision-final.md`，固定素数模非退化 `ax+b/x` 完成和、区间 completion 对数损失、退化出口和 AEX-3 单变量入口估计。
- [x] `EXT-PC1-LI`：新增 `docs/rh-ext-pc1-li-precision-final.md`，固定有限边界零点文内证明与无限边界/上确界的 Landau--Ingham 外部接口。
- [x] GEE 下界/上界同尺度化：LaTeX 主稿已把下界 `Δ log^{-C_route}X` 与上界 `Δ log^{-B_final}X` 比较，要求 `B_final>C_route+C_total+10`，避免旧稿中用 `o(Δ)` 直接压过多对数下界的口径漏洞。
- [~] 主定理 `review form`：仍保留；`docs/rh-final-theorem-promotion-audit.md` 明确当前不能删除 warning，下一步应编号化 C4/C5/C6/C9。


## C6 No-Cycle 主稿编号化更新

新增 `docs/rh-c6-no-cycle-maintext-final.md`。LaTeX 主稿已把 C6 从 consolidated proof 升级为 `Definition C6 internal state graph`、`Lemma C6 self-loop exclusion`、`Lemma C6 mixed-cycle exclusion` 与最终 `C6 internal terminal no-cycle` 的编号化证明链。主定理 warning 仍保留；下一步最优为 C9 Fourier--Vaaler tail closure 的编号化。


## C9 Fourier--Vaaler Tail 主稿编号化更新

新增 `docs/rh-c9-tail-maintext-final.md`。LaTeX 主稿已把 C9 从 consolidated proof 升级为固定复杂度模板定义、原子尾项、布尔稳定性、盒族求和和无自由高频尾项四个编号引理，再推出 `C9 tail closure`。主定理 warning 仍保留；剩余 consolidated proof 为 C4 sparse branch 与 C5 DGap branch。


## C4 Sparse Branch 主稿编号化更新

新增 `docs/rh-c4-sparse-maintext-final.md`。LaTeX 主稿已把 C4 从 consolidated proof 升级为稀疏三分、覆盖/空洞出口、overlap 双锚正规形和主层路由四个编号引理，再推出 `C4 sparse branch`。主定理 warning 仍保留；剩余 consolidated proof 只剩 C5 DGap branch。


## C5 DGap Branch 主稿编号化更新

新增 `docs/rh-c5-dgap-maintext-final.md`。LaTeX 主稿已把 C5 从 consolidated proof 升级为盒局部化、baseline 后 frame 下界、正交投影分配和低维残余抽取四个编号引理，再推出 `C5 DGap branch`。至此 C4/C5/C6/C9 的 `Consolidated proof` 已全部消除；主定理 warning 仍保留，等待最终全文升级审查。


## 最终全文升级审查评审更新

新增 `docs/rh-final-upgrade-review-2026-05-01.md`。自动扫描确认 `Consolidated proof`、`Proof sketch for review`、`Review proof` 均为 0，且 LaTeX `\ref` 未发现缺失标签。但审查结论是不应删除主定理 `review form` 与 `Submission warning`：主稿仍有条件合成口径、AEX 输入接受性和 EXT 页码/定理号核验义务。下一步最优为逐项处理 U1--U3：主定理前提改写、AEX 条件化措辞消除、EXT 精确定理号表。


## U2 AEX 接受性核验更新

新增 `docs/rh-u2-aex-acceptance-review.md`。审查确认 AEX-1 已由 Baseline-Subtraction、PI-Lac、PI-Dense 支撑，PI-Dense 已归约到 DSO-SF/EXT-KL；AEX-2 由 DSO-SF 支撑；AEX-3 的单变量入口由 EXT-KL 支撑，Tail/RKS、双变量 PPI 与 DSO-E 均转入已命名出口或 DSO-SF。LaTeX 主稿已删除 “conditional exactly on AEX-1, AEX-2, AEX-3” 措辞，改为由前文 AEX propositions 与已记录输入支撑。主定理 warning 仍保留；下一步最优为 U3 EXT 页码/定理号表。


## U3 EXT 精确引用表更新

新增 `docs/rh-u3-ext-reference-table.md`。U3 已完成章节/论文级定位：Vaaler、Baker、Vaughan 给出卷期页码；Bourgain--Garaev 给出 arXiv/DOI；Iwaniec--Kowalski、Katz、Titchmarsh--Heath-Brown、Ingham、Halberstam--Richert 给出章节/定理定位与受限使用边界。专著具体页码仍可在最终排版时核对，但不再作为数学逻辑缺口。下一步最优转向 U1/U4：主定理前提和 review-draft 口径统一。
