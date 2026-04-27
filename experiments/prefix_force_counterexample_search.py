#!/usr/bin/env python3
"""前缀强制定理的反例搜索。

搜索是否存在真实骨架达到 saving>=S，但按容量排序的前 k 前缀仍有幸存素数 P<=X。
若找不到，给出搜索束内的正证据；若找到，输出反例前缀和幸存 P。

注意：这是搜索器，不是完整证明器。通过提高 beam/state_limit/residue_limit 可增强覆盖。

用法示例：
    python3 experiments/prefix_force_counterexample_search.py --c 109 --W 100 --S 55 --X 1000000 --k 10 --stateLimit 5000 --residueLimit 12
"""
import argparse
import math
import sys

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prefix_barrier_library import prefix_key, survivor_count
from skeleton_union_bound import q_residue_options


def residue_rows_ranked(opts, residue_limit):
    """按容量优先截断每个 q 的真实余数类。"""
    rows = []
    for q, residue_rows in opts:
        ranked = sorted(residue_rows, key=lambda row: (-row[2], row[1]))
        if residue_limit:
            ranked = ranked[:residue_limit]
        rows.append((q, ranked))
    rows.sort(key=lambda item: (-max(row[2] for row in item[1]), item[0]))
    return rows


def state_signature(chosen, keep):
    """保留前若干高容量项作为去重签名。"""
    ordered = sorted(chosen, key=lambda row: (-row[2], row[0], row[1]))
    return tuple((row[0], row[1], row[2]) for row in ordered[:keep])


def search(c, W, S, X, k, state_limit, residue_limit, keep_signature):
    holes = holes_for_c(c, W)
    opts = q_residue_options(holes)
    rows = residue_rows_ranked(opts, residue_limit)
    primes = primes_upto(X)

    states = [(0, [])]
    checked_prefixes = {}
    best_saving = 0
    for q, choices in rows:
        new_states = states[:]
        for saving, chosen in states:
            for row in choices:
                ns = saving + row[2]
                nchosen = chosen + [row]
                if ns >= S and len(nchosen) >= k:
                    key, prefix = prefix_key(nchosen, k)
                    if key not in checked_prefixes:
                        count, min_ratio, first = survivor_count(prefix, primes, stop_after=0)
                        checked_prefixes[key] = (count, min_ratio, first, prefix, nchosen)
                        if count > 0:
                            return {
                                'found': True,
                                'q': q,
                                'saving': ns,
                                'prefix_key': key,
                                'survivor_count_seen': count,
                                'min_ratio': min_ratio,
                                'first': first,
                                'chosen': nchosen,
                                'checked_prefixes': len(checked_prefixes),
                            }
                else:
                    new_states.append((ns, nchosen))
                if ns > best_saving:
                    best_saving = ns
        # 去重并限制状态数：优先高 saving，其次前缀小模数/高容量稳定。
        dedup = {}
        for saving, chosen in new_states:
            sig = (saving, state_signature(chosen, keep_signature))
            if sig not in dedup or len(chosen) < len(dedup[sig]):
                dedup[sig] = chosen
        compact = [(saving, chosen) for (saving, _), chosen in dedup.items()]
        compact.sort(key=lambda item: (-item[0], len(item[1])))
        states = compact[:state_limit]
    return {
        'found': False,
        'best_saving': best_saving,
        'states': len(states),
        'checked_prefixes': len(checked_prefixes),
        'zero_checked': sum(1 for val in checked_prefixes.values() if val[0] == 0),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=109)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--X', type=int, default=1_000_000)
    parser.add_argument('--k', type=int, default=10)
    parser.add_argument('--stateLimit', type=int, default=5000)
    parser.add_argument('--residueLimit', type=int, default=12)
    parser.add_argument('--keepSignature', type=int, default=12)
    args = parser.parse_args()

    result = search(args.c, args.W, args.S, args.X, args.k, args.stateLimit, args.residueLimit, args.keepSignature)
    print('params', vars(args))
    print('result_found', result['found'])
    for key, value in result.items():
        if key in {'chosen'}:
            compact = [(row[0], row[1], row[2]) for row in value]
            print(key, compact)
        else:
            print(key, value)


if __name__ == '__main__':
    main()
