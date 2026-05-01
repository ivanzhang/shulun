# 最终审稿剩余义务闭合账本

本文汇总 U1--U5 后的全部审稿义务，区分“作者侧可执行义务”和“必须由外部审稿/排版完成的义务”。

## 1. 作者侧可执行义务

| 项目 | 状态 | 证据 |
|---|---|---|
| 主定理 `review form` 删除 | 已完成 | `paper/rh-proof/rh-contradiction-field.tex` 主定理标题已为 `Consolidated contradiction-field theorem` |
| 摘要/标题旧审查稿口径 | 已完成 | 标题为 `Consolidated Verification Manuscript`，摘要改为 verification-file 口径 |
| AEX 条件化措辞 | 已完成 | `docs/rh-u2-aex-acceptance-review.md`；主稿无 `conditional exactly` 残留 |
| EXT 外部输入定位 | 已完成 | `docs/rh-u3-ext-reference-table.md`；主稿 EXT 表接入正式 `\cite{...}` |
| LaTeX/BibTeX 编译 | 已完成 | `docs/rh-u5-final-compile-audit.md`；PDF 已生成 |
| Undefined refs/cites | 已完成 | 40 labels / 57 refs / 11 cites 全匹配；latexmk 日志无 undefined refs/cites |
| 版式警告 | 已完成 | 最新 `rh-contradiction-field.log` 无 overfull/underfull/error/warning 扫描项 |

## 2. 外部审稿/排版义务

| 项目 | 当前状态 | 是否可由当前作者侧直接闭合 |
|---|---|---|
| 专著页码级核验 | 章节/版本级已完成；页码级需最终排版核对纸书或出版社电子版 | 否，不能伪造未核验页码 |
| 独立逐行 referee verification | 主稿、证明包、controlled exits 已整理；仍需独立审稿人逐条验算 | 否，不能由作者自称完成 |
| `Submission warning` 删除 | 形式上只剩外部审稿/排版义务阻止删除 | 暂不删除，避免把验证稿误称最终无条件 RH 证明 |

## 3. 可审稿引用定位状态

- 文章级来源已有卷期页码：Vaaler 1985、Baker 2012、Vaughan 1977。
- arXiv 来源已有编号：Bourgain--Garaev 2012。
- 专著级来源已有版本/章节定位：Iwaniec--Kowalski Chapter 12 / Chapter 6；Katz Kloosterman sheaf chapters；Titchmarsh--Heath-Brown explicit formula/Perron--Mellin sections；Ingham Landau--Ingham oscillation input；Halberstam--Richert Selberg sieve chapters。
- 最终页码级引用应在期刊排版或 referee copyediting 阶段从实体书或授权电子版逐项核对。

## 4. 结论

作者侧可执行的最终审稿义务已经完成。当前唯一诚实保留项是外部独立审稿与排版核验，因此 `Submission warning` 应继续保留。若后续获得独立 referee verification 与页码核验清单，才可进入 U6：删除 warning 并改为最终无条件 RH 定理口径。
