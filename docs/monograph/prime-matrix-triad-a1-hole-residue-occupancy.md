# Triad-A1 HoleResidueOccupancy 引理

**状态：** `hole_residue_occupancy_barrier_materialized`

本文承接 `TailIndependentCompletion`，把其中的抽象项 `|Occ_t|/r` 写成可证明、可审计的结构屏障。

## 1. 设定

令

```text
Q'=rQ
```

其中 `r` 是本次升层加入的 promoted prime。固定旧活跃相位 `t mod Q`，旧低层洞集为：

```text
H_Q(t)={c: 1<=c<P, 对所有 q|Q 都有 ((t-1)P+c) not=0 mod q}。
```

对 fiber residue `b in Z/rZ`，lift 后相位是：

```text
t_b=t+bQ。
```

新增素数 `r` 在该 fiber 中命中的旧洞为：

```text
R_b(H)={c in H_Q(t): ((t+bQ-1)P+c)=0 mod r}。
```

定义：

```text
Occ_t={b: R_b(H) nonempty}
S_t  ={b: lift 后 t+bQ 仍有完成}
TI_t ={b: b notin Occ_t 且 b in S_t}
```

这里 `TI_t` 正是：promoted prime 没有命中任何旧洞，但更高 Tail 仍独立完成旧洞集。

## 2. 核心引理

对非空旧洞集 `H_Q(t)`：

```text
S_t subset Occ_t union TI_t。
```

因此：

\[
{|S_t|\over r}
\le
{|Occ_t|\over r}+{|TI_t|\over r}.
\tag{HRO-1}
\]

又因为每个旧洞列 `c` 至多确定一个 `b mod r`：

\[
|Occ_t|
\le
|\{c\bmod r:c\in H_Q(t)\}|
\le
\min(|H_Q(t)|,r).
\tag{HRO-2}
\]

所以：

\[
{|S_t|\over r}
\le
{\min(|H_Q(t)|,r)\over r}+{|TI_t|\over r}.
\tag{HRO-3}
\]

这就是 promoted-prime 删除势的局部结构屏障。

## 3. 证明

若 `b in S_t` 且 `b notin Occ_t`，则新增素数 `r` 没有覆盖任何旧洞：

```text
R_b(H)=empty。
```

但该 fiber 仍幸存，说明旧洞集 `H_Q(t)` 必须全部由 `Tail_{>r}` 完成。因此 `b in TI_t`。

所以每个幸存 `b` 要么属于 `Occ_t`，要么属于 `TI_t`，得到 `(HRO-1)`。

另一方面，

```text
((t+bQ-1)P+c)=0 mod r
```

等价于

```text
b == -((t-1)P+c) * (QP)^(-1) mod r。
```

由于 `r` 不整除 `Q` 且 `r<P` 时不整除 `P`，每个列 residue `c mod r` 最多贡献一个 `b`，得到 `(HRO-2)`。

## 4. 删除势二分

从 `(HRO-1)` 出发，如果存在固定余量 `eta>0` 使得平均意义上：

```text
|Occ_t|/r + |TI_t|/r <= 1-eta，
```

则该层的 fiber support 至少删除 `eta` 比例，删除熵支付：

```text
D >= -log(1-eta)。
```

若沿无限升层塔删除势不发散，必须有：

```text
|Occ_t|/r + |TI_t|/r -> 1。
```

于是只有两个结构出口：

```text
OccupancySaturation:
  旧洞集 H_Q(t) 在新增素数 r 的 residue 上近乎满占用；
  这要求 |H_Q(t)| >= (1-o(1))r，并形成低层容量/PDEC 压力。

TailIndependence:
  promoted prime 对大量 fiber 非必要；
  这正是 NoDeletion-KL / CleanKLS 入口。
```

因此删除势失败不会回到无名概率波动，而只能回流到命名终端证书。

## 5. 当前两层审计

新增脚本：

```text
experiments/prime_matrix_triad_a1_hole_residue_occupancy_audit.py
```

生成：

```text
docs/monograph/prime-matrix-triad-a1-hole-residue-occupancy-q2310-q30030.md/json
docs/monograph/prime-matrix-triad-a1-hole-residue-occupancy-q30030-q510510.md/json
```

核心结果：

| layer | P | occ rate | TI rate | union bound | actual survival | certified deletion lb | max occ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2310->30030 | 17 | 0.076923 | 0.000000 | 0.076923 | 0.076923 | 0.923077 | 0.076923 |
| 2310->30030 | 19 | 0.149451 | 0.052747 | 0.202198 | 0.202198 | 0.797802 | 0.153846 |
| 2310->30030 | 23 | 0.222812 | 0.087533 | 0.310345 | 0.310345 | 0.689655 | 0.230769 |
| 2310->30030 | 29 | 0.302564 | 0.041026 | 0.343590 | 0.312821 | 0.656410 | 0.307692 |
| 30030->510510 | 19 | 0.058824 | 0.000000 | 0.058824 | 0.058824 | 0.941176 | 0.058824 |
| 30030->510510 | 23 | 0.114630 | 0.048265 | 0.162896 | 0.162896 | 0.837104 | 0.117647 |

读法：

```text
当前层没有出现 OccupancySaturation；
TI 高峰只发生在旧洞数很小的边界桶；
主删除势来自 zero-cover 且 Tail 不能独立补洞的 fiber。
```

## 6. 下一硬点

`HoleResidueOccupancy` 把删除势失败压成两个更窄目标：

```text
HRO-A. OccupancySaturation 排斥
       若 |Occ_t|/r -> 1，则旧洞集在新增素数 residue 上近满；
       需证明这会触发低层容量矛盾、PDEC 或 ColumnCRT。

HRO-B. TailIndependence 排斥
       若 |TI_t|/r -> 1，则 promoted prime 非必要；
       已由 NoDeletion-KL 路由到 PDEC/CleanKLS。
```

所以当前最优下一步不是再扩大统计样本，而是攻击 `HRO-A`：

```text
旧洞 residue 近满占用
=> 低层洞密度过大或相位偏斜持久
=> Capacity/PDEC/ColumnCRT。
```

这会把 promoted-prime 删除势和用户提出的“层叠轮筛刚性”直接接起来。
