# 数字を当てるゲーム

import random

NUM = random.randint(1,100)  # 1~100 間の乱数を生成
print("1~100 から数字を当てるゲーム ! 合計 7 回のチャンス ! ") # ゲームルール説明
# print(NUM)

for a in range(7):
    NUM_GUESS = input("1~100 から数字を当ててください ! \n")
    if NUM == int(NUM_GUESS):
            print("\n当たり ! おめでとうございます ! \n")
            break
    else:
        if a == 6:
            print("もうチャンス残ってない !  \nGame Over ! \n答えは : \"" + str(NUM) + "\" ! ")
            break
<<<<<<< HEAD
        elif NUM_GUESS.isdigit() == False and 1<= int(NUM_GUESS) <= 100:
            print("入力エラー !!! 残り" + str(6-a) + "回のチャンス ! \n")
=======
        elif NUM_GUESS.isdigit() == False:
            print("数字のみ入力可能 !!! 残り" + str(6-a) + "回のチャンス ! \n")
>>>>>>> main
        else:
            if NUM < int(NUM_GUESS):
                print("大きい ! 残り" + str(6-a) + "回のチャンス ! \n")
            elif NUM > int(NUM_GUESS):
                print("小さい ! 残り" + str(6-a) + "回のチャンス ! \n")