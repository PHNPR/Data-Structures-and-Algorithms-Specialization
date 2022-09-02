def change(money):
    # write your code here
    money = (money // 10) + (money % 10) // 5 + (money % 5)
    return money


if __name__ == '__main__':
    m = int(input())
    print(change(m))