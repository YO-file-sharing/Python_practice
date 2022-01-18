for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}x{j}={i*j}",end="    ")
    print()
print()
for i in range(1, 101):
    k = 0
    for j in range(1,i+1):
        if i % j == 0:
            k += 1
    if k == 2:
        print(f"{i}は素数だ。")
    else:
        pass

for i in range(11):
    if i <=5 :
        print("* " * i)
    else:
        print("* " * (10-i))

# a = 0
# while True:
#     a += 1
#     print("...",a)