# Triad-A1 Canonical Selector Retention 路由审计

**状态：** `selector_retention_reduced_to_finite_signature_no_cancellation_or_clean_return`

CanonicalSelectorRetention 已被压成有限签名 pigeonhole：若 exact RIW/Buchstab 路径签名数只有 log^J 个，则最大签名自动保留 log-power 支撑。真正剩余是把 K6 有限标签严格提升为 exact coefficient path partition，并证明所选路径无抵消；失败时必须回到 clean 退出口。

## 1. 有限签名保留律

Selector retention can be proved by a finite-signature pigeonhole principle, not by new density estimates. If the raw thick Buchstab support is partitioned into at most log^J exact RIW path signatures, then the maximal signature retains at least a log^-J fraction. This is enough whenever the Buchstab loss E plus signature loss J does not exceed the support budget C. The remaining exact obstruction is no-cancellation of selected paths and the clean-return contract for failures.

```text
raw support S is partitioned into at most log^J exact signatures;
max signature support >= S/log^J;
if raw S >= interval/log^E and E+J<=C:
  retained support >= interval/log^C;
remaining issue: unique path/no cancellation, or clean return.
```

## 2. 汇总

- `layer_transfer_input_status=layer_transfer_reduced_to_selector_retention_or_clean_return`。
- `layer_transfer_input_next_target=CanonicalSelectorRetentionOrCleanReturn`。
- `all_signature_rows_suffice=True`。
- `conditional_finite_signature_implies_selector_retention=True`。
- `selector_retention_closed=False`。
- `next_internal_target=FiniteSignatureNoCancellationOrCleanReturn`。
- `terminal_gap_after_router=FiniteSignatureNoCancellationOrCleanReturnOrExternalDIBFIOriginalDispersion`。

## 3. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `FiniteSignaturePartition` | K6/tail-label bookkeeping gives polylog-many dyadic labels | raw thick Buchstab support is partitioned into <= log^J exact selector signatures | polylog labels are known abstractly, but not yet tied to exact RIW coefficient paths | define RIW path signature including parity, dyadic bin and truncation state | `False` |
| `MaxSignatureRetention` | finite partition once the previous gate is fixed | one canonical signature retains at least raw_support/log^J | none after finite partition; this is pigeonhole | choose canonical maximal signature with deterministic tie-break | `True` |
| `UniquePathNoCancellation` | Buchstab recursion suggests a decision-tree decomposition | one product belongs to one selected path or same-path coefficient is nonzero | without unique path, different signed paths could cancel the same product | prove path signatures are disjoint, or refine signature until disjoint | `False` |
| `SelectorRetentionCleanReturn` | edge/PDEC/SAE exits exist | if finite signature retention or unique-path noncancellation fails, block exits clean A1 | this contrapositive clean contract is not yet recorded | low-retention or multi-path cancellation must be named as tail-label/PDEC failure | `False` |
| `FiniteSignatureImpliesSelectorRetention` | max-signature pigeonhole plus no-cancellation | retained nonzero support >= interval/log^C | conditional implication is direct; finite partition/no-cancellation/return remain | combine finite signatures with E+J<=C | `True` |

## 4. 签名保留模型

| k | log y | raw support | signature count | max signature support | required support | suffices |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3 | 6.90776 | 15728.4 | 6.90776 | 2276.92 | 2276.92 | `True` |
| 4 | 9.21034 | 66279.4 | 9.21034 | 7196.19 | 7196.19 | `True` |
| 5 | 11.5129 | 202269 | 11.5129 | 17568.8 | 17568.8 | `True` |
| 6 | 13.8155 | 503309 | 13.8155 | 36430.7 | 36430.7 | `True` |
| 7 | 16.1181 | 1.08785e+06 | 16.1181 | 67492.4 | 67492.4 | `True` |
| 8 | 18.4207 | 2.12094e+06 | 18.4207 | 115139 | 115139 | `True` |
| 9 | 20.7233 | 3.822e+06 | 20.7233 | 184431 | 184431 | `True` |

## 5. 结论

新最窄内部目标为：

```text
FiniteSignatureNoCancellationOrCleanReturn:
  promote K6/polylog labels to an exact RIW path-signature partition;
  prove selected path signatures are disjoint or non-cancelling;
  otherwise return the failed block to edge/PDEC/SAE.
```

这一步把 selector retention 的数量问题化为有限签名 pigeonhole；剩余是 exact 路径分割与无抵消的结构合同。
