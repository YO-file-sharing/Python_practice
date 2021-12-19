# 数字を当てるゲーム

import random
import sys

NUM = random.randint(1,100)  # 1~100 間の乱数を生成
print("【百以内の数字を当てるゲーム 】 合計 7 回のチャンス ! ") # ゲームルール説明
# print(NUM) # テスト用

for a in range(7):
    NUM_GUESS = input("1~100 から数字を当てて見てください ! \n")
    if a == 6 and NUM != int(NUM_GUESS):
        print("もうチャンス残ってない !  \nGame Over ! \n答えは : \"" + str(NUM) + "\" ! ")
        break
    else:
        if NUM_GUESS.isdigit() == False :
            print("入力エラー !!! 残り" + str(6-a) + "回のチャンス ! \n")
        elif NUM_GUESS.isdigit() == True:
            if 1 <= int(NUM_GUESS) and int(NUM_GUESS) <= 100:
                if NUM == int(NUM_GUESS):
                    print("\n当たり ! おめでとうございます ! \n")
                    break
                else:
                    if NUM < int(NUM_GUESS):
                        print("大きい ! 残り" + str(6-a) + "回のチャンス ! \n")
                    elif NUM > int(NUM_GUESS):
                        print("小さい ! 残り" + str(6-a) + "回のチャンス ! \n")
            else:
                print("入力エラー !!! 残り" + str(6-a) + "回のチャンス ! \n")

quit = input("終了するには何かのキーを押してください。")
if quit == True:
    sys.exit(0)