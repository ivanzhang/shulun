# AlphaTail `C13` 结构边缘付款的 SlackFloor 合同

**状态：** `slack_floor_sample_closed_global_open`

本文把上一层 `EdgeStructuralPayment` 的最后数值条件

\[
S\ge K E_M
\tag{SF-1}
\]

单独抽出。这里 `S=G_geom-R` 是低筛保存余量，`K=num_primes`，
而

\[
E_M=\sum_{m\in M}
\left(
\sum_{j_1=1}^{m-1}j_1^2+2\binom m3
\right)
\tag{SF-2}
\]

是边缘门结构上界。默认 `M={4,5}` 时 `E_M=72`，`K=8` 时 `K E_M=576`。

## 1. 余量分解

对每个 `m` 层，记

```text
R_m = B2_model(m)+Cap_even(m)；
S_m = G_geom(m)-R_m。
```

则

\[
S_m
=
\bigl(M_2(m)-R_m\bigr)
+
\bigl(G_{\rm geom}(m)-M_2(m)\bigr).
\tag{SF-3}
\]

第一项是共振正余量，第二项是几何截断缓冲。若已知

\[
G_{\rm geom}(m)\ge M_2(m),
\tag{SF-4}
\]

则更强的充分条件为

\[
\sum_{m\in M}\bigl(M_2(m)-R_m\bigr)\ge K E_M.
\tag{SF-5}
\]

这就是 `ResonanceFloor`：它不再依赖边缘层低素分布，也不依赖中间层候选，只要求二阶共振实际量相对模型与端点容量有足够正余量。

## 2. 当前样本审计

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_slack_floor_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_slack_floor_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
edge_envelope=1152；
total_resonance_margin=2487.963717；
total_geometric_buffer=50；
total_slack=2537.963717；
total_resonance_floor_margin=1335.963717；
total_slack_floor_margin=1385.963717；
min_resonance_floor_margin=101.727367；
min_slack_floor_margin=106.727367；
res_pass=True；
slack_pass=True。
```

逐窗口：

```text
p=5003:
  resonance_margin=677.727367；
  geometric_buffer=5；
  S=682.727367；
  K E_M=576；
  resonance_floor_margin=101.727367；
  slack_floor_margin=106.727367。

p=10007:
  resonance_margin=1810.236350；
  geometric_buffer=45；
  S=1855.236350；
  K E_M=576；
  resonance_floor_margin=1234.236350；
  slack_floor_margin=1279.236350。
```

## 3. 缩窄后的全局义务

结合前两层合同，当前局部闭合链可写成：

```text
RatioStructuralVoid
+ MidStructuralVoid
+ EdgeStructuralCeiling
+ SlackFloor
=> FormalLocalPayment。
```

所以完整目标族的剩余付款义务已经缩窄为：

```text
证明每个 C13 高 P 目标窗口满足 ResonanceFloor:
  sum_m (M2(m)-B2_model(m)-Cap_even(m)) >= K E_M；

或较弱地证明 SlackFloor:
  sum_m (G_geom(m)-B2_model(m)-Cap_even(m)) >= K E_M。
```

若个别窗口失败，则必须进入有限证书、formal 去重、PDEC 或 SAE 出口。

## 4. 审稿边界

该合同仍是显式样本闭合与条件接口，不是行命题全局无条件证明。真正未闭合项是：

```text
TargetFamilyGenerator 不遗漏目标窗口；
完整目标族上的 ResonanceFloor/SlackFloor 通用下界；
失败窗口的有限证书或 PDEC/SAE 出口。
```
