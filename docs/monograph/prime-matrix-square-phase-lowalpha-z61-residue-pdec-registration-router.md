# Prime Matrix square-phase low-alpha z=61 Residue-PDEC 登记

**状态：** `z61_singleton_residue_pdec_registered_not_excluded`

Singleton residue gate 分支已登记成三个短残基 PDEC 对象：一条负记录、两条正记录。登记闭合的是失败对象的形式化；仍需排斥 Residue-PDEC，或证明 singleton residue signed count balance。

```text
residue_pdec_registration_closed=true
negative_record_count=1
positive_record_count=2
residue_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. Residue-PDEC Records

| sign | quotient | p | q | a | b | modulus | residue | delta |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `negative` | 1 | 36739 | 53 | 883 | 28842 | 1528626 | 1505989 | 22637 |
| `positive` | 2 | 200003 | 71 | 9767 | 57684 | 4095564 | 3921985 | 173579 |
| `positive` | 4 | 200003 | 37 | 9371 | 115368 | 4268616 | 4268089 | 527 |

## 2. 证明边界

- 已闭合：短残基失败对象的正式登记。
- 未闭合：Residue-PDEC 排斥，或 singleton residue signed count balance。
- 下一目标：`ResiduePDECExclusionOrSingletonResidueSignedCountBalance`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-singleton-residue-gate-router.json` | `fea2eedf1322b16fc049dbd61e9afd30ca2b28459dff222cf2e25e28656d499f` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_residue_pdec_registration_router.py` | `647fa163725dc19e2969e3ef857ad547fb74b9b07444680048bf4f4124b6847e` |
