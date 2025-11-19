T = int(input())
S = input()
vowels = 0
const = 0
for i in S:
    if i in "aeiouAEIOU":
        vowels += 1
    else:
        const += 1
print(vowels, const)