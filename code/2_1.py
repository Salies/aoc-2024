file = open("data/2.txt", "r")
lines = file.readlines()

safe_count = 0
for line in lines:
    numbers = [int(x) for x in line.split()]
    
    mi, ma = 1, 3
    # detect direction of the numbers (decreasing or increasing)
    if numbers[0] < numbers[1]:
        mi, ma = -1 * ma, -1 * mi

    safe_count += 1
    for i in range(len(numbers) - 1):
        if (numbers[i] - numbers[i + 1]) < mi or (numbers[i] - numbers[i + 1]) > ma:
            safe_count -= 1
            break
        
print(safe_count)