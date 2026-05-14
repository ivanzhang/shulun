# Prime Matrix 素数基点 1/2 指数障碍审查路由器

**状态：** `prime_base_square_phase_rigidity_identified_but_half_exponent_not_closed`

把通用短区间定理专门化到 `X=P^2` 后，`X^0.525` 与 `X^0.52` 分别变成 `P^1.05` 与 `P^1.04`，仍长于目标窗口 `P`。限制 `P` 为素数确实给出平方相位刚性：小模禁类为 `r=-P^2 mod q`，且整个 CRT 相位向量落在平方轨道上；但这只提供新的攻击入口，当前尚未推出每个素数平方端点后长度 `P` 内必有素数。因此不能把指数自动压到 `1/2` 以下；下一步应直接攻 square-phase 粗幸存下界，或证明任何 square-phase 覆盖失败都会产生已登记 PDEC/SAE/预算矛盾。

```text
external_0525_or_052_specialization_sufficient=false
prime_base_restriction_auto_breaks_half_barrier=false
square_phase_rigidity_attack_target_identified=true
first_half_prime_square_input_current_corpus_proved=false
row_column_unconditional_closed=false
```

## 1. 尺度换算

| input | interval for X | after X=P^2 | target | sufficient |
| --- | --- | --- | --- | ---: |
| Baker-Harman-Pintz | `X^0.525` | `P^1.05` | `P` | `false` |
| Li arXiv:2308.04458 | `X^0.52` | `P^1.04` | `P` | `false` |
| needed square-endpoint theorem | `X^(1/2) or better on X=P^2` | `P` | `P` | `true` |

## 2. P 为素数带来的结构刚性

| structure | content | effect |
| --- | --- | --- |
| `q=P is harmless` | 0<r<P 时 P 不整除 P^2+r，因此端点自己的素因子不会覆盖窗口。 | 消除一个平凡障碍，但不产生素数存在性下界。 |
| `quadratic phase` | 对每个 q<P，禁类为 r==-P^2 mod q；相位属于负二次剩余轨道。 | 给出平方相位刚性；单模密度仍是一条禁类，未自动改善筛密度。 |
| `CRT square subvariety` | 模 primorial 的相位向量来自同一个 P^2，而不是任意 CRT 向量。 | 这是可攻入口：若能证明 square-phase 短段不能被覆盖，即可突破。 |
| `prime P equidistribution` | P 在小模单位类中随 P 变化近似均匀，P^2 只落在平方类。 | 适合做平均或异常集攻击；但本命题要每个 P，平均不足以闭合。 |
| `parity` | 奇 P 下 P^2+r 为奇数要求 r 偶数。 | 候选点减半，是已知局部密度的一部分，不是负面矛盾。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `External0525SpecializedToPrimeSquareComputed` | `true` | `true` | 把 X=P^2 代入外部 X^theta 短区间定理，只得到 P^(2theta) 长度。 | theta<=1/2 needed |
| `PrimeBaseRestrictionAutomaticallyImprovesExponent` | `false` | `false` | P 为素数只把端点相位限制到平方轨道；现有定理没有给出从 0.52/0.525 到 1/2 的自动降维。 | SquarePhaseRoughSurvivorUniformLowerBound OR PrimeSquareEndpointNoExceptionalPhaseTheorem |
| `SquarePhaseRigidityAttackTargetIdentified` | `true` | `false` | 真正可攻点是证明负平方相位的短区间筛残洞有统一下界，或任何失败产生 PDEC/SAE 缺陷。 | SquarePhaseRoughSurvivorUniformLowerBound OR PDEC/SAE defect |
| `AlmostAllPrimeBaseWouldSuffice` | `false` | `false` | 几乎所有 P 有素数不够；需要所有素数 P，或证明异常集不含任何素数平方端点。 | PrimeSquareEndpointNoExceptionalPhaseTheorem |
| `FirstHalfPrimeSquareClosedByPrimeBaseRigidity` | `false` | `false` | 当前语料和外部输入尚未把 P 为素数的结构刚性转成全局无条件素数存在性。 | PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP OR NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction |

## 4. 下一步

- 主攻 `SquarePhaseRoughSurvivorUniformLowerBound`：证明负平方相位短段中存在统一粗幸存残洞。
- 若 square-phase 粗幸存失败，必须生成 PDEC/SAE/ColumnCRT 缺陷并接回 `NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction`。
- 平行强路线 `PrimeSquareEndpointNoExceptionalPhaseTheorem`：证明通用短区间异常集不含任何素数平方端点；这强于平均结果。

## 5. 外部参考

| source | exponent | url |
| --- | --- | --- |
| Baker-Harman-Pintz, The difference between consecutive primes, II | `0.525` | https://doi.org/10.1112/plms/83.3.532 |
| Runbo Li, The number of primes in short intervals and numerical calculations for Harman's sieve | `0.52 for sufficiently large x` | https://arxiv.org/abs/2308.04458 |

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-diagonal-postsquare-carry-discrepancy-pdec-route.md` | `387ce4c609d73b447c374db4b53986a72b2655427cbc6d64c449eaee9d19f1e5` |
| `docs/monograph/prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md` | `8e9a5381b104901ab29fd2734fd159bb1a9ddff93907e750834283f970ebf92c` |
| `docs/monograph/prime-matrix-inverse-alignment-final-tail-rough-survivor-obstruction-router.json` | `2faaae72cd649b0d469ce260b380b6180570c3c180a054ea092f3d0f9af48bd3` |
| `docs/monograph/prime-matrix-inverse-alignment-two-frontier-direct-attack-router.json` | `e96d2e3199ce385c0b2c7a0dec59b29cad69906ce2291dedc5413992537b51c7` |
| `docs/monograph/prime-matrix-postsquare-first-half-finite-boundary-router.json` | `312fd0f96abd2429da9797614f8beaad66067369b05b1921404a480f59f1e01c` |
| `experiments/prime_matrix_prime_base_exponent_half_barrier_router.py` | `f97cdf710e39236bf92f5c64dfe224b7ba9298a3ad0fc369bc41392947680557` |
