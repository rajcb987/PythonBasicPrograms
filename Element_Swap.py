#Swap first and last no in a list


def elementSwap(newList):
    size = len(newList)
    
    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp
    
    return newList
    

newList = [15 , 35 , 23 , 56 , 66 , 34]

print(elementSwap(newList))
