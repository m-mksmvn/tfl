#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <random>

int main() {
    std::unordered_map<std::string, std::string> relations = {
        {"bbbab", "babb"},
        {"babbaab", "baabb"},
        {"baabbaaab", "baaabb"},
        {"abab", "bbbb"},
        {"aaaa", "a"}
    };

    std::unordered_map<std::string, std::string> new_relations = {
        {"bbbab", "babb"},
        {"babbaab", "baabb"},
        {"baabbaaab", "baaabb"},
        {"bbbb", "abab"},
        {"aaaa", "a"},
        {"babab", "ababb"},
        {"babbab", "ababb"},
        {"baababa", "ababb"},
        {"baabab", "ababb"},
        {"aababb", "ababb"},
        {"baabbab", "ababb"},
        {"baabbb", "ababb"},
        {"baaabbab", "ababb"},
        {"baaabbb", "ababb"},
        {"babbb", "ababb"},
        {"bbaabb", "ababb"},
        {"bbabb", "ababb"},
        {"abaabb", "ababb"},
        {"ababbaaab", "ababb"},
        {"bbaaabb", "ababb"},
        {"abaaabb", "ababb"}
    };

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> len_dist(1, 15);
    std::uniform_int_distribution<> step_dist(1, 15);
    std::uniform_int_distribution<> bit_dist(0, 1);

    int n = 10;
    for (int t = 0; t < n; ++t) {
        // --- генерация случайной строки ---
        int length = len_dist(gen);
        std::string s;
        s.reserve(length);
        for (int i = 0; i < length; ++i) {
            s += (bit_dist(gen) ? 'b' : 'a');
        }

        int T_count_steps = step_dist(gen);

        // --- система 1 ---
        std::unordered_set<std::string> T_steps_results;
        T_steps_results.insert(s);
        for (int i = 0; i < T_count_steps; ++i) {
            for (const auto& [pattern, replacement] : relations) {
                size_t start = 0;
                while (true) {
                    size_t pos = s.find(pattern, start);
                    if (pos == std::string::npos) break;
                    std::string s_new = s.substr(0, pos) + replacement + s.substr(pos + pattern.size());
                    T_steps_results.insert(s_new);
                    start = pos + 1;
                }
            }
        }

        // --- система 2 ---
        std::unordered_set<std::string> T_new_steps_results;
        T_new_steps_results.insert(s);
        for (int i = 0; i < T_count_steps; ++i) {
            for (const auto& [pattern, replacement] : new_relations) {
                size_t start = 0;
                while (true) {
                    size_t pos = s.find(pattern, start);
                    if (pos == std::string::npos) break;
                    std::string s_new = s.substr(0, pos) + replacement + s.substr(pos + pattern.size());
                    T_new_steps_results.insert(s_new);
                    start = pos + 1;
                }
            }
        }

        // --- сравнение множеств ---
        bool has_common = false;
        for (const auto& str1 : T_steps_results) {
            if (T_new_steps_results.find(str1) != T_new_steps_results.end()) {
                has_common = true;
                std::cout << "✅ true " << s << " {" << str1 << "}" << std::endl;
                break;
            }
        }

        if (!has_common) {
            std::cout << "false" << std::endl;
        }
    }

    return 0;
}
//g++ -std=c++17 fuzzing_lab1.cpp -o fuzzing_lab1 && ./fuzzing_lab1
