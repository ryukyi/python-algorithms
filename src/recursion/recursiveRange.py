# RecusrsiveRange --> Write a recursive function that accepts a number and adds all the number from 0 to the number passed
# Reverse --> Write a recursive function that accepts a string and returns a new string in reverse
# IsPalindrome --> Write a recursive function if the string passed to is a palindrome, otherwise return false
# SomeRecursive --> Write a function which accepts an array and a callback. The function returns true if a single value in the array returns true when passed to the callback, otherwise it returns false
# Flatten --> write a recursion function called flatten which accepts an array of arrays and returns a new array with all the values flattened

def recursiveRange(n):
    assert n >= 0, "Number must be greater than or equal to 0"
    if n == 0:
        return 0
    else:
        return n + recursiveRange(n-1)


print(recursiveRange(6))  #ans --> 21
print(recursiveRange(10)) #ans --> 55