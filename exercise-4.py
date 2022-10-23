list_1 = [1, 2, 3, 4, 5, 6]
chunk_size = 2

def chunking_by(array, size):
    if len(array) == 0:
        return array
    else:
        chunked = list()
        for i in range (0, len(array), size):
            chunked.append(array[i: i+size])
        return chunked

new_list = chunking_by(list_1, chunk_size)
print(new_list)
