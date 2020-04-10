#### Compiling consists of four distinct activities. What are those activities and what is their execution order?
1. Preprocessing
2. Compiling
3. Assembling
4. Linking


#### What are the advantes of LinkedLists Compared to Arrays and vice verca?
- Linked Lists: Dynamic Number of Elements; Insertion of Elements
- Arrays: Random Access; Size (Allocated Memory) for n elements is smaller; Binary Search 


#### What is the corresponding ASCII endocing?
- Hello           -     72 101 108 108 111
- HI!             -     72 73 33
- 72 73 33        -     55 50 32 55 51 32 51 51 32


#### You know the concept of abstraction: "Videos are just bunches of images. Images are just bunches of colors. Colors are just patterns of bits. And bits, at the end of the day, are just the result of electricity coming into my machine or transistors turning switches on and off." Describe a different abstraction that ends with computer bits!

#### Please convert the binary number representation 1100101002 to a decimal number, that represents an HTTP status code. Which of the following HTTP-Error Codes did your program catch?
- 	400 - Bad Request
-   200 - OK
-   403 - Forbidden
-   404 - Not found


#### Assume we want to execute a line of code (for example print Hello World) 21 times in C. 
    for (__________________________)
    {
         printf("Hello, world\n");
    }
Which of the following answers execute the program as desired.

- 	int i = 0; i < 21, i++
-   int i = 0; i < 42; i += 2
-   int i = 2; i < 42; i += 2
-   i = 2; i < 42; i += 2


#### Create an Adjacency list from a given graph.

#### Create an Adjacency matrix from a given graph.

#### Which of the following is 42 represented in binary, hexadecimal and octadecimal. The lenght of the values is one byte. Calculate it manually!
- 42 in hexadecimal - 2a
- 42 in octadecimal - 52
- 42 in binary - 0010 1010

#### Navigate trough file systems, copy files, list directories and execute programs through the command line.

#### If "char *s" is a variable that stores a string and can conceptually be seen as an array of chars. Keeping that in mind, what would "char **s" conceptually be?
- the ascii value of the first char of the string
- an array of chars
- an array of strings
- the first char of the string

#### You know how to create a one-sided Linked List in C. Now, we need a list that we cannot only iterate in one way but in both ways (forward and backward). Additionally, we want this list to be circular (i.e. we can iterate infinitely over this list). Which of the pointers do we need to create such a list?
    ​struct node
    {
        int n;
        // your answer will be placed here
    };

multiple selections possible:
- 	struct *next;
- struct node *next;
- struct node *pre;
- int *next;
- struct pre *node;
- struct next *node;

#### Imagine you have a LinkedList, that looks like this: A -> B -> C -> D -> E
One node of the LinkedList looks like this:

    typedef struct NODE {
        char *a;
        struct NODE* next;
    } node;

How would you access the char value of the third element in the LinkedList: "node *list2 = malloc(sizeof(node))"? (Assume the list is already filled with at least 3 elements)

multiple possible:
- list2[2];
- list2->next->next->a;
- list2.next.next;
- list2->next->next.a;
- (*list2).next->next->a;
- list2[3];
- (*list2).(*next).next.a;
- none of the above

#### Imagine you have a LinkedList that looks like this: A -> B -> C -> D -> E
One node of the LinkedList looks like this:

    typedef struct NODE {
        char *a;
        struct NODE* next;
    }node;

How would you access the third element's char value of the LinkedList: "node list;"? (Assume there is already a list with at least three elements!)

multiple possible:
- list.next->next->a
- list.next.next;
- list.next.next->a;
- list[3];
- list.next.next.a;
- list.(*next).(*next).a
- none of the above


#### Suppose you want to allocate memory for one integer. How would you complete the following function:

    void f(void){
    
    a = _______________________;
    
    }


#### What would be displayed on the page with the following underlying HTML:

    <!DOCTYPE html>
    <html lang="en">
       <head>
          <title>
             IntroCS is ez!
          </title>
       </head>
       <body>
       </body>
    </html>

- IntroCS is ez!
- IntroCS is ez!
- 
- none of the above


#### Assume this is a snippet of code in a main() function, to compare two strings:

    string str1 = "hello, world\n";
    string str2 = "hello, world\n";
    if (str1 == str2)
    {
        printf("Yay! The strings are equal!");
    }
    printf("Nay! The strings are not equal!");

What would the program print, and why? What changes would you make in the snippet?