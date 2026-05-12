// strict 中段 psi 分段增量节点输出器。
//
// 用法示例：
//   g++ -O3 -std=c++17 \
//     -o /tmp/middle_psi_segmented_delta \
//     experiments/prime_matrix_middle_psi_segmented_delta_runner.cpp
//
//   /tmp/middle_psi_segmented_delta \
//     0 3 800000037979.274744 \
//     21f4f6553851f218801a733f607426c3dba9ba11 1000
//
// 说明：
//   第 1 个参数是起始节点编号 start_index。
//   第 2 个参数是输出节点数 node_count。
//   第 3 个参数是 start_index 节点处的 psi 上界基值。
//   第 4 个参数可选，是来源 commit。
//   第 5 个参数可选，是每块处理的百万区间数，默认 1000。
//   第 6 个参数可选，是 start_index 节点前已经累计的 Lambda 项数，默认 0。
//   第 7 个参数可选，是否输出 start_index 节点，1 输出，0 只输出后续节点，默认 1。
//   输出 JSONL；每行是一个百万网格节点的保守 psi 上界记录。

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

constexpr long long X_LEFT = 800000000000LL;
constexpr long long MESH_H = 1000000LL;
constexpr long long EXPECTED_NODE_COUNT = 646258LL;
constexpr long double TARGET_RATIO = 1.00002841L;
constexpr long double REQUIRED_NODE_SLACK_FLOOR = 3073386.85452651L;
constexpr long double BASE_NUMERIC_SAFETY = 100.0L;
constexpr long double PER_TERM_NUMERIC_SAFETY = 1.0e-9L;
constexpr long long DEFAULT_SIEVE_WIDTH = 16000000LL;
constexpr long long DEFAULT_STREAM_INTERVAL_COUNT = 1000LL;

long long parse_ll_arg(const char *text, const char *name) {
  char *end = nullptr;
  long long value = std::strtoll(text, &end, 10);
  if (end == text || *end != '\0') {
    std::ostringstream out;
    out << "bad " << name << ": " << text;
    throw std::runtime_error(out.str());
  }
  return value;
}

unsigned long long parse_ull_arg(const char *text, const char *name) {
  char *end = nullptr;
  unsigned long long value = std::strtoull(text, &end, 10);
  if (end == text || *end != '\0') {
    std::ostringstream out;
    out << "bad " << name << ": " << text;
    throw std::runtime_error(out.str());
  }
  return value;
}

long double parse_ld_arg(const char *text, const char *name) {
  char *end = nullptr;
  long double value = std::strtold(text, &end);
  if (end == text || *end != '\0' || !std::isfinite(static_cast<double>(value))) {
    std::ostringstream out;
    out << "bad " << name << ": " << text;
    throw std::runtime_error(out.str());
  }
  return value;
}

std::string sci(long double value) {
  std::ostringstream out;
  out << std::scientific << std::setprecision(18) << value;
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

size_t interval_bucket(long long n, long long x_start) {
  // n 属于 (x_start+(j-1)h, x_start+jh] 时，贡献给第 j 个增量桶。
  return static_cast<size_t>((n - x_start - 1) / MESH_H + 1);
}

void add_prime_contributions(
    long long range_low,
    long long range_high,
    long long x_start,
    const std::vector<int> &base_primes,
    std::vector<long double> &increments,
    std::vector<unsigned long long> &term_counts) {
  if (range_low > range_high) {
    return;
  }

  for (long long chunk_low = range_low; chunk_low <= range_high;) {
    long long chunk_high = std::min(range_high, chunk_low + DEFAULT_SIEVE_WIDTH - 1);
    const size_t len = static_cast<size_t>(chunk_high - chunk_low + 1);
    std::vector<unsigned char> is_prime(len, 1);

    if (chunk_low == 1) {
      is_prime[0] = 0;
    }

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
      const long long n = chunk_low + static_cast<long long>(offset);
      if (n < 2) {
        continue;
      }
      const size_t bucket = interval_bucket(n, x_start);
      if (bucket < increments.size()) {
        increments[bucket] += std::log(static_cast<long double>(n));
        term_counts[bucket] += 1;
      }
    }

    chunk_low = chunk_high + 1;
  }
}

void add_prime_power_contributions(
    long long range_low,
    long long range_high,
    long long x_start,
    const std::vector<int> &base_primes,
    std::vector<long double> &increments,
    std::vector<unsigned long long> &term_counts) {
  if (range_low > range_high) {
    return;
  }

  for (int p_int : base_primes) {
    const long long p = p_int;
    __int128 power = static_cast<__int128>(p) * p;
    if (power > range_high) {
      break;
    }
    const long double logp = std::log(static_cast<long double>(p));
    while (power <= range_high) {
      if (power >= range_low) {
        const long long n = static_cast<long long>(power);
        const size_t bucket = interval_bucket(n, x_start);
        if (bucket < increments.size()) {
          increments[bucket] += logp;
          term_counts[bucket] += 1;
        }
      }
      power *= p;
    }
  }
}

void write_record(
    long long index,
    long double psi_estimate,
    long double increment_from_previous,
    unsigned long long increment_term_count,
    unsigned long long cumulative_terms,
    const std::string &source_commit,
    long long stream_interval_count) {
  const long long x_i = X_LEFT + index * MESH_H;
  const long double error_bound =
      BASE_NUMERIC_SAFETY + PER_TERM_NUMERIC_SAFETY * static_cast<long double>(cumulative_terms);
  const long double psi_upper = psi_estimate + error_bound;
  const long double slack_lower = TARGET_RATIO * static_cast<long double>(x_i) - psi_upper;

  std::cout
      << "{\"i\":" << index
      << ",\"x_i\":" << x_i
      << ",\"delta_algorithm\":\"segmented_sieve_prime_and_prime_power_increment\""
      << ",\"mesh_h\":" << MESH_H
      << ",\"stream_interval_count\":" << stream_interval_count
      << ",\"psi_estimate\":\"" << sci(psi_estimate) << "\""
      << ",\"psi_numeric_error_bound\":\"" << sci(error_bound) << "\""
      << ",\"psi_value\":\"" << sci(psi_upper) << "\""
      << ",\"psi_upper_for_slack\":\"" << sci(psi_upper) << "\""
      << ",\"increment_from_previous\":\"" << sci(increment_from_previous) << "\""
      << ",\"increment_term_count\":" << increment_term_count
      << ",\"cumulative_delta_term_count\":" << cumulative_terms
      << ",\"required_node_slack_floor\":\"3073386.85452651\""
      << ",\"slack_lower_bound\":\"" << sci(slack_lower) << "\""
      << ",\"slack_ge_required_floor\":" << (slack_lower >= REQUIRED_NODE_SLACK_FLOOR ? "true" : "false")
      << ",\"source_commit\":\"" << source_commit << "\""
      << "}\n";
}

}  // namespace

int main(int argc, char **argv) {
  try {
    if (argc < 4 || argc > 8) {
      std::cerr << "usage: " << argv[0]
                << " <start-index> <node-count> <base-psi-upper-at-start>"
                << " [source-commit] [stream-interval-count] [initial-cumulative-term-count]"
                << " [emit-start-node-0-or-1]\n";
      return 2;
    }

    const long long start_index = parse_ll_arg(argv[1], "start-index");
    const long long node_count = parse_ll_arg(argv[2], "node-count");
    const long double base_psi_upper = parse_ld_arg(argv[3], "base-psi-upper-at-start");
    const std::string source_commit =
        (argc >= 5) ? argv[4] : "21f4f6553851f218801a733f607426c3dba9ba11";
    const long long stream_interval_count =
        (argc >= 6) ? parse_ll_arg(argv[5], "stream-interval-count") : DEFAULT_STREAM_INTERVAL_COUNT;
    const unsigned long long initial_cumulative_terms =
        (argc >= 7) ? parse_ull_arg(argv[6], "initial-cumulative-term-count") : 0;
    const bool emit_start_node =
        (argc >= 8) ? (parse_ll_arg(argv[7], "emit-start-node-0-or-1") != 0) : true;

    if (start_index < 0 || node_count <= 0) {
      throw std::runtime_error("start-index/node-count out of range");
    }
    if (stream_interval_count <= 0) {
      throw std::runtime_error("stream-interval-count out of range");
    }
    if (start_index + node_count > EXPECTED_NODE_COUNT) {
      throw std::runtime_error("requested node range exceeds certified mesh");
    }

    const long long x_last = X_LEFT + (start_index + node_count - 1) * MESH_H;
    const long long prime_limit = isqrt_floor(x_last);
    const std::vector<int> base_primes = primes_up_to(prime_limit);

    long double psi_estimate = base_psi_upper;
    unsigned long long cumulative_terms = initial_cumulative_terms;

    if (emit_start_node) {
      write_record(
          start_index,
          psi_estimate,
          0.0L,
          0,
          cumulative_terms,
          source_commit,
          stream_interval_count);
      std::cout.flush();
    }

    long long completed_nodes = 1;
    while (completed_nodes < node_count) {
      const long long intervals_this_chunk =
          std::min(stream_interval_count, node_count - completed_nodes);
      const long long chunk_start_index = start_index + completed_nodes - 1;
      const long long chunk_x_start = X_LEFT + chunk_start_index * MESH_H;
      const long long range_low = chunk_x_start + 1;
      const long long range_high = chunk_x_start + intervals_this_chunk * MESH_H;

      std::vector<long double> increments(static_cast<size_t>(intervals_this_chunk + 1), 0.0L);
      std::vector<unsigned long long> term_counts(static_cast<size_t>(intervals_this_chunk + 1), 0);

      add_prime_contributions(range_low, range_high, chunk_x_start, base_primes, increments, term_counts);
      add_prime_power_contributions(range_low, range_high, chunk_x_start, base_primes, increments, term_counts);

      for (long long offset = 1; offset <= intervals_this_chunk; ++offset) {
        psi_estimate += increments[static_cast<size_t>(offset)];
        cumulative_terms += term_counts[static_cast<size_t>(offset)];
        write_record(
            chunk_start_index + offset,
            psi_estimate,
            increments[static_cast<size_t>(offset)],
            term_counts[static_cast<size_t>(offset)],
            cumulative_terms,
            source_commit,
            stream_interval_count);
      }

      completed_nodes += intervals_this_chunk;
      std::cout.flush();
      std::cerr << "progress nodes=" << completed_nodes << "/" << node_count
                << " last_i=" << (start_index + completed_nodes - 1) << "\n";
    }
  } catch (const std::exception &exc) {
    std::cerr << exc.what() << "\n";
    return 1;
  }
  return 0;
}
