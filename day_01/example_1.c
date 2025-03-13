#include <stdio.h>
#include "lib/uthash.h"

typedef struct {
    char name[50];  // Key
    int grade;      // Value
    UT_hash_handle hh; // Hash table handle
} Student;

int main() {
    Student *students = NULL, *s;

    // Add entries
    s = malloc(sizeof(Student));
    strcpy(s->name, "Thisara");
    s->grade = 85;
    HASH_ADD_STR(students, name, s);

    s = malloc(sizeof(Student));
    strcpy(s->name, "Gihan");
    s->grade = 92;
    HASH_ADD_STR(students, name, s);

    // Lookup
    HASH_FIND_STR(students, "Thisara", s);
    if (s) {
        printf("Thisara's grade: %d\n", s->grade);
    }

    // Clean up
    HASH_CLEAR(hh, students);
    return 0;
}
