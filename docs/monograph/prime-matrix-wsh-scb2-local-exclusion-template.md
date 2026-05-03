# WSH-Hall SCB-2 局部排斥模板

**状态：** `scb2_routing_closed_modulo_endpoint_pdec`

本文把 `SCB-2` 从“待证明的短块排斥”改写成可逐行审查的局部路由定理。结论不是全局
`WSH-Hall` 证明；它闭合的是短块分支的路由：

```text
|B|<=3 且 Hall 失败
=> Endpoint/PDEC deficit，
并在双点/三点紧块中常伴随 Tail-repeat 或 Fixed-offset-full-load。
```

## 1. 定义

固定相邻素数层 `p<q`，行宽为 `q`，取

\[
  R=\lceil 3\log^2 q\rceil,\qquad y=\lfloor p/e\rfloor。
\]

在一行 `I_h` 中令：

```text
B_h = {balanced two-tail semiprimes b=ell_1 ell_2 : y<ell_i<=p},
P_h = {no-tail survivors below q^2}。
```

对连续短块 `B subset B_h` 定义：

\[
  N_R(B)=P_h\cap\bigcup_{b\in B}[b-R,b+R],
  \qquad
  \mathcal M_R(B)=|N_R(B)|-|B|。
\]

定义三个出口：

1. **Endpoint/PDEC deficit**
   \[
     \mathcal M_R(B)<0。
   \]
   经 `n -> q^2-n`，该亏损转写为早期非零类端点亏损块。

2. **Tail-repeat**
   \[
     \max_{\ell\in(y,p]}\#\{b\in B:\ell\mid b\}\ge2。
   \]

3. **Fixed-offset-full-load**
   存在非零偏移 `d`，使得 `d` 同时属于所有 `b in B` 的小轮允许偏移集合：
   \[
     d\not\equiv -b\pmod r,\qquad r\le z。
   \]

## 2. SCB-2 局部路由定理

**命题 SCB2-Routing.**
令 `B` 为 `|B|<=3` 的连续短块。若 `\mathcal M_R(B)<0`，则 `B`
触发 `Endpoint/PDEC deficit`。若 `|B|>=2` 且该短块是紧块，则还应检查
`Tail-repeat` 与 `Fixed-offset-full-load` 两个增强出口。

**证明。**
`Endpoint/PDEC deficit` 的定义正是 `\mathcal M_R(B)<0`。因此任意短块 Hall 失败
已经被命名出口吸收。对 `|B|>=2`，若两个或三个半素数共享尾因子，则触发 `Tail-repeat`。
若存在同一短偏移通道同时可服务所有半素数，则触发 `Fixed-offset-full-load`；其容量由

\[
  \rho_z(d)=\prod_{\substack{r\le z\\r\nmid d}}{r-2\over r-1}
\]

控制。否则剩余失败只能是端点素数真实亏损，经 `q^2-n` 镜像进入 `Endpoint/PDEC`。
证毕。

这一定理是路由闭合，不是出口排除。要得到 `WSH-Hall`，还必须排除 Endpoint/PDEC deficit，
或证明其持久化后与 CRT 相位容量矛盾。

## 3. 有限局部证书

新增脚本：

```text
experiments/prime_matrix_wsh_scb2_local_certificate.py
```

输出：

```text
docs/monograph/prime-matrix-wsh-scb2-local-certificate.md
docs/monograph/prime-matrix-wsh-scb2-local-certificate.json
```

默认参数：

```text
17<=p<=2000
R=ceil(3 log^2 q)
|B|<=3
wheel primes = 2,3,5,7,11,13
```

结果：

```text
size 1 blocks = 1496400, min surplus = 1
size 2 blocks = 1281326, min surplus = 1
size 3 blocks = 1088870, min surplus = 2
negative blocks = 0
zero blocks = 0
tight blocks = 45
```

小余量块的压力标签：

```text
Endpoint-margin: 45
Fixed-offset-full-load: 17
Tail-repeat: 3
```

该证书说明在有限范围内短块不仅没有失败，而且全为正余量。双点与三点紧块中，
`Fixed-offset-full-load` 明显出现，低层紧块还出现 `Tail-repeat`。

## 4. 对全局主链的影响

本文件把 `SCB-2` 从开放形态降为：

```text
SCB-2 closed as a routing lemma modulo Endpoint/PDEC exclusion.
```

因此 `WSH Positive Expansion or Named Defect` 的剩余硬点主要变为：

```text
SCB-1: |B|>=4 的长块正扩张或命名缺陷；
Endpoint/PDEC: 短块端点亏损出口的全局排斥。
```

下一步若继续攻最小硬点，优先顺序应为：

1. 对 `SCB-1` 建立长块自动扩张的组合下界；
2. 对短块 Endpoint/PDEC deficit 建立 `q^2-n` 镜像端点证书；
3. 把固定偏移满载接入 PDEC 相位容量上界。
