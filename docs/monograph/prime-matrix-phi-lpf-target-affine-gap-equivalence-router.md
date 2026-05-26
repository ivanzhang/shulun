# Prime Matrix Phi-LPF target-affine gap equivalence 路由

**状态：** `target_affine_anchor_reduced_to_sqrt_prime_gap_or_signed_phase_payload`
**核验日期：** `2026-05-26`

目标仿射锚 A=kP 并没有自行产生 PDEC；它把 full-cover 等号精确改写为一个 prime gap 覆盖整行的问题。最坏 k≈P 时就是 x≈P^2、H≈sqrt(x) 的 C=1 点态短区间问题；top row 是 prime-indexed Oppermann-left 半窗。因而 target-affine-only 路线也不能闭合，下一手必须加入 signed/phase payload、真正 C=1 sqrt 输入，或 source-keyed spectral/Kloosterman lift。

```text
target_affine_gap_equivalence_synced=true
owner_only_pdec_rejected_imported=true
target_affine_anchor_alone_closes=false
target_affine_owner_pdec_proved=false
row_column_unconditional_closed=false
```

## 1. 等价形式

| name | formula | equivalent form | status |
| --- | --- | --- | --- |
| `TargetAffineFullCover` | `union_{p<=sqrt((k+1)P-1)}D_p(P,k)=[1,P-1]` | pi(kP,(k+1)P)=0 on the punctured row | open to exclude |
| `PrimeGapCrossingRow` | `there exist adjacent primes u<v with u<=kP and v>=(k+1)P` | a prime gap covers the whole target row | open to exclude uniformly |
| `SqrtScaleLocalInput` | `for x=kP, a prime exists in (x,x+P)` | H/P=1 while sqrt(x)/P=sqrt(k/P)<1 | requires C=1 sqrt-scale pointwise input near k~P |
| `TopRowOppermannLeft` | `k=P-1 gives (P^2-P,P^2)` | prime-indexed Oppermann left half-window | necessary subcore, still open |

## 2. target-affine-only 路线被压缩

| route | failure | surviving need |
| --- | --- | --- |
| Affine anchor only | A=kP merely rewrites the row as a prime-gap exclusion problem | add a signed/phase payload or a genuine pointwise sqrt-scale prime theorem |
| Legendre wide square interval | Legendre's interval splits into two halves and does not force the left top row (P^2-P,P^2) | prime-indexed Oppermann-left or full target-row positivity |
| Baker-Harman-Pintz x^0.525 | at x=P^2 it gives length P^1.05, i.e. P^0.05 rows thick | exponent 1/2 with constant <=1, or structural signed substitute |
| RH-shaped explicit formula | sqrt(x) log^2 x errors are larger than the one-row main term scale | cancellation beyond standard RH-size bounds at H=sqrt(x) |

## 3. 外部 gap/短区间尺度

| input | theta | length at x=P^2 | row thickness over P | closes one row | source |
| --- | --- | --- | --- | --- | --- |
| Baker-Harman-Pintz prime gaps | `21/40` | `P^(21/20)` | `P^(1/20)` | `false` | https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/abs/difference-between-consecutive-primes-ii/2EF13261B3B25458A25F41ED74AA2FC2 |
| Guth-Maynard short intervals | `17/30` | `P^(17/15)` | `P^(2/15)` | `false` | https://annals.math.princeton.edu/2026/203-2/p06 |
| Runbo Li Harman-sieve short intervals | `13/25` | `P^(26/25)` | `P^(1/25)` | `false` | https://arxiv.org/abs/2308.04458 |

## 4. 已有有限扫描摘要

| P | min-k | min prime count | strict defect | full cover |
| ---: | ---: | ---: | ---: | --- |
| 31 | 25 | 2 | 2 | `false` |
| 101 | 73 | 7 | 7 | `false` |
| 251 | 108 | 18 | 18 | `false` |
| 499 | 362 | 29 | 29 | `false` |
| 1009 | 905 | 52 | 52 | `false` |
| 2003 | 1256 | 113 | 113 | `false` |
| 5003 | 4980 | 260 | 260 | `false` |

## 5. 下一手

| gate | needed statement | why not circular |
| --- | --- | --- |
| `TargetAffineSignedPhasePayload` | the residues a_p=-kP mod p carry a signed Mobius/Von-Mangoldt or phase law before LPF pushforward | adds cancellation not present in support coverage |
| `PointwiseSqrtPrimeInputCOne` | for every x=kP in the target range, (x,x+P) contains a prime; near k=P this is C=1 sqrt scale | external analytic prime distribution would directly pay the row |
| `SpectralKloostermanResidueLiftWithSourceKeys` | complete target-affine residue fibers into a trace family with conductor and coefficient control | turns residue support into oscillatory cancellation |

```text
selected_next_primary_gate=TargetAffineSignedPhasePayload
selected_parallel_distribution_gate=PointwiseSqrtPrimeInputCOne
selected_parallel_spectral_gate=SpectralKloostermanResidueLiftWithSourceKeys
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `beacb1a89a6d085cb9e93d47add7339560e296f187809f9e030ba8c72de4a1bf` |
| `docs/monograph/external-theorem-index.md` | `207e9ed7e9de3810b7c046c4ad8255e40e1408ee51a643c027b6c49151e21f89` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `4c044305510ceae54c91fa45b1443d7bd9e33872374f8d13e02c6f46bda0459c` |
| `docs/monograph/prime-matrix-phi-lpf-full-cover-owner-pdec-stress-router.json` | `1cacda64073306121b9a09f0859fe640d8ec30119304ad39d7d824644ab8b0f0` |
| `docs/monograph/prime-matrix-phi-lpf-row-inequality-breakthrough-frontier-router.json` | `93b9420810fe6a699bb79d3591e65e1e3f6077e3d0c94e37842649ed8a3bfb32` |
| `docs/monograph/prime-matrix-phi-lpf-row-inequality-target-residue-cover-router.json` | `04b3e0b14d2f12b48232ea386ad31895d9a5b550a631bb8530539335f45b216b` |
| `docs/monograph/prime-matrix-phi-lpf-sqrt-oppermann-toprow-alignment-router.json` | `44cdef5d82dccf99d5dbfd4ef3a8cecde44b77e9f75e5fb04921085498e0cb75` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `12078e5619d66407e5202d49a4b4c8434772edd9b98366a682a4c8a4c951780b` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `595e390ca34f846c4f99ab9264c06464a5046e2b1394f4aca44e9ed1cff9b9c7` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `cd4cc0150ff518dc3cbcd6c6b791042f8e4a4c398db1f43293c2b8275a82267e` |
| `experiments/prime_matrix_phi_lpf_target_affine_gap_equivalence_router.py` | `72f77b8237928020edd093f17fe7f18b5716322c28e1e5cbe72c803974059a49` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `dd249f462f564c6313d4cb7d811aa9663726450c428e98c535aaa16c660a7dbf` |
