# Prime Matrix square-phase low-alpha z=61 final input basis

**状态：** `z61_final_input_basis_reduced_to_schinzel_level_or_primitive_multiatom_pdec_open`

z=61 strict 自足线的局部链条已经压到底：dyadic companion 等价、平方窗口正规形、单参数多项式三元组、以及 primitive/不可约/无固定素因子全部闭合。因此继续在局部同余或有限样本上硬挤不会推出全局闭合；剩余守门项精确二分为：外部 Schinzel/Bateman-Horn 等级的三多项式同步素值输入，或内部同 formal unit 的 primitive 多原子 PDEC family 排斥。当前已物化 PDEC 实例为零，只关闭实例和准入边界，不关闭全局 family。

```text
phase_modulus_b=28842
selected_root_class=200003
local_z61_chain_closed=true
external_prime_tuple_input_available=false
persistent_phase_pdec_excluded=false
final_z61_gate_closed=false
row_column_unconditional_closed=false
```

## 1. 最终输入基定理

`LocalZ61ChainClosed AND (SchinzelOrBatemanHornLevelInput OR PrimitiveMultiAtomSameFormalUnitPDECExclusion) => Z61CompanionGateClosed`。

反过来说，在本仓库当前输入集中，局部链条已闭合但两个全局守门项均未提交，
所以不能把该 z=61 线路登记为无条件闭合。

## 2. 守门表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `Z61FormalUnitAndNoTheoremSwitch` | `true` | `false` | target=bucket unbalanced<=8, omega=4, shell=(8D,16D] | 本证书仍在同一个 z=61 formal unit 内工作，不把目标偷换为别的命题。 |
| `LocalDyadicCompanionEquivalence` | `true` | `false` | z61_dyadic_companion_boundary_requires_independent_square_window_input_open | dyadic companion 的局部等价链已经闭合。 |
| `ShiftedSquareWindowNormalForm` | `true` | `false` | p^2 = A*s - C | 平方窗口已经正规化为单参数二次进位方程。 |
| `PolynomialTupleExactAdmissibility` | `true` | `false` | degree=5, content=1, no_fixed_prime_divisor=true | primitive、不可约、无固定素因子已闭合；局部同余障碍耗尽。 |
| `SampleT0Recovery` | `true` | `false` | t=0, p=200003, a4=9371, a2=9767 | 样本点可恢复局部 companion；它不是全局输入。 |
| `SchinzelOrBatemanHornLevelInput` | `false` | `true` | simultaneous prime values for p(t), a4(t), a2(t) | 若走外部素性路线，必须提交 Schinzel H / Bateman-Horn 等级输入或等价强度定理。 |
| `PersistentPhasePDECAdmissionBoundary` | `true` | `false` | persistent_terminal_reduced_to_primitive_multiatom_pdec_certificate | 持久终端准入边界已闭合；裸持久标签不能直接作为终端。 |
| `CurrentMaterializedPersistentInstances` | `true` | `false` | current materialized primitive non-tautological candidates = 0 | 当前已物化实例关闭，但这不排斥全局 family。 |
| `PrimitiveMultiAtomSameFormalUnitPDECExclusion` | `false` | `true` | global U_CRT < L_PDEC for every admitted same-formal-unit primitive multi-atom certificate | 若走内部自足路线，必须排斥同 formal unit 的 primitive 多原子 PDEC family。 |

## 3. 样本恢复不是全局证明

| object | value | prime |
| --- | ---: | --- |
| `p` | 200003 | `true` |
| `a4` | 9371 | `true` |
| `a2` | 9767 | `true` |

样本点 `t=0` 说明局部 companion 实例真实存在；但全局命题需要同类输入在证明链所需尺度上成立。
这正是 Schinzel/Bateman-Horn 级同步素值输入，或内部 PDEC 排斥必须承担的内容。

## 4. 下一步最窄硬点

- 内部自足线：`PrimitiveMultiAtomSameFormalUnitPDECCertificateForB28842`。
- 外部对接线：`SchinzelHypothesisHLevelInputForZ61PolynomialPrimeTuple`。
- 优先顺序：先攻 `B28842` 同 formal unit primitive 多原子 PDEC 容量排斥；若改走外部线，必须严格匹配三多项式同步素值定理。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-companion-boundary-router.json` | `69fbf839066d2ff7d7c34bd7086a1e59342099c780be06c3a5e04549098847d6` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-algebraic-normal-form-router.json` | `3106b08898673dceec88f43cb038db997802b0cf966bda9a04ef4f4675f01293` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-quadratic-prime-triple-param-router.json` | `cd9ca8bbd7c90b9bbf51bc802b5bf5716929247a6b9d718b9784c5206d95233e` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-polynomial-tuple-admissibility-router.json` | `720bf769224bd9a2b0fc8f392b1a0c28c6edb325d96601f7d4207defc55ea3ab` |
| `docs/monograph/prime-matrix-pdec-cap-persistent-terminal-admission-router.json` | `1993c57c8ba939c0c678e9d70c5a9c49314659b594746e5ff4a3fa1335f41d2e` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_final_input_basis_router.py` | `e69564c8f47eda93839d00493c509cbe52067735995e1e2a9f9eecaa9f073ad3` |
