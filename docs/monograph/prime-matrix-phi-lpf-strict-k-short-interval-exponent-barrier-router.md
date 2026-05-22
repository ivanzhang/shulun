# Prime Matrix Phi-LPF strict k short interval exponent barrier 证书

**状态：** `strict_k_phi_lpf_endpoint_difference_short_interval_exponent_barrier_closed`

Phi-LPF 端点差分可以精确给出 strict 1<k<P 行的素数个数，但若尝试用充分大阈值后的普通短区间素数定理来直接推出正性，任何 theta>1/2 的长度只覆盖低 k<=P^((1-theta)/theta)；顶端 k 接近 P 的无限带仍未覆盖。因此该路线要完全闭合，必须输入 sqrt-scale 常数<=1 的短区间定理，或者回到 raw/rejection 的结构性严格失衡证明。

## 1. 指数适配计算

对 `x=kP`，strict 行目标需要在长度 `P` 内得到素数。若外部定理只给出
`[x, x + C x^theta]` 内有素数，则必须满足：

```text
P >= C*(kP)^theta implies k <= C^(-1/theta)*P^((1-theta)/theta)
```

常数 `C` 只改变前因子；当 `theta>1/2` 时，指数 `(1-theta)/theta<1`，
所以只覆盖 `k` 的低幂次段，不能覆盖全部 `1<k<P`。

## 2. theta 对照表

| name | theta | covered k exponent | all strict k covered | top band remains | needed |
| --- | ---: | ---: | --- | --- | --- |
| `theta_0_525` | `0.525000000000` | `0.904761904762` | `false` | `true` | theta<=1/2, or a separate structural top-band argument |
| `theta_0_51` | `0.510000000000` | `0.960784313725` | `false` | `true` | theta<=1/2, or a separate structural top-band argument |
| `theta_0_5001` | `0.500100000000` | `0.999600079984` | `false` | `true` | theta<=1/2, or a separate structural top-band argument |
| `theta_0_5` | `0.500000000000` | `1.000000000000` | `true` | `false` | sqrt-scale interval with constant <=1 |

## 3. 尺度样本

| P scale | theta | covered k approx | covered fraction | uncovered fraction |
| ---: | --- | ---: | ---: | ---: |
| 1000000 | `theta_0_525` | 268269 | 2.682696e-01 | 7.317304e-01 |
| 1000000 | `theta_0_51` | 581709 | 5.817091e-01 | 4.182909e-01 |
| 1000000 | `theta_0_5001` | 994490 | 9.944901e-01 | 5.509864e-03 |
| 1000000000000 | `theta_0_525` | 71968567300 | 7.196857e-02 | 9.280314e-01 |
| 1000000000000 | `theta_0_51` | 338385515342 | 3.383855e-01 | 6.616145e-01 |
| 1000000000000 | `theta_0_5001` | 989010630771 | 9.890106e-01 | 1.098937e-02 |
| 1000000000000000000000000 | `theta_0_525` | 5179474679231212945408 | 5.179475e-03 | 9.948205e-01 |
| 1000000000000000000000000 | `theta_0_51` | 114504756993828348493824 | 1.145048e-01 | 8.854952e-01 |
| 1000000000000000000000000 | `theta_0_5001` | 978142027778824108769280 | 9.781420e-01 | 2.185797e-02 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PhiLPFStrictKEndpointDifferenceAlreadyClosed` | `true` | `true` | Phi-LPF 已给出 [kP,kP+P] 与内部行的精确端点差分。 | use as exact count, not positivity |
| `ThetaGreaterThanHalfCoversOnlyLowK` | `true` | `true` | 若外部输入只保证 [x,x+C x^theta] 内有素数且 theta>1/2，则常数不改覆盖指数。 | k <= const * P^((1-theta)/theta) |
| `FiniteVerificationPlusThetaGreaterThanHalfCannotCloseAllLargeP` | `true` | `true` | 任何固定 theta>1/2 留下随 P 增长的顶端 k 带；有限验证不能覆盖无限顶端带。 | top band k near P |
| `SquareRootScaleInputIdentifiedAsNecessaryForThisLane` | `true` | `true` | 要靠纯短区间输入覆盖所有 1<k<P，至少需要 sqrt(x) 尺度且常数不超过 1。 | Legendre-scale or structural substitute |
| `SquareRootScaleInputAvailableInCurrentCorpus` | `false` | `false` | 当前语料没有无条件 sqrt-scale strict row 素数输入。 | PositiveRejectionExcess or external Legendre-scale theorem |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层关闭的是阈值+有限验证路线的指数适配，不是行/列命题。 | signed/transport strict imbalance or square-root interval theorem |

## 5. 结论

这层不是否定 Phi-LPF 端点差分；相反，它说明端点差分已经足够精确，问题只剩正性来源。
若正性来源选用“充分大阈值以上的短区间素数存在 + 有限验证”，则任意 `theta>1/2`
都会留下无限顶端带 `P^((1-theta)/theta) < k < P`。因此有限验证只能处理固定初段，
不能替代顶端带的一般证明。下一步必须二选一：提交 sqrt-scale 常数 `<=1` 的外部/内部输入，
或证明上一层的 `PositiveRejectionExcessForStrictKRawLPFIncidence`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_strict_k_short_interval_exponent_barrier_router.py` | `2197be5c8edfff1c264bc2998df5a55a8c606445f2f94379ecf0b7857052854d` |
| `docs/monograph/prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json` | `fda512a55d40c2b2e3dbac432b0bcff1c47efd7bea9e5b96e9bb291804214316` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-router.json` | `dbd0f06356306594afff56e4a199bdc4b27c7eb43688825b17cfd189ca8efa1c` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.json` | `d0b1755f1ba90db1c954b73254aad74aef846825e80dc38b7a128638e7550b6c` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json` | `59bf235653fb8aef057ba81b7e3e42132d7b8bf1b15283671e52330a9cb6ad0d` |
| `docs/monograph/prime-matrix-strict-brun-titchmarsh-short-interval-input-router.json` | `81123122d305deb41ea3e2da5e3da01b7638a99f0137194b9abdd0cc3eb3f8c2` |
