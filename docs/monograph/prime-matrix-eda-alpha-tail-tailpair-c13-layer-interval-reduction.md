# AlphaTail `C13` 高密度层的一维固定 gap 区间归约

**状态：** `c13_layer_interval_reduction_input_ready`

本文接续 `HighDensityEnvelope` 层投影证书。目标是把
`LayerHighDensityEndpointPair` 进一步化为一维 `q` 轴上的固定差值端点带区间证书。

## 1. q-区间

固定高密度层

```text
(p,B,r,m,g,j1,j2,u,side,epsilon; 0<=h<=H).
```

若 `side=left`，则

\[
q=q_-+h,\qquad 0\le h\le H.
\tag{LIR-1}
\]

若 `side=right`，则

\[
q=q_+-h,\qquad 0\le h\le H.
\tag{LIR-2}
\]

因此该层给出一个普通整数区间

\[
J_{\rm band}=[q_-,q_-+H]\quad\text{或}\quad[q_+-H,q_+].
\tag{LIR-3}
\]

其中每个 witness slot 正是一个固定差值尾素对

\[
q,\ q+g\in\mathcal P_{\rm tail}.
\tag{LIR-4}
\]

## 2. 归约引理

**引理 LIR-1（高密度层到一维固定 gap 区间）。**  
任意 `LayerHighDensityEndpointPair` 都给出一个一维区间 `J_band`，并满足

\[
\#\{q\in J_{\rm band}:q,q+g\in\mathcal P_{\rm tail}\}
\ge S_m(E).
\tag{LIR-5}
\]

其中 `S_m(E)` 是该高密度层的 witness slot 数。

**证明。**  
由 `(LIR-1)` 或 `(LIR-2)`，每个深度槽 `h` 与唯一 `q` 一一对应。层投影证书中的每个
observed slot 都来自一个 formal witness pair `(q,q+g)`，故 `(LIR-5)` 成立。□

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_layer_interval_reduction.py
```

压力测试 `C=1.2, eta=0.04`：

```text
high_groups 0
```

路线测试 `C=1.2, eta=0.03`：

```text
high_groups 3
max_required_C 0.787594
```

输出的三个一维区间为：

```text
g=12, J=[1390,1522], witnesses=4, required_C=0.787594；
g=24, J=[1378,1510], witnesses=4, required_C=0.785708；
g=24, J=[1366,1498], witnesses=4, required_C=0.783808。
```

这些区间直接成为固定 gap 端点带高密度证书。

## 4. 对主链的影响

`HighDensityEnvelope` 出口现在细化为：

```text
HighDensityEnvelope
=> LayerHighDensityEndpointPair
=> one-dimensional fixed-gap q-interval certificate
=> fixed-gap endpoint-band density contradiction
   or ColumnCRT/stitching.
```

因此后续排斥不再处理抽象 envelope，而只需处理形如 `(LIR-5)` 的一维固定 gap 区间。

## 5. 审稿边界

已完成：

```text
高密度层到 q-区间的一一归约；
固定 gap witness pair 计数下界；
脚本输出路线测试中的具体 q-区间和 required_C。
```

仍未完成：

```text
全局排斥一维固定 gap 端点带高密度区间；
或证明 eta=1/25 下不会出现 HighDensityEnvelope；
SparseSAE 总 envelope 量的全局可求和。
```

所以本文完成的是高密度出口的一维化，不是行命题最终闭合。
