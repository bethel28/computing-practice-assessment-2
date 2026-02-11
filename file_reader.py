def read_numbers():
    with open("numbers.txt", "r") as f:
        numbers = f.readlines()
    return [int(n.strip()) for n in numbers]
