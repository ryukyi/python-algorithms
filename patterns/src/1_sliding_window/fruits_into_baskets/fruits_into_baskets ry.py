# Fruit=['A', 'B', 'C', 'A', 'C'] => 3 because window with ['C', 'A', 'C'] has 2 C and 1 A
# Fruit=['A', 'B', 'C', 'B', 'B', 'C'] => 5 because window with ['B', 'C', 'B', 'B', 'C'] has 3 B and 2 C
from typing import List

def fruits_into_basket(arr: List[str]) -> int:
    if not arr:
        # empty list will have no count
        return 0
    largest_count: int = 1
    for idx in range(len(arr)):
        if idx == 0:
            fruit_count = {arr[idx]: 1}
        elif arr[idx] in fruit_count:
            fruit_count[arr[idx]] += 1
        # only allowed 2 baskets. Add new fruit if less than 2
        elif arr[idx] not in fruit_count and len(fruit_count.keys()) < 2:
            fruit_count[arr[idx]] = 1
        else:
            # there must be a third fruit type. Reset and check count.
            print(f"counting: {fruit_count}")
            largest_count = max(sum(v for _, v in fruit_count.items()), largest_count)
            # reset the fruit count baskets
            if arr[idx-1] == arr[idx]:
                fruit_count = {arr[idx]: 2}
            else:
                fruit_count = {arr[idx-1]: 1, arr[idx]: 1}
            print(f"Setting new fruit: {fruit_count}")
    return largest_count

# Attempt 2:
# Fruit=['A', 'B', 'C', 'A', 'C'] => 3 because window with ['C', 'A', 'C'] has 2 C and 1 A
# Fruit=['A', 'B', 'C', 'B', 'B', 'C'] => 5 because window with ['B', 'C', 'B', 'B', 'C'] has 3 B and 2 C

def fruits_into_basket1(arr: List[str]) -> int:
    fruit_basket: dict = {}
    total = 1
    for idx in range(len(arr)):
        if arr[idx] not in fruit_basket and len(fruit_basket.keys()) < 2:
            fruit_basket[arr[idx]] = 1
        if arr[idx] not in fruit_basket and len(fruit_basket.keys()) == 2:
            total = max(total, sum(fruit_basket.values()))
            fruit_basket[arr[idx]] = 1
            for key in fruit_basket:
                if key not in [arr[idx], arr[idx-1]]:
                    old_key = key
                    break
            fruit_basket.pop(old_key)
    return total
            


# Attempt 3:
# Fruit=['A', 'B', 'C', 'A', 'C'] => 3 because window with ['C', 'A', 'C'] has 2 C and 1 A
# Fruit=['A', 'B', 'C', 'B', 'B', 'C'] => 5 because window with ['B', 'C', 'B', 'B', 'C'] has 3 B and 2 C
def fruits_into_basket2(arr, baskets: int = 2):
    # need to store order
    fruits = {arr[0]: 1}
    # keep state of order in and out
    ordered_fruit = list(arr[0])
    max_fruit = 0
    for right in range(1, len(arr)):
        if arr[right] in fruits:
            fruits[arr[right]] += 1
        elif arr[right] not in fruits and len(fruits) < baskets:
            ordered_fruit.append(arr[right])
            fruits[arr[right]] = 1
        else:
            # baskets are full and need to rotate
            max_fruit = max(max_fruit, sum(fruits.values()))
            fruits.pop(ordered_fruit[0])
            fruits[arr[right]] = 1
            ordered_fruit = ordered_fruit[1::]
            ordered_fruit.append(arr[right])
        max_fruit = max(max_fruit, sum(fruits.values()))
        print(f"fruits: {fruits}, ordered_fruit: {ordered_fruit}")
    return max_fruit
            

# Attempt 4:
# Fruit=['A', 'B', 'C', 'A', 'C'] => 3 because window with ['C', 'A', 'C'] has 2 C and 1 A
# Fruit=['A', 'B', 'C', 'B', 'B', 'C'] => 5 because window with ['B', 'C', 'B', 'B', 'C'] has 3 B and 2 C

from collections import OrderedDict


def fruits_into_basket4(arr, baskets):
    fruits = OrderedDict()
    max_length = 0
    for right in range(len(arr)):
        if arr[right] in fruits:
            fruits[arr[right]] += 1
        elif arr[right] not in fruits and len(fruits) < baskets:
            fruits[arr[right]] = 1
        else:
            max_length = max(max_length, sum(fruits.values()))
            fruits.popitem(last=False)
            fruits[arr[right]] = 1
        max_length = max(max_length, sum(fruits.values()))
        print(f"max: {max_length}, fruits: {fruits}")        
    return max_length

# Attempt5:
# #### Example 1
# ```
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
# ```

def fruits_into_basket5(arr):
    baskets = {}
    fruit_order = []
    max_fruits = 0
    for right in range(len(arr)):
        if arr[right] in baskets:
            baskets[arr[right]] += 1
        elif len(baskets) < 2:
            baskets[arr[right]] = 1
            fruit_order.append(arr[right])
        else:
            max_fruits = max(max_fruits, sum(baskets.values()))
            print(f"popping: {fruit_order}")
            baskets.pop(fruit_order[0])
            # reordering
            fruit_order[0], fruit_order[1] = fruit_order[1], arr[right]
            baskets[arr[right]] = 1
    max_fruits = max(max_fruits, sum(baskets.values()))
    return max_fruits

        



























