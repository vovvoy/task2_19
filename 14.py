str_1 = input()
l_index = str_1.find('f')
r_index = str_1.rfind('f')
if l_index != -1:
    print (l_index)
if l_index != r_index and r_index != -1:
    print (r_index)

