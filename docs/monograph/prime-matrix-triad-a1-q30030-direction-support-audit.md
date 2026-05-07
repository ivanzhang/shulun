# Triad-A1 LHB 方向支撑审计

**状态：** `direction_support_intersection_audited`

本审计把候选方向支撑 C_F(kappa) 与 LHB 的 supp(M) 相交。默认支撑 WHOLEDEF/BRIDGED 在全部列出 P 上交集为空，因此该子分支在 LHB 分支内闭合。一般 PDEC 方向仍需提交真实 F,kappa,C_F。

## 1. 审计对象

- `Q=30030`。
- 支撑块：`['whole_deficit_phases', 'bridged_critical_phases']`。
- 稀疏阈值：`16`。
- `all_empty=True`。

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `direction_support_script` | `9050982ca17e1948260d685700b9cc3f077f71de398979f09914d81c52061d9f` |
| `multiplicity_cap_json` | `c62dea9f85ebdf6fb69eb9870b0a4e4af89dd88ac696a2247b48dd22c4a4bbba` |
| `phase_blocks_json` | `2996d4f60e0bf882beda51076c457d2163d340cc62ce0005e356720e3a503ea2` |

## 3. 交集表

| P | support size | intersection size | M-mass bound | class | sample |
| ---: | ---: | ---: | ---: | --- | --- |
| 17 | 30002 | 0 | 0 | `EmptyCap` | `[]` |
| 19 | 29662 | 0 | 0 | `EmptyCap` | `[]` |
| 23 | 29094 | 0 | 0 | `EmptyCap` | `[]` |
| 29 | 29420 | 0 | 0 | `EmptyCap` | `[]` |

## 4. 结论

若真实 `C_F(kappa)` 就是本审计的支撑块并集，则 `intersection_size=0` 的行直接闭合：

```text
supp(g) subset C_F(kappa) cap supp(M) = empty。
```

若后续输入真实 PDEC 方向后交集非空，则按 `SparseCap/PersistentCap/FlatCap` 继续回流。
