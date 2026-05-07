# Triad-A1 Maynard 变量翻译矩阵记录

**状态：** `current_wfd_maynard_translation_matrix_open`

本记录把 `CurrentWFDMaynardVariableTranslation` 从一句“建立变量翻译表”改写为一个有限的线性矩阵
证书。它不证明当前 WFD 已落入指数锥，只固定审稿时必须同时提交的变量、对象等式和不等式行。

## 1. 两套变量必须分离

共同变量表已经固定：

```text
X,Q,N,M,C,S,H,lambda,beta,omega,g,A,B(A)。
```

Maynard-W4 指数锥使用：

```text
N_May=x^n；
R_May=x^r；
S_May=x^s；
M_May=x^m；
Q_May=x^q。
```

为避免符号冲突，当前共同变量表中的 `N,M,C,S,H` 不得直接重命名为 Maynard 的
`N_May,M_May,R_May,S_May,Q_May`。必须先给出一张翻译矩阵。

## 2. W4 参数锚点

Maynard-W4 账本给出的参数锚点为：

```text
B_window <= N_May R_May；
C_window <= N_May R_May S_May；
F_window <= N_May / Q_May；
Z_window ≍ S_May^2；
Y_window <= x^o N_May R_May^2 S_May^3 / M_May。
```

其中当前 WFD 非对角对象还必须逐项生成：

```text
z = s1*s2；
y = a*f*(h1*s1-h2*s2)；
b,c = 两个模数窗口。
```

没有这条对象等式，任何指数翻译都只是形式代入，不能关闭当前缺口。

## 3. 指数矩阵

提交当前 WFD 指数向量：

```text
v_WFD = (x_B,x_C,x_F,x_Z,x_Y,x_Q)
```

后，翻译矩阵必须证明存在 `n,r,s,m,q,eta>0` 使：

```text
n+m=1；
q=x_Q；
x_B <= n+r；
x_C <= n+r+s；
x_F <= n-q；
x_Z = 2s；
x_Y <= n+2r+3s-m；
2n+2r+s <= 1-eta；
n+2r+5s+q <= 2-eta；
2n+3r+4s+q <= 2-eta。
```

前三类行是 W4 参数翻译；后三类行是 Maynard 指数锥。这样，尺度侧不再是开放口号，而是一个
可验证的线性可行性问题。

## 4. 当前剩余

因此当前指数锥准入继续压缩为：

```text
CurrentWFDW4ObjectTranslationMatrixAdmission:
  CurrentWFDMatchesW4OffDiagonalForm；
  WFDWindowExponentVectorSubmitted；
  CurrentWFDMaynardTranslationMatrixFeasibleWithSlack。
```

这一步仍未闭合行命题；它只把下一步证明目标固定为“提交 WFD 非对角对象等式 + 提交指数向量 +
检查线性矩阵正余量”。
