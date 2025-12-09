#Part One
#Input has numbers listed horizontally until the last row, with operation symbols listed. Each number or symbol is separated by space
    #The only operations are addition ("+") and multipliccation ("*")
#Each column is an equation, with the operation symbol at the bottom being the operation for each number in the column
#The result is the grant total after adding all the equation results together

#So the first step is to read all of the lines into an array with each being an item in the list
    #Then we want to add spaces to each line so that they are the same width.
    #With that, we can separate problems by columns of blank spaces
#Then we want to read each column into an array
    #If you get to a blank space, break
#Check the last item in each problem
    #Solve each problem, adding it to the grand total sum

# grand_total = 0

# lines = []
# with open("input.txt", "r") as input:
#     for line in input:
#         lines.append(line.rstrip("\n"))

# width = 0
# for line in lines:
#     if len(line) > width:
#         width = len(line)
# for i in range(len(lines)):
#     lines[i] = lines[i].ljust(width)


# equations = []
# current_equation = []
# column = 0

# while column < width:
#     column_chars = []
#     row = 0
#     while row < len(lines):
#         column_chars.append(lines[row][column])
#         row += 1
#     blank_column = True
#     for ch in column_chars:
#         if ch != " ":
#             blank_column = False
#             break

#     if blank_column:
#         if current_equation:
#             equations.append(current_equation)
#             current_equation = []
#     else:
#         current_equation.append(column_chars)
#     column += 1

# if current_equation:
#     equations.append(current_equation)

# for equation in equations:
#     rebuilt_rows = []
#     row_num = 0
#     while row_num < len(lines):
#         row_string = ""
#         col_num = 0
#         while col_num < len(equation):
#             row_string += equation[col_num][row_num]
#             col_num += 1
#         if row_string.strip() != "":
#             rebuilt_rows.append(row_string)
#         row_num += 1
#     operation = rebuilt_rows[-1].strip()

#     numbers = []
#     i = 0
#     while i < len(rebuilt_rows) - 1:
#         num = int(rebuilt_rows[i].strip())
#         numbers.append(num)
#         i += 1
#     if operation == '+':
#         result = 0
#         for n in numbers:
#             result += n
#     else:
#         result = 1
#         for n in numbers:
#             result *= n
#     grand_total += result
    

# print(grand_total)


#Part Two
#The numbers are read differently than part one: 
    #Each column is a single number, read top-down, right to left
        # So in part one the bottom leftmost problm was read as: 123 * 45 * 6
        # In part two, it is read as 356 * 24 * 1

        # 123 328  51 64 
        # 45 64  387 23 
        # 6 98  215 314
        # *   +   *   +  
#The operator logic stays the same, the spacing for the column/row width can stay the same, splitting the columns by the blank columns can stay the same, and the grand total sum can stay the same
#So, the main thing I need to change is how the number(s) are read into the equation

grand_total = 0

lines = []
with open("input.txt", "r") as f:
    for line in f:
        lines.append(line.rstrip("\n"))

width = 0
for line in lines:
    if len(line) > width:
        width = len(line)

for i in range(len(lines)):
    lines[i] = lines[i].ljust(width)

equations = []
current_equation = []
column = 0

while column < width:
    column_chars = []
    row = 0
    while row < len(lines):
        column_chars.append(lines[row][column])
        row += 1

    blank_column = True
    for ch in column_chars:
        if ch != " ":
            blank_column = False
            break

    if blank_column:
        if current_equation:
            equations.append(current_equation)
            current_equation = []
    else:
        current_equation.append(column_chars)

    column += 1

if current_equation:
    equations.append(current_equation)

for equation in equations:
    numbers = []
    for col_index in range(len(equation)-1, -1, -1):
        column = equation[col_index]
        num_str = ""
        for row_index in range(len(column)-1):
            if column[row_index] != " ":
                num_str += column[row_index]
        if num_str != "":
            numbers.append(int(num_str))

    operation = equation[0][-1].strip()

    if operation == '+':
        result = 0
        for n in numbers:
            result += n
    else:
        result = 1
        for n in numbers:
            result *= n

    grand_total += result

print(grand_total)
