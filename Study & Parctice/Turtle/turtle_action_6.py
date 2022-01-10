import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname = r"C:\Windows\Fonts\UDDigiKyokashoN-R.ttc", size = 12)
x = np.linspace(start=0, stop=np.pi*2, num=30)
ys , yc = np.cos(x), np.sin(x)

plt.figure(1)
# plt.subplot(221)

# plt.plot(x, ys, ".", color="blue")
# plt.plot(x, yc, ".", color="green")

# plt.subplot(222)
# plt.plot(x, ys, color="blue")
# plt.plot(x, yc, color="red")

# plt.subplot(223)
# plt.plot(x, ys, marker="o", color="blue", linestyle="--")
# plt.plot(x, yc, marker="o", color="red", linestyle="--")

plt.subplot(111)
plt.plot(x, ys)
plt.plot(x, yc)
plt.xlabel("座標軸 X", FontProperties = font)
plt.ylabel("座標軸 y", FontProperties = font)
plt.title("cos & sin", FontProperties = font)

plt.show()