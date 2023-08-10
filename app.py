with open("input.txt", "rt", encoding="utf-8") as input_file:
    for line in input_file:
        words = line.split()
        for word in words:
            output = f"{word}, "
            print(output, end="")