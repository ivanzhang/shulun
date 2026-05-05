# AlphaTail `C13` Formal 局部付款合同

**状态：** `formal_local_payment_sample_closed_global_open`

本文专攻 `TFC-D` 的逐窗口付款路线。上一层目标族合同显示：`Gate` 口径在
`p=5003` 局部失败，只能走总池；若要得到不依赖总池交换的局部闭合，必须使用
`Formal+MidVoid`。

## 1. 合同分解

对每个高 `P` 窗口，记 `S=G_geom-R` 为低筛保存余量。Formal 局部付款为

\[
D_{\rm formal}
=U_{\rm edge}+N_{\rm mid}+D_{\ge2}.
\tag{FLP-1}
\]

因此逐窗口充分条件为：

```text
FLP-A: lift>=2 void，即 D_ge2=0；
FLP-B: MidVoid，即 N_mid=0；
FLP-C: EdgeExact，即 U_edge<=S。
```

若三者逐窗口成立，则

\[
D_{\rm formal}=U_{\rm edge}\le S,
\tag{FLP-2}
\]

从而 `Formal` 局部付款闭合。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_formal_local_payment_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_formal_local_payment_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 3. 当前样本结果

```text
slack=2537.963717；
edge=527；
mid=0；
ge2=0；
formal=527；
margin=2010.963717；
min_local_margin=411.727367；
max_formal/slack=0.396937；
mid_void=True；
ge2_void=True；
pass=True。
```

逐窗口：

```text
p=5003:
  S=682.727367；
  U_edge=271；
  N_mid=0；
  D_ge2=0；
  margin=411.727367。

p=10007:
  S=1855.236350；
  U_edge=256；
  N_mid=0；
  D_ge2=0；
  margin=1599.236350。
```

## 4. 当前最窄剩余

`FLP-A` 已由比例结构条件接回 `lift>=2` 模 `6` 空性。当前逐窗口付款路线的全局义务变成：

```text
FormalLocalPayment:
  证明完整目标窗口族中 MidVoid 恒成立；
  证明完整目标窗口族中 U_edge<=S；
  若某窗口失败，则进入有限证书或 PDEC/SAE 出口。
```

这比原来的 `TFC-D` 更窄：不再需要局部 Gate 付款，也不需要中间层或高提升层预算，
只需对边缘 formal units 与低筛保存余量建立逐窗口支配。

