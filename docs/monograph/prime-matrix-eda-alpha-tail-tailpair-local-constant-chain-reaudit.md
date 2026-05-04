# AlphaTail 尾素对局部常数全链重审计

**状态：** `alpha_tail_tailpair_local_constant_chain_reaudit_sample_closed_global_open`

本文接续局部常数灵敏度账本，目标是核查把固定 gap 局部常数提升到

\[
C_{\rm local}=1.3
\tag{LCR-1}
\]

后，`TailPairLocalSpike`、`EndpointSpike`、`UnitEndpointTruncation` 与后续
`PDEC/SAE/ColumnCRT` 链条是否仍被启动。

## 1. 审计对象

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_local_constant_chain_reaudit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_local_constant_chain_reaudit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.3 --format table
```

输出摘要：

```text
rows 6 global_C 1.500000 local_C 1.300000 spikes 0 endpoint 0 interior 0 all_global_pass True all_local_pass True downstream_empty True
```

因此在当前六个样本窗口中：

```text
TailPairLocalSpike = 0；
EndpointSpike = 0；
InteriorSpike = 0；
downstream_route = DownstreamEmpty。
```

## 2. 引理：局部常数链清空

**引理 LCR-1（局部常数全链清空）。**  
固定窗口族、点位长度集合与 `C_local`。若对每一行样本都有

\[
\max_{g,J}{A_g(J)\over B_g(J)}\le C_{\rm local},
\tag{LCR-2}
\]

则该样本族不产生 `TailPairLocalSpike`。因此所有由该尖峰路由产生的
`EndpointSpike`、`InteriorSAE`、`UnitEndpointTruncation`、`PDEC/SAE/ColumnCRT`
下游分支同步为空。

**证明。**  
`TailPairLocalSpike` 的定义是存在某个固定差值短区间 `(g,J)` 使

\[
A_g(J)>C_{\rm local}B_g(J).
\]

条件 `(LCR-2)` 正好否定这种存在性。端点尖峰、内部 SAE、单位截断和端点
`PDEC/SAE/ColumnCRT` 分支在本链条中均由 `TailPairLocalSpike` 作为前置责任证书产生；
前置集合为空时，下游路由集合也为空。□

## 3. 与前一版常数的关系

前一版 `C_local=1.2` 的样本链暴露：

```text
EndpointSpike = 41。
```

灵敏度账本进一步显示：

```text
C_local=1.254 时仍有 7 个 EndpointSpike；
C_local=1.3 时所有局部尖峰清空。
```

本重审计不是新的数学闭合定理，而是确认：若正式证明可接受的固定 gap 短区间常数达到
`1.3`，则当前端点/单位截断/PDEC 细链无需继续启动。

## 4. 审稿边界

已完成：

```text
样本全链重审计；
C_local=1.3 下样本 TailPairLocalSpike 清空；
端点、内区、单位截断、PDEC/SAE/ColumnCRT 下游同步清空。
```

仍未完成：

```text
全局固定 gap 短区间常数包 <=1.3 的证明；
或所有超过 1.3 的窗口给出有限/可求和 SAE 证书；
或把目标无限窗口族全部纳入机器可复现证书。
```

因此本文只升级样本链条状态，不把 Prime Matrix 行命题升级为无条件闭合。

