def group_by_rhyme(words):
    rhyme_dict = {}

    for word in words:
        rhyme_key = word[-2:]
        if rhyme_key in rhyme_dict:
            rhyme_dict[rhyme_key].append(word)
        else:
            rhyme_dict[rhyme_key] = [word]

    grouped_rhymes = list(rhyme_dict.values())

    return grouped_rhymes

print("group_by_rhyme:\n", group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']), "\n")
