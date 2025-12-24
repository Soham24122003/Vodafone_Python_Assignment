# Question 1
def count_components(s: str):
    vowels_set = set("aeiouAEIOU")
    vowels = consonants = digits = specials = 0

    for ch in s:
        if ch.isalpha():
            if ch in vowels_set:
                vowels += 1
            else:
                consonants += 1
        elif ch.isdigit():
            digits += 1
        else:
            specials += 1

    return {"vowels": vowels, "consonants": consonants, "digits": digits, "specials": specials}


# Demo
s = "Vodafone @2025 rocks!"
counts = count_components(s)
print(counts)  



# Question 2
def reverse_each_word(s: str) -> str:
    return " ".join(word[::-1] for word in s.split())

#Demo
print(reverse_each_word("I am soham"))


#Question 3
def is_palindrome_indexing(s: str) -> bool:
    
    s = s.replace(" ", "").lower()
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def is_palindrome_slicing(s: str) -> bool:
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Demo
print(is_palindrome_indexing("Madam"))      # True
print(is_palindrome_slicing("A man a plan a canal Panama"))  # True
print(is_palindrome_slicing("Vodafone"))    # False


#Question 4

from collections import Counter

def char_frequency(s: str):
    return dict(Counter(s))

# Demo
s = "abbcccde!!"
freq = char_frequency(s)
print(freq) 


#Question 5

def demonstrate_immutability():
    try:
        s = "Vodafone"
        
        s[0] = 'B'
    except TypeError as e:
        print("Caught TypeError as expected:", e)

    # Correct way: create a new string
    s = "Vodafone"
    s_modified = 'B' + s[1:]
    print("Original:", s)
    print("Modified:", s_modified)

# Demo
demonstrate_immutability()
# Output:
# Caught TypeError as expected: 'str' object does not support item assignment
# Original: Vodafone
# Modified: Bodafone

