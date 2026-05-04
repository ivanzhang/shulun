# AlphaTail 端点 PDEC 的责任频率路由

**状态：** `endpoint_frequency_route_to_one_sided_or_mixed_open`

本文把端点 PDEC 的 Fourier 责任频率进一步拆成三类出口：

```text
missing mirror         -> MirrorImbalanceDefect/PDEC-or-SAE；
axis endpoint frequency -> OneSidedEndpointCRTDefect/ColumnCRT；
mixed endpoint frequency -> TwoEndpointCRTDefect/TailRankinPDEC。
```

这一步的作用是把“同频率 `U_CRT` 上界”拆成更窄的子问题；它仍不是终局排斥。

## 1. 频率分类

端点相位群为

\[
G_Q=(\mathbb Z/Q\mathbb Z)^2.
\]

非零频率记为

\[
h=(h_-,h_+)\in G_Q,\qquad h\ne(0,0),
\]

其中 `h_-` 作用于左端点 `D^-`，`h_+` 作用于右端点 `D^+`。

定义分类：

```text
h_- =0, h_+ !=0  -> RightEndpointAxis；
h_- !=0, h_+ =0 -> LeftEndpointAxis；
h_- =h_+ !=0    -> DiagonalEndpoint；
otherwise        -> TwoEndpointMixed。
```

## 2. 路由引理

**引理 EFR-1（责任频率出口）。**  
对持久端点键 `K`，若镜像闭合失败，则进入
`MirrorImbalanceDefect/PDEC-or-SAE`。若镜像闭合成立，则：

1. `LeftEndpointAxis/RightEndpointAxis` 频率只检测一侧端点的相位偏置，因此进入
   `OneSidedEndpointCRTDefect/ColumnCRT`；
2. `DiagonalEndpoint` 频率进入 `DiagonalEndpointCRTDefect/PDEC`；
3. `TwoEndpointMixed` 频率同时依赖两端点，进入 `TwoEndpointCRTDefect/TailRankinPDEC`。

**证明。**  
镜像闭合失败时，镜像约束不可准入，已由 `EMC-1` 强制路由。镜像闭合成立时，Fourier
项为

\[
e^{2\pi i(h_-D^-+h_+D^+)/Q}.
\]

若恰有一个坐标频率为零，该项只依赖单侧端点；它不能使用双端抵消解释，只能是单侧端点相位
过密，等价于列方向或单端 CRT 缺陷。若两坐标均非零，则该项检测左右端点的联合相位；若
两坐标相等，是对角联合相位，否则是一般双端混合相位。各类出口互斥且覆盖所有非零频率。□

## 3. 样本审计

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_frequency_route_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_frequency_route_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 \
  --phase-modulus 210 --format table
```

样本汇总：

```text
MirrorImbalanceDefect/PDEC_OR_SAE:
  count=5, total_excess=34.73002471518746；

OneSidedEndpointCRTDefect/ColumnCRT:
  count=8, total_excess=120.8777794864998；

TwoEndpointCRTDefect/TailRankinPDEC:
  count=1, total_excess=14.039653381371693。
```

关键压缩：

```text
14 个持久键中，真正双端混合硬核只剩 1 个：
g144:j4-0:u1:B, best_freq=(5,50)。
```

## 4. 对主硬点的影响

当前端点分支已经不是单一大硬点，而是三条窄接口：

1. **MirrorImbalance。**  
   证明缺镜像端点相位不能持久，或提交 SAE 可求和账本。
2. **OneSided/ColumnCRT。**  
   对轴向频率证明列残基容量上界，或进入列 CRT 缺陷排斥。
3. **TwoEndpointMixed。**  
   对唯一混合键使用尾锚不可复用、Rankin 失败回流或双端相位互斥。

因此下一步优先级是 `OneSidedEndpointCRTDefect/ColumnCRT`，因为它承担样本最大质量。

## 5. 审稿边界

已完成：

```text
非零频率分类；
镜像闭合后按轴向/对角/混合无损路由；
样本责任质量分配。
```

未完成：

```text
OneSided/ColumnCRT 的严格上界；
MirrorImbalance 的持久排斥；
TwoEndpointMixed 的尾锚/Rankin 上界。
```
