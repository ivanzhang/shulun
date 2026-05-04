# AlphaTail `C13` 带宽 envelope 的稀疏验收账本

**状态：** `c13_band_sparse_acceptance_sample_closed_global_open`

本文接续端点带宽 envelope。目标是把 envelope 内的实际 witness slots 分成两类：

```text
SparseSAE              : 实际槽密度 <= eta；
HighDensityEnvelope    : 实际槽密度 > eta，必须触发 stitching/ColumnCRT 或新的密度矛盾。
```

当前采用的审稿阈值为

\[
\eta={1\over25}=0.04.
\tag{BSA-1}
\]

## 1. 稀疏验收

对一个 envelope group `E=(p,B,r,K,epsilon)`，记

\[
S(E)=\#\{\text{observed witness depth slots in }E\},
\]

\[
\Omega(E)=\#\{\text{all envelope slots allowed by }DBE\}.
\]

定义密度

\[
\rho(E)={S(E)\over\Omega(E)}.
\tag{BSA-2}
\]

若

\[
\rho(E)\le\eta,
\tag{BSA-3}
\]

则该 group 进入 `SparseSAE`。由深度槽容量引理，每个槽最多贡献 `|M|` 个 formal atoms，
所以该 group 的 atom 贡献满足

\[
\#\mathrm{atoms}(E)\le |M|\,S(E)\le |M|\,\eta\,\Omega(E).
\tag{BSA-4}
\]

若 `(BSA-3)` 失败，则该 group 进入 `HighDensityEnvelope`，不得用稀疏 SAE 吸收。

## 2. 二分引理

**引理 BSA-1（envelope 稀疏/高密度无损二分）。**  
固定 `eta in (0,1)`。每个带宽 envelope group 唯一落入 `SparseSAE` 或
`HighDensityEnvelope`。在 `SparseSAE` 中有 `(BSA-4)`。

**证明。**  
由 `rho(E)<=eta` 与其否定二分。`SparseSAE` 中，先由深度槽容量得
`atoms(E)<=|M|S(E)`，再代入 `S(E)<=eta Omega(E)` 即得 `(BSA-4)`。□

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_band_sparse_acceptance.py
```

默认 `C=1.3`：

```text
raw 0 formal 0 fixed 0 moving 0
groups 0 accepted 0 high 0
```

压力测试 `C=1.2, eta=0.04`：

```text
raw 281 formal 224 fixed 0 moving 224 overflow 0
groups 38 accepted 38 high 0
accepted_slots 215 high_slots 0
max_density 0.037594 min_eta_slack 0.320000
```

更紧阈值 `eta=0.03` 的路线测试：

```text
groups 38 accepted 35 high 3
high_slots 14
```

这说明脚本会真实输出 `HighDensityEnvelope`，不是把失败项静默吸收。

## 4. 对主链的影响

变模 SAE 出口现在细化为：

```text
BandEnvelope
=> SparseSAE(eta=1/25)
   or HighDensityEnvelope.
```

当前压力样本显示 `eta=1/25` 足以吸收所有 observed slots；但全局闭合仍需证明目标窗口族中
所有 envelope group 均满足 `(BSA-3)`，或者证明 `HighDensityEnvelope` 触发
cross-modulus stitching/ColumnCRT。

`HighDensityEnvelope` 的下一层证书见
`prime-matrix-eda-alpha-tail-tailpair-c13-high-density-envelope-certificate.md`：若
`S(E)>eta Omega(E)`，则存在某个具体 `m` 层满足
`S_m(E)>=ceil(S(E)/|M|)`，形成端点带固定差值高密度素对块。

SparseSAE 的总量付款账本见
`prime-matrix-eda-alpha-tail-tailpair-c13-sparse-summability-ledger.md`：
对所有稀疏 group 求和后有
`sum atoms(E)<=|M|*eta*sum Omega(E)`，当前压力样本给出
`accepted_capacity=1922.32` 与 `moving=224`。

## 5. 审稿边界

已完成：

```text
稀疏/高密度 envelope 二分；
SparseSAE 的 atom 上界 |M|*eta*Omega(E)；
HighDensityEnvelope 的层投影证书接口；
样本 C=1.3 无 moving 原子；
C=1.2 压力样本在 eta=1/25 下 high=0。
```

仍未完成：

```text
全局证明所有 C=1.3 反例 envelope 均为 SparseSAE；
SparseSAE 总 envelope 量的全局可求和；
HighDensityEnvelope 的 stitching/ColumnCRT 排斥。
```

所以本文完成的是稀疏验收接口，不是行命题最终闭合。
