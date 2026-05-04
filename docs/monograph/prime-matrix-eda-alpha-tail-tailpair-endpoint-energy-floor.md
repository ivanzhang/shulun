# AlphaTail 端点 PDEC 的 Parseval 能量地板

**状态：** `endpoint_pdec_no_support_only_upper`

本文说明一个关键审稿事实：端点 PDEC 的上界不能只由“总质量 + 相位支撑大小”推出。
这种信息给出的最佳 Parseval 地板正好等于前文构造的 `L_PDEC`，因此若要证明

```text
U_CRT(K,Q)<L_PDEC(K,Q)
```

必须使用额外刚性，例如镜像、列残基、尾锚不可复用、Rankin 回流或端点互斥。

## 1. Parseval 地板

设 `G` 是大小为 `N=Q^2` 的端点相位群。对持久键 `K`，设带权测度 `g` 支撑在
`T` 上，`|T|=s`，总质量

\[
M=\sum_{t\in G}g(t).
\]

在仅固定 `M` 与 `s` 的条件下，

\[
\sum_{t\in G}g(t)^2\ge {M^2\over s},
\tag{EF-1}
\]

等号当且仅当质量在 `T` 上均匀分布。

正交 Fourier 的 Parseval 恒等式给出

\[
\sum_{h\ne0}|\widehat g^{\,{\rm orth}}(h)|^2
=
\sum_t g(t)^2-{M^2\over N}.
\tag{EF-2}
\]

因此

\[
\max_{h\ne0}|\widehat g^{\,{\rm orth}}(h)|
\ge
\sqrt{
{M^2/s-M^2/N\over N-1}
}.
\tag{EF-3}
\]

另一方面，端点指示测试函数给出的下界为

\[
L_{\rm PDEC}
=
{(1-s/N)M\over
\sqrt{N-1}\sqrt{s(1-s/N)}}.
\tag{EF-4}
\]

直接化简 `(EF-4)` 得

\[
L_{\rm PDEC}^2
=
{M^2/s-M^2/N\over N-1}.
\tag{EF-5}
\]

所以

\[
\max_{h\ne0}|\widehat g^{\,{\rm orth}}(h)|
\ge L_{\rm PDEC}.
\tag{EF-6}
\]

这说明：若只知道 `M` 与 `T`，任何企图证明 `U_CRT<L_PDEC` 的上界都会与 Parseval
能量地板冲突。

## 2. 审稿含义

`EF-6` 不是坏消息，而是把硬点定位准确：

```text
不能再用支撑计数、相位个数、总超额质量本身闭合 PDEC；
必须证明当前端点质量不可能以这种相位支撑方式存在，
或证明额外结构迫使质量外泄、镜像抵消、列方向分散、尾锚不可复用。
```

也就是说，下一步真正可攻目标是：

```text
Endpoint rigidity constraints
=> either mass leaves T_K
   or weighted phase vector gains cancellation
   or failure routes to SAE/Rankin/Tail-anchor/ColumnCRT.
```

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_energy_floor_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_energy_floor_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 \
  --phase-modulus 210 --format table
```

样本全部输出：

```text
floor_over_L=1.00000000,
conclusion=NO_SUPPORT_ONLY_UPPER_CAN_BE_STRICT_BELOW_L.
```

这验证了公式 `(EF-5)`，并排除了“仅靠当前端点相位账本自身闭合”的错误路线。

## 4. 下一层硬点

目前端点链条剩余的最小可攻点是：

```text
证明持久端点键 K 若保持在 T_K 上产生正质量，
则必同步触发以下至少一个结构出口：
1. mirror-pair cancellation failure；
2. column residue concentration；
3. tail-anchor reuse overload；
4. Rankin low-mod spike；
5. finite SAE。
```

只有这些额外约束给出严格上界，才可能完成
`U_CRT(K,Q)<L_PDEC(K,Q)`。

## 5. 审稿边界

已完成：

```text
Parseval 能量地板；
L_PDEC 与支撑地板完全相等的证明；
支撑/质量路线不可闭合的排除。
```

未完成：

```text
镜像、列残基、尾锚、Rankin 的定量上界组合；
任一结构出口的全局排斥或 SAE 可求和证明。
```

所以本文是防止错误闭合的必要审稿补强，同时把下一步硬攻方向唯一化为“额外刚性上界”。
