# Prime Matrix square-phase low-alpha z=61 Residue signed absorption

**状态：** `z61_registered_residue_pdec_locally_absorbed_global_balance_open`

已登记的三条 Residue-PDEC 记录在当前 formal unit 内不是净负缺陷：每条记录权重相同，一条负记录由两条正记录吸收，净计数为 `+1`。这闭合的是本地样本 formal unit 的负缺陷吸收；全局仍需证明 residue signed count balance，或排斥未吸收 Residue-PDEC。

```text
constant_unit_weight_closed=true
unit_weight=0.555427
positive_record_count=2
negative_record_count=1
signed_count=1
signed_weight=0.555427
local_negative_residue_pdec_absorbed=true
global_residue_signed_count_balance_proved=false
row_column_unconditional_closed=false
```

## 1. 有符号记录

| sign | quotient | p | q | b | modulus | residue | signed weight |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `negative` | 1 | 36739 | 53 | 28842 | 1528626 | 1505989 | -0.555427 |
| `positive` | 2 | 200003 | 71 | 57684 | 4095564 | 3921985 | 0.555427 |
| `positive` | 4 | 200003 | 37 | 115368 | 4268616 | 4268089 | 0.555427 |

## 2. 证明边界

- 已闭合：当前 formal unit 的本地负 Residue-PDEC 被同权正记录吸收。
- 未闭合：全局 Residue signed count balance，或未吸收 Residue-PDEC 排斥。
- 下一目标：`GlobalResidueSignedCountBalanceOrUnabsorbedResiduePDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-quotient-ladder-router.json` | `e643292f87a63f8164b083991c9166f865e6e1b499dc6a3a9817cf6fd9364387` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-residue-pdec-registration-router.json` | `2ab4df83bf7ddb99382517bc30865d6751f85029883c7bb40e5f593187fd871d` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_residue_signed_absorption_router.py` | `65f9ab21e980ef19a5b7e83efcb280b2535b69624438b7319d92a3ba96eae081` |
