# AlphaTail `C13` 低 q 层共享锚重叠证书

**状态：** `c13_lowq_overlap_certificate_input_ready`

本文接续固定 gap 密度天花板审计。当天花板常数不足以直接排斥低 q 端点层时，下一步不是把
这些层当作彼此独立的异常，而是检查它们是否被同一批尾素锚反复复用。

## 1. 低 q 剩余集合

固定参数 `eta` 与候选天花板常数 `C_FG`。定义低 q 剩余层为所有满足

\[
{C_{\rm FG}\mathfrak S_g\over \log^2 Q}>\eta
\tag{LQO-1}
\]

的一维固定 gap 层

\[
J=[Q,Q+H],\qquad q,q+g\in\mathcal P_{\rm tail}.
\tag{LQO-2}
\]

这些层不能由单层密度天花板自动排斥，必须进入结构审计。

## 2. 共享锚压缩

对低 q 层定义共享锚集

\[
\mathcal A_{\rm low}
=
\{q:\exists g,J,\ q\in J,\ q,q+g\in\mathcal P_{\rm tail}\}.
\tag{LQO-3}
\]

同时定义固定 gap 素对集

\[
\mathcal P_{\rm low}
=
\{(q,q+g,g):q,q+g\in\mathcal P_{\rm tail}
\text{ and occurs in a low q layer}\}.
\tag{LQO-4}
\]

**引理 LQO-1（低 q 剩余到共享锚证书）。**  
所有未被 `(LQO-1)` 排斥的低 q 层，其 witness 总质量都由
`\mathcal A_low` 与 `\mathcal P_low` 支撑。若每个共享锚在后续 ColumnCRT/stitching 中的可复用
次数有上界 `R(q)`，则低 q 分支满足

\[
\sum_{\text{low layers}} S_m
\le
\sum_{q\in\mathcal A_{\rm low}} R(q).
\tag{LQO-5}
\]

**证明。**  
每个低 q 层 witness 按定义都是某个固定 gap 素对 `(q,q+g)`。把所有 witness 投影到第一
坐标 `q` 即得 `\mathcal A_low`，投影到三元组即得 `\mathcal P_low`。若同一 `q` 不能在
ColumnCRT/stitching 中复用超过 `R(q)` 次，则对所有 `q` 求和得到 `(LQO-5)`。□

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_lowq_overlap_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowq_overlap_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --witness-c 1.2 --ceiling-c 1.3 \
  --eta 0.04 --slack-cut 40 --format table
```

输出摘要：

```text
lowq_layers=14；
actual_sparse=14；
actual_high=0；
min_eta_slack=1.320000；
total_layer_witnesses=26；
unique_q=9；
unique_pairs=12；
max_q_multiplicity=6。
```

最重共享锚为

```text
q=1427；
出现 6 次；
支撑素对 1427+12=1439 与 1427+24=1451。
```

低 q 剩余的全部 q 锚为：

```text
1373, 1399, 1409, 1423, 1427, 1429, 1439, 1447, 1459。
```

因此当前样本中，不能由 `C_FG=1.3` 密度天花板排斥的 14 层并非 14 个独立异常，而是 26 个
层 witness 压缩到 9 个 q 锚、12 个固定 gap 素对。并且这些低 q 层的精确有限计数已经全部
满足 `eta=1/25` 稀疏条件，最小整数余量为 `1.32` 个槽；也就是说，当前样本的低 q 分支
可由有限证书排除真实 `HighDensityEnvelope`，但全局证明仍需把这种有限化机制形式化。

## 4. 对主链的影响

低 q 分支现在细化为：

```text
LowQ-Layer-HDE
=> shared q-anchor support
=> bounded q-anchor reuse
=> ColumnCRT/stitching contradiction
   or finite low-q certificate.
```

下一步最小硬点变为：

```text
LowQ-Reuse-Cap:
  证明同一尾素锚 q 在固定 endpoint residue、固定 side、固定 u 的低 q 层中
  不能被过度复用；特别是要用 j-index 几何、gap 三角关系和 ColumnCRT
  把 max_q_multiplicity 压到可支付范围。
```

这一路线比继续改进普通固定 gap 常数更窄：普通 `C_FG=1.3` 卡在低 q 常数，而共享锚证书
直接利用了高密度层的相位复用刚性。

## 5. 审稿边界

已完成：

```text
低 q 未排斥层的共享锚投影；
样本中 14 层到 9 个 q 锚、12 个素对的压缩；
样本中 14 个低 q 层的精确有限稀疏验收；
把后续义务明确为 q-anchor reuse 上界。
```

仍未完成：

```text
全局 LowQ-Reuse-Cap；
共享 q 锚复用与 ColumnCRT/stitching 的严格矛盾；
低 q 剩余的有限证书或可求和证书。
```

所以本文完成的是低 q 分支结构压缩，不是行命题最终闭合。
