# FO-PDEC cross-q 坐标图重叠审计

**状态：** `cross_q_coordinate_persistence_blocked_not_global_proof`

当前 FO-PDEC 的全部 cross-q reuses 都是同一物理候选在重叠 q-row 坐标图中的表示。两层行起点与列号满足 base_gap + column_gap = 0，候选、semiprime、offset 与解释因子相同。因此它们不能作为独立 coordinate persistence 计入同一 PDEC 下界；必须物理去重，或提交新的 非重叠 cross-q persistence theorem。

## 1. 子门裁定

```text
closed_subgate: CrossQCoordinatePersistenceRejectedForAuditedFO-PDEC
cross_level_reuse_count: 9
all_cross_level_reuses_chart_overlap_blocked: true
factor_199_cross_level_reuse_blocked: true
```

## 2. 逐复用审计

| candidate | factor | q layers | residues | base gaps | column gaps | status |
| ---: | ---: | --- | --- | --- | --- | --- |
| 250477 | 19 | [773, 967] | [[773, 2], [967, 13]] | [1] | [-1] | blocked_as_independent_coordinate_persistence |
| 250507 | 397 | [773, 967] | [[773, 325], [967, 260]] | [1] | [-1] | blocked_as_independent_coordinate_persistence |
| 250507 | 631 | [773, 967] | [[773, 325], [967, 260]] | [1] | [-1] | blocked_as_independent_coordinate_persistence |
| 250511 | 31 | [773, 967] | [[773, 15], [967, 12]] | [1] | [-1] | blocked_as_independent_coordinate_persistence |
| 250513 | 67 | [773, 967] | [[773, 57], [967, 59]] | [1] | [-1] | blocked_as_independent_coordinate_persistence |
| 250531 | 29 | [773, 967] | [[773, 6], [967, 28]] | [1] | [-1] | blocked_as_independent_coordinate_persistence |
| 250531 | 53 | [773, 967] | [[773, 7], [967, 48]] | [1] | [-1] | blocked_as_independent_coordinate_persistence |
| 250531 | 163 | [773, 967] | [[773, 162], [967, 97]] | [1] | [-1] | blocked_as_independent_coordinate_persistence |
| 250541 | 199 | [773, 967] | [[773, 126], [967, 61]] | [1] | [-1] | blocked_as_independent_coordinate_persistence |

## 3. 证明读法

同一物理整数 `n` 在两个宽度为 `q_1,q_2` 的行坐标中写成

\[
n=(r_1-1)q_1+c_1=(r_2-1)q_2+c_2。
\]

若 `(r_2-1)q_2-(r_1-1)q_1 = -(c_2-c_1)`，则两个坐标只是同一整数的图变换。当前全部跨 `q` 复用均满足这个恒等式，并且物理候选、半素数核心、offset 与解释因子相同。

所以这类复用不能同时提供两个独立 PDEC 事件。若要把它们合并成 coordinate-cap 阈值，必须额外证明非坐标图意义上的 cross-q persistence；当前样本没有这种结构。

## 4. 剩余

- `physical/primitive PDEC threshold U_CRT < 1.9997507790353146`
- `SAE/Endpoint absorption for physical cross-chart reuses`
- `future non-overlap cross-q persistence theorem, if a non-chart-overlap family appears`
