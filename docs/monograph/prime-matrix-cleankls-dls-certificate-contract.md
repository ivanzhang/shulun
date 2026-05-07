# CleanKLS/DLS 证书合同：平坦残余必须由大筛吸收

**状态：** `cleankls_reduced_to_flat_large_sieve_certificate_or_pdec_not_closed`

本文承接 `prime-matrix-sae-local-certificate-reduction.md`。当前主链剩余为：

```text
PDEC family；
LocalSurvivorCert family；
CleanKLS/DLS。
```

本文把 `CleanKLS/DLS` 固定为可验收证书对象，而不是黑箱出口。它只在所有命名缺陷已经剥离后
才可调用：

```text
无短窗峰；
无低模峰；
无列位移/Bohr cap；
无尾锚/互补因子锚；
同一 formal unit 口径合法；
系数 L2-flat。
```

## 1. Clean formal unit

一个 clean KLS/DLS 输入必须登记：

```text
Omega                 : 同一 formal unit；
m,q,d                 : 互补因子、高素、列位移变量；
W(m,q)                : 平滑或可分块权重；
a_m,b_q               : 系数；
R(P,y)                : 本行剩余待支付余量；
DefectLedger          : 已剥离的 PDEC/SAE/Anchor/Column/cap 列表。
```

中心化残余写成：

\[
\mathcal E
=
\sum_{m,q} a_m b_q W(m,q)
\left(1_{\ q\ {\rm prime}}-\operatorname{model}(q;m)\right).
\tag{CKD-1}
\]

Clean 目标是证明：

\[
|\mathcal E|<R(P,y)
\tag{CKD-2}
\]

或更强的带级/行级吸收不等式。

## 2. Admission 条件

`CleanKLS/DLS-Cert` 必须逐项核验：

```text
K1 dyadic ranges       : m,q,d 位于登记区间；
K2 lowmod orthogonality: q mod W、d mod W 无中心化峰；
K3 no short-window cap : q 短窗峰已剥离；
K4 no column cap       : d mod P 非零频率/Bohr cap 已剥离；
K5 coefficient L2-flat : sum |a_m|^2, sum |b_q|^2 在阈值内；
K6 gcd/unit strata     : 非单位/gcd 层已剥离或多对数可吸收；
K7 formal unit         : 与 PDEC/SAE 账本同口径。
K8 no promotable prime : 最高新素数集中已被晋升门剥离；
K9 no fiber mutual info: 新层 residue 与旧相位没有持久互信息峰。
```

任一条件失败，不能调用 clean KLS；失败项必须回流：

```text
K2 fail => PDEC；
K3 fail => SAE or refined PDEC；
K4 fail => displacement/Bohr-cap PDEC；
K5 fail => coefficient concentration PDEC/SAE；
K6 fail => gcd-stratum PDEC or finite exception；
K7 fail => Multiplicity/Stitching absorption。
K8 fail => TopPrimePromotionGate；
K9 fail => refined (old_phase,residue) PDEC。
```

## 3. 大筛证书

在 K1--K7 全部通过后，可使用两类证书：

### 3.1 内部大筛证书

给出同一 formal unit 上的显式不等式：

\[
|\mathcal E|
\le
\mathcal B_{\rm LS}(\|a\|_2,\|b\|_2,\text{ranges},\text{smoothness})
<R(P,y)。
\tag{CKD-3}
\]

并登记每个损失来源。

### 3.2 外部 KLS/DI/BFI 证书

若调用外部 Kloosterman/dispersion 大筛，必须给出变量适配表：

```text
模数；
逆元变量；
频率范围；
平滑窗口；
系数二范数；
gcd/unit 层；
dyadic 分块损失。
```

`prime-matrix-h3-dsb-hlc-kls-external-adaptation.md` 已给出一个模板：所有不能进入 KLS 的失败项
必须先回流 PDEC/SAE，只有 clean unit 可调用外部输入。

## 4. CleanKLS 失败回流

若 K1--K7 通过但 `(CKD-3)` 失败，则大筛失败本身给出对偶集中对象。按大筛对偶性，必有：

```text
高 L2 系数集中；
某频率/模数方向相关；
某短窗或端点权重主导；
某 gcd/unit 层异常。
```

这些分别回流为：

```text
coefficient PDEC/SAE；
frequency PDEC / Bohr-cap；
SAE endpoint；
gcd-stratum PDEC。
```

所以 `CleanKLS` 失败也不生成新出口。

## 5. 形式化结论

**CleanKLS/DLS Certificate Contract.**
任意 clean residual 必须满足以下之一：

```text
CleanKLS/DLS-Cert 通过，残余被吸收；
admission fail，回流 PDEC/SAE/Multiplicity；
large-sieve fail，输出对偶集中并回流 PDEC/SAE；
外部定理缺失，标为 ExternalInput，而不是无条件证明。
```

因此 `CleanKLS/DLS` 从“出口”改写为：

```text
LargeSieve certificate
or ExternalKLS input
or PDEC/SAE回流。
```

## 6. 当前闭合边界

本文完成：

```text
CleanKLS/DLS 的证书格式与失败回流规则；
KLS 不能吸收未剥离缺陷。
```

本文未完成：

```text
本行命题所需 CleanKLS/DLS-Cert 全集；
完全自足 KLS/DI/BFI 证明；
所有 PDEC family 与 LocalSurvivorCert。
```

最终主链现在压成：

```text
PDEC family；
LocalSurvivorCert family；
CleanKLS/DLS certificates or explicit ExternalKLS input。
```

这仍是结构归约，不是最终无条件行命题证明。

## 7. PersistentCap 支付分散入口

新增 `prime-matrix-triad-a1-persistent-columntail-payment.md/json` 后，`CleanKLS/DLS`
获得一个新的具体 admission 输入。

对 `Q=2310` LHB-PDEC 中的 `PersistentCap`，已登记：

```text
D_C = sum_{phase in C} M(phase) * |H_low(phase)|；
effective support = D_C / max_single_bucket_payment。
```

若 top tail/column residue 支付签名沿正式反例族持久复现，则它不是 clean 输入，而是
`TailAnchor / ColumnCRT displacement PDEC`。只有当这些 top 签名不持久、且需求仍由大量
residue 分散支付时，才满足本文 `K4 no column cap` 与 `K5 coefficient L2-flat` 的方向性入口。

当前有限层读数：

```text
P>=23 时 min effective residue support >= 22.011；
单个 residue 最大支付份额约为 3.5%--4.5%。
```

这不作为全局常数使用；它的作用是给每层、每个 cap 生成本地分散准入量。沿无限层若该有效支撑继续增长或不塌缩，即进入多壳 `CleanKLS/DLS`；若塌缩，则塌缩 residue 本身就是 `PDEC` 回流对象。

## 8. TopPrime 晋升后的 clean 边界

新增 `prime-matrix-triad-a1-topprime-promotion-gate.md/json` 后，`PersistentCap` 的最高支付素数集中已经不再算作 clean 失败：

```text
top prime = 当前 Q 外最小新素数
=> 晋升 Q'=rQ
=> PromotionFiberDeletion。
```

当前 `Q=2310` 层的 `68` 个 persistent cap 全部满足这一规则。故 CleanKLS/DLS 的真正输入不是“有一个新素数承担较多支付”的对象；这种对象必须先升层剥离。Clean 输入只能是升层后仍没有固定 top-prime、固定 residue、固定 column displacement、固定短窗峰的剩余分散质量。

这进一步细化 admission：

```text
K4 no column cap；
K5 coefficient L2-flat；
K8 no promotable top-prime concentration。
K9 no phase-residue mutual information concentration。
```

`K8` 失败时不进入 CleanKLS，而是执行 `TopPrimePromotionGate`；只有晋升删除势停止且没有新的固定签名时，才回到 clean 大筛证书。

## 9. NoDeletion-KL 互信息准入

新增 `prime-matrix-triad-a1-nodeletion-kl-witness-extractor.md/json` 后，`K9` 获得了可检查定义。对旧相位
`T` 与新增 fiber residue `B`：

```text
E_T KL(B|T||U_B)=KL(B||U_B)+I(T;B)。
```

若 `KL(B||U_B)` 持久偏大，则是全局新增 residue PDEC；若 `I(T;B)` 持久偏大，则是 refined
`(old_phase,residue)` PDEC。只有两者都在 NoDeletion 分支趋零，才允许把该层残余送入 CleanKLS/DLS。

当前有限审计仍全部是 `FiberDeletionCurrentLayer`，但形状读数为：

```text
shape_route_counts={'PhaseResidueMutualPDECWitness': 6}；
max_global_residue_normalized_kl=0.0388557；
min_phase_residue_mutual_normalized_kl=0.412500。
```

这说明现有偏斜尚不 clean；只是当前已由删除势吸收，未触发 CleanKLS 终端。
