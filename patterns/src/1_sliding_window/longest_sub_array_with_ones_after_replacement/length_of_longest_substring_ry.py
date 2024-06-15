"""
# Longest Subarray with Ones after Replacement (hard) ✩

Given an array containing 0s and 1s, if you are allowed to replace 
no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.


#### Example 1
```
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
```

#### Example 2
```
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
```
"""

def long_substring(arr, k):
    left, max_length, zero_counter = 0, 0, 0
    for right in range(len(arr)):
        if arr[right] == 0:
            zero_counter += 1

        max_length = max(max_length, right - left + 1)
        while zero_counter > k:
            if arr[left] == 0:
                zero_counter -= 1
            left += 1
        
    return max_length

# attempt2:
#### Example 1
# ```
# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
# ```

# #### Example 2
# ```
# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

def long_substring2(arr, k):
    left, length, max_length, zero_count = 0, 0, 0, 0
    for right in range(len(arr)):
        length += 1
        if arr[right] == 1:
            continue 
        elif arr[right] == 0 and zero_count == k:
            zero_count += 1
            while zero_count > k and left <= right:
                length -= 1
                if arr[left] == 0:
                    zero_count -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        else:
            zero_count += 1
    max_length = max(max_length, right - left + 1)
    print(f"window: {arr[left: left + max_length]}")
    return max_length
            
