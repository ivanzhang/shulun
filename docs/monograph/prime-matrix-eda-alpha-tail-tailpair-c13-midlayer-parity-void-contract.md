# AlphaTail `C13` 中间层奇偶空性合同

**状态：** `midlayer_parity_void_sample_closed_global_open`

本文专攻 `MidVoid`。样本显示所有非空中间门均满足

```text
h/u = 1/2。
```

这使中间层空性不再依赖低素分布，而退化为一个奇偶同余阻断。

## 1. 中间层同余

在 `lift=1` 的 offset 分解中，中间层 `0<h<u` 的低素 `ell` 必须满足

\[
n+h\ell\equiv 0\pmod u,
\tag{MPV-1}
\]

其中

\[
n=-(j-j_1)r.
\tag{MPV-2}
\]

若所有非空中间门都满足 `(h,u)=(1,2)`，则 `(MPV-1)` 化为

\[
n+\ell\equiv0\pmod2.
\tag{MPV-3}
\]

若 `r` 为偶数，则 `n` 为偶数；若低素块满足 `ell>2`，则所有低素 `ell` 为奇数。于是
`n+ell` 为奇数，不可能满足 `(MPV-3)`。因此中间层没有任何低素命中：

\[
N_{\rm mid}=0.
\tag{MPV-4}
\]

## 2. 合同

逐窗口充分条件：

```text
MPV-A: 所有非空中间门都满足 h/u=1/2；
MPV-B: r 为偶数；
MPV-C: 低素块最小素数 L>2。
```

则 `MidVoid` 成立。这里 `MPV-B/C` 在高 `P` 目标族中很弱：当前目标族已要求
`6||r|`，且 `L>alpha p>2`。

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_midlayer_parity_void_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_midlayer_parity_void_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 4. 当前样本结果

```text
layers=4；
mid_gates=148；
integer_ceiling=3922；
mid_exact=0；
half_only=True；
shift_even=True；
low_odd=True；
parity_void=True；
mid_void=True。
```

逐层：

```text
p=5003,m=4: h_ratios={'1/2':24}, exact=0；
p=5003,m=5: h_ratios={'1/2':50}, exact=0；
p=10007,m=4: h_ratios={'1/2':24}, exact=0；
p=10007,m=5: h_ratios={'1/2':50}, exact=0。
```

## 5. 新剩余

`MidVoid` 已从“低素实际 miss”压缩为“所有中间门只有 `h/u=1/2`”。全局剩余为：

```text
证明完整目标族中所有非空中间门满足 h/u=1/2；
若出现 h/u != 1/2，则进入 PDEC/SAE 或有限证书出口。
```

这与 `EdgeGatePayment` 合并后，`FormalLocalPayment` 的两项实质义务变成：

```text
MidHalfOnly；
EdgeGatePayment。
```

