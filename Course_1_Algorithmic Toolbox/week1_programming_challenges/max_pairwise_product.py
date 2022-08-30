_ = int(input())
a = list(map(int, input().split()))
a.sort()
print(max(a[-1]*a[-2] , a[0]*a[1]))

def fib(n):
    f = [0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    print(f[n])