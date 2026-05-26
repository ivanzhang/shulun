# Prime Matrix Phi-LPF row inequality target residue-cover 路由

**状态：** `target_row_residue_cover_standard_form_synced_open`
**核验日期：** `2026-05-26`

行级严格不等式不能推广为任意短区间命题；普通短区间存在 Delta-Phi full-cover 等号。目标必须限制在 Prime Matrix punctured 行 R_{P,k}。在该行上，失败态等价于小素因子同余类 D_p(P,k) 覆盖全部 offset。下一步最快的非循环攻击不是再做无符号计数，而是从 full-cover equality 中抽取命名 owner-residue PDEC，或把 Mobius/trace 签名求和接到同一 residue-cover 标准形上。

```text
target_row_residue_cover_standard_form_synced=true
generic_interval_uniform_defect_false=true
target_punctured_row_full_cover_found_in_scan=false
strict_cover_inequality_proved_uniformly=false
row_column_unconditional_closed=false
```

## 1. 不能推广到任意短区间

| interval | length | Delta-Phi cover | primes | full cover equality | owner buckets |
| --- | ---: | ---: | ---: | --- | --- |
| `(90,96]` | 6 | 6 | 0 | `true` | `{'2': [92, 94, 96], '3': [93], '5': [95], '7': [91]}` |
| `(114,126]` | 12 | 12 | 0 | `true` | `{'2': [116, 118, 120, 122, 124, 126], '3': [117, 123], '5': [115, 125], '7': [119], '11': [121]}` |
| `(200,210]` | 10 | 10 | 0 | `true` | `{'2': [202, 204, 206, 208, 210], '3': [201, 207], '5': [205], '7': [203], '11': [209]}` |

## 2. 目标 punctured 行有限扫描

| P | rows scanned | min primes | min-k | max primes | zero rows |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 31 | 30 | 2 | 25 | 7 | 0 |
| 101 | 100 | 7 | 73 | 20 | 0 |
| 251 | 250 | 18 | 108 | 41 | 0 |
| 499 | 498 | 29 | 362 | 73 | 0 |
| 1009 | 1008 | 52 | 905 | 137 | 0 |

有限扫描只定位结构，不作为全局证明。

## 3. residue-cover 标准形

| object | formula | meaning |
| --- | --- | --- |
| `target row` | `R_{P,k}={kP+r:1<=r<=P-1}, 1<=k<=P-1` | 目标行端点低于 P^2，因而任何合数都有最小素因子 < P。 |
| `coarse divisor fiber` | `D_p(P,k)={r: 1<=r<=P-1, r == -kP mod p}` | p<P 时 P 可逆，斜线/圆柱 residue fiber 是一个确定同余类。 |
| `LPF owner fiber` | `O_p(P,k)=D_p(P,k) minus union_{q<p}D_q(P,k)` | 按最小素因子分桶后的 owner fiber 两两不交。 |
| `row prime count` | `pi(R_{P,k})=#[1,P-1] minus union_{p<=sqrt((k+1)P-1)}D_p(P,k)` | 未被任何小素因子同余类覆盖的 offset 必为素数。 |
| `full-cover equality` | `union_p D_p(P,k)=[1,P-1]` | 这是行级严格不等式失败的 residue-cover 形式，也是 PDEC/SAE 的唯一可攻等号态。 |

## 4. 下一层非循环接口

| name | statement | status | noncircular requirement |
| --- | --- | --- | --- |
| `TargetPuncturedRowResidueCoverDefect` | `union_{p<=sqrt((k+1)P-1)}D_p(P,k) != [1,P-1]` | open; equivalent to target row prime positivity if used alone | prove a structural obstruction to full cover that is not just a restatement of primality |
| `FullCoverOwnerResiduePDEC` | `full cover => named incompatible owner-residue/phase packet` | open; selected next primary target | extract a forbidden CRT/phase packet from the equality case before invoking prime existence |
| `MobiusResidueCoverSignedTrace` | `sum_{d\|Q} mu(d) N_d(P,k)>0 with controlled source-key error` | open | obtain cancellation in the signed divisor sum at row length P, not just Euler-product density |
| `SpectralKloostermanResidueLift` | `complete the kP+r residue fibers into a uniform trace family` | open | supply conductor/coefficient control for q-spine/hinge source keys |

## 5. 外部输入尺度边界

| input | scale at x=P^2 | row thickness | status | source |
| --- | --- | --- | --- | --- |
| Guth--Maynard / Hieu | `P^(17/15)` | `P^(2/15)` | unconditional/preprint scale still thicker than one target row | https://arxiv.org/abs/2405.20552 and https://arxiv.org/abs/2509.04883 |
| Runbo Li Harman-sieve short intervals | `P^(26/25)` | `P^(1/25)` | unconditional/preprint scale still thicker than one target row | https://arxiv.org/abs/2308.04458 |
| Harm conditional short AP refinement | `P*exp((2log P)^alpha), alpha>2/3 under GDH` | `exp((2log P)^alpha)` | conditional and still super-one-row; useful as near-critical boundary, not a closure input | https://arxiv.org/abs/2507.15334 |

## 6. 下一手

```text
selected_primary_next_gate=FullCoverOwnerResiduePDEC
selected_signed_parallel_gate=MobiusResidueCoverSignedTrace
selected_spectral_parallel_gate=SpectralKloostermanResidueLift
```

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `6180a3b1a548942367f2cf9ef1699f91fd48d110a7dd876d96a7ff3a6319d7dc` |
| `docs/monograph/external-theorem-index.md` | `9db6409144a63528bceffd5305f47b74d0a48fe4b010b35e1e58825a2b61f1b3` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `f306fe5c67ba8f71fb21202397f777089eb190fa3883b9f9abcb626b316adcc8` |
| `docs/monograph/prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json` | `74636f1bc6c8e7088a213b0df5440bf93aadb10482989dca7615eb4edaaf3f06` |
| `docs/monograph/prime-matrix-phi-lpf-parity-barrier-transport-edge-sync-router.json` | `de0f3fdf91e7b571cdf60a07c2457cf1ec36255ae1367a59b2f725b028ed4f5e` |
| `docs/monograph/prime-matrix-phi-lpf-row-delta-phi-cover-contract-router.json` | `234ad3d23afb443ae53e5b0faf095f0621e38614b737de87b541a6b194da0cdd` |
| `docs/monograph/prime-matrix-phi-lpf-row-inequality-breakthrough-frontier-router.json` | `93b9420810fe6a699bb79d3591e65e1e3f6077e3d0c94e37842649ed8a3bfb32` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `c68973fa30142137c121ab269fbe7495012495f26d4e94f9d383d3c87293ab6e` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `53e9ffbe3f4de355ba86ad4d29aacde8add8ee454f22bcb3ca2117b9c77bc8d6` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `e731c49ebe43dd35676534e372b9934f1b69c6d61a56ed0593cb25dc410a58ca` |
| `experiments/prime_matrix_phi_lpf_row_inequality_target_residue_cover_router.py` | `3ead605b5a6a6fac8d2889cc481b50245678d4777cd754e25ae6fa7bb291b687` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `472eebac8bbfbb1c5dc398fd643d076baf77bfcbbd08744f74c4387d73be95e7` |
