//You already know Babylonian root-finding from the C-Quiz, where you had to find the pseudocode. Now you have to implement it in C. We provide a CS50 Sandbox as a starting point.
//
//To check your code, you can use:
//
//check50 fau-is/IntroCS/CBabylon
//
//
//
//To remind you:
//
//To calculate \sqrt[k]{a}, the Babylonian root-finding method can be employed. Herefore, the zero points of a function f(x) = x^k - a have to be found with the following iterative computation:
//
//x_{n+1} = \frac{(k-1) \times x_n^k + a}{k \times x_{n}^{k-1}}
//
//Starting with an appropriate initial value x_0, the aforementioned equation is iterated until the result reaches a sufficiently exact value i.e. until two successive values do not differ more than a certain threshold \epsilon: |x_{n+1} - x_n| \leq \epsilon. For simplification reasons the following requirements have to be met for the task:
//
//if k is negative or 0, then the result should always be -1
//if a is negative and k is an even number, then the result should be -1
//if a is negative, then the first guess x_0 = -2; otherwise, x_0 = 2 and the non-negative root should be calculated

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	if (argc != 3)
 	{
        printf("Usage: ./babylon k a\n");
        return 1;
    }
    int k = atoi(argv[1]);
    int a = atoi(argv[2]);
    float eps = 0.01;

    //TODO: conditions where execution is rejected. Make sure "Try again...\n" is printed!

    //TODO: follow instructions
    
    //TODO: print result with 5 decimal places
    return 0;
}