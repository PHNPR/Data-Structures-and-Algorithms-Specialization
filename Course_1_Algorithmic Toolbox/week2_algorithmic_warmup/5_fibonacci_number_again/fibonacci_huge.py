def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    a = [0, 1]
    time_period = 1
    for i in range(2 , n + 1):
        a.append( (a[i-1] + a[i-2]) % m )
        if a[i-1] == 0 and a[i] == 1 :
            time_period = i - 1
            break
    if time_period > 1 : 
        n = n % time_period
    return a[n]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))