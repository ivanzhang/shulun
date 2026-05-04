# AlphaTail `C13` 见证相位的固定模/变模分流

**状态：** `c13_pairphase_modulus_route_no_loss_exits_open`

本文修正 `C13 witness phase ledger` 的一个审稿风险：同一 `shape_key` 的见证原子不一定共享
同一个模数

\[
Q_{\rm pair}=q(q+g).
\]

标准 `PDEC` 证书要求同一坏窗集合在同一周期模数或已经证明可拼接的归一化模数下比较。
因此不能把变化的 `Q_pair` 直接塞入同一个 `PDEC`。本文把见证原子无损拆成固定模分支与
变模深度分支。

## 1. 端点深度阶梯

对端点见证原子，记 `h` 为它离责任区间端点的 `q`-深度：

```text
left  : h=q-q_-；
right : h=q_+-q。
```

端点深度 `s` 满足

\[
s=\varepsilon+u h,\qquad 0\le \varepsilon<u.
\tag{PMR-1}
\]

这里 `epsilon` 是对应责任格点端点与原始端点之间的残差。

**证明。**  
左端时 `d=u(q_-+h)-j_1r`，故
`d-A=(u q_- -j_1r-A)+u h`。括号项是左端首个格点残差，介于 `0` 与 `u-1`。
右端同理。□

因此变模见证不是自由散点；它被迫沿步长 `u` 的端点深度阶梯出现。

## 2. 固定模/变模分流

对同一 `shape_key=(g,j1,j2,u,side)` 的见证原子，按 `Q_pair=q(q+g)` 分组：

```text
FixedModulus-PDEC:
  某个 Q_pair 在该 shape 中出现至少 nu 次；
  可作为同模 PairPhase-PDEC 输入。

MovingModulusDepth-SAE:
  Q_pair 不重复或未达持久阈值；
  不能直接合并成单一 PDEC，必须进入变模深度阶梯/SAE。

MixedFixedAndMoving:
  同一 shape 中两类同时存在；固定模部分与变模部分分别登记。
```

这是无损分流，因为每个见证原子有唯一 `Q_pair`。

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_pairphase_modulus_route.py
```

默认 `C=1.3`：

```text
atoms 0 shapes 0 fixed_atoms 0 moving_atoms 0 depth_failures 0
route_counts none
```

压力测试 `C=1.2`：

```text
atoms 281 shapes 37 fixed_atoms 114 moving_atoms 167 depth_failures 0
route_counts FixedModulus-PDEC:3,
             MixedFixedAndMoving:12,
             MovingModulusDepth-SAE:22
```

这里 `depth_failures=0` 核验 `(PMR-1)`。压力样本说明：即使在人工降常数产生失败的情况下，
也不能把所有 persistent shape 直接视为同模 `PDEC`；多数原子处在变模深度阶梯分支。

## 4. 对主链的影响

`C13` 真实失败出口现在更精确地写成：

```text
C13 failure witness
=> FixedModulus-PDEC
   or MovingModulusDepth-SAE
   or MixedFixedAndMoving.
```

因此下一硬点不再是笼统的 `PairPhase-PDEC`，而是两个更窄目标：

```text
FM-PDEC:
  对固定 Q_pair 的重复见证构造 U_CRT<L_PDEC；

MMD-SAE:
  对变模见证证明端点深度阶梯的可求和上界，
  或证明变模阶梯持久时触发新的 cross-modulus stitching/ColumnCRT。
```

## 5. 审稿边界

已完成：

```text
同一 shape 下固定模与变模的无损二分；
端点深度阶梯 s=epsilon+u*h；
样本 C=1.3 无见证原子；
C=1.2 压力样本中 281 个原子全部满足深度阶梯。
```

仍未完成：

```text
全局证明 C=1.3 下无固定模/变模见证；
固定模 PDEC 的 U_CRT<L_PDEC；
变模深度阶梯的 SAE 可求和或 cross-modulus stitching。
```

所以本文是审稿级接口收紧，不是行命题最终闭合。
