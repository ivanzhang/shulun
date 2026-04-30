# 审稿版引用与附录入口

本文件是审稿版论文的附录入口，只收录最终主链相关材料。大量历史探索稿不作为审稿入口。

## A. 主证明入口

- `docs/final-archive-report.md`：最终归档报告。
- `docs/critical-bucket-single-hit-sieve-attack.md`：主文档；最终主链以第 1273--1275 节为准。
- `docs/final-interface-index.md`：最终接口索引与一致性口径。
- `docs/formal-theoremization-review.md`：最终定理化总览。
- `docs/top-journal-proof-audit.md`：顶刊审稿级复核清单。

## B. 行列归约附录

- `docs/row-column-reduction-formal-appendix.md`：A/B 行列反例到 Structured-EHPD 的正式归约附录证明稿。
- `docs/row-column-reduction-theoremization.md`：A/B 行列反例到 Structured-EHPD 的短定理化历史入口。

## C. Tail-log4 附录

- `docs/tail-log4-formal-appendix.md`：Tail-log4 正式附录证明稿。
- `docs/tail-log4-theoremization.md`：TL4-L/TL4-S/TL4-M 主体定理化。
- `docs/rks-log-reference-audit.md`：RKS-log 与 Bourgain--Garaev 文献的引用匹配审查。
- `docs/rks-bridge-partition.md`：RKS-bridge Type I/II 长度分区。
- `docs/rks-parameter-audit.md`：RKS 对数损失账本，合计 `74<128`。

## D. Structured-EHPD / OMR 附录

- `docs/omr-cgtp-lsmp-theoremization.md`：OMR/CGTP/LSMP 结构包定理化。
- `docs/nrc-theoremization.md`：NRC 非共振完成和定理化。
- `docs/fct-tree-wfe-theoremization.md`：FCT/Tree-WFE 频率碰撞终端定理化。

## E. 显式常数与证书附录

- `docs/explicit-p0-constants.status.md`：显式常数状态，最终口径见第 90--97 节。
- `docs/explicit-p0-constants.structured-conservative.json`：保守结构常数包。
- `docs/explicit-p0-structured-conservative-result.json`：理论阈值抽取证书，`log_P0_upper=3.5`。
- `docs/finite-verify-exp5.json`：有限验证证书，`P<=floor(exp(5))=148` 全部通过。
- `experiments/extract_p0.py`：阈值抽取脚本。
- `experiments/verify_small_prime_square.py`：有限验证脚本。

## F. 外部引用待最终格式化

统一 bibliography 草稿见 `docs/bibliography.md`。

当前已核验的关键外部来源：

- Bourgain--Garaev 型文献：arXiv:1211.4184，*Sumsets of reciprocals in prime fields and multilinear Kloosterman sums*，用于 BG 多线性/双线性倒数 Kloosterman 输入的引用匹配。
- 标准 Weil/Kloosterman 完成和界：用于 NRC 与短侧 Weil 吸收。
- Selberg 二维线性上筛：用于 TL4-M。
- Vaaler/Beurling--Selberg 截断：用于 TL4-L/TL4-S。

最终投稿版应把这些来源转成正式 bibliography，并在对应附录中逐一定理编号引用。
