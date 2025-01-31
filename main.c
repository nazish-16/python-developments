#include <stdio.h>

int main() {
    int low, high, middle, n, key, array[100];

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter %d elements in ascending order:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    printf("Enter the element you want to search: ");
    scanf("%d", &key);

    low = 0;
    high = n - 1;
    middle = (low + high) / 2;

    while (low <= high) {
        if (array[middle] == key) {
            printf("%d found at location %d\n", key, middle + 1);
            return 0; 
        } else if (array[middle] < key) {
            low = middle + 1;
        } else {
            high = middle - 1;
        }
        middle = (low + high) / 2;
    }

    printf("Not found\n");
    return 0;
}