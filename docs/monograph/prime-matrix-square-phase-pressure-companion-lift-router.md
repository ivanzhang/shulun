# Prime Matrix square-phase pressure companion-lift router

**状态：** `registered_pressure_pdec_exclusion_reduced_to_companion_lift_open`

本步把已登记压力 PDEC 的排斥进一步压成 companion-lift 门：RootWindowDefect 要成为终端反例，必须由 k>=1 伴随分支补足 `ceil(PrimeWindow/2)-RootLoad`；KGe1AggregatePressureDefect 要成为终端反例，必须由 k0 伴随分支补足 `ceil(PrimeWindow/2)-KGe1Load`。有限登记样本的 companion gap 全为负，因此都没有终端化；全局仍需证明这种同侧伴随补量不能持久出现。

```text
max_p=5000
finite_prime_count=668
registered_pressure_defect_count=4
terminalized_registered_defect_count=0
row_column_unconditional_closed=false
```

## 1. Companion-lift 公式

RootWindow 分支：

```text
RootWindowDefect terminalizes iff KGe1Load >= ceil(PrimeWindow/2)-RootLoad.
```

KGe1 分支：

```text
KGe1AggregateDefect terminalizes iff RootLoad >= ceil(PrimeWindow/2)-KGe1Load.
```

因此压力缺陷本身不是终端矛盾；它必须与同一 `P,side` 的 companion 分支同时贴合。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| registered pressure defects | 4 |
| RootWindow pressure defects | 3 |
| KGe1 pressure defects | 1 |
| terminalized registered defects | 0 |
| min companion gap | -5 |
| max companion gap | -1 |

## 3. 关键 companion gap

| label | P | side | branch | PrimeWindow | branch loads `(k0,k>=1)` | companion needed | companion available | gap | terminalized |
| --- | ---: | --- | --- | ---: | --- | ---: | ---: | ---: | --- |
| worst gap | 523 | plus | KGe1AggregatePressureDefect | 36 | [3, 10] | 8 | 3 | -5 | `false` |
| best gap | 13 | plus | RootWindowDefect | 3 | [1, 0] | 1 | 0 | -1 | `false` |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `rootwindow_terminalization_companion_lift` | `closed` | A RootWindow pressure defect becomes terminal only if KGe1Load>=ceil(PrimeWindow/2)-RootLoad. |
| `kge1_terminalization_companion_lift` | `closed` | A KGe1 pressure defect becomes terminal only if RootLoad>=ceil(PrimeWindow/2)-KGe1Load. |
| `registered_pressure_defect_terminalization_equivalence` | `closed` | For registered pressure defects, terminality is exactly companion-lift nonnegative gap. |
| `companion_lift_exclusion` | `open` | A global proof still needs to exclude companion-lift for the registered pressure families. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `RootWindowCompanionLiftFormulaClosed` | `true` | `true` | RootWindow 缺陷要终端化，k>=1 伴随负载必须补足阈值缺口。 | closed |
| `KGe1CompanionLiftFormulaClosed` | `true` | `true` | KGe1 缺陷要终端化，k0 伴随负载必须补足阈值缺口。 | closed |
| `FiniteNoRegisteredCompanionLift` | `true` | `false` | 有限扫描 P<=5000 中已登记压力缺陷都未获得伴随补量。 | finite evidence only |
| `CompanionLiftExcludedGlobally` | `false` | `false` | 仍需全局证明两个压力 family 不能同时得到同侧伴随分支补量。 | PressureDefectCompanionLiftExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 PDEC 排斥压成 companion-lift 排斥，不关闭全局行/列命题。 | PressureDefectCompanionLiftExclusion |

## 6. 下一步

- 主攻：`PressureDefectCompanionLiftExclusion`。
- 具体要证明同一 `P,side` 下，压力缺陷分支与 companion 补量不能同时达到终端阈值；或登记更高阶 joint PDEC。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_pressure_companion_lift_router.py` | `703c5ec11e8774efb49f0c77d6ed1602ba560b2a1d3040292ae981515333f652` |
| `experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py` | `e76e3d8cd721359fca8f6eaf0524787010ed2507ba471a448747d9ee6282c970` |
| `data/square-phase-pressure-companion-lift-ledger.json` | `8c33359a34d68781d29c7be516d6c4ce887113be23815acdcfecb250170c37c6` |
