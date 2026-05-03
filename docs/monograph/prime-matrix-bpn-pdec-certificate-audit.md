# BPN-PDEC Fourier 证书审计

**状态：** `explicit_pdec_certificate_checked`

该审计只验证显式 count vector 的 PDEC 上界。若 pass=false，说明该计数向量不能排除 persistent 分支；若 pass=true，则该具体坏窗相位计数与 PDEC 下界矛盾。无限族仍需对偶证书或结构约束生成器。

## 1. 输入与阈值

- `Q=12`，`|S|=12.0`。
- `kappa=1.0`，`||F||_2=100.0`。
- `L_PDEC=0.0361813613493`。
- `exact max nonzero Fourier=2.05136800847e-14`。
- `effective U_CRT=0.01`。
- `pdec_certificate_pass=True`。

## 2. 最大频率

| h | real | imag | abs |
| ---: | ---: | ---: | ---: |
| 11 | 1.90958360236e-14 | 7.49400541622e-15 | 2.05136800847e-14 |

## 3. 前十个频率

| h | abs |
| ---: | ---: |
| 11 | 2.05136800847e-14 |
| 10 | 7.25244215097e-15 |
| 8 | 5.24543664126e-15 |
| 6 | 4.59428243871e-15 |
| 9 | 3.67518168874e-15 |
| 3 | 3.15115217707e-15 |
| 4 | 2.75773678302e-15 |
| 5 | 2.31022446136e-15 |
| 7 | 1.83102671941e-15 |
| 2 | 6.4974136686e-16 |

## 4. 审稿含义

该报告是 `PDEC-Explicit-Cert` 的机器可核验层。正式证明若要覆盖无限族，仍需
`prime-matrix-bpn-pdec-dual-certificate-framework.md` 中的对偶证书或解析主控证书。
