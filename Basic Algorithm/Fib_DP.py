#######Recursive Way###########

def fib1(n):
    if n <= 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

######## Memorized DP###########

def fib2(n,mem):
    if n in mem:
        return mem[n]
    if n <= 2:
        return 1
    else:
        f = fib2(n-1, mem) + fib2(n-2, mem)
        mem[n] = f
        return f

########  Bottom Up DP ################
##### EXACTLY SAME COMPUTATION AS Memo DP############
##### SAVE SPACE#################
def fib3(n):
    fib = {}
    for i in range(1, n+1):
        if i <= 2:
            fib[i] = 1
        else:
            fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

######################################
print fib1(10)
print fib2(10,{})
print fib3(10)

