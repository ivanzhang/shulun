# Prime Matrix LowMod PDEC 容量失败定位路由器

**状态：** `lowmod_pdec_capacity_failure_localized_to_finite_arc_dualcap`

本步把 PersistentLowModPDECInequality 从抽象容量不等式压成失败定位定理：若同一 LowMod formal unit 上的 U_CRT<L_PDEC 不能成立，失败必须显化为有限循环弧 DualCap，并立即进入 SAE、ColumnCRT、refined PDEC、new-layer PDEC 或 CleanKLS。真正未闭合的是未来 LowMod primitive schema 的全局有限弧 cap 质量上界。

```text
lowmod_same_set_capacity_protocol_closed=true
lowmod_capacity_multiplier_discipline_closed=true
lowmod_pdec_inequality_closed=false
row_column_unconditional_closed=false
terminal_gap_before_router=PersistentLowModPDECInequality_UCRT_LT_LPDEC
terminal_gap_after_router=LowModFiniteArcDualCapStabilityOrSparseSAE
new_atomic_input=FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas
```

## 1. 失败见证形状

| field | value |
| --- | --- |
| `formal_unit` | G_B=Z/Q_BZ with phase x mod Q_B |
| `bad_count` | g_B(t)=1_{sign*f_B(t)>=kappa_B} or the corresponding multiplicity count |
| `lower_bound` | L_lowmod=kappa_B*beta/(sqrt(Q_B-1)*\|\|f_B\|\|_2) |
| `dual_success` | U_CRT(G_B,g_B)<L_lowmod excludes the persistent LowMod PDEC branch |
| `dual_failure` | exists nontrivial character h and finite cyclic arc A with g_B(A)>=(L-alpha M)/(1-alpha) |
| `named_returns` | Sparse SAE / displacement ColumnCRT / refined PDEC / new-layer PDEC / CleanKLS |

这一步的核心是逆否：不再把 `U_CRT<L_PDEC` 失败留作抽象黑箱，而是强制它输出可审查的
`LowModDualCap(B,h,zeta,alpha)`。固定 `Q_B` 后，方向帽只是有限循环弧的预像，
因此连续参数退路已经被消掉。

## 2. 判定表

| gate | closed | proved | meaning | output |
| --- | --- | --- | --- | --- |
| `LowModFuturePDECImported` | `true` | `true` | 上一层已把 LowMod endpoint 缺陷压成 future PDEC schema 或 sparse SAE。 | `本步只攻击 persistent LowMod PDEC 容量比较分支。` |
| `SameFormalUnitPinned` | `true` | `true` | LowMod 坏行集合、相位图、测试函数都固定在同一个 Q_B 周期 formal unit 上。 | `U_CRT 与 L_PDEC 必须作用在同一个 g_B=1_S 或计数向量上。` |
| `PDECLowerBoundImported` | `true` | `true` | 持续 LowMod 坏行给出非零 Fourier 下界 L_lowmod。 | `L_lowmod = kappa_B beta /(sqrt(Q_B-1)\|\|f_B\|\|_2)。` |
| `SameSetDualCertificateProtocolRegistered` | `true` | `true` | 若同集 CRT 对偶上界 U_CRT 小于 PDEC 下界，则 persistent 分支被排除。 | `容量成功支已经是标准 PDEC dual certificate。` |
| `MultiplierDisciplineNoEscape` | `true` | `true` | 已知 Type/Fourier/fiber 成本均登记为同 formal unit 的 log-power 乘子。 | `LowMod 容量失败不能归因于账外乘子或口径错配。` |
| `CapLocalizationFailureOutput` | `true` | `true` | 若某方向 U_CRT 达到 L_PDEC，则必须输出方向帽质量集中。 | `LowModDualCap(B,h,zeta,alpha) with mass >= (L-alpha M)/(1-alpha)。` |
| `FiniteArcBasisForLowModCaps` | `true` | `true` | 固定 Q_B 后，所有方向帽都化为有限字符循环弧预像。 | `连续 zeta/alpha 搜索被压成有限 LowMod arc cap 质量界。` |
| `SparseLowRankColumnReturn` | `true` | `true` | 稀疏帽、低秩帽、列位移帽不能作为新 LowMod 终端。 | `回流 SAE / ColumnCRT-as-PDEC / primitive rank boundary。` |
| `PersistentCapNoSameLayerCycle` | `true` | `true` | 持久帽细化不能在同一有限 Q_B 层无穷循环。 | `有限步进入 refined PDEC、ColumnCRT、SAE、new-layer PDEC 或 CleanKLS。` |
| `PersistentLowModPDECInequality` | `false` | `false` | 尚未提交所有未来 LowMod primitive schema 的有限循环弧 cap 质量上界。 | `LowModFiniteArcDualCapStabilityOrSparseSAE。` |

## 3. 新的最窄剩余

```text
PersistentLowModPDECInequality_UCRT_LT_LPDEC
  <= same formal unit PDEC lower bound
     + same-set dual protocol
     + finite cyclic-arc DualCap localization
     + named return absorption
     + FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas.
```

其中前四项已经由现有材料和本路由器接线；最后一项仍未证明。
这说明早期零行假设若真的强制持续 LowMod 缺陷，下一步不能再泛谈低模 CRT 均衡，
必须直接证明所有未来 primitive LowMod schema 的有限弧帽质量界，或从帽见证中抽取
SAE/ColumnCRT/refined PDEC 的显式回流证书。

## 4. 审稿边界

本步仍不是行/列无条件定理证明：

```text
row_column_unconditional_closed=false
```

它完成的是容量失败的强制材料化，排除了“PDEC 不等式失败但不给结构见证”的无名出口。
