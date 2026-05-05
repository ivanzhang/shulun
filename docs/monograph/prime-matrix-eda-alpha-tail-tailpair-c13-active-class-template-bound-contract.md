# AlphaTail `C13` 活跃 AP 类模板上界合同

**状态：** `active_class_template_bound_sample_closed_global_open`

本文把 `ActiveClassBound` 进一步压成一个更窄的模板计数义务：
在 `APSingletonStructural` 已给出 `q<2ell` 后，每个模板骨架最多由 `K` 个低素
`ell` 激活。因此只需证明模板骨架数不超过允许删除量除以 `K`。

## 1. 合同命题

一个活跃 AP 删除类固定完整键

```text
(m,ell,j,residue,g,u,j1,j2)。
```

去掉低素 `ell` 后得到模板骨架

```text
sigma=(m,j,residue,g,u,j1,j2)。
```

若当前低素块大小为 `K`，且所有活跃类满足

\[
q<2\ell,
\tag{ACT-1}
\]

则同一完整 AP 类中至多一个 `q`，并且同一模板骨架至多由 `K` 个低素 `ell`
激活。因此

\[
A(W)\le K\,T(W),
\tag{ACT-2}
\]

其中 `A(W)` 是窗口 `W` 的活跃 AP 类数，`T(W)` 是活跃模板骨架数。
于是 `ActiveClassBound`

\[
A(W)\le Allow(W)
\tag{ACT-3}
\]

可由更强的模板付款条件推出：

\[
K\,T(W)\le Allow(W).
\tag{ACT-4}
\]

这一步不使用素数随机模型，只使用有限低素块大小与 `q<2ell` 的单点化结构。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_active_class_template_bound_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_active_class_template_bound_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 3. 当前样本结果

总账：

```text
active=50；
skeleton=28；
template_ceiling=224；
allowed=1385.963717；
template_margin=1161.963717；
skeleton_margin=145.245465；
q_lt_2ell=True；
template_pay=True。
```

逐窗口：

```text
p=5003:
  active=5；
  skeleton=5；
  template_ceiling=40；
  allowed=106.727367；
  template_margin=66.727367；
  skeleton_margin=8.340921。

p=10007:
  active=45；
  skeleton=23；
  template_ceiling=184；
  allowed=1279.236350；
  template_margin=1095.236350；
  skeleton_margin=136.904544。
```

因此当前样本不仅满足真实活跃类付款 `A(W)<=Allow(W)`，还满足更强的模板付款
`K T(W)<=Allow(W)`。最紧处仍是 `p=5003`，但模板余量为正。

## 4. 剩余接口

该合同把 `LCC-G6` 压窄为两个更清晰的全局义务：

```text
ACT-G1: 完整目标族上证明 q<2ell，或把 q>=2ell 的高提升类送入 PDEC/SAE/有限证书；
ACT-G2: 完整目标族上证明 SkeletonCountBound，即 T(W)<=Allow(W)/K。
```

当前文档不宣称行命题全局闭合。它只说明：一旦 `ACT-G1` 与 `ACT-G2`
在完整目标族上成立，`ActiveClassBound` 就自动闭合，并可接回
`LowDeletionAllowance -> SlackFloor -> FormalLocalPayment` 主链。
