# 数字を当てるゲーム

import random
import sys

NUM = random.randint(1,100)  # 1~100 間の乱数を生成
print("【百以内の数字を当てるゲーム 】 合計 7 回のチャンス ! ") # ゲームルール説明
# print(NUM) # テスト用

for a in range(7): # チャンスを 7 回に設定
    NUM_GUESS = input("1~100 から数字を当てて見てください ! \n") 
    if a == 6 and NUM != int(NUM_GUESS): # Game over 条件を定義
        print("もうチャンス残ってない !  \nGame Over ! \n答えは : \"" + str(NUM) + "\" ! ")
        break
    else:
        if NUM_GUESS.isdigit() == False : # 数字以外入力した場合のエラー条件定義
            print("入力エラー !!! 残り" + str(6-a) + "回のチャンス ! \n")
        elif NUM_GUESS.isdigit() == True: # 数字を入力した場合、正常に進む
            if 1 <= int(NUM_GUESS) and int(NUM_GUESS) <= 100:　# 入力した数字が条件範囲内、進む
                if NUM == int(NUM_GUESS): # 当たり条件
                    print("\n当たり ! おめでとうございます ! \n")
                    break
                else:
                    if NUM < int(NUM_GUESS): # 大きい場合
                        print("大きい ! 残り" + str(6-a) + "回のチャンス ! \n")
                    elif NUM > int(NUM_GUESS): # 小さい場合
                        print("小さい ! 残り" + str(6-a) + "回のチャンス ! \n")
            else: # 入力した数字が範囲外の場合のエラー条件定義
                print("入力エラー !!! 残り" + str(6-a) + "回のチャンス ! \n")

# 終了方法定義
quit = input("終了するには何かのキーを押してください。")
if quit == True:
    sys.exit(0)
