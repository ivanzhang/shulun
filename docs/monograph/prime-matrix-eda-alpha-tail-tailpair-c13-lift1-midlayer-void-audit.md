# AlphaTail `C13` 的 `lift=1` 中间 h 层空性审计

**状态：** `c13_lift1_midlayer_void_sample_closed_global_open`

本文接续 `lift=1` 的 h-layer 分解与边缘层预算。边缘层为 `h=0` 与 `h=u`；
本节处理真正剩余的中间层

\[
0<h<u.
\tag{LMV-1}
\]

## 1. 中间层判据

固定 channel 后仍有

\[
u a=n+h\ell,\qquad q=\ell+a=\frac{(u+h)\ell+n}{u}.
\tag{LMV-2}
\]

中间层候选必须满足：

```text
1 <= h <= u-1；
ell 落入由 q 区间反推得到的 I_h(c)；
h*ell+n == 0 mod u；
0 <= (n+h*ell)/u < ell；
a+g != 0 mod ell。
```

因此中间层的真实整数候选数满足纯门数上界

\[
N_{\rm mid}\le K\,G_{\rm mid},
\tag{LMV-3}
\]

其中 `K=num_primes`，`G_mid` 是满足上述区间与同余门控的非空中间 h-gate 数。

## 2. 样本结构

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_midlayer_void_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_midlayer_void_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
highP-total:
  slack=2537.963717；
  mid_exact=0；
  mid_gates=148；
  mid_integer_ceiling=3922；
  mid_gate_envelope=1184；
  mid_gate_envelope/slack=0.466516；
  mid_void=True。
```

逐窗口：

```text
p=5003:
  mid_exact=0；
  mid_gates=74；
  mid_gate_envelope=592；
  mid_gate_envelope/slack=0.867110。

p=10007:
  mid_exact=0；
  mid_gates=74；
  mid_gate_envelope=592；
  mid_gate_envelope/slack=0.319097。
```

逐层：

```text
p=5003,m=4:
  mid_exact=0；
  mid_gates=24；
  mid_gate_envelope=192；
  mid_gate_envelope/slack=0.867968。

p=5003,m=5:
  mid_exact=0；
  mid_gates=50；
  mid_gate_envelope=400；
  mid_gate_envelope/slack=0.866699。

p=10007,m=4:
  mid_exact=0；
  mid_gate_envelope/slack=0.254201。

p=10007,m=5:
  mid_exact=0；
  mid_gate_envelope/slack=0.363660。
```

当前样本所有中间门的比例均为

\[
\frac{h}{u}=\frac12.
\tag{LMV-4}
\]

这说明样本中间层不是任意 h 层扩散，而是被压缩到唯一半提升层。

## 3. 与边缘层合并

边缘层已有

\[
K\,G_{\rm edge}=848.
\tag{LMV-5}
\]

本节得到

\[
K\,G_{\rm mid}=1184.
\tag{LMV-6}
\]

所以高 P 总池中

\[
K(G_{\rm edge}+G_{\rm mid})
=2032
<2537.963717.
\tag{LMV-7}
\]

这给出一个比“必须证明 `mid_exact=0`”更弱但更稳的样本出口：即使不使用中间层精确空性，
只用纯门数包络也能在高 P 总池付款。

审稿边界必须保留：该付款是总池付款，不是逐窗口付款。`p=5003` 的逐窗口
`edge_gate+mid_gate` 包络超过本窗口 slack，因此若主链要求逐窗口局部付款，
仍需使用 `mid_exact=0` 或 formal 去重。

## 4. 全局接口

当前 `lift=1` 分支可以写成

\[
D_1\le
K(G_{\rm edge}+G_{\rm mid})
\tag{LMV-8}
\]

或更强地写成

\[
D_1\le U_{\rm edge}+N_{\rm mid}.
\tag{LMV-9}
\]

下一步最小硬点变成二选一：

```text
GlobalGatePool:
  证明全局总池 K(G_edge+G_mid) 小于 LowSievePreservation slack。

MidVoid/Formal:
  若总池不够，证明 N_mid=0，或对中间层做 formal unit 去重/PDEC。
```

## 5. 审稿边界

已完成：

```text
中间 h 层判据独立成章；
当前压力样本 mid_exact=0；
当前压力样本中间层全部落在 h/u=1/2；
当前压力样本总池 K(G_edge+G_mid)=2032<2537.963717。
```

仍未完成：

```text
全局证明 GlobalGatePool；
若 GlobalGatePool 失败，则全局证明 MidVoid 或 formal/PDEC 出口；
把 lift=1 总池付款与 lift>=2 Mod6Void 一起接回 LowSievePreservation。
```
