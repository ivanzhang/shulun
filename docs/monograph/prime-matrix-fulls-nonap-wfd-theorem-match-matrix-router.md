# Prime Matrix Full-S non-AP WFD theorem-match 矩阵证书

**状态：** `fulls_nonap_wfd_primary_sources_screened_exact_contract_or_new_theorem_remains`

## 1. 当前目标对象

```text
object=W_full(C,S,H)=sum_{c~C} lambda_c sum_{0<|h|<=H} omega_h sum_{s~S,(s,c)=1} beta_s e_c(a_h s + b_h bar{s})
range=X≈P^2, C≈P/log^O P, S≈P, 0<|h|<=H<=P/log^O P
weights=lambda well-factorable; beta divisor-bounded; omega smooth
boundary=non-AP, uncentered, no hidden projection, no AP-source lift
required_strength=NaturalWFDScale(C,S,H)/log^A P for every A>0
```

## 2. 外部定理逐项匹配矩阵

| source | type | object | weights | window | moduli | smoothing_projection | saving_strength | conclusion | verdict | blocking gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baker-Harman-Pintz / Li short interval | `generic_short_interval` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `rejected_for_HP_top_band` | theta>1/2 gives intervals longer than P at x≈P^2 and gives no WFD/KLS estimate. |
| Friedlander-Iwaniec parity-sensitive sieve | `parity_breaking_model` | `false` | `true` | `false` | `false` | `false` | `false` | `false` | `technology_class_only` | breaks parity for the special polynomial x^2+y^4, not for the current full-S non-AP WFD window. |
| BFI large-moduli AP theorem | `primary_source_ap_dispersion` | `false` | `true` | `true` | `true` | `false` | `true` | `false` | `blocked_without_APSourceLift` | direct theorem is AP discrepancy; current object is uncentered non-AP WFD with no hidden projection. |
| DI/Kuznetsov spectral Kloosterman large sieve | `primary_source_spectral` | `false` | `true` | `true` | `true` | `false` | `true` | `false` | `partial_template_match_not_final_theorem` | phase/moduli/frequency template matches, but c-dependent completed weights and no-projection full-S object are not a ready-made corollary. |
| Maynard/GPY small-gaps machinery | `multidimensional_sieve` | `false` | `false` | `false` | `false` | `false` | `false` | `false` | `blocked_by_Maynard_S_and_conclusion_mismatch` | bounded-gaps/admissible-tuples conclusion does not give every sqrt-window; full-S Maynard-S compression is already ruled out. |
| FullS-KLS-ext external contract | `new_external_contract` | `true` | `true` | `true` | `true` | `true` | `true` | `true` | `matches_if_accepted_as_new_blackbox_theorem` | not derived line-by-line from primary DI/BFI sources; it is the exact theorem input to prove or cite. |
| New automorphic/dispersion proof | `new_theorem_to_prove` | `true` | `true` | `true` | `true` | `true` | `false` | `false` | `open` | must still prove arbitrary log-saving for c-dependent residue weights or actual NC-BLK nonconcentration. |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CurrentFullSNonAPWFDObjectPinned | `true` | `true` | 当前对象、权重、窗口、无中心化/无投影边界已固定。 | theorem-match only |
| PrimarySourcesScreenedItemwise | `true` | `true` | BHP/Li、FI、BFI、DI/Kuznetsov、Maynard 均按对象/权重/窗口/模数/投影/强度逐项筛查。 | none at screening level |
| ReadyMadePrimarySourceMatchFound | `false` | `false` | 现有主来源没有直接覆盖 full-S non-AP uncentered no-projection WFD 对象。 | FullSNonAPWFDKLSTheoremInput |
| ExternalContractExactMatchAvailable | `true` | `true` | FullS-KLS-ext 作为新外部合同与当前目标逐项匹配。 | accepted only as blackbox theorem input |
| PrimarySourceDerivationClosed | `false` | `false` | 尚未从 DI/BFI/Maynard/自守原文逐行推出 FullS-KLS-ext。 | DIBFIPrimarySourceSpecializationProof or NewAutomorphicDispersionProof |
| UnconditionalHPClosureReached | `false` | `false` | theorem-match 矩阵只确定可用输入和缺口，不证明 H_P 无条件闭合。 | FullSNonAPWFDKLSTheoremInput OR APSourceLift OR NCBLKActualBlockNonConcentration |

## 4. 结论

逐项 theorem-match 后，现有 FI/DI/BFI/Maynard/普通短区间主来源均不能直接关闭 当前 full-S non-AP uncentered no-projection WFD 对象。FullS-KLS-ext 与当前对象逐项匹配，但只能作为新外部黑箱定理合同；若要求从主来源推出，仍需 DIBFIPrimarySourceSpecializationProof，等价地需要证明 FullSNonAPWFDKLSTheoremInput、APSourceLift 或实际 NC-BLK 非集中。

当前直接主攻口为：

```text
FullSNonAPWFDKLSTheoremInput OR APSourceLift OR NCBLKActualBlockNonConcentration
```

## 5. 候选来源与允许用法

| source | allowed use | url |
| --- | --- | --- |
| Baker-Harman-Pintz / Li short interval | finite or low-k range only | https://arxiv.org/abs/2308.04458 |
| Friedlander-Iwaniec parity-sensitive sieve | conceptual model for Type-II/parity-sensitive proof design | https://annals.math.princeton.edu/articles/13033 |
| BFI large-moduli AP theorem | usable only if APSourceLift is proved | https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6385-11511_2006_Article_BF02399204.pdf |
| DI/Kuznetsov spectral Kloosterman large sieve | core technology for a new KLS-window proof | https://doi.org/10.1007/BF01390728 |
| Maynard/GPY small-gaps machinery | secondary variable-translation research only | https://annals.math.princeton.edu/2015/181-1/p07 |
| FullS-KLS-ext external contract | conditional external theorem input | docs/monograph/prime-matrix-fulls-kls-ext-acceptance-match-audit.md |
| New automorphic/dispersion proof | primary high-risk route | docs/monograph/prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.md |

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-hp-cramer-local-route-reset-router.json` | `ba52e69983d90efa54c43d08e801ff3fc83a28d5f06932454faa0189503f2e86` |
| `docs/monograph/prime-matrix-fulls-kls-ext-acceptance-match-audit.json` | `76317b8b3ff81ec7ce1a21fce006e267817a7a401a870a7cfe33637481c90d71` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-external-full-s-match-router.json` | `cc43d0554edb5270c84aed9e3a7d3bb910ab489a69c62c000e4820e8e6cdc5ba` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json` | `6a24763e9ec618957f69339a98bdfcc43a625b340589e13eb720fda036cc35be` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.json` | `23fcf1606c36412403096fed957e44d7b3ece1fc8f2c6d5290cd1e29bce7bda8` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json` | `5a24752ca3d01eb90414bd498d9be025bebda93809eaaaebb396296d2f68ba68` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json` | `cdf61edf204d0620243fac7ee0b1a96c6547362ad826938a73db3dfdb3ba853f` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.json` | `6a720ca520c5652928da6b14bd8c314c28396791e9c16c24a75cf5755980898c` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.json` | `e23282e2d3de3d5f70d70dde5013a0f0e8788656d98d04e13e0856dccece5d0f` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-maynard-s-compression-nogo-router.json` | `980b3cce2da33b14c1590365cb582816a522fb6c458ced7cc9e35a5848b1f519` |
| `docs/monograph/kls-window-di-bfi-adaptation-template.md` | `cd3acedb20cfeb4c8dd31d9804d46102bad1665e467ac86c40436b20b6531941` |
| `docs/monograph/external-theorem-index.md` | `f1d19bd0a6f3f4a3ef79426c7f32c69d59ae8c3a8e8a7c9b69f89c2cbd051a96` |
