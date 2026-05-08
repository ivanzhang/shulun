# Prime Matrix 早期零行 cofactor 深度分层路由器

**状态：** `cofactor_depth_gate_closed_primepair_and_recursive_capacity_open`

本步修正并强化 carry-shell 口径：`m=P-b` 是 x-rough cofactor，不必总是素数；但一旦 `x>=sqrt(P)`，它必为素数。因此早期零行剩余被拆成两块：大范围真双素 carry-shell 容量，以及 `x<sqrt(P)` 的复合 cofactor 递归下降/命名回流。

```text
cofactor_depth_gate_closed=true
sqrt_gate_prime_cofactor_closed=true
primepair_carry_shell_capacity_closed=false
recursive_cofactor_capacity_closed=false
row_column_unconditional_closed=false
```

## 1. Cofactor 深度门

设 `c in R_x` 被高素斜线补掉：

```text
xP+c = q m,   x<q<P.
```

上一轮已证明 `x<m<P`。同时 `c in R_x` 表示 `xP+c` 没有不超过 `x` 的素因子，因此 `m` 的每个素因子也都大于 `x`。

若 `Omega(m)=d` 是带重数素因子数，则

```text
m > x^d,   m<P,   因而 d < log(P)/log(x).
```

特别地，当 `x>=sqrt(P)` 时，复合 `m` 至少含两个大于 `x` 的素因子，给出 `m>x^2>=P`，矛盾。所以：

```text
x>=sqrt(P)  =>  m is prime.
```

这把 carry-shell 分成真双素壳和早期复合 cofactor 递归壳。

## 2. 递归回流

当 `x<sqrt(P)` 且 `m` 复合时，`m` 是一个小于 `P` 的 x-rough 数，且所有因子仍在 `>x` 的同一粗骨架内。
若这种复合 cofactor 壳在反例族中持久集中，它就是同 formal unit 的 PDEC 支撑；若只孤立出现，则进入 SAE/LocalSurvivor。
因此复合 cofactor 不是新出口，而是递归下降或命名回流。

## 3. 判定表

| gate | closed | proved | meaning | output |
| --- | --- | --- | --- | --- |
| `CarryShellImported` | `true` | `true` | 上一轮已把高补洞支撑压到带进位壳。 | `继续分解 cofactor m 的乘法深度。` |
| `CofactorWindowAndRoughness` | `true` | `true` | 若 c in R_x 且 xP+c=q m，则 x<m<P，且 m 没有 <=x 的素因子。 | `m 是小于 P 的 x-rough cofactor。` |
| `DepthBound` | `true` | `true` | 若 Omega(m)=d，则 m>x^d 且 m<P，所以 d<log(P)/log(x)。 | `cofactor 深度随 x 增大快速塌缩。` |
| `SqrtGatePrimeCofactor` | `true` | `true` | 当 x>=sqrt(P) 时，复合 m 至少含两个 >x 因子，导致 m>x^2>=P，矛盾。 | `x>=sqrt(P) 的 carry-shell 是真 prime-pair shell。` |
| `CompositeCofactorRecursiveReturn` | `true` | `true` | 若 x<sqrt(P) 且 m 复合，则 m 的全部因子仍在同一 x-rough 递归壳内；持久集中进入 PDEC，孤立进入 SAE。 | `CompositeCofactorDepthRecursivePDECReturnOrSAE。` |
| `SchemaCompatibility` | `true` | `true` | cofactor 深度分层仍使用上一轮同 formal unit 和 SAE/LocalSurvivor 回流纪律。 | `不是新终端。` |
| `SampleDepthAudit` | `true` | `false` | 样本中所有复合 cofactor 都只出现在 x<sqrt(P) 的早期带；这只是审计。 | `cofactor_depth_gate_sample_verified_theorem_algebraic_recursive_capacity_open` |
| `PrimePairCarryShellCapacity` | `false` | `false` | 尚未证明 x>=sqrt(P) 的真双素 carry-shell 容量不能覆盖全部 R_x。 | `PrimePairCarryShellCapacityBoundOrPDECReturn。` |
| `RecursiveCofactorCapacity` | `false` | `false` | 尚未证明 x<sqrt(P) 的复合 cofactor 递归壳必下降到 survivor 或命名 PDEC/SAE 排斥。 | `CompositeCofactorDepthDescentOrNamedReturn。` |

## 4. 样本审计

样本只用于复核分层口径；`sqrt` 门由上面的不等式直接证明。

```text
sample_status=cofactor_depth_gate_sample_verified_theorem_algebraic_recursive_capacity_open
all_composite_only_before_sqrt_gate=true
```

| P | total high filler | prime cofactor | composite cofactor | max depth | composite after sqrt gate |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 101 | 362 | 291 | 71 | 6 | 0 |
| 499 | 4778 | 4312 | 466 | 8 | 0 |
| 997 | 14788 | 13730 | 1058 | 9 | 0 |

## 5. 新最窄剩余

本步把 `CarryShellPrimitiveCapacityBoundOrPDECReturn` 进一步拆成：

```text
PrimePairCarryShellCapacityAndCompositeCofactorDepthDescent
  = PrimePairCarryShellCapacityBoundOrPDECReturn
    AND CompositeCofactorDepthDescentOrNamedReturn
    AND EarlyBandLocalSurvivorOrSAEExclusion.
```

其中第一项处理 `x>=sqrt(P)` 的真双素壳，第二项处理 `x<sqrt(P)` 的复合 cofactor 递归壳，第三项处理递归不能持久化时的孤窗证书。
这仍是自足路线中的结构压缩；尚未给出最终容量排斥。
