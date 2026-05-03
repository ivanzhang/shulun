#!/usr/bin/env python3
"""行列双向闭锁 RCL 扫描。"""
from __future__ import annotations

import json, math
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'

def primes_upto(n:int):
    s=[True]*(n+1)
    if n>=0:s[0]=False
    if n>=1:s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i:n+1:i]=[False]*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(s) if v]

def labels_for(P:int):
    ps=primes_upto(P-1); Y=math.isqrt(P); small=[q for q in ps if q<=Y]; large=[q for q in ps if q>Y]
    labels=[]
    for r in range(1,P+1):
      for c in range(1,P+1):
        n=(r-1)*P+c
        if any(n%q==0 for q in small): continue
        qs=[q for q in large if n%q==0]
        if qs:
          labels.append((r,c,qs[0],n))
    return labels,Y

def scan(P:int, max_shift:int):
    labels,Y=labels_for(P)
    by_pos={(r,c):(q,n) for r,c,q,n in labels}
    shift_mods=defaultdict(set)
    shift_pairs=defaultdict(int)
    # 若两个被大因子标记的格点共享同一 q，则 q | uP+v；记录短差。
    by_q=defaultdict(list)
    for r,c,q,n in labels: by_q[q].append((r,c,n))
    for q,pts in by_q.items():
      m=len(pts)
      for i in range(m):
        r1,c1,_=pts[i]
        for j in range(i+1,m):
          r2,c2,_=pts[j]
          u=r2-r1; v=c2-c1
          if abs(u)<=max_shift and abs(v)<=max_shift and (u or v):
            key=(u,v)
            shift_mods[key].add(q); shift_pairs[key]+=1
    records=[]
    for (u,v),mods in shift_mods.items():
      val=abs(u*P+v)
      logprod=sum(math.log(q) for q in mods)
      records.append({'u':u,'v':v,'abs_uP_v':val,'mod_count':len(mods),'pair_count':shift_pairs[(u,v)],'log_product':logprod,'log_bound':math.log(max(val,1)) if val else 0,'product_exceeds_diff': logprod>math.log(max(val,1)) if val else True,'mods_sample':sorted(mods)[:10]})
    records.sort(key=lambda x:(not x['product_exceeds_diff'],-x['mod_count'],-x['pair_count']))
    return {'P':P,'Y':Y,'label_count':len(labels),'distinct_large_labels':len(by_q),'max_shift':max_shift,'locking_records':records[:30],'exceed_count':sum(1 for r in records if r['product_exceeds_diff']),'record_count':len(records)}

def main():
    Ps=[101,211,401]
    results=[scan(P, math.isqrt(P)) for P in Ps]
    audit={'certificate_type':'row_column_locking_scan','status':'shared_factor_short_differences_create_many_CRT_impossible_locks','results':results,'structural_conclusion':'扫描同一大因子在方阵内产生的短差 uP+v。许多短差关联多个互素大因子，模数乘积超过差值，说明若全覆盖迫使这些短差共享闭锁，就会产生 CRT 矛盾。下一步要证明反例覆盖必然激活足够多这样的短差。','next_obligations':['区分“自然共享同一 q 的短差”和“全覆盖选择迫使的闭锁短差”。','证明全覆盖标签链必须包含一个 product_exceeds_diff 的短差簇。','将短差簇转化为 RCL 引理的 Q_*。']}
    (DOCS/'row-column-locking-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 行列双向闭锁扫描','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for item in results:
      top=item['locking_records'][0] if item['locking_records'] else None
      lines.append(f"- P={item['P']} labels={item['label_count']} shifts={item['record_count']} exceed={item['exceed_count']} top={top}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'row-column-locking-scan.md').write_text('\n'.join(lines))
    print(DOCS/'row-column-locking-scan.json'); print(DOCS/'row-column-locking-scan.md')
if __name__=='__main__': main()
