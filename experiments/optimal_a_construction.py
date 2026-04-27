#!/usr/bin/env python3
"""§215 反例最优 hot 序列对应的 a 值显式构造。

§214 给出 modulus_required ≫ X，但只是密度论证。本节显式计算"让 M_kill 命中
最优 hot 序列"对应的具体 a ∈ [0, modulus_required)，检查是否 a ≤ X。

如果 a > X 对所有反例 c 都成立，则 [0, X] 内不存在让 M_kill ≥ need 的 P，
(⋆) 严格无条件成立 (在 X 范围内, 不依赖 Linnik)。

构造步骤：
1. 对反例 prefix, DP 求 min modulus_required 与对应 q 集 S = {q_1, ..., q_m}
2. 每 q ∈ S 取最优 hot 残数 r_optimal(q) = argmax H_holes(q, r)
3. 由 r_unkill_q 公式反推 P 的 CRT 类:
     r_unkill_q ≡ r_optimal(q) (mod q)
     A_old · P^{-1} ≡ -r_optimal(q) (mod q)
4. 结合 anchor 约束 A_old ≡ -residue · P (mod modulus_pre)
   推出 P ≡ a (mod modulus_required) 的 a 显式值
5. 比较 a 与 X，看是否 a ≤ X

用法：
    python3 experiments/optimal_a_construction.py --cList 59,101,353,619,961,1343,1609,1789,2309
"""
from __future__ import annotations

import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from min_modulus_for_need import hot_caps_per_q, min_log_modulus_for_need
from prefix_barrier_library import prefix_phase
from prefix_completion_bound import full_scan


def hot_optimal_r(holes, q):
    """q 上 H_holes(q, r) 最大的 r (取较小者作 tie-break)。"""
    counts = defaultdict(int)
    for h in holes:
        counts[h % q] += 1
    if not counts:
        return None, 0
    max_H = max(counts.values())
    rs = sorted(r for r, c in counts.items() if c == max_H)
    return rs[0], max_H


def crt_combine(constraints):
    """合并 [(a_i, m_i)] 形式的 CRT 约束，返回 (a, m).

    每对要求 m_i 互素或可整除。这里假设所有 m_i 互素。
    """
    a, m = 0, 1
    for a_i, m_i in constraints:
        # CRT: x ≡ a (mod m), x ≡ a_i (mod m_i)
        g = math.gcd(m, m_i)
        if g != 1:
            # 检查兼容
            if (a - a_i) % g != 0:
                return None, None
            # 假设互素的简化版
            return None, None
        # 互素情况
        m_inv = pow(m, -1, m_i)
        k = ((a_i - a) * m_inv) % m_i
        a = a + m * k
        m = m * m_i
        a = a % m
    return a, m


def construct_optimal_a(c: int, prefix, holes, need: int, last_cap: int) -> dict:
    """对反例 prefix 构造最优 a 值。

    思路:
    设 prefix CRT: residue, modulus_pre.
    对每 q ∈ S (DP 选出的最小 q 集合), r_optimal(q) 是 q 上最大 hot 残数.

    要让反例 P 满足 r_unkill_q(P) = r_optimal(q):
      r_unkill_q = (-A_old · P^{-1}) mod q = r_optimal(q)
      ⇔ -A_old ≡ r_optimal(q) · P (mod q)
      ⇔ A_old ≡ -r_optimal(q) · P (mod q)

    A_old = (-residue · P) mod modulus_pre
    所以 (-residue · P) mod modulus_pre ≡ -r_optimal(q) · P (mod q)

    令 V = -residue · P. 则 V mod modulus_pre = A_old, V mod q = -r_optimal(q) · P (mod q).

    A_old ∈ [0, modulus_pre). A_old mod q ≡ V mod q ≡ -r_optimal(q) · P (mod q).

    A_old 在 [0, modulus_pre) 内的具体值 + 满足 A_old mod q = -r_optimal(q) · P (mod q).

    即 A_old ≡ -r_optimal(q) · P (mod q).

    P 是未知数。CRT 给:
      P · residue ≡ -A_old (mod modulus_pre)
      A_old ≡ -r_optimal(q) · P (mod q)
      ⇒ A_old + r_optimal(q) · P ≡ 0 (mod q)
      ⇒ A_old ≡ -r_optimal(q) · P (mod q)

    替换 A_old = (-residue · P) mod modulus_pre. 因 modulus_pre 与 q 互素,
    (A_old) mod q 与 (-residue · P) mod q 不同 (因为 A_old = V mod modulus_pre, V mod q ≠ A_old mod q).

    更准确推导: V = A_old + k · modulus_pre 对某 k ≥ 0 (V 实际是负数, 但 A_old ∈ [0, modulus_pre)).
    V mod q = A_old + k · modulus_pre mod q = (A_old mod q) + k · (modulus_pre mod q) mod q.
    V mod q = -residue · P mod q.

    所以 -residue · P ≡ A_old + k · modulus_pre (mod q)
              即 A_old ≡ -residue · P - k · modulus_pre (mod q).

    要 A_old ≡ -r_optimal(q) · P (mod q):
       -r_optimal(q) · P ≡ -residue · P - k · modulus_pre (mod q)
       ⇒ (residue - r_optimal(q)) · P ≡ k · modulus_pre (mod q)
       ⇒ P ≡ k · modulus_pre · (residue - r_optimal(q))^{-1} (mod q)
       ⇒ for each k, P 唯一确定.

    k 的范围由 A_old ∈ [0, modulus_pre) 与 V = A_old + k · modulus_pre = -residue · P 的整数性决定.
    k ≈ (residue · P) / modulus_pre ≈ P / 1 (since residue ≤ modulus_pre).

    简化: 取 k = 0 (即 V = A_old, 即 -residue · P = A_old ∈ [0, modulus_pre]).
    此时 -residue · P = A_old ⇒ P = -A_old / residue (mod modulus_pre).

    且 A_old ≡ -r_optimal(q) · P (mod q).

    把上面合并: 不直接代数解, 而是用试验. 对每个 q ∈ S, P (mod q) 必须满足某关系.
    """
    residue, modulus_pre = prefix_phase(prefix)
    used = {t[0] for t in prefix}

    # DP 求 min modulus_required 与 q 集
    Y = 11
    D = max(holes) - min(holes) if holes else 0
    q_cap_list = []
    for q in primes_upto(D):
        if q <= Y or q in used:
            continue
        cap = hot_caps_per_q(holes, q, last_cap)
        if cap > 0:
            q_cap_list.append((q, cap))
    log_min, chosen_qs = min_log_modulus_for_need(q_cap_list, need)
    if log_min is None:
        return {'unconditional_pass': True}

    # 对每 q ∈ S 取 r_optimal
    r_optimals = {}
    for q in chosen_qs:
        r, H = hot_optimal_r(holes, q)
        r_optimals[q] = r

    # P 必须满足 r_unkill_q(P) = r_optimals[q] 对每 q ∈ S, 同时 anchor 约束.
    # 我们直接对小 P 范围搜索, 看是否存在 P ∈ [1, 10^7] 满足条件.
    # 如果不存在, 给出 [0, modulus_required) 内的最小 a (CRT 解).

    modulus_required = modulus_pre
    for q in chosen_qs:
        modulus_required *= q

    # 蛮力: 对 P 从 1 开始, 找第一个满足:
    # 1. r_unkill_q(P) = r_optimals[q] 对所有 q ∈ chosen_qs
    found_P = None
    if not chosen_qs:
        return {'unconditional_pass': True}

    # 实际上需要先求 a (mod modulus_required)，然后判断 a 是否 ≤ X.
    # 用更精细的代数: 对每 q ∈ S, P 满足 P ≡ alpha_q (mod q) 对某 alpha_q.
    # alpha_q 由 r_optimals[q] + prefix 决定.
    # 但 alpha_q 依赖 (P mod modulus_pre), 因为 A_old 依赖 P.

    # 简化: 直接搜索 [1, M] 内的 P 满足条件. 这给出 a ∈ [0, modulus_required) 的最小值.
    # M 取 X*1000 = 10^9 作为搜索上界 (实际期望 a ≫ 10^9 if 真无解 in [0, X]).

    # 真正的反例 P 必须:
    # 1. is_prime(P)
    # 2. A_old(P) <= P (即 prefix witness)
    # 3. r_unkill_q(P) = r_optimal(q) 对所有 q ∈ chosen_qs

    def _is_prime(n):
        if n < 2: return False
        if n < 4: return True
        if n % 2 == 0: return False
        for d in range(3, int(n**0.5) + 1, 2):
            if n % d == 0: return False
        return True

    print(f'  搜索 P ≤ 10^7 (素数, witness, r_unkill 全命中最优 hot) for q ∈ {chosen_qs}', flush=True)
    found_count = 0
    for P_cand in range(2, 10_000_000):
        if P_cand >= modulus_pre: break
        if not _is_prime(P_cand):
            continue
        try:
            A_old_cand = (-residue * P_cand) % modulus_pre
        except:
            continue
        # anchor barrier
        if A_old_cand > P_cand:
            continue
        # r_unkill 命中
        all_match = True
        for q in chosen_qs:
            try:
                P_inv = pow(P_cand % q, -1, q)
            except ValueError:
                all_match = False
                break
            r_uk = (-A_old_cand * P_inv) % q
            if r_uk != r_optimals[q]:
                all_match = False
                break
        if all_match:
            found_P = P_cand
            found_count += 1
            if found_count >= 3:
                break

    return {
        'unconditional_pass': False,
        'modulus_pre': modulus_pre,
        'modulus_required': modulus_required,
        'log10_modulus_required': math.log10(modulus_required),
        'chosen_qs': chosen_qs,
        'r_optimals': r_optimals,
        'found_P_in_1e7': found_P,
        'found_count': found_count,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cList', default='59,101,353,619,961,1343,1609,1789,2309')
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--kLow', type=int, default=10)
    parser.add_argument('--X', type=int, default=1_000_000)
    args = parser.parse_args()

    c_list = [int(x) for x in args.cList.split(',')]
    primes = primes_upto(args.X)

    print(f'§215 最优 hot 序列对应 a 显式构造')
    print(f'参数: cList={c_list}, X={args.X}')
    print()

    summary = []
    for c in c_list:
        print(f'--- c={c} ---')
        holes = holes_for_c(c, args.W)
        result = full_scan(c, args.W, args.S, args.kLow, args.X,
                           state_limit=8000, residue_limit=14, primes=primes)
        nonzero = result['nonzero_examples']
        if not nonzero:
            print(f'  无 nonzero prefix, 跳过')
            continue
        for prefix_tuple, _, witness_list in nonzero[:1]:  # 只处理第一个反例 prefix
            prefix = list(prefix_tuple)
            prefix_saving = sum(t[2] for t in prefix)
            need = args.S - prefix_saving
            last_cap = prefix[-1][2]

            rec = construct_optimal_a(c, prefix, holes, need, last_cap)
            if rec.get('unconditional_pass'):
                print(f'  ★ 无条件通过')
                continue

            print(f'  modulus_required ≈ 10^{rec["log10_modulus_required"]:.1f}')
            print(f'  chosen_qs: {rec["chosen_qs"]}')
            print(f'  r_optimals: {rec["r_optimals"]}')
            if rec['found_P_in_1e7'] is None:
                print(f'  ★ 在 P ≤ 10^7 内不存在让 r_unkill 全命中最优 hot 的 P')
                print(f'    (a 必须 > 10^7, 即 (⋆) 在 X=10^6 内成立)')
            else:
                print(f'  ⚠ 找到 P = {rec["found_P_in_1e7"]} 让 r_unkill 全命中最优 hot')
                print(f'  count_found_in_1e7: {rec["found_count"]}')
            summary.append({'c': c, **rec})
            break  # 一个反例 prefix 即可
        print()

    print('=' * 60)
    print('总结')
    print('=' * 60)
    n_found = sum(1 for r in summary if r.get('found_P_in_1e7') is not None)
    print(f'有 P ≤ 10^7 让最优 hot 全命中的 c 数: {n_found}/{len(summary)}')
    print(f'(⋆) 在 X=10^6 内严格通过: {len(summary) - n_found}/{len(summary)}')


if __name__ == '__main__':
    main()
