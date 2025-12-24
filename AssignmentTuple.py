
# Question 1
def tuple_min_max_manual(t):
    """Manual scan without using min/max built-ins"""
    if not t:
        raise ValueError("Empty tuple has no min/max")
    mn = mx = t[0]
    for x in t[1:]:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    return mn, mx


# 2) Convert a list of tuples into a dictionary

def tuples_to_dict(pairs):
    d = {}
    for k, v in pairs:
        d[k] = v
    return d


# Question3

def count_occurrence(t, target):
    count = 0
    for x in t:
        if x == target:
            count += 1
    return count


# Quesion4

def demo_mutable_inside_tuple():

    t = ([1, 2, 3], {"name": "Soham", "score": 90})
    # Modify the list
    t[0].append(4)
    t[0][1] = 99
    # Modify the dict
    t[1]["score"] = 95
    t[1]["passed"] = True
    return t


# Question5
def swap_tuples_temp(a, b):

    temp = a
    a = b
    b = temp
    return a, b


# DEMO
if __name__ == "__main__":
    # 1) Min/Max
    print("1b) Min/Max (manual):  ", tuple_min_max_manual((10, -5, 20, 0)))

    # 2) Tuples -> Dict
    pairs = [("a", 1), ("b", 2), ("c", 3), ("b", 99)]
    print("2) Dict (overwrite):   ", tuples_to_dict(pairs))


    # 3) Count occurrences
    t = (1, 2, 3, 2, 2, 4)
    print("3) Count of 2:", count_occurrence(t, 2))

    # 4) Mutable-in-tuple modifications
    print("4) Mutable-in-tuple:", demo_mutable_inside_tuple())

    # 5) Swapping tuples
    a2, b2 = (10, 20), (30, 40)
    print("5b) Swapped (temp):    ", swap_tuples_temp(a2, b2))
