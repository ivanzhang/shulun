# RH/GEE 最终剩余输入表

本文对 `docs/rh-merge-unconditional-checklist.md` 中的旧未完成项作归并，避免把已归约的历史硬点重复计算。结论：当前真正剩余不再是九出口整体，也不是 NRC-2D 泛化硬点，而是四组可定位输入。

## 1. 已归约但旧清单仍可见的项目

| 旧项目 | 当前归并去向 |
|---|---|
| `MidCap-Structure` | 已由 `docs/rh-nrc-2d-midcap-structure-route.md` 分流；剩余进入 `PI/DSO` 与低黑箱出口 |
| `GEE-PI/DSO/SC/LSMP/CE` 接收出口 | 低黑箱出口已由 `docs/rh-local-exit-proofs-formal-appendix.md` 处理；PI/DSO 进入 AEX-1/AEX-2 |
| `Lac-Baseline`、`Baseline-Subtraction` | 已由 `docs/rh-gee-baseline-subtraction-lemma.md` 与 AEX-1 账本处理 |
| `Seed-Transfer Consistency` | 已由 `docs/rh-transfer-accounting-formal-appendix.md` 处理 |
| `GEE-FCT/GEE-SC/GEE-A` | 已由低黑箱出口附录处理为内部下降或转出 |
| `NRC-2D` | 已由 AEX-3 改写为 MidCap 转出，不再是独立 NRC 终态 |

## 2. 当前真正剩余输入

| 编号 | 输入 | 作用 | 当前状态 |
|---|---|---|---|
| R1 | `PI-Lac` | lacunary 投影容量 Bessel/Parseval 界 | 已由 `docs/rh-pi-lac-input-final.md` 补齐 |
| R2 | `PI-Dense` | dense fixed-template Carleson/square-function 容量界 | 已归约到 `DSO-SF/EXT-KL` |
| R3 | `DSO-SF` | martingale square-function 基线容量界 | 已由 `docs/rh-dso-sf-input-final.md` 文内证明 |
| R4 | `EXT-Precision` | `EXT-PC1-LI/EXT-KL/EXT-Vaaler/EXT-BG/EXT-Selberg/EXT-Vaughan` 的定理号、变量匹配、常数依赖 | 已由 `docs/rh-ext-precision-final.md` 补齐；页码核验为排版义务 |
| R5 | `Review-Form-Elimination` | 删除或升级 LaTeX 中所有 `Proof sketch`、`Review proof`、`review form` | PC1 与 PC2 已升级；剩余 C9/GEE 汇总/AEX-3 与主定理 review form |

## 3. 依赖关系

`R1` 与 `R2` 完成后，AEX-1 可勾选完成。

`R3` 完成后，AEX-2 可勾选完成，并解除 AEX-3 中 DSO-E 入口依赖。

`R4` 完成后，PC1、NRC 单变量、Vaaler/Fourier、BG/RKS、Selberg/Vaughan 等外部输入可从 restricted-use 升级为正式引用。

`R5` 只能最后完成；否则会把尚未证实的 review-form 证明误改成 final proof。

## 4. 审稿结论

当前文件工程和内部账本已大幅收束。若目标是继续向无条件 RH 证明推进，下一步最优不应再扩展事件图，而应直接专攻 R1--R3 三个容量输入，随后做 R4 外部引用精确化和 R5 review-form 消除。

## 5. PI-Lac 完成状态

新增 `docs/rh-pi-lac-input-final.md`，并在 LaTeX 主稿中加入 PI-Lac input proposition。`PI-Lac` 已由强 lacunary Mellin 支撑有限重叠、单尺度非终端偏差有界和 Baseline-Subtraction 闭合。最终剩余输入从五项降为四项：`PI-Dense`、`DSO-SF`、`EXT-Precision`、`Review-Form-Elimination`。

## 6. PI-Dense 归约状态

新增 `docs/rh-pi-dense-input-final.md`，并在 LaTeX 主稿中加入 PI-Dense reduction proposition。`PI-Dense` 不再作为独立最终输入，而归约到 `DSO-SF` 与 `EXT-KL`：dense pack 的 CRT martingale 正交由 DSO-C/TC 处理，Euler 局部复杂度由 DSO-E/EXT-KL/FCT/LSMP 接收，剩余全局容量基线正是 `DSO-SF`。

最终剩余输入更新为三项：`DSO-SF`、`EXT-Precision`、`Review-Form-Elimination`。

## 7. DSO-SF 完成状态

新增 `docs/rh-dso-sf-input-final.md`，并在 LaTeX 主稿中加入 DSO-SF input proposition。`DSO-SF` 已化为 CRT filtration 上的 Hilbert martingale square-function 恒等式：`Σ||D_kF||_2^2<=||F-E_0F||_2^2`。固定复杂度 frame 只损失多对数；失败项转入命名出口。

最终剩余输入更新为两项：`EXT-Precision` 与 `Review-Form-Elimination`。

## 8. EXT-Precision 完成状态

新增 `docs/rh-ext-precision-final.md`，并在 LaTeX 主稿中加入 EXT-Precision theorem。外部输入已归入六组标准引用并给出受限使用形式、变量匹配和失败出口。页码/定理号核对仍是投稿排版义务，但不再是数学逻辑缺口。

最终剩余输入更新为一项：`Review-Form-Elimination`。

## 9. Review-Form-Elimination 审查状态

新增 `docs/rh-review-form-elimination-audit.md`。GEE 段已消除 review-form 口径；但 PC1--PC4/C4--C9 与主定理仍保留 review-form/proof-sketch。最终剩余从“输入缺口”转为“全文逐行证明升级”：必须逐条升级 PC1、PC2/C3、C4、C5、C6、C9 和主定理证明后，才可宣称 RH 无条件证明定稿。
