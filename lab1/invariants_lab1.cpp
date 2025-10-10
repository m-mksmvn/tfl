#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <random>
#include <ctime>

using namespace std;

// генератор случайных чисел
int randint(int a, int b) {
    static mt19937 gen(time(nullptr));
    uniform_int_distribution<> dist(a, b);
    return dist(gen);
}

// генерация случайной строки из 'a' и 'b'
string random_string(int length) {
    string s;
    for (int i = 0; i < length; ++i)
        s += (randint(0, 1) ? 'a' : 'b');
    return s;
}

// подсчёт подстрок
int count_substr(const string& str, const string& sub) {
    int count = 0;
    size_t pos = str.find(sub);
    while (pos != string::npos) {
        count++;
        pos = str.find(sub, pos + 1);
    }
    return count;
}

int main() {
    srand(time(nullptr));

    map<string, string> relations = {
        {"bbbab", "babb"},
        {"babbaab", "baabb"},
        {"baabbaaab", "baaabb"},
        {"abab", "bbbb"},
        {"aaaa", "a"}
    };

    int n = 5;
    bool j = true;

    for (int t = 0; t < n; ++t) {
        int length = randint(1, 15);
        string s = random_string(length);

        int T_count_steps = randint(1, 15);
        set<string> T_steps_results;
        T_steps_results.insert(s);

        string current = s;

        for (int i = 0; i < T_count_steps; ++i) {
            for (auto& [pattern, replacement] : relations) {
                size_t start = 0;
                while (true) {
                    size_t pos = current.find(pattern, start);
                    if (pos == string::npos) break;
                    string s_new = current.substr(0, pos) + replacement + current.substr(pos + pattern.size());
                    T_steps_results.insert(s_new);
                    start = pos + 1;
                }
            }
            if (!T_steps_results.empty()) {
                int index = randint(0, (int)T_steps_results.size() - 1);
                auto it = T_steps_results.begin();
                advance(it, index);
                current = *it;
            }
        }

        // 1 инвариант — количество 'a'
        int a_s = count(s.begin(), s.end(), 'a');
        int a_str = count(current.begin(), current.end(), 'a');
        if (a_str <= a_s)
            cout << "✅ " << a_s << " " << a_str << " ----- 1 инвариант - True\n";
        else {
            cout << a_s << " " << a_str << " ----- 1 инвариант - False\n";
            j = false;
            break;
        }

        // 2 инвариант — длина строки
        if ((int)current.size() <= (int)s.size())
            cout << "✅ " << s.size() << " " << current.size() << " ----- 2 инвариант - True\n";
        else {
            cout << s.size() << " " << current.size() << " ----- 2 инвариант - False\n";
            j = false;
            break;
        }

        // 3 инвариант — count_a - count_aa - count_ab
        int str1 = count(current.begin(), current.end(), 'a') - count_substr(current, "aa") - count_substr(s, "ab");
        int s1 = count(s.begin(), s.end(), 'a') - count_substr(s, "aa") - count_substr(s, "ab");
        if (str1 <= s1)
            cout << "✅ " << s1 << " " << str1 << " ----- 3 инвариант - True\n";
        else {
            cout << s1 << " " << str1 << " ----- 3 инвариант - False\n";
            j = false;
            break;
        }

        // 4 инвариант — последняя буква 'a'
        bool str_last = (!current.empty() && current.back() == 'a');
        bool s_last = (!s.empty() && s.back() == 'a');
        if (str_last <= s_last)
            cout << "✅ " << s_last << " " << str_last << " ----- 4 инвариант - True\n";
        else {
            cout << s_last << " " << str_last << " ----- 4 инвариант - False\n";
            j = false;
            break;
        }

        // 5 инвариант — первая буква 'a'
        bool str_first = (!current.empty() && current.front() == 'a');
        bool s_first = (!s.empty() && s.front() == 'a');
        if (str_first <= s_first)
            cout << "✅ " << s_first << " " << str_first << " ----- 5 инвариант - True\n";
        else {
            cout << s_first << " " << str_first << " ----- 5 инвариант - False\n";
            j = false;
            break;
        }
    }

    cout << boolalpha << j << endl;
    return 0;
}
//g++ -std=c++17 invariants_lab1.cpp -o invariants_lab1 && ./invariants_lab1