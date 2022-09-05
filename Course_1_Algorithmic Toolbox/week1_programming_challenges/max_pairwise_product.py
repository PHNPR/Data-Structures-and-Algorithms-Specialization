def max_pairwise_product(a):
    if a[0] > a[1]:
        m1 , m2 = a[0] , a[1]
    else :
        m1 , m2 = a[1] , a[0]
    for i in range(2,len(a)):
        if a[i] >= m1 :
            m1 , m2 = a[i] , m1
        elif m1 > a[i] > m2 :
            m2 = a[i]
    return m1*m2

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))