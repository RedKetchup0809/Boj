#include <stdio.h>

int main() {
    int t, i, N;
    scanf("%d", &N);
    for (i=1;i<=N;i++) {
        for (t=1;t<=i;t++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}