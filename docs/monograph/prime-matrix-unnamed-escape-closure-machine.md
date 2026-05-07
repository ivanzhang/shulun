# 行命题无名逃逸闭合机：非固定常数的递归剥离链

**状态：** `unnamed_escape_closure_machine_proved_named_exits_open`

本文把最近 SN-1 到 SN3-E 的推进合并成一个统一结论：

```text
最小早期零行反例不能无限保持无名；
每一步要么给容量矛盾，
要么降低未解释质量，
要么固定 PDEC/ColumnCRT/SAE/Bohr-cap/KLS 命名出口，
要么下降到更小素数层。
```

这不是固定常数路线，也不是统计逼近路线。

## 1. 起点：自归一化正带责任

若第 `x=y-1<P` 行为零行，则 SN-1 给出：

```text
A_{>BY} >= C_allow(P,y) M_{>BY}。
```

等价为远尾正超额必须支付行内真实余量：

```text
E_tail >= R(P,y)。
```

并且

```text
R-E_tail=|S_Y|-T_Y。
```

所以这是原始斜线容量余量，不是人为常数。

## 2. 带级正部

SN-2 给出确定性判据：

```text
若 sum_J E_J^+ < R(P,y)，则零行不可能。
```

若失败，则正二进带必须承担责任。

## 3. SN3 投影剥离

对正带执行低维投影：

```text
q 短窗；
q mod W；
d=Py-qm mod W。
```

结果：

```text
短窗峰       => SAE；
qmod 峰      => PDEC；
dmod 峰      => ColumnCRT；
低维峰全小   => TrueDistributedDLS。
```

SN3-A 进一步证明：

```text
E_beta* >= theta E_J
=> unresolved <= (1-theta)E_J。
```

因此低模峰不能作为无名质量保留。

## 4. 多带与高频

SN3-C 对同行多真分散带给出：

```text
q 壳重叠       => SAE；
低模签名同步   => PDEC/ColumnCRT；
q 壳分离且低模不同步 => KLS-Multishell。
```

SN3-D 对 `KLS-Multishell` 给出：

```text
HighFrequencyColumn/PDEC
或 L2Flat CleanMultishellKLS。
```

SN3-E 对高频列相位给出 Jordan-Bohr 局部化：

```text
HighFrequencyColumn
=> 持久 Bohr-cap/PDEC/ColumnCRT
   或孤立 Bohr-cap/SAE
   或 L2-flat CleanKLS。
```

## 5. 单调势函数

定义势函数：

```text
Phi=(
  P,
  active_shell_count,
  q_window_length,
  -lowmod_rank,
  -frequency_rank,
  unresolved_mass,
  descent_depth
)。
```

按字典序和出口优先级理解：

```text
CapacityGate:
  若 T_Y<S_Y，直接给素数洞；

BandPositive:
  若正带和不足，直接给素数洞；

ShortWindow:
  q 窗严格缩短；不能无限，终为 SAE；

LowModPromotion:
  lowmod_rank 增加；若持久，PDEC/ColumnCRT；

FrequencyPromotion:
  frequency_rank 增加；若持久，Bohr-cap/PDEC/ColumnCRT；

SN3-A Peeling:
  unresolved_mass 至少按 (1-theta) 下降；

ShellSplit:
  active_shell_count 降低或进入 KLS-Multishell；

CleanKLS:
  若成立，unresolved_mass 降到不足以支付 R；
  若失败，失败给高频/短窗/系数集中命名出口；

TotalDescent:
  P 严格下降，最终到 p=2 或首阻断 seam/PDEC/ColumnCRT。
```

因此无名循环不可能。

## 6. 形式化结论

**无名逃逸闭合定理。** 假设存在最小早期零行反例。则该反例不能在容量、远尾、分散带、高频多壳或列相位层级中无限保持无名。它必然在有限步内进入以下之一：

```text
1. 容量矛盾，产生素数洞；
2. SAE/endpoint 证书；
3. PDEC 证书；
4. ColumnCRT 证书；
5. Bohr-cap 高频证书；
6. CleanMultishellKLS 输入；
7. TotalDescent 到更小素数层，或首阻断 seam/PDEC/ColumnCRT。
```

这就是当前真正已经闭合的部分：**无名逃逸闭合**。

## 7. 尚未宣称的部分

要把行命题升级为最终无条件证明，还必须继续完成：

```text
排斥全部 SAE/PDEC/ColumnCRT/Bohr-cap 命名出口；
证明 CleanMultishellKLS；
或证明无上述缺陷时 TotalDescent 必下降到底。
```

因此本文不把行命题标为最终无条件闭合；它把全局剩余压缩为有限命名出口与一个 clean KLS 输入，避免继续出现无名分支。

## 8. 命名出口吸收合同

新增 `prime-matrix-named-exit-absorption-contract.md` 后，上述有限命名出口进一步统一为同一个
吸收算子：

```text
Abs(SAE)           = SAE-Cert；
Abs(PDEC)          = PDEC-Cert；
Abs(ColumnCRT)     = ColumnCRT-Cert or PDEC/SAE；
Abs(BohrCap)       = PDEC/ColumnCRT/SAE or CleanKLS；
Abs(CofactorAnchor)= TailAnchor-Cert or PDEC/ColumnCRT/SAE；
Abs(TotalDescent)  = p=2 contradiction or EndpointSeam；
Abs(EndpointSeam)  = PDEC/ColumnCRT/SAE。
```

因此无名逃逸闭合机的最终输出可改写为：

```text
最小早期零行反例
=> 素数洞
   or SAE-Cert
   or PDEC-Cert
   or ColumnCRT-Cert
   or CleanMultishellKLS
   or p=2 下降矛盾。
```

`Bohr-cap`、`EndpointSeam` 与 `CofactorAnchor` 不再作为独立自由出口保留；它们必须继续吸收到
已有 `SAE/PDEC/ColumnCRT/CleanKLS/TotalDescent` 接口。当前新增闭合的是“出口吸收口径”，不是
`SAE/PDEC/ColumnCRT` 的最终排斥。
