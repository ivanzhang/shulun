# AlphaTail `C13` 固定模见证的 formal unit 去重

**状态：** `c13_fixed_modulus_formal_unit_sample_closed_global_open`

本文接续固定模/变模分流账本，处理 `FixedModulus-PDEC` 的首个审稿义务：同一个物理见证
不能因为出现在多个嵌套审计层中而被重复计入 `PDEC` 下界。

## 1. 物理见证单位

对一个 `C13` 见证原子定义物理键

\[
\mathcal U
=
(p,B,r,g,j_1,j_2,u,\mathrm{side},q,q+g,d).
\tag{FMU-1}
\]

注意 `m` 不进入 `(FMU-1)`。同一个 `p,B,r,d` 和同一尾素对 `(q,q+g)` 若同时出现在
`m=4` 与 `m=5` 审计层，它仍是同一个物理见证，不是两个独立坏窗约束。

## 2. formal unit 去重引理

**引理 FMU-1（嵌套层重复不可作为独立 PDEC 质量）。**  
在构造固定模 `PDEC` 下界前，所有见证原子必须先按 `(FMU-1)` 去重。去重后仍在同一
`shape_key` 与同一 `Q_pair` 下重复出现的原子，才可作为固定模 `PDEC` 的正式输入。

**证明。**  
`PDEC` 下界来自坏窗集合或多重集合中的独立正式单位。若两个记录只是在不同 `m` 层重复记录
同一 `p,B,r,d,q,q+g`，则它们对应同一物理整除事实

\[
q\mid d+j_1r,\qquad q+g\mid d+j_2r.
\]

没有额外独立约束行或独立窗口质量。因此在未证明嵌套层独立性前，必须按 `(FMU-1)` 只计一次。□

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_fixed_modulus_formal_unit.py
```

默认 `C=1.3`：

```text
raw_atoms 0 formal_atoms 0 removed_duplicates 0
raw_fixed_atoms 0 formal_fixed_atoms 0
```

压力测试 `C=1.2`：

```text
raw_atoms 281 formal_atoms 224 removed_duplicates 57 duplicate_classes 57
raw_fixed_atoms 114 formal_fixed_atoms 0
raw_fixed_shapes 15 formal_fixed_shapes 0
```

解释：

```text
人工降常数产生的所有固定模重复，均来自 m=4/5 嵌套审计层的同一物理见证重复；
按 formal unit 去重后，没有任何固定模重复保留下来。
```

## 4. 对主链的影响

固定模出口现在细化为：

```text
Raw FixedModulus-PDEC
=> formal-unit dedupe
=> TrueFixedModulus-PDEC
   or NestedLayerDuplicate removed.
```

当前样本和压力样本显示：

```text
C=1.3: 没有固定模见证；
C=1.2: 原始固定模分支全部被 NestedLayerDuplicate 去重清空。
```

这不证明全局 `TrueFixedModulus-PDEC` 为空；但它关闭了一个重要误用：不能把嵌套层重复当成
`U_CRT<L_PDEC` 需要排斥的真实固定模缺陷。

## 5. 审稿边界

已完成：

```text
formal physical unit 定义；
嵌套 m 层重复不可重复计数；
样本 C=1.3 固定模为空；
C=1.2 压力样本 raw_fixed=114 经去重后 formal_fixed=0。
```

仍未完成：

```text
全局证明 formal_fixed_atoms=0；
或对真实 formal fixed modulus 构造 U_CRT<L_PDEC；
变模深度阶梯的 SAE 可求和或 cross-modulus stitching。
```

所以本文关闭的是固定模分支的重复计数缺口，不是行命题最终闭合。
