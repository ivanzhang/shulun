# H5：RRD / OSPC / Selberg-uniform 证明义务矩阵

本文档推进外审前 H5 义务：把 `RRD/OSPC/SelbergUniform/round` 从一个总常数口径压成六个可逐项验收的不等式。它不是 H5 的完成证明；它是 H5 的接受合同和下一步硬攻顺序。

## 0. 当前判定

H5 尚未闭合，但已经从“笼统常数账本”压缩为六个命名证明义务：

```text
H5.1 RRD-low dichotomy
H5.2 RRD-perp orthogonal estimate
H5.3 RRD-conversion rounding
H5.4 OSPC* => CRTDefect/Tail-anchor
H5.5 SelbergUniform
H5.6 LedgerRounding
```

若六项全部成立，则 H5 常数账本闭合。

## 1. 全局余量

来源：`docs/monograph/rse-rrd-ospc-margin-ledger.md`。

| 项 | 数值 |
|---|---:|
| `target` | `0.350000000000000000` |
| `comp_bound` | `0.29663049024172705` |
| `available_margin` | `0.053369509758272926` |
| 已分配预算 | `0.051000000000000000` |
| 保留余量 | `0.002369509758272926` |

闭合判据为

\[
C_{\rm RRD}+C_{\rm OSPC}+C_{\rm SelbergUniform}+C_{\rm round}
<0.053369509758272926.
\]

## 2. 六项验收矩阵

| 编号 | 目标 | 预算 | 当前状态 | 必须证明 |
|---|---|---:|---|---|
| H5.1 | `RRD-low` | `0.006` | 出口路由已闭合 | `docs/monograph/h5-1-rrd-low-exit-theorem.md` 证明：若 `|E_low|>0.006`，必触发 `OSPC*` 或 `weighted CRTDefect`; 出口排斥转入 H4/PDEC-or-SAE |
| H5.2 | `RRD-perp` | `0.012` | 未闭合 | 低模正交后，Buchstab/CRT 均衡/短窗不可复用给同权测试范数上界 |
| H5.3 | `RRD-conversion` | `0.002` | 待外向舍入 | 振幅线性化二阶项、dyadic 端点、Gram 投影损失均小于预算 |
| H5.4 | `OSPC` | `0.020` | 归一化已修正 | `E_dir>=1+delta_dir` 定量推出 `CRTDefect/Tail-anchor`，Fourier 到出口损失小于预算 |
| H5.5 | `SelbergUniform` | `0.008` | 样本证书已有 | 样本 Selberg 有理矩阵审计升级到 `P>=P0` 的统一谱隙/扰动界 |
| H5.6 | `LedgerRounding` | `0.003` | 部分已有 | H/Q、Selberg 变差、RSE 核、RRD/OSPC 之间所有换算误差外向舍入 |

## 3. H5 接受定理

**Theorem H5-Acceptance.** 假设 H5.1--H5.6 六项全部成立，则

\[
C_{\rm RRD}+C_{\rm OSPC}+C_{\rm SelbergUniform}+C_{\rm round}
\le 0.051
<0.053369509758272926.
\]

因此 RSE 主链中的 `RRD/OSPC/Selberg-uniform` 常数接口闭合。

**证明。** 由 H5.1--H5.3 得

\[
C_{\rm RRD}
\le 0.006+0.012+0.002=0.020.
\]

由 H5.4、H5.5、H5.6 分别得

\[
C_{\rm OSPC}\le0.020,\quad
C_{\rm SelbergUniform}\le0.008,\quad
C_{\rm round}\le0.003.
\]

相加得到总损失不超过 `0.051`。它小于可用余量 `0.053369509758272926`，并保留 `0.002369509758272926` 的安全余量。证毕。

## 4. 当前最小硬点

H5.1 的出口路由已经闭合，形式为：

```text
|E_low| > 0.006
=> OSPC* or weighted CRTDefect.
```

该命题由 `docs/monograph/h5-1-rrd-low-exit-theorem.md` 的 Cauchy--Schwarz 块分解证明。核心估计为

\[
|\mathcal E_{\rm low}|
\le
\sqrt{1+\delta_{\rm dir}}\sum_B \kappa_B m_B.
\]

取 `delta_dir=1/4` 时，若无 `OSPC*` 且

\[
\sum_B\kappa_Bm_B
\le 0.005366563145999495,
\]

则 `RRD-low<=0.006`。

剩余不再是 H5.1 的路由问题，而是下游出口排斥：

1. `OSPC*` 如何定量进入 `CRTDefect/Tail-anchor` 并被 H4 排斥；
2. `weighted CRTDefect` 如何进入 `PDEC-or-SAE` 或 Tail-anchor 并被 H4 排斥。

## 5. H5.2 的正交项目标

令

\[
a(m)=1_{P^-(m)>Y}-\rho_M,
\qquad
a_{\rm perp}=(1-\Pi_{\le Z})a.
\]

H5.2 需要证明对全部临界 RSE 测试函数 `W`：

\[
|\langle a_{\rm perp},W\rangle|
\le 0.012\,K V_\omega.
\]

可用结构：

1. `a_perp` 已剔除小模周期和 Buchstab 低层；
2. CRT 非零类均衡给低阶周期均衡；
3. 大因子短窗不可复用限制局部重复；
4. 同权归一化恒等式把测试范数降到 `V_omega=sum |omega_l|/l`。

不能使用的捷径：

```text
普通粗数密度替换
```

旧扫描显示它在 `M=P^1.2` 压力层最坏约 `0.200002`，远超 `0.012`。

## 6. H5.5 的统一 Selberg 目标

H5.5 不是重跑样本扫描，而是证明样本有理矩阵到无限范围的稳定：

```text
sample rational Selberg audit
=> P>=P0 uniform Selberg moment bound
```

审稿版需要给出：

1. 矩阵条目关于 `1/log P`、`1/P` 或 dyadic 参数的显式 Lipschitz 界；
2. 网格到全区间的外向扰动半径；
3. 最小谱隙大于扰动半径加 `0.008` 预算要求；
4. 若某区间不满足谱隙，则转入有限证书或局部参数重分块。

## 7. 下一步攻坚顺序

1. **先攻 H5.4/H4 出口排斥**：排除 `OSPC*` 与 `weighted CRTDefect` 的下游出口。
2. **再攻 H5.2**：证明低模正交粗数误差的同权测试范数上界。
3. **并行做 H5.6**：把所有外向舍入换算写成一张有限表。
4. **最后做 H5.5**：用统一扰动/谱隙完成 `P>=P0` 的 Selberg 常数。

完成 H5 后，Prime Matrix 主链仍需 H4/H2；H5 只解决 RSE 常数接口，不单独闭合行列命题。
