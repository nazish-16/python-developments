#include <stdio.h>
#include <string.h>

int main() {
    char s1[100], s2[100], a[100], b[100];
    int n;

    printf("Enter the first string s1: ");
    gets(s1);

    printf("Enter the second string s2: ");
    gets(s2);

    n = strlen(s2);
    printf("Length of second string s2 is: %d\n", n);

    if (strcmp(s1, s2) == 0) {
        printf("The strings are equal.\n");
    } else {
        printf("The strings are not equal.\n");
    }

    strcat(s1, s2);
    printf("After concatenation, s1 is: %s\n", s1);

    printf("Enter a string to be copied into another: ");
    gets(a);

    strcpy(b, a);
    printf("The entered string '%s' is copied into b as: %s\n", a, b);

    return 0;
}