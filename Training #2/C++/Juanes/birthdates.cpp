#include <cstdio>
#include <tuple>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<tuple<int, int, int, string>> people;

    for (int i = 0; i < n; i++) {
        char name[15];
        int day, month, year;
        scanf("%s %d %d %d", name, &day, &month, &year);

        people.push_back({year, month, day, string(name)});
    }

    auto youngest = max_element(people.begin(), people.end());
    auto oldest = min_element(people.begin(), people.end());
    
    printf("%s\n", get<3>(*youngest).c_str());
    printf("%s\n", get<3>(*oldest).c_str());

    return 0;
}
