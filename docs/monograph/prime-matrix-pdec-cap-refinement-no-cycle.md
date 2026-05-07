# PDEC cap 细化无循环引理：有限签名群内不能无限分裂

**状态：** `pdec_cap_refinement_no_cycle_reduction_not_exit_exclusion`

本文承接 `prime-matrix-pdec-dual-failure-absorption-contract.md`。上一层说明：

```text
PDEC-Dual-Cert 失败
=> Fourier 方向帽 C_alpha 中有强质量集中
=> sparse cap / persistent cap / Column cap / Multiplicity-Stitching。
```

仍需排除一个逻辑疑问：persistent cap 是否会不断生成 refined PDEC，导致无限分支？
本文证明：在固定有限签名群内，cap 细化不能无限循环；若签名群不断提升，则它已经是
`new-layer PDEC / ColumnCRT / CleanKLS` 的既有出口。

## 1. 固定签名群的分区势函数

固定有限签名群 `G`。一系列 cap 细化给出集合族

```text
C_1,C_2,...,C_n subset G。
```

令 `B_n` 为这些集合生成的 Boolean algebra，`At(B_n)` 为其原子分区。定义：

```text
rank_n = |At(B_n)|；
max_atom_mass_n = max_{A in At(B_n)} g(A)；
unresolved_atoms_n = {A: A 仍承载 persistent defect}。
```

每次新的 cap 若不是由旧分区可测，就严格细分至少一个原子，因此

```text
rank_{n+1}>rank_n。
```

由于 `rank_n<=|G|`，这种严格细分最多发生 `|G|-1` 次。

## 2. 可测 cap 的归宿

若新 cap 已经是 `B_n` 可测，则它只是旧原子的并集，不产生新结构。此时有三种情况：

```text
1. cap 质量稀疏
   => SAE；

2. cap 质量集中在少数旧原子
   => 取这些原子作为更小坏窗集合，进入 explicit/refined PDEC；

3. cap 横跨许多旧原子但每个原子低负载
   => 对偶上界可按原子容量求和；若仍失败，必有某个原子或原子簇承担失败。
```

所以可测 cap 不会生成新自由度；它只把责任下推到旧原子或给 SAE。

## 3. 终止原子

当不能继续严格细分时，persistent 质量位于某些固定原子中。每个原子等价于有限个签名条件：

```text
chi_{h_i}(a) 落在给定 cap/反 cap；
低模相位属于固定 cell；
列位移或端点 seam 标签固定。
```

若原子大小为 `1`，签名完全钉扎：

```text
singleton atom => fixed residue/phase/column displacement
               => ColumnCRT or explicit PDEC row。
```

若原子大小大于 `1`，但所有允许 Fourier 方向在该原子上都不能继续切分，则残余在该原子内部
对当前签名系统不可分辨。此时只有两种合法归宿：

```text
内部平坦 => Clean local KLS / 对偶上界成立；
内部仍有非零频率 => 新 cap 切分原子，矛盾于终止。
```

## 4. 升轮层的处理

若为了继续切分必须把 `G` 提升为更大签名群 `G'`，例如从 `W` 提升到 `Wr`，则这不是同层循环。
它正是层叠轮筛的二分：

```text
新层频率持续同步
  => new-layer PDEC / ColumnCRT；

新层能量高维分散
  => DLS/KLS/CleanKLS。
```

因此允许无穷层叠，但不允许无名循环：每次升层必须产生新层命名缺陷或分散吸收输入。

## 5. 形式化结论

**PDEC-Cap-NoCycle.**
固定有限签名群 `G` 与同一坏窗口径 `g`。从任意 PDEC 对偶失败出发，反复执行
`cap localization -> refined PDEC`，则有限步内必进入以下之一：

```text
SAE；
ColumnCRT / singleton explicit PDEC；
同层 PDEC-Dual-Cert 成功；
Multiplicity/Stitching 口径义务；
提升到新签名层 G'，并进入 new-layer PDEC 或 CleanKLS。
```

因此 `PDEC` 失败细化本身不能无限制造无名出口。

## 6. 当前闭合边界

本文完成：

```text
固定 G 内 refined PDEC 不能无限循环；
升层分支必须回到 new-layer PDEC / ColumnCRT / CleanKLS。
```

本文未完成：

```text
singleton explicit PDEC 的全部排斥；
new-layer PDEC 的全部 U_CRT<L_PDEC；
SAE/ColumnCRT/CleanKLS 的最终证明。
```

所以当前主链变成：

```text
PDEC failure
=> cap concentration
=> finite cap refinement
=> SAE / ColumnCRT / explicit PDEC / new-layer PDEC / CleanKLS。
```

这继续压缩了递归结构，但仍不是最终无条件行命题证明。

## 7. New-layer 塔熵合同

新增 `prime-matrix-newlayer-pdec-tower-entropy-contract.md` 后，`提升到新签名层 G'` 也不再是开放塔。
沿 `G_0<G_1<G_2<...`，每层新增 fiber/cap 偏斜都有相对熵成本

```text
H_{n+1}=sum_A g_n(A)/M * sum_b p_A(b) log(p_A(b)/mu_A(b))。
```

若这些成本发散，则有限截断层或 profinite 极限给出 global `PDEC/ColumnCRT`；若成本可求和，
则新增层偏斜趋零，进入 `CleanKLS/DLS`。若层间口径不一致，则回到 `Multiplicity/Stitching`。
因此 new-layer PDEC 塔也不能保持无名。
