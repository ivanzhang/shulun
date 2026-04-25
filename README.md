# 数论 · 讨论与论文归档

本仓库用于记录一系列数论讨论、猜想提炼、定理证明与论文草稿的演化过程。

## 当前内容

| 文件 | 说明 |
|---|---|
| [`docs/prime-density-waves.md`](docs/prime-density-waves.md) | 素数密度波：CRT 周期场中的原始阶乘邻域定理（由"$15$ 附近四胞胎"与"$30$ 附近合数墙"观察提炼） |
| [`docs/prime-density-waves-II.md`](docs/prime-density-waves-II.md) | 素数密度波 II：$k=3,4,5,6$ 的完整数据清单 + 相位唯一性定理（定理 D、E，证明"这种短区间只能在 $Q_k$、$P_k^\#$ 位置出现"） |
| [`docs/prime-density-waves-III.md`](docs/prime-density-waves-III.md) | 素数密度波 III：CRT 构造性方案。算法 A（最大密度构造）、B（最大间隙构造）、C（给定素数 $p$ 附近的局部最优定位），与 Cramér / RH 的距离评估 |
| [`docs/prime-density-waves-IV.md`](docs/prime-density-waves-IV.md) | 素数密度波 IV：反向问题与结构-构造鸿沟。合数段 ⟺ CRT 覆盖系统的形式对应；容量定理与 Mertens 双面性；**证明 CRT 方法原则上不能推出 Cramér 上界**；通过 Hardy–Littlewood 奇异级数寻找跨鸿沟路径 |
| [`docs/prime-density-waves-V.md`](docs/prime-density-waves-V.md) | 素数密度波 V：字符谱分解与 $L$ 函数零点对偶。**定理 27.1（节点完美枚举）**：节点候选集 $\mathcal{S}(Q_k, M/2)$ 在 $(\mathbb{Z}/M)^\times$ 上双射；**定理 29.1（节点-零点对偶）**：密度波分解为几何因子 $T_\chi$ 与算术因子 $\sum_\rho x^\rho/\rho$；**定理 30.2（对称消除）**：$\Lambda = M/2$ 时非主字符贡献精确抵消 |
| [`docs/prime-density-waves-VI.md`](docs/prime-density-waves-VI.md) | 素数密度波 VI：P×P 方阵假设与 Cramér–GRH 的条件蕴含图谱。**定理 36.5**：H₃ ⟺ Cramér + 均匀短 AP（方阵假设 = Cramér + Linnik 的双向打包）；**定理 37.2**：H 的谱等价为 $F(a) \geq -(M_0 - 1)$（只给负向下界）；**定理 37.4**：H 与 GRH 互不蕴含（独立轴）；实测 $P=101$ 振幅 $\leq 5$ vs GRH 允许 $\sim 440$ |
| [`docs/prime-density-waves-VII.md`](docs/prime-density-waves-VII.md) | 素数密度波 VII（终）：从 $H_{P>5}$ 公理到 Cramér–GRH 的条件演绎链。**定理 43.1**：$H_{P>5}\Rightarrow g(x)\leq 7$；**推论 43.2**：$H_{P>5}\Rightarrow$ Cramér（平凡蕴含）；**定理 46.1**：$H_{P>5}$ 为假（反例 $N=113,P=7$：行 $[114,120]$ 全合）；**定理 47.3**：合理修正 $H^*_{(\log N)^2}\iff$ Cramér + 均匀 Linnik；**定理 47.4**：$H^*_f$ 下零点无零点区 $\beta < 1-c/(\log Q)^\alpha$ |

## 工作约定

- 每个独立主题开一个 `docs/<主题>.md` 或 `docs/<主题>/` 目录。
- 数学公式用 LaTeX 语法 + Markdown 渲染。
- 每次重要的讨论阶段后用 `git commit` 记录；提交信息简述该轮的核心结论或修改点。
- 长公式与推导单独成段，便于 diff 阅读。
