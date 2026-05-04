# AlphaTail 端点列核的嵌套精确类压力

**状态：** `endpoint_column_nested_pressure_open`

本文继续攻主列核

```text
D^+ == 4 mod 35。
```

目标是把它下方的精确列类全部列出，避免把嵌套类误当作不交分割，同时抽取更强的单点
`ColumnCRT` 子目标。

## 1. 子类关系

若

\[
D^+\equiv a_1\pmod{q_1}
\]

满足

\[
q_1\equiv 0\pmod q,\qquad a_1\equiv a\pmod q,
\tag{ECN-1}
\]

则称它是列核

\[
D^+\equiv a\pmod q
\]

的精确子类。

注意：这里的“子类”是事件证书类，不一定是不交列分割。不同键的端点事件可以落在嵌套或相容的
列类中，因此不能用普通分割平均数直接证明容量上界。

## 2. 样本审计

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_column_nested_pressure.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_column_nested_pressure.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 \
  --phase-modulus 210 --core-residue 4 --core-modulus 35 --format table
```

主列核：

```text
D^+ == 4 mod 35:
  key_count=5,
  excess=69.927274,
  C_req=20.247349。
```

精确子类：

```text
D^+ == 4 mod 210:
  key_count=2,
  excess=27.294596,
  C_req=47.418683。

D^+ == 4 mod 105:
  key_count=2,
  excess=27.294596,
  C_req=23.709342。

D^+ == 4 mod 70:
  key_count=1,
  excess=15.338083,
  C_req=8.882243。
```

最强子目标为：

```text
D^+ == 4 mod 210,
C_req=47.418683。
```

## 3. 合法推论

**引理 ECN-1（嵌套压力准入）。**  
主列核 `4 mod 35` 的任一精确子类若持久超载，则它本身就是更强的
`ColumnCRT/PDEC` 输入。特别是 `4 mod 210` 子类给出比主列核更高的容量目标。

**证明。**  
精确子类仍是右端列残基锁相，且其坏窗集合是原 `OneSidedEndpoint/ColumnCRT` 输入的
子证书口径。容量常数按自身模数计算，若持久超载，则同样满足 ColumnCRT 定义，只是周期更细。
因此它可以独立作为更窄 PDEC 输入。□

## 4. 非法推论排除

不得使用以下推论：

```text
三个精确子类构成 4 mod 35 的不交分割。
```

原因是：

```text
D^+ == 4 mod 210 同时包含在 4 mod 105 和 4 mod 70 中；
当前质量按端点事件键计数，不是按列位置不交计数。
```

因此本文只作“更强子目标抽取”，不作“分割平均闭合”。

## 5. 下一步最小硬点

主列核路线可转为更窄目标：

```text
严攻 D^+ == 4 mod 210 的精确 ColumnCRT 子目标，
其 C_req=47.418683。
```

若能证明无 ColumnCRT 时任何单一 `mod 210` 右端列类的容量常数

\[
C_{\rm col}^{(210)}<47.418683,
\]

则该子目标被排斥；若该子目标持久，则它本身就是更强 `ColumnCRT/PDEC`。

## 6. 审稿边界

已完成：

```text
主列核下的精确子类列举；
最强子目标抽取；
嵌套非分割警告。
```

未完成：

```text
mod 210 精确列容量上界；
ColumnCRT/PDEC 排斥；
SAE 可求和或有限证书。
```
