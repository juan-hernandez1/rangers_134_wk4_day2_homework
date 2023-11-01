# Exercise #1
# Reverse the list below in-place using an in-place algorithm.
# For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']

def swap_words(words, v, w, x, y, z):
    words[v], words[w], words[x], words[y], words[z] = words[z], words[y], words[x], words[w], words[v]
    return words

print(f"Before swap: {words}")
swap_words(words, 4, 3, 2, 1, 0)
print(f"After swap: {words}")


# Exercise #2
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def count_words(text):
    word_count = {}
    words = text.split()

    for word in words:
        word = word.strip(",.!?").lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

word_count = count_words(a_text)
print("\n")
print(word_count)
print("\n")


# Exercise #3
# Use binary search to return the index of the target num

# cool_list = [2, 5, 6, 12, 45, 47, 98, 123, 1000]
# target = 123

def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        potential_match = array[middle]
        if target == potential_match:
            return f"The index is... {middle}"
        elif target < potential_match:
            right = middle - 1
        else:
            left = middle + 1
    return -1

binary_search([2, 5, 6, 12, 45, 47, 98, 123, 1000], 123)