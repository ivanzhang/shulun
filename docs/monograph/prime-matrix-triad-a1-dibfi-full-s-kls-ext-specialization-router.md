# Triad-A1 DI/BFI FullS-KLS-ext specialization 路由器

**状态：** `full_s_kls_ext_contract_closed_primary_source_proof_open`

FullS-KLS-ext 外部合同版已闭合：它直接覆盖 full-S 窗口并把无投影兼容写入定理对象。若坚持完全自足或原文逐项核验，唯一剩余单点是 `DIBFIPrimarySourceSpecializationProof`。

## 1. 结构律

The external-theorem version and the self-contained version now separate cleanly. By stating FullS-KLS-ext directly for the uncentered non-projected non-AP WFD object, the external contract absorbs the former scale and no-projection compatibility gaps. The only remaining non-contract gap is a primary-source derivation of this exact specialization from DI/BFI, which is a bibliographic/deep-theorem proof task rather than another prime-matrix structural escape.

```text
previous terminal:
  FullSKLSExternalTheoremSpecialization;

new terminal:
  DIBFIPrimarySourceSpecializationProof;

external theorem contract closed:
  true;

self-contained primary-source proof closed:
  false.
```

## 2. 汇总

- `closed_specialization_gates=['PriorFullSKLSSpecializationFrontierAvailable', 'FullSKLSExtStatementMaterialized', 'NoProjectionCompatibilityInternalized', 'ExternalContractVersionClosed']`。
- `open_specialization_gates=['DIBFIPrimarySourceSpecializationProof']`。
- `terminal_gap_after_router=DIBFIPrimarySourceSpecializationProof`。

## 3. 专门化账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorFullSKLSSpecializationFrontierAvailable` | `true` | 上一层已把 ExternalFullSDIBFIAtomMatch 压成 FullSKLSExternalTheoremSpecialization。 | none at prior-frontier level | `FullSKLSExtStatementMaterialized` |
| `FullSKLSExtStatementMaterialized` | `true` | FullS-KLS-ext 已写成含 C,S,H、well-factorable 权、自然 WFD 尺度和 log-saving 的定理合同。 | none for external-contract statement | `ExternalContractVersionClosed` |
| `NoProjectionCompatibilityInternalized` | `true` | 定理合同直接要求估计当前 non-AP WFD 未中心化无投影对象；内部对象账本仍 open=['DispersionCauchyNoCenteringIdentity', 'KE13DyadicExhaustionNoProjection']，但已被外部合同吸收。 | 若不用外部合同，仍需内部证明 UncenteredWFDToKE13NoProjectionIdentity。 | `ExternalContractVersionClosed` |
| `ExternalContractVersionClosed` | `true` | 在接受 FullS-KLS-ext 作为外部深输入的版本中，full-S scale/object 合同已经闭合。 | 该 closed 只属于外部定理版，不属于完全自足版。 | `DIBFIPrimarySourceSpecializationProof` |
| `DIBFIPrimarySourceSpecializationProof` | `false` | 仓库尚未逐页从 DI/BFI 原文定理推出 FullS-KLS-ext 专门化。 | 若要求完全自足或完全原文核验，必须补这一单点证明。 | `DIBFIPrimarySourceSpecializationProof` |

## 4. 当前结论

外部深定理版中，full-S non-AP WFD 缺口已经被一个精确定理合同吸收。完全自足版只剩：

```text
DIBFIPrimarySourceSpecializationProof:
  derive Theorem FullS-KLS-ext from DI/BFI primary sources line by line.
```

这不是新的结构逃逸口；它是是否接受外部 DI/BFI 深定理输入的边界。
