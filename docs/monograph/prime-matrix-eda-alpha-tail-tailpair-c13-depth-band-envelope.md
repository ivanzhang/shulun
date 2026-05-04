# AlphaTail `C13` 深度槽的端点带宽 envelope

**状态：** `c13_depth_band_envelope_sample_closed_global_open`

本文接续变模深度槽预算。上一层把 moving atoms 压成深度槽；本文进一步把深度槽放进只依赖
端点带宽、残差和步长的确定性 envelope。这是全局 SAE 可求和的前置接口。

## 1. 带宽 envelope

设端点带宽为

\[
s\le \beta |I|,
\qquad \beta=0.1.
\tag{DBE-1}
\]

由深度阶梯

\[
s=\varepsilon+u h
\tag{DBE-2}
\]

可得在固定 `(p,B,r,K,epsilon)` 下，允许的深度槽数至多为

\[
H_{\beta}+1,\qquad
H_{\beta}
=
\left\lfloor{\beta |I|-\varepsilon\over u}\right\rfloor,
\tag{DBE-3}
\]

若 `beta|I|<epsilon`，则该 envelope 为空。

## 2. envelope 引理

**引理 DBE-1（端点带宽槽上界）。**  
所有满足 `(DBE-1)` 的 formal moving atoms，在固定 `(p,B,r,K,epsilon)` 下只能落入
`0<=h<=H_beta` 的深度槽。因此槽数至多为 `(DBE-3)`。

**证明。**  
由 `(DBE-1)` 与 `(DBE-2)` 得 `epsilon+u h<=beta|I|`。移项除以正整数 `u` 后取整即得。□

若某见证不满足 `(DBE-1)`，它不进入本文的 SAE envelope，而进入独立的
`BulkDepthOverflow` 分支：

```text
depth > beta|I| => BulkDepthOverflow / cross-modulus stitching。
```

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_depth_band_envelope.py
```

默认 `C=1.3`：

```text
raw 0 formal 0 fixed 0 moving 0 band 0 overflow 0
```

压力测试 `C=1.2`：

```text
raw 281 formal 224 fixed 0 moving 224
band 224 overflow 0 groups 38
observed_slots 215 envelope_slots 24029
max_obs_over_env 0.037594
```

解释：

```text
压力样本中所有 formal moving atoms 均落入 0.1|I| 端点带；
没有 BulkDepthOverflow；
实际深度槽只占确定性 envelope 的小部分。
```

## 4. 对主链的影响

变模 SAE 出口现在细化为：

```text
MovingModulusDepth-SAE
=> BandEnvelope(beta)
   or BulkDepthOverflow.
```

`BandEnvelope` 给出确定槽数上界，但它本身仍偏宽；要闭合全局，还需继续证明：

```text
实际 witness slots 在 envelope 内满足稀疏/可求和上界；
或若在同一 envelope 中持续高密度出现，则触发 cross-modulus stitching/ColumnCRT。
```

下一层稀疏验收见 `prime-matrix-eda-alpha-tail-tailpair-c13-band-sparse-acceptance.md`：
对每个 envelope group 定义 `rho=observed_slots/envelope_slots`，若 `rho<=1/25` 则进入
`SparseSAE`，否则命名为 `HighDensityEnvelope`。

## 5. 审稿边界

已完成：

```text
端点带宽 envelope 的逐行推导；
BulkDepthOverflow 出口命名；
SparseSAE/HighDensityEnvelope 二分接口已物化；
样本 C=1.3 无 moving 原子；
C=1.2 压力样本 overflow=0，observed/envelope 最大约 0.037594。
```

仍未完成：

```text
全局证明 C=1.3 下 moving=0；
全局 BandEnvelope 内 witness slots 的可求和稀疏上界；
BulkDepthOverflow 或高密度 envelope 的 stitching/ColumnCRT 排斥。
```

所以本文只完成 SAE 可求和的 envelope 前置，不是行命题最终闭合。
