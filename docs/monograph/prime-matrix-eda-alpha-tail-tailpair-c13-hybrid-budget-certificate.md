# AlphaTail `C13` 低 P 有限外壳与高 P 除数外壳的混合预算证书

**状态：** `c13_hybrid_budget_certificate_input_ready`

本文接续预算归一化账本。上一层指出：若逐窗口用 `D2` 付款，`p=997` 窗口的
`D_even` 外壳超出本窗口 `D2`。本文给出修正：低 `P` 窗口使用有限几何证书，高 `P` 窗口
使用闭式 `D_even` 除数外壳。

## 1. 混合策略

固定有限阈值 `P_fin`。定义

```text
若 P<=P_fin：
  使用 finite geometric dedup envelope；

若 P>P_fin：
  使用 closed D_even divisor envelope。
```

这一路线的逻辑是：

```text
低 P 区间数量有限，可以提交机器可复现 group 证书；
高 P 区间必须使用闭式除数和，避免无限枚举。
```

**引理 HBC-1（混合预算充分条件）。**  
若对每个窗口都有

\[
\mathrm{Cap}_{\rm hybrid}(B,r)
\le c_* D_2(B,r),
\tag{HBC-1}
\]

且 `c_*` 小于主链给 `C13` 的逐窗口预算比例，则 `C13` 的 SparseSAE/endpoint 分支可逐窗口
付款。

**证明。**  
`P<=P_fin` 时，有限证书给出真实 group 的确定 envelope 上界；`P>P_fin` 时，`D_even`
除数和上界支配全部几何 group。两者都由前文 SparseSAE 总量付款引理转成 atom 容量。逐窗口
代入 `(HBC-1)` 即可付款。□

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_hybrid_budget_certificate.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_hybrid_budget_certificate.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --eta 0.04 --finite-p-cut 1000 --finite-mode geometric --format table
```

输出摘要：

```text
hybrid_capacity=8227.120000；
D2=11023.070597；
hybrid_capacity/D2=0.746355；
max_window_hybrid/D2=0.780430。
```

窗口级：

```text
p=997   : Finite-geometric, Cap/D2=0.709157；
p=5003  : Divisor-D_even,  Cap/D2=0.780430；
p=10007 : Divisor-D_even,  Cap/D2=0.736789。
```

若低 `P` 使用真实 failure 有限证书，则得到更小读数：

```text
hybrid_capacity=7779.680000；
hybrid_capacity/D2=0.705763；
max_window_hybrid/D2=0.780430。
```

正式无条件稿更适合采用 `finite-mode=geometric`，因为它不依赖真实 failure 的素对分布细节，
只依赖有限可复现 group 外壳。

## 3. 对主链的影响

`C13-Budget-Allocation` 现在细化为：

```text
低 P：
  finite geometric certificate；

高 P：
  D_even divisor envelope；

统一付款：
  Cap_hybrid <= 0.780430 * D2
  in the current pressure sample.
```

这消除了上一层逐窗口 `p=997` 预算不足的问题。剩余不再是“是否能逐窗口付款”，而是：

```text
1. 正式确定 P_fin；
2. 完整生成 P<=P_fin 的有限 group 证书；
3. 证明 P>P_fin 的 D_even 全局外壳满足同一预算比例；
4. 将 0.780430 与主链 H/RRD/OSPC 总预算合并。
```

## 4. 审稿边界

已完成：

```text
低 P 有限、高 P 闭式的混合付款规则；
p=997 逐窗口预算不足的修复；
当前样本逐窗口最大比例降为 0.780430。
```

仍未完成：

```text
全局 P_fin 的正式选择；
P<=P_fin 的完整有限证书；
P>P_fin 的 D_even 统一预算比例证明；
与最终主链预算常数合并。
```

所以本文完成的是 `C13-Budget-Allocation` 的混合证书接口，不是行命题最终闭合。
