# 数字を当てるゲーム

import random

NUM = random.randint(1,100)  # 1~100 間の乱数を生成
print("1~100 から数字を当てるゲーム ! 合計 7 回のチャンス ! ") # ゲームルール説明
# print(NUM)

for a in range(7):
    NUM_GUESS = input("1~100 から数字を当ててください ! ")
    if NUM_GUESS.isdigit() == False:
        print("1~100 間の数字のみ入力可能 ! 残り" + str(6-a) + "回のチャンス ! ")
    else:
        if NUM == int(NUM_GUESS):
            print("当たり ! おめでとうございます ! ")
            break
        elif a == 6:
            print("チャンスもう残ってない !  Game Over !")
            break
        else:
            if NUM < int(NUM_GUESS):
                print("大きい ! 残り" + str(6-a) + "回のチャンス ! ")
            elif NUM > int(NUM_GUESS):
                print("小さい ! 残り" + str(6-a) + "回のチャンス ! ")