#include <stdio.h>

int main()
{
    int n, a = 0, b = 1, next, count = 0;

    printf("Enter the number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci Series:\n");

    while (count < n)
    {
        printf("%d ", a);
        next = a + b; // Calculate next term
        a = b;
        b = next;
        count++;
    }

    printf("\n");
    return 0;
}
