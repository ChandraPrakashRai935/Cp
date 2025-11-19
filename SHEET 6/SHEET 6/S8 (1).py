# You are given string (A) and you have to print the reverse order of words.
# Input:
# Suyash Chaudhary
# Output:
# Chaudhary Suyash

A = input()
rev_A = A.split()[::-1]
current_String = ' '.join(rev_A)
print(current_String)