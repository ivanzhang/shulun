# FO-PDEC 二点原子的 SAE/Endpoint 吸收

**状态：** `audited_two_physical_primitive_atoms_absorbed_by_local_survivor_witnesses`

本文承接：

```text
docs/monograph/prime-matrix-wsh-fo-pdec-physical-primitive-tautology.md
docs/monograph/prime-matrix-wsh-fo-pdec-sae-endpoint-absorption-audit.md
```

上一层已经说明：physical/primitive 口径下的 `1.9997507790353146` 不是可攻 PDEC 阈值，
而是二点 Fourier 恒等式。因此剩余两个物理原子必须转入 `SAE/Endpoint` 或更强局部证书。

## 1. 吸收判据

设一个 primitive 原子 `n=b+d` 位于固定偏移纤维

\[
F_d(B)=\{b'+d:b'\in B\}.
\]

若同一纤维里存在素数候选 `n0`，则该纤维不能作为全覆盖零窗。这个 `n0` 就是
`LocalSurvivorCert` 的本地 witness。若同时解释因子在该纤维内负载为 `1`，则它也不是局部
Tail-anchor 重复型缺陷。

因此二点 primitive 原子的合法吸收路线是：

```text
two-point PDEC tautology
=> sparse SAE/Endpoint packet
=> LocalSurvivor witness in the same fixed-offset fiber
   or persistent blocker signature returning to PDEC.
```

## 2. 当前两个物理原子

审计给出四条来源行，全部有同纤维素数见证：

```text
250541, q=773,row=325,offset=24  -> witness 250543；
250541, q=967,row=260,offset=24  -> witness 250543；
1664237,q=1993,row=836,offset=30 -> witness 1664227；
1664237,q=1993,row=836,offset=30 -> witness 1664227。
```

并且这些纤维中 `factor=199` 的负载均为 `1`。所以当前二点 primitive 分支既不能作为
非退化 PDEC 下界，也不能作为未闭合 SAE/Endpoint 障碍继续保留。

## 3. 结论边界

**引理 SAE-2Atom（当前审计样本）。**  
在当前 FO-PDEC 有限账本中，physical/primitive 二点残留全部由同固定偏移纤维中的本地素数
见证吸收。

**证明。**  
二点 Fourier 阈值由 `PPT-1` 退化；把两个物理原子送入 SAE/Endpoint 后，逐来源检查同一
`(block,q,row,offset)` 纤维。每条来源行均有素数候选，且 `factor=199` 在纤维内负载为 `1`。
故不存在由这两个原子支撑的全覆盖局部零窗。证毕。

这只关闭当前已审计的二点 primitive 子门。完整 Prime Matrix 行/列无条件定理仍需要：

```text
global LocalSurvivorCert family；
future non-tautological primitive PDEC families；
CleanKLS/DLS；
D-structure/Tail-log4/Rankin referee inputs。
```
