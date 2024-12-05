input_text = open("input.txt", "r").readlines()
reports = [line.split() for line in input_text]

safe = 0
true_rep = False

for i in reports:
    if i == sorted(i) or i == sorted(i, reverse=True):
        for n in range(0, len(i) - 1):
            if int(i[n]) != int(i[n + 1]) and abs(int(i[n]) - int(i[n + 1])) in {1,2,3}:
                true_rep = True
            else:
                true_rep = False
                break
    if true_rep == True:
        safe += 1

print(safe)
