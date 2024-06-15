# # Comparing Strings containing Backspaces (medium) ✩

# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.


# ### Example 1
# ```
# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
# ```

# ### Example 2
# ```
# Input: str1="xy#z", str2="xyz#"
# Output: false
# Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
# ```

# ### Example 3
# ```
# Input: str1="xp#", str2="xyz##"
# Output: true
# Explanation: After applying backspaces the strings become "x" and "x" respectively.
# In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
# ```

# ### Example 4
# ```
# Input: str1="xywrrmp", str2="xywrrmu#p"
# Output: true
# Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
# ```

def backspace_pop(string):
    result = []
    for char in string:
        if char == "#":
            result.pop()
        else:
            result.append(char)
    return result

def backspace_compare(str1, str2):
    return backspace_pop(str1) == backspace_pop(str2)

# OR

def backspace_compare1(str1, str2):
    def backspace_pop(string):
        result = []
        for char in string:
            if char == "#":
                result.pop()
            else:
                result.append(char)
        return result
    return backspace_pop(str1) == backspace_pop(str2)



    