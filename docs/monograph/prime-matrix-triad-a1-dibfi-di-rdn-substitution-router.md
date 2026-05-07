# Triad-A1 DI/BFI DI RDN substitution 路由器

**状态：** `di_rdn_substitution_reduced_to_current_wfd_maynard_w4_parameter_ledger_open`

DI 的 R/D/N 变量已在公式层代入到 Maynard-W4 正规形；剩余不再是 DI 定理变量不明，而是当前 WFD 块到 W4 参数表的逐项生成与 J-bound 三项支配。

## 1. 结构律

The extra DI variables R,D,N are no longer abstract: under the standard Maynard application of DI Theorem 12, they alias to Z,B,Y with S_DI=1. The remaining scale work is not theorem-formula work but current-object work: prove that the present uncentered WFD block has the W4 off-diagonal variables z=s1*s2, y=a*f*(h1*s1-h2*s2), with the required dyadic bounds, and then dominate the three W4 J-bound terms.

```text
previous terminal:
  DITheorem12RDNVariableSubstitutionLedger;

DI -> W4 alias:
  {'R_DI': 'Z', 'S_DI': '1', 'N_DI': 'Y', 'D_DI': 'B', 'C_DI': 'C'};

W4 J-bound:
  J^2 <= C(Z+Y)(C+B Z)+C^2 B sqrt((Z+Y)Z)+B^2 Y Z;

new terminal:
  CurrentWFDToMaynardW4ParameterLedger;
```

## 2. 汇总

- `di_rdn_substitution_closed=false`。
- `closed_substitution_gates=['DIToMaynardW4Alias', 'JBoundAfterAlias', 'DIAdditionalVariablesRDNMapped', 'KZEHasW4ShapeInputs']`。
- `open_substitution_gates=['CurrentWFDMatchesW4OffDiagonalForm', 'MaynardW4ParameterBoundsForCurrentWFD', 'JBoundDominanceAfterW4Substitution']`。
- `terminal_gap_after_router=CurrentWFDToMaynardW4ParameterLedger`。

## 3. 代入账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `DIToMaynardW4Alias` | `true` | DI Theorem 12 取 r=z, s=1, n=y, d=b, c=c，得到 Maynard W4 的 J-bound。 | none at pure formula-alias level | `MaynardW4ParameterBoundsForCurrentWFD` |
| `JBoundAfterAlias` | `true` | J^2 被代入为 C(Z+Y)(C+B Z)+C^2 B sqrt((Z+Y)Z)+B^2 Y Z。 | none before current-window substitution | `MaynardW4ParameterBoundsForCurrentWFD` |
| `DIAdditionalVariablesRDNMapped` | `true` | R_DI,D_DI,N_DI 已分别映到 Z,B,Y；S_DI 为平凡窗口 1。 | 仍需把当前 WFD 的内部 S/H/frequency 变量压到 Z,Y,B,C。 | `CurrentWFDToMaynardW4ParameterLedger` |
| `KZEHasW4ShapeInputs` | `true` | KZ-E spine 与共同变量表含 s1/s2、h、C/S/H 和 Kloosterman 逆元相位接口。 | 形状接口可用，但尚未证明当前块等于 Maynard W4 的 off-diagonal 结构。 | `CurrentWFDToMaynardW4ParameterLedger` |
| `CurrentWFDMatchesW4OffDiagonalForm` | `false` | Maynard W4 使用 z=s1*s2、y=a*f*(h1*s1-h2*s2)、b,c 两个模数窗口；当前账本尚未逐项生成这些变量。 | 从当前 E_disp/WFD_core 写出 z,y,b,c 的 dyadic 分解和 off-diagonal ell!=0 归约。 | `CurrentWFDToMaynardW4ParameterLedger` |
| `MaynardW4ParameterBoundsForCurrentWFD` | `false` | Maynard 应用需要 B<=NR、C<=NRS、Z≈S^2、Y<=N R^2 S^3/M 等参数界。 | 把这些 Maynard 参数界翻译为当前 X,Q,N,M,C,S,H 的非冲突变量表。 | `CurrentWFDToMaynardW4ParameterLedger` |
| `JBoundDominanceAfterW4Substitution` | `false` | 上游 open_formula_gates=['DIAdditionalVariablesRDNMapped', 'KLSModulusWindowQuantified', 'InverseVariableWindowQuantified', 'DIJScaleDominanceSubstitution']；J-bound 公式已降维但还未比较目标尺度。 | 证明 C(Z+Y)(C+BZ)、C^2B sqrt((Z+Y)Z)、B^2YZ 均被 WFD 自然尺度/log^A 吸收。 | `CurrentWFDToMaynardW4ParameterLedger` |

## 4. 当前结论

尺度侧的最窄剩余已经变为：

```text
CurrentWFDToMaynardW4ParameterLedger:
  CurrentWFDMatchesW4OffDiagonalForm;
  MaynardW4ParameterBoundsForCurrentWFD;
  JBoundDominanceAfterW4Substitution.
```

这一步关闭了 `R/D/N` 抽象变量缺口，但没有证明当前 WFD 块已经满足 W4 参数界。
