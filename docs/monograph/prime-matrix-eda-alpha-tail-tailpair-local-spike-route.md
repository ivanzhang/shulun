# AlphaTail 尾素对局部尖峰的 SAE/Endpoint 路由

**状态：** `alpha_tail_tailpair_local_spike_route_open`

本文处理 `TailPair Brun acceptance` 中的失败分支：

```text
C_loc(g,J)>C_local.
```

目标是把“局部常数超标”严写成可提交的责任证书，而不是让它重新变成模糊异常。

## 1. 局部尖峰证书

固定 `g,j_1,j_2`，几何截断给出短区间

\[
J=[Q_-,Q_+].
\tag{TLS-1}
\]

记

\[
A_g(J)=\#\{q\in J:q,q+g\in\mathcal P_T\},
\qquad
B_g(J)=\mathfrak S_g {|J|\over \log^2Q_-}.
\tag{TLS-2}
\]

给定阈值 `C_local`，若

\[
A_g(J)>C_{\rm local}B_g(J),
\tag{TLS-3}
\]

则输出责任证书

```text
(p, block, r, m, g, j1, j2, u, J, A_g(J), B_g(J), C_loc).
```

这就是 `TailPairLocalSpike`。

## 2. 回到原始 d 窗口

由

\[
d=qu-j_1r
\tag{TLS-4}
\]

尖峰区间对应原始起点区间

\[
D=[uQ_- - j_1r,\ uQ_+ - j_1r]\subset I_m.
\tag{TLS-5}
\]

因此局部尖峰只能以两种方式对坏窗口持续有贡献：

1. **Endpoint 型。**  
   `D` 长期贴近 `I_m` 的端点，说明尾素对共振由端点截断制造，进入 Endpoint concentration。
2. **Interior SAE 型。**  
   `D` 位于内部但只在少数窗口发生，进入 SAE。

若内部尖峰在许多窗口持续复现，则同一 `(g,j_1,j_2,u)` 的短差值素对过密持续存在，
这不再是 SAE，而是 persistent `TailPairResonance-PDEC/ColumnCRT`。

## 3. 三分路由

给定尺度参数 `theta_end in (0,1)`，定义端点距离

\[
\operatorname{dist}_{I_m}(D)
=\min(D^- - I_m^-, I_m^+ - D^+).
\tag{TLS-6}
\]

若

\[
\operatorname{dist}_{I_m}(D)\le \theta_{\rm end}|I_m|,
\tag{TLS-7}
\]

则标记为 `EndpointSpike`。否则标记为 `InteriorSpike`。对 `InteriorSpike`：

```text
单窗或有限少数 => SAE；
跨窗口同形状持续 => TailPairResonance-PDEC/ColumnCRT。
```

这把 `C_loc` 超标压成具体的 endpoint/SAE/PDEC 责任项。

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_local_spike_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_local_spike_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --format table
```

脚本输出所有 `C_loc>local_c` 的责任区间。若阈值取 `1.5`，当前样本无尖峰；若取
`1.2`，脚本会列出最坏局部区间，用于测试 Endpoint/SAE 路由。

## 5. 审稿边界

已证明：

```text
C_loc 超标 => 显式 TailPairLocalSpike 责任证书；
责任证书通过 d=qu-j1r 映射回原始窗口；
责任证书可三分为 EndpointSpike / InteriorSAE / persistent PDEC-ColumnCRT。
```

尚未证明：

```text
EndpointSpike 全部可排斥；
InteriorSpike 只能孤立出现，或 persistent 分支可由 PDEC/ColumnCRT 排斥。
```

下一步最小硬点是建立跨窗口同形状尖峰的持久性审计；若没有持久性，则把局部尖峰全部转成
有限 SAE 证书。
