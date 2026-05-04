# AlphaTail `C13` 端点持久性合同

**状态：** `c13_endpoint_persistence_contract_no_loss_exits_open`

本文接续 `C13` 端点相位键账本。目标不是排斥端点分支，而是把端点分支中的真实
`C13` 失败质量无损登记到 `SAE` 或 `DirectedEndpointCRTDefect/PDEC`，同时明确：
近门槛但未失败的记录只能作为观察项，不能作为 `PDEC` 下界质量。

## 1. 真实失败原子

对一个端点责任区间 `J`，记

\[
T_{13}(J)=\lfloor 1.3 B_g(J)\rfloor+1,
\qquad
\sigma_{13}(J)=T_{13}(J)-N_g(J).
\tag{CPC-1}
\]

`C13` 真实失败当且仅当

\[
\sigma_{13}(J)\le 0.
\tag{CPC-2}
\]

定义整数失败质量

\[
\mu_{13}(J)=\max(0,1-\sigma_{13}(J)).
\tag{CPC-3}
\]

因此若 `sigma=0`，即 `N_g(J)=T_13(J)`，已经跨过整数门槛，贡献一个失败质量；
若 `sigma>0`，该记录不是失败，不能计入 `PDEC` 下界。

端点相位键仍为

\[
K=(g,j_1,j_2,u,\mathrm{side}).
\tag{CPC-4}
\]

## 2. 无损二分定理

**定理 CPC-1（C13 端点失败质量无损出口）。**  
给定任意有限窗口族 `W`。令 `E_K(W)` 为所有落入端点键 `K` 的 `C13` 失败原子，则

\[
\sum_{J\in E(W)}\mu_{13}(J)
=
\sum_K\sum_{J\in E_K(W)}\mu_{13}(J).
\tag{CPC-5}
\]

每个满足 `sum_{J in E_K} mu_13(J)>0` 的键唯一落入：

```text
persistent failure key -> DirectedEndpointCRTDefect/PDEC；
nonpersistent failure key -> SAE。
```

没有失败质量的 near-threshold 键只进入 `NearThresholdWatchOnly`，不得登记为
`PDEC` 下界。

**证明。**  
端点键 `(g,j1,j2,u,side)` 对每个端点责任原子唯一确定。按键分组是不交分解，故整数
失败质量求和保持 `(CPC-5)`。若某键的失败质量在给定审稿阈值下持久出现，则同一端点
线性映射 `d=qu-j_1r` 在同一短差值形状与同一端点方向上重复跨过 `C13` 门槛，这正是
既有 `DirectedEndpointCRTDefect/PDEC` 输入；若不持久，则它只能作为孤立端点异常进入
`SAE`。若 `mu_13=0`，该记录没有反例质量，只能作为近门槛观察项。□

## 3. 脚本与样本核验

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_endpoint_persistence_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_endpoint_persistence_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
```

输出摘要：

```text
records 123 keys 59 failure_records 0 failure_keys 0 failure_mass 0
min_slack 1 max_required_C 1.292474
route_counts NearThresholdWatchOnly:59
side_counts left:78,right:45
```

解释：

```text
样本中没有 C13 端点真实失败；
59 个键全部只是 near-threshold watch；
因此样本端点分支没有 PDEC 下界质量，也没有 SAE 失败质量。
```

## 4. 与旧端点账本的对齐

本文修正并精确化旧接口：

```text
C13 EndpointPhaseKey
=> if mu_13(K)>0 and persistent: DirectedEndpointCRTDefect/PDEC
=> if mu_13(K)>0 and nonpersistent: SAE
=> if mu_13(K)=0: NearThresholdWatchOnly.
```

这比直接把所有近门槛键送入 `PDEC/SAE` 更严格。正式证明中只有真实失败质量
`mu_13>0` 可以进入反例出口；近门槛键只用于定位未来最紧常数或有限验证。

## 5. 当前最窄剩余

已完成：

```text
C13 端点真实失败质量定义；
按端点键无损分解；
失败键 persistent/SAE 二分；
样本端点分支真实失败质量为 0。
```

仍未完成：

```text
全局证明所有 C13 端点键 mu_13=0；
或证明 persistent failure key 的 PDEC/ColumnCRT 排斥；
或证明 nonpersistent failure key 的 SAE 可求和上界；
以及 large-u 分支的全局 TailCutoffVoid/finite short-q 证书。
```

因此本文进一步压缩了 `C13` 端点出口，但不宣称 Prime Matrix 行命题已无条件闭合。
