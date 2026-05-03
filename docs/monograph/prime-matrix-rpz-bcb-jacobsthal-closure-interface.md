# RPZ-BCB Jacobsthal 型闭合接口

**状态：** `rpz_bcb_jacobsthal_closure_interface`

本文承接 `prime-matrix-rpz-bcb-core-run-obstruction.md`。当前 finite BCB 样本已经显示：
no-TailAnchor 分支要求的低筛零核心长度超过了对应 `h` 层低筛最大连续覆盖长度。现在把这一步
写成全局闭合所需的精确定理接口。

## 1. 低筛连续覆盖函数

令

```text
P(h)=prod_{ell<=h, ell prime} ell。
```

定义

```text
G(h)=max{ N : 存在连续整数区间 I, |I|=N, 且每个 n in I 都被某个 ell<=h 整除 }。
```

等价地，`G(h)+1` 是模 `P(h)` 周期中相邻 `h`-rough residue 之间的最大循环间距。

## 2. BCB-Core 长度判据

对顶层素数 `P`、平台长度 `m=|S|`、阈值 `T`，BCB 强制核心长度为

```text
N_BCB=P+m-1-2T。
```

因此有严格二分：

```text
no TailAnchor + N_BCB>G(h)  =>  矛盾；
no TailAnchor + N_BCB<=G(h) =>  必须继续 endpoint / first-failure / PDEC / ColumnCRT。
```

## 3. 证明

在 no-TailAnchor 分支中，`BCB-Core` 已证明核心区间 `J_T` 是 `h`-筛零区间，即

```text
对每个 n in J_T，存在 ell<=h 使 ell|n。
```

这正是 `G(h)` 定义中的连续低筛覆盖区间。因此若 `|J_T|=N_BCB>G(h)`，则 `J_T` 的存在
与 `G(h)` 的最大性矛盾。证毕。

该证明没有使用 accepted selector、端点相位或下层递归下降；它是更上游的容量障碍。

## 4. 当前有限闭合

`prime-matrix-rpz-bcb-core-run-obstruction.md` 给出当前层精确值：

| h | G(h) |
|---:|---:|
| 5 | 5 |
| 7 | 9 |
| 11 | 13 |
| 13 | 21 |

当前 BCB 样本的 `N_BCB` 为：

| top P | h | N_BCB | G(h) | margin |
|---:|---:|---:|---:|---:|
| 13 | 5 | 9 | 5 | 4 |
| 17 | 7 | 13 | 9 | 4 |
| 19 | 7 | 15 | 9 | 6 |
| 23 | 11 | 19 | 13 | 6 |
| 29 | 13 | 25 | 21 | 4 |

所以当前 finite BCB no-TailAnchor 分支已闭合：若无 TailAnchor，则核心长度超出 `G(h)`；若有
TailAnchor，则回到已命名 TailAnchor 出口。

## 5. 全局剩余义务

要把该分支升级为全局无条件闭合，必须对正式 BCB 抽取中出现的每个 `(P,h,m,T)` 证明：

```text
G(h) < P+m-1-2T。
```

这就是当前最小全局硬点。它不能由当前有限样本或相位枚举自动推出。

若该不等式在某些 formal 层无法证明，则这些层不能宣称已闭合；必须保留以下出口：

```text
TailAnchor；
BCB endpoint / no-candidate；
first-failure seam；
PDEC / ColumnCRT。
```

## 6. 审稿边界

本文完成：

```text
no-TailAnchor BCB core closure <= G(h)<N_BCB。
current finite BCB samples satisfy G(h)<N_BCB。
```

本文没有完成：

```text
formal 全层 Jacobsthal 型上界 G(h)<P+m-1-2T。
TailAnchor / endpoint / first-failure 出口的最终全局排斥。
```

因此，下一步真正可攻目标不是继续放大 accepted-preimage 枚举，而是直接证明或引用
`G(h)<P+m-1-2T` 的全局上界，并检查它在 formal BCB 参数范围内是否有正余量。
