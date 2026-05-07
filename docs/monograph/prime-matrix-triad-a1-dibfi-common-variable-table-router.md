# Triad-A1 DI/BFI 共同变量表路由器

**状态：** `dibfi_common_variable_table_materialized_certificate_open`

共同变量表已建立，两个硬点被锁到同一套变量上。当前不再是两个发散任务，而是一个合取证书：同一变量表上同时证明对象不变转移与尺度不等式。

## 1. 结构律

The two remaining DI/BFI obligations now live on one variable table. Target transfer and scale inequalities cannot be solved independently with different symbols: X,Q,N,M,C,S,H,lambda,beta,omega,g,A,B(A) are shared across AP discrepancy, KE-13/WFD-core and DI/BFI theorem inputs. Therefore the next proof target is a single certificate: prove the listed transfer equations and scale inequalities on this common table.

```text
one variable table:
  X,Q,N,M,C,S,H,lambda,beta,omega,g,A,B(A);

same variables feed:
  AP discrepancy;
  KE-13/WFD-core;
  BFI Theorem 10;
  DI Theorem 12;

next certificate:
  DIBFICommonVariableTransferScaleCertificate.
```

## 2. 汇总

- `common_variable_table_materialized=true`。
- `no_variable_fork=true`。
- `target_transfer_and_scale_share_variables=true`。
- `all_transfer_steps_target_preserving=false`。
- `all_scale_inequalities_closed=false`。
- `open_gates=['TransferAndScaleCertificate']`。
- `next_external_target=DIBFICommonVariableTransferScaleCertificate`。
- `terminal_gap_after_router=DIBFICommonVariableTransferScaleCertificate`。

## 3. 共同变量表

| symbol | prime-matrix role | AP role | WFD role | DI/BFI role | transfer use | scale use | fixed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `X` | clean A1/HLC 分支交给解析 dispersion 的总长度尺度 | BFI prime-AP discrepancy 的 ambient length | Type-I/II 分块满足 N*M≈X | BFI Theorem 10 的 x 参数 | 保持原始误差对象的总质量尺度 | 所有 Q,N,M,C,S,H 的上界都归一到 X | `true` |
| `Q` | clean branch 的 well-factorable 模数总 level | q<=Q 的 AP 模数范围 | lambda_q 或 lambda_c 的总支撑 level | BFI well-factorable level | AP 模权不换成 canonical support 权 | 需证明 Q<=X^(4/7-eps) 或当前引用版允许的等价范围 | `true` |
| `N,M` | Vaughan/Heath-Brown 后的素数/互补因子 dyadic 块 | nm≡a mod q 的双变量 | Type-I/II 输入，N*M≈X | BFI dispersion 的 Dirichlet polynomial blocks | 把 AP 误差拆块但不改变求和对象 | 需证明每个 dyadic 块落入 BFI/DI 处理范围 | `true` |
| `c,C` | CRT/gcd 剥离后的有效 Kloosterman 模数 dyadic 块 | 由 q 或 q 的因子组合产生的模数块 | KE-13 中 c~C 的 well-factorable 模数变量 | DI Theorem 12 的 Kloosterman modulus family | dispersion 后保留同一模数责任，不切到 canonical 分支 | 需证明 C 与 Q、X 的关系满足 DI J-scale 估计 | `true` |
| `s,S` | completion 后的可逆类或尾素/互补单位变量 | Type block 中进入逆元相位的变量 | KE-13 中 s~S, (s,c)=1 的逆元变量 | DI Kloosterman 分子中的可逆类变量 | CRT 合并 s1,s2 后得到同一 s 变量 | 需证明 S 的 dyadic 范围与 DI estimate 的 N/R/S 参数匹配 | `true` |
| `h,H` | sawtooth/Fourier 非零频率 | AP discrepancy 完成后的非主频 | KE-13 中 0<\|h\|<=H 的频率变量 | DI/BFI Kloosterman/Bessel frequency parameter | h=0 主项扣除，h!=0 保留原始误差频率 | 需证明 H 截断尾项和 DI 频率范围同时满足 | `true` |
| `lambda` | generic WFD 分支的 well-factorable 模权 | BFI Theorem 10 的 lambda_q | KE-13 的 lambda_c | well-factorable weight | 不替换为 canonical RIW/Buchstab support 证明 | level 与分解层数只产生 log^O 损失 | `true` |
| `alpha,beta,omega` | Type 系数与平滑频率权 | Dirichlet polynomial coefficients and smooth cutoffs | divisor-bounded beta_s 与 smooth omega_h | DI/BFI 二范数与平滑权输入 | 系数由分解/平滑产生，不能加入块中心化均值扣除 | 二范数、导数和平滑损失进入 log^C 账本 | `true` |
| `g` | 非互素模数层 | q 因子或 r1,r2 的 gcd stratum | (r1,r2)=g 强迫 s1≡s2 mod g | 非互素层的 divisor/gcd 损失 | 不相容层为零，相容层不改变目标对象 | sum_g tau(g)^C/g 进入 log^C | `true` |
| `A,B(A),C0` | 最终任意对数节省目标与损失预算 | x/log^A x 目标强度 | KE-13 的 log^{-A} 节省 | 外部定理给任意 log-saving 后吸收损失 | 所有转移损失只允许进入 log^C0 | 选择 B(A)=A+C0+10 | `true` |

## 4. 对象转移方程

| step | formula | same variables | target preserved | remaining proof |
| --- | --- | --- | --- | --- |
| `APError` | `E_AP(X,Q)=sum_{q<=Q} lambda_q sum_{nm≈X} a_n b_m Delta_q(nm)` | X,Q,N,M,lambda,alpha,beta | `true` | 把 clean A1 generic WFD 残差精确写成该 AP error 或其 dyadic 总和 |
| `TypeDecomposition` | `E_AP=sum_{N*M≈X} E_{N,M}+log^O endpoint errors` | X,N,M,alpha,beta | `true` | 证明 Vaughan/Heath-Brown 分解后的端点误差均进入 log budget |
| `DispersionCauchy` | `E_{N,M} -> E_disp(r1,r2,s1,s2,h) without block-centering insertion` | Q,N,M,c,s,h,lambda,beta,omega | `false` | 写出从 BFI 原始 dispersion 到 KE-5 的逐项恒等式，确认未删同块对角 |
| `CRTPhase` | `phase(r1,r2,s1,s2,h)=e_c(a_h*s+b_h*bar(s))` | c,s,h,g | `true` | 已有模板；最终稿中需把符号与 KE-13 完全统一 |
| `KE13Identification` | `E_disp main nonzero-frequency blocks = WFD_core(C,S,H,lambda,beta,omega)` | C,S,H,lambda,beta,omega,A | `false` | 证明所有 dyadic 主块完全覆盖且无额外中心化/投影项 |

## 5. 尺度不等式表

| inequality | statement | variables | needed for | status | closed |
| --- | --- | --- | --- | --- | --- |
| `TypeProduct` | `N*M≈X` | X,N,M | BFI AP discrepancy and Type-I/II dispersion | `named_not_quantified` | `false` |
| `BFILevel` | `Q<=X^(4/7-eps) or an explicitly stronger admitted range` | X,Q,eps | BFI1986-Theorem10 | `named_not_quantified` | `false` |
| `KLSModulusWindow` | `C is a dyadic sublevel of Q and matches the DI modulus family` | C,Q,X | DI1982-Theorem12 | `named_not_quantified` | `false` |
| `InverseVariableWindow` | `S matches the DI inverse-variable length after completion` | S,N,M,C | DI1982-Theorem12 | `named_not_quantified` | `false` |
| `FrequencyWindow` | `0<\|h\|<=H and Fourier tail is absorbed by B(A)` | H,X,C,S,A | DI/BFI plus sawtooth completion | `named_not_quantified` | `false` |
| `DIJScaleDominance` | `DI Theorem 12 J-scale bound is <= natural WFD scale/log^A after substitution` | C,S,H,N,M,Q,A | KE-13 log-saving | `main_remaining_scale_certificate` | `false` |
| `LogLossAbsorption` | `B(A)=A+C0+10 absorbs dyadic, gcd, endpoint, coefficient and smoothing costs` | A,B(A),C0,g,lambda,beta,omega | final arbitrary log-saving | `ledger_ready_needs_C0_extraction` | `false` |

## 6. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `PreviousFrontierIsWindowMatch` | DIBFIWindowScaleAndTargetTransferMatch | start exactly from DIBFIWindowScaleAndTargetTransferMatch | none | common variable table | `true` |
| `TheoremLocationsStillPinned` | DIBFIOriginalDispersionCurrentWindowHypothesisMatch | BFI Theorem 10 and DI Theorem 12 remain fixed | none | reuse theorem-location certificate | `true` |
| `NoVariableFork` | one table contains AP, WFD and DI/BFI roles for every active symbol | target transfer and scale inequalities must use the same symbols | none after this router | common variable table | `true` |
| `TargetNotChangedByCentering` | SOURCE-CEN no-go keeps the uncentered WFD target | the table cannot add a hidden block-centering variable | none at table level | uncentered target row | `true` |
| `LocalFormulasAvailable` | KZ-E spine and KLS template contain KE-5, KE-8, KE-13 and variable adaptation | common rows must reference existing local formulas | none at table level | transfer rows plus scale rows | `true` |
| `TransferAndScaleCertificate` | common variables are fixed | prove transfer equations and scale inequalities using this table | the actual certificate is not yet proved | DIBFICommonVariableTransferScaleCertificate | `false` |

## 7. 当前结论

共同变量表已经完成，剩余目标不是两个可分散处理的口号，而是一个单一证书：

```text
DIBFICommonVariableTransferScaleCertificate
```

该证书必须同时证明对象转移方程和尺度不等式；若任何一行失败，generic WFD 外部 DI/BFI 引用版仍不能标记闭合。
