## 吃桃子问题
# 1 元可以买 1 个桃子
# 3 个桃核可以换 1 个桃子
# 最多可以吃几个桃子

Peach_Eated = 10
Peach_Pit_Remain = 10
Peach_Pit_Used = 0
i = 0

while True:
    i += 1
    print(i,end =" ")
    if Peach_Pit_Remain // 3 != 0:
        Peach_Eated += (Peach_Pit_Remain // 3)
        Peach_Pit_Used = 3 * (Peach_Pit_Remain // 3)
        Peach_Pit_Remain = Peach_Pit_Remain - Peach_Pit_Used + (Peach_Pit_Used//3)
    elif (Peach_Pit_Remain + 1) // 3 == 1:
        Peach_Eated += 1
        Peach_Pit_Used = 3
        Peach_Pit_Remain = 0
    else:
        break
print()
print(Peach_Eated,Peach_Pit_Remain)