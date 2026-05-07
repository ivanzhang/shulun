# Triad-A1 SquarefreeBuchstabLayerSupport 路由审计

**状态：** `raw_thick_squarefree_support_closed_layer_transfer_open`

SquarefreeBuchstabLayerSupportLowerBound 的原始计数层已经被压下去：在厚的 surviving balanced interval 中，Mertens/Buchstab 型下界足以提供 log-power 级 squarefree product 支撑。真正剩余不再是“有没有足够 squarefree 数”，而是 exact canonical RIW/Buchstab 层是否承认这些 product 且系数非零；若区间太薄，则必须严格回到 edge/PDEC/SAE。

## 1. 结构二分律

The counting part of the squarefree Buchstab support problem is not the terminal obstruction: in any thick admitted balanced interval, Mertens/Buchstab gives interval/log^E many squarefree products, enough for the requested log-power support. The remaining obstruction is exactness: the canonical RIW layer must admit those products with nonzero coefficients, and intervals too thin for this argument must be forced back to an existing edge/PDEC/SAE exit.

```text
if balanced interval is thick and admitted by the canonical layer:
  Mertens/Buchstab gives many squarefree products;
  nonzero coefficient transfer gives alpha/delta absolute support;
else:
  the interval is thin or layer-rejected and must return to edge/PDEC/SAE.
```

## 2. 汇总

- `canonical_input_status=canonical_riw_support_reduced_to_squarefree_buchstab_layer_support`。
- `canonical_input_next_target=SquarefreeBuchstabLayerSupportLowerBound`。
- `raw_thick_squarefree_support_closed=True`。
- `conditional_admitted_layer_implies_squarefree_support=True`。
- `squarefree_buchstab_layer_support_closed=False`。
- `next_internal_target=CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn`。
- `terminal_gap_after_router=CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturnOrExternalDIBFIOriginalDispersion`。

## 3. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `ThickMertensBuchstabSupport` | standard Mertens/Buchstab lower-sieve density on long dyadic intervals | raw squarefree Buchstab products >= interval/log^C in thick admitted blocks | not a Kloosterman gap; it is closed once the block is thick and layer-admitted | use Mertens product plus Buchstab recursion for squarefree product count | `True` |
| `CanonicalLayerAdmission` | previous router asks for a fixed canonical RIW/Buchstab factorization | the exact canonical layer admits the raw squarefree products being counted | a formal well-factorable splitting could select or cancel a sparse sublayer | record the exact layer selector and prove it covers every surviving balanced block | `False` |
| `NonzeroCoefficientTransfer` | divisor-bounded RIW factors and squarefree support model | admitted products have nonzero alpha/delta coefficients with no parity cancellation | absolute support lower bound needs coefficient nonvanishing, not just product existence | prove layer parity/sign rule leaves a nonzero coefficient on each admitted product | `False` |
| `ThinBalancedIntervalReturn` | edge/PDEC/SAE exits exist elsewhere in the A1 ledger | blocks below the Buchstab thickness threshold cannot remain in clean A1 | thinness must be connected to an existing named exit, not silently discarded | prove thin support implies endpoint/edge/tail-label failure and return to PDEC/SAE | `False` |
| `AdmittedSupportImpliesCanonicalRIWSupport` | previous router already proved the final support-to-RIW implication | thick support + layer admission + nonzero transfer + thin return | conditional implication is elementary; the admission/return gates remain | combine the four gates above | `True` |

## 4. 厚区间支撑模型

| k | log y | interval size | thin threshold | raw support | required support | suffices |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3 | 6.90776 | 750514 | 15728.4 | 15728.4 | 2276.92 | `True` |
| 4 | 9.21034 | 5.6225e+06 | 66279.4 | 66279.4 | 7196.19 | `True` |
| 5 | 11.5129 | 2.68102e+07 | 202269 | 202269 | 17568.8 | `True` |
| 6 | 13.8155 | 9.60657e+07 | 503309 | 503309 | 36430.7 | `True` |
| 7 | 16.1181 | 2.82616e+08 | 1.08785e+06 | 1.08785e+06 | 67492.4 | `True` |
| 8 | 18.4207 | 7.1968e+08 | 2.12094e+06 | 2.12094e+06 | 115139 | `True` |
| 9 | 20.7233 | 1.64137e+09 | 3.822e+06 | 3.822e+06 | 184431 | `True` |

## 5. 结论

本步排除一个误区：终端硬点不是普通 squarefree 产品数量不足。厚区间中，Mertens/Buchstab 层的体量足够支付所需对数损失。剩余硬点已经更窄：

```text
CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn:
  prove the exact canonical layer admits the thick Buchstab products with nonzero coefficients,
  and prove every non-thick/non-admitted block exits to edge/PDEC/SAE.
```

因此这还不是行命题最终闭合；它把 SquarefreeBuchstabLayerSupportLowerBound 压缩为 exact 层承认与薄块回流的结构刚性问题。
