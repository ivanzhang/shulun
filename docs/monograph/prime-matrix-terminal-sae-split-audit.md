# Terminal-SAE 分层骨架/尾命中审计

**状态：** `experimental_terminal_sae_split_certificate_not_a_proof`

## 参数

- `max_p`: `1000`
- `y_ratio`: `0.36787944117144233`

## 总结

- 检查奇素数个数：`167`。
- 分层不等式认证全部行的记录数：`167`。
- `p>=7` 未认证记录数：`0`。
- `p>=7` 最小 margin：`1`。
- `p>=19` 最小 margin：`1`。

## 最小 margin 样本

| p | q | y | min margin | min data | certified |
| ---: | ---: | ---: | ---: | --- | --- |
| 3 | 5 | 2 | 1 | {'h': 1, 'skeleton': 2, 'tail_incidence': 1, 'margin': 1} | True |
| 5 | 7 | 2 | 1 | {'h': 1, 'skeleton': 3, 'tail_incidence': 2, 'margin': 1} | True |
| 7 | 11 | 2 | 1 | {'h': 1, 'skeleton': 5, 'tail_incidence': 4, 'margin': 1} | True |
| 11 | 13 | 4 | 1 | {'h': 4, 'skeleton': 4, 'tail_incidence': 3, 'margin': 1} | True |
| 13 | 17 | 4 | 1 | {'h': 5, 'skeleton': 6, 'tail_incidence': 5, 'margin': 1} | True |
| 17 | 19 | 6 | 1 | {'h': 4, 'skeleton': 5, 'tail_incidence': 4, 'margin': 1} | True |
| 19 | 23 | 6 | 1 | {'h': 9, 'skeleton': 6, 'tail_incidence': 5, 'margin': 1} | True |
| 23 | 29 | 8 | 1 | {'h': 29, 'skeleton': 6, 'tail_incidence': 5, 'margin': 1} | True |
| 29 | 31 | 10 | 1 | {'h': 31, 'skeleton': 7, 'tail_incidence': 6, 'margin': 1} | True |
| 31 | 37 | 11 | 1 | {'h': 37, 'skeleton': 7, 'tail_incidence': 6, 'margin': 1} | True |
| 37 | 41 | 13 | 1 | {'h': 41, 'skeleton': 7, 'tail_incidence': 6, 'margin': 1} | True |
| 41 | 43 | 15 | 1 | {'h': 43, 'skeleton': 8, 'tail_incidence': 7, 'margin': 1} | True |
| 43 | 47 | 15 | 1 | {'h': 47, 'skeleton': 9, 'tail_incidence': 8, 'margin': 1} | True |
| 47 | 53 | 17 | 1 | {'h': 53, 'skeleton': 9, 'tail_incidence': 8, 'margin': 1} | True |
| 53 | 59 | 19 | 1 | {'h': 59, 'skeleton': 9, 'tail_incidence': 8, 'margin': 1} | True |
| 59 | 61 | 21 | 1 | {'h': 61, 'skeleton': 10, 'tail_incidence': 9, 'margin': 1} | True |
| 61 | 67 | 22 | 1 | {'h': 67, 'skeleton': 11, 'tail_incidence': 10, 'margin': 1} | True |
| 67 | 71 | 24 | 1 | {'h': 71, 'skeleton': 11, 'tail_incidence': 10, 'margin': 1} | True |
| 71 | 73 | 26 | 1 | {'h': 73, 'skeleton': 12, 'tail_incidence': 11, 'margin': 1} | True |
| 73 | 79 | 26 | 1 | {'h': 79, 'skeleton': 13, 'tail_incidence': 12, 'margin': 1} | True |

## 审稿解释

设 `G_y(h)` 为终端镜像块中避开所有 `ell<=y` 指定类的骨架点数，`T_y(h)` 为这些骨架点被 `y<ell<=p` 指定类命中的总重数。若 `G_y(h)>T_y(h)`，则尾素数不可能覆盖全部骨架点，因而该行存在旧 `p`-筛幸存者。

本脚本已排除 `m=0` 与 `m=q^2-1`，即排除 `n=q^2` 和 `n=1` 两个不能作为素数幸存者的端点。

本审计在样本中显示：取 `y=floor(p/e)` 时，除极小 `p=3,5` 外，`p>=7` 的全部行均满足正 margin。正式证明应转化为两个显式不等式：骨架下界 `G_y(h)` 与尾命中上界 `T_y(h)`。
