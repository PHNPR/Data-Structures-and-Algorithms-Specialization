def signatures(arr) :
    arr = sorted(arr , key = lambda x : x[1])
    start , count , i , ans = arr[0][1] , 1 , 0 , [arr[0][1]]
    while i < len(arr) :
        if arr[i][0] <= start <= arr[i][1] :
            i += 1
        else :
            start = arr[i][1]
            count += 1 
            ans.append(start)
    return count , ans  

points = []
for _ in range(int(input())):
    points.append(list(map(int,input().split())))
    count , dots = signatures(points)
print(count)
print(*dots)
