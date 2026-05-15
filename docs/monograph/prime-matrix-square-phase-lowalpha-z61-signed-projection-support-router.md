# Prime Matrix square-phase low-alpha z=61 signed projection support

**状态：** `z61_root_projection_gate_reduced_to_signed_crt_support_with_carry_open`

根投影门可继续展开为 CRT 局部根的符号支撑问题：`M=57684=4*3*11*19*23`，每个局部模都有两个相反平方根，所以 32 个一级根正好是五维符号向量的 CRT 像。但对外部模 `37/71` 投影时必须保留最小代表 carry：`r=S(sigma)-cM`。在 carry 修正后，`q4=37`、`q2=71` 以及合并模 `2627` 的目标投影纤维都只有同一个符号字 `--++-`，对应 `r=26951`；其余目标类为空。因此最新硬点变成全局符号支撑 carry 界，或登记 SignedProjection-PDEC。

```text
signed_projection_support_group_count=1
all_signed_projection_supports_closed=true
signed_projection_support_global_bound_proved=false
signed_crt_carry_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 符号支撑摘要

| M | local moduli | sign vectors | source roots | selected sign | selected carry | selected root | closed |
| ---: | --- | ---: | ---: | --- | ---: | ---: | --- |
| 57684 | `[4, 3, 11, 19, 23]` | 32 | 32 | `--++-` | 6 | 26951 | true |

## 2. 局部 CRT 系数

| local modulus | roots | + root | basis integer | pre-carry coeff mod 37 | pre-carry coeff mod 71 | pre-carry coeff mod 2627 |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 4 | `[1, 3]` | 1 | 14421 | 28 | 8 | 1286 |
| 3 | `[1, 2]` | 1 | 19228 | 25 | 58 | 839 |
| 11 | `[1, 10]` | 1 | 36708 | 4 | 1 | 2557 |
| 19 | `[9, 10]` | 9 | 42504 | 30 | 59 | 1621 |
| 23 | `[5, 18]` | 5 | 2508 | 34 | 44 | 2032 |

## 3. 单投影目标纤维

| gate | target | fiber size | fiber |
| --- | ---: | ---: | --- |
| `q4_plain_root_projection` | 15 | 1 | `[--++-:26951]` |
| `q4_plain_root_projection` | 16 | 0 | `[]` |
| `q2_shifted_root_projection` | 42 | 1 | `[--++-:26951]` |
| `q2_shifted_root_projection` | 50 | 0 | `[]` |

## 4. 合并投影目标纤维

| class mod 2627 | fiber size | fiber |
| ---: | ---: | --- |
| 681 | 1 | `[--++-:26951]` |
| 1754 | 0 | `[]` |
| 1533 | 0 | `[]` |
| 2606 | 0 | `[]` |

## 5. 自足小引理

若 `M=prod m_i` 且 `x^2+delta=0 mod m_i` 的两个局部根为 `±a_i`，则先有整数符号和

```text
S(sigma)=sum_i sigma_i*a_i*B_i,  sigma_i in {+1,-1},
B_i=(M/m_i)*(M/m_i)^{-1} mod m_i.
r(sigma)=S(sigma)-c(sigma)M,  0<=r(sigma)<M.
```

所以外部小模投影满足

```text
r(sigma) mod ell = S(sigma)-c(sigma)M mod ell.
```

这里 carry `c(sigma)` 不能省略，因为 `gcd(M,ell)=1`。本证书精确枚举该五维符号支撑和 carry，证明目标投影纤维为单点或空纤维。

## 6. 证明边界

- 已闭合：当前 z=61 formal unit 的一级根支撑等于五维 CRT 符号像；保留最小代表 carry 后，目标投影纤维唯一命中 `--++- / r=26951`。
- 关键修正：外部模投影不是纯符号线性投影，必须带 carry；下一硬点因此更精确。
- 未闭合：把这种带 carry 的符号投影支撑单点性提升为全局容量界，或排斥 SignedProjection-PDEC。
- 下一目标：`SignedCRTSupportCarryBoundOrSignedProjectionPDEC`。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-root-projection-gate-router.json` | `4ec06861847a756a7e7b58fdd536bf6518b4c6ca26c0ab19a7378f32befe17a3` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_signed_projection_support_router.py` | `b18028249c5dc9df4250e468f9dab6039582e0dc5af67edbb081605674c30649` |
