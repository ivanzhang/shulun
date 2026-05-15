# Prime Matrix square-phase bad-tail single-variable router

**状态：** `square_phase_bad_tail_reduced_to_shifted_composite_cofactor_slot_bound_open`

坏尾命中已经从高尾覆盖问题压成单变量槽余因子问题：对每个尾素 `q=P-a`，plus 侧全部命中满足 `r=tq-a^2, m=P+a+t`；minus 侧全部命中满足 `r=a^2-tq, m=P+a+t`，其中整数槽 `t` 由 `1<=r<P` 限定为一到两个值。该槽命中是 `BadTail` 当且仅当 `m` 为合数。因此下一步只需控制这些移位余因子合数槽的数量，或证明其过密形成 t 层上的 PDEC/SAE。

```text
max_p=5000
finite_prime_count=668
identity_failure_count=0
bad_tail_composite_cofactor_slot_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 单变量槽公式

令 `y=floor(4P/5)`，取尾素 `q` 满足 `y<q<P`，写 `q=P-a`。因为 `q>4P/5`，每个 `q` 在 `1<=r<P` 中逐侧只命中一到两个相位槽。

plus 侧所有槽由整数 `t` 给出：

```text
r_+(a,t)=t(P-a)-a^2
P^2+r_+(a,t)=(P-a)(P+a+t)
1<=r_+(a,t)<P
```

minus 侧所有槽由整数 `t` 给出：

```text
r_-(a,t)=a^2-t(P-a)
P^2-r_-(a,t)=(P-a)(P+a+t)
1<=r_-(a,t)<P
```

所以坏尾不再需要二维搜索：它等价于这些槽上的 `P+a+t` 为合数。

## 2. 确定性判据

| name | status | statement |
| --- | --- | --- |
| `tail_prime_one_or_two_slots` | `closed` | For alpha=4/5, every tail prime q in (4P/5,P) hits one or two r slots in 1<=r<P on each side. |
| `single_variable_slot_cofactor_formula` | `closed` | Writing q=P-a, all plus slots have r=tq-a^2 and m=P+a+t; all minus slots have r=a^2-tq and m=P+a+t, for the integer t range forced by 1<=r<P. |
| `bad_tail_equivalence` | `closed` | The tail hit is BadTail exactly when the slot cofactor m=P+a+t is composite. |
| `remaining_shifted_composite_slot_bound` | `open` | A global proof needs a bound for composite slot values P+a+t along tail-prime parameters q=P-a, or a PDEC/SAE return. |

## 3. 有限审计摘要

| metric | plus | minus |
| --- | ---: | ---: |
| distinct tail primes | 38678 | 38678 |
| tail slots | 43278 | 43081 |
| good cofactor prime slots | 5046 | 5343 |
| bad composite cofactor slots | 38232 | 37738 |

- plus 最大坏尾比例样本：`P=13`，`bad/slots=1/1`。
- minus 最大坏尾比例样本：`P=13`，`bad/slots=1/1`。
- plus 最大 `t`：`P=4999`，`max_t=250`。
- minus 最大 `t`：`P=4999`，`max_t=248`。

## 4. 样本表

| P | sign | tail primes | slots | good m prime | bad m composite | bad ratio | t range | bad t range |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 13 | `plus` | 1 | 1 | 0 | 1 | 1.0000 | 1..1 | 1..1 |
| 13 | `minus` | 1 | 1 | 0 | 1 | 1.0000 | 0..0 | 0..0 |
| 17 | `plus` | 0 | 0 | 0 | 0 | 0.0000 | 0..0 | 0..0 |
| 17 | `minus` | 0 | 0 | 0 | 0 | 0.0000 | 0..0 | 0..0 |
| 19 | `plus` | 1 | 1 | 0 | 1 | 1.0000 | 1..1 | 1..1 |
| 19 | `minus` | 1 | 1 | 0 | 1 | 1.0000 | 0..0 | 0..0 |
| 23 | `plus` | 1 | 2 | 1 | 1 | 0.5000 | 1..2 | 1..1 |
| 23 | `minus` | 1 | 1 | 0 | 1 | 1.0000 | 0..0 | 0..0 |
| 29 | `plus` | 0 | 0 | 0 | 0 | 0.0000 | 0..0 | 0..0 |
| 29 | `minus` | 0 | 0 | 0 | 0 | 0.0000 | 0..0 | 0..0 |
| 31 | `plus` | 1 | 1 | 0 | 1 | 1.0000 | 1..1 | 1..1 |
| 31 | `minus` | 1 | 1 | 0 | 1 | 1.0000 | 0..0 | 0..0 |
| 101 | `plus` | 3 | 4 | 0 | 4 | 1.0000 | 1..5 | 1..5 |
| 101 | `minus` | 3 | 3 | 0 | 3 | 1.0000 | 0..3 | 0..3 |
| 499 | `plus` | 16 | 18 | 2 | 16 | 0.8889 | 1..25 | 1..25 |
| 499 | `minus` | 16 | 18 | 1 | 17 | 0.9444 | 0..23 | 0..23 |
| 1009 | `plus` | 29 | 32 | 7 | 25 | 0.7812 | 1..50 | 1..49 |
| 1009 | `minus` | 29 | 34 | 7 | 27 | 0.7941 | 0..49 | 0..49 |
| 2003 | `plus` | 51 | 54 | 7 | 47 | 0.8704 | 1..98 | 1..98 |
| 2003 | `minus` | 51 | 57 | 5 | 52 | 0.9123 | 0..97 | 0..97 |
| 4999 | `plus` | 118 | 134 | 17 | 117 | 0.8731 | 1..250 | 1..249 |
| 4999 | `minus` | 118 | 128 | 14 | 114 | 0.8906 | 0..248 | 0..248 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SingleVariableSlotBadTailFormulaClosed` | `true` | `true` | 每个尾素命中的全部 r 槽和余因子 m 都由 a=P-q 与整数槽 t 的单变量公式给出。 | closed |
| `BadTailCompositeCofactorSlotBound` | `false` | `false` | 仍需全局约束 m=P+a+t 为合数的尾素槽数量。 | SquarePhaseBadTailShiftedCompositeCofactorSlotBound |
| `ShiftedCofactorSlotPDECReturn` | `false` | `false` | 若复合余因子过密，需抽取按 t 槽层分布的低模相位异常。 | SquarePhaseBadTailShiftedCofactorSlotPDECSAEReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭 BadTail 的单变量槽参数化，不关闭全局行/列命题。 | SquarePhaseBadTailShiftedCompositeCofactorSlotBound OR SquarePhaseBadTailShiftedCofactorSlotPDECSAEReturn |

## 6. 下一步

- 主攻：`SquarePhaseBadTailShiftedCompositeCofactorSlotBound`。
- 备选回流：`SquarePhaseBadTailShiftedCofactorSlotPDECSAEReturn`。
- 具体要证明：沿尾素参数 `q=P-a` 与一到两个槽 `t`，移位余因子 `P+a+t` 的合数命中不能持续多到压过平方锚素数数；若过密，则按 `t` 层和最小因子层抽取相位缺陷。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-bad-tail-single-variable-ledger.json` | `518f490c8eaba3cdbbb103293a36be0bb11bdde170f677f337cdcdc9d6dc0be7` |
| `experiments/prime_matrix_square_phase_bad_tail_single_variable_router.py` | `b669535af4b91ddf645b893489a6e579435d43a8f1f6e4a80803fd170385e985` |
