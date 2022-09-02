def Car_Fueling(dist , miles , n , gas_stations):

    num_refill , curr_refill , limit = 0 , 0 , miles

    while limit < dist :
        if curr_refill >= n or gas_stations[curr_refill] > limit :
            return -1

        while curr_refill < n-1 and gas_stations[curr_refill + 1] <= limit :
            curr_refill += 1

        num_refill += 1
        limit = gas_stations[curr_refill] + miles
        curr_refill += 1

    return num_refill

d = int(input())
m = int(input())
n = int(input())
stops = list(map(int,input().split()))
print(Car_Fueling(d , m , n , stops))