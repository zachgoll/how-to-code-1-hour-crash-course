# This file is not necessarily part of the course, but was covered at the end of the video.

# Here we are importing a file.  Please refer to this StackOverflow post for 
# instructions on how to use this import syntax - https://stackoverflow.com/a/7583738
my_import = __import__("simple-function")

# Here, we are "calling" the simple_function() that is located in the simple-function.py
# file and storing the result, or "output" of this function in a variable.
my_result = my_import.simple_function(20)

# Here we are printing the variable that we had just assigned above.  It should equal 40
print(my_result)