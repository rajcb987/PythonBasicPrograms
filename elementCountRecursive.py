def count_elements(newList):
    
    if not newList:
        return 0
    else:
        return 1 + count_elements(newList[1:])


newList = [15 , 35 , 23 , 56 , 66 , 34]

print("Length of the list is : ",count_elements(newList))
    
