# LocalSurvivor packet-generation 合同

**状态：** `local_survivor_packet_generation_reduced_to_extractor_completeness_or_pdec`

本文承接：

```text
docs/monograph/prime-matrix-local-survivor-materialized-packet-ledger.md
docs/monograph/prime-matrix-sae-local-certificate-reduction.md
docs/monograph/prime-matrix-terminal-certificate-triad.md
```

当前已物化的 `LocalSurvivor/SAE` 包已经全部闭合。剩余不再是这些具体窗口，而是一个生成问题：
若未来出现新的 sparse/single-window escape，必须能把它抽取成同类有限包；否则它不能保持
`LocalSurvivor` 身份，必须回流为持久 `PDEC/ColumnCRT/CleanKLS` 输入。

## 1. 生成对象

一个 `LocalSurvivor` 包必须包含：

```text
I                      : 局部窗口或固定偏移纤维；
C(I)                   : 候选点集合；
B_low,B_tail,B_col,... : blocker 家族；
projection             : blocker -> C(I) 的命中规则；
witness or deficit     : 未覆盖候选，或 |union blockers|<|C(I)|。
```

若这些数据不能抽取，就不能称为 `LocalSurvivorCert`。它只是一个未命名逃逸，而无第四出口定理
已经禁止未命名逃逸停留。

## 2. 有限签名

对每个候选孤窗定义签名

```text
sigma(I)=(
  entry_route,
  modulus_layer,
  phase_key,
  window_shape,
  blocker_type_set,
  column_signature_set,
  endpoint_signature,
  tail_or_cofactor_signature,
  formal_unit_id
).
```

在固定分支、固定层和固定窗口形状下，`sigma(I)` 的取值有限。于是任何无限反例族中的
未闭合孤窗只有两种可能：

1. 某个签名无限复现；
2. 签名层级不断提升，窗口进入 clean/high-dimensional dispersion 分支。

第一种不是 `LocalSurvivor` 终端，而是持久签名缺陷：

```text
low blocker repeats       => low-mod PDEC；
column signature repeats  => ColumnCRT / displacement PDEC；
endpoint signature repeats=> endpoint PDEC；
tail/cofactor repeats     => TailAnchor / Cofactor PDEC；
formal unit repeats       => primitive or weighted PDEC。
```

第二种进入 `CleanKLS/DLS` admission，而不是第四出口。

## 3. Packet-generation 引理

**引理 LSPG-1（孤窗生成二分）。**  
在终端三证书接口内，任意 sparse/single-window escape 若不能立即给出 `LocalSurvivorCert(I)`，
则它必满足以下之一：

```text
finite packet extractable but witness/deficit 未填；
same signature persists along an infinite counterexample family；
signature layer escapes to CleanKLS/DLS admission；
descent/seam route lowers to an already named PDEC/LocalSurvivor/ColumnCRT packet。
```

**证明。**  
若窗口数据 `I,C(I),B_j,projection` 可抽取，则它就是有限 packet；剩余只是在有限集合上核验
witness 或覆盖不足。若数据不可抽取，失败必来自某类 blocker、端点、列位移、尾锚或 formal unit
没有被固定。沿无限反例族取最小未闭合窗口；若某个签名无限复现，由有限鸽巢得到持久缺陷，按
签名类型回流到 `PDEC/ColumnCRT/TailAnchor/CofactorAnchor`。若没有签名复现，则局部结构在层级上
持续扩散，正是 `CleanKLS/DLS` 的 admission 形态。若窗口来自相邻层缝合或下降，则由既有
`TotalDescent/RPZ` 合同回到命名包。故没有新的终端。证毕。

## 4. 当前总账后果

当前机器总账已经验证：

```text
materialized packets: 9；
materialized phase atoms: 32；
local survivor witnesses: 5；
open materialized obligations: 0。
```

因此当前最窄剩余可以再写成：

```text
PacketExtractorCompleteness:
  prove every future sparse escape emits a finite packet;

or NonTautologicalPDEC:
  same formal unit has >=3 physical atoms
  or an extra fixed-frequency constraint prevents two-point tautology;

or CleanKLS/DLS:
  signature layer escapes all finite packets.
```

## 5. 边界

本文不是最终行列无条件证明。它关闭的是“已物化包之外还有无名 LocalSurvivor 终端”的可能性。
全局仍需提交：

```text
PacketExtractorCompleteness；
NonTautologicalPDEC exclusion；
CleanKLS/DLS or explicit ExternalKLS；
D-structure/Tail-log4/Rankin referee inputs。
```
