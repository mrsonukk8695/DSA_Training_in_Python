#WAP to compare the user define strng with vowels and count the numbers of vowels present in the string.

name=input("Enter String")
vc=len([char for char in name if char in "aeiouAEIOU"])
vc