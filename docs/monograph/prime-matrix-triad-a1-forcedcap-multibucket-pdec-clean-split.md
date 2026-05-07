# Triad-A1 ForcedCap 多桶 PDEC / CleanKLS 结构二分

**状态：** `forcedcap_multibucket_terminal_split_contract_open`

本文接在 `ForcedCap 暴露支配实际支付` 之后。已知当前 forced cap 不能由单个
`residue` 或单个 `column-residue` 支付完成；因此最后硬点不是“找一个最强桶”，而是处理无穷升层中的多桶支付结构。

## 1. 输入对象

固定一个 forced cap `C`。令

```text
Omega_C = tail 低洞支付原子集合；
D_C     = |Omega_C|，带 multiplicity 时按质量计数；
B_C     = 可支付 bucket 集合；
E_C(b)  = #{omega in Omega_C: omega 可由 bucket b 支付}；
A_C(b)  = 实际支付方案在 bucket b 上承担的质量。
```

暴露支配律为：

```text
A_C(b) <= E_C(b)；
sum_b A_C(b) = D_C；
N_C >= ceil(D_C / max_b E_C(b))。
```

这里的 `N_C` 是每个 cap 自归一化的动态桶数下界，不依赖固定常数。
当前核验给出：

```text
forced_cap_count=24；
min actual residue buckets >= 11；
min actual column-residue buckets >= 9。
```

## 2. 升层投影系统

令轮层为：

```text
Q_0 | Q_1 | Q_2 | ...，Q_{i+1}=r_i Q_i。
```

每一层有 bucket 集合 `B_i`、支付测度：

```text
mu_i(b)=A_i(b)/D_i。
```

升层给出自然投影：

```text
pi_i: B_{i+1} -> B_i。
```

因此一个真正能威胁零行的反例族，不能只在某个有限层偶然集中；它必须在这个逆系统中保持某种兼容性。

## 3. 终端二分

假设一个 forced 分支已经通过：

```text
BTLS；
AttachedMass；
DensityBarrier；
ColumnTailExposure；
ExposureDominance。
```

则剩余反例只能落入下面三类之一。

### 3.1 MultiBucketPersistent

存在一族投影兼容的有限多桶签名 `S_i subset B_i`，使得：

```text
pi_i(S_{i+1}) = S_i；
mu_i(S_i) 持久承担正比例支付质量。
```

这时 `S_i` 不是随机分散，而是一个 formal unit。它必须进入：

```text
multi-bucket TailAnchor；
multi-bucket ColumnCRT；
refined PDEC。
```

闭合目标变成：

```text
U_CRT(S_i) < L_PDEC(S_i)。
```

即：同一个多桶签名若想长期承担足够多的洞，就会在 CRT 相位容量上低于 PDEC 所需的最低质量。

### 3.2 DistributedPayment

不存在投影兼容的持久有限桶签名。等价地，对任意固定低层桶组 `S_i`，后继层的支付质量不会长期锁定在
`pi^{-1}(S_i)` 上。

这时支付质量必须向越来越多的新桶扩散。令：

```text
E2_i = sum_{b in B_i} mu_i(b)^2。
```

暴露支配给出原子上界：

```text
max_b mu_i(b) <= max_b E_i(b)/D_i。
```

若没有持久签名，则 `E2_i` 必须由许多小桶贡献，进入：

```text
CleanKLS / DLS admission。
```

闭合目标变成一个大筛型结构不等式：

```text
Distributed tail 支付的跨壳相关能量
  < 覆盖整行所需能量。
```

这一步需要证明的是结构大筛证书，不是数值概率估计。

### 3.3 LiftDeletion / NoDeletion-KL

升层后若支撑被新素数层切掉正质量，则删除势支付：

```text
Phi_{i+1} <= Phi_i - Delta_i。
```

若这种正删除无限发生，则势函数不能无限下降，反例链终止。

若长期几乎无删除，则反过来形成：

```text
NoDeletion-KL / CleanKLS
```

因为“新层不删除”意味着相位对新轮层过度平坦或过度同步，必须进入 KL/大筛门控。

## 4. 递归闭合方程

Forced 分支的终端递归可以压成：

```text
ZeroRow_i
=> MultiBucketPersistent_i
   or DistributedPayment_i
   or (ZeroRow_{i+1} with Phi_{i+1} <= Phi_i - Delta_i)
   or NoDeletionKL_i。
```

因此全局闭合只需要完成三类排斥：

```text
MultiBucketPersistent_i  => PDEC contradiction；
DistributedPayment_i     => CleanKLS/DLS contradiction；
Infinite LiftDeletion    => deletion potential contradiction；
NoDeletionKL_i           => KL/CleanKLS contradiction。
```

这正是无固定常数的递归剥离路径：每一层只使用该层自己的 `D_i/max E_i`、投影兼容性与删除势。

## 5. 当前推进点

当前已经完成：

```text
单桶 actual-payment 逃逸关闭；
forced cap 必须多桶化；
多桶化的剩余形态被压成 PDEC / CleanKLS / deletion-KL 三分支。
```

下一硬点不应再分散扫描固定区段，而应直接攻：

```text
MBCS-1: multi-bucket PDEC 容量不等式 U_CRT(S)<L_PDEC(S)；
MBCS-2: no persistent signature => CleanKLS/DLS admission；
MBCS-3: lift deletion potential 发散或 no-deletion KL。
```

其中 `MBCS-1` 是最窄硬点：一旦持久多桶 formal unit 被 PDEC 排除，forced 分支只能扩散或删除；再由
`MBCS-2/3` 接住，就能把当前 Triad-A1 分支继续向全局闭合推进。
