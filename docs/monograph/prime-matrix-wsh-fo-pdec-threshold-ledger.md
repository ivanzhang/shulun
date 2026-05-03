# FO-PDEC 显式 Fourier 阈值账本

**状态：** `finite_fo_pdec_fourier_threshold_ledger_not_global_proof`

本文档直接计算每个解释因子投影上的非零 Fourier 最大值。该值是同一坏窗方程集合已经产生的显式 `PDEC` 下界；剩余任务是证明同一投影的 `U_CRT` 上界严格小于该阈值。

## 摘要

- 分组数：`19`。
- 全局方程数：`43`。
- 全局最佳因子：`{'best_frequency': 95, 'max_fourier': 3.959247567099438, 'support_pdec_lower_bound': 0.16288018964317724, 'total_count': 4, 'support_size': 3, 'top_residues': [{'residue': 40, 'load': 2}, {'residue': 126, 'load': 1}, {'residue': 61, 'load': 1}], 'factor': 199}`。
- 最大分组 Fourier 阈值：`3.959247567099438`。
- 最小分组最佳 Fourier 阈值：`1.0`。
- 最大支撑型 PDEC 下界：`0.45883146774112354`。

## 分组最佳阈值

| group | equations | factors | best ell | best h | max Fourier | support lower | support | top residues |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| block:1 | 13 | 13 | 17 | 1 | 1.000000 | 0.242536 | 1 | [{'residue': 3, 'load': 1}] |
| block:2 | 9 | 9 | 19 | 1 | 1.000000 | 0.229416 | 1 | [{'residue': 2, 'load': 1}] |
| block:3 | 9 | 9 | 19 | 1 | 1.000000 | 0.229416 | 1 | [{'residue': 13, 'load': 1}] |
| block:4 | 12 | 12 | 19 | 1 | 1.000000 | 0.229416 | 1 | [{'residue': 18, 'load': 1}] |
| global | 43 | 21 | 199 | 95 | 3.959248 | 0.162880 | 3 | [{'residue': 40, 'load': 2}, {'residue': 126, 'load': 1}, {'residue': 61, 'load': 1}] |
| matrix-row:q1993:r836 | 25 | 18 | 19 | 1 | 2.000000 | 0.458831 | 1 | [{'residue': 18, 'load': 2}] |
| matrix-row:q773:r325 | 9 | 9 | 19 | 1 | 1.000000 | 0.229416 | 1 | [{'residue': 2, 'load': 1}] |
| matrix-row:q967:r260 | 9 | 9 | 19 | 1 | 1.000000 | 0.229416 | 1 | [{'residue': 13, 'load': 1}] |
| offset-row:1 | 3 | 3 | 19 | 1 | 1.000000 | 0.229416 | 1 | [{'residue': 18, 'load': 1}] |
| offset-row:10 | 2 | 2 | 29 | 1 | 1.000000 | 0.185695 | 1 | [{'residue': 24, 'load': 1}] |
| offset-row:11 | 5 | 5 | 31 | 1 | 1.000000 | 0.179605 | 1 | [{'residue': 30, 'load': 1}] |
| offset-row:2 | 6 | 6 | 17 | 1 | 1.000000 | 0.242536 | 1 | [{'residue': 3, 'load': 1}] |
| offset-row:3 | 4 | 4 | 23 | 1 | 1.000000 | 0.208514 | 1 | [{'residue': 8, 'load': 1}] |
| offset-row:4 | 3 | 3 | 19 | 1 | 1.000000 | 0.229416 | 1 | [{'residue': 2, 'load': 1}] |
| offset-row:5 | 6 | 6 | 29 | 1 | 1.000000 | 0.185695 | 1 | [{'residue': 6, 'load': 1}] |
| offset-row:6 | 3 | 3 | 19 | 1 | 1.000000 | 0.229416 | 1 | [{'residue': 13, 'load': 1}] |
| offset-row:7 | 6 | 6 | 29 | 1 | 1.000000 | 0.185695 | 1 | [{'residue': 28, 'load': 1}] |
| offset-row:8 | 2 | 2 | 19 | 1 | 1.000000 | 0.229416 | 1 | [{'residue': 18, 'load': 1}] |
| offset-row:9 | 3 | 3 | 83 | 1 | 1.000000 | 0.109764 | 1 | [{'residue': 6, 'load': 1}] |

## 审稿解释

对每个固定因子 `ell`，相位计数向量 `g_ell` 的非零 Fourier 最大模是直接可核验的 `PDEC` 下界。若能从 CRT 结构约束、端点镜像、列容量、尾锚非复用或 SAE 排除中证明同一 `g_ell` 的上界 `U_CRT` 小于该值，则该投影闭合。

本账本没有证明 `U_CRT`。它把下一硬点精确为：为最佳投影给出同一坏窗集合上的 `U_CRT` 上界，而不是继续改变命题或扩大有限样本。
