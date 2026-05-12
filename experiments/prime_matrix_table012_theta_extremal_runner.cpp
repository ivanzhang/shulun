// strict table_012 的 theta 区间极值扫描器。
//
// 用法示例：
//   g++ -O3 -std=c++17 -o /tmp/table012_theta_extremal experiments/prime_matrix_table012_theta_extremal_runner.cpp
//
//   /tmp/table012_theta_extremal --max-rows 1 > data/theta-table012-extremal-sample-first-row.jsonl
//   /tmp/table012_theta_extremal --max-rows 34 > data/theta-table012-extremal-archive.jsonl
//   /tmp/table012_theta_extremal --start-index 19 --initial-theta 1.999982176276821183e+10
//     --initial-prime-count 882206716 --max-rows 34 > data/theta-table012-extremal-resume.jsonl
//   /tmp/table012_theta_extremal --segment-left 100000000000 --segment-right 110000000000
//     --start-index 27 --initial-theta 9.999973765310744470e+10 --initial-prime-count 4118054813
//
// 说明：
//   本工具从 x=1e8 自行筛出 theta(1e8)，再按 table_012 的 34 个连续区间
//   顺序扫描素数跳点。对每行 b1，需验证 theta(x) <= x + b1*x/log(x)。
//   因为右侧函数在 table_012 全域内严格递增，而 theta 在素数间常数，
//   每个区间只需检查左端点和每个素数跳点后的值。

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct TableRow {
  const char *label;
  long long left;
  long long right;
  long double b1;
};

constexpr long long SMALL_LIMIT = 100000000LL;
constexpr long long DEFAULT_CHUNK_WIDTH = 16000000LL;
constexpr long double NUMERIC_SAFETY_ABSOLUTE = 1.0L;
constexpr long double NUMERIC_SAFETY_PER_PRIME = 1.0e-12L;

const TableRow TABLE012[] = {
    {"1E+08", 100000000LL, 200000000LL, -0.00044L},
    {"2E+08", 200000000LL, 300000000LL, -0.00065L},
    {"3E+08", 300000000LL, 400000000LL, -0.00057L},
    {"4E+08", 400000000LL, 500000000LL, -0.00049L},
    {"5E+08", 500000000LL, 600000000LL, -0.00052L},
    {"6E+08", 600000000LL, 700000000LL, -0.00038L},
    {"7E+08", 700000000LL, 800000000LL, -0.00051L},
    {"8E+08", 800000000LL, 900000000LL, -0.00044L},
    {"9E+08", 900000000LL, 1000000000LL, -0.00050L},
    {"1E+09", 1000000000LL, 2000000000LL, -0.00021L},
    {"2E+09", 2000000000LL, 3000000000LL, -0.00018L},
    {"3E+09", 3000000000LL, 4000000000LL, -0.00015L},
    {"4E+09", 4000000000LL, 5000000000LL, -0.00017L},
    {"5E+09", 5000000000LL, 6000000000LL, -0.00018L},
    {"6E+09", 6000000000LL, 7000000000LL, -0.00013L},
    {"7E+09", 7000000000LL, 8000000000LL, -0.00018L},
    {"8E+09", 8000000000LL, 9000000000LL, -0.00016L},
    {"9E+09", 9000000000LL, 10000000000LL, -0.00010L},
    {"1E+10", 10000000000LL, 20000000000LL, -0.00008L},
    {"2E+10", 20000000000LL, 30000000000LL, -0.00006L},
    {"3E+10", 30000000000LL, 40000000000LL, -0.00005L},
    {"4E+10", 40000000000LL, 50000000000LL, -0.00007L},
    {"5E+10", 50000000000LL, 60000000000LL, -0.00004L},
    {"6E+10", 60000000000LL, 70000000000LL, -0.00006L},
    {"7E+10", 70000000000LL, 80000000000LL, -0.00004L},
    {"8E+10", 80000000000LL, 90000000000LL, -0.00006L},
    {"9E+10", 90000000000LL, 100000000000LL, -0.00004L},
    {"1E+11", 100000000000LL, 200000000000LL, -0.00002L},
    {"2E+11", 200000000000LL, 300000000000LL, -0.00002L},
    {"3E+11", 300000000000LL, 400000000000LL, -0.00001L},
    {"4E+11", 400000000000LL, 500000000000LL, -0.00002L},
    {"5E+11", 500000000000LL, 600000000000LL, -0.00001L},
    {"6E+11", 600000000000LL, 700000000000LL, -0.00002L},
    {"7E+11", 700000000000LL, 800000000000LL, -0.00001L},
};

long long parse_ll_arg(const char *text, const char *name) {
  char *end = nullptr;
  const long long value = std::strtoll(text, &end, 10);
  if (end == text || *end != '\0') {
    std::ostringstream out;
    out << "bad " << name << ": " << text;
    throw std::runtime_error(out.str());
  }
  return value;
}

unsigned long long parse_ull_arg(const char *text, const char *name) {
  char *end = nullptr;
  const unsigned long long value = std::strtoull(text, &end, 10);
  if (end == text || *end != '\0') {
    std::ostringstream out;
    out << "bad " << name << ": " << text;
    throw std::runtime_error(out.str());
  }
  return value;
}

long double parse_ld_arg(const char *text, const char *name) {
  char *end = nullptr;
  const long double value = std::strtold(text, &end);
  if (end == text || *end != '\0') {
    std::ostringstream out;
    out << "bad " << name << ": " << text;
    throw std::runtime_error(out.str());
  }
  return value;
}

std::string sci(long double value) {
  std::ostringstream out;
  out << std::scientific << std::setprecision(21) << value;
  return out.str();
}

std::vector<int> primes_up_to(long long limit) {
  if (limit < 2) {
    return {};
  }
  std::vector<unsigned char> is_prime(static_cast<size_t>(limit + 1), 1);
  is_prime[0] = 0;
  is_prime[1] = 0;
  for (long long p = 2; p * p <= limit; ++p) {
    if (!is_prime[static_cast<size_t>(p)]) {
      continue;
    }
    for (long long m = p * p; m <= limit; m += p) {
      is_prime[static_cast<size_t>(m)] = 0;
    }
  }
  std::vector<int> primes;
  for (long long p = 2; p <= limit; ++p) {
    if (is_prime[static_cast<size_t>(p)]) {
      primes.push_back(static_cast<int>(p));
    }
  }
  return primes;
}

long long isqrt_floor(long long n) {
  long long r = static_cast<long long>(std::sqrt(static_cast<long double>(n)));
  while ((__int128)(r + 1) * (r + 1) <= n) {
    ++r;
  }
  while ((__int128)r * r > n) {
    --r;
  }
  return r;
}

long double rhs(long double x, long double b1) {
  return x + b1 * x / std::log(x);
}

long double defect(long double theta, long double x, long double b1) {
  return theta - rhs(x, b1);
}

long double required_b1(long double theta, long double x) {
  return (theta - x) * std::log(x) / x;
}

long double derivative_lower_bound(long long left, long long right, long double b1) {
  // d/dx (x+b1*x/log x)=1+b1*(log x-1)/log^2 x。
  // b1<0 时导数在本范围内仍远大于 0；粗取端点最小值即可登记。
  long double best = std::numeric_limits<long double>::infinity();
  for (long long x : {left, right}) {
    const long double lx = std::log(static_cast<long double>(x));
    const long double d = 1.0L + b1 * (lx - 1.0L) / (lx * lx);
    best = std::min(best, d);
  }
  return best;
}

void kahan_add(long double value, long double &sum, long double &compensation) {
  const long double y = value - compensation;
  const long double t = sum + y;
  compensation = (t - sum) - y;
  sum = t;
}

struct BaseTheta {
  long double theta = 0.0L;
  long double compensation = 0.0L;
  unsigned long long prime_count = 0;
};

BaseTheta compute_theta_to_small_limit() {
  std::vector<unsigned char> is_prime(static_cast<size_t>(SMALL_LIMIT + 1), 1);
  is_prime[0] = 0;
  is_prime[1] = 0;
  for (long long p = 2; p * p <= SMALL_LIMIT; ++p) {
    if (!is_prime[static_cast<size_t>(p)]) {
      continue;
    }
    for (long long m = p * p; m <= SMALL_LIMIT; m += p) {
      is_prime[static_cast<size_t>(m)] = 0;
    }
  }

  BaseTheta base;
  for (long long p = 2; p <= SMALL_LIMIT; ++p) {
    if (!is_prime[static_cast<size_t>(p)]) {
      continue;
    }
    kahan_add(std::log(static_cast<long double>(p)), base.theta, base.compensation);
    ++base.prime_count;
  }
  return base;
}

struct RowResult {
  const TableRow *row = nullptr;
  long double max_defect = -std::numeric_limits<long double>::infinity();
  long double max_required_b1 = -std::numeric_limits<long double>::infinity();
  long long max_x = 0;
  const char *max_kind = "unset";
  unsigned long long row_prime_count = 0;
  long double theta_at_right = 0.0L;
  bool passed_with_guard = false;
  bool passed_raw = false;
};

void observe_point(
    const TableRow &row,
    long double theta,
    long long x,
    const char *kind,
    RowResult &result) {
  const long double dx = defect(theta, static_cast<long double>(x), row.b1);
  const long double rb1 = required_b1(theta, static_cast<long double>(x));
  if (dx > result.max_defect) {
    result.max_defect = dx;
    result.max_required_b1 = rb1;
    result.max_x = x;
    result.max_kind = kind;
  }
}

RowResult scan_row(
    const TableRow &row,
    const std::vector<int> &base_primes,
    long long chunk_width,
    long double &theta,
    long double &theta_compensation,
    unsigned long long &global_prime_count) {
  RowResult result;
  result.row = &row;
  observe_point(row, theta, row.left, "left_endpoint", result);

  for (long long chunk_low = row.left + 1; chunk_low <= row.right;) {
    const long long chunk_high = std::min(row.right, chunk_low + chunk_width - 1);
    const size_t len = static_cast<size_t>(chunk_high - chunk_low + 1);
    std::vector<unsigned char> is_prime(len, 1);

    for (int p_int : base_primes) {
      const long long p = p_int;
      if (p * p > chunk_high) {
        break;
      }
      long long first = ((chunk_low + p - 1) / p) * p;
      first = std::max(first, p * p);
      for (long long m = first; m <= chunk_high; m += p) {
        is_prime[static_cast<size_t>(m - chunk_low)] = 0;
      }
    }

    for (size_t offset = 0; offset < len; ++offset) {
      if (!is_prime[offset]) {
        continue;
      }
      const long long p = chunk_low + static_cast<long long>(offset);
      kahan_add(std::log(static_cast<long double>(p)), theta, theta_compensation);
      ++global_prime_count;
      ++result.row_prime_count;
      observe_point(row, theta, p, "prime_jump", result);
    }

    chunk_low = chunk_high + 1;
  }

  result.theta_at_right = theta;
  const long double error_bound =
      NUMERIC_SAFETY_ABSOLUTE
      + NUMERIC_SAFETY_PER_PRIME * static_cast<long double>(global_prime_count);
  result.passed_raw = result.max_defect < 0.0L;
  result.passed_with_guard = result.max_defect + error_bound < 0.0L;
  return result;
}

void write_row_result(const RowResult &result, unsigned long long global_prime_count) {
  const TableRow &row = *result.row;
  const long double error_bound =
      NUMERIC_SAFETY_ABSOLUTE
      + NUMERIC_SAFETY_PER_PRIME * static_cast<long double>(global_prime_count);
  const long double margin_after_guard = -(result.max_defect + error_bound);
  const long double b1_margin = row.b1 - result.max_required_b1;

  std::cout
      << "{\"label\":\"" << row.label << "\""
      << ",\"left\":" << row.left
      << ",\"right\":" << row.right
      << ",\"b1\":\"" << sci(row.b1) << "\""
      << ",\"row_prime_count\":" << result.row_prime_count
      << ",\"global_prime_count\":" << global_prime_count
      << ",\"theta_at_right\":\"" << sci(result.theta_at_right) << "\""
      << ",\"max_defect\":\"" << sci(result.max_defect) << "\""
      << ",\"numeric_error_bound\":\"" << sci(error_bound) << "\""
      << ",\"margin_after_guard\":\"" << sci(margin_after_guard) << "\""
      << ",\"raw_margin\":\"" << sci(-result.max_defect) << "\""
      << ",\"max_x\":" << result.max_x
      << ",\"max_kind\":\"" << result.max_kind << "\""
      << ",\"max_required_b1\":\"" << sci(result.max_required_b1) << "\""
      << ",\"b1_minus_max_required_b1\":\"" << sci(b1_margin) << "\""
      << ",\"rhs_derivative_lower_bound\":\""
      << sci(derivative_lower_bound(row.left, row.right, row.b1)) << "\""
      << ",\"passed_raw\":" << (result.passed_raw ? "true" : "false")
      << ",\"passed_with_guard\":" << (result.passed_with_guard ? "true" : "false")
      << "}\n";
}

void write_segment_result(
    const RowResult &result,
    unsigned long long global_prime_count,
    long long row_index,
    long long segment_left,
    long long segment_right) {
  const TableRow &row = *result.row;
  const long double error_bound =
      NUMERIC_SAFETY_ABSOLUTE
      + NUMERIC_SAFETY_PER_PRIME * static_cast<long double>(global_prime_count);
  const long double margin_after_guard = -(result.max_defect + error_bound);
  const long double b1_margin = row.b1 - result.max_required_b1;

  std::cout
      << "{\"record_type\":\"table012_theta_segment\""
      << ",\"row_index\":" << row_index
      << ",\"label\":\"" << row.label << "\""
      << ",\"row_left\":" << row.left
      << ",\"row_right\":" << row.right
      << ",\"segment_left\":" << segment_left
      << ",\"segment_right\":" << segment_right
      << ",\"b1\":\"" << sci(row.b1) << "\""
      << ",\"segment_prime_count\":" << result.row_prime_count
      << ",\"global_prime_count\":" << global_prime_count
      << ",\"theta_at_right\":\"" << sci(result.theta_at_right) << "\""
      << ",\"max_defect\":\"" << sci(result.max_defect) << "\""
      << ",\"numeric_error_bound\":\"" << sci(error_bound) << "\""
      << ",\"margin_after_guard\":\"" << sci(margin_after_guard) << "\""
      << ",\"raw_margin\":\"" << sci(-result.max_defect) << "\""
      << ",\"max_x\":" << result.max_x
      << ",\"max_kind\":\"" << result.max_kind << "\""
      << ",\"max_required_b1\":\"" << sci(result.max_required_b1) << "\""
      << ",\"b1_minus_max_required_b1\":\"" << sci(b1_margin) << "\""
      << ",\"passed_raw\":" << (result.passed_raw ? "true" : "false")
      << ",\"passed_with_guard\":" << (result.passed_with_guard ? "true" : "false")
      << "}\n";
}

RowResult scan_segment(
    const TableRow &row,
    const std::vector<int> &base_primes,
    long long chunk_width,
    long long segment_left,
    long long segment_right,
    bool observe_left,
    long double &theta,
    long double &theta_compensation,
    unsigned long long &global_prime_count) {
  RowResult result;
  result.row = &row;
  if (observe_left) {
    observe_point(row, theta, segment_left, "left_endpoint", result);
  }

  for (long long chunk_low = segment_left + 1; chunk_low <= segment_right;) {
    const long long chunk_high = std::min(segment_right, chunk_low + chunk_width - 1);
    const size_t len = static_cast<size_t>(chunk_high - chunk_low + 1);
    std::vector<unsigned char> is_prime(len, 1);

    for (int p_int : base_primes) {
      const long long p = p_int;
      if (p * p > chunk_high) {
        break;
      }
      long long first = ((chunk_low + p - 1) / p) * p;
      first = std::max(first, p * p);
      for (long long m = first; m <= chunk_high; m += p) {
        is_prime[static_cast<size_t>(m - chunk_low)] = 0;
      }
    }

    for (size_t offset = 0; offset < len; ++offset) {
      if (!is_prime[offset]) {
        continue;
      }
      const long long p = chunk_low + static_cast<long long>(offset);
      kahan_add(std::log(static_cast<long double>(p)), theta, theta_compensation);
      ++global_prime_count;
      ++result.row_prime_count;
      observe_point(row, theta, p, "prime_jump", result);
    }

    chunk_low = chunk_high + 1;
  }

  result.theta_at_right = theta;
  const long double error_bound =
      NUMERIC_SAFETY_ABSOLUTE
      + NUMERIC_SAFETY_PER_PRIME * static_cast<long double>(global_prime_count);
  result.passed_raw = result.max_defect < 0.0L;
  result.passed_with_guard = result.max_defect + error_bound < 0.0L;
  return result;
}

void usage(const char *argv0) {
  std::cerr
      << "usage: " << argv0
      << " [--max-rows N] [--chunk-width W]"
      << " [--start-index I --initial-theta T --initial-prime-count C]"
      << " [--segment-left L --segment-right R]\n";
}

}  // namespace

int main(int argc, char **argv) {
  try {
    long long max_rows = static_cast<long long>(sizeof(TABLE012) / sizeof(TABLE012[0]));
    long long chunk_width = DEFAULT_CHUNK_WIDTH;
    long long start_index = 0;
    bool has_initial_theta = false;
    bool has_initial_prime_count = false;
    bool segment_mode = false;
    long double initial_theta = 0.0L;
    unsigned long long initial_prime_count = 0;
    long long segment_left = 0;
    long long segment_right = 0;

    for (int i = 1; i < argc; ++i) {
      const std::string arg = argv[i];
      if (arg == "--max-rows" && i + 1 < argc) {
        max_rows = parse_ll_arg(argv[++i], "--max-rows");
      } else if (arg == "--chunk-width" && i + 1 < argc) {
        chunk_width = parse_ll_arg(argv[++i], "--chunk-width");
      } else if (arg == "--start-index" && i + 1 < argc) {
        start_index = parse_ll_arg(argv[++i], "--start-index");
      } else if (arg == "--initial-theta" && i + 1 < argc) {
        initial_theta = parse_ld_arg(argv[++i], "--initial-theta");
        has_initial_theta = true;
      } else if (arg == "--initial-prime-count" && i + 1 < argc) {
        initial_prime_count = parse_ull_arg(argv[++i], "--initial-prime-count");
        has_initial_prime_count = true;
      } else if (arg == "--segment-left" && i + 1 < argc) {
        segment_left = parse_ll_arg(argv[++i], "--segment-left");
        segment_mode = true;
      } else if (arg == "--segment-right" && i + 1 < argc) {
        segment_right = parse_ll_arg(argv[++i], "--segment-right");
        segment_mode = true;
      } else if (arg == "--help") {
        usage(argv[0]);
        return 0;
      } else {
        usage(argv[0]);
        return 2;
      }
    }

    const long long table_rows = static_cast<long long>(sizeof(TABLE012) / sizeof(TABLE012[0]));
    if (max_rows <= 0 || max_rows > table_rows) {
      throw std::runtime_error("--max-rows out of range");
    }
    if (start_index < 0 || start_index >= max_rows) {
      throw std::runtime_error("--start-index out of range");
    }
    if (chunk_width <= 0) {
      throw std::runtime_error("--chunk-width out of range");
    }
    if (start_index > 0 && (!has_initial_theta || !has_initial_prime_count)) {
      throw std::runtime_error("resume mode requires --initial-theta and --initial-prime-count");
    }
    if (segment_mode) {
      if (!has_initial_theta || !has_initial_prime_count) {
        throw std::runtime_error("segment mode requires --initial-theta and --initial-prime-count");
      }
      const TableRow &row = TABLE012[static_cast<size_t>(start_index)];
      if (segment_left < row.left || segment_right > row.right || segment_left >= segment_right) {
        throw std::runtime_error("bad segment bounds for selected row");
      }
    }

    const long long final_right =
        segment_mode ? segment_right : TABLE012[static_cast<size_t>(max_rows - 1)].right;
    const std::vector<int> base_primes = primes_up_to(isqrt_floor(final_right));

    long double theta = 0.0L;
    long double theta_compensation = 0.0L;
    unsigned long long global_prime_count = 0;
    if (start_index == 0) {
      BaseTheta base = compute_theta_to_small_limit();
      theta = base.theta;
      theta_compensation = base.compensation;
      global_prime_count = base.prime_count;
      std::cerr << "base theta(1e8)=" << sci(theta)
                << " prime_count=" << global_prime_count
                << " max_rows=" << max_rows << "\n";
    } else {
      // 断点续跑只用于工程归档补齐；严格舍入证明仍由独立区间证书承担。
      theta = initial_theta;
      theta_compensation = 0.0L;
      global_prime_count = initial_prime_count;
      std::cerr << "resume start_index=" << start_index
                << " theta=" << sci(theta)
                << " prime_count=" << global_prime_count
                << " max_rows=" << max_rows << "\n";
    }

    if (segment_mode) {
      const TableRow &row = TABLE012[static_cast<size_t>(start_index)];
      const bool observe_left = segment_left == row.left;
      // 子区间模式只扫描一个区块，供 Python 驱动合并成原始行证书。
      const RowResult result = scan_segment(
          row,
          base_primes,
          chunk_width,
          segment_left,
          segment_right,
          observe_left,
          theta,
          theta_compensation,
          global_prime_count);
      write_segment_result(result, global_prime_count, start_index, segment_left, segment_right);
      std::cerr << "completed segment row=" << row.label
                << " [" << segment_left << "," << segment_right << "]"
                << " passed=" << (result.passed_with_guard ? "true" : "false")
                << " max_defect=" << sci(result.max_defect) << "\n";
      return 0;
    }

    for (long long i = start_index; i < max_rows; ++i) {
      const RowResult result = scan_row(
          TABLE012[static_cast<size_t>(i)],
          base_primes,
          chunk_width,
          theta,
          theta_compensation,
          global_prime_count);
      write_row_result(result, global_prime_count);
      std::cout.flush();
      std::cerr << "completed row=" << TABLE012[static_cast<size_t>(i)].label
                << " passed=" << (result.passed_with_guard ? "true" : "false")
                << " max_defect=" << sci(result.max_defect) << "\n";
    }
  } catch (const std::exception &exc) {
    std::cerr << exc.what() << "\n";
    return 1;
  }
  return 0;
}
