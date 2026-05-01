# BMD 直接硬攻：归约到受限 E2 序列 BV 分布（2026-05-01）

## 核心结论

BMD 不再需要作为神秘新猜想表述。模 `2` 在 `w=2` 情形中确定剥离：`p,m` 为奇素数时 `pm-2` 为奇数。因此 BMD 可以精确改写为受限二素数卷积序列

`a_n=#\{(p,m):Y<p<=P, m prime, n=pm, n in I\}`

在奇平方自由模算术级数中的 Bombieri--Vinogradov 平均分布。

## 精确误差

对平方自由 `d`，

`R_d=sum_{n in I, n=2 mod d} a_n - phi(d)^{-1} sum_{n in I,(n,d)=1} a_n`。

若引用标准 BV-`E2`：

`sum_{d<=P/log^B P} max_a |R_d(a)| <<_A N/log^A N`，

则对任意 Rosser/Buchstab 权重 `|lambda_d|<=1`，

`|sum lambda_d R_d| <= N/log^A N = o(|U_Y|)`，

因为 `|U_Y|~N/log^2 P`。

## 参数窗口

- `alpha>2/3`：保证 `n<=P^2` 中 `>Y` 的大素因子最多两个，使 `a_n` 为受限 `E2` 序列。
- `alpha<1`：保证 `Y=P^alpha < P/log^B P`，所有单素数禁曲线 `q<=Y` 都落入 BV level。
- `N=P^2`：BV level `N^{1/2}/log^B N` 正是 `P/log^B P`。

## 审稿状态

若合著稿允许引用标准双素 Type-II/dispersion 定理，则 BMD 误差闭合。若要求完全自足，则唯一剩余义务是新增 BV-`E2` 附录，证明受限二素数卷积在 `N^{1/2}/log^B N` 层的 Bombieri--Vinogradov 分布。

## 下一步

最优下一步不是继续寻找有限模板，而是写 `BV-E2 Appendix`：

1. dyadic 分解 `p~P_1`, `m~M_1`;
2. 用 Vaughan 或 Heath-Brown 恒等式替换素数指示；
3. 对非主角色双线性和应用大筛；
4. 汇总 dyadic 块并处理双曲边界；
5. 输出 `N/log^A N` 级平均误差。
