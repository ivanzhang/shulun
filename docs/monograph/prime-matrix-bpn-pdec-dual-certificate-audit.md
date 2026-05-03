# BPN-PDEC 对偶证书审计

**状态：** `pdec_dual_certificate_checked`

该审计验证 PDEC-Dual-Cert 的线性对偶不等式。若 all_pass=true，则输入证书覆盖的频率方向满足 U_CRT<L_PDEC；若要闭合无限族，还必须证明这些约束确实由边界零行结构产生，并覆盖所有 h 与方向。

## 1. 输入摘要

- `Q=12`，`|S|=12.0`。
- `L_PDEC=0.0361813613493`。
- 不等式 `1` 条，等式 `12` 条。
- 方向证书 `1` 个。
- `all_certificates_pass=True`。
- 最小严格余量 `0.0361813613483`。
- 最小逐相位 slack `0`。

## 2. 方向证书表

| name | h | pointwise | U_CRT | margin | worst phase | min slack | pass |
| --- | ---: | --- | ---: | ---: | ---: | ---: | --- |
| demo_h1_real_direction | 1 | True | 1e-12 | 0.0361813613483 | 0 | 0 | True |

## 3. 审稿含义

该报告只证明输入线性系统下的对偶上界。正式稿仍必须逐条证明 `inequalities` 与
`equalities` 来自 mirror、column、tail-anchor、core-overlap 与 Rankin routing 等结构约束。
