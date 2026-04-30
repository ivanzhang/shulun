# 最终符号交叉编号矩阵

本矩阵把当前审稿包中最后几组补强附录与主链入口逐项交叉编号。目标是把“仍需符号交叉编号”的义务转化为可审查清单。

## 1. D 组符号交叉编号

| 符号/对象 | 定义位置 | 展开位置 | 接入位置 | 状态 |
| --- | --- | --- | --- | --- |
| `(X,w), r` | `docs/d-structure-formal-appendix.md` §1 | `docs/d-structure-line-by-line-expansion.md` §1 | `docs/ab-to-d-interface-match.md` §1 | 已统一为剩余加权候选集合 |
| `φ, S(ξ)` | `docs/d-structure-formal-appendix.md` §1 | `docs/d-structure-line-by-line-expansion.md` §2 | `docs/m5-explicit-gap-lemma.md` §2 | 已统一为倒数相位 Fourier 和 |
| `𝓦(K)` | `docs/d-structure-formal-appendix.md` §1 | `docs/d-structure-line-by-line-expansion.md` §1 | `docs/m5-explicit-gap-lemma.md` §1 | 已统一为允许窗口族 |
| 短簇终端 | `docs/d-structure-formal-appendix.md` §1 | `docs/d-structure-line-by-line-expansion.md` §1, §4 | `docs/fct-tree-wfe-theoremization.md` §3 | 已作为合法终端 |
| 高投影增量 | `docs/d-structure-formal-appendix.md` §3 | `docs/d-structure-line-by-line-expansion.md` §2--§3 | `docs/constants-numbered-inequalities.md` I3/I5 | 已编号 |
| frequency-closure terminal | `docs/d-structure-formal-appendix.md` §6 | `docs/d-structure-line-by-line-expansion.md` §5 | `docs/fct-tree-wfe-theoremization.md` §3--§5 | 已编号 |
| NRC 背景 | `docs/nrc-theoremization.md` | `docs/d-structure-line-by-line-expansion.md` D13/D23 | `docs/ext-citation-final-audit.md` EXT-KL | 已外部引用化 |
| 能量上界 `E<=r` | `docs/d-structure-formal-appendix.md` §1 | `docs/d-structure-line-by-line-expansion.md` D15--D17 | `docs/ab-to-d-interface-match.md` M4 | 已闭合 |

## 2. M5 覆盖缺口交叉编号

| 项 | 定义/证明 | 主链来源 | 状态 |
| --- | --- | --- | --- |
| 剩余集合 `X` | `docs/ab-to-d-interface-match.md` §1 | A/B 三层剥离 | 已定义 |
| 零频基线 `B_0` | `docs/m5-explicit-gap-lemma.md` §1 | CRT 非零类均衡 | 已定义 |
| 覆盖缺口 `Gap=r-B_0` | `docs/m5-explicit-gap-lemma.md` §1 | 全覆盖需求减零频基线 | 已定义 |
| 缺口下界 `γr/log^2P` | `docs/m5-explicit-gap-lemma.md` §1, §4 | `A_star=2` 主缺口尺度 | 已编号到常数 I1 |
| Vaaler 截断 | `docs/m5-explicit-gap-lemma.md` M5.1 | `EXT-Vaaler` | 已引用 |
| 小偏差矛盾 | `docs/m5-explicit-gap-lemma.md` M5.2, M5+ | D 一阶偏差条件 | 已展开 |

## 3. BG/RKS 分区交叉编号

| 分区 | 证明位置 | 外部输入 | 参数账本 | 状态 |
| --- | --- | --- | --- | --- |
| RKS-1 短侧 Weil | `docs/bg-rks-block-match.md` Lemma RKS1 | `EXT-KL` | `A_weil_completion_log=4` | 已匹配 |
| RKS-2 BG 双线性 | `docs/bg-rks-block-match.md` Lemma RKS2 | `EXT-BG` | RKS 损失账本 | 已匹配，投稿需原文定理编号 |
| RKS-3 BG 多线性 | `docs/bg-rks-block-match.md` Lemma RKS3 | `EXT-BG` | RKS 损失账本 | 已匹配，投稿需原文定理编号 |
| RKS-4 低体积 | `docs/bg-rks-block-match.md` Lemma RKS4 | 平凡估计 | Tail-log4 余量 | 已匹配 |
| 总损失 | `docs/rks-parameter-audit.md` | `K_sieve_log_saving=128` | `74<128` | 已编号到 I2 |

## 4. 常数编号交叉编号

| 编号 | 文件 | 抽取器意义 | 状态 |
| --- | --- | --- | --- |
| I1 | `docs/constants-numbered-inequalities.md` | `tail_error_power>A_star` | 已复核 |
| I2 | `docs/constants-numbered-inequalities.md` | RKS 损失小于筛节省 | 已复核 |
| I3 | `docs/constants-numbered-inequalities.md` | D 组结构损失小于筛节省 | 已复核 |
| I4 | `docs/constants-numbered-inequalities.md` | Weil 完成法损失可吸收 | 已复核 |
| I5 | `docs/constants-numbered-inequalities.md` | OMR/CGTP 安全幂余量 | 已复核 |
| I6 | `docs/constants-numbered-inequalities.md` | 理论与有限验证重叠 | 已复核 |
| I7 | `docs/constants-numbered-inequalities.md` | 抽取器一致性 | 已复核 |

## 5. 外部定理编号状态

| EXT | 审稿包定位 | 当前状态 | 投稿前动作 |
| --- | --- | --- | --- |
| EXT-KL | `docs/ext-citation-final-audit.md` §1 | 书籍章节已定位 | 可补具体定理号/页码 |
| EXT-BG | `docs/ext-citation-final-audit.md` §2, `docs/bg-rks-block-match.md` | 论文与分区用途已定位 | 需按 BG 原文标注定理名/编号 |
| EXT-Vaaler | `docs/ext-citation-final-audit.md` §3 | 论文条目已定位 | 可补页码 |
| EXT-Selberg | `docs/ext-citation-final-audit.md` §4 | 书籍来源已定位 | 可补章节定理号 |
| EXT-Vaughan | `docs/ext-citation-final-audit.md` §5 | 原文条目已定位 | 可补页码 |

## 6. 交叉编号结论

当前审稿包的内部符号交叉编号已形成可审查矩阵。剩余的“外部定理编号”不再是数学结构缺口，而是投稿排版层面的原文定理号/页码标注工作；若审稿要求完全显式外部常数，则仍需另行抽取 BG/Baker 的数值常数。
