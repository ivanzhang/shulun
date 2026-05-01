# BV-E2 自足化义务审查（2026-05-01）

## 本轮结论

BMD 已经归约到 BV-E2。引用标准 BV-E2 时，BMD 误差闭合；若要求论文完全自足，则唯一真正深点是 `BE2-3`。

## 关键发现

普通乘法大筛不能闭合 BV-E2。

在平衡块

`p~P`, `m~P`, `Q~P/log^B P`

中，Cauchy 加大筛只给

`P^3/log^{2B} P`，

而目标误差是

`P^2/log^A P`。

差一个 `P` 量级。因此不能把“由大筛”写成证明。

## 最小剩余硬点

`BE2-3`：对平衡双线性卷积

`sum_{rs=a mod d} alpha_r beta_s`

在

`Q<=N^{1/2}/log^B N`

范围内证明 Bombieri--Vinogradov 平均误差。

该步骤需要 dispersion / Kloosterman cancellation / Type-II 均值定理。

## 文稿更新

- 新增 `docs/monograph/bv-e2-appendix.md`
- `docs/monograph/two-point-secondary-sieve-research.md` 新增第 432--435 节
- `docs/monograph/claim-status-table.md` 新增 BV-E2 自足化状态
- `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 新增自足化义务 remark

## 下一步

若继续无黑箱化，应直接专攻 `BE2-3`。若允许标准外部输入，应在最终参考文献中加入 Bombieri--Friedlander--Iwaniec/Motohashi 型 dispersion 来源，并把 BMD 标为“外部输入闭合”。
