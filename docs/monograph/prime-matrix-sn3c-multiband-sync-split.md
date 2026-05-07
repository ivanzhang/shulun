# SN3-C 多真分散带同步分裂：从同行叠加到多壳 KLS

**状态：** `sn3c_multiband_sync_split_reduction_not_closed`

本文接续 `SN3-B 真分散残余目标`。SN3-B 的最紧样本不是单带，而是同一行中多个 `TrueDistributedDLS` 带同向正偏。本文把这种“多带叠加”进一步分裂：

```text
多带叠加
=> q 壳重叠 SAE
   或低模签名同步 PDEC/ColumnCRT
   或真正多壳 KLS/dispersion 候选。
```

## 1. 互反 q 壳分离

固定行 `(P,y)` 与二进互补因子带

```text
J=[A y, B y),     A<B。
```

若 `m in J` 且远尾命中存在，则

```text
ceil((Py-P+1)/m) <= q <= floor((Py-1)/m)。
```

因此该带的 q 壳满足外向界：

```text
q_min(J) >= (Py-P+1)/(B y),
q_max(J) <  Py/(A y) = P/A。
```

对两个带

```text
J_1=[A y,B y),     J_2=[C y,D y),     C>B，
```

若

```text
C > B*y/(y-1+1/P),
```

则

```text
q_max(J_2) < q_min(J_1)。
```

特别地，对非邻二进带 `C>=2B` 且 `y>=2`，q 壳严格分离。于是这类多带叠加不可能由同一个短 q 窗解释；若仍同向超额，必须来自低模同步或高频多壳相关。

## 2. 多带同步分裂

对同一行的真分散带族 `J_1,...,J_s`，每个带都有中心化签名：

```text
V_J^{win}   = (E_{J,Q_i})_i；
V_J^{qmod}  = (E_{J,q=a mod W})_a；
V_J^{dmod}  = (E_{J,d=b mod W})_b。
```

对任意两个带，定义余弦同步度：

```text
cos(V_J,V_K)=<V_J,V_K>/(||V_J||_2 ||V_K||_2)。
```

取阈值 `kappa`。若多带同向正偏，则有三种出口：

```text
ShellOverlap:
  q 壳相交或 q-window 签名高度重叠
  => SAE / short-window refinement；

LowModSync:
  max(cos qmod, cos dmod) >= kappa
  => PDEC / ColumnCRT；

KLS-Multishell:
  q 壳分离且低模余弦 < kappa
  => 真正多壳高频 dispersion/KLS 输入。
```

这是确定性路由。真正未闭合的是第三类 `KLS-Multishell`。

## 3. 当前审计

配套脚本：

```text
experiments/prime_matrix_sn3c_multiband_sync_audit.py
```

当前报告：

```text
docs/sn3c_multiband_sync_audit_20260506.md
docs/sn3c_multiband_sync_audit_20260506.json
```

结果：

```text
multi_true_row_count = 3
pair_count = 3
pair_route_counts = {
  kls_multishell_candidate: 2,
  lowmod_multiband_sync_candidate: 1
}
max_multirow_true_excess_over_required = 0.187188
max_pair_lowmod_cosine = 0.834817
min_pair_q_shell_gap = 2525
```

最紧行：

```text
P=10007,y=75:
  true E/R = 0.187188
  bands:
    [4y,8y): q=[1237,2444], E/R=0.120145
    [1y,2y): q=[4970,9500], E/R=0.067043
  q shell gap = 2525
  q-window cosine = 0
  max lowmod cosine = 0.432620
  route = KLS-Multishell。
```

这说明当前最紧行不是短窗重叠，也不是低模同步，而是真正的多壳高频相关候选。

另一个低模同步样本：

```text
P=100003,y=131:
  route = LowModSync,
  max lowmod cosine = 0.834817 at q mod 30。
```

它应回流到 PDEC，而不是进入 KLS。

## 4. SN3-C 后的剩余硬点

经过 SN3-C，SN3-B 的多带叠加被压成：

```text
1. 低模同步回流 PDEC/ColumnCRT；
2. 真正多壳 KLS-Multishell。
```

当前最窄未闭合输入为：

```text
KLS-Multishell:
  对 q 壳分离、低模签名不同步的多个互补因子带，
  证明其中心化素数误差不能同向叠加到支付 R；
  若失败，则产生高频非零相位证书。
```

这仍不是最终证明，但已经把“同一行多带叠加”排除了短窗和低模解释，只剩高频 dispersion/Kloosterman 型输入。

## 5. SN3-D：KLS-Multishell 到列高频

新增 `prime-matrix-sn3d-kls-multishell-frequency-bridge.md` 与
`experiments/prime_matrix_sn3d_kls_multishell_frequency_audit.py` 后，`KLS-Multishell`
继续分裂为：

```text
HighFrequencyColumn/PDEC；
或 L2Flat CleanMultishellKLS。
```

审计显示当前 `2` 个 KLS-Multishell 候选均有强非零列频率：

```text
P=10007,y=75:  top h=49,  |Rhat(h)|/E=1.374721, flatness=0.014668；
P=50021,y=128: top h=119, |Rhat(h)|/E=2.056175, flatness=0.004695。
```

因此当前样本中的 KLS-Multishell 不是平坦 clean KLS 残余，而应回流高频 Column/PDEC 证书。
