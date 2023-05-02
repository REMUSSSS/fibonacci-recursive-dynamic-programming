'''
GPT4
你是一名資深演算法老師，請翻譯以下題目並解答，並輸出程式碼(加註解)

During our class, we discussed how to calculate the n-th Fibonacci Number, denoted as F(n), using pure recursive and dynamic programming methods. For this exercise, please complete the following tasks:

Write code to measure the execution time of F(10), F(20), ..., F(100) using both pure recursive and dynamic programming methods. Plot the results as a line chart.
Write code to determine the maximum value of n such that computing F(n+1) recursively causes your computer to crash. Then, using dynamic programming to compute F(n+1), determine whether your computer will still crash or not.

首先，我將翻譯題目並提供解答。題目翻譯如下：

在課堂上，我們討論了如何使用純遞歸和動態規劃方法計算第 n 個斐波那契數，表示為 F(n)。對於此練習，請完成以下任務：

編寫代碼以測量使用純遞歸和動態規劃方法計算 F(10)、F(20) ... F(100) 的執行時間。將結果繪製為折線圖。
編寫代碼以確定 n 的最大值，使得遞歸計算 F(n+1) 會導致您的計算機崩潰。然後，使用動態規劃計算 F(n+1)，確定您的計算機是否仍然會崩潰。
'''

'''
以上代码首先测量了純遞歸方法和動態規劃方法计算斐波那契数的执行时间，并将结果绘制成折线图。然后，代码找到了使递归方法崩溃的最大 n 值，并尝试使用动态规划方法计算 F(n+1)。
'''
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

# def fibonacci_dynamic(n, memo={}):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n not in memo:
#         memo[n] = fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2)
#     return memo[n]

# 測量兩種方法的執行時間
'''x = list(range(10, 101, 10))
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
plt.show()'''

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