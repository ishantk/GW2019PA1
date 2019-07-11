import time

def power(num, N):

    i = 1                           # 1 Time Step
    result = 1                      # 1 Time Step
    while i<=N:
        result = result * num       # 1 Time Step
        i += 1                      # 1 Time Step

    print(">> Power of",num,"is",result)    # 1 Time Step

    # 3 + 2N + (N+1) -> 3N + 4
    # timeComplexity -> 3N + 4 -> Order of N O(N)

stamp1 = time.time()

power(5, 3)

stamp2 = time.time()

print(stamp2-stamp1)