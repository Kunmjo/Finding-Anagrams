# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    if len(word) == len(anagram):
        sorted_a = sorted(word)
        sorted_b = sorted(anagram)
        if sorted_a == sorted_b:
            print("True")
        else:
            print("False")
    else:
        print("False")
    # return True

# find_anagram(word="appled", anagram="elbow")
find_anagram("below", "elbow")