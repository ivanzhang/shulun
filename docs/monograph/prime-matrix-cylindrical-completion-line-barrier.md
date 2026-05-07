# 方阵圆柱斜线完成屏障

**状态：** `completed_line_skeleton_promising_reduced_to_incomplete_filler_bound`

本文回到用户提出的方阵斜线覆盖与圆柱环绕模型。核心结论是：  
“所有 `<P` 素因子的斜线未全画完之前不可能整行全覆盖”不能直接作为形式理由；但它可以严写成一个更强、更可攻的二段命题：

```text
已完成斜线 q<=x 形成低素数骨架；
未完成斜线 x<q<P 只能补骨架残洞；
若未完成斜线补不完这些残洞，则该行含素数。
```

这里第 `x` 个乘数行是

\[
I_{P,x}=\{xP+1,\ldots,xP+P-1\},\qquad 1\le x<P .
\tag{CLB-1}
\]

第 `P` 列 `xP+P` 自动被 `P` 覆盖，故只研究列 `1<=c<P`。

## 1. 圆柱斜线精确定义

对每个素数 `q<P`，第 `x` 行被 `q` 覆盖的列为

\[
C_q(x)=\{1\le c<P:\ c\equiv -xP\pmod q\}.
\tag{CLB-2}
\]

因为 `P` 在 `mod q` 中可逆，随着 `x` 增加，`C_q(x)` 的相位在 `q` 行圆柱上周期为 `q`。因此：

```text
q<=x  : 该 q 斜线的圆柱相位已经至少绕完一周；
x<q<P : 该 q 斜线在当前行之前尚未绕完整个 q 圆柱。
```

这给出自然分解：

\[
L_x=\{q<P:q\le x\},\qquad H_x=\{q<P:x<q<P\}.
\tag{CLB-3}
\]

## 2. 已完成骨架与未完成补洞

先只画已完成斜线 `q<=x`。其残洞为

\[
R_x=\{1\le c<P:\forall q\le x,\ q\nmid xP+c\}.
\tag{CLB-4}
\]

这些列对应 `x`-rough 数。未完成斜线能补掉的残洞为

\[
F_x=\{c\in R_x:\exists q,\ x<q<P,\ q\mid xP+c\}.
\tag{CLB-5}
\]

最终未覆盖列为

\[
U_x=R_x\setminus F_x.
\tag{CLB-6}
\]

若 `c in U_x`，则 `xP+c` 没有任何 `<P` 素因子。又因

\[
P<xP+c<P^2,
\tag{CLB-7}
\]

所以 `xP+c` 必为素数。因此：

```text
U_x 非空  => 第 x 行含素数。
```

也就是说，行命题的圆柱完成版本精确化为：

\[
|R_x|>|F_x|,\qquad 1\le x<P.
\tag{CLB-8}
\]

这比“还有斜线没画完”更强，也更接近可证明不等式。

## 3. 为什么原始直觉需要这个加强

单独说“某条斜线还没画完整”不够。原因是：一行全覆盖只需要每列被某条斜线命中，不要求每条斜线都已绕完整个圆柱。甚至前两行的累计列投影在小样本中很快就覆盖了全部列，因此“累计投影没满”不是可用不变量。

真正有用的不变量是 `(CLB-4)--(CLB-6)`：

```text
已完成斜线留下多少 x-rough 残洞；
未完成斜线中有多少能作为高素因子补洞；
补洞后是否仍有 P-rough 残洞。
```

这正好把几何直觉变成筛论对象：低层圆柱骨架 + 高层未完成线补洞。

## 4. 样本审计

脚本：

```text
experiments/prime_matrix_cylindrical_completion_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_cylindrical_completion_audit.py \
  --p-list 23,101,499,997,1999,5003 --format table
```

完整输出保存于：

```text
docs/cylindrical_completion_audit_run_20260505.txt
```

摘要：

| P | 最薄最终洞 | 最薄骨架洞 | 最薄行未完成补洞 | 最薄行 x |
|---:|---:|---:|---:|---:|
| 23 | 2 | 3 | 1 | 14 |
| 101 | 7 | 8 | 1 | 73 |
| 499 | 29 | 29 | 0 | 362 |
| 997 | 54 | 55 | 1 | 916 |
| 1999 | 110 | 111 | 1 | 1881 |
| 5003 | 260 | 260 | 0 | 4980 |

这说明在最薄行，已完成斜线骨架已经非常接近最终素数洞集合；未完成斜线只补掉极少数骨架残洞。换言之，数值上真正的屏障不是“未完成斜线数量不够”，而是：

```text
未完成斜线虽然数量很多，但能命中低骨架残洞的相位极少。
```

## 5. 可证明部分

**Lemma CLB-1（完成分解恒等式）。**  
对每个 `1<=x<P`，

\[
[1,P-1]\setminus\bigcup_{q<P}C_q(x)=R_x\setminus F_x.
\tag{CLB-9}
\]

**证明。**  
素数 `q<P` 被唯一分为 `q<=x` 与 `x<q<P` 两类。先删去前者得到 `R_x`，再删去后者在 `R_x` 内的命中点得到最终未覆盖集合。证毕。

**Lemma CLB-2（最终洞自动为素数）。**  
若 `c in U_x`，则 `xP+c` 为素数。

**证明。**  
`c in U_x` 表示 `xP+c` 没有 `<P` 素因子；又 `1<=x<P,1<=c<P` 给出 `P<xP+c<P^2`。若其合成，则最小素因子 `<P`，矛盾。证毕。

因此完全闭合只剩一个具体不等式：

```text
CLB-FillerBound:
对所有奇素数 P 与 1<=x<P，
未完成斜线命中的骨架残洞数 |F_x| 严格小于骨架残洞数 |R_x|。
```

## 6. 下一最小硬点

`CLB-FillerBound` 可继续拆成两个更窄目标：

1. **低骨架下界。**
   证明
   \[
   |R_x|\ge A(P,x)
   \]
   其中 `A(P,x)` 至少保持正且典型为 `P/log x`。

2. **未完成补洞上界。**
   证明
   \[
   |F_x|\le |R_x|-1.
   \]
   更结构化地，若 `c in F_x`，则
   \[
   xP+c=qm,\qquad x<q<P,\qquad m>x.
   \tag{CLB-10}
   \]
   因而每个补洞点是一个带高素因子的 `x`-rough 合数。若这类点试图吃掉所有 `R_x`，就应触发
   低模 CRT 缺陷、Tail-anchor 集中，或 SAE 单窗逃逸。

当前最优目标因此更新为：

```text
Completed-Line Skeleton
=> Incomplete-FillerBound
=> PDEC/SAE/Tail-anchor 排斥
=> 行命题。
```

这保留了圆柱斜线直觉，同时避免把“斜线未画完”误用成独立证明。

## 7. 底部带缺口坐标

在靠近第 `P` 行的底部带，`Incomplete-FillerBound` 还能进一步几何化。令

\[
x=P-h,\qquad q=P-a.
\tag{CLB-11}
\]

若某个未完成斜线命中骨架残洞，则

\[
xP+c=qm.
\tag{CLB-12}
\]

当 `h<sqrt(P)` 时，样本与直接代数都显示 `m<P`，可写为 `m=P-b`。代入得到

\[
P(P-h)+c=(P-a)(P-b)
=P^2-(a+b)P+ab.
\tag{CLB-13}
\]

由于 `1<=c<P` 且 `ab<P`，必有

\[
a+b=h,\qquad c=ab.
\tag{CLB-14}
\]

所以底部 `sqrt(P)` 带中的未完成补洞列不再是任意列，而只能来自

```text
P-a 与 P-b 同为素数；
a+b=h；
补洞列 c=ab。
```

审计脚本：

```text
experiments/prime_matrix_incomplete_filler_deficit_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_incomplete_filler_deficit_audit.py \
  --p-list 997,1999,5003 --format table
```

完整输出保存于：

```text
docs/incomplete_filler_deficit_audit_run_20260505.txt
```

结果：

```text
P=997  : bottom sqrt(P) band hit rows=4,  max_hits=1, clean_pair_identity=True,
          min(|R|-floor(h/2))=51；
P=1999 : bottom sqrt(P) band hit rows=12, max_hits=2, clean_pair_identity=True,
          min(|R|-floor(h/2))=93；
P=5003 : bottom sqrt(P) band hit rows=18, max_hits=2, clean_pair_identity=True,
          min(|R|-floor(h/2))=245。
```

这给出下一步更锋利的底部带目标：

```text
BottomDeficitPairBound:
在 h<sqrt(P) 中，所有未完成补洞都落在 c=a(h-a) 这条二次缺口曲线上；
证明低骨架残洞 R_{P-h} 不可能全部落在这些二次缺口列上。
```

若 `R_{P-h}` 全部落在 `c=a(h-a)`，则残洞集合同时满足低素数避让和一条短二次乘积曲线，
这应触发低模 CRT/PDEC 缺陷。这个目标比原始 `|F_x|<|R_x|` 更窄，适合作为下一轮硬攻入口。

事实上，在该底部带中有简单容量上界

\[
|F_{P-h}|\le \left\lfloor {h\over2}\right\rfloor,
\tag{CLB-15}
\]

因为 `a` 与 `h-a` 给出同一列 `a(h-a)`；当 `h` 为偶数时，
`a=h/2` 的高素平方 `(P-h/2)^2` 也是合法补洞，必须计入容量。
所以底部带闭合可进一步降为

\[
|R_{P-h}|>\left\lfloor {h\over2}\right\rfloor,\qquad h<\sqrt P.
\tag{CLB-16}
\]

样本中 `(CLB-16)` 的余量很大。下一步若继续无黑箱硬攻，应优先证明底部带低骨架下界
`(CLB-16)`；它比完整行命题弱得多，只要求 `P-h`-rough 数量超过一条长度约 `h/2` 的二次缺口曲线。

后续复核见：

```text
docs/monograph/prime-matrix-bottom-deficit-pair-bound-hard-attack.md
```

该文修正了平方型补洞通道，并用分段筛把样本扩展到 `P=100003`。
