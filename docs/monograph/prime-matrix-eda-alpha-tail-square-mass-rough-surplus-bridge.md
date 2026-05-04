# 平方一阶质量与粗筛盈余桥

**状态：** `alpha_tail_square_mass_rough_surplus_bridge_reduction_open`

当前闭合判据是

\[
{S_1\over mL_2(z)}\ge \Delta^{\rm rough}.
\tag{SMB-1}
\]

本文把它拆成两个可审稿子输入：平方一阶质量下界与粗筛端点盈余上界。若 `(SMB-1)` 失败，则必须产生
`SquareMass-PDEC` 或 `RoughSurplus-PDEC/SAE` 证书。

## 1. 平方一阶模型

在粗筛幸存集 `R=R_{m,r}` 上，

\[
S_1=\sum_{d\in R}H(d),
\qquad
H(d)=\#\{(a,j):a^2\mid d+jr,\ a\le y,\ 0\le j<m\}.
\tag{SMB-2}
\]

完整 residue 模型的一阶平方密度为

\[
W_m(y)=m\sum_{a\le y}{1\over a^2}.
\tag{SMB-3}
\]

定义平方质量缺陷

\[
\mathcal E_{\rm sq}=S_1-|R|W_m(y).
\tag{SMB-4}
\]

若 `\mathcal E_sq` 明显为负，则粗筛幸存集系统性避开小素平方类，产生有限平方模 `PDEC`。

## 2. 粗筛盈余归一化

粗筛盈余为

\[
\Delta^{\rm rough}=|R|-HV.
\tag{SMB-5}
\]

定义归一化盈余

\[
\mathcal R={\Delta^{\rm rough}\over HV}
\tag{SMB-6}
\]

以及平方质量安全余量

\[
\mathcal M={|R|W_m(y)\over mL_2(z)}-\Delta^{\rm rough}.
\tag{SMB-7}
\]

若 `\mathcal M>=0` 且 `\mathcal E_sq>=0`，则 `(SMB-1)` 成立。

**证明。**  
由 `(SMB-4)` 得 `S1>=|R|W_m(y)`。再由 `(SMB-7)` 得
`|R|W_m(y)/(mL2)>=Delta_rough`。证毕。

## 3. 失败二分

若 `(SMB-1)` 失败，则

\[
S_1<mL_2(z)\Delta^{\rm rough}.
\tag{SMB-8}
\]

对任意 `0<theta<1`，至少发生一项：

1. **SquareMass-PDEC。**

\[
\mathcal E_{\rm sq}\le -\theta |R|W_m(y).
\tag{SMB-9}
\]

2. **RoughSurplus-PDEC/SAE。**

\[
\Delta^{\rm rough}>
{(1-\theta)|R|W_m(y)\over mL_2(z)}.
\tag{SMB-10}
\]

第一项说明粗筛幸存集在平方剩余类上有系统性亏损；第二项说明大素粗筛端点盈余超过平方质量可承受范围。
二者都是明确证书出口。

## 4. 审计样本

审计脚本：

```text
experiments/prime_matrix_alpha_tail_square_mass_bridge_audit.py
```

样本：

| p | block | shift | m | R | S1 | model | sq defect | rough surplus | model/Hbound margin | closes |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 997 | 4096 | -36 | 4 | 1186 | 4363 | 2144.785862 | 2218.214138 | -126.796894 | 305.529049 | True |
| 997 | 4096 | -36 | 5 | 995 | 5013 | 2249.222105 | 2763.777895 | 9.905226 | 140.042914 | True |
| 5003 | 8192 | -36 | 4 | 4577 | 13405 | 8279.311786 | 5125.688214 | 0.594104 | 689.348545 | True |
| 5003 | 8192 | -36 | 5 | 4261 | 16504 | 9634.626262 | 6869.373738 | 309.234084 | 333.074333 | True |
| 10007 | 16384 | -900 | 4 | 8518 | 23726 | 15408.597567 | 8317.402433 | 449.915405 | 834.134393 | True |
| 10007 | 16384 | -900 | 5 | 7629 | 27575 | 17250.556299 | 10324.443701 | 1024.280067 | 125.757020 | True |

## 5. 审稿边界

已证明：

```text
if square-mass is not deficient and model/Hbound covers rough surplus,
then E_m<=0.
failure => SquareMass-PDEC or RoughSurplus-PDEC/SAE.
```

尚未证明：

```text
SquareMass-PDEC 与 RoughSurplus-PDEC/SAE 两个出口不可能；
或全局证明 model/Hbound margin 始终非负。
```

下一步最小硬点是分别给 `mathcal E_sq` 下界与 `Delta_rough` 上界；失败时输出平方模或粗筛端点证书。
