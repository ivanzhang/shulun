# AlphaTail 固定 gap 责任区间的格点端点几何引理

**状态：** `lattice_endpoint_geometry_lemma_proved_sample_audited`

本文把 `C13 endpoint gate` 从样本观察提升为一个可直接引用的确定性几何引理。

## 1. 格点责任区间

固定 `g,j_1,j_2` 后，几何截断给出

\[
u={-(j_1-j_2)r\over g}>0,\qquad d=qu-j_1r.
\tag{LEG-1}
\]

原始责任窗口为 `I=[A,B]`。`q` 区间按定义为所有使 `d in I` 的整数 `q`：

\[
J=
\left[
\left\lceil {A+j_1r\over u}\right\rceil,
\left\lfloor {B+j_1r\over u}\right\rfloor
\right].
\tag{LEG-2}
\]

映回 `d` 后得到

\[
D=[d_-,d_+]
=
[u\lceil(A+j_1r)/u\rceil-j_1r,\,
u\lfloor(B+j_1r)/u\rfloor-j_1r].
\tag{LEG-3}
\]

## 2. 端点距离小于步长

**引理 LEG-1（格点端点距离）。**  
若 `D` 非空，则

\[
0\le d_- - A < u,\qquad 0\le B-d_+<u.
\tag{LEG-4}
\]

因此

\[
{\min(d_- -A,\;B-d_+)\over |I|}
< {u\over |I|}.
\tag{LEG-5}
\]

**证明。**  
`d_-` 是同余格点 `d≡-j_1r mod u` 中不小于 `A` 的第一个点，所以 `d_- >= A` 且若
`d_- - A >= u`，则 `d_- - u` 仍是同一同余类并且仍不小于 `A`，这与首点定义矛盾。
右端同理：`d_+` 是不超过 `B` 的最后一个同余格点，若 `B-d_+>=u`，则 `d_++u<=B`
仍在同一同余类，矛盾。□

## 3. 端点门控推论

**推论 LEG-2（小 `u` 强制端点）。**  
给定 `theta in (0,1)`。若

\[
u\le \theta |I|,
\tag{LEG-6}
\]

则该责任区间自动满足 `EndpointGate(theta)`。

**证明。**  
由 `(LEG-5)` 得端点距离比 `<u/|I|<=theta`。□

**推论 LEG-3（非端点区间极短）。**  
若某责任区间不由 `(LEG-6)` 端点化，即 `u>theta|I|`，则

\[
|J|\le \left\lfloor {|I|\over u}\right\rfloor+1
< {1\over\theta}+1.
\tag{LEG-7}
\]

特别地，当 `theta=0.1` 时，非端点责任区间至多含 `10` 个 `q` 值。

**证明。**  
`J` 与 `I` 中步长为 `u` 的同余格点一一对应，故点数不超过 `floor(|I|/u)+1`。
若 `u>theta|I|`，则 `|I|/u<1/theta`。□

## 4. 样本审计

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_lattice_endpoint_geometry_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_lattice_endpoint_geometry_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
```

输出摘要：

```text
records 870 bound_failures 0 slack_cut 40 near 123
near_u_forced 123 near_u_unforced 0
max_near_u_ratio 0.002024
max_near_endpoint_ratio 0.000253
```

这核验两点：

```text
所有责任区间均满足端点距离 < u；
样本中 slack<=40 的近门槛区间全部满足 u<=0.1|I|，所以由 LEG-2 强制端点化。
```

## 5. 对 C13 硬点的影响

`OnePairMargin-C13` 现在被确定拆成：

```text
Small-u branch:
  u<=theta|I|，由 LEG-2 自动进入 EndpointGate；

Large-u branch:
  u>theta|I|，由 LEG-3 得 |J|<1/theta+1，
  对 theta=0.1 是至多 10 点的短 q 窗口；
  若仍触及 C13 门槛，则必须作为 InteriorSAE 或短窗口 PDEC 证书处理。
```

因此当前硬点不再是全体中尺度固定 gap 素对常数，而是：

```text
Large-u short-q exception:
  证明这些至多 10 点的非端点责任区间不能跨过 C13 整数门槛；
  或把它们全部列入 SAE/PDEC 证书。
```

## 6. 审稿边界

已完成：

```text
格点端点距离引理 LEG-1；
小 u 强制端点推论 LEG-2；
非端点责任区间极短推论 LEG-3；
样本近门槛区间全部由小 u 强制端点化。
```

仍未完成：

```text
全局 large-u short-q exception 排斥；
或对应 InteriorSAE/PDEC 证书全集。
```

