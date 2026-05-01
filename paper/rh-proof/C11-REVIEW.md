# C11 LaTeX/PDF 审稿工程记录

## 本轮完成

- 生成单篇 LaTeX 主稿：`paper/rh-proof/rh-contradiction-field.tex`。
- 生成 BibTeX 文件：`paper/rh-proof/rh-references.bib`。
- 主稿已包含符号表、PC1、PC2/C3、C4、C5、C6、C9、外部引用表与合并主定理。
- 主稿保留明确审稿警告：当前是 review form，不能在逐行审稿前宣称 RH 已最终无条件证明。

## 本机限制

当前环境未安装 `pdflatex`、`latexmk` 或 `bibtex`，因此无法在本机完成 PDF 编译验证。

## 后续编译命令

在安装 TeX Live 的环境中执行：

```bash
cd paper/rh-proof
pdflatex rh-contradiction-field.tex
bibtex rh-contradiction-field
pdflatex rh-contradiction-field.tex
pdflatex rh-contradiction-field.tex
```

或：

```bash
cd paper/rh-proof
latexmk -pdf rh-contradiction-field.tex
```

## C11 剩余人工审查

1. 检查 PDF 是否存在 undefined references。
2. 将 Markdown 附录中的 C2/C7 细节逐步内联到主稿。
3. 将外部引用补为期刊要求的页码或定理号。
4. 对 C4--C9 的每个 review-form proof 做逐行数学审稿。
5. 只有所有审稿项通过后，才可考虑将标题从 review draft 改为 final proof draft。

## GEE LaTeX 迁移更新

- 已将 `docs/rh-gee-single-paper-inline-draft.md` 的核心内容迁入 `paper/rh-proof/rh-contradiction-field.tex` 的 `Global Exit Exclusion` 节。
- 新增 `Excess load` 定义、`GEE-0 bookkeeping`、GEE 事件无循环、阈值兼容、GEE 上界和条件矛盾 corollary。
- 仍保留 review-form 口径：这些定理依赖九出口局部机制和外部输入逐条验证，不能改写为 RH 无条件证明定稿。
