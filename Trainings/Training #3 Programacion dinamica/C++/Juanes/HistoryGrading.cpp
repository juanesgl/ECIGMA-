#include <bits/stdc++.h>
using namespace std;

int lcs(const vector<int> &cs, const vector<int> &sq, int n) {
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (cs[i - 1] == sq[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[n][n];
}

int main() {
    int n;
    scanf("%d", &n);

    vector<int> correct_positions(n + 1);
    for (int i = 1; i <= n; ++i) {
        int x;
        scanf("%d", &x);
        correct_positions[x] = i;
    }

    vector<int> student_positions(n);
    while (scanf("%d", &student_positions[0]) != EOF) {
        for (int i = 1; i < n; ++i) {
            scanf("%d", &student_positions[i]);
        }

        // Convert student sequence to a comparable format
        vector<int> student_order(n);
        for (int i = 0; i < n; ++i) {
            student_order[i] = correct_positions[student_positions[i]];
        }

        // Find LCS against sorted sequence 1,2,3,...,n
        vector<int> sorted_order(n);
        for (int i = 0; i < n; ++i) {
            sorted_order[i] = i + 1;
        }

        printf("%d\n", lcs(sorted_order, student_order, n));
    }

    return 0;
}