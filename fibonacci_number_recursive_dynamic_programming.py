import time
import sys
import matplotlib.pyplot as plt

# 純遞歸方法
def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# 動態規劃方法
def fibonacci_dynamic(n):
    if n == 0 or n == 1:
        return n
    dp = [None for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
      dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 測量兩種方法的執行時間
x = list(range(10, 101, 10))
recursive_time = []
dynamic_time = []

for n in x:
#for n in range(2,10):
    start_time = time.time()
    fibonacci_recursive(n)
    end_time = time.time()
    recursive_time.append(end_time - start_time)

    start_time = time.time()
    fibonacci_dynamic(n)
    end_time = time.time()
    dynamic_time.append(end_time - start_time)

# 繪製折線圖
plt.plot(x, recursive_time, label="Recursive")
plt.plot(x, dynamic_time, label="Dynamic Programming")
plt.xlabel("n")
plt.ylabel("Execution Time (s)")
plt.legend()
plt.show()

# 尋找導致遞歸方法崩潰的 n 值
max_n = 0
while True:
    try:
        sys.setrecursionlimit(3000)
        fibonacci_recursive(max_n + 1)
        max_n += 1
    except RecursionError:
        break

# 使用動態規劃方法確定是否會崩潰
try:
    sys.setrecursionlimit(3000)
    fibonacci_dynamic(max_n + 1)
    print(f"Dynamic programming does not crash for n = {max_n + 1}")
except RecursionError:
    print(f"Dynamic programming crashes for n = {max_n + 1}")
