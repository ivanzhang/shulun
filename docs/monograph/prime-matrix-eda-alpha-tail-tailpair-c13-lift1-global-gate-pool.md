# AlphaTail `C13` 的 `lift=1` 全局门数总池证书

**状态：** `c13_lift1_global_gate_pool_sample_closed_global_open`

本文合并边缘层与中间层，给出 `lift=1` 分支的两个付款口径：

```text
GatePool:
  只使用纯门数包络 K(G_edge+G_mid)。

Formal+MidVoid:
  使用边缘 formal unit 去重与中间层精确空性。
```

## 1. 两个付款不等式

由边缘层与中间层分解，

\[
D_1\le N_{\rm edge}+N_{\rm mid}.
\tag{GGP-1}
\]

纯门数包络给出

\[
D_1\le K(G_{\rm edge}+G_{\rm mid}).
\tag{GGP-2}
\]

若使用更精细的 formal 去重与中间层空性，则

\[
D_1\le U_{\rm edge}+N_{\rm mid}.
\tag{GGP-3}
\]

当前样本中 `N_mid=0`，所以

\[
D_1\le U_{\rm edge}.
\tag{GGP-4}
\]

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_global_gate_pool.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_global_gate_pool.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 3. 总池结果

高 P 总池：

```text
slack=2537.963717；
edge_gate=848；
mid_gate=1184；
gate_env=2032；
gate_margin=505.963717；
gate_env/slack=0.800642；
formal=527；
formal_margin=2010.963717；
mid_void=True。
```

因此当前高 P 总池中，纯门数包络已经足以支付全部 `lift=1` 删除。

## 4. 局部边界

逐窗口：

```text
p=5003:
  slack=682.727367；
  gate_env=1168；
  gate_margin=-485.272633；
  formal=271；
  formal_margin=411.727367；
  mid_void=True。

p=10007:
  slack=1855.236350；
  gate_env=864；
  gate_margin=991.236350；
  formal=256；
  formal_margin=1599.236350；
  mid_void=True。
```

逐层：

```text
p=5003,m=4:
  gate_env=368>slack=221.206390；
  formal=77<slack。

p=5003,m=5:
  gate_env=800>slack=461.520978；
  formal=194<slack。
```

所以审稿时必须明确：

```text
若主链允许高 P 总池付款，则 GatePool 样本闭合；
若主链要求逐窗口或逐层局部付款，则必须使用 Formal+MidVoid。
```

## 5. 全局接口

下一步最小硬点分成两个可选闭合路线：

```text
GlobalGatePool:
  在全局高 P 总池中证明 K(G_edge+G_mid)<=S_total。

LocalFormalMidVoid:
  在每个窗口或层证明 U_edge+N_mid<=S_local。
```

当前样本显示：

```text
GlobalGatePool 总池通过；
LocalFormalMidVoid 逐窗口与逐层通过；
LocalGatePool 在 p=5003 失败。
```

这说明下一步不应再攻击局部门数包络，而应优先严写：

```text
1. 总池付款在 HighP-PLT 主链中的合法性；
2. 或 formal+MidVoid 的逐窗口全局化。
```

## 6. 审稿边界

已完成：

```text
lift=1 的 GatePool 与 Formal+MidVoid 两种付款口径；
当前高 P 总池 GatePool 通过；
当前压力样本 Formal+MidVoid 逐窗口、逐层通过；
明确 LocalGatePool 不足，避免误宣称局部闭合。
```

仍未完成：

```text
全局证明 GlobalGatePool 或 LocalFormalMidVoid；
证明该 lift=1 付款口径与 HighP-PLT 的求和口径完全一致；
与 lift>=2 Mod6Void 一起接回 LowSievePreservation。
```
