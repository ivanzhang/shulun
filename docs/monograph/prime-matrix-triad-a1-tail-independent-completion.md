# Triad-A1 TailIndependentCompletion 例外项

**状态：** `tail_independent_completion_profiled_exception_route_open`

本文承接 `DeletionPotential`。上一层说明 promoted prime `r` 的删除势来自：

```text
若 residue b 不命中旧洞 H_Q(t)，fiber 通常死亡。
```

现在把例外项单独抽出：

```text
zero-cover 但仍幸存
<=> Tail_{>r} 不依赖 promoted prime，独立完成旧洞集。
```

这个例外若长期大量出现，正是 `NoDeletion-KL`；若例外少，则它直接给删除势留下正下界。

## 1. 结构分解

固定旧活跃相位 `t` 和旧洞集 `H=H_Q(t)`。对新增素因子 `r` 的 residue `b`，写：

```text
R_b(H)={c in H: ((t+bQ-1)P+c)=0 mod r}。
```

fiber 幸存当且仅当：

```text
H \ R_b(H) 可由 Tail_{>r} 完成。
```

令：

```text
Occ_t={b: R_b(H) nonempty}；
TI_t ={b: R_b(H)=empty, 但 Tail_{>r} 完成 H}。
```

则对非空 `H`：

```text
surviving residues subset Occ_t union TI_t。
```

因此：

\[
{s(t)\over r}
\le
{|Occ_t|\over r}+{|TI_t|\over r}
\le
{|H_Q(t)|\over r}+{|TI_t|\over r}.
\tag{TIC-1}
\]

这就是 DeletionPotential 的一阶结构界。只要 `|H_Q(t)|/r` 与 `|TI_t|/r` 不长期接近 `1`，
就会产生删除势。

## 2. 例外项含义

`TI_t` 不是普通噪声。若它很大，说明 promoted prime `r` 在该相位上近乎非必要：

```text
Tail_{>r} 已经能在大量 zero-cover residue 上完成 H_Q(t)。
```

这正是 `NoDeletion` 的具体形态。因此 `TI_t` 有两种归宿：

```text
TI_t 小：
  支付 DeletionPotential；

TI_t 大：
  promoted prime 非必要，进入 NoDeletion-KL；
  KL 大 => PDEC；
  KL 小 => CleanKLS。
```

## 3. 当前审计

新增脚本：

```text
experiments/prime_matrix_triad_a1_tail_independent_completion_audit.py
```

生成：

```text
docs/monograph/prime-matrix-triad-a1-tail-independent-completion-q2310-q30030.md/json
docs/monograph/prime-matrix-triad-a1-tail-independent-completion-q30030-q510510.md/json
```

审计只统计非空旧洞集上的 zero-cover 幸存；`H=empty` 被单独列为平凡幸存。

| layer | P | nonempty zero-cover slots | TI survivors | killed | TI survival rate | trivial H=empty |
|---|---:|---:|---:|---:|---:|---:|
| 2310->30030 | 17 | 336 | 0 | 336 | 0.000000 | 0 |
| 2310->30030 | 19 | 1548 | 96 | 1452 | 0.062016 | 0 |
| 2310->30030 | 23 | 2344 | 264 | 2080 | 0.112628 | 0 |
| 2310->30030 | 29 | 1360 | 80 | 1280 | 0.058824 | 0 |
| 30030->510510 | 19 | 5760 | 0 | 5760 | 0.000000 | 136 |
| 30030->510510 | 23 | 14088 | 768 | 13320 | 0.054514 | 0 |

读法：

```text
当前 TI 例外项很小；
第二层 P=19 的 zero-cover 幸存主要是 H=empty 平凡情形，不是非空旧洞的 Tail 独立完成。
```

## 4. 对下一硬点的压缩

由 `(TIC-1)`，若沿最小反例族有：

```text
平均 |H_Q(t)|/r 不接近 1；
平均 |TI_t|/r 不接近 1；
```

则 `a_n` 不能接近 `1`，删除势继续增长。

如果 `a_n->1`，则必有：

```text
旧洞几乎占满新增模 r 的残基类；
或 TI_t 例外项巨大。
```

第一种意味着旧洞结构本身过密，可能进入固定层/局部容量矛盾；第二种就是 NoDeletion-KL。

## 5. 当前边界

本文完成：

```text
survival <= occupied residues + TailIndependent exceptions；
非空 zero-cover 幸存的有限审计；
TI 例外项大时自动路由到 NoDeletion-KL。
```

本文未完成：

```text
证明最小反例族中平均 |H_Q(t)|/r 不趋近 1；
证明 TI_t/r 不可长期大，或完成其 NoDeletion-KL 证书；
把 DeletionPotential 发散与最终 LocalSurvivor/容量矛盾完全拼接。
```

下一步最小硬点是 `HoleResidueOccupancy`：研究旧洞集 `H_Q(t)` 在新增素数 `r` 上占用多少 residue。
若它始终远小于 `r`，删除势自动增长；若它接近 `r`，旧洞集已极密，应触发固定层容量矛盾或 PDEC。

## 6. HoleResidueOccupancy 已物化

新增 `prime-matrix-triad-a1-hole-residue-occupancy.md` 后，`(TIC-1)` 中的 `|Occ_t|/r` 已被进一步刚性化：

```text
Occ_t={b: exists c in H_Q(t), ((t+bQ-1)P+c)=0 mod r}
|Occ_t| <= |{c mod r: c in H_Q(t)}| <= min(|H_Q(t)|, r)。
```

两层审计显示当前非空旧洞的 `occupied_rate + TI_rate` 远低于 `1`：

```text
2310->30030: max union bound 0.343590；
30030->510510: max union bound 0.162896。
```

因此当前物化层仍在强删除势区。若未来层删除势失败，只剩两个命名出口：

```text
旧洞 residue 近满占用 => Capacity/PDEC/ColumnCRT；
TI 近满              => NoDeletion-KL/CleanKLS。
```
