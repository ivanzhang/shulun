# P=23, r=59 零行结构分析

区间：`1335..1356`

P=23,r=59 的零行不是随机现象，而是 x=58 使每个 c=1..22 都落入某个根基素数 q 的禁余类 c≡-xP mod q。小素数 2,3,5 先覆盖大部分位置，剩余位置由 7,11,13,17,19 精确补洞。该结构是 CRT 覆盖系统在 r>P 后第一次形成完整覆盖。

## 每列因子
- c=1 n=1335 factors=[3, 5] min=3 quotient=445
- c=2 n=1336 factors=[2] min=2 quotient=668
- c=3 n=1337 factors=[7] min=7 quotient=191
- c=4 n=1338 factors=[2, 3] min=2 quotient=669
- c=5 n=1339 factors=[13] min=13 quotient=103
- c=6 n=1340 factors=[2, 5] min=2 quotient=670
- c=7 n=1341 factors=[3] min=3 quotient=447
- c=8 n=1342 factors=[2, 11] min=2 quotient=671
- c=9 n=1343 factors=[17] min=17 quotient=79
- c=10 n=1344 factors=[2, 3, 7] min=2 quotient=672
- c=11 n=1345 factors=[5] min=5 quotient=269
- c=12 n=1346 factors=[2] min=2 quotient=673
- c=13 n=1347 factors=[3] min=3 quotient=449
- c=14 n=1348 factors=[2] min=2 quotient=674
- c=15 n=1349 factors=[19] min=19 quotient=71
- c=16 n=1350 factors=[2, 3, 5] min=2 quotient=675
- c=17 n=1351 factors=[7] min=7 quotient=193
- c=18 n=1352 factors=[2, 13] min=2 quotient=676
- c=19 n=1353 factors=[3, 11] min=3 quotient=451
- c=20 n=1354 factors=[2] min=2 quotient=677
- c=21 n=1355 factors=[5] min=5 quotient=271
- c=22 n=1356 factors=[2, 3] min=2 quotient=678

## 禁余类覆盖
- q=2 residue=0 new=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22] all=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
- q=3 residue=1 new=[1, 7, 13, 19] all=[1, 4, 7, 10, 13, 16, 19, 22]
- q=5 residue=1 new=[11, 21] all=[1, 6, 11, 16, 21]
- q=7 residue=3 new=[3, 17] all=[3, 10, 17]
- q=13 residue=5 new=[5] all=[5, 18]
- q=17 residue=9 new=[9] all=[9]
- q=19 residue=15 new=[15] all=[15]

## 下一证明义务
- 比较 x<P 时 forbidden residues 是否缺少这种完整覆盖能力。
- 研究贪心覆盖中最后补洞的大素数位置与 x 的同余条件。
- 证明前窗口 x<P 无法让禁余类族覆盖全部 1..P-1。
