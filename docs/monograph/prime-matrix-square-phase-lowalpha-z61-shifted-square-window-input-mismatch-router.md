# Prime Matrix square-phase low-alpha z=61 shifted-square-window input mismatch

**状态：** `z61_shifted_square_window_input_not_supplied_by_registered_standard_routes_open`

当前缺口需要的不是一般短区间素数或单个线性型素数，而是同步移位线性素数对 `a4=71s-1,a2=74s-1` 与同一个 `p` 的平方窗口同余同时成立。仓库内登记的标准路线都没有给出这个形状；若不新增该 companion theorem，就只能转向命名 PersistentPhase-PDEC 排斥。

```text
registered_standard_route_matches_required_shape=false
new_shifted_square_window_companion_theorem_proved=false
persistent_phase_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 所需输入形状

| field | value |
| --- | --- |
| linear prime pair | `{'a4': '71*132-1', 'a2': '74*132-1'}` |
| same-p | `200003` |
| square congruence | `p^2 ≡ -527 mod 57684` |
| endpoint window | `delta + M*span <= p-1 < delta + M*(span+1)` |
| recovered s | `132` |

## 2. 定理形状匹配

| candidate | matches | reason |
| --- | --- | --- |
| `single_short_interval_prime` | `False` | 只能给某短区间内至少一个素数；不同时给出 `a4=71s-1` 与 `a2=74s-1` 两个素数，也不控制 square-window 同余。 |
| `dirichlet_one_linear_form` | `False` | 只能处理单个等差数列中的无限素数；不提供两个同步线性型同时为素数。 |
| `bounded_prime_gaps_maynard_type` | `False` | 可给某些可容许组中至少两个素数，但不指定必须是这两个线性型，也不附带当前平方窗口锁定。 |
| `hardy_littlewood_prime_pair_or_dickson_input` | `formally_close_if_available` | 若另行接受足够强的同步线性素数对加 square-window 版本，可闭合该输入；仓库内没有该已证输入。 |

## 3. 证明边界

- 已闭合：所需外部/内部输入的精确形状已经固定。
- 未闭合：新增 shifted-square-window companion theorem，或排斥 PersistentPhase-PDEC。
- 结论：当前没有可直接调用的已登记标准路线完成无条件闭合。
- 下一目标：`NewShiftedSquareWindowCompanionTheoremOrPersistentPhasePDECExclusion`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-companion-boundary-router.json` | `69fbf839066d2ff7d7c34bd7086a1e59342099c780be06c3a5e04549098847d6` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json` | `57d4e18eadd1bb072db598f782533b7ecefc942472cc8f26d9f0a285e97ad40e` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json` | `26ed4354b18ce54dc2ea66ce943e628fc02f80cacee97084cc3331a15cd17b83` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_shifted_square_window_input_mismatch_router.py` | `4bfc71bc8ce44aa96dd2cbfdd8b3c0159ef4f901b6715bdf94142dfd4adbec4f` |
