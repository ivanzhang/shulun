// strict 中段 psi 原生 range 批量输出器。
//
// 编译示例：
//   g++ -O2 -I/tmp/PsiTheta \
//     -o /tmp/PsiTheta/psi_range_jsonl \
//     experiments/prime_matrix_middle_psi_native_range_runner.cpp \
//     /tmp/PsiTheta/access.o /tmp/PsiTheta/bit_table.o /tmp/PsiTheta/primes.o \
//     /tmp/PsiTheta/psi.o /tmp/PsiTheta/theta.o \
//     -lgmpxx -lgmp -lmpfr
//
// 运行示例：
//   /tmp/PsiTheta/psi_range_jsonl 0 1 30 21f4f6553851f218801a733f607426c3dba9ba11

#include <cstdlib>
#include <cstring>
#include <iostream>
#include <mpfr.h>
#include <sstream>
#include <stdexcept>
#include <string>

#include "psitheta.h"

namespace {

constexpr long X_LEFT = 800000000000L;
constexpr long MESH_H = 1000000L;
constexpr long EXPECTED_NODE_COUNT = 646258L;

std::string mpfr_to_string(mpfr_t value, int digits_after_decimal) {
  char *buffer = nullptr;
  if (mpfr_asprintf(&buffer, "%.*Re", digits_after_decimal, value) < 0) {
    throw std::runtime_error("mpfr_asprintf failed");
  }
  std::string text(buffer);
  mpfr_free_str(buffer);
  return text;
}

std::string one_decimal_ulp(mpfr_t value, int significant_digits) {
  mpfr_exp_t exp10 = 0;
  char *digits = mpfr_get_str(nullptr, &exp10, 10, significant_digits, value, MPFR_RNDN);
  if (digits == nullptr) {
    throw std::runtime_error("mpfr_get_str failed");
  }
  mpfr_free_str(digits);
  std::ostringstream out;
  out << "1e" << (static_cast<long>(exp10) - significant_digits);
  return out.str();
}

long parse_long_arg(const char *text, const char *name) {
  char *end = nullptr;
  long value = std::strtol(text, &end, 10);
  if (end == text || *end != '\0') {
    std::ostringstream out;
    out << "bad " << name << ": " << text;
    throw std::runtime_error(out.str());
  }
  return value;
}

void write_record(long index, int precision, const std::string &source_commit) {
  const long x_i = X_LEFT + index * MESH_H;

  mpfr_t psi_value;
  mpfr_t x_value;
  mpfr_t target_ratio;
  mpfr_t target_value;
  mpfr_t rounding_error_bound;
  mpfr_t psi_upper;
  mpfr_t slack_lower;

  mpfr_init2(psi_value, 256);
  mpfr_init2(x_value, 256);
  mpfr_init2(target_ratio, 256);
  mpfr_init2(target_value, 256);
  mpfr_init2(rounding_error_bound, 256);
  mpfr_init2(psi_upper, 256);
  mpfr_init2(slack_lower, 256);

  // 每个节点使用新的 Psi_computer，避免原源码重复调用时内部表指针复用造成归档污染。
  {
    Psi_computer psi_comp;
    psi_comp.psi(psi_value, x_i, precision);
  }

  const std::string ulp_text = one_decimal_ulp(psi_value, precision);
  mpfr_set_str(rounding_error_bound, ulp_text.c_str(), 10, MPFR_RNDU);
  mpfr_add(psi_upper, psi_value, rounding_error_bound, MPFR_RNDU);

  mpfr_set_si(x_value, x_i, MPFR_RNDN);
  mpfr_set_str(target_ratio, "1.00002841", 10, MPFR_RNDD);
  mpfr_mul(target_value, target_ratio, x_value, MPFR_RNDD);
  mpfr_sub(slack_lower, target_value, psi_upper, MPFR_RNDD);

  const int out_digits_after_decimal = precision + 8;
  std::cout
      << "{\"i\":" << index
      << ",\"psi_precision_decimal_digits\":" << precision
      << ",\"psi_raw_output\":\"" << mpfr_to_string(psi_value, out_digits_after_decimal) << "\""
      << ",\"psi_rounding_error_bound\":\"" << mpfr_to_string(rounding_error_bound, out_digits_after_decimal) << "\""
      << ",\"psi_rounding_mode\":\"MPFR_RNDN_value_wrapped_up_by_one_decimal_ulp_for_slack_lower_bound\""
      << ",\"psi_upper_for_slack\":\"" << mpfr_to_string(psi_upper, out_digits_after_decimal) << "\""
      << ",\"psi_value\":\"" << mpfr_to_string(psi_value, out_digits_after_decimal) << "\""
      << ",\"required_node_slack_floor\":\"3073386.85452651\""
      << ",\"slack_ge_required_floor\":" << (mpfr_cmp_d(slack_lower, 3073386.85452651) >= 0 ? "true" : "false")
      << ",\"slack_lower_bound\":\"" << mpfr_to_string(slack_lower, out_digits_after_decimal) << "\""
      << ",\"source_commit\":\"" << source_commit << "\""
      << ",\"x_i\":" << x_i
      << "}\n";

  mpfr_clear(psi_value);
  mpfr_clear(x_value);
  mpfr_clear(target_ratio);
  mpfr_clear(target_value);
  mpfr_clear(rounding_error_bound);
  mpfr_clear(psi_upper);
  mpfr_clear(slack_lower);
}

}  // namespace

int main(int argc, char **argv) {
  try {
    if (argc < 4 || argc > 5) {
      std::cerr << "usage: " << argv[0] << " <start-index> <count> <precision> [source-commit]\n";
      return 2;
    }
    const long start_index = parse_long_arg(argv[1], "start-index");
    const long count = parse_long_arg(argv[2], "count");
    const long precision_long = parse_long_arg(argv[3], "precision");
    const std::string source_commit =
        (argc == 5) ? argv[4] : "21f4f6553851f218801a733f607426c3dba9ba11";
    if (start_index < 0 || count < 0 || precision_long <= 0) {
      throw std::runtime_error("start-index/count/precision out of range");
    }
    if (start_index + count > EXPECTED_NODE_COUNT) {
      throw std::runtime_error("requested range exceeds certified mesh");
    }
    for (long offset = 0; offset < count; ++offset) {
      write_record(start_index + offset, static_cast<int>(precision_long), source_commit);
    }
  } catch (const std::exception &exc) {
    std::cerr << exc.what() << "\n";
    return 1;
  }
  return 0;
}
