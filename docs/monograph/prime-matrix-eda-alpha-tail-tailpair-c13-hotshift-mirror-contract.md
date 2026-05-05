# AlphaTail `C13` 热门位移正负镜像合同

**状态：** `hotshift_mirror_sample_closed_global_open`

热门差值天然成对出现 `r` 与 `-r`。本文把这类正负并列从“可能遗漏窗口”改写为
镜像归一化：

```text
若 {r,-r} 是同一绝对热门位移，则只保留负向代表；
正向窗口通过 j 方向反射接回同一付款账本。
```

## 1. 镜像原则

对同一 `p,B,|r|`，把链点索引反射为

```text
j -> m-1-j。
```

则 `r` 与 `-r` 的几何窗口、低筛删除允许量、AP 单点化数量、源槽精确付款余量保持一致。
唯一变化是“前向源槽”方向翻转：负向代表满足 `j>j1>j2`，正向代表对应为反向源槽。
因此生成器可固定输出负向代表，而不遗漏正向同强窗口。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_mirror_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_mirror_contract.py \
  --p-list 5003,10007 --finite-p-cut 1000 --eta 0.04 --format table
```

## 3. 当前样本结果

```text
neg_selected=5003:8192:-36,10007:16384:-900；
pos_selected=5003:8192:36,10007:16384:900；
unique=True；
neg_full=True；
pos_local=True；
pos_forward=False；
pos_exact=True；
pos_small=True；
numeric_equal=True；
orientation_closed=True。
```

正负余量完全一致：

```text
mid_margin=6007；
formal_margin=411.727367；
edge_margin=106.727367；
res_margin=101.727367；
active_template_margin=66.727367；
source_exact_margin=66.727367；
small_slack_source_margin=8.340921。
```

## 4. 审稿边界

该合同只闭合当前样本的正负热门位移镜像。全局还需要证明：

```text
每个正负热门对均可用同一索引反射转成负向代表；
若出现多个不同绝对热门位移并列，则生成器需全部输出或给 PDEC/SAE/有限出口。
```
