# DBA-closure 有限生成坏层 Atlas

**状态：** `atlas_extracted_A3_A4_budget_classified_A1_requires_final_source_audit`

## 生成元
### denominator_pole：分母/不可逆层
- 覆盖：函数无定义；CRT/模逆元不可逆；Kloosterman reciprocity 分母退化
- 高度状态：standard_fixed_degree_height

### derivative_zero：一变量导数层
- 覆盖：R'(x_i)=0；coarea 单调段端点；水平集聚集的导数退化
- 高度状态：standard_fixed_degree_height

### ramification：ramification/分支合并层
- 覆盖：水平纤维多根；多前像合并；短弧层数失控
- 高度状态：resultant_height_needed_but_standard

### four_point_rank_failure：四点 rank 失效层
- 覆盖：E mod q 恒等为零；有效素因子未贡献 rank；清分母多项式含高维公共因子
- 高度状态：coefficient_height_standard; high-dimensional factor test remains atlas item

### jacobian_common_branch：Jacobian/临界纤维层
- 覆盖：F 与梯度/Jacobian 共维不足；投影 Jacobian 消失；coarea 法向导数过小
- 高度状态：multivariate_resultant_height_required

### step_frequency_resonance：步长/频率共振层
- 覆盖：q|h；q|t；q|mU；q|mT；差分/Fourier 频率不可检测
- 高度状态：integer_factor_height_trivial; needs averaging 1/q+1/T

### layering_endpoint_low_volume：层化端点/低体积账本
- 覆盖：权重突变；短弧层数超过对数幂；低体积盒端点余量
- 高度状态：not_DBA_polynomial_only; handled by C_L/C_KS and low-volume budget

## 覆盖矩阵
| 来源 | 失败方式 | Atlas 去向 | 预算去向 |
|---|---|---|---|
| 6.10.1 | D_i=0 / 四点分母不可逆 | denominator_pole | DBA polynomial atlas; A2 height + A5 Rankin budget |
| 6.10.1 | E mod q 恒等为零 | four_point_rank_failure | rank/resultant atlas; A2 coefficient height + C_rk budget |
| 6.10.2 | 对角/半对角 | separate_count_not_DBA | separate diagonal/semidiagonal count; not DBA |
| 6.10.3 | 水平纤维厚化根簇过多 | ramification | DBA resultant atlas; A2 resultant height + C_co/C_L budget |
| 6.10.3 | R' 消失 | derivative_zero | DBA polynomial atlas; A2 height + coarea budget C_co |
| 6.10.4 | 局部 rank 低于 1 | four_point_rank_failure or jacobian_common_branch | rank/resultant atlas; A2 coefficient height + C_rk budget; multivariate resultant atlas; A2 multivariate height + C_co budget |
| 6.11.1 | F 与梯度同时小 | jacobian_common_branch | multivariate resultant atlas; A2 multivariate height + C_co budget |
| 6.12.2 | 投影 Jacobian 消失 | derivative_zero or ramification or jacobian_common_branch | DBA polynomial atlas; A2 height + coarea budget C_co; DBA resultant atlas; A2 resultant height + C_co/C_L budget; multivariate resultant atlas; A2 multivariate height + C_co budget |
| 6.13.2 | 小导数单调段 | derivative_zero or jacobian_common_branch | DBA polynomial atlas; A2 height + coarea budget C_co; multivariate resultant atlas; A2 multivariate height + C_co budget |
| 6.13.2 | 分母极点/多值分支合并 | denominator_pole or ramification | DBA polynomial atlas; A2 height + A5 Rankin budget; DBA resultant atlas; A2 resultant height + C_co/C_L budget |
| 6.18.1d | W_h 阶梯端点/权重突变 | layering_endpoint_low_volume | A4 non-polynomial budget; C_L/C_KS/low-volume boxes |
| 6.18.1e | q|h, q|mT, 分母不可逆 | step_frequency_resonance or denominator_pole | A3 step/frequency budget; 1/q enters Rankin, 1/T enters B4; DBA polynomial atlas; A2 height + A5 Rankin budget |
| 6.18.2c | 层化四点厚化异常 | four_point_rank_failure or jacobian_common_branch | rank/resultant atlas; A2 coefficient height + C_rk budget; multivariate resultant atlas; A2 multivariate height + C_co budget |
| 6.7--6.8 | q|t,q|h,q|mU | step_frequency_resonance | A3 step/frequency budget; 1/q enters Rankin, 1/T enters B4 |
| 4.3.6/FS8 | 多逆元 CRT/Kloosterman 分支退化 | denominator_pole or ramification or step_frequency_resonance | DBA polynomial atlas; A2 height + A5 Rankin budget; DBA resultant atlas; A2 resultant height + C_co/C_L budget; A3 step/frequency budget; 1/q enters Rankin, 1/T enters B4 |
| 6.17.1--6.17.3 | sawtooth 端点相位 Fourier 截断尾 | fourier_truncation_tail | Fourier truncation parameter budget B1; not DBA |
| 6.17.6/6.18.1d | 权重 W(a) 变差或 dyadic 端点过多 | layering_endpoint_low_volume | A4 non-polynomial budget; C_L/C_KS/low-volume boxes |
| B.0.3e+ | CRT 逆元 b(a) 分母或兼容失败 | denominator_pole or ramification | DBA polynomial atlas; A2 height + A5 Rankin budget; DBA resultant atlas; A2 resultant height + C_co/C_L budget |
| 6.18.1c | 差分相位 F_h(a) 分母为零或分片无定义 | denominator_pole | DBA polynomial atlas; A2 height + A5 Rankin budget |
| 6.18.1e | 非共振步长检测失败 q|h,q|mT,q|mU | step_frequency_resonance | A3 step/frequency budget; 1/q enters Rankin, 1/T enters B4 |
| 6.18.2a--b | 短弧层化 L 超对数幂 | denominator_pole or derivative_zero or ramification or layering_endpoint_low_volume | DBA polynomial atlas; A2 height + A5 Rankin budget; DBA polynomial atlas; A2 height + coarea budget C_co; DBA resultant atlas; A2 resultant height + C_co/C_L budget; A4 non-polynomial budget; C_L/C_KS/low-volume boxes |
| 6.13.1--6.13.3 | coarea 切片法向导数为零 | derivative_zero or jacobian_common_branch | DBA polynomial atlas; A2 height + coarea budget C_co; multivariate resultant atlas; A2 multivariate height + C_co budget |
| 4.3.6h/6.18.1d-KS-J | Kloosterman reciprocity 模逆元分支退化 | denominator_pole or ramification or step_frequency_resonance | DBA polynomial atlas; A2 height + A5 Rankin budget; DBA resultant atlas; A2 resultant height + C_co/C_L budget; A3 step/frequency budget; 1/q enters Rankin, 1/T enters B4 |
| 6.18.1d-KS | KS-W 双线性权重变差和端点分片 | layering_endpoint_low_volume | A4 non-polynomial budget; C_L/C_KS/low-volume boxes |
| 6.18.1d-KS-J/6.15.3a | KS-J 中 z,t,resultant atlas 退化 | denominator_pole or derivative_zero or ramification or jacobian_common_branch | DBA polynomial atlas; A2 height + A5 Rankin budget; DBA polynomial atlas; A2 height + coarea budget C_co; DBA resultant atlas; A2 resultant height + C_co/C_L budget; multivariate resultant atlas; A2 multivariate height + C_co budget |
| 6.13.6/6.15.3a-K1 | KS-DC 切片端点余量或低体积盒 | layering_endpoint_low_volume or jacobian_common_branch | A4 non-polynomial budget; C_L/C_KS/low-volume boxes; multivariate resultant atlas; A2 multivariate height + C_co budget |
| 6.13.6/6.15.3a-K2 | Kloosterman 八变量 rank 失效 | four_point_rank_failure or jacobian_common_branch | rank/resultant atlas; A2 coefficient height + C_rk budget; multivariate resultant atlas; A2 multivariate height + C_co budget |
| FS8-polymer | skeleton 标签、短块来源、gap-word 端点过多 | layering_endpoint_low_volume | A4 non-polynomial budget; C_L/C_KS/low-volume boxes |
| FS8-polymer | 不同 connected 分量相位分离 | component_split_mobius_cancelled | disconnected cumulant component cancels by Mobius inversion; not DBA |
| FS8-polymer | Hall 叶变量匹配失败 | four_point_rank_failure or jacobian_common_branch | rank/resultant atlas; A2 coefficient height + C_rk budget; multivariate resultant atlas; A2 multivariate height + C_co budget |
| FS8-polymer | 相位差分落入共振弧 | step_frequency_resonance or jacobian_common_branch or four_point_rank_failure | A3 step/frequency budget; 1/q enters Rankin, 1/T enters B4; multivariate resultant atlas; A2 multivariate height + C_co budget; rank/resultant atlas; A2 coefficient height + C_rk budget |
| FS8-polymer | 多 skeleton 坏素重复计数 | rankin_divisor_budget | bad prime multiplicity counted by Rankin/divisor budget C_rk |

## A3/A4 预算归类
### A3_step_frequency_resonance
- 对象：q|h；q|t；q|mU；q|mT；q|m；q|d；q|mdh
- 估计：average over step/frequency gives O(1/q+1/T)
- 吸收：1/q is absorbed by DBA bad-prime Rankin budget C_rk; 1/T is absorbed by B4 with margin 600 in dba-A2-A5-parameter-ledger
- 状态：budget_classified_numeric_margin_available

### A4_layering_endpoint_low_volume
- 对象：W_h step endpoints；short-arc layer count；dyadic endpoints；low-volume boxes；coarea slicing endpoints
- 估计：normal layer count <= log^{C_L} P; Kloosterman slicing/rank overhead <= log^{C_KS} P; low-volume boxes enter explicit low-volume budget
- 吸收：C_L=80 and C_KS=80 are included in C_star=160; KS margins are positive in dba-A2-A5-parameter-ledger
- 状态：budget_classified_numeric_margin_available


## 剩余审查义务
- 确认 source_coverage_matrix 的来源行已覆盖 6.10--6.18 与 4.3.6/FS8 中所有失败方式；当前脚本只检查每个已列来源有合法去向。
- 对 multivariate elimination resultants 给出固定次数/高度标准界引用或附录证明。
- A3/A4 已预算归类；最终需核对正文每次引用均指向 A3_A4_budget 中的相应条目。

## 条件闭合结论
DBA-closure follows; combined with discrete coarea and local rank, this closes 4E-DISP and feeds UAS.
