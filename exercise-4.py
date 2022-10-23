array = [1, 2, 3, 4, 5, 6]
N = 2

def chunking_by(array, N):
    if len(array) == 0:
        return array
    else:
        chunk = list()
        for i in range (0, len(array), N):
            chunk.append(array[i: i+N])
        return chunk

new = chunking_by(array, N)
print(new)