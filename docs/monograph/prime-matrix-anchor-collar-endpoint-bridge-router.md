# Prime Matrix anchor-collar 容量端点缺陷桥路由器

**状态：** `anchor_collar_capacity_reduced_to_endpoint_pdec_or_fiber_saturation`

本步没有证明 anchor-collar 容量不足；它证明容量不足的失败形态已被精确桥接：早期零行使 Prime_x=0，而精确恒等式 H_x=Prime_x+A_x 将反例转为 H_x=A_x。若低骨架主项超过 anchor 容量，则得到强负端点 PDEC；若不超过，则短素数纤维必须近饱和并进入 PDEC/SAE 命名回流。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
anchor_collar_endpoint_bridge_closed=true
anchor_collar_prime_fiber_capacity_fully_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=AnchorCollarPrimeFiberCapacityBoundOrPDECReturn
terminal_gap_after_router=(AnchorCollarEndpointDefectPDECExclusion OR AnchorFiberSaturationPDECOrSAEReturn)
```

## 1. 精确桥

```text
H_x(P)=Prime_x(P)+A_x(P) for x>=sqrt(P)
Assume EarlyZeroRowWithinP => Prime_x(P)=0 => H_x(P)=A_x(P)
H_x(P)=(P-1)V_x(P)+E_x(P); if (P-1)V_x(P)-A_x(P)>=G_x>0 then E_x(P)<=-G_x
```

这仍然是在 `Assume EarlyZeroRowWithinP` 下工作；真实样本缺席不参与证明。

## 2. 替换律

```text
AnchorCollarPrimeFiberCapacityBoundOrPDECReturn
  =>
(AnchorCollarEndpointDefectPDECExclusion OR AnchorFiberSaturationPDECOrSAEReturn)
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AnchorCollarCapacityGateActive` | `true` | `true` | 上一层最新最窄硬点就是 AnchorCollarPrimeFiberCapacityBoundOrPDECReturn。 | `本步只攻击该硬点。` |
| `AnchorGeometryImported` | `true` | `true` | canonical collar 与短素数纤维窗口已经闭合。 | `可定义精确容量 A_x。` |
| `ExactRoughPrimeAnchorIdentity` | `true` | `true` | 对 x>=sqrt(P)，每个 x-rough 点要么是素数洞，要么唯一地是 canonical q*m anchor 点。 | `H_x = Prime_x + A_x。` |
| `EarlyZeroForcesPrimeVoid` | `true` | `true` | 若早期零行存在，则所有 x-rough 点必须被高标签覆盖，所以 Prime_x=0。 | `反例给出 H_x=A_x。` |
| `EndpointDecompositionImported` | `true` | `true` | 包含排除给出 H_x=(P-1)V_x+E_x，完全类似 DLS13 端点桥。 | `若主项超过容量，反例强制 E_x 为负。` |
| `CapacityFailureBecomesEndpointDefect` | `true` | `true` | 若 (P-1)V_x-A_x 存在正间隙 G_x，则早期零行推出 E_x<=-G_x。 | `这就是 anchor-collar 版 PDEC 端点缺陷。` |
| `NoGapMeansFiberSaturation` | `true` | `true` | 若没有正间隙，则 A_x 必须接近或超过低骨架主量，短纤维出现近饱和支付。 | `持久近饱和进入 PDEC；孤立近饱和进入 SAE/LocalSurvivor。` |
| `PDECSchemaAvailableForEndpointDefect` | `true` | `false` | PDEC schema 准入防火墙已存在，但全局 PDEC family 排斥仍未证明。 | `只能路由，不能宣称终端排斥完成。` |
| `SampleIdentityAudit` | `true` | `false` | 样本只复核 H_x=Prime_x+A_x 口径和 canonical anchor 唯一性。 | `anchor_collar_identity_sample_verified_endpoint_bridge_open` |
| `AnchorCollarEndpointBridgeClosed` | `true` | `true` | anchor-collar 容量硬点已转成端点 PDEC 排斥或短纤维饱和命名回流。 | `(AnchorCollarEndpointDefectPDECExclusion OR AnchorFiberSaturationPDECOrSAEReturn)` |
| `AnchorCollarEndpointDefectPDECExclusion` | `false` | `false` | 尚未排斥早期零行强制产生的 E_x<=-G_x 级端点相位缺陷。 | `下一步最窄目标。` |
| `AnchorFiberSaturationPDECOrSAEReturn` | `false` | `false` | 尚未证明无主项间隙时的短纤维近饱和必然给出可排斥 PDEC/SAE。 | `备用分支。` |

## 4. 样本口径审计

样本只用于复核恒等式实现，不作为证明输入。

| P | rows | min prime holes | identity verified |
| ---: | ---: | ---: | --- |
| 101 | 91 | 7 | `true` |
| 499 | 477 | 29 | `true` |
| 997 | 966 | 54 | `true` |

## 5. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND (AnchorCollarEndpointDefectPDECExclusion OR AnchorFiberSaturationPDECOrSAEReturn) AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND (AnchorCollarEndpointDefectPDECExclusion OR AnchorFiberSaturationPDECOrSAEReturn) AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

最窄目标更新为 `AnchorCollarEndpointDefectPDECExclusion`：排斥早期零行强制产生的 `E_x<=-G_x` 级同 formal unit 端点相位缺陷；若主项间隙失败，则进入 `AnchorFiberSaturationPDECOrSAEReturn`。
