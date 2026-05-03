#!/usr/bin/env python3
"""尾部 T/H 最大值拟合汇总。"""
# 手动录入前几轮结果，计算与模型 sum1/q、log(1/c) 的比值。
import math
rows = [
(251,0.3,0.5172,0.2231),(251,0.5,0.3333,0.1299),(251,0.7,0.2143,0.0623),(251,0.9,0.0909,0.0214),
(503,0.3,0.4906,0.2102),(503,0.5,0.2955,0.1131),(503,0.7,0.1951,0.0593),(503,0.9,0.0750,0.0168),
(1009,0.3,0.3918,0.1852),(1009,0.5,0.2469,0.0994),(1009,0.7,0.1250,0.0497),(1009,0.9,0.0563,0.0136),
(2003,0.3,0.3476,0.1704),(2003,0.5,0.2138,0.0944),(2003,0.7,0.1053,0.0485),(2003,0.9,0.0411,0.0126),
]
print('P c maxR sum1q max/sum1q max/log1c max*sqrt(logP)')
for P,c,m,s in rows:
    print(P,c,round(m,4),round(s,4),round(m/s,3),round(m/math.log(1/c),3),round(m*math.sqrt(math.log(P)),3))
print('\nby c: max over P')
for c in sorted(set(r[1] for r in rows)):
    sub=[r for r in rows if r[1]==c]
    print(c, 'maxR sequence', [(P,round(m,4)) for P,_,m,_ in sub], 'max m/s', round(max(m/s for _,_,m,s in sub),3))
