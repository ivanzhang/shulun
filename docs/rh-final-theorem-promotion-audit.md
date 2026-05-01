# RH 主定理升级审查：最终 warning 是否可删除

本文对 `paper/rh-proof/rh-contradiction-field.tex` 中主定理 `review form` 与 `Submission warning` 做最终升级审查。结论先行：当前不能诚实删除 warning；但普通 proof 级审稿标记已经清零，且 `EXT-KL`、`EXT-PC1-LI` 的主稿实际使用形式均已精确适配。

## 1. 已完成的可审稿补正

- `Proof sketch for review` 与 `Review proof` 已从 LaTeX 主稿中全部消除。
- `PC1` 有主稿证明；有限边界零点情形文内闭合，无限边界/上确界情形由 `docs/rh-ext-pc1-li-precision-final.md` 固定为 `EXT-PC1-LI`。
- `PC2` 有主稿 CRT 零频基线证明。
- `EXT-KL` 单变量 NRC 入口已由 `docs/rh-ext-kl-precision-final.md` 固定为素数模非退化 `ax+b/x` 完成和。
- GEE 下界/上界已经同尺度化：下界为 `Δ log^{-C_route}X`，上界通过阈值层级压到 `Δ log^{-B_final}X`，并要求 `B_final>C_route+C_total+10`。

## 2. 仍不能删除 warning 的原因

主定理仍以如下形式成立：在接受 PC1、C4、C5、C6、C9、GEE upper、PC2、C3、GEE0 以及 restricted external inputs 的前提下，离线零点无自由逃逸通道。

这还不是“RH 无条件证明”的最终期刊表述，原因是：

1. 主稿仍称为 `Consolidated Review Draft`，其结构依赖多个已归档证明包的接受性，而非单篇内全部逐行展开。
2. C4/C5/C6/C9 虽在主稿有 consolidated proof，但它们大量引用历史归档中的 routing、capacity、tail、terminal 结论；最终期刊稿需逐条给出定理号或内联证明。
3. 外部输入虽已精确适配为 restricted packages，但页码/定理号仍是排版核验义务。
4. 若删除 warning，会把“条件合成审查稿”误标为“RH 已无条件证明定稿”，这超过当前文档可审查状态。

## 3. 最小剩余审稿义务

要删除主定理 `review form`，至少需要完成以下一张验收表：

| 项 | 需要动作 | 当前状态 |
|---|---|---|
| C4 sparse branch | 将 consolidated proof 展开为逐引理链，或列出精确定理号 | 已完成主稿编号化；见 `docs/rh-c4-sparse-maintext-final.md` |
| C5 DGap branch | 将三接口链与投影/尾项归约逐条编号 | 已完成主稿编号化；见 `docs/rh-c5-dgap-maintext-final.md` |
| C6 no-cycle | 将事件图势函数下降写成形式化图论引理 | 已完成主稿编号化；见 `docs/rh-c6-no-cycle-maintext-final.md` |
| C9 tail closure | 将 Vaaler/Fourier 尾项链逐项定理化 | 已完成主稿编号化；见 `docs/rh-c9-tail-maintext-final.md` |
| EXT packages | 给 Titchmarsh/Ingham/IK/Katz/Vaaler/BG/Baker/Selberg/Vaughan 具体章节/定理号 | 使用形式已固定，页码未核验 |
| Main theorem | 删除 review form 并改题名/摘要口径 | 等上述完成后再做 |

## 4. 审稿结论

本轮可以标记完成的是：`EXT-PC1-LI` 精确适配、`EXT-KL` 精确适配、GEE 同尺度矛盾修补、普通 proof 标记清零。

本轮不能完成的是：把主定理升级为最终无条件 RH 定理。C4、C5、C6、C9 均已完成主稿编号化。下一步应进行主定理升级前的全文交叉引用、外部定理号和 warning 删除条件总审查。


## 最终全文升级审查评审更新

新增 `docs/rh-final-upgrade-review-2026-05-01.md`。自动扫描确认 `Consolidated proof`、`Proof sketch for review`、`Review proof` 均为 0，且 LaTeX `\ref` 未发现缺失标签。但审查结论是不应删除主定理 `review form` 与 `Submission warning`：主稿仍有条件合成口径、AEX 输入接受性和 EXT 页码/定理号核验义务。下一步最优为逐项处理 U1--U3：主定理前提改写、AEX 条件化措辞消除、EXT 精确定理号表。
