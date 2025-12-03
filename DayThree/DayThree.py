#Part One
#Read in input file
    #Line by line because each line is a bank of batteries
#Read each character in each line
    #Test each pair of numbers individually, starting with the first, then pair it with the other numbers in the list. Then go to the next number in the list and test it with each of the numbers after it to find the maximum
#When largest value is found from that line, add it to running some to find the total output joltage
#Return total output joltage (sum of the maximum joltage from each bank)


# Total_Output_Joltage = 0
# Current_Maximum_Joltage = 0

# with open('input.txt', 'r') as input:
#     for line in input.readlines():
#         line = line.strip()
#         for i in range(len(line)):
#             first_value = int(line[i]) * 10
#             print(first_value)
#             for j in range(i+1, len(line)):
#                 second_value = int(line[j])
#                 if first_value + second_value > Current_Maximum_Joltage:
#                     Current_Maximum_Joltage = first_value + second_value
#         Total_Output_Joltage += Current_Maximum_Joltage
#         Current_Maximum_Joltage = 0


# print(Total_Output_Joltage)


#Part Two
#Same problem, but now we can use twelve digits from the battery bank instead of 2
#Can we just for loop it 10 more times? Surely that's not the most efficient?
    #Actually we don't need that many for loops, so the last 11 numbers in the bank won't really matter, so we can just test the bank indexes at (bank.length - 11) and find the largest number there, then the maximum would include the next 11 digits
    #This is called the "greedy" longest common subsequence problem

Total_Output_Joltage = 0

with open('input.txt', 'r') as input:
    for line in input.readlines():
        line = line.strip()
        Current_Maximum_Joltage = []
        first_index = 0
        battery_length = 12

        while len(Current_Maximum_Joltage) < battery_length:
            last_index = len(line) - (battery_length - len(Current_Maximum_Joltage)) + 1
            battery_section = line[first_index:last_index]
            max_digit = max(battery_section)
            best_digit_in_section = battery_section.index(max_digit)
            Current_Maximum_Joltage.append(max_digit)
            first_index += best_digit_in_section + 1
        Total_Output_Joltage += int(''.join(Current_Maximum_Joltage))



print(Total_Output_Joltage)