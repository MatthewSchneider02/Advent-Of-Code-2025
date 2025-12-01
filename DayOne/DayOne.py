count = 0
lock = 50
arr = [] 

with open('input.txt', 'r') as input:
    for line in input.readlines():
            if line[0] == 'L':
                for _ in range(int(line[1:])):
                    lock -= 1
                    lock = lock % 100
                    if lock == 0:
                        count += 1
            if line[0] == 'R':
                for _ in range(int(line[1:])):
                    lock += 1
                    lock = lock % 100
                    if lock == 0:
                        count += 1
print(count)

#Part One:
#Open and read in input
#Track lock position
    #Lock starts at 50
#If there is R, do one thing: increase lock position
    #If there is L, do another: decrease lock position
#If lock goes over 99, then go to 0
    #If lock goes under 0, go to 99
    #If lock lands on 0, increase count


#Part Two:
#If the lock passes 0 at all, increase count