#include <stdio.h>

int main (){
    int N, i, t;
    scanf("%d", &N);
    for(i=1;i<=N;i++) {
        for(t=1;t<=N-i;t++) {
            printf(" ");
        }
        for(t=1;t<=2*i-1;t++) {
            printf("*");
        }
        printf("\n");
    }
    for(i=N-1;i>=1;i=i-1) {
        for(t=1;t<=N-i;t++) {
            printf(" ");
        }
        for(t=1;t<=2*i-1;t++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}