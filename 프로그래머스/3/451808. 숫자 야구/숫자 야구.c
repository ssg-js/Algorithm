#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

extern char* submit(int);

int solution(int n) {
    for(int i = 1000; i <= 9999; i++)
        if (strcmp(submit(i), "4S 0B") == 0) return i;
    return 0;
}