
# Question1

def set_operations(a, b):

    return {
        "union": a | b,
        "intersection": a & b,
        "difference_a_minus_b": a - b,
        "difference_b_minus_a": b - a,
        "symmetric_difference": a ^ b,
    }


# Question2

def remove_common_elements(a, b):
    return a - b, b - a


# Question3

def is_subset(small, big):

    return small.issubset(big)


# Qestion 4

def print_greater_than(s, threshold):
    for x in s:
        if x > threshold:
            print(x)



# Question 5

def unique_list(lst):
    seen = set()
    unique = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            unique.append(x)
    return unique


#DEMO
if __name__ == "__main__":
    # Sample sets
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7}

    # 1) Set operations
    ops = set_operations(A, B)
    print("1) Set Operations:")
    print("   Union:              ", ops["union"])
    print("   Intersection:       ", ops["intersection"])
    print("   A - B:              ", ops["difference_a_minus_b"])
    print("   B - A:              ", ops["difference_b_minus_a"])
    print("   Symmetric Difference:", ops["symmetric_difference"])

    # 2) Remove common elements
    print("\n2) Remove common elements :")
    A2, B2 = {1, 2, 3, 4, 5}, {4, 5, 6, 7}
    A2, B2 = remove_common_elements(A2, B2)
    print("   A2 after removal:   ", A2)
    print("   B2 after removal:   ", B2)

    # 3) Subset check
    print("\n3) Subset check:")
    small = {1, 2}
    big = {1, 2, 3, 4}
    print("   Is {1,2} subset of {1,2,3,4}? ->", is_subset(small, big))
    print("   Is {1,2,5} subset of {1,2,3,4}? ->", is_subset({1, 2, 5}, big))

    # 4) Iterate and print > threshold
    print("\n4) Elements greater than 3 in set {1,2,3,4,5}:")
    print_greater_than({1, 2, 3, 4, 5}, 3)

    # 5) List -> set -> unique list
    print("\n5) Unique elements from list with duplicates:")
    dup_list = [3, 1, 2, 3, 4, 1, 5, 2, 5, 6, 6]
    print("   Unique :   ", unique_list(dup_list))



