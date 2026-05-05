# AlphaTail `C13` 边缘层 Gate 局部付款合同

**状态：** `edge_gate_payment_sample_closed_global_open`

本文继续压缩 `FormalLocalPayment` 的 `EdgeExact` 义务。关键观察是：当前样本不只满足
`U_edge<=S`，还满足更粗、更适合全局证明的边缘 Gate 上界

\[
K\,G_{\rm edge}\le S,
\tag{EGP-1}
\]

其中 `K` 是低大素块固定长度，`G_edge` 是非空边缘门数，`S=G_geom-R` 是低筛保存余量。
由于每个非空边缘门最多贡献 `K` 个低素候选，有

\[
U_{\rm edge}\le K\,G_{\rm edge}.
\tag{EGP-2}
\]

因此 `(EGP-1)` 推出 `EdgeExact`，且不需要证明低素在边缘门内的精确分布。

## 1. 合同

逐窗口充分条件可改写为：

```text
EGP-A: K*G_edge <= S；
EGP-B: MidVoid；
EGP-C: lift>=2 void。
```

由 `EGP-A` 与 `(EGP-2)` 得 `U_edge<=S`。若再有 `EGP-B/C`，则

\[
D_{\rm formal}=U_{\rm edge}+N_{\rm mid}+D_{\ge2}\le S.
\tag{EGP-3}
\]

这给出逐窗口 Formal 局部付款。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_edge_gate_payment_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_edge_gate_payment_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 3. 当前样本结果

```text
slack=2537.963717；
gate_envelope=848；
unique_edge=527；
gate_margin=1689.963717；
unique_margin=2010.963717；
min_gate_margin=106.727367；
max_gate/slack=0.843675；
edge_gate_pass=True；
edge_exact_pass=True。
```

逐窗口：

```text
p=5003:
  S=682.727367；
  G_edge=72；
  K*G_edge=576；
  U_edge=271；
  gate_margin=106.727367；
  unique_margin=411.727367。

p=10007:
  S=1855.236350；
  G_edge=34；
  K*G_edge=272；
  U_edge=256；
  gate_margin=1583.236350；
  unique_margin=1599.236350。
```

## 4. 新最窄硬点

此前 `FormalLocalPayment` 的剩余为 `MidVoid + U_edge<=S`。本层把第二项进一步替换为
更强但更结构化的 `K*G_edge<=S`。因此目标族全局闭合可走：

```text
TargetFamilyGenerator
=> RatioStructuralVoid
=> lift>=2 void
=> MidVoid
=> EdgeGatePayment
=> FormalLocalPayment
=> C13 high-P local closure.
```

剩余真正硬点变为：

```text
1. 证明完整目标族中 MidStructuralVoid，从而推出 MidVoid，或失败进入 PDEC/SAE；
2. 证明完整目标族中 K*G_edge<=S，或失败进入有限证书/PDEC/SAE。
```

这一步避免了对边缘层低素精确分布的依赖，是比 `EdgeExact` 更可审稿的付款接口。

进一步新增 `prime-matrix-eda-alpha-tail-tailpair-c13-edge-structural-ceiling-contract.md`
后，`G_edge` 可在目标条件下由固定公式控制：

```text
G_edge(m) <= sum_{j1=1}^{m-1} j1^2 + 2*C(m,3)。
```

当前 `m in {4,5}` 给出逐窗口结构上界 `72`，默认 `K=8` 时只需
`S>=576`。样本最紧窗口 `p=5003` 的结构付款余量仍为 `106.727367`。
