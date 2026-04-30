#!/usr/bin/env python3
"""显式 P0 阈值机械抽取器。

用法示例：
  python3 experiments/extract_p0.py --template > docs/explicit-p0-constants.template.json
  python3 experiments/extract_p0.py --constants docs/explicit-p0-constants.json --max-log 1000

说明：
  本脚本只在所有原子常数已经由论文证明/引用显式给出后，机械搜索阈值。
  若缺少常数，会直接报错，避免伪造 P0。
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

REQUIRED = {
    "delta_BG_multilinear": None,
    "C_BG_multilinear": None,
    "delta_BG_bilinear": None,
    "C_BG_bilinear": None,
    "C_vaughan_blocks": None,
    "C_rect_variation": None,
    "C_divisor_coeff": None,
    "C_selberg_2linear": None,
    "C_selberg_remainder": None,
    "c_R": None,
    "C_sieve": None,
    "eta": None,
    "rho_tail": None,
    "B_log": None,
    "A_star": None,
    "finite_verified_logP": 0.0,
    "epsilon_C": 0.01,
    "use_direct_c_zone_certificate": False,
    "C_zone_direct_logP": None,
    "tail_error_power": 2.0,
    "use_baker_only": False,
    "delta_Baker_prime_or_bilinear": None,
    "C_Baker_prime_or_bilinear": None,
    "baker_range_theta": None,
    "use_three_interface_pack": False,
    "C_baker_spectrum_low_middle": None,
    "delta_baker_spectrum_low_middle": None,
    "epsilon_baker_spectrum_low_middle": None,
    "theta_baker_spectrum_max": None,
    "C_reciprocal_spectrum_transversal": None,
    "kappa_reciprocal_spectrum": None,
    "epsilon_reciprocal_spectrum": None,
    "C_high_theta_frequency_average": None,
    "delta_high_theta_frequency_average": None,
    "C_uniform_alpha_near_critical": None,
    "alpha_uniform_near_critical": None,
    "delta_uniform_near_critical": None,
    "C_fourth_spectrum_saving": None,
    "eta_fourth_spectrum_saving": None,
    "C_high_moment_spectrum_saving": None,
    "moment_order_2r": None,
    "eta_high_moment_spectrum_saving": None,
    "include_parseval_background_f4s": True,
    "C_weil_completion": None,
    "A_weil_completion_log": None,
    "K_sieve_log_saving": None,
    "C_f4s_background": None,
    "critical_overlap_margin": None,
    "C_bri4_incidence": None,
    "eta_bri4_incidence": None,
    "C_reu4_energy": None,
    "eta_reu4_energy": None,
    "use_omr_pack": False,
    "use_structured_ehpd": False,
    "C_OMR_layer": None,
    "C_OMR_model": None,
    "C_OMR_projection": None,
    "kappa_OMR": None,
    "A_OMR_log": None,
    "epsilon_OMR_power": None,
    "C_CGTP": None,
    "A_CGTP_log": None,
    "C_LSMP": None,
    "A_LSMP_log": None,
    "C_collision_span": None,
    "A_collision_span_log": None,
}

POSITIVE = [
    "delta_BG_multilinear",
    "C_BG_multilinear",
    "delta_BG_bilinear",
    "C_BG_bilinear",
    "C_vaughan_blocks",
    "C_rect_variation",
    "C_divisor_coeff",
    "C_selberg_2linear",
    "C_selberg_remainder",
    "c_R",
    "C_sieve",
    "B_log",
    "A_star",
    "tail_error_power",
]

THREE_INTERFACE_POSITIVE = [
    "C_baker_spectrum_low_middle",
    "delta_baker_spectrum_low_middle",
    "epsilon_baker_spectrum_low_middle",
    "theta_baker_spectrum_max",
    "C_reciprocal_spectrum_transversal",
    "kappa_reciprocal_spectrum",
    "epsilon_reciprocal_spectrum",
    "C_high_theta_frequency_average",
    "delta_high_theta_frequency_average",
    "C_uniform_alpha_near_critical",
    "alpha_uniform_near_critical",
    "delta_uniform_near_critical",
    "C_fourth_spectrum_saving",
    "eta_fourth_spectrum_saving",
    "C_high_moment_spectrum_saving",
    "moment_order_2r",
    "eta_high_moment_spectrum_saving",
    "C_weil_completion",
    "A_weil_completion_log",
    "K_sieve_log_saving",
    "C_f4s_background",
    "critical_overlap_margin",
    "C_bri4_incidence",
    "eta_bri4_incidence",
    "C_reu4_energy",
    "eta_reu4_energy",
]

OMR_POSITIVE = [
    "C_OMR_layer",
    "C_OMR_model",
    "C_OMR_projection",
    "kappa_OMR",
    "A_OMR_log",
    "epsilon_OMR_power",
    "C_CGTP",
    "A_CGTP_log",
    "C_LSMP",
    "A_LSMP_log",
    "C_collision_span",
    "A_collision_span_log",
]


def load_constants(path: Path) -> dict[str, float]:
    """读取并校验显式常数。"""
    data: dict[str, Any] = json.loads(path.read_text())
    use_baker_only = bool(data.get("use_baker_only", False))
    use_three_interface_pack = bool(data.get("use_three_interface_pack", False))
    use_omr_pack = bool(data.get("use_omr_pack", False))
    required_keys = list(REQUIRED)
    three_interface_keys = set(THREE_INTERFACE_POSITIVE) | {"use_three_interface_pack"}
    use_structured_ehpd = bool(data.get("use_structured_ehpd", False))
    omr_keys = set(OMR_POSITIVE) | {"use_omr_pack", "use_structured_ehpd"}
    if use_three_interface_pack:
        required_keys = [
            key for key in required_keys
            if key not in {
                "delta_BG_multilinear",
                "C_BG_multilinear",
                "delta_BG_bilinear",
                "C_BG_bilinear",
                "delta_Baker_prime_or_bilinear",
                "C_Baker_prime_or_bilinear",
                "baker_range_theta",
            }
        ]
    elif use_structured_ehpd:
        required_keys = [
            key for key in required_keys
            if key not in {
                "delta_BG_multilinear",
                "C_BG_multilinear",
                "delta_BG_bilinear",
                "C_BG_bilinear",
                "delta_Baker_prime_or_bilinear",
                "C_Baker_prime_or_bilinear",
                "baker_range_theta",
            } | three_interface_keys
        ]
        required_keys.append("use_omr_pack")
    elif use_baker_only:
        required_keys = [key for key in required_keys if key not in {"delta_BG_multilinear", "C_BG_multilinear", "delta_BG_bilinear", "C_BG_bilinear"} | three_interface_keys]
    else:
        required_keys = [key for key in required_keys if key not in {"delta_Baker_prime_or_bilinear", "C_Baker_prime_or_bilinear", "baker_range_theta"} | three_interface_keys]
    if not use_omr_pack:
        required_keys = [key for key in required_keys if key not in omr_keys]
    if use_structured_ehpd and not use_omr_pack:
        raise SystemExit("use_structured_ehpd=true 时必须同时 use_omr_pack=true。")
    missing = [key for key in required_keys if (key not in data and REQUIRED[key] is None) or data.get(key, REQUIRED[key]) is None]
    if missing:
        raise SystemExit("缺少原子常数，不能抽取 P0：" + ", ".join(missing))
    constants = {}
    for key in REQUIRED:
        value = data.get(key, REQUIRED[key])
        if isinstance(value, bool):
            constants[key] = value
        elif value is None:
            constants[key] = 0.0
        else:
            constants[key] = float(value)
    positive_keys = list(POSITIVE)
    if use_three_interface_pack:
        positive_keys = [key for key in positive_keys if key not in {"delta_BG_multilinear", "C_BG_multilinear", "delta_BG_bilinear", "C_BG_bilinear"}]
        positive_keys += THREE_INTERFACE_POSITIVE
    elif use_structured_ehpd:
        positive_keys = [key for key in positive_keys if key not in {"delta_BG_multilinear", "C_BG_multilinear", "delta_BG_bilinear", "C_BG_bilinear"}]
    elif use_baker_only:
        positive_keys = [key for key in positive_keys if key not in {"delta_BG_multilinear", "C_BG_multilinear", "delta_BG_bilinear", "C_BG_bilinear"}]
        positive_keys += ["delta_Baker_prime_or_bilinear", "C_Baker_prime_or_bilinear", "baker_range_theta"]
    if use_omr_pack:
        positive_keys += OMR_POSITIVE
    bad = [key for key in positive_keys if constants[key] <= 0]
    if bad:
        raise SystemExit("以下常数必须为正：" + ", ".join(bad))
    if not (0 < constants["eta"] < 0.5):
        raise SystemExit("eta 必须位于 (0, 1/2)。")
    if bool(constants.get("use_direct_c_zone_certificate", False)):
        if constants["C_zone_direct_logP"] <= 0:
            raise SystemExit("启用 C 区直接证书时，C_zone_direct_logP 必须为正。")
    if not (0 < constants["rho_tail"] and 2 * constants["rho_tail"] <= constants["eta"]):
        raise SystemExit("rho_tail 必须满足 0<rho_tail 且 2*rho_tail<=eta。")
    if constants["A_star"] <= 1:
        raise SystemExit("A_star 必须大于 1。")
    if use_three_interface_pack:
        if constants["theta_baker_spectrum_max"] >= 0.625:
            raise SystemExit("theta_baker_spectrum_max 必须严格小于 5/8，需给 Baker 大谱留余量。")
        if constants["kappa_reciprocal_spectrum"] >= 5:
            raise SystemExit("kappa_reciprocal_spectrum 必须小于 5，才是对 Baker 任意频率大谱的真改进。")
        if not (0 < constants["alpha_uniform_near_critical"] < 0.125):
            raise SystemExit("alpha_uniform_near_critical 应为小的正数。")
        if constants["moment_order_2r"] < 4 or constants["moment_order_2r"] % 2 != 0:
            raise SystemExit("moment_order_2r 必须是不小于 4 的偶数。")
        if not bool(constants["include_parseval_background_f4s"]):
            raise SystemExit("F4S 必须包含 Parseval 背景项 D*M^4/P，不能关闭。")
        if constants["K_sieve_log_saving"] <= 2.0 * constants["A_weil_completion_log"] + constants["critical_overlap_margin"]:
            raise SystemExit("K_sieve_log_saving 必须大于 2*A_weil_completion_log 加临界拼接余量。")
    if use_omr_pack:
        if constants["kappa_OMR"] >= 1:
            raise SystemExit("kappa_OMR 应为小于 1 的显式增量常数。")
        if constants["epsilon_OMR_power"] <= 4:
            raise SystemExit("epsilon_OMR_power 必须大于 4，以匹配 ε_OMR<=Λ^4 的安全余量。")
        if constants["A_LSMP_log"] + constants["A_CGTP_log"] + constants["A_collision_span_log"] >= constants["K_sieve_log_saving"]:
            raise SystemExit("OMR/CGTP/LSMP/碰撞账本对数损失必须小于 K_sieve_log_saving。")
    return constants


def ok_at_logx(y: float, c: dict[str, float]) -> bool:
    """在 y=log P 下检查所有阈值不等式。"""
    loglog = math.log(y)
    log_loss = c["C_vaughan_blocks"] + c["C_rect_variation"] + c["C_divisor_coeff"]

    # BG/三接口幂节省压过全部对数损失。
    if c.get("use_three_interface_pack", False):
        checks = [
            ("low_middle", c["C_baker_spectrum_low_middle"], c["delta_baker_spectrum_low_middle"]),
            ("transversal", c["C_reciprocal_spectrum_transversal"], max(1e-12, (5.0 - c["kappa_reciprocal_spectrum"]) / 100.0)),
            ("high_theta", c["C_high_theta_frequency_average"], c["delta_high_theta_frequency_average"]),
            ("near_critical", c["C_uniform_alpha_near_critical"], c["delta_uniform_near_critical"]),
            ("fourth_spectrum", c["C_fourth_spectrum_saving"], c["eta_fourth_spectrum_saving"]),
            ("high_moment_spectrum", c["C_high_moment_spectrum_saving"], c["eta_high_moment_spectrum_saving"]),
            ("weil_completion", c["C_weil_completion"], max(1e-12, c["critical_overlap_margin"] / 100.0)),
            ("f4s_background", c["C_f4s_background"], max(1e-12, c["critical_overlap_margin"] / 100.0)),
            ("bri4_incidence", c["C_bri4_incidence"], c["eta_bri4_incidence"]),
            ("reu4_energy", c["C_reu4_energy"], c["eta_reu4_energy"]),
        ]
        for _name, const, delta in checks:
            if math.log(const) - delta * y + (log_loss + c["A_star"]) * loglog > 0:
                return False
    if c.get("use_omr_pack", False):
        # OMR+CGTP+LSMP 包恢复 Λ^2 门槛；这里只检查对数损失可被筛节省吸收。
        omr_log_loss = (
            c["A_OMR_log"]
            + c["A_CGTP_log"]
            + c["A_LSMP_log"]
            + c["A_collision_span_log"]
            + c["C_OMR_layer"]
            + c["C_OMR_projection"]
            + c["C_CGTP"]
            + c["C_LSMP"]
            + c["C_collision_span"]
        )
        if c["epsilon_OMR_power"] * loglog <= (omr_log_loss + c["A_star"]) * math.log(max(loglog, 2.0)):
            return False
    elif c.get("use_structured_ehpd", False):
        # 结构化路线已由 OMR 包提供 Λ² 门槛；不再要求 BG/Baker 幂节省。
        pass
    elif c.get("use_baker_only", False):
        baker = math.log(c["C_Baker_prime_or_bilinear"]) - c["delta_Baker_prime_or_bilinear"] * y + (log_loss + c["A_star"]) * loglog
        if baker > 0:
            return False
    else:
        bg_multi = math.log(c["C_BG_multilinear"]) - c["delta_BG_multilinear"] * y + (log_loss + c["A_star"]) * loglog
        bg_bilin = math.log(c["C_BG_bilinear"]) - c["delta_BG_bilinear"] * y + (log_loss + c["A_star"]) * loglog
        if bg_multi > 0 or bg_bilin > 0:
            return False

    # C 区：默认使用渐近平凡估计；若有直接证书，可在证书范围内跳过该渐近门槛。
    if not (c.get("use_direct_c_zone_certificate", False) and y <= c["C_zone_direct_logP"]):
        eps = c["epsilon_C"]
        c_zone = (11.0 / 12.0 + eps - 1.0) * y + (log_loss + c["A_star"]) * loglog
        if c_zone > 0:
            return False

    # 尾部误差：用抽象 log^{-tail_error_power} 代表显式化后的低/中谱余项。
    if c["tail_error_power"] <= c["A_star"]:
        return False

    # 主体常数账本。
    h0 = c["c_R"] / (4.0 * c["C_sieve"])
    delta = c["c_R"] / 16.0
    lhs = c["C_sieve"] * h0 + (1.0 - c["c_R"]) * (1.0 - h0)
    if lhs > 1.0 - 2.0 * delta:
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", action="store_true", help="输出常数模板 JSON")
    parser.add_argument("--constants", type=Path, help="显式常数 JSON 文件")
    parser.add_argument("--min-log", type=float, default=3.0, help="搜索 log(P) 下界")
    parser.add_argument("--max-log", type=float, default=10000.0, help="搜索 log(P) 上界")
    parser.add_argument("--step", type=float, default=0.1, help="log(P) 搜索步长")
    args = parser.parse_args()

    if args.template:
        print(json.dumps(REQUIRED, ensure_ascii=False, indent=2))
        return 0
    if args.constants is None:
        raise SystemExit("请提供 --constants，或使用 --template 生成模板。")

    c = load_constants(args.constants)
    y = args.min_log
    while y <= args.max_log:
        if ok_at_logx(y, c):
            print(json.dumps({"log_P0_upper": y, "P0_upper_exp_form": f"exp({y:.6g})"}, ensure_ascii=False, indent=2))
            return 0
        y += args.step
    raise SystemExit(f"在 log(P)<={args.max_log} 内未找到阈值；请增大 --max-log 或检查常数。")


if __name__ == "__main__":
    raise SystemExit(main())
