# Prime Matrix square-phase low-alpha z=61 quotient factor lift

**状态：** `z61_quotient_gate_reduced_to_prime_factor_lift_gates_open`

quotient-residue gate 可改写为两个素因子提升门：`q4=37` 门等价于一级平方根从 `M` 提升到 `M*37`，`q2=71` 门等价于带偏移项 `2Mq4` 提升到 `M*71`。样本中两个提升门各自已经唯一选中同一个根 `r=26951`，其合并门也唯一。因此最新硬点从商变量 `K` 收窄为 CRT 根的素因子提升容量界，或登记 LiftGate-PDEC。

```text
quotient_factor_lift_group_count=1
all_quotient_factor_lift_gates_closed=true
prime_factor_lift_gate_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 素因子提升门

| gate | factor | lift modulus | offset/M | pass count | pass residues | uniquely selected |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `q4_plain_square_lift` | 37 | 2134308 | 0 | 1 | `[26951]` | true |
| `q2_shifted_square_lift` | 71 | 4095564 | 74 | 1 | `[26951]` | true |
| `q2q4_combined_lift` | 2627 | 151535868 | 74 | 1 | `[26951]` | true |

## 2. 素数候选的提升残差

| root | p | q4 lift | q2 lift | combined lift | prime p | full source |
| ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1891 | 174943 | 1211364 | 3172620 | 150612924 | true | false |
| 3961 | 177013 | 1961256 | 2711148 | 121482504 | true | false |
| 8009 | 181061 | 115368 | 2365044 | 55607376 | true | false |
| 11219 | 184271 | 1095996 | 3749460 | 16036152 | true | false |
| 11771 | 184823 | 2076624 | 2711148 | 68240172 | true | false |
| 24881 | 197933 | 115368 | 3576408 | 85487688 | true | false |
| 26951 | 200003 | 0 | 0 | 0 | true | true |
| 34495 | 207547 | 1153680 | 2884200 | 43839840 | true | false |
| 46465 | 219517 | 1442100 | 3576408 | 3576408 | true | false |

## 3. 自足小引理

在一级条件 `p^2+delta=M*K` 下，`K+2q4≡0 (mod q)` 等价于

```text
p^2+delta+2M*q4 ≡ 0 (mod M*q).
```

当 `q=q4` 时偏移项 `2M*q4` 已被 `M*q4` 整除，所以退化为普通平方根提升；当 `q=q2` 时得到真正的带偏移提升。两者合并即 quotient gate 的奇素因子部分。

## 4. 证明边界

- 已闭合：样本 q2/q4 两个素因子提升门各自唯一选中同一根。
- 未闭合：全局素因子提升门容量界，或 LiftGate-PDEC 排斥。
- 下一目标：`PrimeFactorLiftGateGlobalBoundOrLiftGatePDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-quotient-gate-router.json` | `7f446ac49e7adea229ea0c83f7b5a1620d4aa7140d09ca5a435bf28a1c29c67e` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_quotient_factor_lift_router.py` | `71f0dba70656d792356d8279d14e73e6a294f45e1f1739266372716aaa4bbb63` |
