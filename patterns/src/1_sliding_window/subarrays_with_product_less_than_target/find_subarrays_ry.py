# # Subarrays with Product Less than a Target (medium) ✩

# Given an array with positive numbers and a positive target number, 
# find all of its contiguous subarrays whose product is less than the target number.

# ### Example 1
# Input: [2, 5, 3, 10], target=30 
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.

# steps:
# right and left = 0
# add to rolling product e.g. 1*arr[left] == 1*2 = 2
# check rolling_product < t
# true => append to result
# and increase right 1 and add right to product
# 

# ### Example 2
# Input: [8, 2, 6, 5], target=50 
# Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
# Explanation: There are seven contiguous subarrays whose product is less than the target.

def subarrays_with_product_less(arr, t):
    left, rolling_product = 0, 1
    result = []
    for right in range(len(arr)):
        rolling_product *= arr[right]
        while rolling_product > t and left <= right:
            print(f"While: rolling_product: {rolling_product}, left: {left}, right: {right}")
            print(f"While: {arr[left:right+1]}")
            left += 1
            rolling_product /= arr[left]

        print(f"Outside: rolling_product: {rolling_product}, left: {left}, right: {right}")
        rolling_product *= arr[right]
    
    return result

if __name__ == "__main__":
    result = subarrays_with_product_less([2, 5, 3, 10], 30)
    print(result)
