number = [4,2,3,1]
def replace_last(number):
    if len(number) <= 1:
        return number
    else:
        number.insert(0, number.pop())
        return number

new_number = replace_last(number)
print (new_number)
