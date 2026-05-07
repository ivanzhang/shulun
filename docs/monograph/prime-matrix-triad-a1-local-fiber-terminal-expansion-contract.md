# Triad-A1 局部 Fiber 终端展开合同

**状态：** `local_fiber_terminal_expansion_contract_open_global_certificates`

本文把当前三类已物化动作统一成一个一般接口：

```text
PhaseResidue 完整 CRT 终端审计；
NoNext ProfiniteObligation 局部解析；
BoundaryTerminal LocalSurvivor 排除。
```

核心原则是：若只关心某个相位原子 `u mod Q` 的终端行，没必要先生成整层后继 `m_vector`。只需在
`u` 的剩余高素 CRT fiber 内局部枚举，就能判断该原子是否会产生前 `P` 行零行，或把它路由为远处
finite/profinite PDEC packet。

## 1. 全周期行集合

令

```text
B_P = prod_{ell<P} ell。
```

第 `r` 行是否为完整小素因子覆盖零行，只依赖 `r mod B_P`，因为对每个 `ell<P`，

```text
(r-1)P+c mod ell
```

只依赖 `r mod ell`，且 `P` 与 `ell` 互素。

记完整终端行残基集合为

```text
C_P subset Z/B_P Z。
```

若 `Q|B_P`，则某层相位质量可写成投影计数

```text
M_Q(u)=#{R in C_P: R=u mod Q}。
```

## 2. 局部 fiber 展开

设

```text
R_Q={ell<P: ell 不整除 Q},
B_Q=prod_{ell in R_Q} ell。
```

因为 `Q` 与 `B_Q` 互素，所有投影到 `u mod Q` 的全周期代表可写成

```text
w = u + yQ,  0<=y<B_Q。
```

于是局部展开计数为

```text
E_Q(u)=#{y mod B_Q: u+yQ in C_P}。
```

**LFTE-1（质量恒等式）。**
若 `M_Q` 与 `C_P` 采用同一 formal unit，则

```text
E_Q(u)=M_Q(u)
```

对每个相位 `u` 成立。

证明：`Z/B_P Z -> Z/QZ` 的 fiber 正是 `u+yQ (mod B_P)`，大小为 `B_Q`。`M_Q(u)` 按定义数
`C_P` 在该 fiber 中的元素，和 `E_Q(u)` 相同。

## 3. 早期出口判据

定义该原子的终端行集合

```text
T_Q(u)={positive representative of u+yQ: u+yQ in C_P}。
```

这里若残基 `u+yQ` 等于 `0 mod B_P`，正代表按 `B_P` 处理；因此它自动大于 `P`，不会形成早期行。

若

```text
min T_Q(u)>P，
```

则相位原子 `u` 不能产生前 `P` 行零行。

当 `Q>P` 时，前 `P` 行判据可进一步降为边界判据：

```text
u not in [1,P]      => 自动 >P；
u in [1,P] 且 y=0 不完整
                    => 全部完成态从 u+Q 开始，自动 >P；
u in [1,P] 且 y=0 完整
                    => 真实早期零行硬点。
```

这就是 `BoundaryTerminal LocalSurvivor` 引理在完整 CRT fiber 语言中的版本。

## 4. 无整层 m_vector 接口

对任意相位原子 `(P,Q,u,expected_mass)`，可执行：

```text
LocalFiberTerminalExpansion:
  1. 检查 Q|B_P；
  2. 枚举 R_Q 与 y mod B_Q；
  3. 对 w=u+yQ 检查 w in C_P；
  4. 核验 count == expected_mass；
  5. 若所有 positive w >P，早期出口关闭；
  6. 若存在 w<=P，交给 BoundaryTerminal/LocalSurvivor 或真实反例矛盾。
```

这个接口的优点是局部性：即使下一层 `Q'=rQ` 或完整 `B_P` 很大，也不必生成所有相位的质量向量；
只要当前证明分支抽出了一个原子，就能局部追踪到底。

## 5. 当前物化实例

已有文件正是该合同的三个实例：

```text
prime-matrix-triad-a1-phase-residue-full-crt-terminal-audit.md:
  已有下一层数据的 12 个原子；
  all_terminal_phases_gt_p=True；
  all_terminal_phases_gt_p2=True。

prime-matrix-triad-a1-no-next-profinite-obligation-resolver.md:
  无下一层 m_vector 的 24 个原子；
  all_mass_identities_hold=True；
  all_terminal_phases_gt_p=True。

prime-matrix-triad-a1-all-phase-residue-terminal-audit.md:
  当前 Q=30030,510510 的全部非零相位；
  total_nonzero_phase_count=5030；
  all_phase_mass_identities_hold=True；
  total_terminal_le_p_count=0。
```

再加上 `BoundaryTerminal LocalSurvivor` 审计：

```text
Q=2310,30030,510510；
total_y0_completion_le_p_count=0；
all_phase_le_p_have_local_survivor=True。
```

当前已物化层的结论可统一写成：

```text
所有已抽出的 phase/fiber 原子
=> 质量恒等式成立；
=> 终端行全部 >P；
=> 不能产生 P 行以内零行。
```

## 6. 对无穷层的作用

该合同给无限升层提供一个“不迷失”的递归动作：

```text
若分支抽出具体 phase atom：
  用 LocalFiberTerminalExpansion 追到底；

若只给出支撑相位集合 A_Q：
  用 BoundaryTerminal 检查 A_Q cap [1,P]；

若无法给出同一 formal unit 的 M_Q：
  回到 Multiplicity-Stitching；

若局部展开质量偏斜持久：
  回到 PDEC/ColumnCRT；

若局部 fiber 平坦且无边界出口：
  回到 CleanKLS/DLS。
```

所以后继层不能作为无名逃逸。它必须给出：

```text
具体终端行；
或边界 LocalSurvivor；
或 PDEC；
或 CleanKLS；
或 formal-unit gap。
```

## 7. 闭合边界

本文完成的是局部展开合同，不是全局证书全集。仍需补齐：

```text
所有正式 PDEC 分支的 expected_mass 来源；
CleanKLS/DLS admission；
LocalSurvivor 证书全集；
formal-unit 一致性。
```

但它把“没有下一层数据”从终端缺口降级为可解析义务：只要给出当前相位原子和同一 `C_P` 口径，
就能局部展开剩余高素 fiber，并直接判断是否可能触碰前 `P` 行。
