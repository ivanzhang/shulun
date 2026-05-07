# Triad-A1 多桶 Formal Unit 投影二分

**状态：** `triad_a1_multibucket_formal_unit_dichotomy_open`

本文接在 `多桶投影坍缩路由器` 之后。裸多桶 LP 已被证明会投影回普通相位质量上界；因此真正有信息量的对象不是
“桶很多”，而是“同一个多桶支付签名在升层塔中投影兼容并持久承担质量”。

## 1. 多桶支付塔

令轮层为：

```text
Q_0 | Q_1 | Q_2 | ...，
```

每层有 bucket 空间 `B_n` 与坏窗支付测度：

```text
mu_n(b)=A_n(b)/D_n。
```

升层给出投影：

```text
pi_n: B_{n+1} -> B_n。
```

一个多桶 formal unit 不是某一层的任意桶组，而是一族有限桶组：

```text
S_n subset B_n
```

满足投影兼容：

```text
pi_n(S_{n+1}) subset S_n
```

并且长期承担正质量：

```text
limsup_n mu_n(S_n) >= eta > 0。
```

这才有资格进入 multi-bucket PDEC。

## 2. 逆极限二分

沿任意正式最小反例子列，只有两种可能。

### 2.1 Persistent Formal Unit

存在 `eta>0` 与投影兼容桶组 `S_n`，使：

```text
mu_n(S_n) >= eta
```

在无限多层成立。由有限签名鸽巢和投影紧性，可以截取一个有限层 `N`，得到同一 formal unit：

```text
S_N；
tau'_N=(phase, bucket-signature, tail/column/cofactor labels)；
Gamma_{S_N}。
```

这时必须提交：

```text
U_CRT^multi(S_N) < L_PDEC^multi(S_N)
```

或输出：

```text
CorrelatedBucketBlock；
ColumnTailMissingRow；
refined/profinite PDEC。
```

### 2.2 Distributed Payment

不存在任何正质量投影兼容桶组。则对任意固定有限层签名 `S_N`：

```text
mu_n(pi_{N,n}^{-1}(S_N)) -> 0
```

沿后继层成立。于是支付质量只能逃向越来越多的新桶、新 residue、新 column-tail 签名。

这正是 CleanKLS/DLS 的准入条件：

```text
no persistent top-prime；
no persistent residue；
no persistent column displacement；
no persistent finite bucket block；
energy spread across growing shells。
```

若大筛对偶失败，它会反过来输出一个持久有限签名，回到 `Persistent Formal Unit`。

## 3. 与裸投影坍缩的关系

裸多桶 LP 只使用：

```text
0<=g_b(t)<=E_b(t)；
sum_b g_b(t)<=M(t)。
```

它无法区分：

```text
同一 formal unit 长期承担质量；
每层由不同桶临时承担质量。
```

所以裸 LP 的坍缩不是坏消息，而是精确指出必须补的结构行：

```text
formal-unit compatibility row；
tail/column/cofactor signature row；
actual payment graph row；
or CleanKLS distributed admission。
```

## 4. 递归闭合方程

ForcedCap 多桶分支现在可写成：

```text
MultiBucketPayment_n
=> PersistentFormalUnit_n
   or DistributedPayment_n。
```

若 `PersistentFormalUnit_n`：

```text
=> multi-bucket PDEC
   or refined ColumnTail/Cofactor row
   or smaller correlated bucket block。
```

若 `DistributedPayment_n`：

```text
=> CleanKLS/DLS；
若 CleanKLS 对偶失败，则输出新的持久 finite signature，回到 PDEC。
```

因此没有第四出口。

## 5. 当前可执行下一步

对已物化的 `48` 个 forced 多桶骨架，下一步机器审计应输出：

```text
同层公共 bucket / bucket-block 候选；
跨 cap 复现质量；
是否存在可作为 S_N 的持久有限签名；
若没有，则路由到 DistributedPaymentCandidate；
若有，则登记 MFU candidate，等待 U_CRT^multi/L_PDEC^multi 或条件行。
```

这仍不是全局证明终点；它把真正终端硬点从“多桶很多”压成“是否存在投影兼容正质量 formal unit”。
