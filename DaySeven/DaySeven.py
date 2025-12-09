#Part One
#Given an input file with many lines, and three different characters; S, ., and ^. 
    # A beam starts at S on line 0, and continues downward.
    #The beam moves freely downward one space if there is a .
    # If it touches a ^, it splits downards into two lines, one to the left and one to the right of the ^
#Need to return the total number of times the beam splits

#I'll need the starting coordinate for S (middle of the starting line?)
#I'll need a grid with width (num of ch in line) and height (num of lines in input)
    # and an array with the list of active beams with their coordinates
    #Also a total count of splits for the result

# 1) Read input
# 2) Find num of ch in a line (width of grid)
# 3) Find num of rows in input (height of grid)
# 4) Locate starting S coordinate
# 5) Move the beam downward row by row
# 6) Check if beam hits empty space (.) or a splitter (^)
    # 6a) simulate beam moving down, simulate new beam if splitter, and increase split count for result
# 7) Stop when beams reach the height of the grid (0 or grid height)
# 8) Return total split count

# lines = []
# split_count = 0

# with open("input.txt", "r") as input:
#     for line in input:
#         lines.append(line.rstrip('\n'))
# width = len(lines[0])
# height = len(lines)

# x = 0
# for ch in lines[0]:
#     if ch == "S":
#         start_col = x
#         break
#     x += 1

# active_beam_coords = [(start_col, 0)]

# while active_beam_coords:
#     next_row_beams = []
#     for (col, row) in active_beam_coords:
#         next_row = row + 1
#         if next_row == height:
#             continue
#         cell = lines[next_row][col]
#         if cell == "^":
#             split_count += 1
#             if col - 1 > 0 :
#                 next_row_beams.append((col-1, next_row))
#             if col + 1 < width:
#                 next_row_beams.append((col+1, next_row))
#         elif cell == ".":
#             next_row_beams.append((col, next_row))
#     active_beam_coords = list(set(next_row_beams))

# print(split_count)


#Part Two
#Instead of counting the number of splits a beam takes, we need to count the number of alternate pathways a beam can take getting from S to the height
#So we can't merge beams like before in part one, because each one has a different path we need to count
#According to Reddit, Memoization is useful here. Research into.
    #Use recursive memoization
    #Basically, recursive depth first search algorithms
#We should be able to get rid of the active beam arrays and use a memo dictionary instead
    #Most of the code should stay relatively similar
    #We will need a function here so we can call it recursively


lines = []
total_timelines = 0

with open("input.txt", "r") as input:
    for line in input:
        lines.append(line.rstrip('\n'))
width = len(lines[0])
height = len(lines)

x = 0
for ch in lines[0]:
    if ch == "S":
        start_col = x
        break
    x += 1

memo = {}

def count_timelines(col, row):
    if row >= height:
        return 1 

    if (col, row) in memo:
        return memo[(col, row)]

    cell = lines[row][col]

    if cell == ".":
        result = count_timelines(col, row + 1)
    elif cell == "^":
        result = 0
        if col - 1 >= 0:
            result += count_timelines(col - 1, row + 1)
        if col + 1 < width:
            result += count_timelines(col + 1, row + 1)

    memo[(col, row)] = result
    return result

total_timelines = count_timelines(start_col, 1)
print(total_timelines)