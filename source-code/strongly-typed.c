// Here we are importing a library from the C programming language that
// will allow us to use the printf() function below
#include <stdio.h>

int main() {
    
    // Declare the variable
    // Notice how we must include the "int" keyword before our variable declaration 
    // unlike in Python
    int myVariable;
    
    // Assign the variable
    myVariable = 37612;
    
    // I could have written the above two lines of code like so: 
    // int myVariable = 37612;
    // but I wanted to show the distinct steps of declaring and then assigning 
    // a value to a variable in C
    
    // Here we are using a built in C function printf() to print the output of the 
    // variable to the terminal
    printf("%i\n", myVariable);
}