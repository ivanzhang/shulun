# AlphaTail `C13` 高 `P` 局部闭合链合同

**状态：** `c13_local_chain_sample_closed_target_family_open`

本文把近期三个窄接口合成为一条不依赖 Gate 总池交换的局部闭合链：

```text
Target syntax
RatioStructuralVoid
MidStructuralVoid
EdgeStructuralPayment
SlackFloor
=> FormalLocalPayment
=> HighP local C13 closure.
```

该链条的意义是：当前样本不再需要逐窗口 `LocalGatePool`，也不再需要边缘层低素精确分布。
付款可由纯局部的 `Formal` 路线完成。

## 1. 链条

### 1.1 结构空性

若目标窗口满足

```text
B/p<1.8；
|r|/p<0.225；
6 divides |r|，
```

则由 `L>alpha p` 推出 `B<2L` 与 `(m-1)|r|<L`，进而由
`lift>=2` 结构判据得到

\[
D_{\ge2}=0.
\tag{LCC-1}
\]

### 1.2 中间层空性

同一比例条件还推出

\[
2B+(m-1)|r|<5L.
\tag{LCC-2}
\]

因此真实低素中间候选先被压到 `(u,h)=(2,1)` 或 `(3,1)`；再由 `6|r`
分别在模 `2` 与模 `3` 下排除，得到中间同余无解：

\[
N_{\rm mid}=0.
\tag{LCC-3}
\]

### 1.3 边缘层付款

边缘结构上界把 `G_edge` 压成固定公式。剩余只需逐窗口满足

\[
K\sum_{m\in M}\left(
\sum_{j_1=1}^{m-1}j_1^2+2\binom m3
\right)\le S,
\tag{LCC-4}
\]

则由边缘门结构上界与 `U_edge<=K G_edge` 得

\[
U_{\rm edge}\le S.
\tag{LCC-5}
\]

结合 `(LCC-1)`、`(LCC-3)`、`(LCC-5)`，

\[
D_{\rm formal}=U_{\rm edge}+N_{\rm mid}+D_{\ge2}\le S.
\tag{LCC-6}
\]

所以逐窗口 `FormalLocalPayment` 成立。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_local_chain_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_local_chain_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 3. 当前样本结果

```text
syntax=True；
ratio_struct=True；
mid_struct=True；
edge_struct=True；
local_chain=True；
mid_margin=6007；
formal_margin=411.727367；
edge_struct_margin=106.727367；
slack_floor=True；
res_floor=True；
res_margin=101.727367；
active_template=True；
source_forward=True；
source_exact=True；
small_slack_cert=True；
full_postlow_chain=True；
target_rule_closed=False。
```

新增后段余量：

```text
active_template_margin=66.727367；
source_exact_margin=66.727367；
small_slack_windows=1；
small_slack_source_margin=8.340921。
```

进一步的 `SlackFloor` 审计显示，当前样本满足更强的
`ResonanceFloor`，最紧窗口正余量为 `101.727367`。
再由 `LowDeletionAllowance` 等价改写，最紧窗口 `p=5003` 的实际低筛删除量为
`5`，允许删除量为 `106.727367`。
新增 `APSingletonReduction` 后，当前样本还满足
`D_low=active_AP_classes` 且 `max_AP_pairs_per_class=1`。
进一步的 `APSingletonStructural` 审计显示，所有活跃 AP 类均满足
`u in {2,3}` 与 `q<2ell`，所以单点化由结构条件推出。
新增 `ActiveClassTemplateBound` 后，活跃类付款进一步被压成模板骨架付款：
当前样本总 `skeleton=28`，`K*skeleton=224`，允许删除量 `1385.963717`；
最紧窗口 `p=5003` 仍有模板余量 `66.727367`。
新增 `SourceSlotStructural` 后，所有当前活跃骨架均满足前向源槽恒等式
`q=ell+(j-j1)|r|/u` 与 `q+g=ell+(j-j2)|r|/u`。粗槽上界已经自动覆盖
`p=10007`，仅 `p=5003` 还需要精确源槽数证书。
新增 `SmallSlackSourceCertificate` 后，当前样本中该小余量窗口也已有限闭合：
`224` 个前向低素试验只有 `5` 个激活，源槽预算余量 `8.340921`。
同步升级脚本后，`c13_local_chain_contract.py` 已把
`ActiveClassTemplateBound`、`SourceSlotStructural` 与
`SmallSlackSourceCertificate` 纳入同一张后段闭合表。
新增 `SmallSlackFiniteReduction` 后，前向源槽付款被分成两个出口：
`Allow>=224` 的大余量窗口自动付款；`Allow<224` 的小余量窗口进入有限表。
当前样本的高 `P` 有限表只含 `(5003,8192,-36)`；`(997,4096,-36)`
按 `finite-p-cut=1000` 路由到低 `P` 有限证书系统。
新增 `HotShiftTargetGenerator` 后，当前高 `P` selected 窗口可由热门位移规则自动生成：
`5003:8192:-36,10007:16384:-900`，并接回 `full_postlow_chain=True`。

因此当前显式高 `P` 压力样本已经由完全局部链闭合；但完整目标窗口族生成器仍未形式化，
所以不能宣称行命题全局闭合。

## 4. 剩余硬点

全局化现在只剩以下生成器义务：

```text
LCC-G1: 证明完整目标窗口族满足比例结构条件；
LCC-G2: 证明完整目标窗口族满足 MidStructuralVoid；
LCC-G3: 证明完整目标窗口族满足 EdgeStructuralPayment；
LCC-G4: 证明完整目标窗口族满足 ResonanceFloor/SlackFloor；
LCC-G5: 证明完整目标窗口族满足 LowDeletionAllowance 密度界；
LCC-G6: 证明完整目标窗口族满足 APSingletonStructural/ActiveClassTemplateBound；
LCC-G7: 证明完整目标窗口族中 Allow<224 的窗口均落入有限源槽证书表；
LCC-G8: 证明 HotShiftGenerator 覆盖所有 C13 高 P 目标窗口，或补充遗漏出口；
LCC-G9: 对失败窗口给有限证书或 PDEC/SAE 出口。
```

这就是当前最窄的高 `P C13` 局部闭合路线图。
