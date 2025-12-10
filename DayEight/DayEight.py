#Part One
#Connect the 1000 closest pairs of junction boxes
#Return the product of the sizes of the three largest ciruits
#DSU algorithm

junction_boxes = []

with open('input.txt', 'r') as input:
    for line in input:
        x, y, z = map(int, line.split(","))
        junction_boxes.append((x, y, z))

number_connections = 1000
number_boxes = len(junction_boxes)

parent = list(range(number_boxes))
component_size = [1] * number_boxes

def find_representative(box_index):
    while parent[box_index] != box_index:
        parent[box_index] = parent[parent[box_index]]
        box_index = parent[box_index]
    return box_index

distance_list = []

for i in range(number_boxes):
    x1, y1, z1 = junction_boxes[i]
    for j in range(i + 1, number_boxes):
        x2, y2, z2 = junction_boxes[j]

        squared_distance = (
            (x1 - x2) * (x1 - x2)
            + (y1 -y2) * (y1 - y2)
            + (z1 - z2) * (z1 - z2)
        )
        
        distance_list.append((squared_distance, i, j))

distance_list.sort(key=lambda entry: entry[0])

for connection_index in range(number_connections):
    _, box_a, box_b = distance_list[connection_index]

    rep_a = find_representative(box_a)
    rep_b = find_representative(box_b)

    if rep_a != rep_b:
        if component_size[rep_a] < component_size[rep_b]:
            rep_a, rep_b = rep_b, rep_a
        parent[rep_b] = rep_a
        component_size[rep_a] += component_size[rep_b]

circuit_sizes = {}

for index in range(number_boxes):
    representative = find_representative(index)
    if representative not in circuit_sizes:
        circuit_sizes[representative] = 0
    circuit_sizes[representative] += 1

sorted_sizes = sorted(circuit_sizes.values(), reverse=True)
result = sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2]

print(result)


#Part Two
#Connect all the junction boxes, until all are in a single circuit
#Return the product of the x coordinates of the last pair you connect

parent = list(range(number_boxes))
component_size = [1] * number_boxes
components_remaining = number_boxes
last_connection_boxes = None

for _, box_a, box_b in distance_list:
    rep_a = find_representative(box_a)
    rep_b = find_representative(box_b)

    if rep_a != rep_b:
        # union by size
        if component_size[rep_a] < component_size[rep_b]:
            rep_a, rep_b = rep_b, rep_a
        parent[rep_b] = rep_a
        component_size[rep_a] += component_size[rep_b]

        components_remaining -= 1

        if components_remaining == 1:
            last_connection_boxes = (box_a, box_b)
            break

x1 = junction_boxes[last_connection_boxes[0]][0]
x2 = junction_boxes[last_connection_boxes[1]][0]
part_two_result = x1 * x2

print(part_two_result)