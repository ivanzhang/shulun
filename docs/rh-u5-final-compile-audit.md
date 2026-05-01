# U5 最终编译与引用一致性审查

本文处理最终升级清单 U5：对 `paper/rh-proof/rh-contradiction-field.tex` 做最终编译、交叉引用、BibTeX 与明显 LaTeX 结构审查。

## 1. 本地 TeX 环境与真实编译

本轮已安装最小 TeX Live 工具链，并在 `paper/rh-proof` 下运行：

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error rh-contradiction-field.tex
```

结果：真实 PDF 已生成，路径为 `paper/rh-proof/rh-contradiction-field.pdf`，共 16 页，约 285 KB。BibTeX 已执行并读取 `rh-references.bib`。

## 2. 已完成的 U5 检查

真实编译与静态脚本交叉核验得到：

- `labels = 40`，`refs = 57`，缺失 `ref = 0`；
- `cites = 11`，`bibkeys = 9`，缺失 `cite = 0`；
- `latexmk` 日志无 undefined references/citations；
- 重复 label：0；
- 重复 bibkey：0；
- `theorem/lemma/corollary/proposition/definition/remark/proof/longtable/abstract/document` 环境 begin/end 数量全部匹配；
- 主稿中 `review form`、`review draft`、`Assume Theorems`、`conditional synthesis` 残留为 0；
- `exttt` 拼写错误残留为 0。

## 3. 本轮补正

U5 静态审查发现主稿此前没有 `\cite{...}`，会导致 BibTeX 参考文献无法真实参与编译。已在 `External references` 表中为全部受限外部输入接入正式 BibTeX 引用：

- `Titchmarsh1986`、`Ingham1932`；
- `IwaniecKowalski2004`、`Katz1988`；
- `Vaaler1985`；
- `BourgainGaraev2012`、`Baker2012`；
- `HalberstamRichert1974`；
- `Vaughan1977`。

同时把 EXT-Precision 命题中的 `Table~\ref{sec:external}` 修正为 `Section~\ref{sec:external}`，因为该 label 标记的是 section 而不是 table counter。

## 4. U5 结论

U5 的本地工程审查已完成：PDF 可生成，BibTeX 可执行，未发现 undefined references/citations，也未发现 LaTeX fatal error。日志仅剩少量 overfull/underfull 版式提示，不影响引用闭合与数学文本结构。

不得据此删除 `Submission warning` 或宣称 RH 无条件证明定稿；剩余义务已精确收缩为：

1. 最终核对专著页码/定理号；
2. 进行独立逐行 referee verification；
3. 若投稿前需要，可继续细调少量 overfull/underfull 版式提示。
