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
    
    number_after.setdefault(key, []).append(value)
    number_after.setdefault(value, [])
    
    number_before.setdefault(key, [])
    number_before.setdefault(value, []).append(key)

sum = 0
# for each update
for u in updates:
    u = u.split(',')
    middle_element = get_middle_element(u)
    # split the update for each number
    for i in range(len(u)):
        u_numbers_before = [u[:i]][0]
        u_numbers_after = [u[i+1:]][0]
        number = u[i]

        valid_before = set(u_numbers_before).issubset(number_before[number])
        valid_after = set(u_numbers_after).issubset(number_after[number])

        if not valid_before or not valid_after:
            middle_element = 0
            break

    sum += int(middle_element)

print(sum)