input_text = open("input.txt", "r").readlines()

list1 = sorted(int(line.split()[0]) for line in input_text)
list2 = sorted(int(line.split()[1]) for line in input_text)

distance = sum(abs(k - n) for k, n in zip(list1, list2))

print(distance)
