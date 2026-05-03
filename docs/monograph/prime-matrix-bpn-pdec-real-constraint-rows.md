# BPN-PDEC 真实结构约束行生成报告

**状态：** `finite_crt_real_constraint_rows_generated`

本报告开始填入真实结构约束行：phase cap、mirror pair cap、mass、low-hole bucket 均来自完整 CRT 周期枚举。它们是有限样本的真实系数和界值；无条件证明仍需把这些有限枚举约束替换为符号化结构定理。

## 1. CRT 扫描摘要

- `P=23`，`Q=210`。
- 根基素数 `[2, 3, 5, 7, 11, 13, 17, 19]`。
- `Q` 中低素数 `[2, 3, 5, 7]`。
- CRT 行周期 `9699690`。
- 真实零行数 `3456`，非零相位数 `44`。
- 镜像不匹配数 `0`。
- 前若干零行 `[59, 2612, 5539, 5840, 6569, 10747, 13709, 14759, 15084, 17686, 17792, 19049, 20239, 20480, 42269, 45302, 46682, 53282, 57869, 58459]`。

## 2. Phase cap 约束

`phase_cap_t` 的形式是：

\[
g(t)\le C_t.
\]

- 非零 phase cap 数 `44`。

| phase | cap |
| ---: | ---: |
| 37 | 324 |
| 59 | 324 |
| 79 | 324 |
| 101 | 324 |
| 110 | 324 |
| 132 | 324 |
| 152 | 324 |
| 174 | 324 |
| 6 | 24 |
| 12 | 24 |
| 15 | 24 |
| 19 | 24 |

## 3. Low-hole bucket 约束

低骨架洞数阈值约束形式为：

\[
\sum_{h_Q(t)\ge m}g(t)\le B_m.
\]

| threshold m | phase count | bound |
| ---: | ---: | ---: |
| 3 | 210 | 3456 |
| 4 | 202 | 864 |
| 5 | 166 | 0 |
| 6 | 54 | 0 |
| 7 | 4 | 0 |

## 3A. 关键读数

- `P=23,Q=210` 样本中，真实零行只落在 `44/210` 个相位。
- 最大 phase cap 为 `324`，对应低骨架相位簇。
- `low-hole>=5` 的 bucket 上界为 `0`：在该有限周期中，需要至少 5 个高层补洞的低骨架相位没有真实零行。
- 这给出下一步符号化目标：证明高洞数低骨架相位无法由尾锚/核心补洞容量填满。

## 4. Mass 与 Mirror

- 完整零行族质量等式：`sum_t g(t)=3456`。
- 条件 mirror 等式数量：`105`。
- `phase_cap` 对任意零行子族安全；`mass` 与强 `mirror_eq` 只对完整零行族或已证明镜像闭合的坏窗族安全。

## 5. 审稿边界

这些行已经是实际系数和界值，但来源是有限 CRT 枚举。下一步要把这些行提升为符号定理：

```text
finite phase cap table -> symbolic phase capacity bound；
finite low-hole bucket -> tail/core capacity theorem；
conditional mirror equality -> mirror-closed bad-family lemma。
```
