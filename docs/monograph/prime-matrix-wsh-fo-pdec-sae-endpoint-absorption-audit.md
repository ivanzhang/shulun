# FO-PDEC 二点原子的 SAE/Endpoint 本地吸收审计

**状态：** `audited_two_physical_primitive_atoms_absorbed_by_local_survivor_witnesses`

当前 physical/primitive PDEC 只剩两个物理原子；二点 Fourier 阈值已退化为恒等式。把这两个原子送入 SAE/Endpoint 后，审计发现每个关联固定偏移纤维都有本地素数见证，且 factor=199 在每个纤维内负载至多为 1。因此当前有限二点分支被 LocalSurvivor 见证吸收；这关闭的是已审计样本子门，不是完整 LocalSurvivor/PDEC 终端全集。

## 1. 子门裁定

```text
input_subgate: PhysicalPrimitivePDECThresholdDegeneratesToTwoPointTautology
closed_subgate: TwoPhysicalPrimitiveAtomsAbsorbedByLocalSurvivorWitnesses
physical_atom_count: 2
source_row_count: 4
unique_fixed_offset_fiber_count: 4
all_sources_have_local_survivor_witness: true
all_factor_199_fibers_are_sparse_load_one: true
```

## 2. 吸收行

| atom | block | q | row | offset | residue | primes in fiber | missing | factor199 load | witness primes | route |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 250541 | 2 | 773 | 325 | 24 | 126 | 1 | 3 | 1 | [250543] | LocalSurvivorWitnessInSameFixedOffsetFiber |
| 250541 | 3 | 967 | 260 | 24 | 61 | 1 | 3 | 1 | [250543] | LocalSurvivorWitnessInSameFixedOffsetFiber |
| 1664237 | 1 | 1993 | 836 | 30 | 40 | 1 | 4 | 1 | [1664227] | LocalSurvivorWitnessInSameFixedOffsetFiber |
| 1664237 | 4 | 1993 | 836 | 30 | 40 | 1 | 3 | 1 | [1664227] | LocalSurvivorWitnessInSameFixedOffsetFiber |

## 3. 证明读法

二点 primitive Fourier 信号不能作为 PDEC 排斥阈值后，剩余对象必须改按稀疏孤窗处理。
对每个来源行，若同一固定偏移纤维中存在素数候选，则该纤维不是全覆盖零窗；这个素数候选就是
`LocalSurvivorCert` 的 witness。若 witness 不存在，才需要继续生成更细的 SAE/Endpoint 证书。

本审计中所有来源行都有 witness prime，且 `factor=199` 在每个纤维内都是负载 `1` 的稀疏标签，
所以当前两个物理原子不能继续作为终端 PDEC/SAE 障碍。

## 4. 剩余

- `global LocalSurvivorCert family for unaudited sparse windows`
- `future primitive PDEC only for at least three non-tautological physical atoms or an extra fixed-frequency constraint`
- `CleanKLS/DLS and D-structure/Rankin referee inputs for the full row-column theorem`
