# factorial function
def fac(n):
    if(n == 0 or n == 1):
        return 1
    return n*fac(n-1)


# Memoization
def facdp(n, dp):
    if(n == 0 or n == 1):
        return 1

    if(dp[n] != -1):
        return dp[n]

    dp[n] = n*facdp(n-1, dp)

    return dp[n]


n = int(input("Enter the value of n:"))

dp = []
for i in range(n+1):
    dp.append(-1)

print(facdp(n, dp))
print(fac(5))


# fibonacci number
def fib(n):
    if(n == 0 or n == 1):
        return n

    return fib(n-1)+fib(n-2)


print(fib(6))
