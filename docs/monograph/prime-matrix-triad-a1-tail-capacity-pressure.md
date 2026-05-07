# Triad-A1 TailCapacityPressure 引理

**状态：** `tail_capacity_pressure_reduced_to_deletion_or_kl`

本文承接 `OccupancySaturation`。目标是把：

```text
旧洞 residue 近满 + 大量 fiber 幸存
```

压成一个确定性二分：

```text
Tail 容量不足 => fiber 死亡，删除势继续增长；
Tail 仍能完成 => Tail 完成集合很小，产生 KL/PDEC/CleanKLS 压力。
```

## 1. 残余洞集

固定升层 `Q'=rQ`、旧相位 `t`、旧洞集 `H=H_Q(t)`。对 residue `b`：

```text
R_b(H)={c in H: ((t+bQ-1)P+c)=0 mod r}
Residual_b=H\R_b(H)
```

`b` 幸存当且仅当 `Tail_{>r}` 能完成 `Residual_b`。

设 Tail 素数集合为：

```text
L={ell: ell<P, ell not| Q'}。
```

对每个 `ell in L` 与 `y mod ell`，定义覆盖集：

```text
C_ell(a)={c in Residual_b: ((t+bQ-1)P+c)+Q'P y =0 mod ell}
```

于是 Tail 完成等价于存在一组 residue `a_ell` 使：

```text
Residual_b subset union_{ell in L} C_ell(a_ell)。
```

这正是脚本中 `high_completion_stats` 的 CRT set-cover DP。

## 2. 容量门

定义简单容量：

```text
Cap_1(Residual_b)=sum_{ell in L} max_a |C_ell(a)|。
```

若：

```text
|Residual_b| > Cap_1(Residual_b)，
```

则任何 Tail residue 选择都无法覆盖全部残余洞，所以：

```text
b notin S_t。
```

更强地，对任意子集 `W subset Residual_b`，若：

```text
|W| > sum_{ell in L} max_a |C_ell(a) cap W|，
```

则同样不可能完成。这是 Hall 型亏损门。

## 3. KL 压力门

令：

```text
M_tail=prod_{ell in L} ell。
```

设 `m_b` 是能完成 `Residual_b` 的 Tail CRT 选择数。若 `m_b=0`，fiber 死亡。

若 `m_b>0`，但正式坏窗质量必须全部落在这些完成选择中，则相对 Tail 均匀基准的条件 KL 至少为：

\[
D_{\rm KL}
\ge
\log {M_{\rm tail}\over m_b}.
\tag{TCP-1}
\]

因此，若删除不发生且大量幸存 fiber 的 `m_b/M_tail` 很小，就不能保持无偏平坦；只能进入：

```text
KL 累计     => new-layer/PDEC；
KL 可求和   => CleanKLS/DLS admission。
```

这正是 `NoDeletion-KL` 的局部容量来源。

## 4. 与 OccupancySaturation 的拼接

`OccupancySaturation` 给出：

```text
无删除且非 TI
=> 多数 t 满足 |Occ_t|/r 近 1
=> 多数旧洞集 H 在 r-residue 上近满且 |H| 近 r。
```

对这些相位，若 promoted prime 每个 `b` 只删除少量旧洞，则 `Residual_b` 仍大。

于是：

```text
Residual_b 大于 Tail 容量:
  b 死亡，删除势恢复；

Residual_b 可由 Tail 完成:
  完成集合 m_b 通常远小于 M_tail，
  正式质量被压进小集合，支付 KL。
```

所以 `OccupancySaturation` 不能成为无名逃逸；它被 `TailCapacityPressure` 吸收。

## 5. 当前两层审计

新增脚本：

```text
experiments/prime_matrix_triad_a1_tail_capacity_pressure_audit.py
```

生成：

```text
docs/monograph/prime-matrix-triad-a1-tail-capacity-pressure-q2310-q30030.md/json
docs/monograph/prime-matrix-triad-a1-tail-capacity-pressure-q30030-q510510.md/json
```

审计一致性：

```text
consistency_mismatch_count=0
```

说明逐槽残余洞 DP 与 lift 层 `M(t+bQ)` 完全同口径。

核心结果：

| layer | P | survival | Hall dead | Hall uncert dead | avg KL floor | max KL floor |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2310->30030 | 17 | 0.076923 | 0.923077 | 0 | 0.000000 | 0.000000 |
| 2310->30030 | 19 | 0.202198 | 0.797802 | 0 | 2.771622 | 2.833213 |
| 2310->30030 | 23 | 0.310345 | 0.689655 | 0 | 4.937726 | 5.084505 |
| 2310->30030 | 29 | 0.312821 | 0.687179 | 0 | 6.996641 | 7.121387 |
| 30030->510510 | 19 | 0.058824 | 0.941176 | 0 | 0.000000 | 0.000000 |
| 30030->510510 | 23 | 0.162896 | 0.837104 | 0 | 2.889912 | 2.944439 |

读法：

```text
当前所有死亡槽位均由 Hall/capacity 亏损解释；
没有 hall_uncertified dead slot；
幸存槽位若 Tail 非平凡，则已经带有正 KL 下界。
```

## 6. 当前闭合位置

`DeletionPotential` 现在变成：

```text
Occ+TI 不满:
  删除势增长；

TI 近满:
  NoDeletion-KL / CleanKLS；

Occ 近满:
  TailCapacityPressure；
    residual capacity fails => 删除势增长；
    residual capacity succeeds in small Tail set => KL/PDEC/CleanKLS。
```

因此 A1 new-layer 分支中，“旧洞近满占用”已经不再是逃逸口，而是会被容量或 KL 吸收的中间状态。

尚未完成的是终端证书全集：

```text
PDEC 排斥；
CleanKLS/DLS 大筛；
Sparse/LocalSurvivor 与最终行命题拼接。
```

## 7. TailUnitDensity KL 下界已补入

新增 `prime-matrix-triad-a1-tail-unit-density-kl-floor.md` 后，`TailCapacityPressure` 中的 KL 门获得统一下界。

对任一非空残余洞集，取一个洞 `c0`。Tail 全部不命中 `c0` 的密度为：

```text
u_tail=prod_{ell in Tail}(1-1/ell)。
```

因此：

```text
m_b/M_tail <= 1-u_tail；
KL >= -log(1-u_tail)。
```

当前审计 `all_unit_density_bounds_pass=True`。这说明“容量成功但完成集合接近满层”的情况，只有在
`u_tail->0` 或非空残余洞幸存质量消失时才可能逃过 KL；前者进入 CleanKLS/DLS，后者回到删除/空洞分支。
