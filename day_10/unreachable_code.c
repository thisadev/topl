# include <stdio.h>

int main(void) {

    printf("Code before the check.\n");

    // This condition is always false
    if (1 < 0) {
        // *** Start of Unreachable Code ***
        printf("This message is inside the unreachable block.\n");
        int dead_variable = 100;
        printf("This will also not print: %d\n", dead_variable);
        // *** End of Unreachable Code ***
    }

    printf("Code after the check (this is reachable).\n");

    return 0;
}
