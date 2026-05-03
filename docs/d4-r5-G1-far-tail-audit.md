# D4/R5 G1 far tail 分桶容量审计

**状态：** `far_tail_reduced_to_low_tau_buckets`

far 最坏仍在 x=1023400，far/head≈0.4331，略高于目标 0.43，说明当前 0.43 常数过紧；若放宽到 0.435，则扫描通过。far 质量几乎完全来自 tau_sum<=8 且 count<=2 的低容量团：tau<=4 贡献约 0.225H，5<=tau<=8 贡献约 0.145H。tau>=9 的总贡献很小。

## 推荐常数调整
- `near_bound`：0.35
- `far_bound`：0.435
- `combined`：0.785
- `target_11_over_14`：0.7857142857142857
- `passes_tail44`：True

## far 最坏记录
- {'x': 1023400, 'head_sum': 0.07441142592365829, 'w20': 0.0022568707839301753, 'far_count': 59, 'far_sum': 0.03222726723044008, 'far_over_head': 0.4330956816161989, 'bucket_values': {'tau_le_4': {'count': 37, 'sum': 0.01675839513030003, 'over_head': 0.2252126595113652}, 'tau_5_8': {'count': 16, 'sum': 0.010793454826484963, 'over_head': 0.1450510414564345}, 'tau_9_16': {'count': 5, 'sum': 0.0045129843524985315, 'over_head': 0.060649077698478535}, 'tau_17_32': {'count': 1, 'sum': 0.00016243292115655436, 'over_head': 0.002182902949920633}, 'tau_33_59': {'count': 0, 'sum': 0, 'over_head': 0.0}, 'heavy_short': {'count': 0, 'sum': 0, 'over_head': 0.0}}, 'far_top10': [{'weight': 0.0011215404356566265, 'offset': 45, 'tau_sum': 6, 'count': 2, 'average_kernel': 0.0001869234059427711}, {'weight': 0.0011116623785564995, 'offset': 134, 'tau_sum': 8, 'count': 2, 'average_kernel': 0.00013895779731956244}, {'weight': 0.0010765279400316863, 'offset': 320, 'tau_sum': 12, 'count': 1, 'average_kernel': 8.971066166930719e-05}, {'weight': 0.0010697699745417892, 'offset': 92, 'tau_sum': 10, 'count': 2, 'average_kernel': 0.00010697699745417892}, {'weight': 0.0010516595661350927, 'offset': 112, 'tau_sum': 6, 'count': 2, 'average_kernel': 0.00017527659435584878}, {'weight': 0.0010077621527651711, 'offset': 155, 'tau_sum': 6, 'count': 2, 'average_kernel': 0.00016796035879419519}, {'weight': 0.0009762676110262663, 'offset': 60, 'tau_sum': 6, 'count': 2, 'average_kernel': 0.00016271126850437773}, {'weight': 0.0009746294123251596, 'offset': 57, 'tau_sum': 4, 'count': 2, 'average_kernel': 0.0002436573530812899}, {'weight': 0.0009447144590078746, 'offset': 20, 'tau_sum': 4, 'count': 1, 'average_kernel': 0.00023617861475196865}, {'weight': 0.0009426588637565296, 'offset': 18, 'tau_sum': 3, 'count': 1, 'average_kernel': 0.0003142196212521765}]}

## 分桶最坏
- `tau_le_4`：x=1023400, over_head=0.2252126595113652, count=37
- `tau_5_8`：x=1001500, over_head=0.16548701889262674, count=24
- `tau_9_16`：x=1012300, over_head=0.11773373665509294, count=12
- `tau_17_32`：x=1064700, over_head=0.05029419715206437, count=6
- `tau_33_59`：x=1075900, over_head=0.012306907517546047, count=1
- `heavy_short`：x=1000000, over_head=0.0, count=0

## 证明义务
- F1: tau_sum<=4 far bucket <=0.23 head20
- F2: 5<=tau_sum<=8 far bucket <=0.17 head20
- F3: tau_sum>=9 far bucket <=0.035 head20
- Then far/head <=0.435 and near/head<=0.35 imply tail/head<=0.785<11/14
