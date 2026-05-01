# 合著论著命题状态总表

本文给出合著论著 `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 的命题状态。状态必须诚实区分：已在文稿中证明、已归约、外部输入、计算证书、仍需独立审稿。

| 模块 | 命题/输入 | 当前状态 | 主要证据 | 是否可称无条件终稿 |
|---|---|---|---|---|
| Prime Matrix A/B | 行/列反例归约到 Structured-EHPD | 已归约 | `docs/row-column-reduction-formal-appendix.md` | 否，仍依赖 D 组排斥 |
| Prime Matrix D | Structured-EHPD 排斥 | 审稿包/需逐行复核 | `docs/final-top-journal-unconditional-review.md` | 否 |
| Prime Matrix finite | 小素数有限验证 | 计算证书 | `docs/finite-verify-exp5.json` 等 | 仅覆盖有限段 |
| RH PC1/PC2 | 离线零点到素数异常与 CRT baseline | 主稿编号化 | `paper/rh-proof/rh-contradiction-field.tex` | 需 referee verification |
| RH C4/C5/C6/C9 | sparse/dense/no-cycle/tail | 主稿编号化 | `paper/rh-proof/rh-contradiction-field.tex` | 需 referee verification |
| RH AEX/GEE | analytic exits 与 global exit exclusion | 主稿合成，审稿包完成 | `docs/rh-final-referee-obligations-closure.md` | 需 referee verification |
| RH EXT | 外部解析输入 | 章节/论文级定位完成 | `docs/rh-u3-ext-reference-table.md` | 专著页码仍需 copyediting |
| RH U5 | LaTeX/PDF/BibTeX | 已完成 | `docs/rh-u5-final-compile-audit.md` | 工程项完成 |

## 结论

合著论著当前应标为“contradiction-field synthesis and verification manuscript”。不得标为“RH 与方阵行列命题的最终无条件证明”。

## 审稿闭合更新

新增 `docs/monograph/referee-review-and-closure-audit.md`。合著论著当前已经闭合的是“审稿结构、依赖边界、状态标注和统一矛盾场方法”；尚未闭合的是“RH 与方阵行列命题作为最终无条件定理”。后者必须等待 Prime Matrix D 组排斥与 RH controlled exits 的独立逐行 referee verification。


## 内部逐行复核更新

新增 `docs/monograph/line-by-line-internal-referee-matrix.md`。作者侧逐行复核未发现新的 `BLOCK-MATH`，但 Prime Matrix 终局与 RH 终局仍为 `BLOCK-REFEREE`：必须由独立审稿接受 D-structure/Tail-log4/finite 接口与 RH controlled exits 后，才可升级为最终无条件定理。
