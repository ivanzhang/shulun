# Triad-A1 TailUnitDensity KL 下界

**状态：** `tail_unit_density_kl_floor_proved_current_layers_audited`

本文继续收紧 `TailCapacityPressure` 中的 KL 门。核心结论是：只要残余洞集非空，Tail 完成集合就不可能接近整个 Tail CRT 空间，除非 Tail 的未命中密度本身趋零。

## 1. 单洞未命中体积

固定 Tail 素数集合：

```text
L={ell: ell<P, ell not| Q'}。
```

Tail CRT 空间大小为：

```text
M_tail=prod_{ell in L} ell。
```

取任一非空残余洞集 `Residual_b` 中的一个洞 `c0`。对每个 `ell in L`，`ell` 覆盖 `c0` 只对应一个 `y mod ell` 残基。因此 `ell` 不覆盖 `c0` 的比例是：

```text
1-1/ell。
```

由 CRT 独立性，所有 Tail 素数都不覆盖 `c0` 的比例为：

\[
u_{\rm tail}
=
\prod_{\ell\in L}\left(1-{1\over \ell}\right).
\tag{TUD-1}
\]

## 2. 完成集合上界

若 Tail 完成整个 `Residual_b`，它至少必须覆盖 `c0`。所以完成集合满足：

\[
{m_b\over M_{\rm tail}}
\le
1-u_{\rm tail}.
\tag{TUD-2}
\]

这不依赖残余洞集的其他结构，是对任意非空残余洞的统一上界。

因此正式坏窗质量若必须落在完成集合中，则相对 Tail 均匀基准支付：

\[
D_{\rm KL}
\ge
-\log(1-u_{\rm tail}).
\tag{TUD-3}
\]

## 3. 极限二分

若沿无限最小反例族存在大量非空残余洞幸存，并且：

```text
u_tail >= eta > 0，
```

则每层支付正 KL 成本：

```text
D_KL >= -log(1-eta)。
```

于是只能进入：

```text
KL 累计 => PDEC。
```

若要避免 KL 累计，则必须发生：

```text
u_tail -> 0
或
非空残余洞幸存质量 -> 0。
```

第二种回到 promoted-prime 删除/空残余洞分支；第一种表示 Tail 素数层极厚，Tail 对单洞的覆盖概率趋满。此时若仍没有 PDEC，就必须满足 CleanKLS/DLS admission：所有低模、列位移、短窗和系数集中缺陷都已剥离。

所以 `TailCapacityPressure` 后没有新的无名出口：

```text
非空残余洞 + u_tail 不小 => KL/PDEC；
非空残余洞消失          => 删除/空洞分支；
u_tail -> 0 且无偏斜     => CleanKLS/DLS。
```

## 4. 当前审计

新增脚本：

```text
experiments/prime_matrix_triad_a1_tail_unit_density_gate.py
```

生成：

```text
docs/monograph/prime-matrix-triad-a1-tail-unit-density-gate.md/json
```

当前审计：

```text
all_unit_density_bounds_pass=True。
```

核心表：

| layer | P | u_tail | 1-u_tail | KL floor | positive residual survival | max actual completion ratio | positive actual avg KL |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2310->30030 | 17 | 1.000000 | 0.000000 | infinity | 0.000000 | 0.000000 | infinity |
| 2310->30030 | 19 | 0.941176 | 0.058824 | 2.833213 | 0.198675 | 0.058824 | 2.833213 |
| 2310->30030 | 23 | 0.891641 | 0.108359 | 2.222304 | 0.310345 | 0.108359 | 4.937726 |
| 2310->30030 | 29 | 0.852874 | 0.147126 | 1.916465 | 0.312821 | 0.015076 | 6.996641 |
| 30030->510510 | 19 | 1.000000 | 0.000000 | infinity | 0.000000 | 0.000000 | infinity |
| 30030->510510 | 23 | 0.947368 | 0.052632 | 2.944439 | 0.160363 | 0.052632 | 2.944439 |

读法：

```text
实际最大完成比例全部被 1-u_tail 压住；
非空残余洞幸存时，正 KL 下界已经出现；
残余洞为空的幸存不属于此 KL 门，而回到 promoted-prime 命中旧洞的删除/占用账本。
```

## 5. 对总链的作用

`TailUnitDensity` 把 `容量成功但 KL 不大` 的逃逸再压窄：

```text
若 residual nonempty 且 u_tail 不小：
  KL 不可能小；

若 KL 小：
  residual nonempty 的幸存质量必须消失，
  或 u_tail 必须趋零并进入 CleanKLS admission。
```

这正是用户要求的“无穷层叠但非固定常数”结构：每层不需要固定同一个常数，只需要登记本层自带的 `u_tail`。若这些局部 KL 成本累计，就进入 PDEC；若不累计，剩余对象自动满足更平坦的 CleanKLS 入口。
