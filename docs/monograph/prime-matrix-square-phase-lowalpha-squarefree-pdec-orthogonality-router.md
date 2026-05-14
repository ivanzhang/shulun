# Prime Matrix square-phase low-alpha squarefree PDEC 正交路由

**状态：** `coefficient_remainder_inner_product_identity_closed_angle_bound_open`

跨模数正负配对不应按贪心边证明，而应回到 Selberg 余项的真实代数对象：`Q_direct-Q_model=<c,R>`，其中 `c_m` 是二次型 lcm 系数，`R_m=A_m-N/m` 是 squarefree 低模余项向量。本步闭合内积恒等式和 Cauchy 包络，并显示样本净余项对应很小夹角；全局剩余是证明这种系数-余项近正交，或把大夹角命名为 VectorSquarefree-PDEC 并排斥。

```text
coefficient_remainder_inner_product_identity_closed=true
cauchy_vector_envelope_closed=true
sample_small_angle_observed=true
coefficient_remainder_orthogonality_angle_bound_proved=false
vector_squarefree_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 正交账本

| z | moduli | packets | net | abs | cauchy | net/cauchy | abs/cauchy | threshold signed | subthreshold correction |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 7 | 16 | 4 | -17.369282 | 262.296524 | 352.451999 | 0.049281 | 0.744205 | -16.596104 | -0.773178 |
| 13 | 64 | 8 | -15.038287 | 651.410806 | 908.950054 | 0.016545 | 0.716663 | -29.637369 | 14.599083 |
| 31 | 1116 | 16 | 16.031115 | 1867.716185 | 3133.330619 | 0.005116 | 0.596080 | 16.700129 | -0.669014 |
| 61 | 5726 | 19 | 5.883923 | 3211.751427 | 5404.798742 | 0.001089 | 0.594241 | -45.434731 | 51.318654 |

## 2. 证明边界

- 已闭合：`Q_direct-Q_model=<c,R>` 的内积恒等式。
- 已闭合：`|<c,R>|<=||c||_2 ||R||_2` 的向量包络。
- 已校正：阈值包 residual 还会被 subthreshold 包继续修正，因此单独研究阈值配对不够。
- 未闭合：全局证明 `c` 与 `R` 的夹角足够小，或证明大夹角会形成可排斥的 VectorSquarefree-PDEC。
- 下一目标：`CoefficientRemainderOrthogonalityAngleBoundOrVectorSquarefreePDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json` | `0d1bdccce7bb03e1110bbd6a937b914c354c1d365d403abde42be12aebf9cba2` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-squarefree-pdec-pairing-ledger-router.json` | `feb8f96e8356e5e71feefa79f80d272067765bc20b68d83a6ea130b409931cc7` |
| `experiments/prime_matrix_square_phase_lowalpha_squarefree_pdec_orthogonality_router.py` | `4dc7bfa155cb792ea1ebfd58a9988127f870f9acd52d772fac0d76be9127da62` |
