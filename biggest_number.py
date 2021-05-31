arr = []
x = 0
for _ in range(int(input("input range :"))):
    arr.append(int(input("input number :")))
for i in arr:
    if i > x:
        x = i
print(x)
