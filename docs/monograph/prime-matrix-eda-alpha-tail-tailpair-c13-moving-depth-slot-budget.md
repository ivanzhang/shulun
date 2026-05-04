# AlphaTail `C13` 变模见证的端点深度槽预算

**状态：** `c13_moving_depth_slot_budget_sample_closed_global_open`

本文接续固定模 formal unit 去重。去重后，当前压力样本中的固定模重复全部消失，剩余对象是
`MovingModulusDepth-SAE`。本文把变模原子再压缩为端点深度槽，作为 SAE 可求和账本的正式单位。

## 1. 深度槽

对 formal moving atom，记端点深度阶梯

\[
s=\varepsilon+u h,\qquad 0\le \varepsilon<u.
\tag{MDB-1}
\]

其中 `h` 是 `q` 到责任区间端点的深度。定义深度槽

\[
\Xi=(p,B,r,K,\varepsilon,h),
\qquad
K=(g,j_1,j_2,u,\mathrm{side}).
\tag{MDB-2}
\]

这里 `m` 不进入槽键。`m` 只表示嵌套审计层；同一个槽内，不同 `m` 层最多各贡献一个候选。

## 2. 槽容量引理

**引理 MDB-1（端点深度槽容量）。**  
固定有限点位层集合 `M`。对任意深度槽 `Xi`，落入该槽的 formal moving atoms 数量不超过
`|M|`。

**证明。**  
固定 `p,B,r,K,epsilon,h` 后，对每个 `m`，责任区间端点 `q_-` 或 `q_+` 已确定。若
`side=left`，则 `q=q_-+h`；若 `side=right`，则 `q=q_+-h`。因此每个 `m` 至多给出一个
`q`，也至多给出一个尾素对 `(q,q+g)` 与一个 `d=qu-j_1r`。对有限集合 `M` 求和即得容量
`|M|`。□

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_moving_depth_slot_budget.py
```

默认 `C=1.3`：

```text
raw 0 formal 0 fixed 0 moving 0 slots 0
```

压力测试 `C=1.2`：

```text
raw 281 formal 224 fixed 0 moving 224
slots 215 slot_capacity 430 slot_slack 206
max_slot_load 2 capacity_failures 0 collision_slots 9
```

解释：

```text
formal moving 原子 224 个；
压缩为 215 个深度槽；
每槽负载不超过 |M|=2；
9 个碰撞槽全部只是 m=4 与 m=5 两层共同命中同一深度槽。
```

## 4. 对 SAE 出口的影响

变模出口现在应写成：

```text
MovingModulusDepth-SAE
=> formal physical unit
=> depth slot Xi=(p,B,r,K,epsilon,h)
=> slot load <= |M|.
```

因此 SAE 总量不再按所有变模原子直接计数，而按深度槽计数，并乘以固定层容量 `|M|`。
全局闭合还需要证明：

```text
目标窗口族中可产生 C13 失败的 depth slots 总量可求和；
或同一深度槽/相邻深度槽持久出现时触发 cross-modulus stitching/ColumnCRT。
```

## 5. 审稿边界

已完成：

```text
深度槽 formal unit 定义；
槽容量 load<=|M| 的逐行证明；
样本 C=1.3 无 moving 原子；
C=1.2 压力样本 moving=224 压成 slots=215，capacity_failures=0。
```

仍未完成：

```text
全局 depth slot 总量可求和；
跨尺度 persistent depth slot 的 stitching/ColumnCRT 排斥；
全局证明 C=1.3 下 moving=0。
```

所以本文完成的是变模 SAE 的容量单位化，不是行命题最终闭合。
