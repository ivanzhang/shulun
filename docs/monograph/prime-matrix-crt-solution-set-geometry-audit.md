# CRT 零/非零同余解集几何审计

**状态：** `crt_mirror_exact_but_middle_rough_density_not_boundary_proof`

CRT 筛幸存集合有精确镜像：R(N-r+1)=P-R(r)，所以零行镜像严格成立。但中区素数/粗合数密集是数值层现象，不是 CRT 行幸存数的单调势能；它不能单独推出边界零行不存在。

## 总表

| P | N | hist | zero count | first zeros | mirror counts? | boundary counts rows 2..P |
| ---: | ---: | --- | ---: | --- | --- | --- |
| 13 | 2310 | `{0: 4, 1: 180, 2: 966, 3: 992, 4: 168}` | 4 | `[169, 702, 1609, 2142]` | True | `[3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 2, 3]` |
| 17 | 30030 | `{0: 28, 1: 1020, 2: 6642, 3: 12848, 4: 8148, 5: 1344}` | 28 | `[1211, 1638, 2323, 4744, 5171, 6530, 8277, 9618, 10063, 10938]` | True | `[4, 4, 4, 4, 3, 4, 2, 4, 3, 3, 4, 1, 4, 3, 4, 3]` |
| 19 | 510510 | `{0: 496, 1: 12888, 2: 87588, 3: 205728, 4: 166188, 5: 36852, 6: 770}` | 496 | `[3659, 4101, 4731, 6705, 6820, 7671, 9004, 9981, 10275, 11429]` | True | `[4, 4, 5, 3, 6, 2, 4, 3, 3, 4, 3, 4, 3, 5, 1, 4, 2, 4]` |
| 23 | 9699690 | `{0: 3456, 1: 104400, 2: 867960, 3: 2793840, 4: 3709440, 5: 1899324, 6: 309750, 7: 11520}` | 3456 | `[59, 2612, 5539, 5840, 6569, 10747, 13709, 14759, 15084, 17686]` | True | `[5, 5, 5, 6, 3, 4, 5, 4, 4, 4, 4, 4, 4, 2, 5, 4, 3, 4, 4, 4, 4, 3]` |

## 精确镜像引理

令 `N=prod_{ell<P}ell`。若行 `r` 的幸存列集合为

\[
R(r)=\{1\le c<P:( (r-1)P+c, N)=1\},
\]

则

\[
R(N-r+1)=\{P-c:c\in R(r)\}.
\]

证明是取负映射：`(r-1)P+c` 变为 `NP-((r-1)P+c)=(N-r)P+(P-c)`。因此行幸存数和零行集合严格镜像。

## 中区与边界的区别

前窗口 `r<=P` 中，任何 CRT 幸存者都小于 `P^2`，所以自动为素数。中区幸存者只保证没有 `<P` 小因子，可能是素数，也可能是 `P`-rough 合数。故“中区粗合数密集”属于数值层，不能直接推出 CRT 筛层的边界非覆盖。

## 样本画像

### P=13 边界窗口最薄行
- row=10 survivors=1 prime_survivors=1 rough_composites=0 data=`[{'col': 10, 'value': 127, 'is_prime': True, 'small_factor_check': []}]`
- middle sample row=1142 survivors=2 prime_survivors=1 rough_composites=1

### P=17 边界窗口最薄行
- row=13 survivors=1 prime_survivors=1 rough_composites=0 data=`[{'col': 7, 'value': 211, 'is_prime': True, 'small_factor_check': []}]`
- middle sample row=15032 survivors=3 prime_survivors=0 rough_composites=3

### P=19 边界窗口最薄行
- row=16 survivors=1 prime_survivors=1 rough_composites=0 data=`[{'col': 8, 'value': 293, 'is_prime': True, 'small_factor_check': []}]`
- middle sample row=255236 survivors=3 prime_survivors=1 rough_composites=2

### P=23 边界窗口最薄行
- row=15 survivors=2 prime_survivors=2 rough_composites=0 data=`[{'col': 9, 'value': 331, 'is_prime': True, 'small_factor_check': []}, {'col': 15, 'value': 337, 'is_prime': True, 'small_factor_check': []}]`
- middle sample row=4849822 survivors=4 prime_survivors=2 rough_composites=2

## 下一证明义务

- 把镜像作为两端帽约束使用，而不是短周期或单调密度证明。
- 若要利用中区粗合数密集，必须先构造连接数值层与 CRT 筛层的势函数。
- 主链继续回到 BPN 势函数或 GridPrimeGap 条件输入。
