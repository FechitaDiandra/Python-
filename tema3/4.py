def ex4(a, b, startingNotePosition):
    song = [a[startingNotePosition]]
    position = startingNotePosition

    for i in range(len(b)):
        position += b[i]
        if position >= len(a) or position < 0:
            position = position % len(a)
        song.append(a[position])

    return song

print("ex4:\n", ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2), "\n")
