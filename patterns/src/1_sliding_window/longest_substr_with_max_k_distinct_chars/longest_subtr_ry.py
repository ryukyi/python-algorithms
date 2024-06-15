""" 
# Longest Substring with maximum K Distinct Characters (medium) ✩

Given a string, find the length of the longest substring in it with no more than K distinct characters.


#### Example 1
```
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
```

#### Example 2
```
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
```

#### Example 3
```
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
```

#### Example 4
```
Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".
```
"""

def longest_substr(arr, k):
    # window bigger than array
    if k >= len(arr):
        return len(arr)
    unique_char = set()
    max_left_idx, max_len, left = 0, 0, 0
    for right in range(len(arr)):
        if arr[right] in unique_char:
            continue
        elif arr[right] not in unique_char and len(unique_char) < k:
            unique_char.add(arr[right])
            continue
        elif max_len < right - left:
            max_len = right - left
            max_left_idx = left 
            print(f"max_len: {max_len}, max_left_idx: {max_left_idx}")
        left = right 
        unique_char = {arr[right]}
    print(f"string: {arr[max_left_idx:max_left_idx+max_len]}")
    return max_len


# Attempt2:
def longest_substr2(arr, k):
    distinct = {}
    left, max_idx, max_len = 0, 0, 0
    for right in range(len(arr)):
        distinct[arr[right]] = distinct.get(arr[right], 0) + 1
        if len(distinct) <= k:
            continue
        sum_d = sum(distinct.values()) - 1
        if sum_d > max_len:
            max_idx = left
            max_len = sum_d
        while len(distinct) > k:
            distinct[arr[left]] -= 1
            if distinct[arr[left]] == 0:
                del distinct[arr[left]]
            left += 1
    if sum_d > max_len:
        max_idx = left
        max_len = sum_d
    print(f"array: {arr[max_idx: max_idx + max_len]}")
    return max_len