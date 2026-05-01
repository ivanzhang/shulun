# RH 主稿最终全文升级审查评审（2026-05-01）

本文对 `paper/rh-proof/rh-contradiction-field.tex` 做最终升级审查，目标是判断是否可以删除主定理 `review form` 与 `Submission warning`，并把稿件从 review draft 升级为最终无条件 RH 证明稿。

## 1. 自动扫描结论

- `Consolidated proof`：0 处。
- `Proof sketch for review`：0 处。
- `Review proof`：0 处。
- LaTeX 交叉引用：未发现缺失 `\ref` 对应的 `\label`。
- 普通主链 C4/C5/C6/C9 已完成编号化：
  - C4：`docs/rh-c4-sparse-maintext-final.md`；
  - C5：`docs/rh-c5-dgap-maintext-final.md`；
  - C6：`docs/rh-c6-no-cycle-maintext-final.md`；
  - C9：`docs/rh-c9-tail-maintext-final.md`。

## 2. 仍保留的升级阻断点

主稿仍明确包含：

- `Consolidated contradiction-field theorem, review form`；
- `Submission warning`；
- 摘要与 GEE 段中的 `review draft` / `conditional synthesis` 口径；
- GEE analytic exit reduction 中的“conditional exactly on AEX-1, AEX-2, AEX-3 and accepted external estimates”。

这些不是排版残留，而是数学审稿状态信号。它们说明当前稿件是“条件合成审查稿”：内部 proof 标记已经清零，但主定理仍依赖若干上游证明包与外部输入被最终接受。

## 3. 是否可以删除 warning？

**结论：当前不应删除。**

理由如下：

1. 主定理仍表述为“Assume Theorems... and restricted external inputs”；这是条件合成定理，而不是单句 RH 最终定理。
2. `AEX-1/AEX-2/AEX-3` 虽已有主稿 proposition，但 analytic exit reduction 的证明仍以这些输入及外部估计为条件。
3. `EXT-*` 输入已完成受限适配，但页码/定理号仍需投稿排版核验；这不一定是数学缺口，但足以阻止“最终定稿”口径。
4. 摘要仍称本文为 review package；若仅删除 theorem warning 而不改摘要、GEE 条件化措辞和主定理前提，会造成文体与数学状态不一致。

## 4. 删除 warning 前的最小剩余清单

| 编号 | 必做项 | 通过标准 |
|---|---|---|
| U1 | 改写主定理前提 | 从“Assume Theorems...”改为“By the preceding theorems...”且所有前置定理均已在稿内或引用中闭合 |
| U2 | AEX 输入接受性核验 | AEX-1/2/3 不再以条件输入形式出现，或明确其被前文 theorem 完全证明 |
| U3 | EXT 页码/定理号核验 | `EXT-PC1-LI/KL/Vaaler/BG/Selberg/Vaughan` 均有精确书目、章节或定理号 |
| U4 | 摘要与标题口径统一 | 删除 review package/review draft/conditional synthesis 相关措辞 |
| U5 | 最终编译审查 | 在 TeX 环境中跑 `latexmk`/BibTeX，确认无 undefined refs/cites |
| U6 | 主定理升级 | 完成 U1--U5 后，才删除 `review form` 与 `Submission warning` |

## 5. 推荐下一步

下一步最优不是继续扩展数学框架，而是执行 U1--U3 的逐项核验：

1. 先专攻 AEX-1/2/3 在主稿中的“条件化措辞”消除；
2. 再做 EXT 页码/定理号表；
3. 最后统一摘要、标题、主定理和 warning。

在这些完成前，本文应保持当前诚实状态：普通证明审稿标记已清零，但主定理仍是 review-form 条件合成定理，不能宣称 RH 无条件证明定稿。
