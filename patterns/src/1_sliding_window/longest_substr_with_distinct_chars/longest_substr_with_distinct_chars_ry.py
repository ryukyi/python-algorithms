"""
# Longest Substring with Distinct Characters (hard) ✩

Given a string, find the length of the longest substring, which has all distinct characters.


#### Example 1
```
Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".
```

#### Example 2
```
Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".
```

#### Example 3
```
Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".
```
"""

def long_substring(string):
    max_length, max_left_idx = 0, 0
    left = 0
    distinct_char = set()
    for right in range(len(string)):
        if string[right] not in distinct_char:
            distinct_char.add(string[right])
            continue
        if max_length < right - left:
            max_length = right - left
            max_left_idx = left
        left = right
        distinct_char = {string[right]}
    print(f"string: {string[max_left_idx : max_left_idx + max_length]}")
    return max_length



# Attempt 2:
# ```
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring with distinct characters is "abc".
# ```

# #### Example 2
# ```
# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring with distinct characters is "ab".
# ```

# #### Example 3
# ```
# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings with distinct characters are "abc" & "cde".
def long_substring2(string):
    distinct = set()
    max_len, max_idx, left = 0, 0, 0
    for right in range(len(string)):
        if string[right] in distinct:
            if len(distinct) > max_len:
                max_idx = left
                max_len = len(distinct)
            distinct = {string[right]}
            left = right
        else:
            distinct.add(string[right])
    print(string[max_idx:max_idx + max_len])
    return max_len

