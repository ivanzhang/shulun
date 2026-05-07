# Triad-A1 无限塔删除/熵预算

**状态：** `finite_budget_for_infinite_tower_dichotomy`

有限审计显示 P=19,23 已连续两层强删除，product_survival 很小。该文件的证明价值在于把后续无限塔硬点压成 deletion-potential divergence versus NoDeletion entropy dichotomy。

## 1. 极限二分律

沿同一 C_P 投影塔，若删除势 sum_n -log a_n(P) 发散，则支撑密度趋零；若删除势可求和，则 a_n(P)->1，必须进入 fiber 条件分布的 KL/PDEC 或 CleanKLS 二分。

设第 `n` 层平均支撑幸存率为 `a_n(P)`。投影单调性给出：

```text
density(A_{Q_N}) = density(A_{Q_0}) * product_{n<N} a_n(P)。
```

因此：

```text
sum -log a_n(P)=infinity  => density(A_{Q_N}) -> 0；
sum -log a_n(P)<infinity  => a_n(P)->1，进入 NoDeletion。
```

`NoDeletion` 不能无名停留：若 fiber 条件分布持续偏斜，则进入 new-layer PDEC；若偏斜趋零，则进入 CleanKLS/DLS。

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `budget_script` | `7bda923d8f09494d24eab8b99f5c429b60b457ee0221bbd6f4fc8017a2c31ed6` |
| `audit_1` | `a0cf1d6b5560d5568754bf9fb23462924bcf53453889cc2e3fa85357b576e504` |
| `audit_2` | `f07a7ba629db204c7b1d948851b52f35ac7f76697d434f68ea8dad21afdf31ed` |

## 3. P 路径预算

| P | layers | Q start | Q end | product survival | product drop | deletion potential | entropy range | KL range |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 17 | 1 | 2310 | 30030 | 0.0769231 | 13 | 2.56495 | `0..0` | `1..1` |
| 19 | 2 | 2310 | 510510 | 0.016031 | 62.379 | 4.13323 | `0.274194..0.455023` | `0.544977..0.725806` |
| 23 | 2 | 2310 | 510510 | 0.0505539 | 19.7809 | 2.98472 | `0.461487..0.565879` | `0.434121..0.538513` |
| 29 | 1 | 2310 | 30030 | 0.312821 | 3.19672 | 1.16213 | `0.576893..0.576893` | `0.423107..0.423107` |

## 4. 层级明细

### P=17

| layer | survival | deletion | drop | deletion potential | entropy | KL | class |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Q=2310->30030 | 0.0769231 | 0.923077 | 13 | 2.56495 | 0 | 1 | `ReSparsifiedByFiberDeletion` |

### P=19

| layer | survival | deletion | drop | deletion potential | entropy | KL | class |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Q=2310->30030 | 0.202198 | 0.797802 | 4.94565 | 1.59851 | 0.455023 | 0.544977 | `ReSparsifiedByFiberDeletion` |
| Q=30030->510510 | 0.0792839 | 0.920716 | 12.6129 | 2.53472 | 0.274194 | 0.725806 | `ReSparsifiedByFiberDeletion` |

### P=23

| layer | survival | deletion | drop | deletion potential | entropy | KL | class |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Q=2310->30030 | 0.310345 | 0.689655 | 3.22222 | 1.17007 | 0.565879 | 0.434121 | `ReSparsifiedByFiberDeletion` |
| Q=30030->510510 | 0.162896 | 0.837104 | 6.13889 | 1.81464 | 0.461487 | 0.538513 | `ReSparsifiedByFiberDeletion` |

### P=29

| layer | survival | deletion | drop | deletion potential | entropy | KL | class |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Q=2310->30030 | 0.312821 | 0.687179 | 3.19672 | 1.16213 | 0.576893 | 0.423107 | `ReSparsifiedByFiberDeletion` |

## 5. 闭合边界

本文给出无限塔的结构预算公式与有限层读数。它还没有证明 `sum -log a_n(P)` 必然发散，
也没有完成 NoDeletion 分支的最终 PDEC/CleanKLS 排斥。下一步应攻：

```text
NoDeletion => KL 偏斜不可长期隐藏；
若 KL 偏斜隐藏，则高维平坦大筛吸收。
```
