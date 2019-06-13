str_1 = input()
k = 0
z = 0
str_1 = str_1.strip()
#print (str_1)
for x in str_1:
    if x == " ":
        k += 1
    if (x != " " and k != 0):
        k = 0
        z += 1
print (z + 1)

