#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main() {
    int test_cases;
    scanf("%d", &test_cases);

    while (test_cases--) {
        int town_citizens, pairs_of_people;
        scanf("%d %d", &town_citizens, &pairs_of_people);

        vector<int> disSet(town_citizens, -1);


        for (int i = 0; i < pairs_of_people; i++) {
            int citizen1, citizen2;
            scanf("%d %d", &citizen1, &citizen2);

            citizen1--;
            citizen2--;

            while (disSet[citizen1] >= 0) {
                citizen1 = disSet[citizen1];
            }
            while (disSet[citizen2] >= 0) {
                citizen2 = disSet[citizen2];
            }

            if (citizen1 != citizen2) {
                if (citizen1 > citizen2) {
                    swap(citizen1, citizen2);
                }
                disSet[citizen1] += disSet[citizen2];
                disSet[citizen2] = citizen1;
            }
        }

        int max_size = 0;
        for (int i = 0; i < town_citizens; i++) {
            if (disSet[i] < 0) {
                max_size = max(max_size, -disSet[i]);
            }
        }

        printf("%d\n", max_size);
    }

    return 0;
}
