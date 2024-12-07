input_text = open("input.txt", "r").readlines()
rules = [line.strip() for line in input_text]

fin_rules = set(rules[:1176])
updates = rules[1177:]
update_groups = [list(map(int, item.split(','))) for item in updates]

middle_val = 0

for group in update_groups:
    n = len(group)
    fin_update = {f"{group[k]}|{group[i]}" for k in range(n) for i in range(k + 1, n)}
    good_update = all(pair in fin_rules for pair in fin_update)
    if good_update:
        middle_val += group[n // 2]

print(middle_val)