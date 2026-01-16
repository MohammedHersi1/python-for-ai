# #Work 6: Count vowels in a word
Name=input("Enter the string: ").lower()
vowel_count=0
for char in Name:
    if char in "aeiou":
        vowel_count+=1
print("Number of the vowels in the word: ",vowel_count)