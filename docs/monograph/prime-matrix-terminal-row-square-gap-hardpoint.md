# 终端行与平方前素数间隙硬点

**状态：** `terminal_row_equivalent_to_prime_gap_before_square_open`

本文记录圆柱斜线路线必须面对的终端硬点。它不是新的失败，而是行命题中无法绕开的最小子命题。

## 1. 终端行定义

固定奇素数 `P`。第 `P` 行对应乘数

\[
x=P-1,
\tag{TRG-1}
\]

非平凡列为

\[
(P-1)P+c,\qquad 1\le c<P.
\tag{TRG-2}
\]

第 `P` 列是 `P^2`，自动被 `P` 覆盖，不参与找素数。

## 2. 与圆柱完成模型的关系

在第 `x=P-1` 行，所有 `q<P` 都满足 `q<=x`，所以所有 `<P` 斜线都已经绕完整个圆柱。
因此未完成补洞集为空：

```text
F_{P-1}=empty。
```

行命题在这一行退化为：

\[
R_{P-1}\ne\varnothing.
\tag{TRG-3}
\]

而 `R_{P-1}` 中的每个点都没有 `<P` 素因子；又它小于 `P^2`，所以必为素数。于是：

\[
R_{P-1}
=
\{c: (P-1)P+c\ \text{is prime},\ 1\le c<P\}.
\tag{TRG-4}
\]

## 3. 精确等价

令 `p_-(P^2)` 为小于 `P^2` 的最大素数。则终端行成立当且仅当

\[
P^2-p_-(P^2)<P.
\tag{TRG-5}
\]

等价地：

```text
区间 (P^2-P, P^2) 中存在素数。
```

这是行命题的终端行子命题。它比一般 Legendre 区间更窄：Legendre 只要求
`((P-1)^2,P^2)` 中有素数，而这里要求素数落在最后长度 `P` 的上半段。

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_terminal_row_gap_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_terminal_row_gap_audit.py --max-p 5000 --format table
```

完整输出保存于：

```text
docs/terminal_row_gap_audit_run_20260505.txt
```

样本结果：

```text
max_p=5000；
odd primes checked=668；
failures=0；
min terminal prime count=1；
worst observed P=3929；
gap_to_square=98；
gap_to_square/P=0.0249427335。
```

样本强烈支持 `(TRG-5)`，但这仍是平方根尺度短区间素数命题，不能由“未完成斜线补不完洞”解释，因为在终端行已经没有未完成斜线。

## 5. 对主线的影响

圆柱斜线路线现在分为两个互补目标：

```text
Bottom/Interior:
  prove |F_x|<|R_x| for 1<=x<P-1。

Terminal:
  prove p_-(P^2)>P^2-P。
```

终端目标是行命题的硬核边界条件。任何声称完全闭合行命题的证明，都必须显式给出 `(TRG-5)` 的证明或一个更强的等价证书。

因此下一步不能只继续讨论“斜线未画完”；必须同时攻两个口：

1. `Incomplete-FillerBound` 闭合 `x<P-1` 的未完成斜线补洞；
2. `TerminalSquareGap` 闭合 `x=P-1` 的平方前素数间隙。

第二项目前最干净的形式是一个低骨架残洞非空命题：

\[
\#\{1\le c<P:\gcd(P(P-1)+c,\prod_{q<P}q)=1\}>0.
\tag{TRG-6}
\]

这是下一轮必须正面硬攻的终端最小硬点。

## 6. Terminal-SAE 最新接口

终端行也可在相邻素数 `p<q` 的镜像变量中写成 SAE 分层不等式。最新两个审计文件为：

```text
docs/terminal_sae_split_audit_p2000_20260505.md
docs/terminal_sae_cancellation_audit_p2000_20260505.md
```

读数：

```text
p<=2000；
odd primes checked=302；
split unresolved records for p>=7=0；
cancellation unresolved records for p>=7=0；
min margin for p>=7=1；
max omega_tail=3；
eventual omega_tail<=2 from p=11；
last y^3<=q^2 exception p=31。
```

因此终端支线当前不再只是平方前素数间隙的裸形式，也有一个更窄的内部接口：

```text
RCI/PDEC:
无尾储备数 > 多尾碰撞超额，
或失败触发持续端点/尾锚 CRT 缺陷。
```

这仍不是全局证明；它是 `TerminalSquareGap` 的当前最小可攻证书形式。

进一步剥离见：

```text
docs/monograph/prime-matrix-terminal-rci-boundary-split.md
```

该文证明镜像 `h=q` 边界块在 `y^2>q` 后恒有余量 `1`，因此终端剩余硬点可集中到
非底块 `1<=h<q` 的 `RCI/PDEC`。
