# AlphaTail 尾素对局部常数灵敏度账本

**状态：** `alpha_tail_tailpair_local_constant_sensitivity_open`

本文接续单位截断到固定差值短区间常数的归约。目标是审计局部常数 `C_local` 的选择对
`TailPairLocalSpike`、`EndpointSpike` 与后续 PDEC/SAE 分支的影响。

## 1. 常数角色

尾素对常数包有两个层次：

```text
C_global : 控制总体 Brun/Selberg 包络；
C_local  : 控制单个固定 gap 短区间局部尖峰。
```

若某窗口满足

\[
\max_{g,J}{A_g(J)\over B_g(J)}\le C_{\rm local},
\tag{LCS-1}
\]

则该窗口没有 `TailPairLocalSpike`，也不会进入后续端点 PDEC/SAE 链。

## 2. 样本审计

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_local_constant_sensitivity.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_local_constant_sensitivity.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-candidates '1.2,1.25,1.254,1.3,1.5' --format table
```

输出摘要：

```text
rows=6；
max_required_C_BS=0.857166；
max_local_required_C=1.292474；
global_C=1.5 全部通过。
```

候选局部常数：

```text
C_local=1.2   : 6/6 行有尖峰，41 个 EndpointSpike；
C_local=1.25  : 4/6 行仍有尖峰，12 个 EndpointSpike；
C_local=1.254 : 3/6 行仍有尖峰，7 个 EndpointSpike；
C_local=1.3   : 6/6 行全部通过，0 个尖峰；
C_local=1.5   : 6/6 行全部通过，0 个尖峰。
```

因此在当前样本族中，选择

\[
C_{\rm local}=1.3
\tag{LCS-2}
\]

即可吸收全部局部固定 gap 短区间尖峰，前面端点分支只是在 `C_local=1.2` 下暴露出的细化出口。

## 3. 引理：局部常数吸收

**引理 LCS-1（局部常数吸收）。**  
若对某个窗口族和点位长度集合有 `(LCS-1)`，则该窗口族不产生
`TailPairLocalSpike`，从而无需进入 `EndpointSpike / UnitEndpointTruncation / ColumnCRT`
这些下游出口。

**证明。**  
`TailPairLocalSpike` 的定义正是存在某个固定差值短区间满足

\[
A_g(J)>C_{\rm local}B_g(J).
\]

若 `(LCS-1)` 成立，则不存在这样的 `g,J`。所有下游端点、列残基和单位截断分支都是由
`TailPairLocalSpike` 路由产生，因此同步为空。□

## 4. 对当前证明链的影响

当前样本链条可分两种使用方式：

1. **保持 `C_local=1.2`。**  
   需要继续处理端点 PDEC/SAE 细分；目前已压缩到固定 gap 常数缺口。
2. **升级到 `C_local=1.3`。**  
   样本中所有局部尖峰消失，端点链条在样本层面无需启动。

全局证明不能只凭样本升级；需要证明：

\[
\sup_{g,J}{A_g(J)\over B_g(J)}\le1.3
\tag{LCS-3}
\]

在目标窗口族中成立，或给出有限异常 SAE 账本。

## 5. 审稿边界

已完成：

```text
样本局部常数阈值抽取；
C_local=1.3 吸收全部样本局部尖峰；
端点分支与固定 gap 常数包的接口明确化。
```

未完成：

```text
全局固定 gap 短区间常数 <=1.3 的证明；
或所有超 1.3 窗口的有限 SAE 证书；
或调整 C_local 后对完整无限族的重审计。
```
