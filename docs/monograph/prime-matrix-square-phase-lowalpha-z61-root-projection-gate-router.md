# Prime Matrix square-phase low-alpha z=61 root projection gate

**状态：** `z61_affine_root_selector_reduced_to_root_projection_gate_open`

仿射选择器可继续消去 `K`：因 `p=hM+r` 且 `p^2+delta=M*K`，`K+offset≡0 (mod ell)` 等价于 `(r+hM)^2+delta+offset*M≡0 (mod ell)`。在当前 z=61 样本中，`q4=37` 投影根为 `r≡15,16`，`q2=71` 移位投影根为 `r≡42,50`；但 32 个一级 CRT 根支撑上，两门各自以及合并门都只命中 `r=26951`。因此最新硬点进一步收窄为根支撑投影容量界，或登记 Projection-PDEC。

```text
root_projection_gate_group_count=1
all_root_projection_gates_closed=true
root_projection_gate_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 投影门摘要

| M | h | roots | q4 unique | q2 unique | combined classes | combined pass | selected | closed |
| ---: | ---: | ---: | --- | --- | --- | --- | ---: | --- |
| 57684 | 3 | 32 | true | true | `[681, 1754, 1533, 2606]` | `[26951]` | 26951 | true |

## 2. 单投影门

| gate | ell | offset/M | root solutions | p solutions | pass roots | unrealized solutions | unique |
| --- | ---: | ---: | --- | --- | --- | --- | --- |
| `q4_plain_root_projection` | 37 | 0 | `[15, 16]` | `[18, 19]` | `[26951]` | `[16]` | true |
| `q2_shifted_root_projection` | 71 | 74 | `[42, 50]` | `[4, 67]` | `[26951]` | `[50]` | true |

## 3. 合并投影纤维

| class mod q2q4 | roots in CRT support |
| ---: | --- |
| 681 | `[26951]` |
| 1754 | `[]` |
| 1533 | `[]` |
| 2606 | `[]` |

## 4. 候选根投影残差

| root | p | r mod 37 | r mod 71 | q4 proj | q2 proj | prime p | full source |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1891 | 174943 | 4 | 45 | 21 | 56 | true | false |
| 3961 | 177013 | 2 | 56 | 34 | 13 | true | false |
| 8009 | 181061 | 17 | 57 | 2 | 34 | true | false |
| 11219 | 184271 | 8 | 1 | 19 | 21 | true | false |
| 11771 | 184823 | 5 | 56 | 36 | 13 | true | false |
| 24881 | 197933 | 17 | 31 | 2 | 67 | true | false |
| 26951 | 200003 | 15 | 42 | 0 | 0 | true | true |
| 34495 | 207547 | 11 | 60 | 20 | 38 | true | false |
| 46465 | 219517 | 30 | 31 | 25 | 67 | true | false |

## 5. 自足小引理

若 `p=hM+r` 且 `p^2+delta=M*K`，并且 `gcd(M,ell)=1`，则

```text
K+offset ≡ 0 (mod ell)
⇔ M*(K+offset) ≡ 0 (mod ell)
⇔ (r+hM)^2+delta+offset*M ≡ 0 (mod ell).
```

因此仿射选择器不是新的大变量条件，而是一级 CRT 根集合在小模 `37`、`71` 上的投影筛选。

## 6. 证明边界

- 已闭合：样本仿射门等价于根相位投影门，且两个单投影门与合并投影门均唯一选中同一根。
- 新发现：理论投影根共有四个合并类，但一级 CRT 根支撑只实现其中一个类；其余三个类是支撑空纤维。
- 未闭合：全局根支撑投影容量界，或 Projection-PDEC 排斥。
- 下一目标：`RootProjectionGateGlobalBoundOrProjectionPDEC`。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-affine-lift-selector-router.json` | `2ac894c685b6e8b035c7d02751db47f25ba5cfe238cd4bec7fc7efef5f9cb7dd` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_root_projection_gate_router.py` | `00f4c90ab133bdde83dae6bdcc5f07b0ed6b0a406b925e1f57b5f7412451d2a6` |
