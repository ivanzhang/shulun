# Triad-A1 Q=30030 LHB LP 骨架

**状态：** `lp_skeleton_materialized_dual_comparison_open`

LHB 分支现在已有机器可读的 g(t)<=M(t) 行生成器和 WHOLEDEF/BRIDGED 零容量行。这些行只能闭合强制支撑落在零容量块内的 PDEC 方向。由于仍存在非零 M 相位，仅靠 box 容量不能证明全局 Fourier 抵消；下一证明义务是带有额外结构行的 theta 级 LP/对偶证书。

## 1. 证书语义

所有行都作用在同一个 LHB-typed 坏窗推前计数 g(t) 上。使用这些行必须先证明 S subset Z_LHB(p,Q)。

本骨架只生成同一 `g(t)` 上的合法行生成器；它不声称已经完成 `U_CRT<L_PDEC`。

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `lp_skeleton_script` | `3c4617e3b0b37b769216569a0c89b5e97c5ed0d7b3fde5d95173c7ee9ada38fb` |
| `multiplicity_cap_json` | `c62dea9f85ebdf6fb69eb9870b0a4e4af89dd88ac696a2247b48dd22c4a4bbba` |
| `phase_blocks_json` | `2996d4f60e0bf882beda51076c457d2163d340cc62ce0005e356720e3a503ea2` |

## 3. P 列表摘要

| P | total M | nonzero M phases | zero M phases | max M | WHOLEDEF bound | BRIDGED bound | box-only obstruction |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 17 | 28 | 28 | 30002 | 1 | 0 | 0 | phase 1211 has M=1 |
| 19 | 496 | 368 | 29662 | 17 | 0 | 0 | phase 111 has M=1 |
| 23 | 3456 | 936 | 29094 | 35 | 0 | 0 | phase 59 has M=2 |
| 29 | 6416 | 610 | 29420 | 112 | 0 | 0 | phase 199 has M=6 |

## 4. 已闭合行

对每个列出的 `P`，以下行已经可在 LHB-typed 且 `S subset Z_LHB` 的分支中使用：

```text
g(t)>=0；
g(t)<=M_p(t)；
sum_{t in WHOLEDEF} g(t)<=0；
sum_{t in BRIDGED} g(t)<=0。
```

因此若某个 PDEC 方向强制坏相位完全落在 `WHOLEDEF union BRIDGED` 中，该分支直接空。

## 5. 新发现的阻断点

只靠 `g(t)<=M(t)` 不能推出全局 Fourier 抵消：只要存在 `M(t)>0`，单相位支撑就是 box-only 可行解，
其非零频率 Fourier 模长等于质量本身。因此下一步不能继续调常数，必须补入以下结构行之一：

```text
PDEC 方向支撑相对 M(t) 的限制；
column/displacement 相位兼容行；
tail/cofactor nonreuse 行；
direction-arc dual certificate。
```

## 6. 当前结论

LHB 分支已经从文档骨架推进为机器可读 LP 骨架；但完整 `U_CRT<L_PDEC` 仍未提交。
