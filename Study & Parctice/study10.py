# x = 10000
# t = 0.0325
# Years = 0

# while True:
#     x *= (1 + t)
#     Years += 1
#     if x >= 20000:
#         print(f"{Years}年が必要。")
#         break


# x = 100 # ボールの高さ
# Count = 0
# for i in range(1,11):
#     Count += x
#     x /= 2
#     Count += x
#     print(i, x, Count)

# x = 1

# for i in range(1,11):
#     x = (x+1)*2
#     print(f"{11-i}日目",x)

# x = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         x -= i
#     else:
#         x += i
#     print(i,x)

from random import randint
data = [randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100)]
max_n = data[0]
min_n = data[0]
print(data)
for i in data:
    if i > max_n:
        max_n = i
    elif i < min_n:
        min_n = i
else:
    print(max_n,min_n)