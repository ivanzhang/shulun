# RH 主稿最终全文升级审查评审（2026-05-01）

本文对 `paper/rh-proof/rh-contradiction-field.tex` 做最终升级审查，目标是判断是否可以删除主定理 `review form` 与 `Submission warning`，并把稿件从审查稿口径推进为可最终编译审查的验证稿。

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

- `Submission warning`；
- 主定理已由 U1 改为“By the preceding theorems...”合成口径，不再使用 `review form` 标签；
- 摘要与 GEE 段已由 U4 改成 verification manuscript / final synthesis 口径，不再使用旧审查稿措辞；
- GEE analytic exit reduction 的 AEX 条件化措辞已由 U2 消除；EXT 精确引用定位已由 U3 完成。当前仍保留的是最终编译审查 U5 与独立逐行 referee verification 义务。

这些不是排版残留，而是数学审稿状态信号。它们说明当前稿件已进入“验证稿”状态：内部 proof 标记和主定理 review-form 标签已经清零，但最终 warning 仍提示若干上游证明包、controlled exits 与外部输入需要最终接受。

## 3. 是否可以删除 warning？

**结论：当前不应删除。**

理由如下：

1. U1 已把主定理从“Assume Theorems...”改为“By Theorems...”的前文合成口径。
2. U4 已把标题、摘要和 GEE 段从 review-draft 口径改为 verification manuscript / final synthesis 口径。
3. U2 已消除 AEX-1/2/3 的条件化措辞，U3 已完成 EXT 章节/论文级定位。
4. 但 `Submission warning` 仍应保留：它现在不是为了标记 review-form 文体，而是为了诚实提示最终无条件 RH 证明仍需 U5 编译审查、专著页码核验和独立逐行 referee verification。

## 4. 删除 warning 前的最小剩余清单

| 编号 | 必做项 | 通过标准 |
|---|---|---|
| U1 | 改写主定理前提 | 已完成：主定理改为“By Theorems...”前文合成口径；不再把前文编号定理作为额外假设 |
| U2 | AEX 输入接受性核验 | 已完成；见 `docs/rh-u2-aex-acceptance-review.md`，主稿已消除 “conditional exactly on AEX-1/2/3” 措辞 |
| U3 | EXT 页码/定理号核验 | 已完成章节/论文级定位；见 `docs/rh-u3-ext-reference-table.md`，专著页码留作排版核验 |
| U4 | 摘要与标题口径统一 | 已完成：标题、摘要、GEE 段改为 verification manuscript / final synthesis 口径 |
| U5 | 最终编译审查 | 在 TeX 环境中跑 `latexmk`/BibTeX，确认无 undefined refs/cites |
| U6 | 主定理升级 | `review form` 已删除；`Submission warning` 需等 U5 与独立逐行审查完成后才可考虑删除 |

## 5. 推荐下一步

下一步最优不是继续扩展数学框架，而是执行 U5 与最终一致性审查：

1. U1 已完成：主定理前提改为前文合成口径；
2. U2 已完成：AEX-1/2/3 条件化措辞已消除；
3. U3 已完成：EXT 章节/论文级定位表已补齐；
4. U4 已完成：标题、摘要和 GEE 段口径已统一；
5. 下一步处理 U5：在 TeX 环境中最终编译，核查 undefined refs/cites、BibTeX 和专著页码。

在 U5 与独立逐行审查完成前，本文应保持当前诚实状态：主定理已不是 review-form 条件合成定理，但仍不能宣称 RH 无条件证明定稿。
