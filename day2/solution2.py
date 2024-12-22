input_text = open("input.txt", "r").readlines()
reports = [line.split() for line in input_text]

safe_rep = 0
unsafe_rep = []


def safe_check(report):
    report = list(map(int, report))
    if report == sorted(report) or report == sorted(report, reverse=True):
        for n in range(0, len(report) - 1):
            if int(report[n]) != int(report[n + 1]) and abs(
                int(report[n]) - int(report[n + 1])
            ) in {1, 2, 3}:
                continue
            else:
                return False
        return True
    return False


for i in reports:
    if safe_check(i):
        safe_rep += 1
    else:
        unsafe_rep.append(i)


for k in unsafe_rep:
    original_rep = k.copy()
    for m in range(len(original_rep)):
        cutted_rep = original_rep[:m] + original_rep[m + 1 :]
        if safe_check(cutted_rep):
            safe_rep += 1
            break
print("Second part:", safe_rep)
