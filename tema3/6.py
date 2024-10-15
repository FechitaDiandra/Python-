def ex6(x, *lists):
    all_lists = []
    result = []
    
    for i in lists:
        all_lists += i
    
    for lst in all_lists:
        if all_lists.count(lst) == x and lst not in result:
            result.append(lst)
    
    return result  

print("ex6:\n", ex6(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]), "\n")
