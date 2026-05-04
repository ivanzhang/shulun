# AlphaTail `C13` 的 `HighP-PLT` 低筛闭合桥

**状态：** `c13_highp_plt_closure_bridge_sample_closed_global_open`

本文把低筛保存总池桥接进一步接回 `HighP-PLT`。核心检查是：

\[
G_{\rm geom}-D_{\rm low}^{\rm upper}\ge R,
\tag{HPC-1}
\]

其中 `R=B2+Cap_even` 是 `HighP-PLT` 要求的固定 gap 尾素对下界。

## 1. 闭合判据

对目标族 `F`，若

\[
\sum_{a\in F}\bigl(G_{\rm geom}(a)-D_{\rm low}^{\rm upper}(a)\bigr)
\ge
\sum_{a\in F}R(a),
\tag{HPC-2}
\]

则 `HighP-PLT` 成立。由 `PLT-1`，这进一步推出高 P 的 `D2` 预算条件。

本文同时检查两种删除上界：

```text
Gate:
  D_low^upper = K(G_edge+G_mid)+D_ge2。

Formal:
  D_low^upper = U_edge+N_mid+D_ge2。
```

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_highp_plt_closure_bridge.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_highp_plt_closure_bridge.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 3. 高 P 总池结果

```text
geom=17860；
required=15322.036283；
actual_low=17810；
gate_deleted=2032；
formal_deleted=527；
gate_low_lower=15828；
formal_low_lower=17333；
actual_margin=2487.963717；
gate_margin=505.963717；
formal_margin=2010.963717；
gate_pass=True；
formal_pass=True。
```

所以当前压力样本的高 P 总池中，

\[
G_{\rm geom}-D_{\rm Gate}^{\rm upper}
=15828
>15322.036283
=R.
\tag{HPC-3}
\]

这给出样本级 `HighP-PLT` 闭合证书。

## 4. 局部边界

逐窗口：

```text
p=5003:
  geom=6325；
  required=5642.272633；
  gate_low_lower=5157；
  gate_margin=-485.272633；
  formal_low_lower=6054；
  formal_margin=411.727367。

p=10007:
  geom=11535；
  required=9679.763650；
  gate_low_lower=10671；
  gate_margin=991.236350；
  formal_low_lower=11279；
  formal_margin=1599.236350。
```

因此：

```text
Gate 口径只在高 P 总池中闭合；
Formal 口径在当前样本逐窗口也闭合。
```

这与前一层 `LocalGatePool` 失败完全一致，没有口径冲突。

## 5. 审稿边界

已完成：

```text
把 LowSievePreservation 上界直接接回 HighP-PLT；
当前压力样本的高 P 总池 Gate 口径闭合；
当前压力样本的 Formal 口径逐窗口闭合；
明确 p=5003 的 Gate 局部失败不能用于局部证明。
```

仍未完成：

```text
全局证明完整目标族的 Gate 总池不等式；
或全局证明 Formal 逐窗口不等式；
全局证明 lift>=2 Mod6Void；
将该 HighP-PLT 闭合桥推广到所有高 P 目标窗口。
```

所以本文闭合当前压力样本的 `HighP-PLT` 桥，不是行命题全局闭合。
