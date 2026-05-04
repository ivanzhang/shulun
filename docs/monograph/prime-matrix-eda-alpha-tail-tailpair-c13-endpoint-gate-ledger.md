# AlphaTail `C_local=1.3` 近门槛端点门控账本

**状态：** `c13_endpoint_gate_sample_closed_global_open`

本文接续整数余量账本。上一层把硬点压成 `OnePairMargin-C13`：排除偶 gap 中尺度区间跨过
`C_local=1.3` 整数门槛的最后一个额外素对。本文件继续审计这些近门槛区间是否来自内区，
还是全部贴到原始 `d` 窗口端点。

## 1. 端点门槛定义

对固定 gap 责任区间 `J=[q_-,q_+]`，映回原始变量

\[
d=qu-j_1r.
\tag{EG-1}
\]

得到 `d` 责任区间 `D=[d_-,d_+]`。设原始窗口为 `I=[A,B]`，定义端点距离比

\[
\theta(D,I)=
{\min(d_--A,\;B-d_+)\over |I|}.
\tag{EG-2}
\]

若 `\theta(D,I)<=0.1`，则该近门槛区间进入 `EndpointGate`；否则才是真正内区
`InteriorOnePair`。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_endpoint_gate_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_endpoint_gate_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.3 \
  --slack-cuts '1,2,4,8,12,20,40' --format table
```

输出摘要：

```text
active_even_positive 167 local_C 1.300000 endpoint_theta 0.100000
```

近门槛分类：

```text
slack<=1   : near=2,   endpoint=2,   interior=0；
slack<=2   : near=6,   endpoint=6,   interior=0；
slack<=4   : near=14,  endpoint=14,  interior=0；
slack<=8   : near=31,  endpoint=31,  interior=0；
slack<=12  : near=49,  endpoint=49,  interior=0；
slack<=20  : near=81,  endpoint=81,  interior=0；
slack<=40  : near=123, endpoint=123, interior=0。
```

最大端点距离比仅为：

```text
max_endpoint_ratio=0.000253。
```

最紧记录：

```text
p=997, block=4096, shift=-36, m=5, gap=24, u=3,
q_length=1317, actual=65, threshold=66, slack=1,
required_C=1.292474, endpoint_ratio=0.000253。
```

## 3. 结构含义

样本中 `C13` 压力并非来自窗口中部随机聚集，而是来自贴边责任区间：

```text
OnePairMargin-C13(sample)
=> EndpointGate(sample)。
```

这与前文 `EndpointSpike` 链条一致：端点贴边会把固定 gap 局部常数压力重新送回
`Endpoint/PDEC/SAE/ColumnCRT`，而不是留下新的内区素对常数黑箱。

## 4. 当前最小硬点

全局下一步应直接证明或证书化：

```text
EndpointGate-C13:
  若目标窗口族中偶 gap 区间满足 Delta_13<=L
  （例如 L=40，特别是失败所需的 Delta_13<=0），
  则该区间必须是 EndpointGate；
  若存在 InteriorOnePair，则输出 InteriorSAE 或 PDEC 证书。
```

一旦 `EndpointGate-C13` 成立，本层就可接回已经建立的端点链：

```text
EndpointGate
=> Endpoint concentration
=> Directed endpoint CRTDefect
=> PDEC/SAE/ColumnCRT。
```

## 5. 可引用引理

**引理 EG-1（端点门控路由）。**  
固定 `theta`。若所有满足 `Delta_13<=L` 的目标区间均有 `theta(D,I)<=theta`，则
全部近门槛固定 gap 压力都进入 `EndpointGate`；内区固定 gap 常数包只需处理
`Delta_13>L` 的有正整数余量区间。

**证明。**  
这是 `(EG-2)` 的分类定义。近门槛集合按 `theta(D,I)<=theta` 与其补集二分；若补集为空，
全部近门槛压力均为端点压力。□

## 6. 审稿边界

已完成：

```text
样本中 slack<=40 的近门槛区间全部端点化；
最紧的一票余量区间 endpoint_ratio≈0.000253；
中尺度 C13 压力进一步从内区常数包转向端点门槛链。
```

仍未完成：

```text
全局 EndpointGate-C13；
InteriorOnePair 的 SAE/PDEC 证书化；
端点链最终 PDEC/SAE/ColumnCRT 排斥。
```

因此当前硬点已经从“证明全部中尺度素对常数 <=1.3”压缩为
“近门槛区间是否必贴端点；若不贴端点，则必须物化内区异常证书”。

