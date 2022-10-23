array = [1, 2, 3, 4]
num = 2

def index_power(list_1, number):
    if number >= len(list_1):
        return -1
    else:
        return list_1[number] ** number

power = index_power(array, num)
print (power)
