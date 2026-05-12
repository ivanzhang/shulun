// table_012 logl 与 MPFR 点审计器。
//
// 用法示例：
//   g++ -O2 -std=c++17 -Wall -Wextra -o /tmp/table012_logl_mpfr_point_audit
//     experiments/prime_matrix_table012_logl_mpfr_point_audit.cpp -lmpfr -lgmp
//
//   /tmp/table012_logl_mpfr_point_audit 100000000 179845447 800000000000
//
// 说明：
//   该工具只审计给定整数点的 std::log(long double) 与 MPFR 高精度 log 的差。
//   它是证据审计，不是全域证明；全域闭合仍需要 libm 源码误差证明或 MPFR 全量重扫。

#include <cmath>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <string>

#include <mpfr.h>

namespace {

constexpr mpfr_prec_t MPFR_PRECISION = 256;
constexpr const char *THRESHOLD = "1e-12";

unsigned long long parse_ull(const char *text) {
  char *end = nullptr;
  const unsigned long long value = std::strtoull(text, &end, 10);
  if (end == text || *end != '\0') {
    throw std::runtime_error(std::string("bad integer: ") + text);
  }
  return value;
}

std::string mpfr_sci(const mpfr_t value) {
  char buffer[256];
  mpfr_snprintf(buffer, sizeof(buffer), "%.50Re", value);
  return std::string(buffer);
}

void audit_one(unsigned long long n) {
  mpfr_t exact_arg;
  mpfr_t exact_log;
  mpfr_t logl_value;
  mpfr_t diff;
  mpfr_t abs_diff;
  mpfr_t threshold;
  mpfr_inits2(MPFR_PRECISION, exact_arg, exact_log, logl_value, diff, abs_diff, threshold, nullptr);

  const std::string n_text = std::to_string(n);
  mpfr_set_str(exact_arg, n_text.c_str(), 10, MPFR_RNDN);
  mpfr_log(exact_log, exact_arg, MPFR_RNDN);

  const long double native_log = std::log(static_cast<long double>(n));
  mpfr_set_ld(logl_value, native_log, MPFR_RNDN);
  mpfr_sub(diff, logl_value, exact_log, MPFR_RNDN);
  mpfr_abs(abs_diff, diff, MPFR_RNDN);
  mpfr_set_str(threshold, THRESHOLD, 10, MPFR_RNDN);
  const bool passed = mpfr_cmp(abs_diff, threshold) <= 0;

  std::cout
      << "{\"record_type\":\"table012_logl_mpfr_point\""
      << ",\"n\":" << n
      << ",\"mpfr_precision_bits\":" << MPFR_PRECISION
      << ",\"logl_value\":\"" << mpfr_sci(logl_value) << "\""
      << ",\"mpfr_log\":\"" << mpfr_sci(exact_log) << "\""
      << ",\"signed_error\":\"" << mpfr_sci(diff) << "\""
      << ",\"abs_error\":\"" << mpfr_sci(abs_diff) << "\""
      << ",\"threshold\":\"" << THRESHOLD << "\""
      << ",\"passed\":" << (passed ? "true" : "false")
      << "}\n";

  mpfr_clears(exact_arg, exact_log, logl_value, diff, abs_diff, threshold, nullptr);
}

}  // namespace

int main(int argc, char **argv) {
  try {
    if (argc < 2) {
      std::cerr << "usage: " << argv[0] << " N [N...]\n";
      return 2;
    }
    for (int i = 1; i < argc; ++i) {
      audit_one(parse_ull(argv[i]));
    }
  } catch (const std::exception &exc) {
    std::cerr << exc.what() << "\n";
    return 1;
  }
  return 0;
}
