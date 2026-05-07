# Triad-A1 DI Theorem 12 公式记录

**状态：** `di_theorem12_formula_extracted_substitution_open`

本记录只固定 DI Theorem 12 在当前 non-AP scale ledger 中实际需要代入的公式形态。来源为
Maynard `arXiv:2006.07088` 源码中的 `Deshouillers-Iwaniec estimate` 引理；该引理明示其为
Deshouillers--Iwaniec Theorem 12，并修正 `\mathscr J^2` 最后一项的小排印问题。

## 1. 外部公式

需要核查的 DI 输入形态为：

```text
sum_{r~R} sum_{s~S,(r,s)=1} sum_{n~N} b_{n,r,s}
  sum_{d~D} sum_{c~C,(rd,sc)=1} g(c,d) e(n * bar(d r)/(c s))

  << x^eps (sum_{r,s,n}|b_{n,r,s}|^2)^{1/2} * J
```

其中

```text
J^2 =
  C*S*(R*S+N)*(C+D*R)
  + C^2*D*S*sqrt((R*S+N)*R)
  + D^2*N*R.
```

## 2. 对当前账本的直接后果

当前 `DIKloostermanWindowSubstitutionLedger` 不能只用 `C,S,H` 三个符号关闭。DI 公式实际还需要
把 `R,D,N` 精确接到当前 dispersion/WFD 共同变量表：

```text
DIFormulaVariableTable:
  C: DI 的 c~C 窗口；
  D: DI 的 d~D 窗口；
  R: DI 的 r~R 窗口；
  S: DI 的 s~S 可逆变量窗口；
  N: DI 的 n~N 系数/频率窗口。
```

所以尺度侧的真实剩余不是“泛泛证明 J-scale”，而是：

```text
DITheorem12RDNVariableSubstitutionLedger:
  1. 把当前 KZ-E/KE-13 的 c,s,h,lambda,beta,omega 块精确重命名为 DI 的 C,D,R,S,N；
  2. 把上式 J^2 三项逐项代入；
  3. 证明每一项均被当前 WFD 自然二范数尺度与 log^{-A} 余量吸收。
```

这一步没有关闭 DI 侧；它把最后尺度硬点从三个描述性门控压成一个可审稿的公式代入账本。
