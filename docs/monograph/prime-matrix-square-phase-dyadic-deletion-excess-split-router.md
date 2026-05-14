# Prime Matrix square-phase dyadic 删除过量分裂路由器

**状态：** `dyadic_deletion_excess_split_to_first_moment_or_overlap_pdec_open`

`DyadicNegativeSquarePhaseDeletionExcessPDEC` 已进一步原子化。在进入块 survivor set `S_z` 上，若 dyadic 块删除量超过独立模型，则不是无名过删：要么一阶命中负载 `H_B` 过高，给出线性 Fourier/PDEC；要么一阶负载正常但 union 仍过大，说明二阶及高阶重叠不足，给出pair-correlation/交叉相位 PDEC。两个出口尚未排斥。

```text
deletion_excess_split_closed=true
first_moment_route_identified=true
overlap_route_identified=true
dyadic_defect_excluded=false
row_column_unconditional_closed=false
```

## 1. 分裂对象

| object | formula | meaning |
| --- | --- | --- |
| `survivor_set` | `S_z={k: k survives all q<=z}` | 进入 dyadic 块前的条件样本空间。 |
| `block_union` | `U_B=\|{k in S_z: exists q in B, k=-P^2 mod q}\|` | 该 dyadic 块真实删除量。 |
| `first_moment` | `H_B=sum_{q in B} \|S_z cap {-P^2 mod q}\|` | 一阶命中负载；高于期望即线性相位 PDEC。 |
| `overlap` | `I_B=sum_{q1<q2 in B} \|S_z cap a_{q1} cap a_{q2}\|` | 二阶重叠；低于期望则是 pair-correlation 缺陷。 |
| `bonferroni_gate` | `U_B <= H_B, and U_B >= H_B-I_B` | 过删必须由一阶过载或二阶/高阶重叠异常承担。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `DyadicDeletionObjectsDefined` | `true` | `true` | 单块删除量、一阶负载和二阶重叠均已定义在同一进入块 survivor set 上。 | none |
| `DeletionExcessSplitClosed` | `true` | `true` | 若 union 删除超过独立模型，则必须是一阶负载过高，或重叠/高阶结构低于正常抵消。 | DyadicSquarePhaseFirstMomentLoadPDEC OR DyadicSquarePhaseOverlapDeficitOrPairCorrelationPDEC |
| `FirstMomentRouteIdentified` | `true` | `false` | 一阶过载等价于 S_z 对移动残基 -P^2 mod q 的平均命中过高，可 Fourier 化为线性 PDEC。 | DyadicSquarePhaseFirstMomentLoadPDEC |
| `OverlapRouteIdentified` | `true` | `false` | 若一阶正常但 union 过大，则多重命中重叠不足，形成 q1*q2 交叉相位 pair-correlation PDEC。 | DyadicSquarePhaseOverlapDeficitOrPairCorrelationPDEC |
| `DyadicDefectExcluded` | `false` | `false` | 尚未排除一阶过载与二阶重叠缺陷。 | exclude DyadicSquarePhaseFirstMomentLoadPDEC and DyadicSquarePhaseOverlapDeficitOrPairCorrelationPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | LDG dyadic 缺陷与 RFP reciprocal-floor 缺陷仍未全部排除。 | LDG dyadic split exclusions + RFP reciprocal-floor exclusion |

## 3. 下一步

- 先攻 `DyadicSquarePhaseFirstMomentLoadPDEC`：对 `sum_{q in B} |S_z cap {-P^2 mod q}|` 建立 Fourier/PDEC 上界。
- 并行保留 `DyadicSquarePhaseOverlapDeficitOrPairCorrelationPDEC`：若一阶正常但 union 过删，必须解释为 pair-correlation 缺陷。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-low-skeleton-quadratic-defect-router.json` | `1262152377e4b7477fef34bd370861bd1829bb06a3b964c19dc833db2cb2128d` |
| `docs/monograph/prime-matrix-square-phase-moving-cutoff-dyadic-defect-router.json` | `4515b50a029982ce414c9ef9b290c4dbf026bba67099c6048cb1979ced0891f6` |
| `experiments/prime_matrix_square_phase_dyadic_deletion_excess_split_router.py` | `cd7124356d0a9e3c61fd0964b9be2e84c8339672a10abe9d1716295440758cdc` |
