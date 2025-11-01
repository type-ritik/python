def sumofN(num):
    if num <= 0:
        return 0
    return num + sumofN(num - 1)


num = 5
print(sumofN(num))


def sumofNum(num):
    sum = 0
    for i in range(num):
        sum += pairSum(i, i + 1)
    return sum


def pairSum(a, b):
    return a + b


num = 5
print(sumofNum(num))


def min_max():
    min = -90000
    mix = 90000
