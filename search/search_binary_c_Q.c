//In contrast to the previous task, where you programmed a linear search approach for an unsorted array of numbers, you will now implement a binary search algorithm for a sorted array of numbers.
//
//Like previously we provide a CS50 Sandbox with some starting code.
//
//Note: in the Sandbox, you can use the check50 command to check your solution:
//
//check50 fau-is/IntroCS/CBinarySearch --local
//
//You can run it without "--local", but it is faster when you run the check locally.
//
//Some description:
//
//int to_search[10] = {10, 20, 30, 40, 50, 60, 70 , 80, 90, 100};
//
//For the above-mentioned array the program should print:
//
//When the number is in the array, it should print the number and the index in the following way and exit with code 0 (main returns 0):
//
//./binary 10
//
//"Number 10 is at index 0"
//
//When the number is in the array, it should print the number in the following way and exit with code 1 (main returns 1):
//
//./binary 3
//
//"Number 3 not found"

#include <stdio.h>
#include <stdlib.h>

int to_search[10] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: ./binary Number\n");
        return 1;
    }
    int to_find = atoi(argv[1]);
    int array_length = sizeof(to_search)/sizeof(to_search[0]);
    
    // Helpers
    // Initial index of first element
    int start = 0;
    //Initial index of last element
    int end = array_length - 1;
    // Initial middle
    int middle = end / 2; 
    
    // TODO Iterative Binary Search 
    // Hint: Maybe a while loop helps
    
    
    printf("Number %i not found\n", to_find);
    return 1;

}
