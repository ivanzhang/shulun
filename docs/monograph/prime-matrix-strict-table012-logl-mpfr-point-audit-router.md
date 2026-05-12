# Prime Matrix strict table_012 logl/MPFR 点审计证书

**状态：** `logl_mpfr_point_audit_passed_global_logl_proof_still_open`

本步没有闭合全域 logl 证明，但把证据层补齐：归档端点、极值点、邻点和结构锚点全部通过 MPFR 对照，最大观测误差远小于 1e-12。严格自足闭合仍只剩二选一：先绑定 glibc 2.39 x86_64 logl 源码/二进制路径，再证明其 x87 指令精度；或用 MPFR 外向 log 全量重扫归档。

```text
logl_mpfr_point_audit_closed=true
std_logl_abs_error_1e_minus_12_closed=false
certified_log_summation_interval_arithmetic_closed=false
row_column_unconditional_closed=false
```

## 1. 点审计摘要

| field | value |
| --- | --- |
| `path` | `data/theta-table012-logl-mpfr-point-audit.jsonl` |
| `sha256` | `ee3edf00e4e59d82d7190a2869a77103eb8147d393a74566a89f6f8748740e99` |
| `point_count` | `464` |
| `failed_count` | `0` |
| `max_abs_error` | `1.27986243615315792839963303572673370321801965823783e-18` |
| `max_abs_error_n` | `68719476736` |
| `threshold` | `1e-12` |

## 2. 证明边界

| item | value |
| --- | --- |
| `what_this_closes` | 给 table_012 端点、极值点和结构锚点提供 MPFR 对照证据，并锁定本机 glibc/libm 行为。 |
| `why_not_global` | 有限点审计不能排除未采样整数上的 libm 异常；黑箱函数没有可用的连续性证明。 |
| `remaining` | Glibc239X86_64ELoglSSourceAndBinaryPathBindingLedger OR CertifiedMPFRIntervalThetaExtremalRescanArchive |

## 3. 判定表

| gate | closed | meaning | remaining |
| --- | --- | --- | --- |
| `StructuredCriticalPointLogLAudit` | `true` | 所有归档端点、极值点、邻点和二进制锚点的 logl/MPFR 差均小于 1e-12。 | closed as evidence only |
| `StdLogLAbsErrorLe1eMinus12ForIntegerInputsUpTo8e11` | `false` | 要把证据升级成证明，必须覆盖所有整数输入，而不是有限点。 | Glibc239X86_64ELoglSSourceAndBinaryPathBindingLedger OR CertifiedMPFRIntervalThetaExtremalRescanArchive |
| `Glibc239X86_64ELoglSSourceAndBinaryPathBindingLedger` | `false` | 证明 glibc 2.39 x86_64 ldbl-96 logl 的范围约化和多项式误差全域小于 1e-12。 | source-level polynomial/range-reduction error certificate |
| `CertifiedMPFRIntervalThetaExtremalRescanArchive` | `false` | 绕开 libm：用 MPFR 外向 log 全量重扫 theta 极值并登记新 hash。 | heavy full rescan |

## 4. 下一最窄点

```text
Glibc239X86_64ELoglSSourceAndBinaryPathBindingLedger
```

