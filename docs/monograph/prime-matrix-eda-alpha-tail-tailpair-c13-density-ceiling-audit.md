# AlphaTail `C13` 固定 gap 密度天花板审计

**状态：** `c13_density_ceiling_reduction_input_ready`

本文接续 `LayerHighDensityEndpointPair` 的一维化。目标是检验：高密度端点带是否能仅由固定
gap Brun/Selberg 上界直接排斥。

## 1. 密度天花板

对一维层区间

\[
J=[Q,Q+H]
\tag{DCE-1}
\]

若固定 gap 上界输入为

\[
N_g(J)
\le
C_{\rm FG}\,\mathfrak S_g {|J|\over \log^2 Q},
\tag{DCE-2}
\]

则该层 witness 槽密度满足

\[
{N_g(J)\over |J|}
\le
{C_{\rm FG}\mathfrak S_g\over \log^2 Q}.
\tag{DCE-3}
\]

因此：

```text
若 C_FG*S_g/log(Q)^2 <= eta，
则该单层不可能成为 eta-高密度层；

若 C_FG*S_g/log(Q)^2 <= eta/|M|，
则通过 HDE 层投影鸽巢也能排斥总 envelope 高密度。
```

等价的 q 下界为

\[
Q\ge
\exp\sqrt{C_{\rm FG}\mathfrak S_g/\eta}.
\tag{DCE-4}
\]

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_density_ceiling_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_density_ceiling_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --witness-c 1.2 --ceiling-c 1.3 \
  --slack-cut 40 --eta 0.04 --format table
```

输出摘要：

```text
layers=54；
single_layer_sparse_cert=40；
pigeonhole_sparse_cert=0；
max_actual_density=0.030075；
max_ceiling_density=0.049882。
```

最紧未排斥层：

```text
g=24, J=[1366,1498], m=4；
observed=4；
actual_density=0.030075；
required_C=0.783808；
critical_C_eta=1.042465；
critical_C_layer_eta=0.521232。
```

所以 `C_FG=1.3` 不能单独证明 `eta=1/25` 下全局无 `HighDensityEnvelope`。若只要求单层
密度排斥，最坏低 q 层需要约 `C_FG<=1.042465`；若坚持经由两层鸽巢排斥，则需要约
`C_FG<=0.521232`，明显不是普通固定 gap 上筛常数可直接给出的目标。

作为路线测试，若把天花板常数降到 `C_FG=1.0`，当前样本 54 个层全部满足单层
`eta=1/25` 稀疏证书，但仍不能满足 `eta/|M|` 鸽巢证书。这说明真正剩余不是计数程序错误，
而是低 q 端点层的常数精度或层间结构信息不足。

## 3. 对主链的影响

`HighDensityEnvelope` 分支现在有精确二分：

```text
高 q 层：
  若 Q >= exp sqrt(C_FG*S_g/eta)，
  则固定 gap 上界直接排斥单层高密度；

低 q 层：
  必须继续使用 endpoint phase、ColumnCRT、stitching、
  或证明更强的目标族局部常数 C_FG<=1.04。
```

这把高密度出口的最小剩余压成：

```text
LowQ-Layer-HDE:
  对 q 低于临界阈值的端点带层，
  证明层唯一性/相位互斥，
  或给出 <=1.04 的目标族固定 gap 局部上界，
  或把该层送入 ColumnCRT/stitching 排斥。
```

## 4. 审稿边界

已完成：

```text
固定 gap 上界到端点带密度天花板的逐行推导；
显式 q 临界阈值与临界常数公式；
样本中 40/54 层由 C_FG=1.3 单层天花板排斥；
定位 14 个低 q 层为真正剩余。
```

仍未完成：

```text
全局证明低 q 层不存在或可有限化；
目标端点带固定 gap 常数 <=1.04；
层间鸽巢所需的 eta/|M| 强排斥；
ColumnCRT/stitching 对低 q 高密度层的最终排斥。
```

所以本文完成的是高密度分支的密度天花板归约，不是行命题最终闭合。
