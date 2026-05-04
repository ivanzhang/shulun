# AlphaTail 尾素对共振剥离

**状态：** `alpha_tail_tailpair_resonance_peeling_open`

`PairCRTDefect` 样本显示，最热尾素对往往不是任意低模偏置，而是满足
`q_2-q_1=|r|` 的结构共振。本文把该现象从 PDEC 中剥离，避免把确定的尾素对几何误标为
随机 CRT 偏差。

## 1. 乘数方程

若 `d` 同时被尾素对 `(q_1,q_2)` 在点位 `(j_1,j_2)` 命中，则存在正整数 `u_1,u_2` 使

\[
d+j_1r=q_1u_1,\qquad d+j_2r=q_2u_2.
\tag{TPR-1}
\]

相减得到核心刚性方程

\[
q_1u_1-q_2u_2=(j_1-j_2)r.
\tag{TPR-2}
\]

这不是概率事件，而是一个短右端的线性丢番图方程。由于 `|r|` 很小而 `q_i` 是尾大素，
可行的 `(u_1,u_2)` 强烈受限。

## 2. 单位乘数共振

最强的结构支是

\[
u_1=u_2=1.
\tag{TPR-3}
\]

此时

\[
q_1-q_2=(j_1-j_2)r.
\tag{TPR-4}
\]

也就是说，尾素对的素数间距必须等于某个点位差乘以 `|r|`。在样本中主峰正是
`q_2-q_1=|r|`。该支每个点位对至多给出一个 `d`：

\[
d=q_1-j_1r=q_2-j_2r.
\tag{TPR-5}
\]

因此它是稀疏的“尾素对共振点”，应进入 `TailPairResonance/SAE` 账本，而不是直接作为
低模 PDEC 随机偏差。

## 3. 非单位乘数支

剩余支满足 `(u_1,u_2)\ne(1,1)`。由 `(TPR-2)`，

\[
q_1(u_1-u_2)+(q_1-q_2)u_2=(j_1-j_2)r.
\tag{TPR-6}
\]

若 `q_1,q_2>|(j_1-j_2)r|` 且 `q_1-q_2` 不处在短共振集合中，则 `u_1-u_2`
也被迫很小。于是非单位支要么：

1. 继续落入有限个短差值尾素对共振；
2. 在固定 `q_1,q_2` 上形成许多乘数解，触发 `ColumnCRT/PDEC`；
3. 只在单窗出现，进入 `SAE`。

这给出剥离后的出口：

```text
PairCRT positive bias
=> TailPairResonance
   or nonresonant correlation-PDEC
   or SAE.
```

## 4. 与 tail-overlap 的关系

二阶交集矩 `D_2` 的正偏差可以拆为

\[
D_2=D_2^{\rm res}+D_2^{\rm nonres}.
\tag{TPR-7}
\]

`D_2^{res}` 由 `(TPR-2)` 的短乘数方程支付，属于尾素对共振容量；
`D_2^{nonres}` 才是真正需要 `correlation-PDEC` 排斥的低模偏差。

因此下一步最小硬点从“排斥全部 `D_2`”缩小为：

```text
证明 D2_res 的总容量不足以支付 Xi_T；
或若 D2_res 足够大，则它触发 TailPairResonance/SAE；
剩余 D2_nonres 接入 correlation-PDEC。
```

## 5. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_resonance_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_resonance_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --format table
```

输出最热尾素对的 `gap/|r|`、实际交集数、单位乘数共振数、等乘数共振数和非单位数。

## 6. 审稿边界

已证明：

```text
任意尾素对交集点满足乘数方程 q1*u1-q2*u2=(j1-j2)r；
单位乘数支等价于 q1-q2=(j1-j2)r；
该支是稀疏尾素对共振点，应从 PDEC 主项中剥离。
```

尚未证明：

```text
全局 D2_res 容量不足以支付 tail-overlap 缺口；
或 TailPairResonance/SAE 出口全部排斥。
```

下一步最小硬点是建立 `D2_res` 的全局容量上界，尤其是固定短差值 `|r|,2|r|,...`
的尾素对共振计数上界。
