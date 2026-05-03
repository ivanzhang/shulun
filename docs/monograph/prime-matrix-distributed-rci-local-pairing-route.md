# Distributed-RCI 的局部配对/Hall 路线

**状态：** `local_pairing_or_defect_exit_reduction`

上一节把 `Distributed-RCI` 化为：

```text
平衡双尾半素数数 < 素数数。
```

本文继续压缩下一硬点：如果不能直接用筛估计比较两类数量，则尝试构造一个
局部注入，把每个平衡双尾半素数配给同一行内附近的不同素数。若这种配对失败，
失败本身就是一个局部素数亏损/半素数过密缺陷，应进入 `PDEC/Tail-anchor`。

## 1. 对象

固定终端块 `I_h`。记

\[
\mathcal P_h=\{n\in I_h:\ n\ \text{prime}\},
\]

\[
\mathcal B_h=\{n\in I_h:\ n=\ell_1\ell_2,\ y<\ell_1,\ell_2\le p\}.
\]

`Distributed-RCI` 目标为

\[
|\mathcal B_h|<|\mathcal P_h|.
\tag{D}
\]

## 2. 局部配对命题

给定半径 `R`，构造二分图：

- 左侧顶点为 `\mathcal B_h`；
- 右侧顶点为 `\mathcal P_h`；
- 若 `|b-\pi|\le R`，连接 `b` 与 `\pi`。

若存在覆盖所有 `\mathcal B_h` 的匹配，并且至少有一个素数未被使用，则 `(D)` 成立。

由 Hall 定理，这等价于对任意子集 `S⊂\mathcal B_h`，

\[
|N_R(S)|\ge |S|.
\]

在一维有序集合中，只需检查区间型子集；即对任意整数区间 `J⊂I_h`，

\[
\#(\mathcal B_h\cap J)
\le
\#(\mathcal P_h\cap (J+[-R,R])).
\tag{Hall-R}
\]

因此下一步可攻目标是：

```text
存在可控 R，使 Hall-R 成立；
若 Hall-R 失败，则失败区间给出 PDEC/Tail-anchor 缺陷。
```

## 3. 为什么这比原命题更窄

原命题要求整块素数总数压过半素数总数。局部配对路线更结构化：

1. 若半素数分散，每个半素数附近的素数云足以吸收；
2. 若某段半素数过密且附近素数不足，则该段本身就是可定位的异常；
3. 该异常同时表现为短区间素数亏损和双尾乘积集中，正好接入
   `Endpoint CRT defect` 或 `Tail-anchor defect`。

这与前面的三分支一致：

```text
配对成功 => Distributed-RCI；
配对失败且半素数集中 => Tail-anchor；
配对失败且素数亏损持续 => PDEC。
```

## 4. 实验审计

新增脚本：

```text
experiments/prime_matrix_distributed_rci_pairing_audit.py
```

报告：

```text
docs/monograph/prime-matrix-distributed-rci-pairing-audit.md
```

在 `17<=p<=2000`、`y=floor(p/e)` 下：

- 含平衡半素数的行数：`215074`；
- 配对失败行数：`0`；
- 最大最小匹配半径：`132`；
- 最大 `radius/log^2(q)`：约 `2.3772`；
- 最大半素数/素数比值：`2/3`。

实验说明：局部配对路线是可行的；但最大半径不是常数级，正式证明不能只靠
固定小邻域。大半径样本应被纳入“局部素数亏损区间”并送入缺陷出口。

## 5. 下一步严格目标

当前最小硬点可写为：

**LPH/PDEC（Local Pairing Hall or Defect）。**
存在显式半径

\[
R(q)=C\log^2 q
\]

或稍弱的可控半径，使得对每个终端块要么 `(Hall-R)` 成立，要么存在区间 `J`
满足：

1. `\mathcal B_h` 在 `J` 中异常过密；
2. `\mathcal P_h` 在 `J+[-R,R]` 中异常过疏；
3. 该异常触发 `Tail-anchor` 或 `Endpoint CRT defect`。

若 `LPH/PDEC` 成立，则 `Distributed-RCI` 成立，进而闭合 `CDB-1`。

## 6. 轮筛阴影强化

`docs/monograph/prime-matrix-semiprime-wheel-shadow-rigidity.md` 给出两个可直接并入
局部 Hall 图的刚性约束。

第一，若半素数 `b` 要配到素数 `b+d`，则对每个小素数 `r<=z`，

\[
d\not\equiv -b\pmod r.
\tag{WS}
\]

第二，对固定短偏移 `d`，在模

\[
W_z=\prod_{r\le z}r
\]

的粗相位中，同时允许 `b` 与 `b+d` 避开全部小素数的比例精确为

\[
\rho_z(d)=
\prod_{\substack{r\le z\\ r\nmid d}}
{r-2\over r-1}.
\tag{FOS}
\]

这把原 Hall 图削成轮筛允许图：

- 奇数偏移由模 `2` 完全删除；
- `±2,±4,±8` 等偶偏移仍被 `3,5,7,...` 逐层削减；
- `±6,±12,±30` 等含更多小素因子的偏移较宽，但仍不是自由通道；
- 若某个短区间只能靠少数固定偏移补洞，则这些偏移的相位容量由 `(FOS)`
  给出显式上界。

因此 `LPH/PDEC` 可升级为：

**WSH-Hall/PDEC（Wheel-shadow Hall or defect）。**
对每个区间 `J`，要么轮筛允许图满足 Hall 条件，要么存在下列缺陷之一：

1. 固定偏移 `d` 的粗相位负载超过 `\rho_z(d)` 容量；
2. 多个半素数集中到少数尾标签，形成 Tail-anchor；
3. 轮筛允许通道存在但素数缺席，形成 Endpoint/PDEC。

这个版本直接吸收“半素数与素数不能任意靠太近”的结构事实，并避免把双粗半素数
当作自由补洞点。

## 7. 审稿边界

本文没有证明 `LPH/PDEC`，但它把下一步硬点从全局短区间素数比较进一步压成了：

```text
轮筛允许的局部 Hall 配对不等式，或可定位的短区间异常出口。
```

这比直接证明每个长度 `q` 区间素数数下界更窄，因为半素数位置已知且稀疏；
只需在这些位置附近找到足够多素数，或证明找不到时异常不可隐藏。
