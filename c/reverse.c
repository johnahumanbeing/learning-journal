#include <stdio.h>
#include <string.h>

/**
 * reverseString - Reverses a string
 * @str: The string to be reversed
 */
void reverseString(char *str)
{
    int length = strlen(str);
    int i;
    char temp;

    for (i = 0; i < length / 2; i++)
    {
        temp = str[i];
        str[i] = str[length - i - 1];
        str[length - i - 1] = temp;
    }
}

/**
 * main - Entry point
 *
 * Return: Always 0 (Success)
 */
int main(void)
{
    char str[] = "hello";

    reverseString(str);
    printf("Reversed String: %s\n", str);

    return (0);
}
