# Prime Matrix Phi-LPF row inequality breakthrough frontier 路由

**状态：** `row_delta_phi_breakthrough_formula_frontier_synced_open`
**核验日期：** `2026-05-26`

行级奇偶性障碍现在已压成一个明确不等式，但要真正破障，必须给出严格覆盖缺口、覆盖等号 PDEC、点态 theta/psi 平方根行输入，或 source-keyed signed divisor/trace/Type-II 族。当前外部短区间最强输入仍厚于一行；固定 wheel 与 Euler product 主项只能定位残差，不能独立支付正性。

```text
breakthrough_formula_frontier_synced=true
strict_cover_inequality_proved_uniformly=false
row_column_unconditional_closed=false
```

## 1. 临界尺度

```text
x=P^2
row_length=P=x^(1/2)
expected_prime_count=P/(2 log P)
needed_error_strength=total Delta-Phi/signed-distribution error must be o(P/log P) or produce one explicit survivor/PDEC
```

最小新定理格式：

```text
For every target Prime Matrix row (A,B], either sum_{p<=sqrt(B)}(C_p(B)-C_p(A)) <= B-A-1, or the equality/overcover case returns a named LPF-owner residue PDEC/SAE.
```

## 2. 可真正破障的公式接口

| priority | name | formula | new content needed | status |
| ---: | --- | --- | --- | --- |
| 1 | `UniformDeltaPhiCoverDefect` | `sum_{p<=sqrt(B)}(C_p(B)-C_p(A)) <= B-A-1` | prove a uniform strict deficit in the LPF owner cover, not merely the exact prefix identity | open |
| 2 | `NamedLPFOwnerResiduePDEC` | `Delta-Phi cover equality => forbidden LPF-owner residue/phase packet` | turn the equality case into a structured contradiction involving owner residues, cofactors, and phase keys | open |
| 3 | `PointwiseThetaPsiCOneInputAtSqrtRowScale` | `theta(B)-theta(A)>0, or psi(B)-psi(A)>PrimePowerTail(A,B)` | zero-exception pointwise lower bound for H=sqrt(x) rows | open; stronger than current published/preprint short-interval inputs |
| 4 | `SourceKeyedMobiusVonMangoldtTraceTypeIIFamily` | `Lambda/Mobius/Type-I-II decomposition with source-keyed error < row main term` | admissible signed coefficients before pushforward, conductor control, and Type-II cancellation at q,m~sqrt(x) | open |
| 5 | `SpectralKloostermanTraceLift` | `completed trace/Kloosterman family attached to q-spine/hinge source keys` | upgrade finite q-spine ledgers to a uniform trace family with stable source keys | open |
| 6 | `ExplicitFormulaBeyondRHAtH=sqrt(x)` | `psi(x+H)-psi(x)=H+error with error < H-PrimePowerTail, H=sqrt(x)` | zero cancellation stronger than the standard RH-size error at the exact square-root scale | open |

## 3. 外部短区间尺度缺口

| input | theta | length at x=P^2 | row thickening | closes one strict row | source |
| --- | --- | --- | --- | --- | --- |
| Guth--Maynard zero-density / short intervals | `17/30` | `P^(17/15)` | `P^(2/15)` | `false` | https://arxiv.org/abs/2405.20552 |
| Le Duc Hieu APs of primes in short intervals | `17/30` | `P^(17/15)` | `P^(2/15)` | `false` | https://arxiv.org/abs/2509.04883 |
| Runbo Li Harman-sieve short intervals | `13/25` | `P^(26/25)` | `P^(1/25)` | `false` | https://arxiv.org/abs/2308.04458 |

## 4. 假突破路线的安全用法

| route | failure | safe use |
| --- | --- | --- |
| more wheel refinement | fixed wheel margins become N(P,k)>R_S(P,k); at primorial limit this returns to row primality itself | use wheels only to localize a PDEC equality case or to shrink residual composites |
| Euler product main term only | floor/periodic boundary errors at row length P are the same scale as the target survivor | must carry exact Legendre-Phi floors or prove a signed saving |
| generic short interval theorem with theta>1/2 | proves a prime after thickening the row by P^(2theta-1), leaving fixed rows unresolved | can bound zero-row runs, but cannot close every row |
| support-only P2/rough count | P2 and rough composites can saturate the same support classes as primes | only as an owner/phase ledger feeding signed trace or PDEC |

## 5. 下一手

```text
chosen_primary_attack_target=UniformDeltaPhiCoverDefectOrNamedLPFOwnerResiduePDEC
chosen_parallel_signed_target=SourceKeyedMobiusVonMangoldtTraceTypeIIFamily
chosen_parallel_distribution_target=PointwiseThetaPsiCOneInputAtSqrtRowScale
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `d2de4e9375983aa24acb2f99961d3e9af7ebb174af8405a24ce87c50192beb72` |
| `docs/monograph/external-theorem-index.md` | `4f91cb59775b3bb9159b5caa684e14589f9daf8ece7820ec7acff408136294e8` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `2bd303074576fb83b80617bf786a8a5e2edbc10ea009a36354da63faf266705a` |
| `docs/monograph/prime-matrix-external-frontier-theorem-stress-router.json` | `3a8f50d512a77ad9eeb8f113226fd0e1c3e33e6637b4accec90f77f381195780` |
| `docs/monograph/prime-matrix-phi-lpf-fixed-wheel-residual-rough-composite-audit.json` | `222183794d5de930940980e7b616f7ddda3ccde6bdff782a6d5c8aa22e6d9f5a` |
| `docs/monograph/prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json` | `74636f1bc6c8e7088a213b0df5440bf93aadb10482989dca7615eb4edaaf3f06` |
| `docs/monograph/prime-matrix-phi-lpf-parity-barrier-transport-edge-sync-router.json` | `de0f3fdf91e7b571cdf60a07c2457cf1ec36255ae1367a59b2f725b028ed4f5e` |
| `docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-wheel30-capacity-router.json` | `2ec71522b5e0e82fb2f420c5322dd66ad72814be1174acff8f373ac4b00b0393` |
| `docs/monograph/prime-matrix-phi-lpf-row-delta-phi-cover-contract-router.json` | `234ad3d23afb443ae53e5b0faf095f0621e38614b737de87b541a6b194da0cdd` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `cf76ee4bfa3c32e162ead42e6fc533591a75b0d0305603b6e04316440c660324` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `6c0cfbd11405ad4d29f672216704353c9e026861d252efedd119030c809ab88b` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `daa9a19b44baa1af02d578f3a477ae9e1415a6a9a364eca1b84a2c64a6735821` |
| `experiments/prime_matrix_phi_lpf_row_inequality_breakthrough_frontier_router.py` | `9d6228461a6c5ab4c12e0460c20bf0a8319b0b612f7a532009908f0a61d95740` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `e32e76d64059e73e203116ddbef24fb0a48de9b704284f8618b38cf15ddf60ed` |
