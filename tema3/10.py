def ex10(*lists):
    maxNrOfElements = max(len(lst) for lst in lists)
    listOfTuples = []
    
    for i in range(maxNrOfElements):
        currentTuple = ()
        for lst in lists:
            try:
                currentTuple += (lst[i],)  
            except IndexError: 
                currentTuple += (None,) 
        listOfTuples.append(currentTuple)

    return listOfTuples


print("ex10:\n", ex10([1, 2], [5, 6, 7], ["a", "b", "c"]), "\n")
