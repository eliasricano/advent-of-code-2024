def read_sort_file(filename):
    list1 = []
    list2 = []

    with open(filename) as file:
        for line in file:
            columns = line.strip().split('   ')
            list1.append(int(columns[0]))
            list2.append(int(columns[1]))
        list1.sort()
        list2.sort()
    return list1, list2

input = 'input.txt'
left_list, right_list = read_sort_file(input)

similarity_score = 0
for i in left_list:
    times_appeared = 0
    for j in right_list:
        if i == j:
            times_appeared += 1
    similarity_score += i * times_appeared

print(similarity_score)