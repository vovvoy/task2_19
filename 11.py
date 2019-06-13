str_1 = input()

print (str_1[2])

print(str_1[len(str_1) - 2])

for i, x in enumerate(str_1):
    if i == 4:
        print (str_1[i])
        break
    print (x, end = "")
    
print (str_1[len(str_1) - 2]+str_1[len(str_1) - 1])
 
z = 1
for x in str_1:
    if z % 2 == 0:
        print (x, end = "")
    z += 1
print ("\n")
z = 1
for  x in str_1:
    if z % 2 == 1:
        print (x, end = "")
    z += 1
print ("\n")
print (str_1 [::-1])

str_2 = str_1 [::-1]
z = 1
for x in str_2:
    if z % 2 == 0:
        print (x, end = "")
    z += 1
print ("\n")
    



print (len(str_1))















