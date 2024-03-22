def write(filename, data):
    with open(filename, 'w') as file:
        for measurement in data:
            file.write(f"{measurement[0]}\t{measurement[1]}\n")

filename = "1.txt"
data = [(1, 20),(2, 30),(3, 40),(4, 35),(5, 22),(6, 10)]
write(filename, data)