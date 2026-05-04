# AlphaTail 尾素对端点尖峰吸收

**状态：** `alpha_tail_tailpair_endpoint_absorption_open`

前文 `TailPair local spike route` 显示，局部常数超标会输出责任区间 `D`。样本压测中
`C_local=1.2` 的全部尖峰均为 `EndpointSpike`。本文把这类端点尖峰接入已有
Endpoint/PDEC 出口，避免它继续占用内部尾素对容量预算。

## 1. 端点领口

给定起点窗口

\[
I_m=[A,B],\qquad H=B-A+1.
\tag{TEA-1}
\]

定义端点领口

\[
E_\theta(I_m)=
[A,A+\theta H]\cup[B-\theta H,B].
\tag{TEA-2}
\]

若局部尖峰对应的 `d` 区间

\[
D=[D^-,D^+]
\tag{TEA-3}
\]

满足

\[
\min(D^- - A, B-D^+)\le \theta H,
\tag{TEA-4}
\]

则该尖峰被标记为 `EndpointSpike`。

## 2. 吸收原则

`EndpointSpike` 的本质不是内部尾素对过密，而是几何截断区间贴住 `I_m` 边界：

\[
d=qu-j_1r
\tag{TEA-5}
\]

使 `q` 区间由 `I_m` 端点裁切而来。若这种端点尖峰持续出现，则它给出端点方向的
尾素对共振过密，进入已有的

```text
Endpoint concentration / Directed endpoint CRTDefect / PDEC-or-SAE.
```

若只在单窗出现，则进入 `SAE`。因此在主 tailpair 内区预算中，可以剥离端点尖峰，
只保留 `InteriorSpike`。

## 3. 内区验收

给定 `C_local,theta`，定义

\[
\mathcal S_{\rm int}(C_{\rm local},\theta)
=
\{ \text{local spikes with } C_{\rm loc}>C_{\rm local}
\text{ and }D\not\subset E_\theta(I_m)\}.
\tag{TEA-6}
\]

若

\[
\mathcal S_{\rm int}(C_{\rm local},\theta)=\varnothing,
\tag{TEA-7}
\]

则所有局部尖峰均被吸收到 Endpoint/SAE 出口；内部尾素对共振由 `C_local` 常数包控制。

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_absorption_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_absorption_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --format table
```

输出端点尖峰数、内区尖峰数和是否通过 `interior_clear`。

## 5. 审稿边界

已证明：

```text
局部尖峰可按 d 区间端点距离严格分类；
EndpointSpike 可回流 Endpoint/PDEC/SAE；
若 interior_clear，则内部 TailPairResonance 由 C_local 常数包控制。
```

尚未证明：

```text
Endpoint/PDEC/SAE 出口全部可排斥；
或全局所有窗口均满足 interior_clear。
```

下一步最小硬点是跨窗口扫描/证明 `InteriorSpike` 不持续；若发现持久内区尖峰，则它就是
新的 `TailPairResonance-PDEC/ColumnCRT` 证书。
