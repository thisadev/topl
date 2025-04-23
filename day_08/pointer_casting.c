#include <stdio.h>

int main() {
    int myInteger = 1078523331;
    float myFloat;

    float *floatPointer = (float *) &myInteger;
    myFloat = *floatPointer;

    printf("Original integer value: %d\n", myInteger);
    printf("Memory interpreted as float: %f\n", myFloat);

    float actualFloat = 1.1f;
    int *intPointer = (int*) &actualFloat;
    printf("\nActual float 1.1f represented as integer bits: %d\n", *intPointer);


    return 0;

}
