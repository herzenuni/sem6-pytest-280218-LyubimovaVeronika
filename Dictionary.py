def Dictionary(keys,values):
    res = {}
    border = len(values)

    for i in range(len(keys)):
        if (i >= border):
            res.update({keys[i]: None})
        else:
            res.update({keys[i] : values[i]})

    return res
#print(Dictionary([1,2,3],[321,32,1]))
#print(Dictionary(['а','б'],['б','а']))