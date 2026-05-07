# FO-PDEC physical/primitive 二点 tautology 审计

**状态：** `physical_primitive_pdec_threshold_degenerates_to_two_point_tautology`

物理去重后当前 factor=199 前沿只剩两个物理候选。模素数上任意两个不同残基都可由某个 非零频率送成相邻对偶点，从而 Fourier 达到 2*cos(pi/ell)。因此 U_CRT < 1.9997507790353146 不是可攻的 PDEC 缺陷阈值，而是二点 Fourier tautology。 当前分支应转入 SAE/Endpoint，除非未来出现至少三点且同一 formal unit 的 primitive PDEC 家族。

## 1. 子门裁定

```text
closed_subgate: PhysicalPrimitivePDECThresholdDegeneratesToTwoPointTautology
factor: 199
physical_event_count: 2
two_point_tautology_bound: 1.9997507790353146
all_residue_choices_are_two_point_tautology: true
ambiguous_phase_event_count: 1
```

## 2. 物理原子

| candidate | factor | multiplicity | residues | semiprime | offset | q layers |
| ---: | ---: | ---: | --- | --- | --- | --- |
| 250541 | 199 | 2 | [61, 126] | [250517] | [24] | [773, 967] |
| 1664237 | 199 | 2 | [40] | [1664207] | [30] | [1993] |

## 3. 残基选择审计

| chosen residues | h | dual residues | Fourier | tautology bound |
| --- | ---: | --- | ---: | ---: |
| [61, 40] | 180 | [35, 36] | 1.999750779035 | 1.999750779035 |
| [126, 40] | 118 | [142, 143] | 1.999750779035 | 1.999750779035 |

## 4. 证明读法

若模数 `ell` 为素数，两个不同残基 `a,b` 的差 `b-a` 可逆。取

\[
h\equiv (b-a)^{-1}\pmod \ell，
\]

则 `ha` 与 `hb` 在对偶圆周上相邻，故

\[
\max_{h\ne0}|e(ha/\ell)+e(hb/\ell)|=2\cos(\pi/\ell)。
\]

所以二点 physical/primitive Fourier 近质量上界不是异常，而是恒等现象。PDEC 必须捕捉持久偏斜；当前只有两个物理原子的分支应作为稀疏局部对象进入 SAE/Endpoint。

## 5. 剩余

- `SAE/Endpoint absorption for the two physical primitive atoms`
- `future primitive PDEC only if a same-formal-unit family has at least three non-tautological physical atoms or extra constraints`
