# AlphaTail `C13` AP 单点化结构合同

**状态：** `ap_singleton_structural_sample_closed_global_open`

本文把上一层 `APSingleton` 从样本现象推进为一个可审稿的结构充分条件：
若活跃 AP 删除类满足 `q<2ell`，则同一低素模 `ell` 的同一残基类中至多有一个尾素对。

## 1. 单点化充分条件

一个 AP 删除类固定了

```text
(ell,j,residue,g,u,j1,j2)
```

并要求

\[
q\equiv residue\pmod \ell,\qquad q,q+g\in T.
\tag{ASS-1}
\]

若该类中所有可能的 `q` 都满足

\[
q<2\ell,
\tag{ASS-2}
\]

则 `q` 必为唯一候选

\[
q=\ell+residue,
\tag{ASS-3}
\]

因为尾素块在低素块之后，`q>ell`，而同一残基类小于 `2ell` 的正代表只有
`residue` 与 `ell+residue`，其中 `residue<ell` 不能进入尾素块。

因此 `(ASS-2)` 推出 `APSingleton`。

## 2. 当前样本结构

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_ap_singleton_structural_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_ap_singleton_structural_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --format table
```

输出摘要：

```text
active=50；
all_u23=True；
all_q_lift1=True；
all_q_lt_2ell=True；
singleton=True；
max_q/ell=1.099922；
u_hist={2:25,3:25}；
lift_hist={1:50}。
```

逐窗口：

```text
p=5003:
  active=5；
  u_hist={2:5}；
  max_q/ell=1.011871。

p=10007:
  active=45；
  u_hist={2:20,3:25}；
  max_q/ell=1.099922。
```

## 3. 新剩余

`APSingleton` 现在可由以下结构链闭合：

```text
ActiveAPClass
=> u in {2,3} and q=ell+residue
=> q<2ell
=> one q per AP class。
```

当前样本已经满足该链条。完整目标族还需证明：

```text
任意活跃 AP 类不会落入 q>=2ell 的高提升残基；
或把 q>=2ell 的活跃 AP 类送入 PDEC/SAE/有限证书；
证明 ActiveClassBound，即活跃 AP 类数不超过允许删除量。
```

## 4. 审稿边界

该合同闭合的是显式样本的结构单点化，不是全局行命题证明。全局未闭合项仍为：

```text
目标族生成器无遗漏；
完整目标族上的 q<2ell 结构排除；
完整目标族上的 ActiveClassBound。
```
