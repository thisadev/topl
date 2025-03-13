#include <stdio.h>


int calculateEvenSum(int range) {
    int sum = 0;
    for (int i = 1; i <= range; ++i) {
        if (i % 2 == 0) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    int result = calculateEvenSum(10);
    printf("Sum of even numbers from 1 to 10: %d\n", result);
    return 0;
}

