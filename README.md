# 数论 · 讨论与论文归档

本仓库用于记录一系列数论讨论、猜想提炼、定理证明与论文草稿的演化过程。

## 当前内容

| 文件 | 说明 |
|---|---|
| [`docs/prime-density-waves.md`](docs/prime-density-waves.md) | 素数密度波：CRT 周期场中的原始阶乘邻域定理（由"$15$ 附近四胞胎"与"$30$ 附近合数墙"观察提炼） |
| [`docs/prime-density-waves-II.md`](docs/prime-density-waves-II.md) | 素数密度波 II：$k=3,4,5,6$ 的完整数据清单 + 相位唯一性定理（定理 D、E，证明"这种短区间只能在 $Q_k$、$P_k^\#$ 位置出现"） |
| [`docs/prime-density-waves-III.md`](docs/prime-density-waves-III.md) | 素数密度波 III：CRT 构造性方案。算法 A（最大密度构造）、B（最大间隙构造）、C（给定素数 $p$ 附近的局部最优定位），与 Cramér / RH 的距离评估 |

## 工作约定

- 每个独立主题开一个 `docs/<主题>.md` 或 `docs/<主题>/` 目录。
- 数学公式用 LaTeX 语法 + Markdown 渲染。
- 每次重要的讨论阶段后用 `git commit` 记录；提交信息简述该轮的核心结论或修改点。
- 长公式与推导单独成段，便于 diff 阅读。
