def setOps(list1: list, list2: list):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    reunion = set1.union(set2)
    adiffb = set1.difference(set2)
    bdiffa = set2.difference(set1)

    return (intersection, reunion, adiffb, bdiffa)


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]

print(setOps(l1, l2))