# 最终接口索引与一致性口径

本文件统一当前归档稿的最终证明接口，避免主文档历史探索段中的“候选/剩余/下一步”表述造成误读。

## 1. 最终阅读入口

审稿阅读顺序应为：

1. `docs/final-submission-manifest.md`：归档文件与证书；
2. `docs/formal-theoremization-review.md`：最终定理化总览；
3. `docs/row-column-reduction-theoremization.md`：A/B 行列归约；
4. `docs/tail-log4-theoremization.md`：C Tail-log4；
5. `docs/omr-cgtp-lsmp-theoremization.md`：D 结构包；
6. `docs/nrc-theoremization.md` 与 `docs/fct-tree-wfe-theoremization.md`：D 的剩余子接口；
7. `docs/explicit-p0-constants.status.md` 第 90--97 节：显式阈值与有限验证状态。

主文档 `docs/critical-bucket-single-hit-sieve-attack.md` 的早期章节保留探索历史；若与上述文件冲突，以上述最终接口文件为准。

## 2. A--D 当前状态

| 接口 | 文件 | 当前状态 | 剩余审稿义务 |
| --- | --- | --- | --- |
| A Column-Closure 归约 | `docs/row-column-reduction-theoremization.md` | 已短定理化 | 核对三层分解不重不漏 |
| B Row-Closure 归约 | `docs/row-column-reduction-theoremization.md` | 已短定理化 | 核对 45 度锁定只进入小因子层 |
| C Tail-log4 | `docs/tail-log4-theoremization.md`, `docs/rks-log-reference-audit.md`, `docs/rks-bridge-partition.md` | 已拆成 TL4-L/S/M | RKS-bridge-minor 近极端不平衡块 |
| D OMR/CGTP/LSMP | `docs/omr-cgtp-lsmp-theoremization.md` | 已拆成 OMR/CGTP/LSMP/NRC/FCT | 统一符号与常数，核对 Tree-WFE 终端定义 |
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
