file = open("data/2.txt", "r")
lines = file.readlines()

def check_safety(numbers):
    mi, ma = 1, 3
    # detect direction of the numbers (decreasing or increasing)
    if numbers[0] < numbers[1]:
        mi, ma = -1 * ma, -1 * mi

    safe = True
    for i in range(len(numbers) - 1):
        if (numbers[i] - numbers[i + 1]) < mi or (numbers[i] - numbers[i + 1]) > ma:
            safe = False
            break

    return safe

safe_count = 0
for line in lines:
    numbers = [int(x) for x in line.split()]
    
    is_safe = check_safety(numbers)

    if is_safe:
        safe_count += 1
        continue

    # brute force: try removing each number and check if the sequence is safe
    for i in range(len(numbers)):
        new_numbers = numbers[:i] + numbers[i + 1:]
        is_safe = check_safety(new_numbers)
        if is_safe:
            safe_count += 1
            break

        
print(safe_count)