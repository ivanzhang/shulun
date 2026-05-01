# NRC/EXT 最终引用审查：非共振完成和与外部定理包

本文对 `NRC/EXT` 做最终审稿级引用核查。目标是确认 PC3/PC4 中所有“非共振解析估计”均落到已命名外部定理标签，且失败分支明确转入 FCT/LSMP/PI，不形成新的黑箱。

## 1. NRC 使用的唯一深解析输入

`docs/nrc-theoremization.md` 的核心估计是：对素数模数 `P`，非退化倒数/混合相位满足

`|Σ_{x∈F_P^*} e_P(ax+b/x)| <= 2P^{1/2}`，

不完全区间和经完成法多 `logP` 损失。该输入正是 `docs/external-theorem-package.md` 的 `EXT-KL`。

NRC 其余步骤为：有限复杂度展开、Vaaler/平滑截断、完成法和三角不等式；这些只造成固定对数损失，已并入 `K_eff` 与常数包。

## 2. 非共振失败的出口

NRC 的非共振条件为

`ξ notin Span_H(Ξ(g))`。

若失败，则不调用 `EXT-KL`，而记录为 frequency-collision terminal，即 `FCT_seed`。该出口由：

- `docs/fct-tree-wfe-theoremization.md`；
- `docs/rh-pc4-fct-noether-descent-ledger.md`；
- `docs/rh-pc4-terminal-final-no-cycle-audit.md`

接收。因此 NRC 不存在“估计失败但未命名”的分支。

## 3. EXT 标签覆盖矩阵

| 标签 | 用途 | 使用位置 | 审稿状态 |
| --- | --- | --- | --- |
| `EXT-KL` | Weil/Kloosterman 完整和与完成法 | NRC、DSO-E2、RKS 短侧 | 精确到 Iwaniec--Kowalski/Katz |
| `EXT-BG` | 倒数 Kloosterman 多线性对数节省 | Tail-log4/RKS | 已有 BG/Baker 引用 |
| `EXT-Vaaler` | 区间指标 Fourier 截断 | PPI、Tail-log4、D 组 | Vaaler 1985 |
| `EXT-Selberg` | 二维线性上筛 | Tail-log4-M | Halberstam--Richert/Iwaniec--Kowalski |
| `EXT-Vaughan` | von Mangoldt Type I/II | Tail-log4/RKS | Vaughan/Iwaniec--Kowalski |
| `EXT-PC1-EF` | 平滑 ζ 显式公式 | PC1 | Titchmarsh/Iwaniec--Kowalski |
| `EXT-PC1-LI` | Landau--Ingham 振荡 | PC1 | Titchmarsh/Ingham |

这覆盖了当前文档中所有非初等外部解析输入。

## 4. DSO-E 与 NRC 的匹配

`docs/rh-pc4-dso-e-unconditionalization-audit.md` 已说明：

- 单层字符正交是有限群 Parseval，无需外部深定理；
- 纯倒数差可化为非主加法字符和；
- 混合相位调用 `EXT-KL`；
- 退化/共振失败转 FCT；
- 大局部复杂度转 LSMP-Freq 或 FCT。

因此 DSO-E 的解析引用也被 `EXT-KL + NRC/FCT/LSMP` 覆盖。

## 5. Tail-log4/RKS 外部引用边界

`EXT-BG/EXT-Selberg/EXT-Vaughan/EXT-Vaaler` 主要支撑 Tail-log4/RKS/D 组结构附录。当前 RH 总攻主链只需要它们作为已命名外部输入，不再把它们混入 PC4 终端事件图。若审稿要求更细页码，应在 `docs/ext-citation-final-audit.md` 的对应条目补齐，不改变逻辑链。

## 6. NRC/EXT 最终引用定理

**Theorem NRC-EXT-Citation-Closure。** 当前总攻文档中所有 NRC/EXT 解析输入均可归入 `EXT-KL`, `EXT-BG`, `EXT-Vaaler`, `EXT-Selberg`, `EXT-Vaughan`, `EXT-PC1-EF`, `EXT-PC1-LI` 七类标签。NRC 的非共振估计成功时由 `EXT-KL` 给出，失败时按定义转入 FCT；因此 NRC/EXT 不提供新的未命名逃逸通道。

**证明。** NRC 主定理的唯一深估计是 Kloosterman 完整和与完成法，即 `EXT-KL`。PC1 的解析输入由 `EXT-PC1-EF/LI` 覆盖。Tail-log4/RKS/D 组所需外部事实由 BG、Vaaler、Selberg、Vaughan 标签覆盖。各失败分支在相应文档中均转入 FCT、LSMP、PI 或容量事件。证毕。

## 7. 剩余编辑义务

数学逻辑上，NRC/EXT 已可作为命名外部定理包引用。投稿编辑阶段仍需：

1. 给 `EXT-PC1-LI` 选择具体定理编号或教材章节；
2. 给 `EXT-KL` 的不完全和完成法补页码；
3. 若使用 Tail-log4/RKS，补 BG/Baker/Selberg/Vaughan 的精确定理编号。
