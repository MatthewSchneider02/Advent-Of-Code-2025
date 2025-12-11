#Part One
#Input has coordinates for where the red tiles are
    #grid starts at (0,0)
    #position is given as x, y (new line)
#The largest rectangle will be the one with the largest difference
    #max((x2-x1) * (y2-y1))
#Could probably just brute force it, but it may come back to bite me in part two. Oh well
#Return the largest area of the largest rectangle you can make


# coords = []

# with open("input.txt", 'r') as input:
#     for line in input:
#         line = line.rstrip('\n')
#         x, y = line.split(",")
#         coords.append((int(x),int(y)))

# max_area = 0
# for i in range(len(coords)):
#     x1, y1 = coords[i]
#     for j in range(i+1, len(coords)):
#         x2, y2, = coords[j]
#         area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1) #Forgot to include the corner tile in calculation the first time so that's what the +1 is for
#         if area > max_area:
#             max_area = area

# print(max_area)




#Part Two
#Each red tile coordinate is connected to the next coordinate in the input by a (straight) line of green tiles
    #They alternate between vertical and horizontal.
        #i.e x1, y1 (first coord) connects to x1, y2 (second coord) vertically, then x1, y2 (second coord) connects to x2, y2 (third coord) horizontally. Then x2, y2, (third coord) connects to x3, y2 (fourth coord) to complete the rectangle.
            #Repeat until end of input. Every four lines is a new rectangle.
#Basically, rectangles have four red tile corners and green tile perimeters
    #Also the area of the rectangle will have green tiles covering inside the rectangle

#So, we're going to want to read the four red corners, and connect them together with green tiles
    #Then fill all the inside tiles as green            NOTE: This takes wayyy too long so have to figure out a different method
        #Might be better to track the empty tiles outside the rectangle instead? Not sure yet
#Then we can do something similar to part one, but we need to check whether every tile inside the two red corners is allowed (is green or red)
    #Then as we do that find the pair with the max area



#######################################################################################################################################################################

#NOTE: Every solution (if they were actually solutions) I came up with would take entirely too long to run, so this answer comes almost entirely from mgtezak on reddit/github. (https://github.com/mgtezak/Advent_of_Code/blob/master/2025/09/p2.py)

#######################################################################################################################################################################

#Use this for future reference and study. Comments are from me to better understand the code
with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def part2(puzzle_input):
    #Gets the red tile coordinates
    corners = [tuple(map(int, line.split(','))) for line in puzzle_input.splitlines()]
    n = len(corners)

    #Function for getting the rectangle area
    def get_size(x1, y1, x2, y2):
        x = abs(x1 - x2) + 1
        y = abs(y1 - y2) + 1
        return x * y

    #Gets and sorts the rectangle edges and sizes
    edges = []
    sizes = []
    for i in range(n):
        edges.append(sorted((corners[i], corners[i-1])))
        for j in range(i+1, n):
            c1, c2 = sorted((corners[i], corners[j]))
            sizes.append((get_size(*c1, *c2), c1, c2))

    edges.sort(reverse=True, key=lambda e: get_size(*e[0], *e[1]))
    sizes.sort(reverse=True)

    #Checks the rectangles, starting with the largest 
    #Looks to see if an edge lies entirely inside the rectangles, and if any edge is inside, the rectangle is not allowed
    for size, (x1, y1), (x2, y2) in sizes:
        y1, y2 = sorted((y1, y2))
        if not any(
            (x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2)
            for (x3, y3), (x4, y4) in edges
        ):
            return size

result = part2(puzzle_input)
print(result)

#So it looks like this looks only at the largest rectangles, which saves a good amount of time, rather than going one by one.
    #This means it can stop as soon as it finds a valid rectangle, because it must be the largest
#It also only checks the edge tiles, not every tile inside the rectangles (which most of my ideas were doing)