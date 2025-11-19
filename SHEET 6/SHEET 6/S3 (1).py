# Write a program to input T strings (S) from user and print 1 if it is palindrome otherwise print 0.
# NOTE:A string is palindrome if it reads the same from backward as from forward.
# Input:
# 3
# abcba
# axax
# abba
# Output:
# 1
# 0
# 1

s = input()
if s == s[::-1]:
    print("1")
else:
    print("0")
