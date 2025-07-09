#include <bits/stdc++.h>

using namespace std;

map<int, int> dict;

int collatz(int n) {
    if (n == 1) return 1;

    if (dict.find(n) != dict.end()) {
        return dict[n];
    }

    int next_n;
    if (n % 2 == 0) {
        next_n = n / 2;
    } else {
        next_n = 3 * n + 1;
    }

    dict[n] = 1 + collatz(next_n);
    return dict[n];
}

int collatz_max_sequence(int n, int m) {
    if (n > m) {
        swap(n, m);
    }

    int max_sequence = 0;
    for (int i = n; i <= m; ++i) {
        int sequence_length = collatz(i);
        if (sequence_length > max_sequence) {
            max_sequence = sequence_length;
        }
    }
    return max_sequence;
}

int main() {
    int n, m;
    while (scanf("%d %d", &n, &m) != EOF) {
        int result = collatz_max_sequence(n, m);
        printf("%d %d %d\n", n, m, result);
    }
    return 0;
}
