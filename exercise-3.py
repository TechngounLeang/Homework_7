
def remove_all_after(list, N):
    if N not in list:
        return list
    else:
        daval = list.index(N)
        new = list[:daval + 1]
        return new

newlist = remove_all_after([1,2,3,5,4,6], 3)
print(newlist)
