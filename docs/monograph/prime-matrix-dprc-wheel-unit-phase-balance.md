# DPRC W=30单位相位平衡扫描

**状态：** `audit_not_a_proof`

本文接续 `DPRC-BES 近危险结构审计`，把 `WheelUnitPhaseBalance(W=30)` 从样本扩展为全范围扫描。

## 1. 扫描对象

脚本：

```text
experiments/prime_matrix_dprc_wheel_unit_phase_balance_scan.py
```

报告：

```text
docs/dprc_wheel_unit_phase_balance_w30_p100000_20260506.md
docs/dprc_wheel_unit_phase_balance_w30_p100000_20260506.json
```

参数：

```text
alpha=0.43；
13<=P<=100000；
P>=2003 与 P>=10007 两个阈值；
plus/minus 共 19174 条记录，高段 P>=2003 有 18578 条。
```

## 2. 核心读数

`P>=2003` 与 `P>=10007` 的关键读数相同：

| 指标 | 数值 |
|---|---:|
| `danger_l1_l2_6_5_count` | `0` |
| `danger_l1_l2_cauchy_count` | `0` |
| `max_unit30_peak_over_sqrt` | `1.076781` |
| `max_unit30_positive_l1_over_sqrt` | `2.589921` |
| `high_l1_count` | `2` |
| `high_l1_max_unit30_peak` | `0.902430` |
| `high_l2_count` | `1` |
| `high_l2_max_l1` | `2.078474` |
| `max_l1_when_unit30_peak_ge_0_8` | `2.442672` |
| `max_l2_when_unit30_peak_ge_0_8` | `1.177635` |

最大 `mod30` 单位相位峰：

```text
P=64853 minus:
  unit30 peak = 1.076781；
  BES L1      = 0.493686；
  BES L2      = 0.281040。
```

最高 `BES L1` 样本：

```text
P=30137 minus:
  BES L1      = 2.468627；
  BES L2      = 1.138250；
  unit30 peak = 0.544278。
```

最高 `BES L2` 样本：

```text
P=83267 plus:
  BES L1      = 2.078474；
  BES L2      = 1.233496；
  unit30 peak = 0.670042。
```

## 3. 结构结论

第一层轮相位峰是真实存在的，但它与 BES 危险交集不同步：

```text
unit30 peak 很高时，BES L1/L2 低；
BES L1 很高时，L2 低于危险阈值；
BES L2 唯一超 Cauchy 阈值时，L1<12/5。
```

因此 `W=30` 不是终局规律，而是第一层可见偏斜。它揭示低模单位类内部有方向性，但这种方向性在当前扫描范围内没有与高素多尺度覆盖能力同步到危险程度。

## 4. 单位类顶峰分布

`P>=10007` 的 top residue histogram：

```text
{1: 2131, 7: 2045, 11: 2128, 13: 2074,
 17: 2152, 19: 2114, 23: 2065, 29: 2017}
```

八个单位类出现次数接近平衡。这支持如下判断：

```text
mod30 层有局部偏斜；
但没有固定单位类长期主导；
全局规律表现为单位类之间的轮换，而不是某个静态残基规律。
```

## 5. 下一硬点

当前最小硬点从 `W=30` 升级为：

```text
Layered WheelUnitPhaseBalance:
  W=30 的单位类峰不同步；
  继续检查 W=210/2310 的更细单位类；
  若某层出现高单位峰与 BES 危险交集同步，
  则该层给出 W-unit PDEC；
  若所有有限提升层都不同步，
  则剩余偏差必须由高模分散能量承担，进入大筛界。
```

这与“素数规律是无穷层叠”的直觉一致：每一层小模连乘给出一个真实但不终局的结构；证明不能停在某一固定轮，而要证明这些层级偏斜不能同时同步成整行覆盖。
