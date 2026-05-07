# SAE 局部证书归约：孤窗逃逸不是独立终端

**状态：** `sae_reduced_to_local_survivor_cert_or_pdec_not_closed`

本文承接 `prime-matrix-columncrt-displacement-pdec-absorption.md`。当前终端列表为：

```text
PDEC family；
SAE family；
CleanKLS/DLS。
```

本文继续压缩 `SAE family`。`SAE` 的含义是 sparse/single-window escape：某个坏窗没有形成持久
低模频率，不能直接用 PDEC 排斥。本文证明它不是独立结构出口，而是一个局部证书义务：

```text
SAE-window
=> LocalSurvivorCert
   or local blocker defect
      => PDEC / displacement PDEC / cofactor PDEC / smaller SAE。
```

## 1. SAE 窗口对象

固定孤立坏窗 `I`。令 `C(I)` 是该窗内还可能成为素数洞的候选点集合。`I` 成为零行反例的一部分，
必须有一组阻塞者覆盖 `C(I)`：

```text
low-factor blockers       : 小素因子直接覆盖；
tail/cofactor blockers    : 远尾互补因子覆盖；
column blockers           : 固定列位移覆盖；
endpoint/seam blockers    : 端点或缝合相位覆盖；
core-overlap blockers     : 旧核心高重叠覆盖。
```

因此局部证书的基本目标是：

```text
找到 n in C(I) 没有任何 blocker。
```

若找到，则 `n` 是 survivor，孤窗闭合。

## 2. LocalSurvivorCert

一个 `LocalSurvivorCert(I)` 必须给出：

```text
C(I)                     : 候选点集合；
B_low,B_tail,B_col,...   : 各类 blocker 子集；
cover_count(n)           : 每个候选点被哪些 blocker 命中；
witness n0               : cover_count(n0)=0；
或严格不等式             : |union blockers|<|C(I)|。
```

这不是统计估计；它是有限局部覆盖证书。若证书成立，`SAE(I)` 排除。

## 3. 证书失败的分型回流

若 `LocalSurvivorCert(I)` 失败，即 blocker 覆盖了全部 `C(I)`，则取承担覆盖的最小 blocker 族。
按类型分解：

### 3.1 小因子阻塞

若小因子阻塞在固定低模签名上集中，则进入：

```text
low-mod PDEC。
```

若只在该孤窗出现，则缩小为更具体的 `SAE-lowfactor`，其候选集严格小于 `C(I)`。

### 3.2 尾锚/互补因子阻塞

若尾锚或互补因子阻塞承担固定比例覆盖，则由 `TailAnchor/CofactorAnchor` 吸收合同进入：

```text
cofactor PDEC
or SAE-cofactor with smaller support。
```

### 3.3 列位移阻塞

若固定非零列位移余类承担覆盖，则由 `ColumnCRT` 吸收合同进入：

```text
displacement PDEC
or SAE-column with smaller support。
```

### 3.4 端点/缝合阻塞

若端点 seam 相位承担覆盖，则进入：

```text
endpoint PDEC
or SAE-endpoint with smaller support。
```

因此 SAE 失败不会生成新类型；它只会把阻塞者命名为 PDEC 家族，或产生更小的 SAE 子证书。

## 4. SAE 局部下降势函数

定义局部势函数：

```text
Psi_SAE=(
  |C(I)|,
  blocker_type_count,
  active_signature_rank,
  endpoint_depth,
  tail_anchor_count,
  column_signature_count
)。
```

每一次 SAE 失败回流只能：

```text
找到 survivor                         => 闭合；
固定一个持久 blocker 签名              => PDEC family；
缩小候选集或 blocker 支撑              => |C(I)| 下降；
增加签名秩                             => 回到 PDEC/cap no-cycle；
进入相邻素数层下降                     => TotalDescent/RPZ；
```

由于 `C(I)` 有限，固定孤窗内不能无限下降。若孤窗类型沿反例族无限复现，则 finite signature
鸽巢把它变成 persistent defect，回到 PDEC。

## 5. 与递归下降的连接

某些 SAE 窗口来自相邻素数壳或 seam。若局部 survivor 不在当前层显式出现，则有两种情况：

```text
lift:
  同相位或相邻漂移窗复现
  => PDEC / TotalDescent；

higher-defect:
  阻塞来自更高层尾锚、列位移或端点 seam
  => 对应 PDEC family。
```

所以 `Lift` 与 `Higher-defect` 不是额外出口；它们分别回到 `PDEC/TotalDescent` 和 PDEC family。

## 6. 形式化结论

**SAE-Local Reduction.**
任意 sparse/single-window escape，有限步内必进入：

```text
LocalSurvivorCert；
PDEC family；
TotalDescent / RPZ lower descent；
更小候选集上的 SAE。
```

固定孤窗内该过程有限终止；沿无限反例族复现则由鸽巢转为 PDEC。

因此 `SAE family` 从终端出口列表中改写为：

```text
LocalSurvivor certificates
or PDEC family
or descent.
```

## 7. 当前闭合边界

本文完成：

```text
SAE 不再是独立结构终端；
它被规约为局部 survivor 证书或 PDEC/下降回流。
```

本文未完成：

```text
所有 LocalSurvivorCert；
所有 PDEC family 终端排斥；
CleanKLS/DLS 全局证明。
```

最终主链现在压成：

```text
PDEC family；
LocalSurvivorCert family；
CleanKLS/DLS。
```

这仍是结构归约，不是最终无条件行命题证明。

## 8. CleanKLS/DLS 证书合同

新增 `prime-matrix-cleankls-dls-certificate-contract.md` 后，`CleanKLS/DLS` 也不再是黑箱出口。
它必须先核验 K1--K7 admission：

```text
dyadic ranges；
lowmod orthogonality；
no short-window cap；
no column/Bohr cap；
coefficient L2-flat；
gcd/unit strata；
formal unit consistency。
```

通过后提交内部大筛证书或明确外部 `KLS/DI/BFI` 输入；任一 admission 或大筛失败项都必须回流
`PDEC/SAE/Multiplicity`。因此 clean 分支是证书接口，不是无名终端。
