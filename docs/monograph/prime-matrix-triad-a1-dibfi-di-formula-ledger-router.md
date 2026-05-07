# Triad-A1 DI/BFI DI formula ledger 路由器

**状态：** `di_kloosterman_formula_extracted_rd_n_substitution_open`

DI 侧已从描述性 `DIKloostermanWindowSubstitutionLedger` 压成 `DITheorem12RDNVariableSubstitutionLedger`。公式已固定；未闭合的是 R/D/N 变量抽取和 J^2 三项逐项支配。

## 1. 结构律

The DI-side scale gap is now formula-level. The old C/S/H wording is insufficient because DI Theorem 12 uses variables R,S,N,D,C and the three-term J^2 expression. The remaining task is one substitution ledger: extract R,D,N from the current dispersion/WFD block, then compare each J^2 term to the WFD natural norm with the log-saving budget.

```text
previous terminal:
  DIKloostermanWindowSubstitutionLedger;

new DI-side terminal:
  DITheorem12RDNVariableSubstitutionLedger;

expansion:
  ['DIAdditionalVariablesRDNMapped', 'KLSModulusWindowQuantified', 'InverseVariableWindowQuantified', 'DIJScaleDominanceSubstitution'].
```

## 2. 汇总

- `di_formula_ledger_closed=false`。
- `closed_formula_gates=['DITheorem12FormulaExtracted', 'KLSInterfaceRowsReady']`。
- `open_formula_gates=['DIAdditionalVariablesRDNMapped', 'KLSModulusWindowQuantified', 'InverseVariableWindowQuantified', 'DIJScaleDominanceSubstitution']`。
- `terminal_gap_after_router=DITheorem12RDNVariableSubstitutionLedger`。

## 3. 公式账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `DITheorem12FormulaExtracted` | `true` | Maynard 公开源码中的 DI 引理已记录 J^2 三项；定理位置仍为 DI1982-Theorem12。 | none at formula-extraction level | `DITheorem12RDNVariableSubstitutionLedger` |
| `KLSInterfaceRowsReady` | `true` | KLS 模板与共同变量表已有 C/S/H、相位、gcd、平滑和 log-loss 接口。 | 模板只有 C/S/H 接口，尚未给出 DI 公式中的 R,D,N 分拆。 | `DITheorem12RDNVariableSubstitutionLedger` |
| `DIAdditionalVariablesRDNMapped` | `false` | DI Theorem 12 的 J^2 需要 R,D,N；当前共同变量表只有 X,Q,N,M,C,S,H。 | 必须把 r~R、d~D、n~N 从当前 dispersion/WFD 块中逐项抽出并固定。 | `DITheorem12RDNVariableSubstitutionLedger` |
| `KLSModulusWindowQuantified` | `false` | C 窗口已命名，但 DI 公式使用 C,D,R 的组合模数结构 C+D*R。 | 证明当前模数族可唯一分解为 DI 的 c~C,d~D,r~R 三个窗口。 | `DITheorem12RDNVariableSubstitutionLedger` |
| `InverseVariableWindowQuantified` | `false` | S 窗口已命名，但 DI 公式要求 (r,s)=1 且相位 e(n*bar(dr)/(cs))。 | 证明当前 CRT 合并变量 s、可逆条件和频率/系数 n 与 DI 的 S,N 完全同一。 | `DITheorem12RDNVariableSubstitutionLedger` |
| `DIJScaleDominanceSubstitution` | `false` | 旧 open_scale_gates=['KLSModulusWindowQuantified', 'InverseVariableWindowQuantified', 'DIJScaleDominanceSubstitution']；J^2 三项已记录但未代入。 | 把 J^2 三项逐项比较到 WFD 自然二范数尺度/log^A。 | `DITheorem12RDNVariableSubstitutionLedger` |

## 4. 当前结论

尺度侧的最窄剩余为：

```text
DITheorem12RDNVariableSubstitutionLedger:
  extract R,D,N from the current WFD block;
  substitute J^2;
  dominate all three J^2 terms by the natural WFD scale/log^A.
```

这一步关闭了“公式未固定”的退路，但没有关闭 DI 代入本身。
