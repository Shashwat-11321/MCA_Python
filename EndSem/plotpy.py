import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, color='red', marker='o', linestyle='--', linewidth=2)
plt.title("Customized Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)  # Adds a grid
plt.show()





