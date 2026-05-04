# AlphaTail 尾素对端点尖峰到 Directed Endpoint CRTDefect

**状态：** `alpha_tail_tailpair_endpoint_crtdefect_bridge_open`

本文把 `TailPair endpoint absorption` 的 `EndpointSpike` 接到已有
`Directed Endpoint CRTDefect` 出口。结论仍是桥接，不是排斥：端点尖峰若持久出现，
就变成有向端点 CRT 缺陷；若不持久，则进入 SAE。

## 1. 端点尖峰相位键

一个端点尖峰责任证书包含

\[
(g,j_1,j_2,u,J,D,A_g(J),B_g(J),C_{\rm loc}).
\tag{TEC-1}
\]

其中

\[
d=qu-j_1r,\qquad D=[uJ^- - j_1r,\ uJ^+ - j_1r]\subset I_m.
\tag{TEC-2}
\]

设 `side in {L,R,B}` 表示 `D` 贴左端、贴右端或同时贴两端。定义端点相位键

\[
\mathcal K=(g,j_1,j_2,u,\operatorname{side}).
\tag{TEC-3}
\]

同一 `K` 在多个窗口中持续超标，说明相同几何端点方向反复产生短差值素对过密。

## 2. 持久端点缺陷

令 `W` 是一族窗口。对相位键 `K` 定义超额

\[
\mathcal E_K(W)
=
\sum_{w\in W:\mathcal K(w)=K}
\left(A_g(J_w)-C_{\rm local}B_g(J_w)\right)_+.
\tag{TEC-4}
\]

若

\[
\mathcal E_K(W)\ge \Lambda_K
\tag{TEC-5}
\]

则称出现 `TailPairEndpointDefect(K)`。

该缺陷是端点方向的局部 sawtooth/截断偏差：同一线性端点映射 `d=qu-j_1r`
在同一 gap 和同一点位形状下反复超出平滑素对模型。

## 3. 到 Directed Endpoint CRTDefect 的桥

若 `TailPairEndpointDefect(K)` 持久出现，则有两种情况：

1. **有限孤立。**  
   超额只来自有限少数窗口，进入 `SAE`。
2. **相位持久。**  
   同一 `K` 在许多窗口中持续出现。由于 `D` 贴住 `I_m` 端点，窗口端点的单位旋转相位
   持续偏向同一短差值素对结构；这正是 `Directed Endpoint CRTDefect` 的输入对象。

因此有桥接：

```text
persistent TailPairEndpointDefect
=> Directed Endpoint CRTDefect / PDEC；
non-persistent
=> SAE.
```

该桥与 `prime-matrix-directed-endpoint-crtdefect-bridge.md` 的 DEC 定义兼容：端点尖峰给出
一个显式端点块投影，持久超额通过鸽巢落入某个非零端点相位块。

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_crtdefect_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_crtdefect_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --format table
```

脚本输出端点尖峰按相位键聚合后的超额、左右端点分布和最大责任键。

## 5. 审稿边界

已证明：

```text
EndpointSpike 可聚合成显式端点相位键 K；
同一 K 持久超额 => Directed Endpoint CRTDefect/PDEC；
非持久超额 => SAE。
```

尚未证明：

```text
Directed Endpoint CRTDefect/PDEC 全部排斥；
或所有 TailPairEndpointDefect 只孤立出现并由 SAE 吸收。
```

下一步最小硬点是把端点相位键 `K` 接入统一 PDEC 上界证书，或生成有限 SAE 账本。
