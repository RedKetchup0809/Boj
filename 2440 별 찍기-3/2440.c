#include <stdio.h>

int main() {
    int i, t, N;
    scanf("%d", &N);
    for (i=N;i>=1;i=i-1) {
        for (t=1;t<=i;t++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}