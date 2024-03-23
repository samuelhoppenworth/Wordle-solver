import math
def f():
    list = []
    for i in range(22, 99):
        num = i*i
        print(i*i)
        str_num = str(num)
        if str_num[0] == str_num[1] and str_num[2] == str_num[3]:
            list.append(num)
    return list

def m():
    list = []
    for i in range(1000, 2000):
        print(i)
        s1 = int(i%10) + int((i/10)%10) + (i/100)%10 +i/1000
        print(f"s1: {s1}")
        s2 = s1%10 + s1/10
        if s1 + s2 + i == 1500:
            list.append(i)
    return list



print(m())
