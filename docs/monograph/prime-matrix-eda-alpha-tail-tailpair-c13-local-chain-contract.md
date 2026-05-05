# AlphaTail `C13` 高 `P` 局部闭合链合同

**状态：** `c13_local_chain_sample_closed_target_family_open`

本文把近期三个窄接口合成为一条不依赖 Gate 总池交换的局部闭合链：

```text
Target syntax
RatioStructuralVoid
MidStructuralVoid
EdgeStructuralPayment
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

若逐窗口满足

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
target_rule_closed=False。
```

因此当前显式高 `P` 压力样本已经由完全局部链闭合；但完整目标窗口族生成器仍未形式化，
所以不能宣称行命题全局闭合。

## 4. 剩余硬点

全局化现在只剩以下生成器义务：

```text
LCC-G1: 证明完整目标窗口族满足比例结构条件；
LCC-G2: 证明完整目标窗口族满足 MidStructuralVoid；
LCC-G3: 证明完整目标窗口族满足 EdgeStructuralPayment；
LCC-G4: 证明目标窗口族不遗漏任何 C13 高 P 目标窗口；
LCC-G5: 对失败窗口给有限证书或 PDEC/SAE 出口。
```

这就是当前最窄的高 `P C13` 局部闭合路线图。
