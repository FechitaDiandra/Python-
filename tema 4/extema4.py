# ex1:
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

# ex2:
def getDictOfString(string):
    to_return = dict()
    for i in string:
        to_return[i] = to_return.get(i, 0) + 1
    return to_return

# ex3:
def recursive_compare(ct1, ct2):
    if isinstance(ct1, dict) and isinstance(ct2, dict):  # dictionaries
        if len(ct1) != len(ct2):
            return False

        for key, value in ct1.items():
            if not recursive_compare(value, ct2.get(key)):
                return False
        return True

    elif isinstance(ct1, type(ct2)):  # now checking if the args have the same type
        if isinstance(ct1, list) or isinstance(
            ct1, set
        ):  # basic containers: list and set
            if len(ct1) != len(ct2):
                return False

            for i, j in zip(ct1, ct2):  # basic containers: tuple
                if not recursive_compare(i, j):
                    return False

            return True

        elif isinstance(ct1, tuple):
            return recursive_compare(ct1[0], ct2[0]) and recursive_compare(
                ct1[1], ct1[1]
            )

        elif ct1 == ct2:  # basic types
            return True

    return False

# ex4:
def build_xml_element(tag, content, **attributes):
    to_return = "<" + tag

    for key, value in attributes.items():
        to_return += " "
        to_return += key
        to_return += '=\\"'
        to_return += value
        to_return += '\\"'

    to_return += "> "
    to_return += content
    to_return += " </" + tag + ">"

    return to_return

# ex5:
def validate_dict(rules, d):
    for key, value in d.items():
        rule_not_found_flag = True

        for rule in rules:
            if key == rule[0]:
                prefix_pos = value.find(rule[1])

                if prefix_pos != 0:
                    return False
                mid_pos = value.find(rule[2], prefix_pos + 1)
                suffix_pos = value.rfind(rule[3])
                if suffix_pos != len(value) - len(rule[3]):
                    return False
                if mid_pos == -1 or mid_pos > suffix_pos:
                    return False
                
                rule_not_found_flag = False

        if(rule_not_found_flag):
            return False
        
    return True

# ex6:
def get_list_stats(list):
    unique_elements = set(list)
    return (len(unique_elements), len(list) - len(unique_elements))

# ex7:
def get_dict_of_set_ops(*sets):
    to_return = dict()
    for i in range(0,len(sets)):
        for j in range(i+1,len(sets)):
            to_return[str(sets[i]) + " | " + str(sets[j])] = sets[i].union(sets[j])
            to_return[str(sets[i]) + " & " + str(sets[j])] = sets[i].intersection(sets[j])
            to_return[str(sets[i]) + " - " + str(sets[j])] = sets[i].difference(sets[j])
            to_return[str(sets[j]) + " - " + str(sets[i])] = sets[j].difference(sets[i])

    return to_return

# ex8:
def loop(mapping):
    to_return = list()
    current_key = mapping["start"]
    
    while current_key != "start":
        to_return.append(current_key)
        current_key = mapping[current_key]
        if current_key in to_return:
            break
    
    return to_return

# ex9:
def my_function(*positional_args, **keyword_args):
    keyword_values = [value for key,value in keyword_args.items()]
    return len([i for i in positional_args if i in keyword_values])

print("ex1:", setOps(l1, l2))
print("ex2:", getDictOfString("Ana has apples."))
print("ex3 - basic:", recursive_compare("aaa", "aaa"))

print("ex3 - simple1:", recursive_compare({"a": "dd", 3: 5}, {"a": "dd", 3: 5}))
print("ex3 - simple2:", recursive_compare({"a": "dd", 3: 5}, {"a": "dd", 3: 6}))

print("ex3 - medium1:", recursive_compare({"a": [1, 2], 3: {1, 2}}, {"a": [1, 2], 3: {1, 2}}))
print("ex3 - medium2:", recursive_compare({"a": [1, 2], 3: {1, 2}}, {"a": [1, 2], 3: {1, 4}}))

print(
    "ex3 - hard1:",
    recursive_compare(
        [
            {"a": [1, 2], 3: {1, 2}},
            {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
            [{3, 4, 5, 6}, {"a": "b", "c": 55}],
        ],
        [
            {"a": [1, 2], 3: {1, 2}},
            {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
            [{3, 4, 5, 6}, {"a": "b", "c": 55}],
        ],
    ),
)
print(
    "ex3 - hard2:",
    recursive_compare(
        [
            {"a": [1, 2], 3: {1, 2}},
            {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
            [{3, 4, 5, 6}, {"a": "b", "c": 55}],
        ],
        [
            {"a": [1, 2], 3: {1, 2}},
            {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
            [{3, 4, 5, 6}, {"a": "b", "c": 53}],
        ],
    ),
)

print(
    "ex3 - harerest:",
    recursive_compare(
        {
            "a": [
                {"a": [1, 2], 3: {1, 2}},
                {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
                [{3, 4, 5, 6}, {"a": "b", "c": 55}],
            ],
            "b": [
                {"a": [1, 2], 3: {1, 2}},
                {"a": [1, 2], 3: [{1, 4}, {"inside": "this"}]},
                [{3, 4, 5, 6}, {"a": "b", "c": 55}],
            ],
        },
        {
            "a": [
                {"a": [1, 2], 3: {1, 2}},
                {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
                [{3, 4, 5, 6}, {"a": "b", "c": 55}],
            ],
            "b": [
                {"a": [1, 2], 3: {1, 2}},
                {"a": [1, 2], 3: [{1, 4}, {"inside": "this"}]},
                [{3, 4, 5, 6}, {"a": "b", "c": 55}],
            ],
        },
    ),
)
print(
    "ex4:",
    build_xml_element(
        "a",
        "Hello there",
        href=" http://python.org ",
        _class=" my-link ",
        id=" someid ",
    )
)
print("ex5 - rule not found: ",
    validate_dict(
        {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
        {"key1": "come inside, it's too cold out", "key3": "this is not valid"},
    )
)
print("ex5 - rule found + valid dict: ",
    validate_dict(
        {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
        { "key1": "come inside, it's too cold out","key2": "start this middle in the winter"},
    )
)
print("ex5 - rule found + invalid dict: ",
    validate_dict(
        {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
        { "key1": "come inside, it's too cold out", "key2": "start this middle not in the winter"},
    )
)

print("ex6:", get_list_stats([1, 2, 3, 4, 4, 5, 5, 5]))
print("ex7:", get_dict_of_set_ops({1, 2, 3}, {2, 3, 4}, {3, 4, 5}))
print("ex8:", loop({"start": "a", "a": "b", "b": "start"}))
print("ex9:", my_function(1, 2, 3, a=2, b=3))
