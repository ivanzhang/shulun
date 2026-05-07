# ColumnCRT 位移 PDEC 吸收合同：列缺陷不是独立终端

**状态：** `columncrt_absorbed_to_displacement_pdec_or_sae_not_closed`

本文承接 `prime-matrix-tailanchor-cofactor-absorption-contract.md`。当前终端列表中仍有
`ColumnCRT`。本文把它改写为带列位移标签的 generalized `PDEC`：

```text
persistent nonzero displacement overload => displacement PDEC；
sparse displacement overload             => SAE/Endpoint；
zero displacement                         => CD0 contradiction or small exception；
balanced displacement load                => cannot pay named defect budget。
```

因此 `ColumnCRT` 不再作为独立终端。

## 1. 列位移对象

沿用 `h4-pdec-column-defect-routing-contract.md`。对活动列点

```text
n_c=Hq+c
```

取同列素数见证

```text
pi_c=r_c q+c
```

并定义列位移：

```text
d_c=r_c-H。
```

若旧标签 `ell` 覆盖 `n_c`，且 `pi_c!=ell`，则已有 CD0 引理：

\[
d_c\not\equiv 0\pmod \ell。
\tag{CCD-0}
\]

所以任何持续列缺陷都落在非零位移余类上。

## 2. 位移签名

把 ColumnCRT 事件写成有限签名：

```text
sigma_col(x)=(ell, d_c mod ell)
```

或在需要全局列相位时写成：

```text
sigma_col'(x)=(ell, d_c mod ell, d_c mod Q, base tau(x))。
```

对固定 `(ell,a)`，定义零均值测试函数：

```text
F_{ell,a}(x)=1_{sigma_col(x)=(ell,a)} - baseline_{ell,a}。
```

若坏窗集合在非零位移余类 `(ell,a)` 上持久过密，则

\[
\sum_{x\in S}F_{\ell,a}(x)>0
\]

并由 Fourier/有限签名展开进入 generalized `PDEC-Cert`。这就是 displacement PDEC。

## 3. ColumnCRT 三分

给定同口径坏窗集合 `S` 与位移负载

```text
R_{ell,a}(S)=#{x in S: lambda(x)=ell, d_c=a mod ell}。
```

对每个非零 `a` 必有：

### 3.1 Sparse displacement

若超载只在有限窗口出现，或不沿正式最小反例族持久，则进入：

```text
SAE-column / endpoint。
```

### 3.2 Persistent displacement

若 `R_{ell,a}` 在同一分支中持续超过阈值，则有限签名鸽巢给出固定 `(ell,a)`，进入：

```text
displacement PDEC。
```

若同一 `(ell,a)` 又对应固定端点 seam 或固定第 `P` 列锚残基，则它是 endpoint/cofactor
版本的同一 PDEC。

### 3.3 Balanced displacement

若所有非零位移余类均不超载，则 ColumnCRT 不能承担命名缺陷预算；对应条件行

```text
R_{ell,a}(g)<=L_D
```

可作为 `PDEC-Dual-Cert` 的合法约束行，正是 `h4-pdec-column-defect-routing-contract.md`
中的 CD2。

## 4. 兼容性失败的处理

若 `sigma_col` 不是旧相位 `tau` 的函数，则不能直接把 ColumnCRT 行写进旧 `g(t)`。此时只有两种合法处理：

```text
细化 tau'=(tau,sigma_col)，进入 refined/displacement PDEC；
或按 formal unit 商掉不兼容事件，进入 primitive PDEC / SAE。
```

这与 `Multiplicity-Stitching` 合同一致。

## 5. 形式化结论

**ColumnCRT-Displacement Absorption.**
任意 ColumnCRT/ColumnRadius 出口，有限步内必进入：

```text
displacement PDEC；
SAE-column / endpoint；
PDEC-Dual-Cert 条件约束行；
CD0 zero-class contradiction or finite exception；
formal-unit refinement / primitive quotient。
```

因此 `ColumnCRT` 从独立终端列表中删除。

## 6. 当前闭合边界

本文完成：

```text
ColumnCRT 是 displacement PDEC 或 SAE；
非零位移过载不是新终端。
```

本文未完成：

```text
displacement PDEC 的 U_CRT<L_PDEC；
SAE-column 排斥；
全局 L_D 阈值证明或有限证书推广。
```

最终终端列表进一步压成：

```text
PDEC family:
  explicit / profinite / weighted / primitive / cofactor / displacement；
SAE family；
CleanKLS/DLS。
```

这仍是结构归约，不是最终无条件行命题证明。

## 7. SAE 局部证书归约

新增 `prime-matrix-sae-local-certificate-reduction.md` 后，`SAE family` 也不再作为模糊终端。
孤窗逃逸必须提交 `LocalSurvivorCert`：

```text
C(I) 候选点集合；
各类 blocker 集合；
一个未被 blocker 覆盖的 witness n0，
或 |union blockers|<|C(I)|。
```

若局部证书失败，覆盖者按低模、小因子、尾锚、列位移、端点 seam 分型；持久者回到 PDEC family，
孤立者进入更小支撑的 SAE。固定孤窗内该下降有限，沿无限反例族复现则由鸽巢转为 PDEC。
