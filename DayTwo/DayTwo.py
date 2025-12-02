#Part One
#Read in input with ID ranges separated by commas
    #ID range values separated by a dash (-)
#Invalid IDs are ID's with repeating number patterns
    #Becuase of this, the invalid ID's must be even
    #i.e. from their example: 123 is valid, but 123123 is invalid
        #Add an if-break statement when testing for odd length numbers
#Add invalid ID's to an array
#Sum all the ID's in the array together
#Final answer is the sum of all the invalid ID's


#Part Two
#An Id is now invalid if a sequence of numbers is repeated at least twice
    #This means invalid id's can now have odd lengths
    #It also means splitting the digit down the middle no longer works as a test


arr = []
invalid_id = []
sum = 0

with open('input.txt', 'r') as input:
    for line in input:
        arr = line.split(',')
    for item in arr:
        id_range = item.split('-')
        start = int(id_range[0])
        end = int(id_range[1])
    #testing ID validity section
        for id in range(start, end + 1):
            id_str = str(id)
            str_length = len(id_str)
            #For Part One
            #if len(id_str) % 2 != 0:
            #    continue
            #else:
            #    mid = len(id_str) // 2
            #    if id_str[:mid] == id_str[mid:]:
            #        invalid_id.append(id)
            for x in range(1, str_length // 2 + 1):
                if str_length % x == 0:
                    sequence = id_str[:x]
                    if sequence * (str_length//x) == id_str:
                        invalid_id.append(id)
                        break

for item in invalid_id:
    sum += item
print(sum)