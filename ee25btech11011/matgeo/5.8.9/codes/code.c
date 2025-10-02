#include <stdio.h>

void solve(int* l, int* b) {
    int i, j;
    for (i = 0; i <= 100; i++) {
        for (j = 0; j <= 100; j++) {
            if ((3 * i - 5 * j == 6) && (2 * i + 3 * j == 61)) {
                printf("Found solution: l = %d, b = %d\n", i, j);
                *l = i;
                *b = j;
                return;
            }
        }
    }
    printf("No solution found.\n");
    *l = -1;
    *b = -1;
}
