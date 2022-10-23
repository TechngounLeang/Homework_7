array = [1, 2, 3, 4]
border_element = 3

def index_power(array, border_element):
    if N >= len(array):
        return -1
    else:
        return array[border_element] ** border_element

power = index_power(array, border_element)
print (power)
