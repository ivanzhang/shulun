# AlphaTail `C13` 的低筛保存总池桥接

**状态：** `c13_lowsieve_global_pool_bridge_sample_closed_global_open`

本文把 `lift=1` 的 `GlobalGatePool/Formal+MidVoid` 与 `lift>=2` 空性合成，并说明何时可接回
`HighP-PLT`。

## 1. 总池付款引理

对目标族 `F` 中每个层 `a`，记

```text
G_geom(a)  低筛前的固定 gap 几何候选数；
R(a)       HighP-PLT 要求的下界；
S(a)       = G_geom(a)-R(a)；
D_low(a)  低筛删除量。
```

若

\[
\sum_{a\in F}D_{\rm low}(a)\le \sum_{a\in F}S(a),
\tag{LGP-1}
\]

则

\[
\sum_{a\in F}G^L(a)
=
\sum_{a\in F}\bigl(G_{\rm geom}(a)-D_{\rm low}(a)\bigr)
\ge
\sum_{a\in F}R(a).
\tag{LGP-2}
\]

这正是 `HighP-PLT` 的聚合输入。因此：

**引理 LGP-1（总池低筛保存）。**  
只要 `HighP-PLT` 的目标族按同一集合 `F` 求和，低筛删除余量可以在 `F` 内总池付款。

**证明。**  
直接由 `(LGP-1)` 代入 `G^L=G_geom-D_low` 得 `(LGP-2)`。该式与 `PLT-7`
同口径，因此推出聚合 `LowSievePreservation`。□

## 2. 两种 lift=1 付款口径

由前文：

\[
D_1\le K(G_{\rm edge}+G_{\rm mid})
\tag{LGP-3}
\]

或更强地

\[
D_1\le U_{\rm edge}+N_{\rm mid}.
\tag{LGP-4}
\]

再与 `lift>=2` 合成：

\[
D_{\rm low}
\le
K(G_{\rm edge}+G_{\rm mid})+D_{\ge2}
\tag{LGP-5}
\]

以及

\[
D_{\rm low}
\le
U_{\rm edge}+N_{\rm mid}+D_{\ge2}.
\tag{LGP-6}
\]

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_global_pool_bridge.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_global_pool_bridge.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 4. 样本结果

高 P 总池：

```text
slack=2537.963717；
gate_lift1=2032；
formal_lift1=527；
ge2_both=0；
ge2_candidates=1368；
gate_consumed=2032；
formal_consumed=527；
gate_margin=505.963717；
formal_margin=2010.963717；
mid_void=True；
ge2_void=True；
gate_pass=True；
formal_pass=True。
```

逐窗口：

```text
p=5003:
  slack=682.727367；
  gate_consumed=1168；
  gate_margin=-485.272633；
  formal_consumed=271；
  formal_margin=411.727367；
  gate_pass=False；
  formal_pass=True。

p=10007:
  slack=1855.236350；
  gate_consumed=864；
  gate_margin=991.236350；
  formal_consumed=256；
  formal_margin=1599.236350；
  gate_pass=True；
  formal_pass=True。
```

所以当前压力样本有两个可用出口：

```text
1. 若 HighP-PLT 允许高 P 目标族总池付款：
   使用 GatePool，低筛保存总池闭合。

2. 若要求逐窗口局部付款：
   使用 Formal+MidVoid，当前样本逐窗口闭合。
```

## 5. 审稿边界

已完成：

```text
总池低筛保存引理；
GatePool+lift>=2 的高 P 总池闭合；
Formal+MidVoid+lift>=2 的逐窗口样本闭合；
明确 LocalGatePool 在 p=5003 失败，不能误用。
```

仍未完成：

```text
全局证明完整目标族的 GatePool 总池不等式；
或全局证明每个窗口的 Formal+MidVoid 不等式；
全局证明 lift>=2 Mod6Void，或给未空候选 PDEC/SAE 出口；
把该桥接应用到所有高 P 目标窗口族。
```

因此本文完成的是当前压力样本的主链接口桥接，不是行命题全局闭合。
