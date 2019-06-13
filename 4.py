hour_1 = int (input())
minet_1 = int (input())
sec_1 = int (input())
hour_2 = int (input())
minet_2 = int (input())
sec_2 = int (input())
total_1 = hour_1 * 3600 + minet_1 * 60 + sec_1
total_2 = hour_2 * 3600 + minet_2 * 60 + sec_2
z = abs(total_1 - total_2)
a = z // 3600
b = z % 3600 // 60
c = z % 60

print (a * 3600 + b * 60 + c)
