# Prime Matrix Full-S theorem-match 真剩余切割证书

**状态：** `ap_lift_filtered_ncblk_expanded_true_remainder_external_or_actual_source_core_open`

## 1. 输入前沿

```text
FullSNonAPWFDKLSTheoremInput OR APSourceLift OR NCBLKActualBlockNonConcentration
```

## 2. 切割表

| gate | boundary closed | proved/accepted | effect | remaining |
| --- | --- | --- | --- | --- |
| LatestTheoremMatchFrontierImported | `true` | `false` | 上一层给出 FullSNonAPWFDKLSTheoremInput OR APSourceLift OR NCBLKActualBlockNonConcentration。 | 需要删除伪剩余并展开 NCBLK。 |
| APSourceLiftFilteredByNoGo | `true` | `true` | APSourceLift 在当前 non-AP uncentered no-projection 对象中被分支定义和对象账本阻断。 | 若新增上游 AP source identity，那已经是新定理输入，不是现有捷径。 |
| NCBLKExpandedToExactSourceEntropy | `true` | `false` | NCBLKActualBlockNonConcentration 经 BWFD/BSC/KFLS 与 branch alignment 压成 exact full-S source entropy 或外部谱定理。 | ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov。 |
| ExactEntropyReducedToSupportCapacity | `true` | `false` | exact source entropy 降为 u/v 精确因子支撑与 Type/Fourier 容量兼容；balanced range 已闭合。 | ActualNoncanonicalFullSFactorSupportCapacityTheoremInput。 |
| GenericAntiAtomRefuted | `true` | `true` | generic full-S WFD 反原子被 moving-delta capacity model 反证。 | 只能证明 actual noncanonical source theorem、限制 canonical source、或接受外部 FullS-KLS-ext。 |
| ExternalContractNotPrimarySourceClosure | `true` | `false` | FullS-KLS-ext 逐项匹配但只是外部合同；现有 DI/BFI/Maynard 主来源未逐行推出它。 | ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch or NewAutomorphicDispersionProof。 |
| DStructureRankinPromotionIndependent | `true` | `false` | 即使 full-S 数学输入完成，全局晋级仍需 DStructure/Tail-log4/finite Rankin 独立验收。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。 |
| TrueRemainderCutClosed | `true` | `false` | 最新三口已被切成两条数学输入线加一个独立晋级门；APSourceLift 不再是活动真剩余。 | (ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。 |

## 3. 删除的伪剩余

- `APSourceLift`
- `generic FullS WFD anti-atom`
- `NCBLK as an opaque terminal name`

## 4. 最新真剩余基

无黑箱/主来源逐项版：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

接受外部黑箱合同版：

```text
AcceptedFullSKLSExt AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 结论

最新 theorem-match 的三口不是三个同等真剩余。APSourceLift 已由 no-go 证书过滤；NCBLK 作为黑箱名已展开到 actual noncanonical full-S 源的支撑/容量核心；FullS-KLS-ext 只在接受外部黑箱合同后给出条件闭合，尚未由 DI/BFI 主来源逐项推出。因此当前无黑箱/主来源版真剩余为 exact primary-source full-S KLS 定理匹配，或 actual noncanonical full-S factor-support/capacity 定理，再加 DStructure/Rankin 独立晋级验收。

本证书不证明无条件闭合；它只删除伪剩余并把真剩余压到更窄的数学输入格式。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json` | `4f9aa4016fbbf8d51f98c595772ce5fae1d2c224deb27047f719305ffa1e4f01` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.json` | `e23282e2d3de3d5f70d70dde5013a0f0e8788656d98d04e13e0856dccece5d0f` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.json` | `6a720ca520c5652928da6b14bd8c314c28396791e9c16c24a75cf5755980898c` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-ncblk-branch-alignment-router.json` | `3006ac19a18cf8402ca96b39b084a98424095983c116453ed451e9b3b31710b1` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-exact-full-s-source-entropy-reduction-router.json` | `728b7afab5a9458bc19eb2bc92d973eb254a7e489559a589963372d0cd7fbed1` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-full-s-support-range-router.json` | `f2816bc3d999d89883a123b655d62d2c774412f1728d7216c2bc62c21c680e0a` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json` | `de12a79203d9b8264eeefb078253174fa5cc139b6c6188dc7acda079cf1b7f66` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-full-s-terminal-split-router.json` | `68cbb58cee80000dafab75f8a8bcd7bcb66fb3ddf498986d81d418df7a610404` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json` | `3a91fb657721093983006356a1bff7ce7e89be6a63c0ec98537453bdcfb495b4` |
| `docs/monograph/prime-matrix-self-contained-narrowest-core-router.json` | `b2e32aa8662277151d3dec40e8ce6622590fbb05c9e396c83b08741624a58bc4` |
| `docs/monograph/prime-matrix-noncanonical-source-core-atomization-router.json` | `cc605d7c0c26af7b1ff8ab3644629dc9821d805e817dd4fb141943a9830a0a08` |
| `docs/monograph/prime-matrix-final-open-input-current-attack-router.json` | `75b70b201b9ca46d4b7dd7d88341fe1c1e3b7df992f19017fb592eb97a74bde9` |
| `docs/monograph/prime-matrix-three-final-atoms-hard-attack-router.json` | `bb7fe40452cd5a75239ec656fcab12fe617346db6daa6a05cb636d48f69110fe` |
| `docs/monograph/prime-matrix-dstructure-rankin-promotion-acceptance-router.json` | `6a25a769df2b107f8a5a31e1374395d99717c4d0dd8188c969111477a648de7a` |
