# RPZ 双轨攻坚闭合路线

**状态：** `rpz_dual_track_routes_to_named_exits_or_p2_descent`

本文承接 `prime-matrix-rpz-bcb-endpoint-persistence-route.md`。当前 RPZ 主链已经把单窗分散、
滑动平台、边界压缩、网格端点失败逐层压缩。现在同步推进两个目标：

```text
Track A：SAE/PDEC/ColumnCRT 证书闭合；
Track B：下层 h-筛零行递归下降。
```

二者不是重复路线。Track A 处理所有端点/持久相位出口；Track B 处理 BCB-Core 已经给出的
完整下层零行。

## 1. Track A：出口证书接口

端点失败相位

\[
\tau=(h,\ N\bmod h,\ u\bmod h,\ \Delta)
\]

已经由 `prime-matrix-rpz-bcb-endpoint-persistence-route.md` 路由为：

| 分支 | 输入 | 验收义务 |
|---|---|---|
| `SAE` | 每个端点相位负载 `<=B_SAE` | 给出有限孤立窗口证书，或证明 survivor/lift/higher-defect |
| `PDEC` | 某端点相位负载 `>B_SAE` 且跨平台持久 | 接入 `h4-pdec-certificate-template.md`，证明同一坏窗集合的 `U_CRT<L_PDEC` |
| `ColumnCRT` | 持久端点相位同时携带列位移/标签余类 | 接入 `h4-pdec-column-defect-routing-contract.md`，给出非零位移余类负载证书 |

因此 Track A 的下一步不是再定义端点失败，而是物化三类证书：

```text
RPZ-SAE finite package；
RPZ-PDEC endpoint phase row；
RPZ-ColumnCRT endpoint displacement row。
```

## 2. Track B：下层零行递归下降定理

设 `p>2`，`r` 是 `p` 的前一素数。若 `p` 对齐行

\[
I=[(a-1)p+1,\ ap]
\]

是 `p`-筛零行，则剥到 `r` 层后，`r`-筛幸存者只能来自端点

\[
ap=p\cdot a,
\]

且该端点实际复活当且仅当 `(a,P(r))=1`。

**Lemma RPZ-LowerDescent（下层零行下降）。**
在上述条件下，若 `I` 完整包含一条 `r` 对齐行 `J`，且 `J` 不含端点穿孔 `ap`，
则 `J` 是 `r`-筛零行。

**证明。**
若 `n∈J` 是 `r`-筛幸存者，则因为 `I` 是 `p`-筛零行，`n` 必须被某个素数 `ell`、
`r<ell<=p` 整除。由于 `r,p` 相邻，唯一可能是 `ell=p`。而 `I` 的长度为 `p`，其中
`p` 的倍数只有端点 `ap`。若 `J` 不含该端点，则这样的 `n` 不存在。证毕。

当递归到 `p=2` 时，任意 `2` 对齐行 `[2m-1,2m]` 且 `m>1` 都含奇数 `2m-1`，不可能是
`2`-筛零行。因此若下降路径到达 `p=2`，反例分支直接矛盾。

## 3. 有限下降审计

新增审计：

```text
experiments/prime_matrix_rpz_lower_zero_descent_audit.py；
docs/monograph/prime-matrix-rpz-lower-zero-descent-audit.json；
docs/monograph/prime-matrix-rpz-lower-zero-descent-audit.md。
```

审计输入为 `prime-matrix-rpz-bcb-core-audit.json` 中的
`would_be_zero_rows_after_tail_deletion`。结果：

| 指标 | 数值 |
|---|---:|
| 起始条件下层零行数 | `6` |
| 到达 `p=2` 直接矛盾的起始支数 | `6` |
| 被端点穿孔或网格缺口阻断的节点数 | `0` |
| 含端点穿孔的节点数 | `7` |
| 最大下降深度 | `5` |

这说明样本中 Track B 不需要调用出口证书：每条 BCB 下层零行都可递归下降到 `p=2`。

## 4. 双轨合成

当前 RPZ 链条可写成：

```text
RPZ absorption
=> TailAnchor/ColumnCRT/ColumnRadius/PDEC/SAE named exits
   or BCB lower h-zero-row
=> recursive lower descent
=> p=2 contradiction
   or descent endpoint/grid obstruction
=> SAE/PDEC/ColumnCRT named exits。
```

因此下一硬点不再是“找新出口”，而是两个明确义务：

1. 证明正式反例平台满足下层下降网格条件直到 `p=2`，或每个阻断都进入端点相位账本；
2. 对所有进入账本的 `SAE/PDEC/ColumnCRT` 分支提交证书。

## 5. 审稿边界

本文完成：

```text
Track A 的证书接口表；
Track B 的下层零行下降引理；
样本级下降到 p=2 的可复现审计。
```

本文没有完成：

```text
全局下降网格条件；
SAE/PDEC/ColumnCRT 证书排斥；
最终 Prime Matrix 行命题无条件闭合。
```

下一步最小硬点更新为：

```text
LowerDescent-Grid persistence
and RPZ-SAE/PDEC/ColumnCRT certificate materialization。
```
