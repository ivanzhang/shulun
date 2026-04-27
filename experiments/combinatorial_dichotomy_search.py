#!/usr/bin/env python3
"""纯组合穷举 R/M 段序列，检验分型判别的可证明版本。

模型：段链 R^{a1} M^{b1} ... R^{as}，ai,bi>=1。
能量 E = sum(ai-1)+sum(max(0,bi-2))+distinct_shapes。
交替长度 alt 为展开 R/M 字符串的最长交替子串长度。

用法示例：
  python3 experiments/combinatorial_dichotomy_search.py --max-s 8 --max-len 5
"""
import argparse
from itertools import product


def expand(a_list, b_list):
    """展开为 R/M 字符串。"""
    out = []
    for i, a in enumerate(a_list):
        out.extend("R" for _ in range(a))
        if i < len(b_list):
            out.extend("M" for _ in range(b_list[i]))
    return "".join(out)


def max_alt_len(word):
    """最长交替子串。"""
    best = 0
    cur = 0
    prev = None
    for ch in word:
        if prev is None or ch != prev:
            cur += 1
        else:
            cur = 1
        best = max(best, cur)
        prev = ch
    return best


def energy(a_list, b_list):
    """组合能量。"""
    r_internal = sum(a - 1 for a in a_list)
    m_deep = sum(max(0, b - 2) for b in b_list)
    shapes = set((a_list[i], b_list[i], a_list[i + 1]) for i in range(len(b_list)))
    return r_internal + m_deep + len(shapes)


def search(max_s, max_len, coef, alt_divisor):
    """搜索反例：E <= coef*s 且 alt < s/alt_divisor。"""
    bad = []
    for s in range(2, max_s + 1):
        for a_list in product(range(1, max_len + 1), repeat=s):
            for b_list in product(range(1, max_len + 1), repeat=s - 1):
                e = energy(a_list, b_list)
                alt = max_alt_len(expand(a_list, b_list))
                if e <= coef * s and alt < max(3, s // alt_divisor):
                    bad.append((s, e, alt, a_list, b_list, expand(a_list, b_list)))
                    if len(bad) >= 20:
                        return bad
    return bad


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-s", type=int, default=8)
    parser.add_argument("--max-len", type=int, default=5)
    parser.add_argument("--coef", type=float, default=2.0)
    parser.add_argument("--alt-divisor", type=int, default=2)
    args = parser.parse_args()
    bad = search(args.max_s, args.max_len, args.coef, args.alt_divisor)
    print(f"checked max_s={args.max_s} max_len={args.max_len} coef={args.coef} alt_divisor={args.alt_divisor} bad={len(bad)}")
    for row in bad:
        s, e, alt, a, b, word = row
        print(f"s={s} E={e} alt={alt} a={a} b={b} word={word}")


if __name__ == "__main__":
    main()
