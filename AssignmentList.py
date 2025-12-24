#Question1
def dedupe_preserve_order(lst):
    result = []
    seen = []
    for x in lst:
        if x not in seen:  # O(n) check: overall O(n^2) in worst case
            seen.append(x)
            result.append(x)
    return result

# Demo
data = [3, 1, 2, 3, 2, 4, 1, 5, 5]
print(dedupe_preserve_order(data))  # [3, 1, 2, 4, 5]

#Question2

def evens_only(nums):
    return [n for n in nums if n % 2 == 0]

# Demo
nums = [10, 11, 12, 13, 14, 15]
print(evens_only(nums))  # [10, 12, 14]


#Question3


def second_largest(lst):
    uniq = dedupe_preserve_order(sorted(lst, reverse=True))
    if len(uniq) < 2:
        raise ValueError("No second largest among distinct values")
    return uniq[1]


# Demo
print(second_largest([5, 1, 5, 3, 4]))  # 4
print(second_largest([-1, -5, -3, -3]))  # -3


#Question 4
def sums_of_inner_lists(nested):
    return [sum(inner) for inner in nested]

# Demo
nested = [[1, 2, 3], [10, -5, 5], [], [7]]
print(sums_of_inner_lists(nested))  # [6, 10, 0, 7]

#Question 5

import copy

def demonstrate_copy_behavior():
    original = [[1, 2], [3, 4], [5, [6, 7]]]

    shallow = original.copy()         # or list(original) or copy.copy(original)
    deep = copy.deepcopy(original)

    # Mutate inner elements
    original[0][0] = 999            # change inside first inner list
    original[2][1].append(8)        # mutate nested inner list [6,7] -> [6,7,8]

    print("Original:", original)
    print("Shallow :", shallow)     # reflects changes (shared inner lists)
    print("Deep    :", deep)        # unaffected (independent copies)

# Demo
demonstrate_copy_behavior()
# Example output:
# Original: [[999, 2], [3, 4], [5, [6, 7, 8]]]
# Shallow : [[999, 2], [3, 4], [5, [6, 7, 8]]]
# Deep    : [[1, 2], [3, 4], [5, [6, 7]]]


