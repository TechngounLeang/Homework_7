array = [4,2,3,1]
def replace_last(list_1):
    if len(list_1) <= 1:
        return list_1
    else:
        list_1.insert(0, list_1.pop())
        return list_1

new_list = replace_last(array)
print (new_list)
