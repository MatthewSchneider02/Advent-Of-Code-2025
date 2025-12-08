#Part One
# You are given many ranges of numnbers, inclusive (separated by a dash)
    #each range is separated by a new line
#A blank line separates the ranges and the ingredient id numbers
#Then you are given single numbers, separated by a new line
#Determine how many of the single numbers are can be found in the ranges given
    #The numbers count if they can be found in any of the ranges, the order of the numbers or ranges doesn't matter to whether it is fresh or not

# fresh_ranges = []
# ingredient_id = []
# parsing_ranges = True
# num_fresh = 0

# with open('input.txt', 'r') as input:
#     for line in input:
#         line = line.strip()

#         if line == "":
#             parsing_ranges = False
#             continue

#         if parsing_ranges:
#             x, y = line.split("-")
#             fresh_ranges.append((int(x), int(y)))
#         else:
#             ingredient_id.append(int(line))

# for x in ingredient_id:
#     for y, z in fresh_ranges:
#         if y <= x <= z:
#             num_fresh += 1
#             break
# print(num_fresh)


#Part Two
#Find the number of total id numbers that consider an ingredient fresh
    #i.e. if there are three ranges, 3-5, 10-14, 16-20, 12-18, then there are 14 fresh id numbers (3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    #the provided ingredient ids are useless now (i think?), only the ranges matter
    #I'm confused how to handle the overlapping ranges, I'll have to think on that for a minute
        #First step is sorting the ranges given by highest to lowest
        #Then add the first range to a new array (listed so that it will include all numbers in the range)
        #(Because we sorted it) Next we can check to see if the next range starts a) before or b) after the first range
            #a) we can replace the end of the first range to the end of the second range, then add that list to the new array
            #b) we can just list and add the numbers in the range to the new array
    #Then we can return the length of the new array of ranges
        #NOT LENGTH, we would need a for loop to loop through the new array and get the total number of ids that way.

fresh_ranges = []
total_id_num = 0

with open('input.txt', 'r') as input:
    for line in input:
        line = line.strip()
        if line == "":
            break

        x, y = line.split("-")
        fresh_ranges.append((int(x), int(y)))

merged_fresh_ranges = []
fresh_ranges.sort()

for x in fresh_ranges:
    if merged_fresh_ranges == []:
        merged_fresh_ranges.append(list(x))
    else:
        last_range = merged_fresh_ranges[-1]
        if x[0] <= last_range[1]:
            last_range[1] = max(last_range[1], x[1])
        else:
            merged_fresh_ranges.append(list(x))

for a, b in merged_fresh_ranges:
    total_id_num += (b - a + 1)

print(total_id_num)