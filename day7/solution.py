input_text = open("input.txt", "r").readlines()
rules = [line.strip() for line in input_text]

total_sum = 0


def can_form_result(nums, target):
    results = {nums[0] + nums[1], nums[0] * nums[1]}

    for i in range(2, len(nums)):
        next_results = set()
        for result in results:
            next_results.add(result + nums[i])
            next_results.add(result * nums[i])
        results = next_results
    return target in results


for rule in rules:
    res = int(rule.split(":")[0])
    nums = list(map(int, rule.split(":")[1].strip().split()))
    if can_form_result(nums, res):
        total_sum += res

print("total_sum", total_sum)
