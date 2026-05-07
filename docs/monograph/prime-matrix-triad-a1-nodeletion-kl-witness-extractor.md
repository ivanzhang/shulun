# Triad-A1 NoDeletion-KL 见证提取器

**状态：** `nodeletion_kl_witness_extracted_terminal_open`

当前已物化层仍全部由 FiberDeletion 支付；但 KL 形状显示偏斜主要藏在旧相位-新增 residue 的互信息中，而不是全局 residue 投影峰。

## 1. 结构分解

对每层 fiber，条件 KL 满足 E_t KL(B|t||U_B)=KL(B||U_B)+I(T;B)。全局 residue KL 累计给 GlobalResiduePDEC；互信息累计给 refined (old_phase,residue) PDEC；二者在 NoDeletion 下同时趋零才进入 CleanKLS。

写成公式就是：

```text
H_cond = E_t KL(B|t || U_B)
       = KL(B || U_B) + I(T;B)。
```

因此：

```text
KL(B||U_B) 持久累计       => GlobalResiduePDEC；
I(T;B) 持久累计           => refined (old_phase,residue) PDEC；
二者在 NoDeletion 下趋零  => CleanKLS/DLS admission。
```

## 2. 参数

- `top_limit=6`。
- `nodeletion_survival=0.9`。
- `global_normalized_kl_pdec_threshold=0.1`。
- `mutual_normalized_kl_pdec_threshold=0.1`。
- `clean_normalized_kl_threshold=0.05`。
- `threshold_meaning=阈值只用于有限审计分流；正式链条使用 KL 链式分解和极限累计/趋零。`。

## 3. 汇总

- `row_count=6`。
- `gate_route_counts={'FiberDeletionCurrentLayer': 6}`。
- `shape_route_counts={'PhaseResidueMutualPDECWitness': 6}`。
- `current_nodeletion_triggered=False`。
- `max_global_residue_normalized_kl=0.0388557`。
- `max_global_residue_tv_to_uniform=0.186813`。
- `min_phase_residue_mutual_normalized_kl=0.4125`。
- `max_kl_chain_abs_error=0`。

## 4. 层级明细

| layer | P | survival | global norm KL | global TV | cond norm KL | mutual norm KL | gate | shape |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Q=2310->30030 | 17 | 0.0769231 | 0.0388557 | 0.186813 | 1 | 0.961144 | `FiberDeletionCurrentLayer` | `PhaseResidueMutualPDECWitness` |
| Q=2310->30030 | 19 | 0.202198 | 0.00892964 | 0.0983251 | 0.544977 | 0.536048 | `FiberDeletionCurrentLayer` | `PhaseResidueMutualPDECWitness` |
| Q=2310->30030 | 23 | 0.310345 | 0.00967229 | 0.0974893 | 0.434121 | 0.424449 | `FiberDeletionCurrentLayer` | `PhaseResidueMutualPDECWitness` |
| Q=2310->30030 | 29 | 0.312821 | 0.010607 | 0.0940917 | 0.423107 | 0.4125 | `FiberDeletionCurrentLayer` | `PhaseResidueMutualPDECWitness` |
| Q=30030->510510 | 19 | 0.0792839 | 0.00194873 | 0.0422201 | 0.725806 | 0.723858 | `FiberDeletionCurrentLayer` | `PhaseResidueMutualPDECWitness` |
| Q=30030->510510 | 23 | 0.162896 | 0.00218822 | 0.0458197 | 0.538513 | 0.536325 | `FiberDeletionCurrentLayer` | `PhaseResidueMutualPDECWitness` |

## 5. 代表性互信息原子

每行列出贡献最大的 `(old_phase,residue)` 原子。若这种原子族持久复现，就是 refined PDEC 输入。

| layer | P | old phase | residue | mass | within phase | residue share | lift/independent | mutual contrib |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Q=2310->30030 | 17 | 13 | 1 | 1 | 1 | 0.0357143 | 28 | 0.119007 |
| Q=2310->30030 | 17 | 964 | 9 | 1 | 1 | 0.0357143 | 28 | 0.119007 |
| Q=2310->30030 | 17 | 1347 | 3 | 1 | 1 | 0.0357143 | 28 | 0.119007 |
| Q=2310->30030 | 19 | 111 | 10 | 17 | 0.586207 | 0.0826613 | 7.09167 | 0.0671405 |
| Q=2310->30030 | 19 | 2200 | 2 | 17 | 0.586207 | 0.0826613 | 7.09167 | 0.0671405 |
| Q=2310->30030 | 19 | 962 | 11 | 17 | 0.586207 | 0.0866935 | 6.76183 | 0.065508 |
| Q=2310->30030 | 23 | 919 | 9 | 35 | 0.380435 | 0.0500579 | 7.5999 | 0.0205396 |
| Q=2310->30030 | 23 | 1392 | 3 | 35 | 0.380435 | 0.0500579 | 7.5999 | 0.0205396 |
| Q=2310->30030 | 23 | 152 | 7 | 35 | 0.380435 | 0.0601852 | 6.32107 | 0.0186736 |
| Q=2310->30030 | 29 | 1036 | 0 | 112 | 0.903226 | 0.0798005 | 11.3185 | 0.0423569 |
| Q=2310->30030 | 29 | 1275 | 12 | 112 | 0.903226 | 0.0798005 | 11.3185 | 0.0423569 |
| Q=2310->30030 | 29 | 228 | 5 | 112 | 0.282828 | 0.0586035 | 4.82613 | 0.0274771 |
| Q=30030->510510 | 19 | 111 | 8 | 1 | 1 | 0.0483871 | 20.6667 | 0.00610589 |
| Q=30030->510510 | 19 | 3051 | 8 | 1 | 1 | 0.0483871 | 20.6667 | 0.00610589 |
| Q=30030->510510 | 19 | 3239 | 8 | 1 | 1 | 0.0483871 | 20.6667 | 0.00610589 |
| Q=30030->510510 | 23 | 1602 | 15 | 19 | 0.542857 | 0.0486111 | 11.1673 | 0.0132659 |
| Q=30030->510510 | 23 | 28429 | 1 | 19 | 0.542857 | 0.0486111 | 11.1673 | 0.0132659 |
| Q=30030->510510 | 23 | 14664 | 5 | 19 | 0.542857 | 0.051794 | 10.4811 | 0.0129172 |

## 6. 读法

当前 `gate` 全部仍是 `FiberDeletionCurrentLayer`，所以不能把本报告当作 NoDeletion 反例闭合。
它的作用是把未来 `a_n->1` 时的 KL 硬点具体化：偏斜若不在全局 residue，就必在 `(old_phase,residue)` 互信息中登记。
