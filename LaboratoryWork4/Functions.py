def myMap(func, oldList):
    newList = []
    for item in oldList:
        newList.append(func(item))
    return newList


def myReduce(func, oldList):  
    result = func(oldList[0], oldList[1])
    for i in oldList[2:]:
        result = func(result, i)
    return result


if __name__ == "__main__":
    print(myMap(lambda x: x * 2 + 3, [10, 15, 21, 33, 42, 55]))
    print(myReduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))