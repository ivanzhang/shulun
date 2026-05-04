# AlphaTail `C13` 低 q 高密度分支的有限阈值定理

**状态：** `c13_lowq_finite_threshold_input_ready`

本文接续固定 gap 密度天花板与低 q 共享锚证书。目标是把低 q 高密度剩余从无限问题压成
显式有限验证问题。

## 1. 阈值定理

设尾素满足统一下界

\[
q\ge \alpha P.
\tag{LFT-1}
\]

固定 gap 上界给出

\[
{N_g(J)\over |J|}
\le
{C_{\rm FG}\mathfrak S_g\over \log^2 Q}.
\tag{LFT-2}
\]

若 envelope group 至多由 `L=|M|` 个 `m` 层投影，则只要

\[
{C_{\rm FG}\mathfrak S_g\over \log^2(\alpha P)}
\le
{\eta\over L},
\tag{LFT-3}
\]

每个层都低于 `eta/L`，故由层投影鸽巢不能形成 `eta`-高密度 envelope。等价地，

\[
P\ge P_0(g)
:=
{1\over \alpha}
\exp\sqrt{ {C_{\rm FG}\mathfrak S_g L\over \eta} }.
\tag{LFT-4}
\]

**定理 LFT-1（低 q 分支有限化）。**  
对任意固定参数族，若

\[
P\ge \max_g P_0(g),
\tag{LFT-5}
\]

则 `HighDensityEnvelope` 不能从低 q 层产生。若 `P<max_g P_0(g)`，该分支只剩有限个
`P` 与有限个 endpoint-band group，需要提交精确 `SparseSAE` 或 `ColumnCRT/stitching`
证书。

**证明。**  
由 `(LFT-1)`，每个尾素端点层的左端 `Q` 至少为 `alpha P`。将此代入 `(LFT-2)` 得到
`(LFT-3)`。若某个 envelope group 的总密度大于 `eta`，按层投影鸽巢，至少一个 `m` 层密度
大于 `eta/L`，与 `(LFT-3)` 矛盾。故 `P>=max_g P_0(g)` 时高密度出口为空。反之
`P<max_g P_0(g)` 给出有限范围，需由显式证书处理。□

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_lowq_finite_threshold.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowq_finite_threshold.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --witness-c 1.2 --ceiling-c 1.3 \
  --eta 0.04 --slack-cut 40 --format table
```

输出摘要：

```text
groups=38；
accepted=38；
high=0；
max_density=0.037594；
min_eta_slack=0.320000；
max_qcrit_group=522098.62；
max_pcrit_group=580109.58；
routes=FiniteExactSparse:38。
```

其中最坏阈值来自奇异因子较大的 `g=900` 层；对 `g=12,24,36` 这类低端点层，
`P_0≈99420.62`。因此当前样本族中所有尚未由鸽巢密度天花板自动排斥的 group，均由精确
`SparseSAE` 计数通过。

## 3. 对主链的影响

`LowQ-Layer-HDE` 现在变为：

```text
P >= P0(C_FG,eta,alpha,S_g,L)
  => density ceiling + layer pigeonhole 排斥；

P < P0
  => finite exact SparseSAE / ColumnCRT certificate。
```

这一步把低 q 高密度分支从“无限低端异常”压成一个显式阈值问题。后续若要闭合全局行命题，
必须补齐：

```text
1. 目标参数族中所有允许 gap 的奇异因子上界；
2. P<P0 范围内所有目标窗口的有限证书；
3. 或者更强的目标族固定 gap 常数，降低 P0。
```

## 4. 审稿边界

已完成：

```text
低 q 分支的显式阈值公式；
样本族中 38 个 band group 的精确 SparseSAE 通过；
当前参数下 max_pcrit_group=580109.58 的审计输出。
```

仍未完成：

```text
全局目标族的 gap 奇异因子统一上界；
P<P0 的完整有限验证清单；
把有限证书接入主稿终局 theorem 环境。
```

因此本文闭合的是 `LowQ-Layer-HDE` 的有限化接口，不是行命题最终无条件证明。
