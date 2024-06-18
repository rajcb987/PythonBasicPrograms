def most_frequent(List):
    frequency = {}
    
    for i in List:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
            
    most_frequent_element = max(frequency, key=frequency.get)
    
    return most_frequent_element

List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))
