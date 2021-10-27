#Author:JTI 10/27/21

word1 = input("Enter word: ")
word2 = input("Enter another word: ")

if word1 < word2:
    print(word1 + " comes before " + word2 + " in the alphebet")
elif word2 < word1:
    print(word2 + " comes before " + word1 + " in the alphebet")
else:
    print(word1 + " and " + word2 + " are the same")