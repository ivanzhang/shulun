# 最终闭合障碍与处理决策清单

日期：2026-04-28

## 1. 当前主线状态

本文当前主线采用硬窗口路线：

\[
USC/DBA+四点能量+离散coarea+DBA\text{-}closure
\Longrightarrow B.0.4^*
\Longrightarrow 行命题,
\]

列命题仍走高阈值列场 USC、一致集中、容量比较与坏列整数化。平滑 `B.0.4S/B.0.4S-short` 只保留为备选路线，不参与主线闭合。

## 2. 最后硬障碍

### 2.1 `B.0.4*` admissibility 核查

需要逐项确认附录 B 叶剥离产生的所有对象满足：

- `Q\le \log^{C_Q}P`；
- `b(a)` 在正常层是有限复杂度有理/CRT 可逆分片函数；
- `W(a)` 有统一有界变差或可分片为有界变差权；
- 非可逆分母、导数小、ramification、Jacobian 退化与步长共振均进入 `6.14` 六类坏层。

若某一项不满足 admissibility 且不落入坏层，则它是新的唯一剩余缺口。

### 2.2 `USC(log P)` 常数增长

需要把附录 A 的 connected cumulant 展开整理为正式引理，重点核查：

- `r≤c\log P` 下 Bell/Möbius 分区常数不爆炸；
- skeleton 计数与 tiny/near/far 三层 Rankin 账本可和；
- 中心化叶剥离在高模数 CRT 投影中只产生可吸收误差。

### 2.3 四点能量到 UAS 的逆推

需要确认四点能量异常确实反推短弧少根性失败，且所有退化四元组已经被：

- 对角/半对角计数；
- `4E-DISP`；
- 离散 coarea；
- `DBA-closure` 坏层矩阵

完整覆盖。

### 2.4 列方向坏列整数化

列命题的最终闭合需要把坏列期望/概率界严格转成坏列数 `<1`，并核对容量比较中 `e^{-γ}>2(1-α)` 的余量没有被对数损失吃掉。

### 2.5 显式阈值与有限验证

当前数值验证仅覆盖 `P≤1000`。若论文要声明“所有奇素数”，必须先从所有渐近估计中抽取显式 `P_*`，再运行：

```bash
python3 experiments/verify_finite_p_grid.py --max-p P_* --quiet
```

## 3. 未处理文件决策

### 3.1 应纳入证明稿的文件

- `docs/final-proof-draft.md`
- `docs/final-proof-review.md`
- `docs/final-closure-obstacles.md`

这些文件共同描述当前主线、审查结论与最后硬障碍。

### 3.2 暂不纳入主证明提交的文件

- `docs/rigid-patch-lemma-experiments.md`
- `experiments/rigid_patch_lemma_scan.py`
- 当前 134 个未跟踪 `experiments/*.py`

原因：这些文件多为探索性数值实验或长日志，其中 `docs/rigid-patch-lemma-experiments.md` 已达约 1.9 万行，更适合作为后续实验资料分批整理，不宜混入最终证明稿提交。

## 4. 下一步严写顺序

1. 以 `6.17` 为索引，逐项反查附录 B 中每个边界项的 `W(a),b(a),Q` 来源；
2. 对每个非 admissible 分片标注其进入 `6.14` 哪一类坏层；
3. 把 `USC(log P)` 的常数增长账本压缩成 5--7 个正式命题；
4. 对列方向补一张“坏列整数化与容量余量表”；
5. 最后抽取显式 `P_*` 并做有限验证。

## 5. 数学诚实声明

当前文稿已经把主线最终缺口压缩到有限清单审查：`B.0.4*` admissibility、`USC(log P)` 常数增长、四点能量退化覆盖、列坏列整数化与显式阈值。只有这些项目全部严写通过后，才能声明无条件完整证明闭合。


## 6. 本轮新推进：admissibility 与相消分层

已在 `docs/final-proof-draft.md` 的 `6.17.6--6.17.7` 增补核查：附录 B 生成的 `Q,b(a),W(a),N,Y` 均能映射到 `B.0.4*` 的 admissible sawtooth 接口；失败情形进入小筛剔除、低体积盒或 `DBA-closure` 坏层。

但该核查只说明接口无遗漏，不等于自动证明 sawtooth 相消。真正硬解析核心仍是 6.7--6.15 的 UAS/FNL、四点能量、离散 coarea 与 DBA-closure 链条。后续若要无条件闭合，应继续严写该链条，而不是再扩大实验或平滑素数权路线。


## 6.18 sawtooth 相消链条严写补充

新增 `6.18` 节把硬窗口 `B.0.4*` 的 sawtooth 相消拆成三段：`LV` 大 Fourier 值反推短弧集中，`AE` 短弧集中反推四点厚化能量异常，最后由四点 rank、离散 coarea 与 `DBA-closure` 排除异常。该节还把旧的 `FNL/NL => B.0.4S-short` 主线修正为 `FNL/NL => B.0.4*`，平滑素数权接口继续只作为备选路线。

当前最后审稿点进一步缩小为：加权 van der Corput 常数、短弧可分辨层数 `L` 的上界、以及 coarea/DBA 坏层覆盖是否无遗漏。
