# AlphaTail `C13` 端点相位键接入账本

**状态：** `c13_endpoint_phase_ledger_sample_closed_endpoint_exits_open`

本文接续 `C13` 二分路由定理。short-`q` 分支已由 TailCutoffVoid 样本清空；本文处理
small-`u` 端点分支如何接入既有 `Endpoint/PDEC/SAE/ColumnCRT` 链。

## 1. 端点相位键

对 small-`u` 责任区间，由格点端点引理自动进入 `EndpointGate`。定义端点相位键

\[
K=(g,j_1,j_2,u,\mathrm{side}),
\tag{EPL-1}
\]

其中 `side` 是较近端点：

```text
left  : d_- 更靠近 A；
right : d_+ 更靠近 B。
```

同一 `K` 的近门槛记录若跨窗口族持久出现，则进入既有端点缺陷链：

```text
EndpointGate(K)
=> Endpoint concentration
=> Directed endpoint CRTDefect
=> PDEC/ColumnCRT。
```

若只出现有限次，则登记为 `SAE`。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_endpoint_phase_ledger.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_endpoint_phase_ledger.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
```

输出摘要：

```text
records 123 failures 0 keys 59 slack_cut 40
min_slack 1 max_required_C 1.292474
side_counts {'left': 78, 'right': 45}
```

最紧端点键：

```text
K=(24,2,0,3,left), count=2, failures=0, min_slack=1, max_required_C=1.292474；
K=(24,3,1,3,left), count=2, failures=0, min_slack=1, max_required_C=1.289379。
```

因此当前样本中 near-C13 端点分支没有实际失败；若把阈值继续压紧，则最先触发的也是
明确的端点相位键，而不是无结构的中尺度素对异常。

## 3. 可引用引理

**引理 EPL-1（C13 端点键路由）。**  
任何 small-`u` 的 `C13` 失败或近门槛记录都带有端点相位键 `(EPL-1)`。若同一键在无限
窗口族中持久承担正超额，则它进入 `Directed endpoint CRTDefect/PDEC/ColumnCRT`；否则它
是有限或可求和 `SAE`。

**证明。**  
small-`u` 由 `LEG-2` 强制端点化。固定 `g,j_1,j_2,u` 与端点侧后，责任区间的端点位置
由同余格点 `d≡-j_1r mod u` 的首末点决定，故形成固定相位键。持久正超额正是既有
`EndpointDefect` 定义；非持久情形按定义进入 SAE。□

## 4. 对主链的影响

`C13` 分支现在合成为：

```text
TailPairLocalSpike(C13)
=> small-u EndpointPhaseKey K
   or large-u TailCutoffVoid / finite short-q certificate.
```

样本中：

```text
large-u 已 TailCutoffVoid；
small-u 近门槛 keys=59，但 failures=0。
```

因此样本 `C13` 分支已全清空；全局剩余只剩端点键的 persistent 排斥或 SAE 登记。

## 5. 审稿边界

已完成：

```text
C13 small-u 端点相位键定义；
样本 near-C13 端点键账本；
端点分支接入既有 Endpoint/PDEC/SAE/ColumnCRT 链。
```

仍未完成：

```text
全局持久端点键 PDEC/ColumnCRT 排斥；
全局非持久端点键 SAE 可求和账本；
TailCutoffVoid 不等式在目标无限窗口族上的证明。
```

