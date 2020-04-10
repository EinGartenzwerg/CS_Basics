//Now that you know how to implement some search-algorithms in C, we need to dive even deeper and start with sorting. In this exercise, you should implement the Bubble Sort algorithm that sorts an array of integers into either ascending or descending order.
//
//Like previously, we provide a CS50 sandbox as a starting point.
//
//You can check your code with check50:
//
//check50 fau-is/IntroCS/CBubbleSort
//
//We use a similar array to the one in the search tasks:
//
//int to_sort[10] = {4711, 8, 2, 33, 5, 23, 42, 78, 123, 2398};
//
//The program should behave as follows:
//
//If the program is called with argv[1] is equal to "asc" then it should sort the array to_sort in ascending order and print the result (a print function is provided).
//
//./bubble asc
//
//[2, 5, 8, 23, 33, 42, 78, 123, 2398, 4711]
//
//If the program is called with argv[1] is equal to "dsc" then it should sort the array to_sort in descending order and print the result (a print function is provided).
//
//./bubble dsc
//
//[4711, 2398, 123, 78, 42, 33, 23, 8, 5, 2]
//
//Print usage if the user provides neither asc nor dsc:
//
//./bubble asdf
//
//Usage: ./bubble [asc|dsc]\n

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int to_sort[10] = {4711, 8, 2, 33, 5, 23, 42, 78, 123, 2398};

// Helper to print arrays
void pretty_printer(int *to_print);

int main(int argc, char **argv)
{
    //sorting direction
    int asc = 0;
    if (argc != 2)
    {
        printf("Usage: ./bubble [asc|dsc]\n");
        return 1;
    }

    //TODO: check if sorting in asc (ascending) or dsc (descending) order
    

    // Some helpers
    // Limit (length of the array - 1)
    // HINT: You need to compare the ith element with the i+1th element
    int limit = sizeof(to_sort)/sizeof(to_sort[0]) - 1;
    
    // Was there a "bubble" before (Did the program swap at least two numbers), initially true
    bool swp = true;
    
    //TODO
    //HINT: Do you need a do-while or while loop when swp = true initially?
    //HINT: It might make sense to bubble values (up or down)  with a for loop
    
    
    return 0;

}

void pretty_printer(int *to_print, size_t size)
{
    printf("[");
    for (int i = 0; i < size; i++)
    {
        if (i == size - 1)
        {
            printf("%i", to_print[i])   
        }
        else
        {
            printf("%i, ", to_print[i]);
        }
    }
    printf("]\n");
}
