# Prime Matrix strict table_012 glibc logl 源码绑定证书

**状态：** `glibc_logl_source_bound_x87_instruction_accuracy_open`

glibc logl 的源码对象已绑定清楚：Ubuntu glibc 2.39 的 x86_64 long-double log 实际依赖 x87 `fyl2x/fyl2xp1`，不是可直接做系数审计的软件多项式。因此旧的多项式误差证明路线应删除；唯一内部硬点改成 x87 指令精度账本。若不接受硬件指令精度证明，唯一自足替代就是 MPFR 外向 log 全量重扫。

```text
glibc_logl_source_binding_closed=true
software_polynomial_error_route_rejected=true
x87_instruction_accuracy_closed=false
std_logl_abs_error_1e_minus_12_closed=false
certified_log_summation_interval_arithmetic_closed=false
row_column_unconditional_closed=false
```

## 1. 源码与二进制

| field | value |
| --- | --- |
| `source_url` | `https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=sysdeps/x86_64/fpu/e_logl.S;hb=glibc-2.39` |
| `source_sha256` | `e81a3af5ed1994187e0a2ef24e969ee5f83ef5ad16a3c0aa3de774050fa37ae2` |
| `libm_sha256` | `1b87a1a50b496cfead2b0ad134c2ff536705c82608db240c7e8aa48d6c0e4217` |
| `disassembly_sha256` | `68a283988c24ebf9b809c313200d4846a1ccaa48e7ac9917644f9506675f45ab` |
| `wrapper_jumps_to_core_0x1a510` | `true` |
| `core_uses_fyl2x` | `true` |
| `core_uses_fyl2xp1` | `true` |

## 2. 判定表

| gate | closed | meaning | remaining |
| --- | --- | --- | --- |
| `Glibc239Ldbl96LoglSourceAndPolynomialErrorLedger` | `false` | 旧名字里的 polynomial route 与源码不匹配；glibc 2.39 x86_64 logl 走 x87 指令。 | Glibc239X86_64ELoglSSourceAndBinaryPathBindingLedger |
| `Glibc239X86_64ELoglSSourceAndBinaryPathBindingLedger` | `true` | 官方 e_logl.S、本机符号表和反汇编已绑定到同一个 x87 fyl2x/fyl2xp1 实现路径。 | closed |
| `X87FYL2X_FYL2XP1InstructionAccuracyLedger` | `false` | 需从 Intel/AMD x87 指令语义或实测形式化证书推出 FYL2X/FYL2XP1 在本输入域误差 <= 1e-12。 | architectural instruction error bound or exhaustive interval replacement |
| `CertifiedMPFRIntervalThetaExtremalRescanArchive` | `false` | 替代路线：完全绕开 x87/libm，用 MPFR 外向 log 全量重扫 theta 极值归档。 | heavy full archive rescan |
| `StdLogLAbsErrorLe1eMinus12ForIntegerInputsUpTo8e11` | `false` | 只有 x87 指令精度账本或 MPFR 重扫闭合后，logl 全域误差命题才闭合。 | X87FYL2X_FYL2XP1InstructionAccuracyLedger OR CertifiedMPFRIntervalThetaExtremalRescanArchive |

## 3. 下一最窄点

```text
X87FYL2X_FYL2XP1InstructionAccuracyLedger
```

