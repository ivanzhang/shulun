# Triad-A1 ForcedCap 暴露支配合同

**状态：** `forcedcap_exposure_dominates_actual_payment_terminal_open`

本文把 ForcedCap 的 `column-tail 暴露账本` 推进一步：暴露不是实际支付，但它给实际支付提供逐桶上界。
因此可以无条件推出动态多桶下界。

## 1. 支配律

对任意 bucket `B`，实际支付满足：

```text
ActualPayment(B) <= Exposure(B)。
```

原因是 `Exposure(B)` 数的是所有低洞需求中“可以由 bucket B 支付”的总质量；实际支付只能从这些可支付事件中选择。

若 cap 总需求为 `D_C`，最大 bucket 暴露为 `E_max`，则任何实际支付方案都需要至少：

```text
ceil(D_C / E_max)
```

个 bucket。这是每个 cap 自归一化的动态下界，不使用固定常数。

## 2. 当前机器路由

对应审计：

```text
experiments/prime_matrix_triad_a1_forcedcap_exposure_dominance_router.py
docs/monograph/prime-matrix-triad-a1-forcedcap-exposure-dominance-router.md/json
```

当前结果：

```text
forced_cap_count=24；
all_single_residue_actual_payment_excluded=True；
all_single_column_residue_actual_payment_excluded=True；
global_min_actual_residue_buckets_by_exposure=11；
global_min_actual_column_residue_buckets_by_exposure=9。
```

所以当前 forced cap 不可能由一个固定 residue 或一个固定 column-residue 支付完成。

## 3. 终端二分

实际支付只剩两种归宿：

```text
MultiBucketPersistent:
  某一组多 bucket 签名沿正式反例族持久承担需求；
  => multi-bucket TailAnchor / ColumnCRT / refined PDEC。

DistributedPayment:
  没有持久 bucket 集合；
  => 多壳分散 CleanKLS/DLS。
```

若后续 lift 改变支撑，则回到 `next-lift deletion/KL`。

## 4. 闭合边界

本文完成：

```text
单 bucket forced-tail 支付排除；
实际支付必须多桶化；
forced cap 终端义务压成 multi-bucket PDEC 或 CleanKLS。
```

本文未完成：

```text
multi-bucket PDEC 的 U_CRT<L_PDEC；
DistributedPayment 的 CleanKLS/DLS 大筛证书；
后继 lift 删除势发散。
```

因此它是最后终端入口的继续压缩，不是全局证明终点。
