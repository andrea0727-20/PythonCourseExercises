
from itertools import repeat


number = int(input("Enter a number of times that you want the word to be repeated: "))
word = input("Enter a word: ")

for value in repeat(word, number):
    print(value)