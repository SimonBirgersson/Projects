# List comprehensions
# Creates new lists based on other lists

# For example, let's say we need to create a list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)

# using list comprehensions, this is much quicker
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"] # THIS IS KEY
print(words)
print(word_lengths)

# EXCERCISE - Using a list comprehension, create a new list called "newlist" out of the list "numbers", which contains only the positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x >= 0] # so here int(x) generates a list containing the integers for "numbers" if they are equal to or larger than 0.
print(newlist)
