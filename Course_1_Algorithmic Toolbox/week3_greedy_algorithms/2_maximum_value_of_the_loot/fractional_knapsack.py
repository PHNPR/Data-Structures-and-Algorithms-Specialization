n , capacity = map(int,input().split())
val_cap = []
for _ in range(n):
    val_cap.append(list(map(int,input().split()))) 
val_cap.sort(key= lambda x : x[0] / x[1] , reverse= True) 
value = 0
for i in val_cap :
    if capacity >= i[1]:
        capacity -= i[1]
        value += i[0]
    else :
        value += ( i[0] / i[1] ) * capacity
        break
print("{:.4f}".format(value))