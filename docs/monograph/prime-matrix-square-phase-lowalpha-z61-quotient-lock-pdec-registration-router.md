# Prime Matrix square-phase low-alpha z=61 QuotientLock-PDEC registration

**状态：** `z61_unique_quotient_lock_pdec_registered_not_excluded`

唯一精确商锁已登记为固定核心 QuotientLock-PDEC：同模板失败不再有参数自由度，只能是 `core=4807=11*19*23`、`q4=37`、`q2=71`、`M=57684` 这一对象。这完成失败对象登记，但尚未排斥该固定核心。

```text
quotient_lock_pdec_registration_closed=true
fixed_core_candidate_unique=true
fixed_core_m_residue_sources_closed=true
quotient_lock_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. PDEC 对象

| field | value |
| --- | --- |
| formal unit | `z61|bucket=unbalanced<=8|omega=4|shell=(8D,16D]|core=4807|factors=11,19,23|q4=37|q2=71` |
| core | `4807=[11, 19, 23]` |
| modulus | `57684` |
| q4/q2 | `37, 71` |
| elimination | `b=(2*a-117)/(a^2-126)` |

## 2. 商锁

| side | equation | left | right | quotient |
| --- | --- | ---: | ---: | ---: |
| q4 | `a*c+6=7*(2*b-1)` | 259 | 259 | 7 |
| q2 | `a*b+4=3*(3*c+2)` | 213 | 213 | 3 |

## 3. 残差源复核

| modulus | residue | expected |
| ---: | ---: | ---: |
| 37 | 1 | 1 |
| 71 | 32 | 32 |

## 4. 证明边界

- 已闭合：QuotientLock-PDEC 的失败对象登记，并证明同模板只有一个固定核心候选。
- 未闭合：对该固定核心做独立排斥检查，或证明全局模板界。
- 下一目标：`QuotientLockPDECExclusionByFixedCoreCheckOrGlobalTemplateBound`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-quotient-lock-router.json` | `abbde832ff4cea92c7e3cbec2f0ce7436b8e8d7d51670c8ab220c6eddb92bce5` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_quotient_lock_pdec_registration_router.py` | `d7691e7d40a6c150323a74be1a6fca871b80307e5e61d57f7584fc894f230192` |
