# Triad-A1 递归晋升二分

**状态：** `recursive_promotion_dichotomy_materialized_terminal_open`

本文承接：

```text
PersistentCap ColumnTail 支付审计；
TopPrimePromotionGate；
无限塔删除-熵二分。
```

核心作用是把“素数规律无穷层叠”改写成可审稿的递归链，而不是寻找一个固定全局常数。

## 1. 层级对象

在某一层轮筛 `Q_n` 上，`PersistentCap` 的低洞支付账本给出：

```text
D_C = sum_{phase in C} M_n(phase) * |H_low(phase)|。
```

全部低洞需求必须由 `Q_n` 之外的高素数 residue 支付。令 `r_n` 是当前支付账本中的 top-prime。

当前 `Q_0=2310` 的机器审计已经证明：

```text
r_0=13；
r_0 是 Q_0 外的最小新素数；
晋升 Q_1=13Q_0 后，68 个 persistent cap 全部进入 PromotionFiberDeletion。
```

## 2. 递归三分

对任意后继层重复同一动作。每层只有三种合法归宿：

```text
A. top prime persists:
   r_n 固定且为 Q_n 外的新素数；
   => 晋升 Q_{n+1}=r_n Q_n；
   => 进入 fiber deletion / sparse / 下一层。

B. fixed residue or column signature persists:
   (ell,a)、column residue、位移签名等固定复现；
   => TailAnchor / ColumnCRT displacement / refined PDEC。

C. no fixed signature persists:
   支付被迫跨许多 prime/residue/column 桶分散；
   => CleanKLS/DLS admission。
```

这不是概率统计，而是有限签名鸽巢加结构账本：

```text
若存在持久集中，必有某个有限签名无限复现；
若没有任何有限签名复现，则质量只能逃向更多新增层和更多桶；
新增层若由 top prime 承担，就被晋升吸收。
```

## 3. 与删除势塔拼接

每次晋升 `Q_{n+1}=r_n Q_n` 后，旧相位 fiber 的幸存率为：

```text
a_n = average_t s_n(t)/r_n。
```

删除势为：

```text
D_n^{del} = -log a_n。
```

于是：

```text
sum D_n^{del}=infinity
  => 支撑密度趋零
  => Sparse/LocalSurvivor 或容量/PDEC 回流；

sum D_n^{del}<infinity
  => a_n->1
  => 删除停止，进入 NoDeletion-KL / CleanKLS 二分。
```

因此 top-prime 持久支付不会产生第四类终端；它只会把反例链送入删除势塔。

## 4. 与 CleanKLS 拼接

若某层不再有可晋升的 top-prime 集中，也没有固定 residue/column 签名，则必须满足：

```text
no promotable top-prime concentration；
no fixed residue cap；
no fixed column displacement；
no short window cap；
effective support 大，单桶份额小。
```

这正是 `CleanKLS/DLS` 的 admission 方向。若大筛失败，则大筛对偶又输出某个集中签名，回到 PDEC 或晋升门控。

## 5. 对行命题的意义

这条链直接服务于 `P` 行以内不能形成零行的目标：

```text
早期 SparseCap:
  已由 LocalSurvivor / finite PDEC 关闭 P×P 早期出口；

PersistentCap:
  top-prime 集中 => 晋升删除；
  residue/column 集中 => PDEC；
  无集中 => CleanKLS/DLS；

ForcedCap:
  固定 Q 同层循环已由 lift 账本禁止；
  继续持久也必须走同一晋升/column-tail/CleanKLS 链。
```

所以当前结构闭合形态是：

```text
零行反例
=> DualCap/Sparse/Persistent/ForcedPersistent
=> LocalSurvivor 或 finite PDEC
   或 top-prime 晋升删除势
   或 fixed-signature PDEC
   或 CleanKLS/DLS。
```

## 6. 当前未闭合项

本文完成的是递归路由，不是最终排斥全集。剩余终端仍是：

```text
1. finite/profinite/refined PDEC 的 U_CRT<L_PDEC；
2. CleanKLS/DLS 的正式大筛证书；
3. LocalSurvivorCert 全部窗口证书；
4. 删除势发散支与最终行命题的完全拼接。
```

但本文消除了一个关键无名逃逸：`top-prime 持久支付` 不能作为新终端存在；它必然被下一层轮筛晋升吸收。

## 7. 删除势账本接入

新增：

```text
experiments/prime_matrix_triad_a1_promotion_deletion_potential_ledger.py
docs/monograph/prime-matrix-triad-a1-promotion-deletion-potential-ledger.md/json
```

该账本把 `TopPrimePromotionGate` 的 lift survival 转成删除势：

```text
a_n = lift_survival_rate；
D_n = -log(a_n)。
```

当前 `Q=2310 -> 30030` 晋升层结果：

```text
cap_count=68；
all_positive_deletion_potential=True；
global_min_deletion_potential_current_layer=0.8800788718999966；
global_max_survival_current_layer=0.4147501982553529。
```

这不作为全局固定常数使用。它的正式作用是：

```text
每层 top-prime 晋升都必须登记本地 D_n；
若 sum D_n = infinity，则支撑密度趋零；
若 sum D_n < infinity，则 D_n->0，a_n->1，进入 NoDeletion-KL/CleanKLS；
若某层出现固定 residue/cap，则回到 PDEC。
```

所以递归晋升链现在不只是路由，而且有可累加的势函数。
