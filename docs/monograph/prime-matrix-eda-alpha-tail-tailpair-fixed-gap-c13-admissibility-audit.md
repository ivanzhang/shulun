# AlphaTail 固定 gap `C_local=1.3` 可采纳性审查

**状态：** `fixed_gap_c13_admissibility_open`

本文直接审查上一层得到的硬输入：

\[
N_g(J)\le 1.3\,\mathfrak S_g{|J|\over \log^2 J_-}.
\tag{C13-1}
\]

这里 `N_g(J)=#{q in J:q,q+g prime}`，`\mathfrak S_g` 为本文已归一化的固定差值局部因子。
目标是防止把样本链条中的 `C_local=1.3` 误写成无条件全局定理。

## 1. 当前链条真正需要的输入

由 `local constant chain reaudit` 可知，当前样本在 `C_local=1.3` 下全链清空。形式上，行命题链条只需要以下二分之一：

```text
FGC-13:
  目标窗口族内所有固定 gap 短区间均满足 (C13-1)；

FGC-13-SAE:
  不满足 (C13-1) 的窗口全部进入有限/可求和 SAE，
  或进入 persistent PDEC/ColumnCRT 后被排斥。
```

**引理 C13-1（可采纳二分）。**  
若 `FGC-13` 成立，则 `TailPairLocalSpike` 全局为空。若 `FGC-13-SAE` 成立，则
`TailPairLocalSpike` 不会形成未命名的持续反例出口。因此二者任一成立，都足以关闭
本层固定 gap 局部常数分支。

**证明。**  
`TailPairLocalSpike` 的定义正是存在 `(g,J)` 违反 `(C13-1)`。若 `FGC-13` 成立，违反集合为空。
若只满足 `FGC-13-SAE`，每个违反窗口都已有有限 SAE 或 persistent PDEC/ColumnCRT 排斥证书，
因此也不会留下未闭合出口。□

## 2. 不能使用的过强说法

无条件地对所有固定 gap 区间断言 `(C13-1)` 是错误的。取

\[
g=2,\qquad J=\{5\}.
\]

则 `5` 与 `7` 均为素数，所以 `N_2(J)=1`。而本文归一化下 `\mathfrak S_2=1`，且

\[
{1\over \log^2 5}<0.387.
\]

于是

\[
{N_2(J)\over \mathfrak S_2|J|/\log^2J_-}>2.58>1.3.
\tag{C13-2}
\]

所以 `C_local=1.3` 若要成为正式输入，必须带有目标窗口族条件、尺度下界、有限例外表，
或 SAE/PDEC 出口；不能写成“所有固定 gap 短区间”的点态上界。

## 3. 样本给出的真实余量

当前审计样本的最大局部需求为：

```text
p=997,m=5      max_local_C=1.292474；
p=5003,m=5     max_local_C=1.251074；
p=10007,m=5    max_local_C=1.262503。
```

最紧项的 Brun/Selberg 标准量约为：

```text
actual=65, scale=50.291, required_C=1.292474。
```

这说明样本中的 `1.3` 不是随意常数，而是非常贴近最坏局部尖峰的验收线。审稿上必须给
`0.007526` 量级的外向余量来源，不能靠粗常数包覆盖。

## 4. 下一步最小硬点

当前最小硬点应写成：

```text
FGC-13-admissible:
  对所有目标窗口族中的固定 gap 区间，
  要么证明 N_g(J)<=1.3*S_g*|J|/log^2 J_-，
  要么输出可求和 SAE/PDEC 证书。
```

可行攻坚顺序：

1. 先证明目标窗口族的尺度下界，排除单点或极短区间反例。
2. 对大尺度窗口建立局部 Selberg/Brun 上筛常数，常数必须低于 `1.3`。
3. 对仍超标的窗口证明端点贴边、相位持久或孤立性，分别进入 `Endpoint/PDEC/SAE`。
4. 若第 2 步只能给出 `C>1.3`，则不能关闭本层，只能回到端点证书链。

## 5. 审稿边界

已完成：

```text
明确 `C_local=1.3` 的可采纳形式；
证明无条件全区间点态 `C_local=1.3` 表述为假；
把剩余任务压缩为目标窗口族的 admissible 常数包或 SAE/PDEC 证书。
```

仍未完成：

```text
目标窗口族尺度下界的全局证明；
目标窗口族上的 `1.3` 局部 Selberg/Brun 常数；
全部超 `1.3` 窗口的有限/可求和 SAE/PDEC 证书。
```

因此 `C_local=1.3` 目前是样本闭合常数与正式攻坚目标，不是行命题无条件闭合输入。

