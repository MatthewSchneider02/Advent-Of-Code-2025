#Part One
#Read input line by line
    #Save each line as string
        #Make a set of coordinates where there are rolls (@)
#Test for adjacent @
    #Position (x,y) tested against (x-1, y), (x, y-1), (x-1, y-1), (x+1, y), (x, y+1), (x+1, y+1), (x+1, y-1), (x-1, y+1)
    #if/when 4 of those have an @, break and don't count (x,y)
    #if less than 4 of those have an @, increase count
#Return count as answer

# count = 0
# adjacent_coords = [(-1, 0), (0, -1), (-1, -1), (1, 0), (0, +1), (1, 1), (1, -1), (-1, 1)]

# rolls = set()


# with open('input.txt', 'r') as input:
#     for r, line in enumerate(input):
#             for c, ch in enumerate(line):
#                 if ch == '@':
#                      rolls.add((r,c))

# for (r, c) in rolls:
#     adjacent_roll_count = 0

#     for adj_r, adj_c in adjacent_coords:
#         if (r + adj_r, c + adj_c) in rolls:
#              adjacent_roll_count += 1

#     if adjacent_roll_count < 4:
#         count += 1

# print(count)


#Part Two 
#Remove a roll if there is less then 4 rolls around it
#Check again and see if any more rolls can be removed
# Repeat until no more rolls can be removed 

count = 0
adjacent_coords = [(-1, 0), (0, -1), (-1, -1), (1, 0), (0, +1), (1, 1), (1, -1), (-1, 1)]

rolls = set()


with open('input.txt', 'r') as input:
    for r, line in enumerate(input):
            for c, ch in enumerate(line):
                if ch == '@':
                     rolls.add((r,c))

while True:
    rolls_removed_after_loop = set()

    for (r, c) in rolls:
        adjacent_roll_count = 0

        for adj_r, adj_c in adjacent_coords:
            if (r + adj_r, c + adj_c) in rolls:
                adjacent_roll_count += 1

        if adjacent_roll_count < 4:
            rolls_removed_after_loop.add((r,c))
    if not rolls_removed_after_loop:
         break
    
    count += len(rolls_removed_after_loop)
    rolls -= rolls_removed_after_loop

print(count)