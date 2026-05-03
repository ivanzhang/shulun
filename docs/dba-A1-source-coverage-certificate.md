# DBA-A1 来源覆盖逐行证书

**状态：** `verified`

- 行数：`32`
- 已验证：`32`
- 待复核：`0`
- 未知去向：`0`

| # | 来源 | 失败方式 | 去向 | 状态 |
|---:|---|---|---|---|
| 1 | 6.10.1 | D_i=0 / 四点分母不可逆 | denominator_pole | verified |
| 2 | 6.10.1 | E mod q 恒等为零 | four_point_rank_failure | verified |
| 3 | 6.10.2 | 对角/半对角 | separate_count_not_DBA | verified |
| 4 | 6.10.3 | 水平纤维厚化根簇过多 | ramification | verified |
| 5 | 6.10.3 | R' 消失 | derivative_zero | verified |
| 6 | 6.10.4 | 局部 rank 低于 1 | four_point_rank_failure or jacobian_common_branch | verified |
| 7 | 6.11.1 | F 与梯度同时小 | jacobian_common_branch | verified |
| 8 | 6.12.2 | 投影 Jacobian 消失 | derivative_zero or ramification or jacobian_common_branch | verified |
| 9 | 6.13.2 | 小导数单调段 | derivative_zero or jacobian_common_branch | verified |
| 10 | 6.13.2 | 分母极点/多值分支合并 | denominator_pole or ramification | verified |
| 11 | 6.18.1d | W_h 阶梯端点/权重突变 | layering_endpoint_low_volume | verified |
| 12 | 6.18.1e | q|h, q|mT, 分母不可逆 | step_frequency_resonance or denominator_pole | verified |
| 13 | 6.18.2c | 层化四点厚化异常 | four_point_rank_failure or jacobian_common_branch | verified |
| 14 | 6.7--6.8 | q|t,q|h,q|mU | step_frequency_resonance | verified |
| 15 | 4.3.6/FS8 | 多逆元 CRT/Kloosterman 分支退化 | denominator_pole or ramification or step_frequency_resonance | verified |
| 16 | 6.17.1--6.17.3 | sawtooth 端点相位 Fourier 截断尾 | fourier_truncation_tail | verified |
| 17 | 6.17.6/6.18.1d | 权重 W(a) 变差或 dyadic 端点过多 | layering_endpoint_low_volume | verified |
| 18 | B.0.3e+ | CRT 逆元 b(a) 分母或兼容失败 | denominator_pole or ramification | verified |
| 19 | 6.18.1c | 差分相位 F_h(a) 分母为零或分片无定义 | denominator_pole | verified |
| 20 | 6.18.1e | 非共振步长检测失败 q|h,q|mT,q|mU | step_frequency_resonance | verified |
| 21 | 6.18.2a--b | 短弧层化 L 超对数幂 | denominator_pole or derivative_zero or ramification or layering_endpoint_low_volume | verified |
| 22 | 6.13.1--6.13.3 | coarea 切片法向导数为零 | derivative_zero or jacobian_common_branch | verified |
| 23 | 4.3.6h/6.18.1d-KS-J | Kloosterman reciprocity 模逆元分支退化 | denominator_pole or ramification or step_frequency_resonance | verified |
| 24 | 6.18.1d-KS | KS-W 双线性权重变差和端点分片 | layering_endpoint_low_volume | verified |
| 25 | 6.18.1d-KS-J/6.15.3a | KS-J 中 z,t,resultant atlas 退化 | denominator_pole or derivative_zero or ramification or jacobian_common_branch | verified |
| 26 | 6.13.6/6.15.3a-K1 | KS-DC 切片端点余量或低体积盒 | layering_endpoint_low_volume or jacobian_common_branch | verified |
| 27 | 6.13.6/6.15.3a-K2 | Kloosterman 八变量 rank 失效 | four_point_rank_failure or jacobian_common_branch | verified |
| 28 | FS8-polymer | skeleton 标签、短块来源、gap-word 端点过多 | layering_endpoint_low_volume | verified |
| 29 | FS8-polymer | 不同 connected 分量相位分离 | component_split_mobius_cancelled | verified |
| 30 | FS8-polymer | Hall 叶变量匹配失败 | four_point_rank_failure or jacobian_common_branch | verified |
| 31 | FS8-polymer | 相位差分落入共振弧 | step_frequency_resonance or jacobian_common_branch or four_point_rank_failure | verified |
| 32 | FS8-polymer | 多 skeleton 坏素重复计数 | rankin_divisor_budget | verified |

## 说明
This is a coverage certificate for listed failure modes. It verifies that each listed source has evidence and a legal atlas/budget destination; it does not prove that no unlisted source exists beyond the audited sections.
