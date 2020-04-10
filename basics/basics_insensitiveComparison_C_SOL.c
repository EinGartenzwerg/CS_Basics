//Write a program that performs a case-insensitive comparison of two strings (char *) given as command-line arguments.
//
//Therefore, finish the code in the main() function and the code in the strlwr() function!
//
//Requirements:
//
//Main:
//
//The main function should return 0, if the strings are equal
//The main function should return 1, if the strings are not equal
//strlwr:
//
//Does not leak memory
//returns a char* that is the lowercase parameter.
//Hints:
//
//You may use standard functions from stdio.h, string.h, and ctype.h.

#include <stdio.h>
#include <string.h>
#include <ctype.h>

// makes a string lowercase
char *strlwr(char *string);

int main(int argc, char **argv)
{
    if (argc != 3)
    {
        return 1;
    }
    char *left =  strlwr(argv[1]);
    char *right = strlwr(argv[2]);

    if (strcmp(left, right) == 0)
    {
        return 0;
    }
    return 1;
}

char *strlwr(char *string)
{
    int i = 0;
    while (string[i])
    {
        string[i] = tolower(string[i]);
        i++;
    }
    return string;

}