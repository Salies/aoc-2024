file = open("data/5.txt", "r")
input = file.read()

rules_block, updates_block = input.split('\n\n')
rules_block, updates_block = rules_block.strip(), updates_block.strip()

rules = rules_block.split('\n')
updates = updates_block.split('\n')

def get_middle_element(array):
    return array[len(array) // 2]

number_before = {}
number_after = {}

for rule in rules:
    key, value = rule.split('|')
    key, value = int(key), int(value)

    number_after.setdefault(key, []).append(value)
    number_after.setdefault(value, [])
    
    number_before.setdefault(key, [])
    number_before.setdefault(value, []).append(key)

sum = 0
for u in updates:
    u = [int(page) for page in u.split(",")]

    for i, number in enumerate(u):
        u_numbers_before = set(u[:i])
        u_numbers_after = set(u[i+1:])

        valid_before = set(u_numbers_before).issubset(number_before[number])
        valid_after = set(u_numbers_after).issubset(number_after[number])

        if not valid_before or not valid_after:
            sorted_u = sorted(u, key=lambda x: (
                len(set(number_before[x]) & set(u)), 
                -len(set(number_after[x]) & set(u))
            ))
            middle_element = get_middle_element(sorted_u)
            sum += middle_element
            break

print(sum)