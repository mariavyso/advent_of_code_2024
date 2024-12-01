input_text = open("input.txt", "r").readlines()

list1 = [int(line.split()[0]) for line in input_text]
list2 = [int(line.split()[1]) for line in input_text]

similarity_score = sum(i * list2.count(i) for i in list1)

print(similarity_score)
