## 蜗牛爬井问题
# 高 10 米，每天爬 3 米，晚上掉 2 米，求需要几天

W_Up = 3 # 白天爬 3 米
W_Down = 2 # 晚上掉 2 米
W_Day = 1 # 天数
W_Now = 0 # 现在的高度计算
W_Target = 10 # 井口高度

while True:
    W_Now += W_Up # 白天向上爬的米数
    if W_Now >= W_Target: # 达到井口后的条件
        break
    else: # 未达标则前进
        W_Now -= W_Down
    W_Day += 1 # 天数计算器

print(f"到达井口花费了 {W_Day} 天")
