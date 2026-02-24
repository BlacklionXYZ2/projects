
i = [2, 3, 4, 5, 6, 7]

data = {
}

def find(find, obj):
    layer = 1
    for x in find:
        store = [x]
        obj.update({f'layer{layer}': store})
        layer += 1

find(i, data)
print(data)
