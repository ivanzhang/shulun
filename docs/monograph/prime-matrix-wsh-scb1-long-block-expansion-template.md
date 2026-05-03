# WSH-Hall SCB-1 长块扩张模板

**状态：** `finite_scb1_certificate_and_global_proof_target`

本文把 `SCB-1` 从“长块自动扩张”改写为可审稿的有限证书加全局证明目标。结论不是全局
`WSH-Hall` 证明；当前闭合的是证书格式、长块压力字段和下一步出口。

```text
|B|>=4 的连续平衡双尾半素数长块
=> 有限范围内 Hall 余量 >=3；
全局证明仍需：
   positive long-block expansion
   or fixed-offset/PDEC / Tail-anchor / Endpoint absorption.
```

## 1. 定义

固定相邻素数层 `p<q`，行宽为 `q`，取

\[
  R=\lceil 3\log^2 q\rceil,\qquad y=\lfloor p/e\rfloor。
\]

在一行 `I_h` 中令：

```text
B_h = {balanced two-tail semiprimes b=ell_1 ell_2 : y<ell_i<=p},
P_h = {no-tail survivors below q^2}.
```

对连续长块 `B subset B_h`，`|B|>=4`，定义

\[
  N_R(B)=P_h\cap\bigcup_{b\in B}[b-R,b+R],
  \qquad
  \mathcal M_R(B)=|N_R(B)|-|B|。
\]

## 2. SCB-1 长块目标

**命题目标 SCB1-Long.**
若 `B` 是 `|B|>=4` 的连续长块，则至少一项成立：

```text
(1) M_R(B)>=3；
(2) Tail-anchor / Tail-repeat 出口触发；
(3) Fixed-offset-full-load 或 Fixed-offset-heavy-load 进入 fixed-offset/PDEC；
(4) q^2-n 端点镜像给出 Endpoint/PDEC deficit。
```

该命题一旦证明，将与 `SCB-2` 的短块路由合并为
`WSH Positive Expansion or Named Defect`。当前文件只给出证书支持和证明接口，尚不证明
`SCB1-Long` 的全局形式。

## 3. 有限长块证书

新增脚本：

```text
experiments/prime_matrix_wsh_scb1_long_block_certificate.py
```

输出：

```text
docs/monograph/prime-matrix-wsh-scb1-long-block-certificate.md
docs/monograph/prime-matrix-wsh-scb1-long-block-certificate.json
```

默认参数：

```text
17<=p<=2000
R=ceil(3 log^2 q)
|B|>=4
wheel primes = 2,3,5,7,11,13
```

结果：

```text
prime records = 297
rows with balanced semiprimes = 215074
long blocks = 4573823
global minimum long-block surplus = 3
negative long blocks = 0
zero long blocks = 0
tight long blocks = 4
```

最紧签名：

| surplus | semiprime count | block count |
| ---: | ---: | ---: |
| 3 | 4 | 3 |
| 3 | 5 | 1 |

全部最紧长块同时触发：

```text
Endpoint-margin
Fixed-offset-full-load
```

这说明在审计范围内，长块不是危险随机缺口；最紧情形集中到固定偏移通道满载，并同时贴近
端点镜像亏损出口。

## 4. 证明链中的精确作用

`SCB-1` 与 `SCB-2` 的合成状态应写为：

```text
SCB-2 routing closed modulo Endpoint/PDEC exclusion.
SCB-1 has finite long-block certificate with min surplus 3.
Global closure still requires long-block expansion or fixed-offset/PDEC absorption.
```

因此当前主链压缩为：

```text
RCI/PDEC
=> Distributed-RCI
=> WSH-Hall/PDEC
=> WSH Positive Expansion or Named Defect
=> SCB-1 + SCB-2 + Endpoint/PDEC exclusion.
```

其中 `SCB-2` 已是路由闭合；`SCB-1` 的下一步不是继续扩大有限枚举，而是证明：

```text
若长块 Hall 余量低于 3，则固定偏移满载、尾锚重复或端点镜像亏损必然触发。
```

## 5. 下一步最小硬点

当前最小硬点为：

```text
Fixed-offset/PDEC absorption for long tight blocks.
```

需要补的逐行内容是：

1. 把固定偏移允许集合
   \[
     d\not\equiv -b\pmod r,\quad r\le z
   \]
   转为同一 `d` 上的容量上界；
2. 证明长块中 `max_allowed_offset_load >= |B|` 时，坏窗指示函数在低模相位上产生
   persistent CRT defect；
3. 若该缺陷不持久，则把对应块送入 `SAE` 或 `Endpoint/PDEC` 稀疏出口；
4. 与 `SCB-2` 的端点亏损出口统一，形成单一 `Endpoint/PDEC exclusion` 待排斥接口。

这一步完成后，`WSH-Hall/PDEC` 的剩余将只剩最终 `Endpoint/PDEC` 排斥，而不是长短块内部路由。
