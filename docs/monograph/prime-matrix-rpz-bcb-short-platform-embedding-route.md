# RPZ-BCB 短平台 Jacobsthal 嵌入路由

**状态：** `rpz_bcb_short_platform_jacobsthal_embedding_route`

本文承接 `prime-matrix-rpz-bcb-platform-length-threshold.md`。平台长度阈值账本说明：

```text
no-TailAnchor BCB 直接闭合  <=  m >= G(h)-P+2+2T。
```

若平台长度达不到该阈值，不能直接用低筛连续覆盖长度矛盾闭合。但该分支也不是新的无限自由度：
no-TailAnchor 已强制 `J_T` 是 `h`-筛零区间，所以 `J_T` 必须嵌入某个 `h` 层 Jacobsthal 覆盖块。

## 1. 短平台缺口

令

```text
N=P+m-1-2T,
D=G(h)-N。
```

短平台分支就是

```text
D>=0。
```

此时若 no-TailAnchor 成立，则 `J_T` 是长度为 `N` 的 `h`-筛零区间。

## 2. Jacobsthal 嵌入引理

**Lemma BCB-JEmbed（短平台嵌入）。**
设 `B` 是模 `P(h)` 上所有极大 `h`-筛覆盖块的集合。若 `J_T` 是长度 `N` 的 `h`-筛零区间且
`N<=G(h)`，则

```text
left(J_T) mod P(h)
```

属于有限集合

```text
E_{h,N}={a+t mod P(h): [a,a+L-1] in B, 0<=t<=L-N}。
```

特别地，若只用最大长度 `G(h)` 的覆盖块，则相位候选数至多

```text
#max_blocks(h) * (G(h)-N+1)。
```

**证明。**
`J_T` 中每个整数均被某个 `<=h` 的素数整除，所以它在模 `P(h)` 的周期中落入一个连续覆盖段。
将该覆盖段向左右极大延伸，得到某个极大覆盖块 `[a,a+L-1]`，且 `L>=N`。因此 `J_T` 左端必为
`a+t`，其中 `0<=t<=L-N`。证毕。

## 3. 接入 PDEC/ColumnCRT

短平台分支现在有无损路由：

```text
short platform + no TailAnchor
=> left(J_T) mod P(h) in E_{h,N}
=> finite endpoint phase family。
```

若该有限相位只出现有限次或低负载，则进入 `SAE`；若在 formal 反例族中持续复现，则进入
`PDEC/ColumnCRT`。因此短平台失败不是第三出口，而是一个 Jacobsthal 端点相位出口。

## 4. 当前与下一义务

当前已完成：

```text
平台达标 => no-TailAnchor BCB 长度矛盾；
平台不达标 => Jacobsthal embedding finite phase。
最长块端点 => Emax_{h,N} 可由 CRT 证书材料化。
```

仍未完成：

```text
完整 E_{h,N} 的全局显式证书；
证明所有长度 >=N 的覆盖块可归入最长块相位族，或枚举完整覆盖块族；
短平台相位进入 PDEC/ColumnCRT 后的最终排斥；
TailAnchor 出口的最终排斥。
```

新增证书：

```text
experiments/prime_matrix_rpz_bcb_short_platform_embedding_certificate.py；
docs/monograph/prime-matrix-rpz-bcb-short-platform-embedding-certificate.json；
docs/monograph/prime-matrix-rpz-bcb-short-platform-embedding-certificate.md。
```

该证书把 Ziller--Morack 附属表中的最长 Jacobsthal 覆盖块模表示转成 CRT 左端相位，并验证每个
重建块的覆盖性与两侧边界非覆盖。当前 `m=5,T=4` 参数下，首个 `h>=5` 短平台为
`h=43,P=89,N=85,D=4`，最长块端点族含 `240` 个唯一相位；全表共验证 `1197` 个最长块，失败数为
`0`。

## 5. 审稿边界

本文不宣称 Prime Matrix 行命题已闭合。它把失败路线从“平台长度不足”压缩为可审查的有限相位
接口。最长块端点证书只覆盖 `Emax_{h,N}`，不是完整 `E_{h,N}`。下一步若要继续推进全局闭合，
应证明完整覆盖块族可归约到该证书，或生成完整 `E_{h,N}` 证书，并把每个持续相位接入既有
PDEC/ColumnCRT 材料化接口。
