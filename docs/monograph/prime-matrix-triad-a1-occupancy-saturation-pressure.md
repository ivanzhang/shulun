# Triad-A1 OccupancySaturation 压力引理

**状态：** `occupancy_saturation_pressure_reduced_to_capacity_or_kl`

本文继续攻击 `HoleResidueOccupancy` 后剩下的 `HRO-A`：

```text
若删除势不发散，且 TailIndependentCompletion 不接管，
则旧洞集在新增素数 r 上必须近满占用。
```

目标不是给出新统计常数，而是把这种“近满占用”本身变成容量压力或相位缺陷。

## 1. 从无删除到近满占用

固定一层 `Q'=rQ`。对旧活跃相位 `t`，沿用：

```text
S_t   = lift 后幸存的 fiber residue；
Occ_t = promoted prime r 命中旧洞的 residue；
TI_t  = promoted prime 未命中旧洞但 Tail 独立完成的 residue。
```

由 `HoleResidueOccupancy`：

```text
|S_t|/r <= |Occ_t|/r + |TI_t|/r。
```

对某个活跃相位集合 `A` 取平均。若：

```text
avg_A |S_t|/r >= 1-delta，
avg_A |TI_t|/r <= epsilon，
```

则必有：

```text
avg_A |Occ_t|/r >= 1-delta-epsilon。
```

再由 `0<=|Occ_t|/r<=1`，对任意 `eta>0`：

```text
#{t in A: |Occ_t|/r < 1-eta}/|A|
<= (delta+epsilon)/eta。
```

所以若删除几乎停止且 `TI` 没有接管，则多数旧活跃相位必须满足：

```text
|Occ_t| >= (1-eta)r。
```

这就是 `OccupancySaturation` 的严格来源。

## 2. 近满占用的含义

因为：

```text
|Occ_t| <= |{c mod r: c in H_Q(t)}| <= min(|H_Q(t)|, r)，
```

`|Occ_t| >= (1-eta)r` 立即推出：

```text
|H_Q(t)| >= (1-eta)r，
```

并且旧洞列必须命中几乎所有 `c mod r` 的 residue。

这不是普通“大洞数”事件，而是双重刚性：

```text
数量刚性：旧低层骨架留下至少约 r 个洞；
分布刚性：这些洞不能集中在少数 r-residue 中。
```

若数量刚性失败，则删除势继续增长。若数量刚性成立，但 Tail 不能覆盖这些大量分散旧洞，则容量矛盾。若 Tail 长期能覆盖，则 Tail 的 CRT 选择必须对这些分散洞产生强条件同步，进入 KL/PDEC/CleanKLS。

## 3. 容量压力形式

对每个幸存 residue `b`，Tail 必须完成残余旧洞：

```text
H_Q(t) \ R_b(H)。
```

因此任意 Tail 容量上界 `Cap_tail(t,b)` 都给出确定性门：

```text
Cap_tail(t,b) < |H_Q(t)\R_b(H)|
=> b notin S_t。
```

当 `|Occ_t|` 近满时，多数 `b` 至多删除旧洞中的一个 residue class；若旧洞在 `r` 上分散，则大量残余集仍很大。于是要维持 `|S_t|/r -> 1`，Tail 必须在大量 `b` 上几乎满负荷完成。

这产生二分：

```text
Tail capacity insufficient:
  大量 b 死亡，删除势继续支付。

Tail capacity sufficient on most b:
  Tail CRT 选择对 (t,b,H_Q(t)) 产生持久条件偏斜；
  进入 NoDeletion-KL、PDEC 或 CleanKLS。
```

## 4. 与层叠轮筛刚性的关系

用户提出的 `P^2±k mod 30,210,2310,...` 层叠轮筛刚性，在这里对应为：

```text
每加入一个新素数 r，旧洞集必须通过一个新的 residue 占用门；
若占用小，则新层删除；
若占用近满，则旧层已经留下过多且过分分散的洞；
若 Tail 仍能补，则更高层 CRT 条件分布发生同步偏斜。
```

因此无穷层叠不是寻找固定周期公式，而是一个递归压力机：

```text
低层洞不足       => promoted prime 删除；
低层洞近满       => 容量压力；
高层 Tail 强补   => KL/PDEC/CleanKLS；
条件同步不持久   => 删除势累计发散。
```

## 5. 当前证据位置

当前两层 `HoleResidueOccupancy` 审计还没有触发 `OccupancySaturation`：

```text
2310->30030: max phase occupied ratio = 0.307692；
30030->510510: max phase occupied ratio = 0.117647。
```

所以当前物化层仍处在强删除势区。本文的作用是提前封住未来可能出现的逃逸：

```text
若某后继层出现 occupied ratio -> 1，
它不再是无名反例，
而是 Capacity/KL/PDEC 的输入证书。
```

## 6. 下一步

现在 `DeletionPotential` 分支被压成终端三路：

```text
1. avg(|Occ|+|TI|)/r <= 1-eta
   => 删除熵发散；

2. avg |TI|/r -> 1
   => NoDeletion-KL / CleanKLS；

3. avg |Occ|/r -> 1
   => OccupancySaturation；
      再由本文转入 Tail capacity pressure 或 KL/PDEC。
```

剩余最小硬点是把第 3 路的 `Tail capacity pressure` 写成可复用证书：

```text
近满旧洞 residue + 大量幸存 fiber
=> Tail 条件分布高 KL
   or 低层容量矛盾。
```

## 7. TailCapacityPressure 已接入

新增 `prime-matrix-triad-a1-tail-capacity-pressure.md` 后，第 3 路已进一步物化。

对每个 residue `b`：

```text
Residual_b=H_Q(t)\R_b(H)。
```

若 Tail 简单容量或 Hall 子集容量不足，则 `b` 必死；若 `b` 幸存且 Tail 完成数为 `m_b`，则正式质量相对 Tail 均匀基准支付：

```text
KL >= log(M_tail/m_b)。
```

当前两层审计显示：

```text
所有死亡槽位均 Hall-certified；
hall_uncertified_dead_slots=0；
非平凡幸存槽位有正 KL floor。
```

因此 `OccupancySaturation` 的后续已被压成：

```text
容量亏损 => 删除势；
容量成功但完成集合小 => NoDeletion-KL/PDEC/CleanKLS。
```
