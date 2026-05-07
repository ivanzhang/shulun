# Triad-A1 ForcedCap ColumnTail 暴露合同

**状态：** `forcedcap_columntail_exposure_contract_materialized_terminal_open`

本文补齐 ForcedCap 的 column-tail 输入。`ForcedPersistentByDensityBarrier` 已经说明固定 `Q` 层普通
cap 不能闭合；但它仍必须解释 cap 内低洞如何被高素数支付。先登记轻量暴露账本：

```text
对每个低洞列 c 和每个高素数 ell，
计算覆盖该洞所需的唯一 residue y mod ell；
exposure(ell,residue,column) += M(phase)。
```

它不是完整完成态支付选择枚举；它给出 forced cap 后续 PDEC/ColumnTail 证书必须面对的候选签名。

## 1. 暴露方程

对 forced cap `C`，定义：

```text
D_C = sum_{phase in C} M(phase) * |H_low(phase)|。
```

每个低洞列对每个高素数 `ell` 诱导唯一 residue：

```text
((phase+yQ-1)P+c)=0 mod ell。
```

于是可登记：

```text
prime exposure；
tail-residue exposure；
column-residue exposure。
```

若某个暴露 bucket 沿正式反例族持久承担实际支付，则它就是可提交的 PDEC/ColumnCRT/TailAnchor 方向。
若实际支付无法固定在任何暴露 bucket 上，则支付跨多壳分散，进入 CleanKLS/DLS。

## 2. 当前机器审计

对应文件：

```text
experiments/prime_matrix_triad_a1_forcedcap_columntail_payment_audit.py
docs/monograph/prime-matrix-triad-a1-forcedcap-columntail-payment.md/json
```

当前审计覆盖 `P=43,47` 的 `24` 个 forced cap。它核验：

```text
old intersection size/mass 重算一致；
每个 cap 输出 top prime/residue/column-residue 暴露签名。
```

## 3. 闭合边界

本文完成：

```text
ForcedCap 的 column-tail 暴露账本物化；
forced cap 的终端义务从“持久帽”压成 fixed-signature PDEC 候选或 distributed CleanKLS。
```

本文未完成：

```text
证明 top 暴露签名实际承担支付并持久时的 U_CRT<L_PDEC；
证明实际支付不持久时的 CleanKLS/DLS 大筛界；
forced cap 后继 lift 的删除势发散。
```

所以它仍是终端输入合同，不是 forced 分支的最终排斥。
