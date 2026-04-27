#!/usr/bin/env python3
"""2q 链的 B11 禁区密度模型。"""
import argparse
from collections import Counter

M_ODD = 3 * 5 * 7 * 11
SMALL = (3, 5, 7, 11)


def allowed_pattern(q, offset):
    """返回 t 周期内 offset+2qt 是否避开 3,5,7,11。"""
    step = 2 * q
    return [all((offset + step * t) % p for p in SMALL) for t in range(M_ODD)]


def window_maxima(pattern, max_span_t):
    """返回长度 1..max_span_t+1 的周期窗口最大允许点数。"""
    n = len(pattern)
    total = sum(pattern)
    doubled = pattern + pattern
    pref = [0]
    for value in doubled:
        pref.append(pref[-1] + int(value))
    out = []
    for span_t in range(max_span_t + 1):
        length = span_t + 1
        full, rem = divmod(length, n)
        base = full * total
        if rem == 0:
            out.append((span_t, base))
        else:
            out.append((span_t, base + max(pref[i + rem] - pref[i] for i in range(n))))
    return out


def q_stats(q, max_span_t=20):
    records = []
    density_hist = Counter()
    best_span = [(span_t, 0) for span_t in range(max_span_t + 1)]
    # offset 只需模 M_ODD；奇偶已由 r-c 为奇数保证，2q*t 不改变奇偶。
    for offset in range(M_ODD):
        pattern = allowed_pattern(q, offset)
        cnt = sum(pattern)
        density_hist[cnt] += 1
        records.append((cnt, offset, pattern))
        spans = window_maxima(pattern, max_span_t)
        best_span = [(s, max(v, spans[s][1])) for s, v in best_span]
    records.sort(reverse=True)
    return density_hist, records[0], best_span


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--q', type=int, default=13)
    parser.add_argument('--q-list', default='')
    parser.add_argument('--show', type=int, default=20)
    parser.add_argument('--max-span-t', type=int, default=20)
    args = parser.parse_args()
    qs = [int(x) for x in args.q_list.split(',') if x.strip()] if args.q_list else [args.q]
    for q in qs:
        hist, best, span_rows = q_stats(q, args.max_span_t)
        cnt, offset, pattern = best
        print('q', q, 'period', M_ODD, 'density_hist_allowed_count', sorted(hist.items()), 'best_count', cnt, 'best_density', f'{cnt/M_ODD:.6f}', 'best_offset', offset)
        print('span_t max_allowed_hits', span_rows[:args.show])
        print('best_pattern_first80', ''.join('1' if x else '0' for x in pattern[:80]))
        print('---')


if __name__ == '__main__':
    main()
