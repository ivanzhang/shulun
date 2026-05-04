# 粗筛盈余的条件高大素尾分解

**状态：** `alpha_tail_roughsurplus_conditional_tail_reduction_open`

本文修正并强化 `RoughSurplus-PDEC` 的高尾出口。完整粗筛盈余不能简单写成 `full surplus - low surplus`；
正确恒等式必须保留尾模型因子。

## 1. 低大素集合与尾集合

令

\[
\mathcal P_L=\{q:y<q\le D\},\qquad
\mathcal P_T=\{q:D<q\le z\}.
\tag{RCT-1}
\]

定义低大素幸存集

\[
L=\{d\in I_m:\phi_q(d)=1\ \forall q\in\mathcal P_L\},
\tag{RCT-2}
\]

完整粗筛幸存集

\[
R=\{d\in L:\phi_q(d)=1\ \forall q\in\mathcal P_T\}.
\tag{RCT-3}
\]

记

\[
V_L=\prod_{q\in\mathcal P_L}\left(1-{b_q\over q}\right),
\qquad
V_T=\prod_{q\in\mathcal P_T}\left(1-{b_q\over q}\right).
\tag{RCT-4}
\]

## 2. 精确分解

粗筛完整盈余为

\[
\Delta_{\rm full}=|R|-H V_LV_T.
\tag{RCT-5}
\]

低大素盈余为

\[
\Delta_L=|L|-HV_L.
\tag{RCT-6}
\]

条件尾盈余为

\[
\Xi_T=|R|-|L|V_T.
\tag{RCT-7}
\]

则精确恒等式

\[
\Delta_{\rm full}=V_T\Delta_L+\Xi_T.
\tag{RCT-8}
\]

**证明。**

\[
|R|-HV_LV_T=(|R|-|L|V_T)+V_T(|L|-HV_L).
\]

证毕。

因此若完整盈余为正，而低大素 `PDEC` 已排除或不足以解释，则必须有条件尾盈余 `Xi_T>0`。

## 3. 条件尾盈余的删除解释

在低幸存集 `L` 上，对 `q in P_T` 定义尾删除事件

\[
\mathcal A_q=\{d\in L:\exists j<m,\ d+jr\equiv0\pmod q\}.
\tag{RCT-9}
\]

尾幸存数为

\[
|R|=|L|-\left|\bigcup_{q\in\mathcal P_T}\mathcal A_q\right|.
\tag{RCT-10}
\]

模型预期尾删除比例为 `1-V_T`。所以

\[
\Xi_T>0
\quad\Longleftrightarrow\quad
\left|\bigcup_q\mathcal A_q\right|<|L|(1-V_T).
\tag{RCT-11}
\]

也就是说，高尾盈余等价于尾大素删除不足。

## 4. 尾删除不足二分

令一阶尾删除质量

\[
T_1=\sum_{q\in\mathcal P_T}|\mathcal A_q|.
\tag{RCT-12}
\]

若 `Xi_T>=Xi_0>0`，则至少发生一项：

1. **尾一阶质量不足。**  
   `T_1` 明显小于 `|L| sum_{q in P_T} b_q/q`，进入 tail-mass `PDEC`。
2. **尾删除重叠过强。**  
   `T_1` 正常但并集偏小，说明许多 `L` 中点同时被多个高素尾删除，进入 Rankin/ColumnCRT。
3. **孤窗尾异常。**  
   条件尾盈余只在单块出现，进入 `SAE`。

这把高大素尾出口压成三个可证书对象。

## 5. 审计样本

审计脚本：

```text
experiments/prime_matrix_alpha_tail_roughsurplus_tail_audit.py
```

样本：

| p | block | shift | m | low count | full count | Vtail | full surplus | low scaled | Xi tail | T1 | tail deleted |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 4 | 3871 | 1186 | 0.34073314 | -126.796894 | 6.181075 | -132.977969 | 4682 | 2685 |
| 997 | 4096 | -36 | 5 | 3812 | 995 | 0.26024726 | 9.905226 | 6.967766 | 2.937460 | 5755 | 2817 |
| 5003 | 8192 | -36 | 4 | 8032 | 4577 | 0.57012205 | 0.594104 | 2.814445 | -2.220340 | 5462 | 3455 |
| 5003 | 8192 | -36 | 5 | 7986 | 4261 | 0.49538252 | 309.234084 | 4.358903 | 304.875182 | 6794 | 3725 |
| 10007 | 16384 | -900 | 4 | 13636 | 8518 | 0.59169309 | 449.915405 | 0.242377 | 449.673028 | 8718 | 5118 |
| 10007 | 16384 | -900 | 5 | 12728 | 7629 | 0.51893343 | 1024.280067 | 0.264786 | 1024.015281 | 10162 | 5099 |

## 6. 审稿边界

已证明：

```text
rough full surplus = V_tail * low surplus + conditional tail surplus;
conditional tail surplus >0
=> tail deletion union below model
=> tail-mass PDEC or tail-overlap Rankin/ColumnCRT or SAE.
```

尚未证明：

```text
条件尾盈余不可能；
或 tail-mass / tail-overlap / SAE 三出口全部可排斥。
```

下一步最小硬点是证明尾一阶质量下界，或证明尾重叠过强必被 Rankin/ColumnCRT 吸收。
