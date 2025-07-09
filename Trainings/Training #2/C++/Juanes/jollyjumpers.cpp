#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;

bool jolly_jumper(const int n, const vector<int> & numbers) {

    if (n < 2) {
        return true;
    }

    vector<int> differences(n - 1, 0);

    for (int i = 0; i < n - 1; i++) {
        int dif = abs(numbers[i] - numbers[i + 1]);

        if (dif >= 1 && dif < n) {
            differences[dif - 1] = 1;
        }
    }

    for (int i = 0; i < n - 1; i++) {

        if (differences[i] == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int n;
    while (scanf("%d", &n) != EOF) {
        vector<int> numbers(n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &numbers[i]);
        }

        if (jolly_jumper(n, numbers)) {
            printf("Jolly\n");
        } else {
            printf("Not jolly\n");
        }
    }
    return 0;
}
