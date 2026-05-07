# Triad-A1 DI/BFI Maynard S-compression barrier 路由器

**状态：** `maynard_s_common_inverse_direct_identification_rejected_open`

朴素把共同逆元窗口 S 当作 Maynard 的 S_May 已被指数锥排除；当前硬点变为证明 Maynard-S 压缩映射，或给出替代 W4 对象路由。

## 1. 结构律

The Maynard exponent cone forces s <= (2-q)/5. With the current level q=1/2+o(1), S_May must have exponent at most 3/10-o(1). Therefore the common inverse window S_common≈P=X^(1/2) cannot be identified with S_May. A genuine S-compression map or an alternate W4 object route is required.

```text
previous terminal:
  CurrentWFDW4ObjectTranslationMatrixAdmission;

forced exponents:
  q=1/2+o(1);
  S_common=1/2+o(1);
  S_May<=3/10-o(1);

new terminal:
  MaynardSCompressionMapOrAlternateW4Rerouting;
```

## 2. 汇总

- `s_compression_barrier_closed=false`。
- `closed_barrier_gates=['PriorTranslationMatrixFrontierAvailable', 'QExponentPinnedAtHalf', 'CommonInverseSExponentPinnedAtHalf', 'MaynardSUpperBoundFromCone', 'NaiveCommonSToMaynardSRejected']`。
- `open_barrier_gates=['MaynardSCompressionMap', 'AlternateW4ObjectRerouting']`。
- `terminal_gap_after_router=MaynardSCompressionMapOrAlternateW4Rerouting`。

## 3. 障碍账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorTranslationMatrixFrontierAvailable` | `true` | 上游已经把 Maynard 翻译压成 WFD 对象等式、WFD 指数向量和线性矩阵。 | none at prior-frontier level | `NaiveCommonSToMaynardSRejected` |
| `QExponentPinnedAtHalf` | `true` | X≈P^2 且 Q<=P log^O P，故 q=x_Q=1/2+o(1)。 | 若后续改用更小 Q_May，需要另建 q<1/2 的翻译行。 | `MaynardSUpperBoundFromCone` |
| `CommonInverseSExponentPinnedAtHalf` | `true` | 共同变量表/KE-13 逆元窗口为 S_common≈P=X^(1/2+o(1))。 | 该 S_common 不能未经压缩直接当作 S_May。 | `NaiveCommonSToMaynardSRejected` |
| `MaynardSUpperBoundFromCone` | `true` | 由 n+2r+5s+q<=2 和 n,r>=0 得 s<=3/10+o(1) when q=1/2。 | none at cone-inequality level | `NaiveCommonSToMaynardSRejected` |
| `NaiveCommonSToMaynardSRejected` | `true` | S_common exponent=1/2 exceeds Maynard cone bound 3/10；直接同一化矛盾。 | 必须给出 S 压缩映射或改走另一对象路由。 | `MaynardSCompressionMapOrAlternateW4Rerouting` |
| `MaynardSCompressionMap` | `false` | 需要从当前 s1,s2/h/completion 结构中抽出真实 S_May<=X^(3/10-o(1))。 | 尚无压缩映射；这是真实新硬点。 | `MaynardSCompressionMapOrAlternateW4Rerouting` |
| `AlternateW4ObjectRerouting` | `false` | 若无法压缩 S_May，则必须证明当前 WFD 非对角对象进入另一已登记可闭合 dispersion 原子。 | 尚未给出替代对象路由。 | `MaynardSCompressionMapOrAlternateW4Rerouting` |

## 4. 当前结论

当前最窄尺度侧剩余变为：

```text
MaynardSCompressionMapOrAlternateW4Rerouting:
  MaynardSCompressionMap;
  AlternateW4ObjectRerouting.
```

这一步关闭的是朴素变量同一化退路，不是最终命题闭合。
