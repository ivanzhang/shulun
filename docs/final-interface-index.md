# 最终接口索引与一致性口径

本文件统一当前归档稿的最终证明接口，避免主文档历史探索段中的“候选/剩余/下一步”表述造成误读。

## 1. 最终阅读入口

审稿阅读顺序应为：

1. `docs/final-submission-manifest.md`：归档文件与证书；
2. `docs/references-and-appendices.md`：审稿版引用与附录入口；
3. `docs/bibliography.md`：统一参考文献标签；
4. `docs/formal-theoremization-review.md`：最终定理化总览；
5. `docs/row-column-reduction-formal-appendix.md`：A/B 行列归约正式附录；
6. `docs/tail-log4-theoremization.md`：C Tail-log4；
7. `docs/d-structure-formal-appendix.md`：D 结构包正式附录；
8. `docs/nrc-theoremization.md` 与 `docs/fct-tree-wfe-theoremization.md`：D 的剩余子接口；
9. `docs/explicit-p0-constants.status.md` 第 90--97 节：显式阈值与有限验证状态。

主文档 `docs/critical-bucket-single-hit-sieve-attack.md` 的早期章节保留探索历史；若与上述文件冲突，以上述最终接口文件为准。

## 2. A--D 当前状态

| 接口 | 文件 | 当前状态 | 剩余审稿义务 |
| --- | --- | --- | --- |
| A Column-Closure 归约 | `docs/row-column-reduction-formal-appendix.md` | 已形成正式归约附录稿 | 与 D 组 Structured-EHPD 定义逐项匹配 |
| B Row-Closure 归约 | `docs/row-column-reduction-formal-appendix.md` | 已形成正式归约附录稿 | 与 D 组 Structured-EHPD 定义逐项匹配 |
| C Tail-log4 | `docs/tail-log4-formal-appendix.md`, `docs/tail-log4-theoremization.md`, `docs/rks-parameter-audit.md` | 已形成正式附录证明稿 | 最终期刊引用格式化 |
| D OMR/CGTP/LSMP | `docs/d-structure-formal-appendix.md` | 已形成正式附录证明稿 | A/B 坏配置标准形式与 D 五项定义逐项匹配 |
| NRC | `docs/nrc-theoremization.md` | 已用完成法 + Weil/Kloosterman 定理化 | 核对允许窗口展开复杂度 |
| FCT/Tree-WFE | `docs/fct-tree-wfe-theoremization.md` | 已定理化为 span 计数与树容量账本 | 核对 frequency-closure terminal 与主命题终端一致 |

## 3. 机械证书状态

- 理论抽取：`docs/explicit-p0-structured-conservative-result.json`，`log_P0_upper=3.5`。
- 有限验证：`docs/finite-verify-exp5.json`，`P<=floor(exp(5))=148` 的 33 个奇素数全部通过。
- 覆盖关系：`exp(3.5)<exp(5)`，两段重叠覆盖全部奇素数。

## 4. 禁止误读

- `experiments/extract_p0.py` 只组合已证明的常数输入，不证明解析估计本身。
- 早期章节中的“行命题未闭合”“下一步硬点”等是历史探索记录，不是最终接口状态。
- 当前稿件不宣称理论入口已降到 `P=5`；全部奇素数成立依赖理论段 `P>exp(3.5)` 与有限验证段 `P<=exp(5)` 的重叠。
- 若要达到顶级期刊完全无条件版本，需把表中“剩余审稿义务”逐项核对到可引用定理或附录证明。
