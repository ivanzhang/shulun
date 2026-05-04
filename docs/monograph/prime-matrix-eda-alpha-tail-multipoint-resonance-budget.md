# 多点共振压力预算接口

**状态：** `alpha_tail_multipoint_resonance_budget_reduction_open`

本文把五射线共振从“多点链出口”推进为可核验预算。核心是一个精确计数恒等式：
在三边尾锚的三点链基集合上，`s=±r` 的跨点对数正好由四点链控制，`s=±2r` 的跨点对数正好由五点链控制。

## 1. 基集合与差值对

令

\[
T_{3,r}=\{d:d,d+r,d+2r\ {\rm pass}\}.
\tag{MRB-1}
\]

对 `h=1,2` 定义共振差值对

\[
R_h^+(r)=\{(d_1,d_2)\in T_{3,r}^2:d_1-d_2=hr\},
\tag{MRB-2}
\]

\[
R_h^-(r)=\{(d_1,d_2)\in T_{3,r}^2:d_1-d_2=-hr\}.
\tag{MRB-3}
\]

## 2. 精确共振恒等式

有双射

\[
R_1^+(r)\leftrightarrow T_{4,r},\qquad (d+r,d)\leftrightarrow d,
\tag{MRB-4}
\]

\[
R_2^+(r)\leftrightarrow T_{5,r},\qquad (d+2r,d)\leftrightarrow d.
\tag{MRB-5}
\]

反向差值同理。因此

\[
|R_1^+(r)|=|R_1^-(r)|=|T_{4,r}|,
\tag{MRB-6}
\]

\[
|R_2^+(r)|=|R_2^-(r)|=|T_{5,r}|.
\tag{MRB-7}
\]

也即无符号共振容量精确为

\[
C_{\rm res}(r)=2|T_{4,r}|+2|T_{5,r}|.
\tag{MRB-8}
\]

**证明。**  
若 `(d_1,d_2) in R_1^+`，则 `d_1=d_2+r`。由于 `d_2,d_2+r,d_2+2r` 通过，且
`d_1,d_1+r=d_2+2r,d_1+2r=d_2+3r` 通过，得到四点链
`d_2,d_2+r,d_2+2r,d_2+3r`。反向由任一四点链起点 `d` 生成 `(d+r,d)`。`h=2`
同理给五点链。证毕。

## 3. 有符号压力上界

三边尾锚中的局部权是符号权，逐点绝对值不超过 `1`；锚点增量每个非平凡坐标的绝对值至多 `2`。
因此任意单位归一化的边投影 `u` 的共振跨点压力满足

\[
|\mathcal P_{\rm res}(u;r)|
\le C_u\bigl(2|T_{4,r}|+2|T_{5,r}|\bigr),
\tag{MRB-9}
\]

其中 `C_u` 是由正式锚点归一化固定的显式常数。若使用未归一化三坐标向量，保守可取
`C_u<=12`；若先把每个锚点投影除以其坐标最大值，则可取 `C_u=1`。

这一步只用三角不等式，不使用随机性。

## 4. Selberg 预算替换

设四点/五点链 Selberg 上筛预算为

\[
|T_{m,r}|\le U_m(r)+E_m(r),\qquad m=4,5,
\tag{MRB-10}
\]

其中 `U_m(r)` 是主项预算，`E_m(r)` 是端点/低模误差。由多点链包络，

\[
U_m(r)=|I_m|\cdot \mathcal V_{m,r}(z)\cdot C_{m,\lambda},
\tag{MRB-11}
\]

\[
\mathcal V_{m,r}(z)=\prod_{y<q\le z}\left(1-{b_{m,q}(r)\over q}\right),
\qquad
b_{m,q}(r)=\#\{-jr\bmod q:0\le j<m\}.
\tag{MRB-12}
\]

代入 `(MRB-9)`，得到正式共振预算

\[
|\mathcal P_{\rm res}(u;r)|
\le
2C_u\{U_4(r)+U_5(r)+E_4(r)+E_5(r)\}.
\tag{MRB-13}
\]

## 5. 预算失败的出口

若正式反例要求

\[
|\mathcal P_{\rm res}(u;r)|>\mathcal L_{\rm needed},
\tag{MRB-14}
\]

而

\[
2C_u(U_4(r)+U_5(r))<\mathcal L_{\rm needed},
\tag{MRB-15}
\]

则至少发生一项：

1. **多点 Selberg 包络失败。**  
   `|T_4|>U_4+E_4` 或 `|T_5|>U_5+E_5`。
2. **端点相位缺陷。**  
   `E_4+E_5` 承担超过
   `(\mathcal L_needed-2C_u(U_4+U_5))/(2C_u)` 的负向缺口，进入 `PDEC`。
3. **奇异因子过大。**  
   `U_4+U_5` 的大值主要由 `q|r` 的一禁退化造成，进入 `ColumnCRT/Rankin`。
4. **孤窗异常。**  
   上述压力只发生在单个块，进入 `SAE`。

这就是共振分支的审稿级预算接口：若主预算不足，失败不再是模糊“共振多”，而是明确证书出口。

## 6. 审计样本

审计脚本：

```text
experiments/prime_matrix_alpha_tail_resonance_budget_audit.py
```

样本：

| p | block | shift | T3 | T4 | T5 | res cap | T4/T3 | T5/T3 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 362 | 189 | 101 | 580 | 0.522099 | 0.279006 |
| 5003 | 8192 | -36 | 1686 | 1209 | 916 | 4250 | 0.717082 | 0.543298 |
| 10007 | 16384 | -900 | 3720 | 2860 | 2302 | 10324 | 0.768817 | 0.618817 |

## 7. 审稿边界

已证明：

```text
five-ray resonant crosspoint pressure
=> exact capacity 2T4+2T5
=> Selberg main budget + endpoint/PDEC + singular-factor/ColumnCRT + SAE.
```

尚未证明：

```text
正式参数下 2C_u(U4+U5) 小于反例所需压力；
以及 E4/E5、奇异因子、SAE 出口全部可排斥。
```

下一步最小硬点是显式选择 `z,lambda,C_u`，核验 `(MRB-15)` 的常数余量，或输出失败证书。
