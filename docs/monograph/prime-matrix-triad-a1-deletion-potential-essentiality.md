# Triad-A1 DeletionPotential：新增素因子必要性引理

**状态：** `promoted_prime_essentiality_profiled_structural_route_open`

本文继续攻 `DeletionPotential`。目标是解释为什么升层会产生删除势，而不是只记录 `density drop`。

核心观察：

```text
Q' = rQ 时，新增素因子 r 的每个 fiber residue 只覆盖旧洞集 H_Q(t) 的一个 r-残基类；
若该 residue choice 不能让剩余高层完成补洞，则该 fiber 被删除。
```

因此删除势等价于：新增素因子 `r` 的 residue choice 在旧洞集上有多大比例是“必要选择”。

## 1. fiber 生死公式

固定旧活跃相位 `t in A_Q`，旧低洞集为：

```text
H=H_Q(t)。
```

对新层 residue `b in Z/rZ`，新增素因子 `r` 覆盖的旧洞为：

```text
R_b(H)={c in H: ((t+bQ-1)P+c)=0 mod r}。
```

剩余高层记为 `Tail_{>r}`。该 fiber 幸存当且仅当：

```text
H \ R_b(H) 可由 Tail_{>r} 完成。
```

于是

```text
s(t)=#{b: H\R_b(H) is Tail-completable}。
```

这不是概率模型，而是 CRT 分解后的确定性等价。

## 2. 一阶删除界

令

```text
Z_t={b: R_b(H)=empty}。
```

若 `Tail_{>r}` 不能单独完成 `H`，则所有 `b in Z_t` 都死亡。因此：

```text
s(t) <= r-|Z_t|。
```

更强地，若 `Tail_{>r}` 必须由 `r` 至少删去一个关键洞才能完成，则：

```text
s(t) <= #{r-残基类实际命中 H_Q(t)} <= |H_Q(t)|。
```

这给出删除势的结构来源：

```text
old holes occupy few residues mod r
=> most fiber residues do not hit any useful old hole
=> deletion rate large。
```

若反过来大量 zero-cover residue 也能幸存，则新增素因子 `r` 对该相位近乎非必要，已经进入
`NoDeletion` 语义，而不是删除势分支。

## 3. 当前两层审计

新增脚本：

```text
experiments/prime_matrix_triad_a1_deletion_potential_profile.py
```

生成：

```text
docs/monograph/prime-matrix-triad-a1-deletion-potential-profile-q2310-q30030.md/json
docs/monograph/prime-matrix-triad-a1-deletion-potential-profile-q30030-q510510.md/json
```

### 3.1 总删除势

| layer | P | survival | deletion | deletion potential | support hist |
|---|---:|---:|---:|---:|---|
| 2310->30030 | 17 | 0.076923 | 0.923077 | 2.56495 | `{1:28}` |
| 2310->30030 | 19 | 0.202198 | 0.797802 | 1.59851 | `{2:132, 13:8}` |
| 2310->30030 | 23 | 0.310345 | 0.689655 | 1.17007 | `{3:208, 13:24}` |
| 2310->30030 | 29 | 0.312821 | 0.687179 | 1.16213 | `{1:20, 3:2, 4:120, 13:8}` |
| 30030->510510 | 19 | 0.079284 | 0.920716 | 2.53472 | `{1:360, 17:8}` |
| 30030->510510 | 23 | 0.162896 | 0.837104 | 1.81464 | `{2:888, 17:48}` |

### 3.2 zero-cover residue 的生死

`zero-cover` 指 promoted prime 在该 residue 下没有覆盖任何旧洞。当前审计：

| layer | P | zero-cover survived | zero-cover killed | zero-cover survival rate | positive-cover survival rate |
|---|---:|---:|---:|---:|---:|
| 2310->30030 | 17 | 0 | 336 | 0.000000 | 1.000000 |
| 2310->30030 | 19 | 96 | 1452 | 0.062016 | 1.000000 |
| 2310->30030 | 23 | 264 | 2080 | 0.112628 | 1.000000 |
| 2310->30030 | 29 | 80 | 1280 | 0.058824 | 0.898305 |
| 30030->510510 | 19 | 136 | 5760 | 0.023066 | 1.000000 |
| 30030->510510 | 23 | 768 | 13320 | 0.054514 | 1.000000 |

读法：当前大多数 zero-cover residue 都死亡，而 positive-cover residue 几乎都幸存。这说明当前层的
删除势不是噪声，而是“新增素因子必须命中旧洞”的结构必要性。

## 4. 对 DeletionPotential 的可攻路径

若沿无限塔反例仍停留在删除势分支，则需要证明：

```text
zero-cover residue 的死亡比例不可求和；
或等价地，promoted prime 长期必须命中旧洞才能让 fiber 幸存。
```

一个一般充分条件是：

```text
Tail_{>r} 对 H_Q(t) 的独立完成能力不足；
且 H_Q(t) 占用的 r-残基类比例 bounded away from 1。
```

此时

```text
s(t)/r <= occupied_residues_r(H_Q(t))/r + tail-independent-exception。
```

若这个上界在正质量相位上长期小于 1，就得到 `sum D_n=infinity`。

若该充分条件失败，则失败本身有明确含义：

```text
Tail_{>r} 已能在大量 zero-cover residues 上完成 H_Q(t)。
```

这正是 `NoDeletion`：新增素因子 `r` 近乎非必要。于是回到 `NoDeletion-KL`：

```text
若 tail completion 有偏斜 => PDEC；
若 tail completion 平坦 => CleanKLS。
```

## 5. 当前边界

本文完成：

```text
promoted prime 删除势的确定性生死公式；
zero-cover death 作为删除势来源的有限审计；
DeletionPotential 失败自动进入 NoDeletion-KL 的结构路由。
```

本文未完成：

```text
证明任意最小反例族中 zero-cover death 比例不可求和；
Tail_{>r} 独立完成能力不足的一般不等式；
NoDeletion 后 PDEC/CleanKLS 证书全集。
```

所以下一步最小硬点是 `TailIndependentCompletion`：证明在正式反例族中，剩余高层不能长期不依赖 promoted prime
就完成旧洞集；否则该“不依赖”必须表现为低 KL 平坦或可命名 PDEC 偏斜。

## 6. TailIndependentCompletion 接入

新增 `prime-matrix-triad-a1-tail-independent-completion.md` 后，Tail 独立完成被单独登记为例外项 `TI_t`。
对非空旧洞集：

```text
s(t)/r <= |H_Q(t)|/r + |TI_t|/r。
```

当前两层审计显示 `TI_t` 很小；特别是 `30030->510510, P=19` 的 zero-cover 幸存全部来自 `H=empty`
平凡情形，非空旧洞的 `TI` 幸存为 `0`。

因此下一硬点从 `TailIndependentCompletion` 进一步压成：

```text
HoleResidueOccupancy:
  控制 |H_Q(t)|/r；
  若 |H_Q(t)|/r 不接近 1 且 TI_t 小，则删除势继续增长；
  若 |H_Q(t)|/r 接近 1，则旧洞集过密，进入容量/PDEC。
```
