"""
- For the first 5 numbers (subarray from index 0-4), the average is: (1+3+2+6-1)/5 => 2.2
- The average of next 5 numbers (subarray from index 1-5) is: (3+2+6-1+4)/5 => 2.8
- For the next 5 numbers (subarray from index 2-6), the average is: (2+6-1+4+1)/5 => 2.4
- For the next 5 numbers (subarray from index 3-7), the average is: (6-1+4+1+8)/5 => 3.6
- For the next 5 numbers (subarray from index 4-8), the average is: (-1+4+1+8+2)/5 => 2.8

```
Input: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
"""

def ave_subarrays(arr, k):
    if len(arr) == 0:
        return float('inf')
    result = []
    for right in range(k, len(arr)+1):
        left = right - k
        sum_window = sum(arr[left:right])
        if sum_window == 0:
            return float('inf')
        result.append(sum_window / k)
    return result
        
        




"""
Interview slight change
Input: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [1.0, 2.0, 2.0, 3.0, 2.2, 2.8, 2.4, 3.6, 2.8, 3.75, 3.67, 5.0, 2.0]

Explanation

- Set the first window to only include 1
- Set the second window to include 1+3
- Set the third window to include 1+3+2
- Continue sliding the window until a full window 5 numbers (subarray from index 0-4)
- the last windows will be [8,2] then [2]
"""

# Attempt 1:
from typing import List
from random import randint

def random_number_list(length, min_val, max_val):
    return [randint(min_val, max_val) for num in range(length)]

def mean(arr: List) -> float:
    arr_len = len(arr)
    arr_sum = sum(arr)
    if arr_len == 0:
        return 0.0 
    if arr_sum == 0:
        return float('inf')
    return round(arr_sum / arr_len, 2)

def index_is_valid(idx, arr_len):
    return 0 <= idx < arr_len

def rolling_mean(arr: List, window: int) -> List[float]:
    rolling_means = []
    arr_len = len(arr)
    for i in range(arr_len):
        indexes = range(max(0, i - window + 1), i + 1)
        arr_window = [arr[idx] if index_is_valid(idx, arr_len) else 0 for idx in indexes]
        rolling_means.append(mean(arr_window))
    return rolling_means

if __name__ == "__main__":
    ran_num_list = random_number_list(10, -2, 10)
    print(ran_num_list)
    roll_mean = rolling_mean(ran_num_list, 3)
    print(roll_mean)

# Attempt 2:
# Input: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

def rolling_mean2(arr: List, K: int):
    arr_len = len(arr)
    if arr_len == 0:
        return 0
    if arr_len <= K:
        return mean(arr)
    roll_mean = []
    for idx in range(arr_len+ K -1):
        start_index = max(0, idx - K +1)
        end_index = min(idx + 1, arr_len)
        slice = arr[start_index:end_index]
        avg = mean(slice)
        roll_mean.append(avg)
        print(f"idx: {idx}, start: {start_index}, end: {end_index}: slice: {slice} mean: {avg}")
    return roll_mean

# Attempt 3:
def rolling_mean3(arr: List, K: int):
    arr_len = len(arr)
    if arr_len == 0:
        return 0
    if arr_len <= K:
        return mean(arr)
    roll_mean = []
    for idx in range(len(arr)+K-1):
        start = max(0, idx - K + 1)
        end = min(idx + 1, len(arr))
        window = arr[start:end]
        roll_mean.append(mean(window))
    return roll_mean


def rolling_mean4(arr, k):
    result = []
    left = 0
    for right in range(k-1, len(arr)):
        win_sum = sum(arr[left:right+1])
        if win_sum == 0:
            result.append(float('inf'))
        else:
            result.append(sum(arr[left:right+1])/k)
        left += 1
    return result

# Input: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]