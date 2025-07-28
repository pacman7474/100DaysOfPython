s = ""
s = input("Enter String> ")
i = int(input("Enter an index> "))
t = ""

for x in range(len(s)):
    if x != i:
        t+=s[x]
print(t)
