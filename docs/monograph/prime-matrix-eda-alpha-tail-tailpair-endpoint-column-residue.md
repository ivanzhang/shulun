# AlphaTail 单侧端点锁相的列残基核归约

**状态：** `endpoint_column_residue_core_reduction_open`

本文把 8 条 `OneSidedEndpoint/ColumnCRT` 锁相输入进一步反解为真实右端列残基类。结论是：

```text
8 条轴向锁相输入并非分散；
它们坍缩到两个低模列残基核。
```

这一步把下一层 ColumnCRT 硬点从“8 条独立锁相行”压缩为“两类低模列核容量上界”。

## 1. 锁相方程反解

右端轴向频率给出

\[
hD^+\equiv \lambda\pmod Q.
\tag{ECR-1}
\]

令

\[
g=(h,Q).
\]

若 `g|lambda`，则 `(ECR-1)` 等价于唯一简化列残基类

\[
D^+\equiv a\pmod {Q/g},
\tag{ECR-2}
\]

其中

\[
a\equiv (h/g)^{-1}(\lambda/g)\pmod {Q/g}.
\tag{ECR-3}
\]

若 `g∤lambda`，锁相方程不相容，应回流为审计错误或异常出口。

## 2. 引理：轴向锁相到列核

**引理 ECR-1（列残基反解）。**  
每条 `ExactAxisPhaseLock` 输入都给出一个唯一列残基类 `(a mod Q/g)`。同一端点侧的多条
残基类若满足

\[
a_i\equiv a_j\pmod{(q_i,q_j)},
\tag{ECR-4}
\]

则它们有公共低模投影

\[
D^+\equiv a_0\pmod{\gcd_i q_i}.
\tag{ECR-5}
\]

**证明。**  
`(ECR-2)` 是一元线性同余的标准化简。兼容条件 `(ECR-4)` 是两个同余类交非空的必要充分
条件；对一个兼容连通分量重复取最大公约数，得到公共低模投影 `(ECR-5)`。□

## 3. 样本审计

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_column_residue_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_column_residue_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 \
  --phase-modulus 210 --format table
```

精确残基类：

```text
D^+ == 8 mod 70   : excess=28.759861；
D^+ == 4 mod 105  : excess=27.294596；
D^+ == 4 mod 210  : excess=27.294596；
D^+ == 4 mod 70   : excess=15.338083；
D^+ == 8 mod 35   : excess=12.854342；
D^+ == 8 mod 30   : excess=9.336303。
```

兼容分量进一步坍缩为两个低模列核：

```text
ColumnCore A:
  D^+ == 4 mod 35,
  key_count=5,
  total_excess=69.927274；

ColumnCore B:
  D^+ == 3 mod 5,
  key_count=3,
  total_excess=50.950505。
```

注意：`ColumnCore B` 的公共投影只有 `mod 5`，因为其中一个输入是 `D^+==8 mod 30`。
若不合并该输入，则可保留更强的 `D^+==8 mod 35/70` 子核；正式证书可按需要选择精确类或
兼容投影类，但不能把弱投影误写成强结论。

## 4. 对 ColumnCRT 硬点的压缩

上一层：

```text
8 条精确右端锁相 ColumnCRT 输入。
```

本文压缩为：

```text
两个低模右端列核：
  D^+ == 4 mod 35；
  D^+ == 3 mod 5。
```

因此下一步最小硬点是证明：

```text
右端端点质量不能在这两个低模列核中持久超载；
若超载，则触发 ColumnCRT/PDEC；
若只有限出现，则进入 SAE。
```

## 5. 审稿边界

已完成：

```text
锁相方程 hD^+==lambda mod Q 的逐行反解；
精确列残基类登记；
兼容低模列核聚合。
```

未完成：

```text
两个列核的容量上界；
ColumnCRT/PDEC 的全局排斥；
有限 SAE 账本或可求和证明。
```
