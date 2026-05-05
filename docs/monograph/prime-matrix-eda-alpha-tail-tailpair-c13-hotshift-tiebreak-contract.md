# AlphaTail `C13` 热门位移 tie-break 合同

**状态：** `hotshift_tiebreak_sample_closed_global_open`

热门差值计数满足正负对称：

\[
C_D(r)=C_D(-r).
\tag{HTB-1}
\]

因此目标生成器必须指定方向代表，否则同一绝对热门差值会产生两个等强窗口。
本文采用规则：

```text
若最大热门差值的绝对值唯一，则取负向代表 r=-|r|。
```

## 1. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_tiebreak_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_tiebreak_contract.py \
  --p-list 997,5003,10007 --format table
```

## 2. 当前样本结果

```text
all_sign_symmetric=True；
all_oriented_unique=True；
generated_selected=997:1024:-36,5003:8192:-36,10007:16384:-900；
max_abs_counts={997:1,5003:1,10007:1}。
```

逐点：

```text
p=5003:
  max_diffs={-36,36}；
  max_abs_diffs={36}；
  oriented_shift=-36。

p=10007:
  max_diffs={-900,900}；
  max_abs_diffs={900}；
  oriented_shift=-900。
```

## 3. 剩余边界

该合同闭合当前样本的方向选择；全局仍需证明：

```text
所有高 P 目标窗口的最大热门绝对差值唯一；
或当多个绝对热门差值并列时，生成器全部输出或给出 PDEC/SAE/有限出口。
```
