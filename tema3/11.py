def ex11(lists):
    n = len(lists)

    for i in range(n):
        for j in range(0, n - i - 1):
            if len(lists[j][1]) > 2 and len(lists[j + 1][1]) > 2:
                chr1 = lists[j][1][2]  
                chr2 = lists[j + 1][1][2]
                if ord(chr1) > ord(chr2):
                    
                    lists[j], lists[j + 1] = lists[j + 1], lists[j]

    return lists


print("ex11:\n", ex11([('abc', 'bcd'), ('abc', 'zza'), ('abc', 'yyc')]), "\n")
