# Prime Matrix 终端证书包压缩路由器

**状态：** `terminal_package_compressed_to_sae_pdec_columncrt_certificates`

TerminalCertificatePackage 已从五项独立输入压缩为三类证书族：SAE、PDEC、ColumnCRT。这补齐了第一包的结构压缩，但尚未证明三类证书族本身。

## 1. 压缩律

The first package no longer has five independent terminal inputs. No-unnamed-escape and named-exit absorption are already contract closed. CleanKLS is absorbed on the canonical branch and belongs to the noncanonical/external package otherwise. TotalDescent either reaches p=2 or produces a first-grid-fail seam already routed to PDEC/ColumnCRT/SAE. Therefore the independent terminal work is compressed to three certificate families: SAE, PDEC, and ColumnCRT.

```text
terminal_package_compression_closed=true
terminal_package_fully_proved=false
row_column_unconditional_closed=false
```

## 2. 压缩表

| item | current status | compression | independent after compression | remaining input |
| --- | --- | --- | --- | --- |
| `NoUnnamedEscape` | `closed` | 所有未命名逃逸必须进入命名出口或下降。 | `false` | none; feeds named exits |
| `NamedExitAbsorption` | `contract_closed` | Bohr-cap、EndpointSeam、CofactorAnchor 吸收到 SAE/PDEC/ColumnCRT/CleanKLS/TotalDescent。 | `false` | none; feeds certificate interfaces |
| `SAE-Cert` | `interface_open` | 稀疏/孤立坏窗不能再生成新分支；必须逐窗给 survivor/lift/higher-defect 或有限证书。 | `true` | Global SAE finite/window certificate family |
| `PDEC-Cert` | `template_ready_not_filled` | 所有持久低模/帽/端点/轮筛缺陷统一到同一坏窗集合上的 U_CRT<L_PDEC。 | `true` | PDEC-Dual/Explicit certificates for all persistent families |
| `ColumnCRT-Cert` | `routing_contract_closed_exclusion_open` | 列位移出口已条件路由；固定非零位移负载必须被排斥或回流 PDEC/SAE。 | `true` | ColumnCRT exclusion or PDEC/SAE return certificates |
| `CleanMultishellKLS` | `canonical_branch_closed_noncanonical_externalized` | canonical-source clean 分支已被最终边界吸收；noncanonical/generic clean 分支属于补集输入包或外部 KLS。 | `false` | move to NoncanonicalFullSComplementPackage or external KLS |
| `TotalDescent` | `absorbed_to_p2_or_first_seam` | 正式下降路径存在则到 p=2；不存在则首个 grid-fail seam 已材料化为 PDEC/ColumnCRT/SAE。 | `false` | first-seam PDEC/ColumnCRT/SAE, already counted above |
| `TerminalPackagePresence` | `listed` | 第一包经压缩后只剩 SAE/PDEC/ColumnCRT 三个真正独立证书族。 | `false` | SAE + PDEC + ColumnCRT certificate families |

## 3. 压缩后的独立输入

- Global SAE finite/window certificate family
- PDEC-Dual/Explicit certificates for all persistent families
- ColumnCRT exclusion or PDEC/SAE return certificates

## 4. 判定

第一包已经完成结构压缩：`CleanMultishellKLS` 不再作为 canonical 分支的独立终端，`TotalDescent` 不再作为平行终端，所有首阻断 seam 已回流到 `PDEC/ColumnCRT/SAE`。剩下必须真正证明的是三类证书族本身。完整行/列无条件命题仍未闭合。
